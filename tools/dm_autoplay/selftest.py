#!/usr/bin/env python3
"""
Offline self-test: (1) classifier spot checks on realistic label / (P)-line strings,
(2) synthetic sessions through enrich_labels (offline, with a fake album cache) and analyze.
Run: python3 selftest.py
"""
import json
import os
import random
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from label_map import classify  # noqa: E402

CASES = [
    # label, P line, artists, expected group
    ("Republic Records", "(P) 2024 UMG Recordings, Inc.", ["Drake"], "UMG"),
    ("Interscope", "℗ 2023 Interscope Records", ["Billie Eilish"], "UMG"),
    ("Columbia", "(P) 2024 Sony Music Entertainment", ["Beyoncé"], "SONY"),
    ("RCA Records Label", "(P) 2023 RCA Records, a division of Sony Music Entertainment", ["SZA"], "SONY"),
    ("Atlantic Records", "(P) 2024 Atlantic Recording Corporation", ["Charli xcx"], "WMG"),
    ("Warner Records", "(P) 2022 Warner Records Inc.", ["Dua Lipa"], "WMG"),
    ("Top Dawg Entertainment", "(P) 2017 Top Dawg Entertainment, under exclusive license to Interscope Records", ["Kendrick Lamar"], "DIST_UMG"),
    ("Taylor Swift", "(P) 2022 Taylor Swift", ["Taylor Swift"], "DIY"),  # known trap -> override file
    ("Big Machine Records, LLC", "(P) 2014 Big Machine Label Group, LLC", ["Taylor Swift"], "DIST_UMG"),
    ("AWAL Recordings Ltd", "(P) 2023 AWAL Recordings Ltd", ["Laufey"], "DIST_SONY"),
    ("Some Indie Label", "(P) 2023 Some Indie Label, distributed by The Orchard", ["X"], "DIST_SONY"),
    ("XL Recordings", "(P) 2021 XL Recordings Ltd", ["Adele"], "INDIE"),
    ("Domino Recording Co", "(P) 2023 Domino Recording Co Ltd", ["Arctic Monkeys"], "INDIE"),
    ("Concord Records", "(P) 2024 Concord Records, Inc.", ["Y"], "INDIE"),
    ("1234567 Records DK", "(P) 2024 1234567 Records DK", ["Bedroom Artist"], "DIY"),
    ("Bedroom Artist", "(P) 2024 Bedroom Artist", ["Bedroom Artist"], "DIY"),
    ("DistroKid", "(P) 2024 Someone", ["Someone"], "DIY"),
    ("Mystery Imprint", "(P) 2020 Mystery Imprint", ["Z"], "UNVERIFIED"),
    ("EMI", "(P) 2019 EMI Records Ltd", ["Q"], "UMG"),
    ("Emily's Songs", "(P) 2019 Emily's Songs", ["Emily"], "UNVERIFIED"),  # EMI token must not fire on 'Emily'
    ("Elektra (NEK)", "(P) 2023 Elektra Entertainment Group", ["W"], "WMG"),
    ("Spinnin' Records", "(P) 2023 Spinnin' Records B.V.", ["V"], "WMG"),
]


def test_classifier():
    bad = 0
    for label, p, artists, want in CASES:
        got = classify(label, [{"text": p, "type": "P"}], artists)
        flag = "ok " if got.group == want else "BAD"
        if got.group != want:
            bad += 1
        print(f"  {flag} {label!r:32} -> {got.group:10} ({got.note}) via {got.matched_on}   expected {want}")
    print(f"classifier: {len(CASES) - bad}/{len(CASES)} passed")
    return bad == 0


def synth(tmp):
    """Simulate: WMG participates in DM (over-represented in autoplay), UMG/SONY do not, DIY lifted."""
    rng = random.Random(7)
    groups = ["UMG", "SONY", "WMG", "DIST_SONY", "INDIE", "DIY", "UNVERIFIED"]
    control_p = [0.30, 0.20, 0.15, 0.05, 0.15, 0.10, 0.05]
    treat_p = [0.27, 0.18, 0.19, 0.05, 0.14, 0.13, 0.04]
    fake_labels = {"UMG": ("Republic Records", "(P) 2024 UMG Recordings, Inc."), "SONY": ("Columbia", "(P) 2024 Sony Music Entertainment"),
                   "WMG": ("Atlantic Records", "(P) 2024 Atlantic Recording Corporation"), "DIST_SONY": ("Indie Co", "(P) 2024 Indie Co, distributed by The Orchard"),
                   "INDIE": ("XL Recordings", "(P) 2024 XL Recordings Ltd"), "DIY": ("5551212 Records DK", "(P) 2024 5551212 Records DK"),
                   "UNVERIFIED": ("Mystery Imprint", "(P) 2024 Mystery Imprint")}
    plays, cache = [], {}
    tid = 0

    def emit(surface, session, k, probs):
        nonlocal tid
        g = rng.choices(groups, probs)[0]
        tid += 1
        aid = f"alb{tid}"
        cache[aid] = {"label": fake_labels[g][0], "copyrights": [{"text": fake_labels[g][1], "type": "P"}], "artists": [f"artist{tid % 400}"]}
        plays.append({"row_type": "play", "session_id": session, "account": "acct1", "surface": surface, "position": k,
                      "track_id": f"t{tid}", "artists": [f"artist{tid % 400}"], "album_id": aid, "popularity": rng.randint(5, 95)})

    for s in range(150):  # autoplay sessions, with within-session correlation: tilt probs per session
        tilt = [p * rng.uniform(0.6, 1.4) for p in treat_p]
        for k in range(1, 21):
            emit("autoplay", f"acct1-ap{s}", k, tilt)
    for s in range(24):  # 6 accounts x 4 weeks of DW+RR
        for k in range(1, 61):
            emit("discover_weekly", f"acct{s % 6}-dw{s // 6}", k, control_p)
    with open(os.path.join(tmp, "raw.jsonl"), "w") as f:
        for r in plays:
            f.write(json.dumps(r) + "\n")
    with open(os.path.join(tmp, "albums_cache.json"), "w") as f:
        json.dump(cache, f)


def test_pipeline():
    here = os.path.dirname(os.path.abspath(__file__))
    with tempfile.TemporaryDirectory() as tmp:
        synth(tmp)
        r = subprocess.run([sys.executable, os.path.join(here, "enrich_labels.py"), "--offline",
                            "--inputs", os.path.join(tmp, "raw.jsonl"), "--out", os.path.join(tmp, "enriched.jsonl"),
                            "--albums-cache", os.path.join(tmp, "albums_cache.json"),
                            "--overrides", os.path.join(tmp, "none.csv"), "--review", os.path.join(tmp, "review.csv")],
                           capture_output=True, text=True)
        print(r.stdout, r.stderr)
        assert r.returncode == 0, "enrich failed"
        r = subprocess.run([sys.executable, os.path.join(here, "analyze.py"), "--inputs", os.path.join(tmp, "enriched.jsonl"),
                            "--treatment", "autoplay", "--control", "discover_weekly",
                            "--baseline", "UMG=0.37,SONY=0.26,WMG=0.16,MAJOR_FRONTLINE=0.71", "--reps", "1000"],
                           capture_output=True, text=True)
        print(r.stdout, r.stderr)
        assert r.returncode == 0, "analyze failed"
        assert "WMG relatively over-represented" in r.stdout, "expected to detect the simulated WMG lift"
        assert "DM lift visible" in r.stdout, "expected the DIY positive control to fire"
    print("pipeline: ok")


if __name__ == "__main__":
    ok = test_classifier()
    test_pipeline()
    sys.exit(0 if ok else 1)
