# Discovery Mode → gross margin: method, estimate, and how it wires into the revenue build

Companion to `analysis/discovery_mode_gross_margin.xlsx` (model) and `analysis/discovery_mode_efficacy.xlsx` (the r/musicmarketing evidence). Research as of 2 Oct 2026. Updated the same day to anchor the model on the house view that Discovery Mode is at least 80% of Marketplace gross profit.

## Answer in one paragraph

The model now runs on the Marketplace anchor. Marketplace gross profit was "more than €160m" in 2021 and about 4× that by 2025 (~€640m); with Discovery Mode (DM) at 80% of it, **DM is worth about €510m, or ~300bp of gross margin, in FY2025**. That is roughly half of the 518bp of reported margin expansion between FY2021 and FY2025. Across Bear/Base/Bull the FY2030 contribution runs **~235bp / ~325bp / ~395bp**. On public bounds alone (no anchor), the same chain gives only ~70bp and ~€120m, and the model keeps that figure visible beside the anchored one because the two cannot both be right: the anchor needs DM streams to be about a fifth of all music streams, which strains Spotify's own statements about how much listening is programmed.

## The chain

```
DM saving (% of revenue) = s_ctx × s_dm × d × r_rec × m
```

| Term | Meaning | Public bounds | Anchored (mode 1) | Where it comes from |
|---|---|---|---|---|
| s_ctx | Share of music streams in DM contexts (Spotify Radio, Autoplay, Spotify Mixes) | 14.0% | ~61% | Triangulated 9–20%; anchor back-solves it |
| s_dm | Share of those context streams that are DM-enrolled | 33.0% | 33.0% | House assumption, held in mode 1 |
| d | Commission on recording royalties for DM streams | 30% | 30% | Spotify for Artists terms, unchanged under Sept 2025 T&Cs |
| r_rec | Recording royalties as % of music revenue | 54% | 54% | Not disclosed; MIDiA per-stream split 30/56/14 |
| m | Music share of total revenue | 92% | 92% | Assumption; podcast ads and audiobook à-la-carte carry no DM |
| Product | DM saving as % of revenue | 0.69% | 2.98% | |

**Why it is a margin item, not a redistribution.** The FY2024 and FY2025 20-Fs say cost of revenue "reflects discounts provided by certain rights holders in return for promotional activities in connection with marketplace programs," and every 2025–26 shareholder letter attributes Premium margin gains to "music costs net of marketplace programs." Spotify keeps the commission.

## The Marketplace anchor (Inputs, section F)

| Item | Value | Source |
|---|---|---|
| Marketplace gross profit FY2021 | €160m | Investor Day, 8 Jun 2022: "more than €160m" |
| Multiple by FY2025 | 4.0× | Third-party recap of Investor Day, 21 May 2026 |
| Implied Marketplace gross profit FY2025 | ~€640m | Geometric interpolation for 2022–24 |
| DM share of Marketplace gross profit | 30% → 80% (FY2021 → FY2025) | House view for FY2025; ramp assumed for earlier years |
| Anchor DM gross profit FY2025 | ~€512m, ~298bp | |
| DM streams required as % of all music streams | ~20% | = anchor ÷ (revenue × d × r_rec × m) |
| Same product from public bounds | 4.6% | 14% × 33% |

**Calibration modes** (`Inputs!B50`): 0 runs the public-bounds inputs unchanged; 1 holds s_dm at 33% and lets the context share absorb the anchor (~61%); 2 holds s_ctx and lets enrollment absorb it (~143%, capped at 100%, so the anchor cannot be reached this way); 3 splits the gap (~29% × ~69%). History (FY2021–25) is back-solved to the anchor by year. Forecast years take the anchored FY2025 product plus each scenario's change in s_ctx × s_dm versus FY2025 as entered, so the scenario deltas carry over in full.

**What the anchor strains.** Spotify said in January 2022 that "the majority of streams" come from active sessions, and DM contexts are a subset of programmed listening, so a 61% context share contradicts that statement. Mode 3's ~29% × ~69% is more plausible on the context side but puts enrollment above the ~57% no-majors ceiling from the catalog math below, implying either major-label participation or an Autoplay share far larger than the 25bn-stream sample captured. And on the anchor, DM alone explains about half of the FY2021–25 margin expansion, more than management's "about a third from music" leaves for all of music. One of three things gives: the "4×" recap overstates Marketplace gross profit, the music third was framed over a different period, or the public bounds on programmed listening are stale. This is the first question to put to the Tegus calls (Topic 2 of the triangulation matrix).

## Estimating s_ctx from public sources (the public-bounds case)

| Source | What it says | Implication for DM contexts |
|---|---|---|
| F-1 prospectus, Feb 2018 | ~31% of all listening is Spotify-programmed (editorial + algorithmic) | Ceiling for all programmed listening |
| Spotify for Artists, Jan 2022 | "The majority of streams" are active; "over a quarter" of new-artist *discoveries* come from Mixes, Radio and Autoplay | Programmed < 50%; discovery share overstates stream share, so DM contexts < 25% |
| Your Music Marketing sample via Music Ally, Feb 2024 | 25bn streams: 18.7% from algorithmic playlists and mixes incl. radio, ~21% in the last 12 months | Strip Discover Weekly / Release Radar / On Repeat, add Autoplay: ~10–16% |
| Anderson et al. (Spotify Research) 2020, cited 2021 | "Up to one-fifth" of streams attributable to algorithmic recommendations | ≤20% for everything algorithmic |
| r/musicmarketing corpus | DM-context share of enrolled indie artists' streams: 3.5–5% for 500k+ monthly-stream artists, median 7.5%, up to 33–50% for catalog-heavy acts | Indie-only; big indie acts in single digits |

Selection: 14% Base for FY2025, 9% Bear and 20% Bull bookends. Before Daily Mix joined DM on 3 Jan 2024 only Radio + Autoplay counted, modelled at 9–9.5% for FY2021–23.

## Checking s_dm = 33% (catalog math)

Enrolled catalog starts with its natural share of context streams, *e*, and is boosted *b*-fold by the DM signal inside a fixed inventory: s_dm = e·b / (e·b + 1 − e).

- Streams outside UMG, Sony, WMG and Merlin: ~28% (FY2025 20-F: the four ≈ 72%).
- Share of that catalog enrolled: ~45% (assumption; self-serve needs 25k+ monthly listeners; Believe says it moves "hundreds of thousands of tracks every month").
- Add ~2pp for Merlin members and labels enrolling via Spotify's partnerships team → *e* ≈ 14.6%.
- Boost *b* ≈ 3.1, from the +214% median Spotify-reported lift across 13 artist screenshots.
- Implied s_dm ≈ 35%, matching the 33% assumption.

With no major label, *e* cannot exceed ~30%, which caps s_dm near 45–57% even at a 2–3× boost. If the boost has faded to the 2025–26 campaign level (~1.8×), holding 33% needs enrollment near 70% of eligible catalog. That mechanism drives the Bear case.

## Scenarios (FY2026–FY2030), anchored

| | Bear | Base | Bull |
|---|---|---|---|
| s_ctx path (as entered) | Flat 14% | +0.5pp/yr → 16.5% | +1pp/yr plus +3pp step in FY2027 (DM extended to other surfaces) → 22% |
| s_dm path (as entered) | −1.5pp/yr → 25.5% (boost fades, enrollment churns) | +1pp/yr → 38% | Major label opts in FY2027 (+8pp), then +2.5pp/yr → 50% |
| d | 30%, cut to 25% from FY2028 (regulatory/litigation) | 30% | 30% |
| FY2030 contribution, anchored | ~235bp | ~325bp | ~395bp |
| FY2030 contribution, public bounds only | 44bp | 93bp | 164bp |

## Wiring into the revenue build

- Paste your revenue into `Inputs` row 40 (override). Reported margin = ex-DM margin + DM contribution; ex-DM is derived for history and rolls forward by the bp steps in `Inputs` row 45, or paste your own ex-DM levels into row 46.
- Or link directly: `'Revenue & GM'!row 22` is DM as % of revenue by year; row 27 is DM in EUR m. Subtract row 27 from your cost of revenue line.
- Scenario selector `Inputs!B4`; calibration mode `Inputs!B50`; DM share of Marketplace `Inputs!G54`.

## Caveats

- Both unknowns are estimates; neither is disclosed. The sensitivity grid on the Summary sheet covers s_ctx 10–60% × s_dm 20–100% for FY2030.
- The "4×" Marketplace figure is a third-party recap, not a Spotify number; the FY2021 €160m is Spotify's.
- Financial history was taken from search renderings of the 20-Fs and letters because the research environment could not fetch sec.gov or spotify.com directly. Items marked (v) on the Financials sheet should be re-checked before external use. FY2022 cost of revenue (€8,801m) and gross profit (€2,926m) were confirmed against the 20-F.
- The placeholder revenue build compounds at ~11% to FY2030, below management's mid-teens target. It only turns percentages into euros. Replace it.
- Lean-back growth does not automatically reach DM: AI DJ, Smart Shuffle and Discover Weekly are not DM contexts today.

## What to watch

1. A major label opting in (Bull trigger). The 2025 UMG/WMG/Sony deals do not mention Discovery Mode in any public rendering.
2. Spotify extending DM to Smart Shuffle, DJ or other personalised surfaces.
3. Changes to the 30% commission under Congressional, CMA or litigation pressure (Capolongo class action, arbitration compelled Apr 2026).
4. Distributor-level enrollment signals (Believe/TuneCore, DistroKid) and the per-track lift artists report, which the efficacy workbook tracks.
5. Any Spotify disclosure of Marketplace revenue or gross profit that would firm up the anchor.
