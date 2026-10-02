#!/usr/bin/env python3
"""
Dump a playlist's tracks in the same JSONL "play" row format as collect_autoplay.py, so a
NON-Discovery-Mode surface (Discover Weekly, Release Radar, an editorial playlist) can be used as
the control arm in analyze.py.

Note: apps created after 27 Nov 2024 cannot read Spotify-owned algorithmic/editorial playlists via
the API. Workaround: in the app, open Discover Weekly -> select all -> "Add to playlist" -> a
playlist you own (one per week), then dump THAT playlist id here.

Example
  python3 dump_playlist.py --playlist-id 37i9dQ... --surface discover_weekly --account acct1 \
      --week 2026-W41 --out data/control_acct1.jsonl
"""
from __future__ import annotations
import argparse
import datetime as dt
import json
import os

from spotify_auth import Client


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--playlist-id", required=True)
    ap.add_argument("--surface", required=True, help="e.g. discover_weekly, release_radar, editorial_<name>")
    ap.add_argument("--account", default="acct1")
    ap.add_argument("--week", default=dt.date.today().strftime("%G-W%V"))
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    sp = Client(user=True)
    pid = args.playlist_id.split(":")[-1].split("?")[0]
    session_id = f"{args.account}-{args.surface}-{args.week}"
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    n = 0
    with open(args.out, "a", encoding="utf-8") as out:
        url = f"/playlists/{pid}/tracks"
        params = {"limit": 100, "offset": 0}
        pos = 0
        while url:
            page = sp.get(url, params=params)
            for it in page.get("items", []):
                t = it.get("track") or {}
                if not t or t.get("type") != "track" or not t.get("id"):
                    continue
                pos += 1
                out.write(json.dumps({
                    "row_type": "play", "ts": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
                    "session_id": session_id, "account": args.account, "surface": args.surface,
                    "seed_uri": None, "seed_group": None, "position": pos,
                    "track_id": t["id"], "track_uri": t.get("uri"), "track_name": t.get("name"),
                    "artists": [a["name"] for a in t.get("artists", [])],
                    "artist_ids": [a["id"] for a in t.get("artists", [])],
                    "album_id": (t.get("album") or {}).get("id"), "album_name": (t.get("album") or {}).get("name"),
                    "album_type": (t.get("album") or {}).get("album_type"),
                    "release_date": (t.get("album") or {}).get("release_date"),
                    "duration_ms": t.get("duration_ms"), "popularity": t.get("popularity"),
                    "explicit": t.get("explicit"), "context": {"type": "playlist", "uri": f"spotify:playlist:{pid}"},
                }, ensure_ascii=False) + "\n")
                n += 1
            url = page.get("next")
            params = None
    print(f"wrote {n} tracks from playlist {pid} as surface={args.surface} session={session_id} -> {args.out}")


if __name__ == "__main__":
    main()
