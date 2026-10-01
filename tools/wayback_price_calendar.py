#!/usr/bin/env python3
"""Spotify Premium price calendar by market, from Wayback Machine snapshots.

Builds the exact hike dates per market so the ARPU lapping schedule can be
weighted by subscriber mix (thesis point 1).

Usage:
  python3 tools/wayback_price_calendar.py --countries us gb de fr es it nl se br mx in id \
      --from 2023-01 --to 2026-10 --out data/price_calendar.csv

Then: open the CSV, sort by country/date, and mark every month where
`individual_price_guess` changes. That is the hike calendar.
"""
import argparse, csv, re, sys, time
import requests

CDX = "https://web.archive.org/cdx/search/cdx"
UA = {"User-Agent": "spot-diligence/1.0 (research; contact via github)"}
PRICE = re.compile(
    r"(?:US\$|\$|€|£|₹|R\$|MX\$|Rp|kr|zł|A\$|C\$|CHF|¥)\s?\d{1,3}(?:[.,]\d{2,3})?",
    re.I,
)


def snapshots(url, frm, to):
    params = {
        "url": url,
        "output": "json",
        "from": frm.replace("-", ""),
        "to": to.replace("-", ""),
        "filter": "statuscode:200",
        "collapse": "timestamp:6",  # one per month
        "fl": "timestamp,original",
    }
    r = requests.get(CDX, params=params, headers=UA, timeout=60)
    r.raise_for_status()
    rows = r.json()
    return rows[1:] if rows else []


def fetch(ts, original):
    r = requests.get(f"https://web.archive.org/web/{ts}id_/{original}", headers=UA, timeout=60)
    r.raise_for_status()
    return r.text


def individual_guess(html):
    """Price nearest to the word 'Individual' (falls back to most common price token)."""
    best = None
    for m in re.finditer(r"Individual", html):
        window = html[m.start(): m.start() + 600]
        p = PRICE.search(window)
        if p:
            best = p.group(0).replace(" ", "")
            break
    if best:
        return best
    toks = [t.replace(" ", "") for t in PRICE.findall(html)]
    if not toks:
        return ""
    return max(set(toks), key=toks.count)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--countries", nargs="+", default=["us", "gb", "de", "fr", "br", "mx", "in", "id"])
    ap.add_argument("--from", dest="frm", default="2023-01")
    ap.add_argument("--to", default="2026-12")
    ap.add_argument("--out", default="data/price_calendar.csv")
    a = ap.parse_args()

    with open(a.out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["country", "snapshot", "individual_price_guess", "all_prices_seen"])
        for cc in a.countries:
            url = f"spotify.com/{cc}/premium/"
            try:
                snaps = snapshots(url, a.frm, a.to)
            except Exception as e:
                print(f"[{cc}] CDX failed: {e}", file=sys.stderr)
                continue
            print(f"[{cc}] {len(snaps)} monthly snapshots")
            for ts, original in snaps:
                try:
                    html = fetch(ts, original)
                except Exception as e:
                    print(f"[{cc}] {ts} fetch failed: {e}", file=sys.stderr)
                    continue
                toks = sorted(set(t.replace(" ", "") for t in PRICE.findall(html)))
                w.writerow([cc, f"{ts[:4]}-{ts[4:6]}-{ts[6:8]}", individual_guess(html), " | ".join(toks[:12])])
                f.flush()
                time.sleep(1.0)
    print(f"wrote {a.out}")


if __name__ == "__main__":
    main()
