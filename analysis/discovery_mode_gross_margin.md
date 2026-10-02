# Discovery Mode → gross margin: method, estimate, and how it wires into the revenue build

Companion to `analysis/discovery_mode_gross_margin.xlsx` (model) and `analysis/discovery_mode_efficacy.xlsx` (the r/musicmarketing evidence). Research as of 2 Oct 2026.

## Answer in one paragraph

On Base inputs, Discovery Mode (DM) is worth about **69bp of gross margin in FY2025, roughly €118m** of retained royalty commission. That is ~12% of the 518bp of reported margin expansion between FY2021 and FY2025, and about a third of the "music" third of the expansion that management cited at the May 2026 Investor Day. Across Bear/Base/Bull the FY2030 contribution runs **44bp / 93bp / 164bp**, so DM moves the FY2030 margin by roughly ±50bp around Base. It is a real lever but a second-order one next to price, mix and the 35–40% FY2030 target.

## The chain

```
DM saving (% of revenue) = s_ctx × s_dm × d × r_rec × m
```

| Term | Meaning | FY2025 Base | Where it comes from |
|---|---|---|---|
| s_ctx | Share of music streams in DM contexts (Spotify Radio, Autoplay, Spotify Mixes) | 14.0% | Triangulated, 9–20% range (see below) |
| s_dm | Share of those context streams that are DM-enrolled | 33.0% | Your assumption; consistent with catalog math (below) |
| d | Commission on recording royalties for DM streams | 30% | Spotify for Artists terms, unchanged under Sept 2025 T&Cs |
| r_rec | Recording royalties as % of music revenue | 54% | Not disclosed; MIDiA per-stream split 30/56/14; range 50–58% |
| m | Music share of total revenue | 92% | Assumption; podcast ads and audiobook à-la-carte carry no DM |

Product: 0.14 × 0.33 × 0.30 × 0.54 × 0.92 = 0.69% of revenue.

**Why it is a margin item, not a redistribution.** The FY2024 and FY2025 20-Fs say cost of revenue "reflects discounts provided by certain rights holders in return for promotional activities in connection with marketplace programs," and every 2025–26 shareholder letter attributes Premium margin gains to "music costs net of marketplace programs." Spotify keeps the commission.

## Estimating s_ctx (the softest number)

Spotify has never disclosed the Radio/Autoplay/Mixes share of streams. The public bounds:

| Source | What it says | Implication for DM contexts |
|---|---|---|
| F-1 prospectus, Feb 2018 | ~31% of all listening is Spotify-programmed (editorial + algorithmic) | Ceiling for all programmed listening |
| Spotify for Artists, Jan 2022 | "The majority of streams" are active; "over a quarter" of new-artist *discoveries* come from Mixes, Radio and Autoplay | Programmed < 50%; discovery share overstates stream share, so DM contexts < 25% |
| Your Music Marketing sample via Music Ally, Feb 2024 | 25bn streams: 18.7% from algorithmic playlists and mixes incl. radio, ~21% in the last 12 months | Strip Discover Weekly / Release Radar / On Repeat, add Autoplay: ~10–16% |
| Anderson et al. (Spotify Research) 2020, cited 2021 | "Up to one-fifth" of streams attributable to algorithmic recommendations | ≤20% for everything algorithmic |
| r/musicmarketing corpus | DM-context share of enrolled indie artists' streams: 3.5–5% for 500k+ monthly-stream artists, median 7.5%, up to 33–50% for catalog-heavy acts | Indie-only; big indie acts in single digits |

Selection: **14% Base for FY2025**, 9% Bear and 20% Bull bookends. Before Daily Mix joined DM on 3 Jan 2024 only Radio + Autoplay counted, modelled at 9–9.5% for FY2021–23 with a +3.5pp step in FY2024.

## Checking s_dm = 33%

Enrolled catalog starts with its natural share of context streams, *e*, and is boosted *b*-fold by the DM signal inside a fixed inventory:

```
s_dm = e·b / (e·b + 1 − e)
```

- Streams outside UMG, Sony, WMG and Merlin: ~28% (FY2025 20-F: the four ≈ 72%).
- Share of that catalog enrolled: ~45% (assumption; self-serve needs 25k+ monthly listeners; Believe says it moves "hundreds of thousands of tracks every month").
- Add ~2pp for Merlin members and labels enrolling via Spotify's partnerships team → *e* ≈ 14.6%.
- Boost *b* ≈ 3.1, from the +214% median Spotify-reported lift across 13 artist screenshots.
- Implied s_dm ≈ 35%, matching the 33% assumption.

The same math gives the ceiling question (Topic 3 in the triangulation matrix): with no major label, *e* cannot exceed ~30%, which caps s_dm near 45–57% even at a 2–3× boost. If the boost has faded to the 2025–26 campaign level (~1.8×), holding 33% needs enrollment near 70% of eligible catalog. That mechanism drives the Bear case.

**Sanity bound from Marketplace disclosures.** Marketplace gross profit was ">€160m" in 2021 (Investor Day 2022) and "about 4×" that by 2025 per a third-party Investor Day 2026 recap, so ~€640m. The Base DM estimate of €118m is ~18% of that, the rest being Marquee and Showcase. If DM were all of Marketplace, s_ctx × s_dm would be 25% versus the model's 4.6%, so the estimate is conservative relative to that bound.

## Scenarios (FY2026–FY2030)

| | Bear | Base | Bull |
|---|---|---|---|
| s_ctx path | Flat 14% | +0.5pp/yr → 16.5% | +1pp/yr plus +3pp step in FY2027 (DM extended to Smart Shuffle or other surfaces) → 22% |
| s_dm path | −1.5pp/yr → 25.5% (boost fades, enrollment churns) | +1pp/yr → 38% | Major label opts in FY2027 (+8pp), then +2.5pp/yr → 50% |
| d | 30%, cut to 25% from FY2028 (regulatory/litigation) | 30% | 30% |
| FY2030 contribution | 44bp | 93bp | 164bp |
| FY2030 DM gross profit (placeholder revenue) | €131m | €275m | €483m |

## Wiring into the revenue build

- Paste your revenue into `Inputs` row 40 (override) and your ex-DM gross margin path into `Inputs` row 45. Reported margin = ex-DM margin + DM contribution.
- Or link directly: `'Revenue & GM'!row 22` is DM as % of revenue by year; row 27 is DM in EUR m. Subtract row 27 from your cost of revenue line.
- The scenario selector is `Inputs!B4`. All three scenarios are computed side by side on `DM build`, so charts and the sensitivity grid do not depend on the selector.

## Caveats

- Both unknowns are estimates; neither is disclosed. The sensitivity grid on the Summary sheet shows FY2030 bp for s_ctx 10–22% × s_dm 20–60%.
- Financial history was taken from search renderings of the 20-Fs and letters because the research environment could not fetch sec.gov or spotify.com directly. Items marked (v) on the Financials sheet should be re-checked against filing tables before external use. FY2022 cost of revenue (€8,801m) and gross profit (€2,926m) were confirmed against the 20-F.
- The placeholder revenue build compounds at ~11% to FY2030, below management's mid-teens target. It only exists to turn percentages into euros; replace it.
- Growth in lean-back listening does not automatically reach DM: AI DJ, Smart Shuffle and Discover Weekly are not DM contexts today.

## What to watch

1. A major label opting in (Bull trigger). The 2025 UMG/WMG/Sony deals do not mention Discovery Mode in any public rendering.
2. Spotify extending DM to Smart Shuffle, DJ or other personalised surfaces.
3. Changes to the 30% commission under Congressional, CMA or litigation pressure (Capolongo class action, arbitration compelled Apr 2026).
4. Distributor-level enrollment signals (Believe/TuneCore, DistroKid) and the per-track lift artists report, which the efficacy workbook tracks.
