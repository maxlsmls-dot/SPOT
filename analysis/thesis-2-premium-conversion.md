# Thesis 2 — Market overestimates Spotify's premium conversion funnel

All figures below are pulled from `SPOT_Cit_Case.xlsx` (tab named in the source map at the bottom). Street = 10-broker set on the `Totals` tab (median EoP subs 315M / 339.5M / 364.7M for 4Q26 / FY27 / FY28; mean net adds 24.6M / 24.4M for FY27 / FY28).

## Paragraph (full)

Consensus currently models ~24.6M and ~24.4M premium net adds in FY27 and FY28 (10-broker mean), implying 7.8% and 7.4% y/y subscriber growth, which on consensus MAUs requires global premium mix to hold at 38.2-38.6% through FY28. This generalizes the US/EU conversion curve onto emerging-market MAUs, which we believe to be a misunderstanding of how stage 2 operates: roughly two-thirds of Street's FY27 net adds sit in LatAm and Rest of World (per the MS/Guggenheim regional splits), yet mix in those regions has been falling, not rising (RoW from 17.2% at Q4-24 to 15.2% at Q2-26; global from 40.8% at Q1-23 to 38.6%). We built a regional premium-mix model off Q2-26 actual mix that decomposes each region's Q1-23 to Q2-26 mix trend into three measured levers plus a residual: (1) offline incentive, the data cost of 2 hours/day of streaming as a ratio of the Premium price (ITU 10GB basket), which fell from 0.83x to 0.45x in LatAm from 2022 to 2025 as 4G population coverage across our EM set reached ~99%, removing the download-to-save-data reason to pay; (2) substitutes, Spotify's share of Spotify + YouTube Music web visits, which fell from 68.5% to 64.9% TTM (Brazil YT Music visits +41% vs. Spotify +20%, and +79% vs. +10% y/y in Sep-26), scaled by Android share since YT Music ships preinstalled on the dominant EM platform (India 95%, Indonesia 89%, Brazil 87%); and (3) affordability, Premium Individual as a % of monthly GNI per capita, where the EM median of 0.60% is 1.9x the developed-market 0.32% (India 4x and Indonesia 5x the US), and where Spotify has already run its stage 3 playbook in reverse by cutting the Standard tier 30% in India (INR 199 to 139), 25% in Indonesia (IDR 79,900 to 59,900) and 25-26% in Saudi Arabia, the UAE and South Africa in Q2-26. Applying base elasticities of 0.05 / 0.5 / -0.4 and crediting 50% of the unexplained historical tailwind (product, bundles, marketing), mix drifts to 37.3% by Q4-27 and 36.6% by FY28 on consensus MAUs, yielding 331M and 345M premium subscribers vs. Street's 339.5M and 364.7M, or 16.7M and 14.3M net adds vs. 24.6M and 24.4M. On a qualitative level, our numbers show that Street underestimates how much of the developed-market funnel was a one-off: LatAm + RoW are 59% of MAUs but 39% of subscribers, Morgan Stanley's build needs RoW mix to climb to 19.6% by FY28 after falling ~200bps in six quarters, and the mature-market cushion is thinning as the share of Spotify Reddit posts carrying cancel/switch language doubled from 1.2% in 2025 to 2.4% in 2026 YTD (net sentiment from -11pp to -18pp) following a 30% cumulative US Individual price increase since Q3-23, with playlist portability and agent-assisted switching lowering the cost of acting on that sentiment. Our 5.3% and 4.3% subscriber growth represents ~250bps and over 300bps delta below Street for FY27 and FY28, a 19M (5.3%) subscriber gap by FY28 worth ~€1.2bn or ~5.6% of FY28 premium revenue at base ARPU, and our bear case (elasticities 0.08 / 0.75 / -0.5 with YT Music share gains at 1.5x their trailing pace) widens the FY28 gap to 43M subscribers, nearly 600bps below Street's two-year subscriber CAGR.

## Paragraph (tight cut, for a slide)

Consensus models ~24.6M and ~24.4M premium net adds in FY27 and FY28 (7.8% and 7.4% y/y), which on consensus MAUs requires global premium mix to hold flat at ~38.5% even though two-thirds of those adds sit in LatAm and Rest of World, where mix is falling (RoW 17.2% at Q4-24 to 15.2% at Q2-26), which we believe to be a misunderstanding of how stage 2 operates outside the US and EU. We built a regional mix model off Q2-26 actuals that decomposes each region's mix trend into three measured levers: offline incentive (data cost of 2 hrs/day streaming fell from 0.83x to 0.45x of the Premium price in LatAm, 2022-25), substitutes (Spotify's share of Spotify + YouTube Music web visits fell from 68.5% to 64.9% TTM, scaled by 87% / 82% Android exposure in LatAm / RoW), and affordability (Premium is 0.60% of monthly income in EMs vs. 0.32% in developed markets, with Spotify already cutting the Standard tier 25-30% in India, Indonesia, Saudi Arabia, the UAE and South Africa in Q2-26). At base elasticities, mix drifts to 36.6% by FY28, yielding 345M subscribers vs. Street's 364.7M, with net adds of 16.7M / 14.3M vs. 24.6M / 24.4M. Qualitatively, Street misses that the mature-market tailwind that masked these headwinds is fading (cancel/switch language in Spotify Reddit posts doubled to 2.4% of posts in 2026 YTD after a 30% cumulative US price increase since Q3-23) and that Morgan Stanley's build needs RoW mix to climb to 19.6% by FY28 after falling ~200bps in six quarters. Our 5.3% / 4.3% subscriber growth is ~250bps / 310bps below Street for FY27 / FY28, a 19M subscriber gap worth ~€1.2bn (5.6%) of FY28 premium revenue, widening to 43M in our bear case.

## Source map (figure -> model tab)

| Figure | Tab / cell |
|---|---|
| Street net adds 24.58M FY27 / 24.42M FY28 (mean); EoP median 315 / 339.5 / 364.65 | `Totals` rows 27-33 |
| Street y/y sub growth 7.8% / 7.4%; implied mix 38.3% / 38.2% / 38.6% | median EoP subs ÷ consensus MAUs (`RPM` row 4) |
| ~2/3 of Street FY27 net adds in LatAm + RoW | `Proxy` rows 7-12 (blended MS/Guggenheim shares) |
| RoW mix 17.2% (Q4-24) -> 15.2% (Q2-26); global 40.8% (Q1-23) -> 38.6% (Q2-26) | `RPM` row 32; row 43 ÷ row 4 |
| LatAm offline payback 0.83 -> 0.45 (2022 -> 2025) | `Premium Mix Levers` C17:D17 |
| EM 4G coverage median 98.9% (2025) | `Snapshot` O25 |
| Spotify share of SPOT + YT Music visits 68.5% -> 64.9% | `Premium Mix Levers` G21:G22 |
| Brazil TTM visits: YT Music +40.5%, Spotify +19.6%; Sep-26 y/y +79% / +10% | `SPOT vs YT in Brazil` (TTM Oct-24-Sep-25 vs Oct-25-Sep-26) |
| Android share: India 95.3%, Indonesia 89.1%, Brazil 86.7% (2025); LatAm 86.7% / RoW 81.5% exposure | `Android_Annual`; `Premium Mix Levers` I17:I18 |
| Premium % of monthly income: EM median 0.60%, DM median 0.32% (1.89x); India 0.65%, Indonesia 0.85%, US 0.16% | `Snapshot` F6:F26 |
| Standard-tier cuts Q2-26: India -30%, Indonesia -25%, Saudi -25%, UAE -25%, South Africa -26% | `Hike log` (negative "Implied change %" rows); `Historical Market Pricing` rows 62, 69 |
| Base elasticities 0.05 / 0.5 / -0.4; w_tail 0.5; bear 0.08 / 0.75 / -0.5, yt_pace 1.5 | `Premium Mix Levers` C6:E11 |
| Base mix 37.3% Q4-27, 36.6% FY28; subs 331.2M / 345.5M; net adds 16.7M / 14.3M | `RPM` rows 43, 4; `Assumptions` rows 32-50 |
| LatAm + RoW = 59% of MAUs, 39% of subs (Q2-26) | `RPM` rows 8-9, 39, 41 |
| MS RoW subs 77.6M FY28 -> 19.6% of consensus RoW MAUs (395.3M) | `Brokers` F7 ÷ `RPM` AB23 |
| Cancel/switch share 1.2% (2025) -> 2.4% (2026 YTD); net sentiment -11.2pp -> -18.2pp | `DM Data Sentiment` rows 36, 42 |
| US Individual $9.99 -> $12.99 (+30%) since Q3-23 | `Hike log` rows 2-4 |
| 19.1M FY28 gap x 12 x €5.10 ARPU ≈ €1.17bn = 5.6% of FY28 premium revenue (€20.7bn) | `RPM` AB52, AB55 |
| Bear FY28 subs 321.4M (43M below Street); 2-yr CAGR 1.7% vs Street 7.6% | `Premium Mix Levers` row 100 |

## Caveats to resolve before publishing

- The thesis text says ~45% of MAUs are in stage 2 markets; the model's LatAm + RoW bucket is 59% of MAUs. The 59% figure is used above because it is what the model carries; RoW also includes Japan, Australia and other mature markets, so 45% may be the right number for the stage 2 subset specifically.
- "Worsened sentiment in mature markets 2x leading 3 month baseline" is not in the model. The closest model figure is the doubling of cancel/switch language in Reddit posts (1.2% -> 2.4%); the Reddit corpus is not region-tagged, so "mature markets" is an inference from Reddit's US/UK skew.
- Portability / agent-assisted switching has no quantification in the model and is included as a qualitative clause only.
- Street subscriber figures are the broker set as of Aug-Sep 2026 notes; regional splits are a proxy built from MS and Guggenheim only.
