#!/usr/bin/env python3
"""
Attach label / copyright / parent-group fields to every "play" row.

Pipeline: unique album ids -> GET /albums?ids= (20 per call, client-credentials auth is enough)
-> cache to albums_cache.json -> classify with label_map.classify -> write enriched JSONL
-> write a review CSV of the highest-frequency UNVERIFIED / "label == artist" cases so you can
   add rows to label_overrides.csv and re-run.

Example
  python3 enrich_labels.py --inputs data/autoplay_*.jsonl data/control_*.jsonl \
      --out data/enriched.jsonl --overrides label_overrides.csv --review data/review.csv
"""
from __future__ import annotations
import argparse
import collections
import csv
import glob
import json
import os

from label_map import classify, load_overrides


def read_rows(patterns):
    for pat in patterns:
        for path in sorted(glob.glob(pat)) or [pat]:
            with open(path, encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    r = json.loads(line)
                    if r.get("row_type") == "play" and r.get("track_id"):
                        yield r


def fetch_albums(ids, cache_path):
    cache = {}
    if os.path.exists(cache_path):
        with open(cache_path, encoding="utf-8") as f:
            cache = json.load(f)
    missing = [i for i in ids if i and i not in cache]
    if missing:
        from spotify_auth import Client
        sp = Client(user=False)
        for i in range(0, len(missing), 20):
            batch = missing[i:i + 20]
            res = sp.get("/albums", params={"ids": ",".join(batch)}) or {}
            for alb in res.get("albums", []):
                if not alb:
                    continue
                cache[alb["id"]] = {
                    "label": alb.get("label"), "copyrights": alb.get("copyrights", []),
                    "album_name": alb.get("name"), "album_type": alb.get("album_type"),
                    "release_date": alb.get("release_date"), "total_tracks": alb.get("total_tracks"),
                    "artists": [a["name"] for a in alb.get("artists", [])],
                }
            print(f"  albums fetched: {min(i + 20, len(missing))}/{len(missing)}")
        with open(cache_path, "w", encoding="utf-8") as f:
            json.dump(cache, f, ensure_ascii=False, indent=0)
    return cache


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--inputs", nargs="+", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--albums-cache", default="data/albums_cache.json")
    ap.add_argument("--overrides", default="label_overrides.csv")
    ap.add_argument("--review", default="data/review.csv")
    ap.add_argument("--offline", action="store_true", help="never call the API; rows with uncached albums get UNVERIFIED")
    args = ap.parse_args()

    rows = list(read_rows(args.inputs))
    album_ids = sorted({r["album_id"] for r in rows if r.get("album_id")})
    print(f"{len(rows)} play rows, {len(album_ids)} unique albums")
    if args.offline:
        cache = {}
        if os.path.exists(args.albums_cache):
            with open(args.albums_cache, encoding="utf-8") as f:
                cache = json.load(f)
    else:
        cache = fetch_albums(album_ids, args.albums_cache)
    overrides = load_overrides(args.overrides)

    review = collections.Counter()
    review_example = {}
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as out:
        for r in rows:
            alb = cache.get(r.get("album_id"), {})
            c = classify(alb.get("label"), alb.get("copyrights"), r.get("artists"), r.get("album_id"), overrides)
            r2 = {**r, "label": alb.get("label"),
                  "p_line": " | ".join(x.get("text", "") for x in alb.get("copyrights", []) if x.get("type") == "P"),
                  "c_line": " | ".join(x.get("text", "") for x in alb.get("copyrights", []) if x.get("type") == "C"),
                  "group": c.group, "group_note": c.note, "matched_on": c.matched_on,
                  "licensed_to_major": c.licensed_to_major}
            out.write(json.dumps(r2, ensure_ascii=False) + "\n")
            if c.group == "UNVERIFIED" or c.matched_on == "artist":
                key = (c.group, alb.get("label") or "", r["artists"][0] if r.get("artists") else "")
                review[key] += 1
                review_example.setdefault(key, (r2["p_line"], r.get("album_id"), r.get("track_name")))

    os.makedirs(os.path.dirname(os.path.abspath(args.review)), exist_ok=True)
    with open(args.review, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["served_count", "group", "label", "first_artist", "p_line", "example_album_id", "example_track"])
        for key, n in review.most_common():
            w.writerow([n, *key, *review_example[key]])
    groups = collections.Counter(json.loads(l)["group"] for l in open(args.out, encoding="utf-8"))
    print("group counts:", dict(groups))
    print(f"review queue: {len(review)} distinct (label, artist) pairs -> {args.review}")


if __name__ == "__main__":
    main()
