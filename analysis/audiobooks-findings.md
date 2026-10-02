# Audiobooks economics — findings

Model: `analysis/audiobooks_model.py` → `data/SPOT_audiobooks_model.xlsx` (live formulas; estimates shaded on the Inputs sheet). Identity: N(t) = B(t) + A_gp(t) − C(t). The June 2024 price increase is deliberately outside N.

## 1. The bridge

| €M | 2024 | 2025 | 2026E | 2027E |
|---|---|---|---|---|
| B  bundle saving, net of hand-backs | 158 | 118 | 74 | 74 |
| A_gp  gross profit on paid hours | 2 | 13 | 34 | 54 |
| C  licensing cost on included hours | 190 | 300 | 429 | 558 |
| **N = B + A_gp − C** | **-30** | **-168** | **-322** | **-430** |
| N, bp of group revenue | -19 | -98 | -165 | -202 |
| ΔN y/y, €M (the headwind) | — | -138 | -153 | -109 |
| ΔN y/y, bp | — | -81 | -79 | -51 |
| memo: Jun-24 US price increase, annualized (excluded) | 500 | | | |

Against consensus gross-margin expansion of ~115bp (2026) and ~130bp (2027), audiobooks absorb 68% and 39% of what the Street needs.

## 2. Who clawed it back

| ΔN decomposition, €M | 2025 | 2026E | 2027E |
|---|---|---|---|
| Music publishers reclaim the bundle saving (ΔB) | -39 | -44 | 0 |
| Book publishers paid on consumption (−ΔC) | -110 | -129 | -129 |
| Paid hours offset (ΔA_gp) | +11 | +20 | +20 |
| Net | -138 | -153 | -109 |

Two different rights-holder groups, two different mechanisms. The music publishers' claw-back is contractual: UMPG (Jan-25), Warner Chappell (Feb-25) and Sony Music Publishing (Sep-25) moved to direct US licences that reporting describes as nullifying the bundle discount. The book publishers' claw-back is volumetric: per-title fees and pool payments on consumption that the company reports growing 35–60% a year. The priced channel offsets roughly a sixth of the book-publisher cost growth.

## 3. How each term was sized

**B.** Spotify's own 6-K puts the bundle reduction at €205M for the 13 months to March 2025, a run-rate of €189M a year, consistent with the NMPA's $230M first-year figure and Billboard's finding that MLC mechanical payments fell 45% between Q4-23 and Q4-25. Hand-backs assume the three majors' publishers hold ~61% of US mechanicals and that their direct deals restore 100% of the discount; the Billboard series cannot test this because direct-licensed publishers drop out of MLC data. The remaining €74M (independents) is what the MLC's amended complaint is pursuing.

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
| 2. Music publishers claw back the bundle saving (B falls) | B(2026) < B(2024) | B: 2024 158 → 2025 118 → 2026 74 (direct deals reported to nullify the discount; restoration factor is an assumption) | SUPPORTED |
| 3. Net contribution N is negative by 2026 | N(2026) ≤ 0 | N: 2024 -30, 2025 -168, 2026 -322, 2027 -430 (€M). Negative in every year once the price increase is excluded | CONFIRMED |
| 4. Paid attach is low after a full year | < 1% of eligible subscribers; < 3% of listeners | payers / global subscribers: 0.3%; payers / eligible-market subscribers: 0.7%; payers / monthly listeners (25% of eligible): 2.9%; payers / monthly listeners (25% of global): 1.3% | CONFIRMED |
| 5. C grows faster than Premium revenue | C growth > Premium revenue growth | C +58% / +43% vs Premium revenue +11% / +15% | CONFIRMED |
| 6. Residual cross-check (incremental content-cost ratio) shows an audiobook step | Visible jump in FY25 or H1-26 ratio | FY24 (royalty component): 47.8%; FY25 (royalty component): 50.0%; 9M-25 (royalty component): 48.2%; H1-26 (content component): 48.8%. Flat at 48–50%: inconclusive, bounds C's growth to ~€100–150M/yr | INCONCLUSIVE |
| 7. Market-share triangulation agrees with C(2025) | Base C(2025) inside the triangulated range | C(2025) base 300 vs triangulation 301–421 €M | CHECK |

## 7. Sensitivity (ΔN 2027, bp of group revenue)

| C growth p.a. | restoration 0.5 | restoration 1.0 | restoration 1.0 + MLC loss |
|---|---|---|---|
| 20% | -24 | -24 | -59 |
| 30% | -45 | -45 | -80 |
| 45% | -82 | -82 | -117 |
| 60% | -126 | -126 | -160 |

## 8. What the result means for the pitch

- The audiobook 'margin contribution' the Street absorbed in 2024 was a royalty reclassification worth ~€158M plus a price increase worth ~€500M annualized. Audiobook consumption itself cost more than the reclassification saved in the same year.
- From 2025 the reclassification is being handed back to the majors' publishers through direct deals while consumption compounds. On base assumptions the net line moves from about −€30M in 2024 to −€430M in 2027, a 81/79/51bp headwind in 2025/2026/2027.
- Spotify's only governors are the hour cap (already 12 h in every market launched since 2024), the per-title triggers, and the pool rate. Audible at $8.99 and Amazon's free book remove the price lever.
- The priced channel is real but small: it funds roughly a sixth of the consumption cost growth and attaches below 1% of eligible subscribers, which is the platform's own evidence against a 3% Music Pro attach.
- Caveats: C is triangulated, not disclosed; the restoration factor on the direct deals is reported, not quantified; the residual method is silent. The direction survives every sensitivity in section 7; the size ranges from ~30 to ~110bp a year.