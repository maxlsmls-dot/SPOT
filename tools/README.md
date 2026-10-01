# tools/ — data desk for the SPOT short

Five scripts that produce numbers the Street does not have, each mapped to a thesis point. All run locally; none need paid data. Install once:

```
pip install requests google-play-scraper spotipy
```

| Script | Thesis point | What it produces | Runtime |
|---|---|---|---|
| `wayback_price_calendar.py` | 1 Pricing | Premium price by market by month from Wayback snapshots → exact hike dates per market → lapping schedule weighted by subscriber mix | ~10 min unattended |
| `play_store_reviews.py` | 1 Pricing, 3 EM | Weekly counts of Google Play reviews mentioning price / cancel / switching, and ads / ad load, by country → churn-intent and friction-timing proxies | ~5 min per country |
| `reddit_cancel_mentions.py` | 1 Pricing | Weekly count of Reddit posts about cancelling or switching from Spotify, 2023 → now, overlaid on hike dates | ~10 min |
| `daily_mix_label_audit.py` | 4 DM ceiling | Share of tracks in your Daily Mixes / Radio that sit in DM-addressable (non-major) catalog → a structural ceiling on DM's share of recommendations | ~2 min per account |
| `transcript_phrase_tracker.py` | all | Counts of key phrases across the earnings-call series pasted into `transcripts/earnings/` → the narrative shift in management's own words | seconds |

Outputs land in `data/`. Each script prints a short summary and writes a CSV.
