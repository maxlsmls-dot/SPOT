#!/usr/bin/env python3
"""
Run seeded Autoplay sessions on the experiment account and log every track Autoplay serves.

How a session works
  1. Start ONE seed track on the chosen device (PUT /me/player/play with a single track URI, so
     there is no album/playlist context left to continue into).
  2. When the seed ends, Spotify's Autoplay takes over. Every track that plays after the seed, that
     this script did not start, is by construction an Autoplay-served track.
  3. Poll GET /me/player/currently-playing every --poll seconds; each change of track id is one
     served track (position 1..K). Also snapshot GET /me/player/queue once Autoplay begins, so you
     can test whether the queue already exposes the upcoming Autoplay batch (if it does, later runs
     can shorten --dwell).
  4. After K served tracks, pause and move to the next seed.

Requirements
  - Premium account (playback control endpoints need Premium), Autoplay ON in the account settings.
  - An active device: the official desktop app or web player logged into the experiment account, or
    a Spotify Connect device. Use --list-devices to find it.
  - Env vars from spotify_auth.py.

Output: JSON lines. row_type "play" rows carry the served tracks (position 0 = seed, exclude it in
analysis); "queue" rows carry the queue snapshot; "event" rows carry errors/timeouts.

Example
  python3 collect_autoplay.py --seeds seeds.csv --account acct1 --device-name "DESKTOP-ABC" \
      --tracks-per-session 20 --out data/autoplay_acct1.jsonl
"""
from __future__ import annotations
import argparse
import csv
import datetime as dt
import json
import os
import random
import sys
import time

from spotify_auth import Client


def now():
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def track_row(item, st):
    return {
        "track_id": item["id"],
        "track_uri": item.get("uri"),
        "track_name": item.get("name"),
        "artists": [a["name"] for a in item.get("artists", [])],
        "artist_ids": [a["id"] for a in item.get("artists", [])],
        "album_id": item.get("album", {}).get("id"),
        "album_name": item.get("album", {}).get("name"),
        "album_type": item.get("album", {}).get("album_type"),
        "release_date": item.get("album", {}).get("release_date"),
        "duration_ms": item.get("duration_ms"),
        "popularity": item.get("popularity"),
        "explicit": item.get("explicit"),
        "context": st.get("context"),
        "progress_ms_first_seen": st.get("progress_ms"),
        "is_playing": st.get("is_playing"),
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--seeds", help="CSV with columns seed_uri,seed_group,genre,pop_tier,note")
    ap.add_argument("--account", default="acct1", help="label for this Spotify account (cluster id)")
    ap.add_argument("--surface", default="autoplay")
    ap.add_argument("--out", default="data/autoplay.jsonl")
    ap.add_argument("--device-id")
    ap.add_argument("--device-name")
    ap.add_argument("--list-devices", action="store_true")
    ap.add_argument("--tracks-per-session", type=int, default=20)
    ap.add_argument("--poll", type=float, default=10.0, help="seconds between currently-playing polls")
    ap.add_argument("--dwell", type=float, default=0.0,
                    help="seconds to let each served track play before skipping; 0 = play in full (recommended)")
    ap.add_argument("--shuffle-seeds", action="store_true", help="randomise seed order (do this; log keeps the order)")
    ap.add_argument("--max-sessions", type=int, default=0)
    ap.add_argument("--skip-done", action="store_true", help="skip seeds already present in --out for this account")
    ap.add_argument("--seed-timeout", type=float, default=120.0, help="extra seconds past seed duration to wait for Autoplay")
    args = ap.parse_args()

    sp = Client(user=True)

    if args.list_devices:
        for d in (sp.get("/me/player/devices") or {}).get("devices", []):
            print(f"{d['id']}  {d['name']!r}  type={d['type']} active={d['is_active']}")
        return
    if not args.seeds:
        sys.exit("--seeds is required (or --list-devices)")

    device_id = args.device_id
    if not device_id:
        devs = (sp.get("/me/player/devices") or {}).get("devices", [])
        if args.device_name:
            devs = [d for d in devs if d["name"] == args.device_name]
        if not devs:
            sys.exit("No matching device. Open the Spotify app on the experiment account, then --list-devices.")
        device_id = devs[0]["id"]
        print(f"[device] {devs[0]['name']} ({device_id})")

    with open(args.seeds, newline="", encoding="utf-8") as f:
        seeds = [r for r in csv.DictReader(f) if r.get("seed_uri")]
    if args.shuffle_seeds:
        random.shuffle(seeds)

    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    done = set()
    if args.skip_done and os.path.exists(args.out):
        with open(args.out, encoding="utf-8") as f:
            for line in f:
                try:
                    r = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if r.get("row_type") == "play" and r.get("position") == 0 and r.get("account") == args.account:
                    done.add(r.get("seed_uri"))

    out = open(args.out, "a", encoding="utf-8")

    def emit(row):
        out.write(json.dumps(row, ensure_ascii=False) + "\n")
        out.flush()

    n_sessions = 0
    for seed in seeds:
        if args.max_sessions and n_sessions >= args.max_sessions:
            break
        if seed["seed_uri"] in done:
            continue
        seed_id = seed["seed_uri"].split(":")[-1]
        session_id = f"{args.account}-{dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%S')}-{seed_id[:8]}"
        base = {"session_id": session_id, "account": args.account, "surface": args.surface,
                "seed_uri": seed["seed_uri"], "seed_group": seed.get("seed_group"),
                "seed_genre": seed.get("genre"), "seed_pop_tier": seed.get("pop_tier")}
        print(f"\n[session {n_sessions + 1}] {session_id} seed={seed['seed_uri']} ({seed.get('note', '')})")

        # 1. start the seed with no context
        try:
            sp.put("/me/player/play", params={"device_id": device_id}, json_body={"uris": [seed["seed_uri"]]})
        except RuntimeError as e:
            emit({**base, "row_type": "event", "ts": now(), "event": "play_failed", "detail": str(e)})
            print("  play failed:", e)
            continue

        # confirm the seed is playing
        seed_item, st = None, None
        t0 = time.time()
        while time.time() - t0 < 60:
            time.sleep(3)
            st = sp.get("/me/player/currently-playing") or {}
            item = st.get("item")
            if item and item.get("id") == seed_id:
                seed_item = item
                break
        if not seed_item:
            emit({**base, "row_type": "event", "ts": now(), "event": "seed_not_confirmed"})
            print("  seed never showed up as currently playing; skipping")
            continue
        emit({**base, "row_type": "play", "ts": now(), "position": 0, **track_row(seed_item, st)})
        seed_duration_s = (seed_item.get("duration_ms") or 240000) / 1000.0

        # 2. wait for the seed to end and Autoplay to begin, then log K served tracks
        prev_id = seed_id
        k = 0
        last_change = time.time()
        idle_polls = 0
        deadline_first = time.time() + seed_duration_s + args.seed_timeout
        while k < args.tracks_per_session:
            time.sleep(args.poll)
            st = sp.get("/me/player/currently-playing") or {}
            item = st.get("item")
            if not item or item.get("type") != "track":
                idle_polls += 1
                if k == 0 and time.time() > deadline_first:
                    emit({**base, "row_type": "event", "ts": now(), "event": "autoplay_never_started"})
                    print("  Autoplay never started (is Autoplay enabled? is the device still active?)")
                    break
                if k > 0 and idle_polls * args.poll > 180:
                    emit({**base, "row_type": "event", "ts": now(), "event": "playback_stopped", "after_tracks": k})
                    print("  playback stopped mid-session")
                    break
                continue
            idle_polls = 0
            if item["id"] != prev_id:
                k += 1
                prev_id = item["id"]
                last_change = time.time()
                row = {**base, "row_type": "play", "ts": now(), "position": k, **track_row(item, st)}
                emit(row)
                print(f"  {k:>2}. {item['name']} — {', '.join(a['name'] for a in item['artists'])}  pop={item.get('popularity')}")
                if k == 1:
                    try:
                        q = sp.get("/me/player/queue") or {}
                        emit({**base, "row_type": "queue", "ts": now(),
                              "queue_track_ids": [t.get("id") for t in q.get("queue", []) if t.get("type") == "track"],
                              "queue_names": [f"{t.get('name')} — {', '.join(a['name'] for a in t.get('artists', []))}"
                                              for t in q.get("queue", []) if t.get("type") == "track"]})
                    except RuntimeError as e:
                        emit({**base, "row_type": "event", "ts": now(), "event": "queue_failed", "detail": str(e)})
            elif args.dwell > 0 and (st.get("progress_ms") or 0) >= args.dwell * 1000 and k > 0:
                sp.post("/me/player/next", params={"device_id": device_id})
            elif k == 0 and time.time() > deadline_first:
                emit({**base, "row_type": "event", "ts": now(), "event": "autoplay_never_started"})
                print("  seed finished but nothing new played; skipping")
                break
            elif k > 0 and time.time() - last_change > 20 * 60:
                emit({**base, "row_type": "event", "ts": now(), "event": "stuck", "after_tracks": k})
                print("  no track change for 20 min; moving on")
                break

        try:
            sp.put("/me/player/pause", params={"device_id": device_id})
        except RuntimeError:
            pass
        n_sessions += 1
        time.sleep(5)

    out.close()
    print(f"\ndone: {n_sessions} sessions -> {args.out}")


if __name__ == "__main__":
    main()
