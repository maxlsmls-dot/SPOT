# Driving a gross margin assumption from Discovery Mode and autoplay growth

Date: 2026-10-02. Inputs: `data/spotify_autoplay_sentiment.xlsx`, `data/discovery_mode_efficacy.xlsx`. Model tabs: `data/SPOT_DM_Tabs.xlsx` (built by `analysis/dm_model_tabs.py`), formatted to the operating model's conventions so the eight tabs can be copied in as they are. Nothing here is an investment view; it is a way to turn the two datasets and Spotify's disclosures into a margin input.

## Bottom line

- Discovery Mode (DM) is a royalty discount, not revenue. Spotify's saving is simply: enrolled DM-context streams × 30% × their royalty. It does not depend on whether the artist gains, so falling *efficacy* for artists does not by itself cut the saving. What it does is cap future growth of the lever and raise the odds of backlash.
- The lever is bounded. At the measured inputs (33% of streams on DM-eligible surfaces, 33% of those enrolled, so 10.9% of all streams) the saving is about EUR 340m, ~200 bp of consolidated gross margin. Each further point of enrollment is worth roughly EUR 12m, and the contribution only rises in bp terms while the saving grows faster than revenue.
- "Growth slowing" is a margin headwind, not just slower help. Gross margin is a ratio: marketplace gross profit grew roughly 41% a year from 2021 to 2025 and now sits at ~370 bp of margin. With revenue compounding at 9-14%, marketplace has to grow at least that fast to hold its contribution flat. A marketplace growing 10-15% is ~zero incremental bp; one growing 0-5% is negative.
- Translated into the tabs: the Base case gives a Discovery Mode effect on gross margin of +42 bp in FY'26E and +10 bp in FY'27E, against +44 bp in FY'25, i.e. the saving's growth decelerating from ~40% to ~37% to ~14% as it converges on revenue growth. Bull gives +55 and +28 bp; Bear +19 and 0 bp. On the illustrative path that is FY'27E gross margin of 34.6% / 34.3% / 34.0% for Bull / Base / Bear, with the ex-DM drivers held at a placeholder that should be replaced from the model's own GM build.
- The two workbooks support the *direction* (plateauing autoplay salience, fading DM lift, defensive enrollment) but not magnitudes. The two numbers the expert calls or the burner-account sampling must pin down are exactly the model's two levers: the share of streams on DM-eligible surfaces (Topic 3, the ceiling) and the share of those that are enrolled (Topic 2).

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

- The workbook is internally consistent. Every formula is correct, the By Year counts reconcile to the 4,000 scored rows, there are no duplicate posts, and the theme patterns are documented on the Notes tab.
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
- The Summary labels 7.5% as the "median DM share of monthly streams (established artists)", but the underlying list mixes four established artists at 3.5-5% with catalog-heavy and tiny artists at 33-50%. Use 4% for established artists; the data tab now separates the two groups.
- Everything is self-selected from one subreddit; the workbook says so itself ("illustrates a thesis; it cannot carry one on its own").

Verdict: strong on mechanism and direction, weak on magnitude. It justifies modelling the enrolled share as creeping up rather than compounding, and the eligible-surface share as capped.

## 2. How Discovery Mode reaches gross margin

Accounting, from Spotify's 20-F: "Cost of revenue also reflects discounts provided by certain rights holders in return for promotional activities in connection with marketplace programs." DM lowers cost of revenue. Marquee and Showcase, the other marketplace products, are sold to labels and booked as Ad-Supported revenue. Each quarter's Premium gross margin driver sentence reads "revenue growth outpacing music royalty costs net of certain marketplace programs", so DM is inside the Premium margin line.

What Spotify has disclosed about size:

| | Figure | Source |
|---|---|---|
| Marketplace gross profit, 2018 | under EUR 20m | Investor Day, June 2022 |
| Marketplace gross profit, 2021 | more than EUR 160m | Investor Day, June 2022 |
| Marketplace gross profit, 2025 | 4x 2021 (so EUR 640m or more) | Investor Day, May 2026 |
| Ad-Supported gross profit, 2025 | EUR 330m (18% margin), up EUR 101m | FY2025 20-F |
| Consolidated gross margin | 2024 30.1%; 2025 32.0%; Q1 2026 33.0%; Q2 2026 33.4%; Q3 2026 guide 32.9% | 20-F, shareholder letters |
| Premium gross margin | 2023 29%; 2024 33%; 2025 34%; Q2 2026 35% | 20-F, Q2 2026 letter |
| 2030 target | gross margin 35-40%, mid-teens revenue CAGR | Investor Day, May 2026 |
| Royalties paid to music rights holders | USD 10bn in 2024, USD 11bn in 2025 (~EUR 9.3bn, ~EUR 10.1bn) | Loud & Clear 2025, 2026 |

The Ad-Supported line is the sanity check on the split. Marquee and Showcase sit in that segment at near-100% margin, so they cannot be much more than EUR 150-300m unless the core ad business loses money at the gross level. At the measured inputs the tabs imply Marquee + Showcase of about EUR 300m, just inside that ceiling, and Discovery Mode at ~53% of the disclosed marketplace figure.

The chain the tabs use, bottom-up from the two measured stream shares:

    enrolled DM-context streams, % of all streams  = e × s
    royalty pool before discounts                  = royalties paid / (1 − e × s × d)
    Discovery Mode saving                          = pool × e × s × d
    gross margin                                   = gross margin ex-DM + saving / revenue

where `e` is the share of streams on DM-eligible surfaces (Radio, Autoplay, Mixes), `s` is the share of those streams that are enrolled, and `d` is the 30% discount. The eligible-surface share is what "autoplay growth" moves; the enrolled share is what DM adoption moves; `e × s` is "share of streams via Discovery Mode", which is Topic 2 of the triangulation matrix; the ceiling on `e` and `s` is Topic 3. The gross-up line matters because the royalties Spotify reports paying are already net of the discount. The disclosed marketplace figure (4x 2021) no longer drives anything; it sits at the bottom of the bridge as a cross-check.

Why DM is zero-sum for artists but not for Spotify: the program reallocates slots, it does not create listening. The one artist in the dataset who checked total streams saw Spotify report +55% in DM contexts while the song's total fell. So Spotify's saving is `pool × e × s × d` whether or not the artist benefits.

## 3. FY'25 as built (`DM GM Bridge`, sections 1-4)

With e = 33%, s = 33%, royalties paid of EUR 10.1bn (58.8% of revenue) and the 30% discount:

| | Value |
|---|---|
| Enrolled DM-context streams, share of all streams (`e × s`) | 10.9% |
| Royalty pool before discounts | ~EUR 10.4bn |
| Royalties on enrolled DM-context streams, before discount | ~EUR 1.14bn |
| Discovery Mode saving FY'25 | ~EUR 341m, ~198 bp |
| Gross margin excluding Discovery Mode FY'25 | 30.0% (reported 32.0% less 198 bp) |
| Cross-check: saving as share of disclosed marketplace gross profit (EUR 640m) | 53% |
| Cross-check: implied Marquee + Showcase vs Ad-Supported gross profit | EUR 299m vs EUR 330m |

FY'24 e and s are back-fills (31% and 27.5%), not measurements, set so the FY'24 to FY'25 growth in the saving is close to the disclosed 2021-25 marketplace CAGR of ~41%; they only affect the FY'25 y/y line (+44 bp). The `DM Sensitivity` tab grids the FY'27E contribution, the FY'27E gross margin and the FY'27E y/y effect for `e` from 25% to 40% and `s` from 25% to 60%.

## 4. Translating "growth slowing" into the levers

| Lever | Evidence in the workbooks | Evidence elsewhere | Base-case setting |
|---|---|---|---|
| `e`, eligible-surface share | Autoplay topic share peaked in 2025; DJ / Smart Shuffle discussion halved since 2024; Smart Shuffle made removable; AI-slop complaints at 4.6% of topic posts and Spotify's Sept 2025 clean-up trims recommendation inventory | 2018 prospectus: ~30% of listening Spotify-programmed before Autoplay default-on, Smart Shuffle and Mixes; 33% of discoveries in algorithmic contexts | 33%, +1.0 pt then +1.5 pt (cumulative) |
| `s`, enrolled share | Lift fading (4.1x to 0.8x medians, n small); 100% of sub-10k artists go up so the tail keeps enrolling; above 10k a coin flip; enrollment is defensive (opting out costs 50-70% of radio streams) | Billboard: manager-reported lifts fell from 200-300% to 20-30%; House Judiciary letters on "race to the bottom"; majors largely not participating | 33% measured, +5.5 pt then +6.5 pt (cumulative) |
| `d`, discount | not observable | Label renewals and regulatory pressure are the only things that move it | 30% held (per-year input on the inputs tab) |

The ratio point is the heart of the answer. The saving must grow at the revenue growth rate just to hold its ~200 bp contribution. If it grows 10-15% from here it is margin-neutral, and if it grows below that it is a headwind even though it keeps growing in euros. Marquee and Showcase are outside this bridge: they are Ad-Supported revenue and belong in the ad-supported build.

## 5. Case outputs (`DM GM Bridge`, sections 3-5)

Common: revenue EUR 17.2bn → 19.5bn → 21.3bn (same placeholders as the audiobook tabs; link to the IS); royalties at 58.8% of revenue; y/y expansion excluding Discovery Mode of +100 / +80 bp (placeholder; replace from the model's own GM build).

| | FY'25 | FY'26E | FY'27E |
|---|---|---|---|
| Bull: gross margin (e +1.5 / +2.5 pt, s +7 / +10 pt) | 32.0% | 33.6% | 34.6% |
| Base: gross margin (e +1 / +1.5 pt, s +5.5 / +6.5 pt) | 32.0% | 33.4% | 34.3% |
| Bear: gross margin (e flat, s +3 / +3 pt) | 32.0% | 33.2% | 34.0% |
| Discovery Mode y/y gross margin effect, Bull / Base / Bear (bp) | +44 | +55 / +42 / +19 | +28 / +10 / 0 |
| Discovery Mode contribution to gross margin, Base (bp, level) | 198 | 240 | 250 |
| Implied growth in the saving, Base | 40% | 37% | 14% |
| Consensus gross margin (placeholder) | 32.0% | 33.2% | 34.5% |

Reading: the y/y effect is the change in bp level, so the shape of the enrollment path sets the shape of the effect. Base is front-loaded (+5.5 pt of enrollment in FY'26E, +1 pt more in FY'27E) so the contribution decays from +44 to +42 to +10 bp as the saving's growth converges on revenue growth. Bull keeps the saving growing above 40% in FY'26E; Bear caps enrollment after a small defensive step, so the saving grows with the pool only and the contribution is flat in bp by FY'27E. The Base path sits 22 bp above the consensus placeholder in FY'26E and 18 bp below in FY'27E.

## 6. Dropping the tabs into the model

**Premium gross margin build (`data/SPOT_DM_PremiumGM_Tab.xlsx`, built by `analysis/dm_premium_gm_tab.py`).** The model-side version of the chain, annual FY'25-FY'30 in the layout of the model's Sheet2: premium revenue from RPM row 55, a normal label royalty rate before Discovery Mode (61% of premium revenue, input), e and s with Bear/Base/Bull rows in the Assumptions-tab pattern (FY'25 from DM Inputs D30/D35, FY'26E-FY'27E from the DM Inputs case rows, faded linearly to flat by FY'30E), royalty % after the 30% haircut = normal rate × (1 − e × s × 30%), other premium cost of revenue plugged at FY'25 so the reported 34% is reproduced, and premium gross margin = 1 − royalty % after haircut − other %. A memo block weights it with an ad-supported margin for the consolidated row the DCF reads. Paste the `DM Premium GM` tab, then Find & Replace `[SPOT_DM_PremiumGM_Tab.xlsx]` with nothing so the links point at the model's own RPM, Valuation and DM Inputs tabs.

1. Copy the eight `DM ...` tabs from `data/SPOT_DM_Tabs.xlsx`. They reference only each other.
2. On `DM Inputs`: set the case selector (C4) to `=Valuation!$C$3`; link the FY'26E-FY'27E revenue cells (row 7) to the IS and the royalty-% cells (row 12) to the music-cost line if the model has one; link the consensus rows (30-31) to the consensus tab; replace the ex-DM expansion placeholder (row 29) with the model's own GM build excluding Discovery Mode. The levers are e (D16), s (D21) and their case rows (18-20, 23-25, cumulative changes vs FY'25 in points).
3. On `DM GM Bridge`: the row to carry into the GM build is "Y/y gross margin effect of Discovery Mode, bp" (yellow box, section 3), added to the y/y expansion from other drivers; or take the "Gross Margin" row in section 4 directly if the ex-DM expansion input is the model's own. The level row "Discovery Mode contribution to gross margin, bp" is already inside reported gross margin and is there for sizing.
4. Watch Premium gross margin, not consolidated: DM accrues almost entirely there. A quarter where Premium stalls while pricing is still flowing through is the first read on the thesis.
5. Signposts: whether Q3 2026 lands above the 32.9% guide; whether the letters keep using "net of certain marketplace programs" in the Premium driver sentence; any new DM surface (Smart Shuffle, DJ sessions, Discover Weekly would be a step up in `e` and a regulatory tripwire); label renewal language on the discount; Ad-Supported margin, where Marquee sits.
6. Questions for the calls, phrased as model cells: (a) what share of total streams is served from Radio, Autoplay and Mixes, and is it still growing; (b) what share of those streams is enrolled, by major versus independent (the burner-account sampling in `tools/dm_autoplay` answers the same question from the outside); (c) is there a product rule, label-negotiated cap, or engagement guardrail on enrolled share within those surfaces; (d) has the 30% ever been negotiated down, and is it on the table in the next major-label cycle.

## Sources

- Spotify FY2024 and FY2025 Form 20-F (revenue EUR 15,673m and 17,186m; Premium gross margin 33% and 34%; Ad-Supported gross profit EUR 330m in 2025; marketplace discounts in cost of revenue; royalty structure)
- Spotify Q1 2026 and Q2 2026 shareholder letters (6-K exhibits: gross margin 33.0% and 33.4%; Premium 34.8% and 35%; Q3 guide 32.9%)
- Spotify Investor Day, June 8 2022 transcript (marketplace gross profit under EUR 20m in 2018, more than EUR 160m in 2021)
- Spotify Investor Day, May 21 2026 recap (marketplace gross profit 4x 2021; 2030 targets 35-40% gross margin)
- Spotify 2018 Form F-1 (Spotify-programmed listening about 30% of all listening)
- Spotify Loud & Clear 2025 and 2026 (USD 10bn and 11bn royalties paid)
- Spotify for Artists Discovery Mode page (+50% saves, +44% playlist adds, +37% follows in month one; 33% of discoveries in algorithmic contexts; Mixes added January 2024)
- Billboard, "Spotify Discovery Mode: Hated by Politicians, Loved by Managers" (lift fade reported by managers; House Judiciary scrutiny); Digital Music News, March 2023 (major-label stance)
