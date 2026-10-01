#!/usr/bin/env python3
"""Label-group composition of Discovery Mode contexts.

Measures what share of the tracks in the DM contexts you can observe (Daily
Mixes, artist Radio, Discover Weekly) sit in major-label vs distributor/indie
catalog. Interpretation depends on whether the majors participate in DM:
  - if they do not, the non-major share is a hard ceiling on DM's reach;
  - if they do (the working assumption from expert calls), the split shows who
    bears the haircut and whether slots skew to major frontline releases.
Run it on several accounts (friends, with permission) to get a range
(thesis point 4).

Setup (one time):
  1. Create an app at developer.spotify.com; set redirect URI http://127.0.0.1:8080/callback
  2. export SPOTIPY_CLIENT_ID=... SPOTIPY_CLIENT_SECRET=... SPOTIPY_REDIRECT_URI=http://127.0.0.1:8080/callback
  3. In the Spotify app: Daily Mix 1-6 / an artist Radio / Discover Weekly -> Share -> Copy link

Usage:
  python3 tools/daily_mix_label_audit.py --playlists <url1> <url2> ... --out data/dm_ceiling.csv
"""
import argparse, csv, re
from collections import Counter
import spotipy
from spotipy.oauth2 import SpotifyOAuth

MAJOR = [
    # Universal
    "universal", "umg", "capitol", "interscope", "republic", "def jam", "island", "polydor", "virgin", "motown",
    "geffen", "emi", "decca", "deutsche grammophon", "verve", "blue note", "mercury", "big machine", "umle", "umgb",
    # Sony
    "sony", "columbia", "rca", "epic", "arista", "legacy", "ultra", "the orchard", "alamo", "sony music latin",
    # Warner
    "warner", "atlantic", "elektra", "parlophone", "nonesuch", "reprise", "rhino", "asylum", "300 entertainment",
    "big beat", "fueled by ramen", "roadrunner", "warner records", "wm ", "ada",
]


def is_major(label):
    l = (label or "").lower()
    return any(m in l for m in MAJOR)


def pid(u):
    m = re.search(r"playlist[/:]([A-Za-z0-9]+)", u)
    return m.group(1) if m else u


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--playlists", nargs="+", required=True)
    ap.add_argument("--out", default="data/dm_ceiling.csv")
    a = ap.parse_args()
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-read-private playlist-read-collaborative"))

    rows = []
    for u in a.playlists:
        p = pid(u)
        meta = sp.playlist(p, fields="name")
        album_ids, tracks = [], 0
        results = sp.playlist_items(p, fields="items(track(album(id))),next", additional_types=["track"])
        while results:
            for it in results["items"]:
                t = it.get("track") or {}
                if t.get("album", {}).get("id"):
                    album_ids.append(t["album"]["id"])
                    tracks += 1
            results = sp.next(results) if results.get("next") else None
        labels = []
        for i in range(0, len(album_ids), 20):
            for alb in sp.albums(album_ids[i:i + 20])["albums"]:
                labels.append(alb.get("label", ""))
        maj = sum(is_major(l) for l in labels)
        top = Counter(labels).most_common(8)
        rows.append([meta["name"], tracks, maj, tracks - maj, round((tracks - maj) / max(tracks, 1), 3), "; ".join(f"{l} ({n})" for l, n in top)])
        print(f"{meta['name']}: {tracks} tracks, non-major (DM-addressable) share {rows[-1][4]:.0%}")

    with open(a.out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["playlist", "tracks", "major", "non_major", "dm_addressable_share", "top_labels"])
        w.writerows(rows)
    print(f"wrote {a.out}")


if __name__ == "__main__":
    main()
