#!/usr/bin/env python3
"""
Classify a Spotify album's `label` + `copyrights` text into a parent-label group.

Groups (column `group`):
  UMG, SONY, WMG          -> major-owned frontline imprint (per the (P) line / label field)
  DIST_UMG/DIST_SONY/DIST_WMG -> content that reaches Spotify via a major-owned distributor
                             (Virgin Music / Ingrooves / Caroline, The Orchard / AWAL, ADA)
                             or that is "under exclusive license to" a major. These are NOT on
                             Spotify's public Discovery Mode licensor list, so keep them separate.
  INDIE                   -> known independent label / independent distributor (Merlin-type,
                             Believe, EMPIRE, Concord, BMG, Beggars, Secretly, ...)
  DIY                     -> self-released via a DIY distributor that supports Discovery Mode
                             (DistroKid, TuneCore, CD Baby, UnitedMasters, Amuse, ...), or the
                             label field is just the artist's own name. DIY is the POSITIVE CONTROL.
  UNVERIFIED              -> nothing matched. Treated as non-major in the analysis but listed for
                             manual review (see `--review` in enrich_labels.py).

Matching uses the (P) copyright line first (most reliable for parent identification), then the
`label` field, then the (C) line. Overrides win over everything (label_overrides.csv).

Usage as a library:  from label_map import classify
Usage as a CLI:      python3 label_map.py "Republic Records" "(P) 2024 UMG Recordings, Inc."
"""
from __future__ import annotations
import csv
import os
import re
import sys
from dataclasses import dataclass

# ---------------------------------------------------------------------------
# Pattern tables. Each entry: (regex, group, note). Case-insensitive unless the
# regex is wrapped in (?-i:...) for tokens like EMI/ADA/UMG/MCA that collide with words.
# Order within a table matters only for the `note`; group precedence is handled below.
# ---------------------------------------------------------------------------

MAJOR_FRONTLINE = [
    # ---- Universal Music Group ----
    (r"(?-i:\bUMG\b)", "UMG", "UMG Recordings"),
    (r"universal music", "UMG", "Universal Music"),
    (r"\bcapitol\b", "UMG", "Capitol"),
    (r"interscope", "UMG", "Interscope"),
    (r"republic records", "UMG", "Republic"),
    (r"def jam", "UMG", "Def Jam"),
    (r"island (records|def jam)", "UMG", "Island"),
    (r"\bmotown\b", "UMG", "Motown"),
    (r"\bpolydor\b", "UMG", "Polydor"),
    (r"(?-i:\bEMI\b)", "UMG", "EMI"),
    (r"\bgeffen\b", "UMG", "Geffen"),
    (r"verve (records|label|music)", "UMG", "Verve"),
    (r"\bdecca\b", "UMG", "Decca"),
    (r"blue note", "UMG", "Blue Note"),
    (r"deutsche grammophon", "UMG", "DG"),
    (r"astralwerks", "UMG", "Astralwerks"),
    (r"mercury (records|studios|nashville|kx)", "UMG", "Mercury"),
    (r"virgin records", "UMG", "Virgin Records"),
    (r"(?-i:\bMCA\b)", "UMG", "MCA"),
    (r"aftermath", "UMG", "Aftermath"),
    (r"cash money", "UMG", "Cash Money"),
    (r"young money", "UMG", "Young Money"),
    (r"quality control", "UMG", "Quality Control"),
    (r"spinefarm", "UMG", "Spinefarm"),
    (r"lost highway", "UMG", "Lost Highway"),
    (r"capitol christian|sparrow records", "UMG", "Capitol CMG"),
    (r"fontana", "UMG", "Fontana"),
    (r"universal[- ]island", "UMG", "Universal-Island"),
    (r"\bumle\b|universal m[uú]sica", "UMG", "UMLE"),
    # ---- Sony Music ----
    (r"sony music", "SONY", "Sony Music"),
    (r"sony classical|masterworks", "SONY", "Sony Classical"),
    (r"\bcolumbia\b", "SONY", "Columbia"),
    (r"(?-i:\bRCA\b)", "SONY", "RCA"),
    (r"epic records", "SONY", "Epic"),
    (r"\barista\b", "SONY", "Arista"),
    (r"legacy recordings", "SONY", "Legacy"),
    (r"ultra records|ultra music", "SONY", "Ultra"),
    (r"\bjive\b|zomba|laface", "SONY", "Zomba/Jive/LaFace"),
    (r"provident|essential records", "SONY", "Provident"),
    (r"alamo records", "SONY", "Alamo"),
    (r"disruptor records", "SONY", "Disruptor"),
    (r"ministry of sound|relentless records|black butter|syco", "SONY", "Sony UK"),
    (r"century media", "SONY", "Century Media"),
    (r"som livre", "SONY", "Som Livre"),
    (r"monkey puzzle", "SONY", "Monkey Puzzle"),
    # ---- Warner Music Group ----
    (r"warner (records|music|bros\.? records|classics|chappell)", "WMG", "Warner"),
    (r"\batlantic\b", "WMG", "Atlantic"),
    (r"\belektra\b", "WMG", "Elektra"),
    (r"parlophone", "WMG", "Parlophone"),
    (r"\breprise\b", "WMG", "Reprise"),
    (r"nonesuch", "WMG", "Nonesuch"),
    (r"fueled by ramen", "WMG", "FBR"),
    (r"roadrunner", "WMG", "Roadrunner"),
    (r"\brhino\b", "WMG", "Rhino"),
    (r"asylum records", "WMG", "Asylum"),
    (r"big beat records", "WMG", "Big Beat"),
    (r"300 entertainment", "WMG", "300"),
    (r"10k projects", "WMG", "10K"),
    (r"spinnin", "WMG", "Spinnin'"),
    (r"\bsire\b", "WMG", "Sire"),
    (r"\berato\b", "WMG", "Erato"),
    (r"artist partner group|\bAPG\b", "WMG", "APG"),
    (r"east west records|\bffrr\b", "WMG", "Warner UK"),
    (r"canvasback", "WMG", "Canvasback"),
]

# Major-owned distribution / artist-services arms. Not on the public Discovery Mode licensor list.
MAJOR_DISTRIBUTOR = [
    (r"virgin music", "DIST_UMG", "Virgin Music Group"),
    (r"ingrooves", "DIST_UMG", "Ingrooves"),
    (r"caroline (records|international|distribution)", "DIST_UMG", "Caroline"),
    (r"big machine", "DIST_UMG", "Big Machine (HYBE-owned, UMG-distributed)"),
    (r"hollywood records|walt disney records|disney music", "DIST_UMG", "Disney Music Group (UMG-distributed)"),
    (r"the orchard", "DIST_SONY", "The Orchard"),
    (r"(?-i:\bAWAL\b)", "DIST_SONY", "AWAL"),
    (r"alternative distribution alliance|(?-i:\bADA\b)", "DIST_WMG", "ADA"),
    (r"level music", "DIST_WMG", "Level"),
]

# "distributed" phrasing in the (P)/(C) line. If the parent named after the phrase is a major,
# the track is major-distributed indie/artist-owned content.
LICENSE_PHRASE = re.compile(
    r"(under (exclusive )?licen[cs]e to|distributed by|marketed (and|&) distributed by|"
    r"manufactured (and|&) (marketed|distributed) by|exclusively licensed to|"
    r"licensed exclusively to|in association with|dist\.? by)",
    # NB: "a division of <major>" means the imprint IS the major (frontline), so it is not here.
    re.IGNORECASE,
)

# DIY distributors that appear on Spotify's public Discovery Mode licensor list (or are widely
# documented as supporting it). A label field made of these = self-released, DM-eligible.
DIY_DISTRIBUTOR = [
    (r"distrokid|\d{4,} records dk\b", "DIY", "DistroKid"),
    (r"tunecore", "DIY", "TuneCore"),
    (r"cd ?baby", "DIY", "CD Baby"),
    (r"unitedmasters|united masters", "DIY", "UnitedMasters"),
    (r"\bamuse\b", "DIY", "Amuse"),
    (r"ditto music|\bditto\b", "DIY", "Ditto"),
    (r"symphonic", "DIY", "Symphonic"),
    (r"repost network|repost by soundcloud", "DIY", "Repost"),
    (r"soundrop", "DIY", "Soundrop"),
    (r"\blandr\b", "DIY", "LANDR"),
    (r"routenote", "DIY", "RouteNote"),
    (r"\bstem\b disintermedia|stem disintermedia", "DIY", "Stem"),
    (r"emubands|horus music|recordjet|feiyr|rebeat|venice music|\bvydia\b|onerpm|one ?rpm", "DIY", "other DM-listed distributor"),
]

KNOWN_INDIE = [
    (r"\bbelieve\b (digital|music)?", "INDIE", "Believe"),
    (r"\bempire\b", "INDIE", "EMPIRE"),
    (r"\bconcord\b|fantasy records|rounder|fearless records|loma vista|craft recordings", "INDIE", "Concord"),
    (r"\bbmg\b", "INDIE", "BMG"),
    (r"\bkobalt\b", "INDIE", "Kobalt"),
    (r"\bxl recordings\b|\b4ad\b|matador|rough trade|young recordings|beggars", "INDIE", "Beggars"),
    (r"\bdomino\b", "INDIE", "Domino"),
    (r"sub pop", "INDIE", "Sub Pop"),
    (r"secretly|dead oceans|jagjaguwar", "INDIE", "Secretly Group"),
    (r"ninja tune", "INDIE", "Ninja Tune"),
    (r"\bwarp\b", "INDIE", "Warp"),
    (r"epitaph|anti- records|\banti\b records", "INDIE", "Epitaph"),
    (r"mom ?\+ ?pop", "INDIE", "Mom+Pop"),
    (r"glassnote", "INDIE", "Glassnote"),
    (r"partisan", "INDIE", "Partisan"),
    (r"\bmute\b", "INDIE", "Mute"),
    (r"\bpias\b", "INDIE", "PIAS"),
    (r"cooking vinyl", "INDIE", "Cooking Vinyl"),
    (r"\barmada\b", "INDIE", "Armada"),
    (r"monstercat", "INDIE", "Monstercat"),
    (r"\bncs\b|nocopyrightsounds", "INDIE", "NCS"),
    (r"hopeless records|rise records", "INDIE", "Hopeless/Rise"),
    (r"nuclear blast|napalm records|metal blade|century media", "INDIE", "metal indies"),
    (r"\bmerlin\b", "INDIE", "Merlin"),
    (r"\bkartel\b|\bawal\b", "INDIE", "artist services"),
    (r"\bmad decent\b|\bowsla\b|\bdim mak\b|\bmonstercat\b", "INDIE", "dance indies"),
    (r"top dawg|\btde\b", "INDIE", "TDE (Interscope-distributed; (P) line usually catches)"),
    (r"\bovo sound\b", "INDIE", "OVO"),
    (r"\bghostly\b|\bstones throw\b|\brhymesayers\b|\bbrainfeeder\b", "INDIE", "indie hip-hop/electronic"),
    (r"\blofi girl\b|\bchillhop\b", "INDIE", "lofi labels"),
]

GROUP_ORDER = ["UMG", "SONY", "WMG", "DIST_UMG", "DIST_SONY", "DIST_WMG", "INDIE", "DIY", "UNVERIFIED"]
MAJORS = {"UMG", "SONY", "WMG"}
NON_MAJOR = {"INDIE", "DIY", "UNVERIFIED"}


def _compile(table):
    return [(re.compile(rx, re.IGNORECASE), g, n) for rx, g, n in table]


_MAJOR = _compile(MAJOR_FRONTLINE)
_DIST = _compile(MAJOR_DISTRIBUTOR)
_DIY = _compile(DIY_DISTRIBUTOR)
_INDIE = _compile(KNOWN_INDIE)


@dataclass
class Classification:
    group: str
    note: str
    matched_on: str        # "override" | "P" | "label" | "C" | "artist" | "none"
    licensed_to_major: bool  # (P)/(C) line says the content is licensed/distributed to a major


def _first_match(table, text):
    for rx, g, n in table:
        if rx.search(text):
            return g, n
    return None


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "")).strip().lower()


def load_overrides(path: str | None):
    """label_overrides.csv columns: match_type,key,group,note  (match_type in album_id|label|artist)."""
    overrides = {"album_id": {}, "label": {}, "artist": {}}
    if not path or not os.path.exists(path):
        return overrides
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            mt = row["match_type"].strip()
            if mt not in overrides:
                raise ValueError(f"bad match_type {mt!r} in {path}")
            overrides[mt][_norm(row["key"])] = (row["group"].strip(), row.get("note", "").strip())
    return overrides


def classify(label: str, copyrights: list[dict] | None, artists: list[str] | None,
             album_id: str | None = None, overrides=None) -> Classification:
    """
    label      : album.label from the Web API
    copyrights : album.copyrights, list of {"text": ..., "type": "P"|"C"}
    artists    : list of artist display names on the track (for the DIY = artist-name heuristic)
    """
    overrides = overrides or {"album_id": {}, "label": {}, "artist": {}}
    artists = artists or []
    copyrights = copyrights or []
    p_lines = " | ".join(c.get("text", "") for c in copyrights if c.get("type") == "P")
    c_lines = " | ".join(c.get("text", "") for c in copyrights if c.get("type") == "C")
    label = label or ""

    # 0. overrides
    if album_id and _norm(album_id) in overrides["album_id"]:
        g, n = overrides["album_id"][_norm(album_id)]
        return Classification(g, n, "override", False)
    if _norm(label) in overrides["label"]:
        g, n = overrides["label"][_norm(label)]
        return Classification(g, n, "override", False)
    for a in artists:
        if _norm(a) in overrides["artist"]:
            g, n = overrides["artist"][_norm(a)]
            return Classification(g, n, "override", False)

    licensed = bool(LICENSE_PHRASE.search(p_lines) or LICENSE_PHRASE.search(c_lines))

    # 1. (P) line: who owns the master. A major named here after a license phrase means
    #    major-distributed; a major named with no license phrase means frontline.
    for source_name, text in (("P", p_lines), ("label", label), ("C", c_lines)):
        if not text:
            continue
        dist = _first_match(_DIST, text)
        if dist:
            return Classification(dist[0], dist[1], source_name, licensed)
        major = _first_match(_MAJOR, text)
        if major:
            if licensed and source_name != "label":
                # e.g. "(P) 2023 Top Dawg Entertainment, under exclusive license to Interscope Records"
                return Classification("DIST_" + major[0], f"licensed to {major[1]}", source_name, True)
            return Classification(major[0], major[1], source_name, licensed)

    # 2. DIY distributors / artist-name label
    for source_name, text in (("label", label), ("P", p_lines), ("C", c_lines)):
        diy = _first_match(_DIY, text)
        if diy:
            return Classification("DIY", diy[1], source_name, licensed)
    if label and any(_norm(label) == _norm(a) for a in artists):
        return Classification("DIY", "label == artist name (verify: some major artists own their (P))", "artist", licensed)

    # 3. known indies
    for source_name, text in (("label", label), ("P", p_lines), ("C", c_lines)):
        ind = _first_match(_INDIE, text)
        if ind:
            return Classification("INDIE", ind[1], source_name, licensed)

    return Classification("UNVERIFIED", "", "none", licensed)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    lab = sys.argv[1]
    cps = [{"text": t, "type": "P" if t.strip().lower().startswith(("(p)", "℗", "p ")) else "C"} for t in sys.argv[2:]]
    print(classify(lab, cps, []))
