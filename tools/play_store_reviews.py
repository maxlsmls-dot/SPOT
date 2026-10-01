#!/usr/bin/env python3
"""Google Play review mining for Spotify, by country.

Produces weekly counts of reviews that mention (a) price / cancelling /
switching to YouTube or Apple (churn intent, thesis point 1) and (b) ads /
ad load (free-tier friction timing, thesis point 3), plus the 1-star share.

Usage:
  python3 tools/play_store_reviews.py --countries us gb in id br --count 4000 --out data/reviews.csv

Overlay the weekly series on the hike dates (US: 2023-07, 2024-06, 2026-02;
many intl markets: 2025-09) and on the EM friction change (2026 Q2/Q3).
"""
import argparse, csv, datetime as dt
from collections import defaultdict
from google_play_scraper import Sort, reviews

APP = "com.spotify.music"
LANG = {"us": "en", "gb": "en", "ca": "en", "au": "en", "in": "en", "id": "id", "br": "pt", "mx": "es",
        "de": "de", "fr": "fr", "es": "es", "it": "it", "nl": "nl", "se": "sv", "ph": "en", "ng": "en"}

CHURN = ["price", "expensive", "cost", "cancel", "cancelled", "canceled", "unsubscribe", "switch", "youtube music",
         "apple music", "amazon music", "too much", "raise", "increase", "hike", "preço", "caro", "cancelar",
         "precio", "mahal", "harga", "berlangganan", "teuer", "preis", "kündigen", "prix", "cher"]
ADS = ["ads", "advert", "too many ads", "ad every", "commercial", "iklan", "anúncio", "anuncio", "werbung", "pub ",
       "publicité", "publicidad"]
AI = ["ai dj", " dj ", "ai playlist", "ai generated", "ai music", "slop"]


def hit(text, words):
    t = f" {text.lower()} "
    return any(w in t for w in words)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--countries", nargs="+", default=["us", "in", "id", "br"])
    ap.add_argument("--count", type=int, default=3000)
    ap.add_argument("--out", default="data/reviews.csv")
    a = ap.parse_args()

    agg = defaultdict(lambda: defaultdict(int))  # (country, week) -> counters
    for cc in a.countries:
        got, token = 0, None
        while got < a.count:
            batch, token = reviews(APP, lang=LANG.get(cc, "en"), country=cc, sort=Sort.NEWEST,
                                   count=min(200, a.count - got), continuation_token=token)
            if not batch:
                break
            for r in batch:
                d = r["at"]
                week = (d - dt.timedelta(days=d.weekday())).date().isoformat()
                k = (cc, week)
                agg[k]["total"] += 1
                agg[k]["one_star"] += int(r["score"] == 1)
                txt = r["content"] or ""
                agg[k]["churn_price"] += int(hit(txt, CHURN))
                agg[k]["ads"] += int(hit(txt, ADS))
                agg[k]["ai"] += int(hit(txt, AI))
            got += len(batch)
            if token is None:
                break
        print(f"[{cc}] {got} reviews, oldest week {min(w for c, w in agg if c == cc) if any(c == cc for c, _ in agg) else 'n/a'}")

    with open(a.out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["country", "week", "total", "one_star", "churn_price", "ads", "ai", "one_star_share", "churn_share", "ads_share"])
        for (cc, week), c in sorted(agg.items()):
            t = c["total"] or 1
            w.writerow([cc, week, c["total"], c["one_star"], c["churn_price"], c["ads"], c["ai"],
                        round(c["one_star"] / t, 3), round(c["churn_price"] / t, 3), round(c["ads"] / t, 3)])
    print(f"wrote {a.out}")


if __name__ == "__main__":
    main()
