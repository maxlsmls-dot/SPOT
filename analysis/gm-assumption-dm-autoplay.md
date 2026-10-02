# Driving a gross margin assumption from Discovery Mode and autoplay growth

Date: 2026-10-02. Inputs: `data/spotify_autoplay_sentiment.xlsx`, `data/discovery_mode_efficacy.xlsx`. Model: `analysis/spot_gm_driver_model.xlsx` (built by `analysis/build_gm_model.py`). Nothing here is an investment view; it is a way to turn the two datasets and Spotify's disclosures into a margin input.

## Bottom line

- Discovery Mode (DM) is a royalty discount, not revenue. Spotify's saving is simply: enrolled DM-context streams × 30% × their royalty. It does not depend on whether the artist gains, so falling *efficacy* for artists does not by itself cut the saving. What it does is cap future growth of the lever and raise the odds of backlash.
- The lever is bounded. At the calibrated inputs (eligible surfaces = 18% of streams, ~53% of those streams enrolled) the entire remaining DM runway at today's surfaces and discount is roughly 150 bps of consolidated gross margin, and that runway shrinks in bps terms every year revenue grows.
- "Growth slowing" is a margin headwind, not just slower help. Gross margin is a ratio: marketplace gross profit grew roughly 41% a year from 2021 to 2025 and now sits at ~370 bps of margin. With revenue compounding at 12-14%, marketplace has to grow at least that fast to hold its contribution flat. A marketplace growing 8-12% is ~zero incremental bps; one growing 0-5% is negative.
- Translated into the model: a street-style continuation (Scenario A) puts 2028E gross margin near 36.2%; the slowing thesis (B) near 34.5%; saturation with backlash (C) near 33.6%. The DM-and-autoplay piece alone is worth about 165 bps between A and B in 2028 and 260 bps between A and C. The non-marketplace drivers (pricing, audiobooks, podcasts, ad mix) are a placeholder in the model and should be replaced from the P&L model.
- The two workbooks support the *direction* (plateauing autoplay salience, fading DM lift, defensive enrollment) but not magnitudes. The two numbers the expert calls must pin down are exactly the model's two levers: the share of streams on DM-eligible surfaces (Topic 3, the ceiling) and the share of those that are enrolled (Topic 2).

## 1. What the two workbooks contain, and how far to trust them

### 1a. `spotify_autoplay_sentiment.xlsx` (listener side)

Every post in r/spotify and r/truespotify from January 2023 to October 1 2026 (210,365 posts, Arctic Shift archive), filtered by a keyword topic filter to 19,948 "autoplay / recommendation" posts, with a random 1,000 per year scored for sentiment by a RoBERTa tweet-sentiment model and tagged with eight keyword themes.

| | 2023 | 2024 | 2025 | 2026 YTD |
|---|---|---|---|---|
| All posts | 67,394 | 72,114 | 45,831 | 25,026 |
| Autoplay / rec posts, share of all | 7.1% | 9.9% | 11.8% | 10.3% |
| Share negative, headline | 34.0% | 36.6% | 39.1% | 42.4% |
| Share negative, intact posts only | 37.9% | 39.2% | 39.9% | 43.5% |
| Net sentiment (positive minus negative) | -10.8 | -12.0 | -11.2 | -18.2 |
| DJ / daylist / Smart Shuffle, share of topic posts | 19.8% | 17.2% | 14.3% | 16.0% |
| AI-generated music, share of topic posts | 0.3% | 0.6% | 3.1% | 4.6% |
| Paid / pushed content, share of topic posts | 0.5% | 1.2% | 1.0% | 1.8% |
| Cancel / switch language, share of scored posts | 0.6% | 1.4% | 1.2% | 2.4% |

What holds up:

- The workbook is internally consistent. Every formula is correct, the By Year counts reconcile to the 4,000 scored rows, there are no duplicate posts, and the theme patterns are documented on the Notes tab. Blue/black colour convention is followed.
- Topic salience rose through 2025 and the tone of the discussion has worsened every year. 2026 H1 was the most negative half-year in the series (44% negative on all posts). Discussion of the AI DJ / Smart Shuffle novelty has fallen by half since 2024, and in April 2025 Spotify made Smart Shuffle removable (the 959-upvote "You can now remove Smart Shuffle! Finally" post).
- AI-generated music went from a non-topic to 4.6% of autoplay posts. The highest-upvoted posts of 2025-26 are about AI tracks surfacing in Discover Weekly and recommendations.

What does not hold up, or needs care:

- **The headline sentiment trend is partly a composition artifact.** Deleted and removed posts (title only) score ~21% negative versus ~40% for intact posts. They were 26% of the 2023 sample and only 4-5% of 2025-26. On intact posts the deterioration is about 5.6 points, not 8.4. Still rising, but roughly half the size, and 2026 Q3 improved to 39%.
- The model scores overall tone, not tone toward the algorithm. Median post length rose from 270 to 416 characters; long rants skew negative regardless of subject.
- Absolute counts are unreliable: subreddit volume fell from 72k posts (2024) to ~33k annualized (2026), and the 2026 sample thins out after June (July 81, September 63 posts), which suggests archive lag rather than a real decline. The 2026 drop in topic share is weak evidence of a plateau.
- Only one of the 4,000 scored posts mentions "Discovery Mode" by name. Listeners experience the program as "sponsored recs" and "same songs over and over", so the listener dataset informs the autoplay share lever, not DM enrollment.
- Upvote-weighted negativity jumps around (43% / 44% / 29% / 62%) because a handful of viral posts dominate each year. Do not read a trend into it.

Verdict: usable as a direction-of-travel input for the autoplay share lever, worth at most about one point a year in either direction, and as evidence that listener tolerance for low-intent recommendations is falling.

### 1b. `discovery_mode_efficacy.xlsx` (artist side)

130 r/musicmarketing posts that mention Discovery Mode plus 1,953 comments, hand-coded into 70 first-hand artist experiences, with 35 Spotify for Artists screenshots read for campaign reports.

| Metric | Value | n |
|---|---|---|
| Median Spotify-reported lift, campaigns Aug 2023 - Nov 2024 | 4.06x | 4 |
| Median Spotify-reported lift, campaigns Jan 2025 - Jul 2026 | 0.78x | 3 |
| Saves + playlist adds per DM listener, median | 1.2% | 8 campaigns |
| Saves per listener, artists' overall audience, median | 19.9% | 4 dashboards |
| First-hand reports that went up, artists under 10k listeners | 100% | 8 |
| First-hand reports that went up, artists 10k+ | 39% | 18 |
| First-hand reports that went up, all | 56% | 70 |
| Reports saying Discover Weekly / algorithmic streams fell after opting in | 12 | of 70 |
| DM-context streams as share of an enrolled established artist's streams | 3.5-5% | 4 |

What holds up:

- Formulas are correct throughout (lifts, medians, COUNTIFS by year, size banding). The Summary tab links to the data tabs rather than hardcoding.
- The mechanism argument is sound and matches how the program is documented: DM is a relative boost inside a fixed pool of Radio, Autoplay and (since January 2024) Mixes slots, so per-track payoff must fall as enrollment grows. The Dec 2023 case (4 of 6 enrolled songs got zero DM streams) and the 2025 case (7 of 12 at 0-100 radio streams while enrolled) are the symptoms you would expect.
- The engagement gap is the most robust finding. DM listeners keep a song about 1% of the time; Spotify's own program page quotes "intent" rates in the same range. Those streams still carry a royalty (at 70%), and they are what listeners describe as "same songs over and over".
- The "defensive enrollment" pattern is well documented in the on/off cases: switching off cut radio/autoplay streams by 50-71% in two charted cases, and artists re-enrol out of fear. This matters for the model because it means enrollment can keep rising even as the lift fades.
- Billboard's reporting corroborates the fade independently: a manager who saw 200-300% gains in the program's first year later saw 20-30%.

What does not hold up, or needs care:

- **The lift comparison is 4 campaigns versus 3.** A rank test on those seven values is not significant (roughly p = 0.1). The lift metric also rewards songs with a tiny prior base (the 7.4x Oct 2024 campaign had 359 prior-28-day streams). The direction is plausible; the magnitude is not evidence.
- **The 18 before/after pairs trend toward "Up" over time** (2023: 1 up / 5 down; 2025-26: 3 up / 0 down), the opposite of the thesis. The workbook explains this as mix shift toward small artists, which is reasonable, but it means the pairs cannot support the time claim either way.
- The Reference tab's undated list of 13 "lift (%)" figures mixes multiples (2.77, 0.55) with percentages (20, 30, 60), so its median of 2.14 is meaningless. The intent-rate list is labelled "%" but stored as fractions (harmless).
- The Summary labels 7.5% as the "median DM share of monthly streams (established artists)", but the underlying list mixes four established artists at 3.5-5% with catalog-heavy and tiny artists at 33-50%. Use 4% for established artists.
- Everything is self-selected from one subreddit; the workbook says so itself ("illustrates a thesis; it cannot carry one on its own").

Verdict: strong on mechanism and direction, weak on magnitude. It justifies modelling the enrolled share as creeping up rather than compounding, and the eligible-surface share as capped.

## 2. How Discovery Mode reaches gross margin

Accounting, from Spotify's 20-F: "Cost of revenue also reflects discounts provided by certain rights holders in return for promotional activities in connection with marketplace programs." DM lowers cost of revenue. Marquee and Showcase, the other marketplace products, are sold to labels and booked as Ad-Supported revenue (they added EUR 58m to Ad-Supported revenue in 2024). Each quarter's Premium gross margin driver sentence reads "revenue growth outpacing music royalty costs net of certain marketplace programs", so DM is inside the Premium margin line.

What Spotify has disclosed about size:

| | Figure | Source |
|---|---|---|
| Marketplace gross profit, 2018 | under EUR 20m | Investor Day, June 2022 |
| Marketplace gross profit, 2021 | more than EUR 160m | Investor Day, June 2022 |
| Marketplace gross profit, 2025 | 4x 2021 (so EUR 640m or more) | Investor Day, May 2026 |
| Consolidated gross margin | 2023 ~25.6%; 2024 ~30%; 2025 32%; Q1 2026 33.0%; Q2 2026 33.4%; Q3 2026 guide 32.9% | 20-F, shareholder letters |
| Premium gross margin | 2023 29%; 2024 33%; 2025 34%; Q2 2026 35% | 20-F, Q2 2026 letter |
| 2030 target | gross margin 35-40%, mid-teens revenue CAGR | Investor Day, May 2026 |
| Royalties paid to music rights holders, 2025 | USD 11bn (~EUR 10.1bn) | Loud & Clear 2026 |

The identity the model uses:

    DM gross profit = royalty pool × e × s × d

where `e` is the share of streams on DM-eligible surfaces (Radio, Autoplay, Mixes), `s` is the share of those streams that are enrolled, and `d` is the 30% discount. The eligible-surface share is what "autoplay growth" moves; the enrolled share is what DM adoption moves; `e × s` is "share of streams via Discovery Mode", which is Topic 2 of the triangulation matrix; the ceiling on `e` and `s` is Topic 3.

Why DM is zero-sum for artists but not for Spotify: the program reallocates slots, it does not create listening. The one artist in the dataset who checked total streams saw Spotify report +55% in DM contexts while the song's total fell. So Spotify's saving is `pool × e × s × d` whether or not the artist benefits.

## 3. Calibration to 2025

With marketplace gross profit at EUR 640m (372 bps of 2025 revenue) and DM assumed to be 45% of it (the split is undisclosed; Marquee is the older and larger-revenue product):

| | Value |
|---|---|
| DM gross profit 2025 | ~EUR 288m, ~168 bps |
| Marquee + Showcase 2025 | ~EUR 352m, ~205 bps |
| Royalty pool on eligible surfaces (EUR 10.1bn × 18%) | ~EUR 1.8bn |
| Implied enrolled share `s` | ~53% |
| Implied DM-context enrolled streams, share of all streams (`e × s`) | ~9.5% |
| Ceiling at 100% enrollment, today's surfaces | ~EUR 545m, ~317 bps |
| Remaining runway | ~EUR 257m, ~150 bps of 2025 revenue |

The Inputs tab has a grid of implied `s` for `e` from 12% to 25% and DM share of marketplace from 35% to 65%. Any expert-call answer on Topic 2 or 3 should land in one of those cells; combinations above 100% are impossible and would mean the DM share of marketplace is set too high.

## 4. Translating "growth slowing" into the levers

| Lever | Evidence in the workbooks | Evidence elsewhere | Scenario B setting |
|---|---|---|---|
| `e`, eligible-surface share | Autoplay topic share peaked in 2025; DJ / Smart Shuffle discussion halved since 2024; Smart Shuffle made removable; AI-slop complaints at 4.6% of topic posts and Spotify's Sept 2025 clean-up trims recommendation inventory | Spotify: 33% of discoveries happen in algorithmic contexts; no new DM surface announced since Mixes (Jan 2024) | flat at 18% |
| `s`, enrolled share | Lift fading (4.1x to 0.8x medians, n small); 100% of sub-10k artists go up so the tail keeps enrolling; above 10k a coin flip; enrollment is defensive (opting out costs 50-70% of radio streams) | Billboard: manager-reported lifts fell from 200-300% to 20-30%; House Judiciary letters on "race to the bottom" | +3 pts a year (creep, not compounding) |
| `d`, discount | not observable | Label renewals and regulatory pressure are the only things that move it | 30% held |
| Marquee / Showcase | not covered | Ad-Supported gross margin fell to 13.0% in Q1 2026; marketplace revenue growth not called out in 2026 letters | +10% a year |

The ratio point is the heart of the answer. Marketplace gross profit must grow at the revenue growth rate (14% / 13% / 12% in the model) just to hold its ~370 bps contribution. Over 2021-25 it grew ~41% a year, which is why it has been a visible driver of the 25% to 32% expansion (roughly 200 of the ~520 bps; management says about a third of expansion came from the music business). If it grows 10-15% from here it is margin-neutral, and if it grows below that it is a headwind even though it keeps growing in euros.

## 5. Scenario outputs (from `Scenarios` tab)

Common: revenue EUR 17.2bn → 19.6bn → 22.1bn → 24.8bn; royalty pool at 58.8% of revenue; "other drivers" placeholder of +100 / +180 / +240 bps cumulative (set so Scenario B lands near H1 2026 actuals and the Q3 guide; replace from the P&L model).

| | 2025A | 2026E | 2027E | 2028E |
|---|---|---|---|---|
| A: continued growth (e +1.5 pt/yr, s +8 pt/yr, Marquee +20%) | 32.0% | 33.5% | 34.9% | 36.2% |
| B: slowing (e flat, s +3 pt/yr, Marquee +10%) | 32.0% | 33.0% | 33.9% | 34.5% |
| C: saturation with backlash (e -1 pt/yr, s capped, Marquee flat) | 32.0% | 32.7% | 33.2% | 33.6% |
| DM change vs 2025, A / B / C (bps) | 0 | +42 / +10 / -3 | +88 / +20 / -12 | +138 / +29 / -22 |
| Marquee change vs 2025, A / B / C (bps) | 0 | +11 / -7 / -25 | +24 / -12 / -46 | +40 / -16 / -63 |
| Implied marketplace gross profit growth, A / B / C | | 30% / 15% / 6% | 29% / 14% / 3% | 27% / 14% / 3% |

Reading: Scenario A needs marketplace to keep growing near 30% a year and enrollment to reach ~77% of eligible-surface streams by 2028, which is the kind of saturation the artist data says is already biting. Scenario B is what the two workbooks describe, and under it DM adds about 10 bps a year. Scenario C is the case where listener backlash (AI slop, "sponsored recs", Smart Shuffle removal) shrinks the surfaces the program lives on.

The `Sensitivity 2028` tab gives DM's 2028 contribution for any `e` × `s` pair. At `e` = 18%, each 10 points of enrolled share is worth ~32 bps in 2028; `e` has to rise to ~24% for DM to add 100 bps without enrollment moving.

## 6. Recommended way to carry this into the model

1. Carry gross margin as `2025 base + non-marketplace bridge + ΔDM + ΔMarquee`, with ΔDM from `pool × e × s × d` rather than a growth rate on a "marketplace" line. It makes the ceiling explicit and lets the expert calls update one cell.
2. Under the slowing thesis, use ΔDM of +10 bps a year and ΔMarquee of about -5 to -10 bps a year (it is growing, but slower than revenue). That puts the marketplace piece at roughly zero to +15 bps a year versus the ~+50 bps a year it has contributed since 2021. Everything beyond that in the path to 35-40% by 2030 has to come from pricing, audiobooks, podcasts and ad-supported mix.
3. Watch Premium gross margin, not consolidated: DM accrues almost entirely there. Premium went 29% → 33% → 34% → 35% (Q2 2026); a quarter where Premium stalls while pricing is still flowing through is the first read on the thesis.
4. Signposts: whether Q3 2026 lands above the 32.9% guide; whether the letters keep using "net of certain marketplace programs" in the Premium driver sentence; any new DM surface (Smart Shuffle, DJ sessions, Discover Weekly would be a step up in `e` and a regulatory tripwire); label renewal language on the discount; Ad-Supported margin, where Marquee sits.
5. Questions for the calls, phrased as model cells: (a) what share of total streams is served from Radio, Autoplay and Mixes, and is it still growing; (b) what share of those streams is enrolled, by major versus independent; (c) is there a product rule, label-negotiated cap, or engagement guardrail on enrolled share within those surfaces; (d) has the 30% ever been negotiated down, and is it on the table in the next major-label cycle.

## Sources

- Spotify FY2025 Form 20-F (revenue EUR 17,186m; Premium gross margin 34%; marketplace discounts in cost of revenue; royalty structure)
- Spotify Q1 2026 and Q2 2026 shareholder letters (6-K exhibits: gross margin 33.0% and 33.4%; Premium 34.8% and 35%; Q3 guide 32.9%)
- Spotify Investor Day, June 8 2022 transcript (marketplace gross profit under EUR 20m in 2018, more than EUR 160m in 2021)
- Spotify Investor Day, May 21 2026 recap (marketplace gross profit 4x 2021; 2030 targets 35-40% gross margin)
- Spotify Loud & Clear 2026 (USD 11bn royalties paid in 2025)
- Spotify for Artists Discovery Mode page (+50% saves, +44% playlist adds, +37% follows in month one; 33% of discoveries in algorithmic contexts; Mixes added January 2024)
- Billboard, "Spotify Discovery Mode: Hated by Politicians, Loved by Managers" (lift fade reported by managers; House Judiciary scrutiny)
- Spotify 2024 20-F (marketplace programs added EUR 58m to Ad-Supported revenue)
