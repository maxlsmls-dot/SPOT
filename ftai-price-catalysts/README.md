# FTAI price-action catalyst map (May 2015 IPO → Sep 2026)

Images in `images/`:

| File | What it shows |
|---|---|
| `00_overview.png` | Full history (log scale), 5 eras, all 41 numbered catalysts with a key |
| `01_…` – `05_…` | One page per era: zoomed chart + a card per catalyst (what happened / why the stock moved) |
| `06_playbook.png` | Aerospace Products EBITDA & margin by quarter, earnings scorecard, five recurring patterns |

Rebuild: `python3 src/render.py && NODE_PATH=$(npm root -g) node src/shoot.cjs`

**Data caveat:** no price feed was reachable when this was built, so the price line in
`src/prices.py` is rebuilt from sourced anchors plus month-end estimates (±10%).
Put a daily `Date,Close` CSV at `data/ftai_daily.csv` (e.g. a Yahoo export with
unadjusted closes) and rebuild — the charts will use it automatically. Catalysts are in `src/events.py`.
