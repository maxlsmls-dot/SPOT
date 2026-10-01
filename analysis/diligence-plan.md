# SPOT short — diligence plan

Companion to `short-pitch-SPOT.md`. One section per thesis point. Each item states the source, the exact thing to extract, and what result confirms or refutes the point. Items marked **[pre-Oct 22]** can be finished before the Q3 print on 22 Oct 2026 and should be.

---

## 1. Price hikes: cadence, elasticity, and who keeps the increase

**Alt data**
- **[pre-Oct 22] Antenna (US subscription panel).** Pull Spotify Premium monthly churn, gross adds and net adds Jan-2023 to latest. Overlay the three US hikes (Jul-23, Jun-24, Feb-26). Extract: churn in the 4 months after each hike vs the 4 months before; share of Spotify cancels that resurface as YouTube Music or Apple Music sign-ups. *Confirms:* post-Feb-26 churn spike larger than post-Jun-24, with switching to YouTube/Apple visible. *Refutes:* no measurable churn delta.
- **[pre-Oct 22] Credit-card panel (Second Measure / Consumer Edge / Earnest).** US Spotify billings per paying account and active-payer count, monthly. Extract: realized ARPU step in Feb/Mar-26 vs list price step, and payer-count trajectory Feb to Sep 2026. A realized step below the list step means promo mix or downgrades to Duo/Family/Student. *Confirms:* payer count flat to down in NA since Feb-26.
- **Price scrape.** Script spotify.com/premium across all ~180 markets weekly (price, plan set, currency). Spotify gives ~30 days notice to subscribers, so new-market hikes show on the web before the call. *Confirms:* no US/UK/EU individual-plan change through Q1-27. Also tracks whether Spotify ever moves to $13.99 while YouTube/Apple sit at $11.99.
- **Regional subscriber back-solve.** From each quarterly deck's regional mix percentages, back out NA and Europe subscriber counts (±1.5M rounding). Build the q/q series since 2023. *Confirms:* NA q/q decline in Q1-26 and sub-trend growth in Q2/Q3.

**Expert calls**
- Former Spotify Premium pricing / revenue-management lead (2022–2025). Ask: how hike timing is decided; internal churn threshold that blocks a hike; whether a price premium to Apple/YouTube is an explicit constraint; what share of a hike flows to labels under the 2025 deals; whether 2027 plan assumed a hike and when.
- Former major-label digital commercial exec (post-2025 deals). Ask: mechanics of the Streaming 2.0 wholesale escalators, is it a fixed per-sub minimum, a % of the increase, or an ARPU floor; what triggers a wholesale step-up; UMG's "3.5pts from wholesale price increases" as a read on Spotify's cost.

**Survey**
- 1,000 US Spotify Premium subscribers, conjoint on $12.99 vs $13.99 vs YouTube Music $11.99 / Apple Music $11.99 with feature bundles. Extract stated switching at a $2 premium. Benchmark against the same design at the $1 premium that existed in 2024. *Confirms:* switching intent at $2 materially above the $1 result.

**Model work**
- Quarterly ARPU bridge (price / mix / FX) from each deck; project the lapping schedule explicitly (Sep-25 intl laps Q4-26; Feb-26 US laps Q1-27). Confirm Visible Alpha quarterly ARPU consensus for Q4-26 to Q2-27; the delta table in the pitch assumes +4.5% cc in Q2-27.

---

## 2. Add-ons: Music Pro, AI covers, superfan

**Expert calls**
- Former Spotify product lead on the superfan / "Supremium" / Music Pro workstream (2023–2025). Ask: why the tier has slipped since the Feb-2025 reporting; which features were pulled into Premium (lossless, Reserved) and why; internal attach-rate assumptions; whether launch is gated on labels or on product.
- Former major-label or Merlin commercial exec. Ask: what wholesale rate the labels asked for on a superfan tier (as % of the add-on price); whether the AI covers add-on revenue share is a fixed split; whether UMG's own direct-to-fan superfan products compete with the DSP tier.
- Former Spotify audiobooks lead. Ask: attach rate on Audiobooks+ top-ups, the one add-on precedent Spotify actually sells; what the 15-hour allowance costs per subscriber; how Audible at $8.95 and Amazon's free bundle changed the pricing discussion.

**Precedent work**
- Table of paid hi-res / superfan tiers and what happened: Tidal HiFi Plus (folded), Amazon Music HD (made free 2021), Apple lossless (free 2021), Deezer HiFi (merged), Spotify lossless (free Sep-25), Netflix extra member (attach disclosed in 2023–24). Extract attach rates where disclosed. *Confirms:* no DSP add-on has sustained >3% attach at a $5+ price point.

**Monitoring**
- APK teardowns (9to5Google, Android Authority, Reddit r/truespotify) for "Music Pro" / "Pro" / remix-tool strings; Spotify's own newsroom; Live Nation commentary on Reserved uptake; UMG/WMG calls for "superfan tier" language. *Confirms:* no launch strings or label commentary pointing to a Q1-27 launch.

**Survey**
- Same US panel: willingness to pay $5.99 for (a) remix tool, (b) early tickets, (c) hi-res, (d) all three. Extract share at ≥$5.99.

---

## 3. Emerging markets: conversion, price architecture, funnel friction

**Alt data**
- **[pre-Oct 22] Sensor Tower / data.ai.** Monthly MAU and installs for Spotify in India, Indonesia, Brazil, Mexico, Nigeria, Pakistan, Jan-2025 to latest. Extract: MAU q/q in Q3-26 after the friction changes. App-store net revenue estimates for India and Indonesia before and after the May-26 price cut. *Confirms:* MAU down q/q in India/Indonesia in Q3 with no step-up in app-store billings after the cut.
- Regional back-solve (as in point 1) for RoW and LatAm MAU and subs; compute subs/MAU conversion by region each quarter since 2023. *Confirms:* RoW conversion flat or falling while MAU growth slows.
- Similarweb / Google Trends: spotify.com/premium traffic and "Spotify Premium" search by country.

**Expert calls**
- Former Spotify India or SEA country/growth lead (2023–2026). Ask: India subs/MAU conversion (order of magnitude); why Lite was scrapped at six months; Platinum uptake; the share of Indian "subs" that are telco or bundle-driven and at what ARPU; what "deprecating lower-end Android devices" removes from MAU; how ad load and free-tier limits were changed and the measured conversion lift.
- Former Spotify growth analytics lead. Ask: how "quality MAU" is defined internally; whether the Q3 MAU guide reflects a one-time reset or an ongoing throttle; expected MAU trajectory through 2027.

**Channel checks**
- Telco bundle inventory: Airtel, Jio, Telkomsel, Claro, Telcel bundles that include Spotify; list price and whether Spotify counts them as Premium subs. *Confirms:* a rising share of RoW/LatAm adds coming from sub-€2 bundles, i.e. the "product/market mix" ARPU drag persists.

---

## 4. Discovery Mode ceiling and the gross margin bridge

This is the leg that needs primary evidence. The repo's `topic-matrix.md` topics 2 and 3 are the framework; fill them.

**Expert calls (the core of the budget)**
- Distributor executives with DM dashboards: DistroKid, TuneCore, CD Baby, Believe/TuneCore, Symphonic, Amuse. Ask each: % of their eligible catalog enrolled today vs 2023 and 2024; whether enrollment growth has plateaued; per-track stream uplift in DM contexts now vs 2023; whether any clients have withdrawn; whether the 30% haircut has changed; which surfaces are eligible and whether any were added since 2024.
- Former Spotify marketplace PM or BD lead (2021–2025). Ask: the product rule or guardrail on the share of recommendations that can be DM-enrolled; which surfaces were considered and rejected; whether majors participate and on what terms; how the Texas CID and the arbitration have changed the roadmap; Marquee/Showcase demand trend from label marketing budgets.
- Former Spotify recommendations/ML engineer. Ask: the measured engagement cost of raising DM share; where the guardrail sits (skip rate, session length); whether it has been loosened.
- Major-label digital exec. Ask: does the major participate in DM; is DM participation or exclusion written into the 2025 deals; label view on Spotify extending DM to Smart Shuffle or DJ.

**Model work**
- Premium gross-margin bridge each quarter: Premium revenue growth vs Premium cost of revenue growth, with the deck's stated drivers (music costs net of marketplace, audiobooks, Partner Program). Estimate marketplace gross profit from the 2022 Investor Day base and the "quadrupled since 2021" statement; express as points of gross margin. Sensitivity: marketplace flat vs +15% in 2027.
- Track the "music royalty costs net of certain marketplace programs" language in each 6-K; a change in wording is a signal.

**Monitoring**
- Spotify for Artists help page listing DM-eligible contexts (Radio, Autoplay, Mixes): archive weekly, flag any addition.
- Texas AG docket (CIDs issued 22 Apr 2026), the Capolongo arbitration, any FTC endorsement-guide action, and congressional letters. A disclosure or opt-out requirement is a direct hit to the lever.
- Partner Program: payout disclosures (>$100M/quarter), eligibility changes, Nordic and other market expansions.

*Confirms:* enrollment share plateaued above ~50% of eligible catalog, per-track uplift decayed, no surface added since 2024, majors out, Premium GM expansion decelerating in Q3/Q4. *Refutes:* enrollment still rising, a new surface, or a major joining.

---

## 5. AI operating expense

**Filings (highest signal per hour)**
- **[pre-Oct 22] Google Cloud purchase commitments.** Spotify's 20-F discloses unconditional purchase obligations with Google Cloud by year. Compare the 2025 20-F to 2024 and 2023. A step-up in committed spend is direct evidence of the compute ramp management calls temporary. Also pull the "information technology expense" delta and its stated driver from each 2026 6-K.
- Opex by line (R&D, S&M, G&A) each quarter, ex social charges and ex FX; Q4 S&M as % of revenue in 2023–2025 to size the Wrapped seasonality that consensus needs opex to fall into.

**Alt data**
- **[pre-Oct 22] Pathmatics / Sensor Tower ad intelligence.** Spotify's estimated paid media spend by month and market, 2024 to latest. *Confirms:* spend running well above 2025 through Q4-26, not stepping down after Q3.
- Job postings (LinkedIn, Revelio): Spotify open roles by function. Headcount is flat; a mix shift toward ML/inference and trust & safety raises cost per head.

**Expert calls**
- Former Spotify ML infrastructure or platform lead (2023–2026). Ask: inference cost per DAU for DJ, Prompted Playlists, SongDNA, and the remix tool; how inference scales with usage; what "Chirp"/"Xirp" actually saves; whether compute is in cost of revenue or opex.
- Former Spotify FP&A lead. Ask: whether the 2027 plan assumed the €200M dropped out; how marketing is now tied to subscriber targets; what "normalize" meant internally.
- Former Spotify content integrity / trust & safety lead. Ask: volume of AI-generated uploads per day; cost of the AI persona labeling and spam removal programs; whether this cost is growing with upload volume.
- Former label AI-licensing exec or ex-Suno/Udio commercial lead. Ask: what the labels expect to earn from AI licensing in 2027; what Spotify must ship to keep creation inside the app.

**Read-throughs**
- Deezer's disclosures on AI share of daily uploads (20 to 30%); Warner's "material contribution from FY27" AI licensing guide; UMG's Udio/Klay revenue commentary. *Confirms:* AI revenue accrues to labels while Spotify's AI line is cost.

---

## Cross-cutting

- **[pre-Oct 22] Visible Alpha quarterlies** for ARPU, subs, MAU, GM, opex and OI through Q4-27. Replace the reconstructed consensus in the pitch's delta table.
- **[pre-Oct 22] Sell-side notes.** Benchmark (margin), KeyBanc (ads), Evercore (estimate cut), Inderes (2027 EBIT €3.12B). Map which analysts carry 2027 opex growth under 6%; those are the cuts that move consensus.
- **Label prints.** UMG Q3 (~29 Oct), WMG FQ4 (mid-Nov), Sony (Nov): subscription growth, wholesale escalator commentary, superfan tier timing, AI licensing revenue.
- **Management access.** Post-Q3 IR call. Questions in order: Q4 opex vs Q3 in absolute euros; whether any DM-eligible surface has been added in 2026; add-on launch gating; ARPU growth framing for Q1-27.
- **Positioning.** 13F deltas at the Nov filing; borrow and utilization; options-implied move into 22 Oct.

## Priority order (conviction gained per dollar and per day)

1. Antenna and credit-card panel churn after the Feb-26 hike (point 1).
2. Two or three distributor calls on DM enrollment and uplift (point 4).
3. Google Cloud commitment step-up in the 20-F plus Pathmatics marketing spend (point 5).
4. Former India/SEA growth lead on conversion and the Lite reversal (point 3).
5. Major-label digital exec on superfan wholesale ask and Streaming 2.0 escalators (points 1 and 2).

Items 1, 3, and the first distributor call can be done before 22 Oct.
