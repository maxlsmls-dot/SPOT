# Audiobooks economics — findings

Model: `analysis/audiobooks_model.py` → `data/SPOT_audiobooks_model.xlsx` (two tabs, Audiobooks_Inputs and Audiobooks_Analysis, live formulas; forecast placeholders for 2026E–2027E are flagged LINK TO MODEL). Identity: N(t) = B(t) + A_gp(t) − C(t). The June 2024 price increase is deliberately outside N.

## 1. The bridge

| €M | 2024 | 2025 | 2026E | 2027E |
|---|---|---|---|---|
| B  bundle saving, net of hand-backs | 150 | 146 | 99 | 99 |
| A_gp  gross profit on paid hours | 2 | 13 | 34 | 54 |
| C  licensing cost on included hours | 190 | 300 | 429 | 558 |
| **N = B + A_gp − C** | **-38** | **-141** | **-297** | **-405** |
| N, bp of group revenue | -24 | -82 | -152 | -190 |
| ΔN y/y, €M (the headwind) | — | -103 | -156 | -109 |
| ΔN y/y, bp | — | -60 | -80 | -51 |
| memo: Jun-24 US price increase, annualized (excluded) | 500 | | | |

Against consensus gross-margin expansion of ~115bp (2026) and ~130bp (2027), audiobooks absorb 70% and 39% of what the Street needs.

## 2. Who clawed it back

| ΔN decomposition, €M | 2025 | 2026E | 2027E |
|---|---|---|---|
| Music publishers reclaim the bundle saving (ΔB) | -4 | -47 | 0 |
| Book publishers paid on consumption (−ΔC) | -110 | -129 | -129 |
| Paid hours offset (ΔA_gp) | +11 | +20 | +20 |
| Net | -103 | -156 | -109 |

Two different rights-holder groups, two different mechanisms. The music publishers' claw-back is contractual: UMPG (Jan-25), Warner Chappell (Feb-25), Kobalt (Aug-25), Sony Music Publishing (Sep-25) and BMG (Oct-25) moved to direct US licences that supersede the bundle rate. The book publishers' claw-back is volumetric: per-title fees and pool payments on consumption that the company reports growing 35–60% a year. The priced channel offsets roughly a sixth of the book-publisher cost growth.

## 3. How each term was sized

**B.** The gross saving is disclosed. Every 6-K and 20-F since Q2-24 states the additional royalties that would be due to the MLC if Premium were not a bundle, cumulative from 1 March 2024. The quarterly increments run at €50-56M from Q4-24 to Q1-26, so the gross discount is about €150M for 2024 (ten months) and €208M for 2025. Billboard's analysis of Spotify's MLC reports gives the same answer independently: at the Q4-23 per-stream rate, Q4-25 streams would have cost $110M against $53.3M paid, a discount of €49M for the quarter versus the filing increment of €50M. Streams in the MLC reports grew between the two quarters, so the direct-licensed publishers have not left the blanket licence: the contingency is gross and the hand-back must be estimated. Five direct deals (UMPG Jan-25, Warner Chappell Feb-25, Kobalt Aug-25, Sony Music Publishing Sep-25, BMG Oct-25) cover an estimated 69% of US mechanicals; restoration is set at 75% because Spotify calls the offset partial and the Warner terms still distinguish bundled from music-only listeners. The remaining independents' share (€64M a year) is what the MLC's amended complaint pursues.

| Filing | Period end | Cumulative €M | Increment €M | Months | €M per month |
|---|---|---|---|---|---|
| 6-K Q2-24 | Jun-24 | 46 | 46 | 4 | 11.5 |
| 6-K Q3-24 | Sep-24 | 94 | 48 | 3 | 16.0 |
| 20-F FY24 | Dec-24 | 150 | 56 | 3 | 18.7 |
| 6-K Q1-25 | Mar-25 | 205 | 55 | 3 | 18.3 |
| 6-K Q2-25 | Jun-25 | 256 | 51 | 3 | 17.0 |
| 6-K Q3-25 | Sep-25 | 308 | 52 | 3 | 17.3 |
| 20-F FY25 | Dec-25 | 358 | 50 | 3 | 16.7 |
| 6-K Q1-26 | Mar-26 | 410 | 52 | 3 | 17.3 |
| 6-K Q2-26 | Jun-26 | 437 | 27 | 3 | 9.0 |

The Q2-26 figure is quoted by Music Ally as €437M; a second reading of the same filing gives €473M. The increment is €27M on the first reading and €63M on the second. Verify in the Q2-26 6-K legal-proceedings note. The 2026E placeholder uses the Q2-25 to Q1-26 average and does not depend on it.

**C.** Anchored on the company's words: 'tens of millions' three months after US launch (Feb-24) and 'hundreds of millions of dollars a year' by Oct-24, set at €190M for 2024 and grown by disclosed consumption growth. Market-share triangulation: 10%–14% of $2.43B US publisher receipts, times 1.4x for non-US markets, gives €301–421M for 2025 against the base €300M. Low/high cases at 80%/125% of base.

**A.** Audiobooks+ reached ~$100M ARR and >1M payers by mid-2026 (ARR per payer ≈ $100/yr, consistent with the $11.99 price and a mix of top-ups). Gross profit assumes paid hours carry the same publisher payments at a 55% cost ratio.

## 4. Residual cross-check (inconclusive, and that matters)

| Period | Incremental content-cost ratio |
|---|---|
| FY24 (royalty component) | 47.8% |
| FY25 (royalty component) | 50.0% |
| 9M-25 (royalty component) | 48.2% |
| H1-26 (content component) | 48.8% |

The incremental ratio sits at 48–50% in every period against a ~66% average, with no visible step in FY25 or H1-26. Read correctly, this does not refute C: music royalties, the bundle saving, marketplace offsets and the Partner Program all move inside the same line, and a €100–150M annual audiobook increase is 7–10% of the €765M FY25 royalty increase. But it does mean the audiobook cost cannot be proven from the P&L alone. The claim rests on the company's own cost phrases, the consumption growth it reports, and the publisher-side confirmations. A former audiobooks lead with the per-title fee and the hours-per-listener figure would turn this from triangulated to measured.

## 5. The add-on test

| Attach measure | Value |
|---|---|
| payers / global subscribers | 0.3% |
| payers / eligible-market subscribers | 0.7% |
| payers / monthly listeners (25% of eligible) | 2.9% |
| payers / monthly listeners (25% of global) | 1.3% |
| Basic-plan opt-out share, US individual (inverse signal) | 15.5% |
| bull-case Music Pro attach assumption | 3.0% |

After a full year of the paid add-on and three years of the feature, fewer than one in a hundred eligible subscribers pays for more hours, while roughly one in six US individual subscribers took a $1 discount to give the feature up. The bull case's 3% Music Pro attach is four to nine times the attach Spotify achieved on its most engaged add-on.

## 6. Decision rules

| Test | Threshold | Result | Verdict |
|---|---|---|---|
| 1. Book publishers' cost (ΔC, €M) grows faster than priced-channel gross profit (ΔA_gp, €M) | ΔC > ΔA_gp in 2025 and 2026 | 2025: ΔC +110 vs ΔA_gp +11; 2026: ΔC +129 vs ΔA_gp +20 | CONFIRMED |
| 2. Music publishers claw back the bundle saving (B falls) | B(2026) < B(2024) | B: 2024 150 → 2025 146 → 2026 99. Gross saving is disclosed (€150M 2024, €208M 2025); five direct deals cover ~69% of US mechanicals; restoration (75%) is an estimate | SUPPORTED |
| 3. Net contribution N is negative by 2026 | N(2026) ≤ 0 | N: 2024 -38, 2025 -141, 2026 -297, 2027 -405 (€M). Negative in every year once the price increase is excluded | CONFIRMED |
| 4. Paid attach is low after a full year | < 1% of eligible subscribers; < 3% of listeners | payers / global subscribers: 0.3%; payers / eligible-market subscribers: 0.7%; payers / monthly listeners (25% of eligible): 2.9%; payers / monthly listeners (25% of global): 1.3% | CONFIRMED |
| 5. C grows faster than Premium revenue | C growth > Premium revenue growth | C +58% / +43% vs Premium revenue +11% / +15% | CONFIRMED |
| 6. Residual cross-check (incremental content-cost ratio) shows an audiobook step | Visible jump in FY25 or H1-26 ratio | FY24 (royalty component): 47.8%; FY25 (royalty component): 50.0%; 9M-25 (royalty component): 48.2%; H1-26 (content component): 48.8%. Flat at 48–50%: inconclusive, bounds C's growth to ~€100–150M/yr | INCONCLUSIVE |
| 7. Market-share triangulation agrees with C(2025) | Base C(2025) inside the triangulated range | C(2025) base 300 vs triangulation 301–421 €M | CHECK |

## 7. Sensitivity (ΔN 2027, bp of group revenue)

| C growth p.a. | restoration 50% | restoration 75% (base) | restoration 75% + MLC loss |
|---|---|---|---|
| 20% | -24 | -24 | -54 |
| 30% | -45 | -45 | -75 |
| 45% | -82 | -82 | -112 |
| 60% | -126 | -126 | -156 |

## 8. What the result means for the pitch

- The audiobook 'margin contribution' the Street absorbed in 2024 was a royalty reclassification worth ~€150M plus a price increase worth ~€500M annualized. Audiobook consumption itself cost more than the reclassification saved in the same year.
- From 2025 the reclassification is being handed back to the majors' publishers through direct deals while consumption compounds. On base assumptions the net line moves from about −€38M in 2024 to −€405M in 2027, a 60/80/51bp headwind in 2025/2026/2027.
- Spotify's only governors are the hour cap (already 12 h in every market launched since 2024), the per-title triggers, and the pool rate. Audible at $8.99 and Amazon's free book remove the price lever.
- The priced channel is real but small: it funds roughly a sixth of the consumption cost growth and attaches below 1% of eligible subscribers, which is the platform's own evidence against a 3% Music Pro attach.
- Caveats: C is triangulated, not disclosed; the gross bundle saving is disclosed but the restoration factor on the direct deals is an estimate; the residual method is silent. The direction survives every sensitivity in section 7; the size ranges from ~30 to ~110bp a year.