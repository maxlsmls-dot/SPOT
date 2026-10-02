# dm_autoplay — Discovery Mode label-participation experiment

Scripts for the method described in `analysis/dm-label-participation-method.md`. Python 3.10+, only
`requests` beyond the standard library. Nothing here is tested against the live API yet; the
classifier and the analysis were tested on synthetic data (`python3 selftest.py`).

## Files

| file | what it does |
|---|---|
| `spotify_auth.py` | tiny Web API client (client-credentials or authorization-code with refresh) |
| `collect_autoplay.py` | plays one seed track with no context, lets Autoplay take over, logs every served track |
| `dump_playlist.py` | dumps a playlist (Discover Weekly / Release Radar copy) in the same row format = control arm |
| `enrich_labels.py` | album -> `label` + (P)/(C) lines via `GET /albums`, classifies into parent-label group, writes a review queue |
| `label_map.py` | the imprint -> parent regex table and `classify()`; edit this and `label_overrides.csv` as the review queue dictates |
| `analyze.py` | shares per surface, session-bootstrap CIs, three-major differential test, DIY positive control, baseline check, power helper |
| `seeds.example.csv` | seed design template (copy to `seeds.csv`, fill with real track URIs) |
| `label_overrides.example.csv` | override template (copy to `label_overrides.csv`) |
| `selftest.py` | offline tests |

## Setup (once)

1. Create an app at developer.spotify.com/dashboard; add redirect URI `http://127.0.0.1:8888/callback`.
2. `export SPOTIFY_CLIENT_ID=... SPOTIFY_CLIENT_SECRET=...`
3. On the experiment account: Premium, Settings -> Autoplay ON, Private Session OFF, no "Liked Songs"
   history. Open the desktop app or web player on the machine that will run the collector.
4. `python3 collect_autoplay.py --list-devices` (first run opens the OAuth URL; paste the redirect back).

## Run

```bash
# treatment arm: seeded Autoplay sessions, 20 served tracks each, played in full
python3 collect_autoplay.py --seeds seeds.csv --account acct1 --device-name "MY-PC" \
    --tracks-per-session 20 --shuffle-seeds --skip-done --out data/autoplay_acct1.jsonl

# control arm (weekly): copy Discover Weekly and Release Radar into playlists you own, then
python3 dump_playlist.py --playlist-id <copy id> --surface discover_weekly --account acct1 --out data/control_acct1.jsonl
python3 dump_playlist.py --playlist-id <copy id> --surface release_radar  --account acct1 --out data/control_acct1.jsonl

# labels + classification (client-credentials auth is enough)
python3 enrich_labels.py --inputs "data/autoplay_*.jsonl" "data/control_*.jsonl" \
    --out data/enriched.jsonl --overrides label_overrides.csv --review data/review.csv
#   -> open data/review.csv, add overrides for the high-count UNVERIFIED / artist-name rows, re-run

# readout
python3 analyze.py --inputs data/enriched.jsonl --treatment autoplay \
    --control discover_weekly,release_radar --baseline UMG=0.37,SONY=0.26,WMG=0.16 \
    --out ../../analysis/dm-autoplay-results.md
```

## Sample-size helper

`python3 analyze.py --power 0.20 0.23` prints the n per arm needed to see a 3-point move in one
major's share (about 2,900 major-label tracks per arm before the clustering design effect).
