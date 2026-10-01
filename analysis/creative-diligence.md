# Creative diligence — SPOT short, 30-hour version

Everything here is free, public, and runnable in the window alongside the Tegus reading track in `30-hour-sprint.md`. Scripts live in `tools/`; outputs in `data/`. Each item states what it produces and what result would refute us.

## Point 1 — Price hikes: cadence, elasticity, who keeps the increase

| # | Method | Produces | Refutes us if | Time |
|---|---|---|---|---|
| 1.1 | **Wayback price calendar** (`tools/wayback_price_calendar.py`) across 12+ markets, monthly snapshots since 2023 | Exact hike date per market; a lapping schedule weighted by the Q2-26 subscriber mix (Europe 36 / NA 25 / LatAm 24 / RoW 15); the "ARPU tailwind decay" chart by quarter | Snapshots show an Aug–Sep 2026 international round (moves Q4-26 lapping out a year) | 10 min unattended |
| 1.2 | **Competitor parity series** via Wayback for youtube.com/premium, apple.com/apple-music, music.amazon.com | Spotify's US premium/discount to each peer by month since 2023, overlaid on the NA subscriber back-solve | NA adds held up during the Feb–Jul 2026 $2-premium window | 20 min |
| 1.3 | **Google Play review mining** (`tools/play_store_reviews.py`, US/GB/DE) | Weekly share of reviews citing price, cancelling or switching, around each of the three US hikes | Feb-26 spike no larger than Jun-24 | 15 min |
| 1.4 | **Reddit cancel/switch counts** (`tools/reddit_cancel_mentions.py`) | Weekly post counts for "cancel spotify", "switch youtube music", "switch apple music" since 2023 | Same | 10 min unattended |
| 1.5 | **Google Trends** (manual export): "cancel spotify" ÷ "spotify premium", US; "youtube music" vs "spotify premium" | Churn-intent ratio per hike; the only free series that goes back through all three hikes | Ratio spike in 2026 below 2024 | 5 min |
| 1.6 | **Deferred revenue check** from the 6-K balance sheets | Deferred revenue growth vs Premium revenue growth; annual-plan lock-in after a hike shows as deferred revenue outrunning Premium revenue, its absence suggests fewer subscribers locking in | Deferred revenue growth ≥ Premium revenue growth in H1-26 | 10 min |
| 1.7 | **EDGAR full-text search** (efts.sec.gov): "wholesale" near "streaming" in WMG 10-K and UMG annual report; "Streaming 2.0" | Mechanics of the escalators the labels take from each hike | Filings describe escalators as volume-based, not price-based | 15 min |

## Point 2 — Add-ons: Music Pro, AI covers, superfan

| # | Method | Produces | Refutes us if | Time |
|---|---|---|---|---|
| 2.1 | **iOS App Store listing, "In-App Purchases" section** (US and India), plus Wayback history of the listing | The complete list of SKUs Spotify currently sells; a "Pro" or "Music Pro" SKU appearing is the earliest public signal of launch | A Pro SKU is already listed | 5 min |
| 2.2 | **Trademark search** (USPTO TSDR, EUIPO, WIPO): "Music Pro", "Supremium", "Spotify Pro", "Spotify Platinum" | Filing dates and status; shows how long the tier has been planned and whether filings lapsed | Fresh filings in 2026 with live status | 10 min |
| 2.3 | **Spotify careers page** (lifeatspotify.com), now vs the Jan-2026 Wayback snapshot: roles mentioning superfan, premium tiers, lossless, ticketing, remix | Staffing signal for the tier | Role count rising sharply | 15 min |
| 2.4 | **Audiobooks+ price history** via Wayback (the one add-on Spotify actually sells) | Price points by market; any cuts are evidence of weak attach | Prices rising | 10 min |
| 2.5 | **Live Nation Q2 transcript** (Tegus/IR) for "Reserved" uptake; **UMG Q2 transcript** for "artists to opt in" | Whether the superfan features Spotify already shipped are getting traction | Live Nation cites meaningful Reserved volumes | 15 min |
| 2.6 | **EDGAR full-text**: "superfan" in UMG, WMG, SPOT filings | How the labels describe the tier and its economics | Labels describe a near-term DSP launch | 10 min |

## Point 3 — Emerging markets: conversion, price architecture, friction

| # | Method | Produces | Refutes us if | Time |
|---|---|---|---|---|
| 3.1 | **Google Play review mining** (India, Indonesia, Brazil, Mexico) | Weekly share of reviews complaining about ads and ad load; dates the friction change and sizes the reaction; price-mention share after the May-26 India cut | No rise in ad complaints after Q2-26 | 20 min |
| 3.2 | **Top-grossing rank history** (AppBrain / Similarweb free app rankings) India and Indonesia, Music & Audio category: Spotify vs YouTube Music vs JioSaavn | Whether the 30% Standard cut lifted billings rank | Spotify's grossing rank improved materially after May | 15 min |
| 3.3 | **Minimum Android version** support page via Wayback, plus StatCounter Android-version share for India/Indonesia | The date old devices were cut and the share of installed base affected, i.e. the MAU at risk from "deprecation" | Affected share under 2% | 15 min |
| 3.4 | **Telco bundle inventory** (Airtel, Jio, Telkomsel, Claro, Telcel pages, with Wayback) | Which markets bundle Spotify, at what effective price; a rising bundle share explains the persistent ARPU mix drag | Bundles shrinking | 20 min |
| 3.5 | **Regional back-solve** from the decks, Q1-24 to Q2-26 | MAU and subs by region; conversion by region; the NA q/q series | RoW conversion rising through 2026 | 30 min |
| 3.6 | **Google Trends by country**: "Spotify Premium", "Spotify Lite", "YouTube Music" in India and Indonesia, 2025–26 | Demand response to the Lite launch and its removal | Premium interest up after the cut | 5 min |

## Point 4 — Discovery Mode ceiling

| # | Method | Produces | Refutes us if | Time |
|---|---|---|---|---|
| 4.1 | **Daily Mix / Radio label audit** (`tools/daily_mix_label_audit.py`) on 5–10 accounts | The label-group composition of the DM contexts (major vs distributor/indie catalog). If majors participate, this no longer bounds DM; it shows who bears the haircut and whether recommendation slots skew to major frontline releases, which is what major enrollment looks like from the outside. If majors do not participate, the non-major share is a hard ceiling on DM's reach in those surfaces | Non-major share tiny and majors confirmed out (DM has little room either way) | 2 min per account |
| 4.2 | **Loud & Clear 2026** site: counts of artists above listener and earnings thresholds, 2021–2025 | Growth of the DM-eligible pool (≥25k monthly listeners, ≥3 eligible songs); a flattening pool means enrollment TAM is flattening | Eligible pool still growing double digits | 10 min |
| 4.3 | **Spotify for Artists DM page** via Wayback | Any change to eligibility thresholds, contexts, or the 30% haircut; a lowered threshold is Spotify reaching for enrollment, which is what a nearing ceiling looks like | A new context added | 10 min |
| 4.4 | **Distributor help centers and blogs** (TuneCore, DistroKid, CD Baby, Symphonic Aug-2026 post) via Wayback | Stated uplift claims over time (TuneCore once cited 1.5x for sub-1M-listener artists); default-enrollment policies | Uplift claims rising | 20 min |
| 4.5 | **EDGAR full-text**: "Discovery Mode" and "marketplace" across SPOT 20-Fs 2023–25 and WMG/UMG filings | Year-over-year drift in Spotify's own marketplace language and any label risk-factor mention | Language strengthening | 15 min |
| 4.6 | **Texas AG and Travis County court search** for Spotify CID enforcement; Capolongo arbitration docket | Whether the regulatory ceiling is moving toward enforcement | CID closed with no action | 10 min |
| 4.7 | **Marquee / Showcase pages** via Wayback | Market expansions and minimum budgets; whether the paid side of marketplace is still growing | Rapid expansion into new markets in 2026 | 10 min |
| 4.8 | **Spotify for Artists dashboards from artist or manager contacts** (any artist with ≥25k monthly listeners sees a Discovery Mode tab: streams in DM contexts, uplift, enrolled tracks). Also **crowdsourced DM stats**: search Reddit r/musicmarketing, r/WeAreTheMusicMakers, r/spotify for posted "Discovery Mode results" screenshots 2022–26 | First-hand per-track uplift now vs 2023–24 and the share of an artist's streams coming through DM contexts; a crowdsourced uplift distribution over time. This is the only free primary data on the economic ceiling | Uplift stable or rising; DM-context share of streams still growing | 30 min plus outreach |
| 4.9 | **Major-label catalog in DM, observed**: on a few test accounts, seed Radio from a major-label frontline artist and log how often the next 50 tracks are same-label frontline releases vs catalog vs indie, repeated across labels | A weak but observable signal of whether major catalog is being promoted in DM contexts; use only alongside a transcript that states participation | Pattern indistinguishable across labels | 30 min |

## Point 5 — AI opex

| # | Method | Produces | Refutes us if | Time |
|---|---|---|---|---|
| 5.1 | **Meta Ad Library + Google Ads Transparency Center** (manual): advertiser "Spotify", by country | Count of active creatives and their start dates since Jan-26, by market; promo offers ("3 months for $0") by market. Direct observation of marketing intensity and promo reliance, monthly | Active creative count falling into Q4 | 30 min |
| 5.2 | **iSpot.tv** Spotify TV ad page (free) | Estimated US TV spend and airings by month | Spend stepping down after Q3 | 5 min |
| 5.3 | **Careers page** now vs Jan-26 Wayback: roles citing inference, GPU, LLM, ML platform, trust & safety, content integrity | Mix shift in a flat headcount toward costlier AI and integrity roles | Role mix unchanged | 15 min |
| 5.4 | **20-F contractual obligations** (BamSEC): Google Cloud minimum commitment by year, FY-23 vs FY-24 vs FY-25 | The hardest evidence available on whether compute is temporary | Commitment flat | 10 min |
| 5.5 | **Spotify Engineering and R&D blogs, Google Cloud Next 2026 talks** | Disclosed scale (events/day, inference volumes, cost per task from the Xirp post) | Posts describe falling inference cost per user | 15 min |
| 5.6 | **Deezer H1-26 report; Spotify safety updates** | AI share of daily uploads; spam/AI tracks removed | Upload share flat | 10 min |
| 5.7 | **Opex by line** (6-Ks), ex social charges and FX; Q4 S&M as % of revenue 2023–25 | The seasonality consensus needs opex to fall into | Q4 S&M historically flat to Q3 | 30 min |

## Cross-cutting

| # | Method | Produces | Time |
|---|---|---|---|
| X.1 | **Guidance track record** table, 12 quarters: guide vs actual for MAU, subs, revenue, GM, OI from the decks | Where beats come from (OI beats via social charges and GM timing) and where misses started (MAU, Q2-26). Rebuts "management is conservative" | 30 min |
| X.2 | **Transcript phrase tracker** (`tools/transcript_phrase_tracker.py`) on the last 8 calls pasted from Tegus | What management started saying ("monetization lever", "friction", "temporary") and stopped saying ("superfan", "1 billion") | 15 min incl. pasting |
| X.3 | **Form 144 and 6-K insider filings** (EDGAR): Ek, Lorentzon, UMG | Supply calendar through the hold period | 10 min |
| X.4 | **Reverse DCF** at $487 | What 2030 revenue and margin the price already requires; shows the stock needs the Investor Day targets hit exactly | 20 min |
| X.5 | **Estimate dispersion** (Canalyst / Visible Alpha / Bloomberg): which analysts have not updated since 21 May | The cuts that move consensus | 20 min |
| X.6 | **Options and borrow** (broker): implied move into 22 Oct, skew, borrow rate, utilization | Entry sizing | 5 min |

## Running it inside the 30 hours

- **Hours 0–3, data desk.** Install, kick off 1.1, 1.3/3.1, 1.4 (unattended). Do 2.1, 2.2, 5.1, 5.2, 4.3, 3.3, X.6 by hand. Set up 4.1 and run it on your own account; recruit 4–8 friends' accounts for the evening.
- **Hours 3–16, Tegus reading** (see sprint file). Scripts finish in the background; check `data/` at hour 8.
- **Hours 16–22, filings and analysis.** 5.4, 5.7, 3.5, 1.6, X.1, X.3, X.4, X.5. Chart 1.1 and 4.1.
- **Hours 22–27, grade and rewrite.** Every point gets a grade and the one chart that carries it: the ARPU tailwind decay (1.1), the label composition of DM contexts (4.1) and the crowdsourced uplift series (4.8), the review ad-complaint spike (3.1), the Meta Ad Library creative count by month (5.1).
- **Hours 27–30, Q&A.**

The four charts above are the "what did you find that the Street does not have" answer.
