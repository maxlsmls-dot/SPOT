#!/usr/bin/env python3
"""Weekly count of Reddit posts about cancelling / switching from Spotify.

Uses the pullpush.io mirror of Reddit search (public, no key). Overlay on
hike dates to see whether the Feb-2026 hike produced a larger spike than
Jun-2024 or Jul-2023 (thesis point 1). If pullpush is down, run the same
queries manually in Reddit search and note weekly counts.

Usage:
  python3 tools/reddit_cancel_mentions.py --from 2023-01-01 --out data/reddit_cancel.csv
"""
import argparse, csv, datetime as dt, time
import requests

API = "https://api.pullpush.io/reddit/search/submission/"
QUERIES = {
    "cancel": "cancel spotify",
    "switch_youtube": "switch youtube music",
    "switch_apple": "switch apple music",
    "price": "spotify price increase",
}
SUBS = ["spotify", "truespotify", "music", "all"]


def count(q, sub, after, before):
    params = {"q": q, "after": int(after.timestamp()), "before": int(before.timestamp()), "size": 100}
    if sub != "all":
        params["subreddit"] = sub
    r = requests.get(API, params=params, timeout=60)
    r.raise_for_status()
    return len(r.json().get("data", []))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--from", dest="frm", default="2023-01-01")
    ap.add_argument("--out", default="data/reddit_cancel.csv")
    a = ap.parse_args()
    start = dt.datetime.fromisoformat(a.frm)
    end = dt.datetime.now()
    with open(a.out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["week", "subreddit", "query", "posts_capped_100"])
        wk = start
        while wk < end:
            nxt = wk + dt.timedelta(days=7)
            for sub in SUBS:
                for name, q in QUERIES.items():
                    try:
                        n = count(q, sub, wk, nxt)
                    except Exception as e:
                        n = -1
                    w.writerow([wk.date().isoformat(), sub, name, n])
                    time.sleep(0.4)
            f.flush()
            print(wk.date())
            wk = nxt
    print(f"wrote {a.out}")


if __name__ == "__main__":
    main()
