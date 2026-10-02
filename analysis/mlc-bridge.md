# MLC data bridge: from Spotify's filings to the bundle-saving term

Purpose: replace the estimated bundle saving in the audiobooks model with the figure Spotify itself discloses, and show exactly how that figure becomes the B term in N = B + A − C. Data file: `data/mlc_contingency.csv`. Model: `analysis/audiobooks_model.py` → `data/SPOT_audiobooks_model.xlsx`, Audiobooks_Analysis section 1.

## 1. What the filings disclose

Since Q2-24 every 6-K and 20-F carries a legal-proceedings note on MLC v. Spotify USA Inc. that states the additional royalties that would be due if the MLC were entirely successful in its claim that Premium is not a bundle. The figure is cumulative from 1 March 2024, the month Spotify began reporting Premium as a bundle.

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

The Q2-24 filing adds that €35M of the €46M relates to April to June 2024, so March 2024 alone was about €11M. From Q3-25 the note adds: "Any liability would be partially offset by direct deals with publishers."

**Q2-26 needs verification.** Music Ally (7 Sep 2026) quotes the Q2-26 figure as €437M. A second reading of the same filing gives €473M, which is also the dollar value of the Q1-26 figure (€410M ≈ $473M), so the two may have been conflated. The increment is €27M on the first reading and €63M on the second. Read the legal-proceedings note in the Q2-26 6-K before quoting either. Nothing in the model depends on it: the 2026E placeholder uses the Q2-25 to Q1-26 average.

## 2. What the increments say

The increment is the bundle discount for the quarter: the difference between what the statutory standalone rate would have required and what Spotify reported at the bundle rate, on the whole US paid-tier base. It ran at €50M to €56M a quarter from Q4-24 through Q1-26, about €17M a month, with no step down when UMPG (Feb-25), Warner Chappell (Mar-25), Kobalt (Sep-25), Sony Music Publishing (Oct-25) or BMG (Nov-25) moved to direct licences.

That tells you the figure is gross. Spotify still reports every paid-tier stream through the MLC at the bundle rate and pays the direct-licensed publishers a negotiated top-up outside the MLC. The "partially offset by direct deals" sentence is Spotify saying the top-ups already paid would count against any MLC award.

So the filings measure the gross saving by year directly:

| | 2024 (10 months) | 2025 | 2026E | 2027E |
|---|---|---|---|---|
| Gross bundle saving, €M | 150 | 208 | 205 | 205 |
| Source | 20-F FY24 | 20-F FY25 less 20-F FY24 | 4 × Q2-25 to Q1-26 average (placeholder, link to model) | flat (placeholder, link to model) |

The Phonorecords IV settlement that permits the bundle rate runs to the end of 2027, which is why 2027E is held flat rather than extended.

## 3. Independent cross-check: Billboard's analysis of Spotify's MLC reports

Billboard compared Spotify's paid-tier reports to the MLC for Q4-23 and Q4-25.

| | Q4-23 | Q4-25 |
|---|---|---|
| Mechanical royalties paid, $M | 97.3 | 53.3 |
| Blended per-stream rate, $ | 0.00068 | 0.00033 |
| Implied streams, bn | 143 | 162 |

At the Q4-23 rate, Q4-25 streams would have cost $110M. Spotify paid $53M. The implied quarterly discount is $57M, or €49M at a Q4-25 rate of 1.16, against the €50M increment in the 20-F for the same quarter. Two sources that share no inputs agree within €1.3M.

The same table settles the gross-versus-net question. Streams in the MLC reports grew by 19bn between the two quarters. If the direct-licensed publishers' works had left the blanket licence, reported streams would have collapsed, not grown. The trade press confirms that independents "continue to be paid royalties with the bundling discount applied via the MLC."

## 4. Hand-back to direct-licensed publishers

| Publisher | Announced | Start month used | Est. share of US mechanicals | Months on deal, 2025 |
|---|---|---|---|---|
| UMPG | 26 Jan 2025 | Feb-25 | 22% | 11 |
| Warner Chappell | 6 Feb 2025 | Mar-25 | 13% | 10 |
| Kobalt | 13 Aug 2025 | Sep-25 | 5% | 4 |
| Sony Music Publishing | 18 Sep 2025 | Oct-25 | 26% | 3 |
| BMG | 9 Oct 2025 | Nov-25 | 3% | 2 |
| **Sum** | | | **69%** | |

Shares are estimates from published US publishing market rankings (Sony ranked first in every quarter of 2025). Start months are the month after announcement; effective dates are not disclosed.

Restoration, the share of the discount the direct deals give back, is set at 75% with a 50% to 100% range. The evidence for "partial" rather than "full": Spotify's own word is "partially"; Music Business Worldwide reported that the Warner terms "continue to recognize a difference between bundled and music-only listeners" while payments were "substantially improved"; Kobalt's deal pays "bespoke terms rather than the compulsory licence rates." None of the five contracts is public.

Hand-back(year) = gross saving × Σ(share × months on deal / 12) × restoration.

## 5. The bridge to B and to N

| €M | 2024 | 2025 | 2026E | 2027E |
|---|---|---|---|---|
| Gross bundle saving (disclosed) | 150 | 208 | 205 | 205 |
| Hand-back to direct-licensed publishers | 0 | (62) | (106) | (106) |
| **B  Net bundle saving** | **150** | **146** | **99** | **99** |
| A  Gross profit on paid hours | 2 | 14 | 34 | 54 |
| C  Licensing cost on included hours | (190) | (300) | (429) | (558) |
| **N = B + A − C** | **(38)** | **(141)** | **(297)** | **(405)** |
| Change in N, €M | | (103) | (156) | (109) |
| Change in N, bp of group revenue | | (60) | (80) | (51) |
| of which music publishers (ΔB) | | (4) | (47) | 0 |
| of which book publishers (−ΔC) | | (110) | (129) | (129) |
| of which paid hours (ΔA) | | +11 | +20 | +20 |
| Headwind as share of consensus GM expansion | | | 70% | 39% |

Of the €99M Spotify retains from 2026, about €64M is the independents' share (31% of €205M) and about €35M is the un-restored quarter of the direct-licensed share.

## 6. What changed against the previous version

| | Before | Now | Why |
|---|---|---|---|
| Gross saving 2024 | 158 (run-rate × 10/12) | 150 | 20-F FY24 figure |
| Gross saving 2025 | 189 (13-month run-rate) | 208 | 20-F FY25 less 20-F FY24 |
| Gross saving 2026E | 189 | 205 | Q2-25 to Q1-26 average × 4 |
| Direct deals | 3 majors, 61% | 5 publishers, 69% | Kobalt and BMG added |
| Restoration | 100% | 75% | "partially offset"; bundled vs music-only distinction retained |
| B 2024 / 2025 / 2026E / 2027E | 158 / 118 / 74 / 74 | 150 / 146 / 99 / 99 | |
| N 2024 / 2025 / 2026E / 2027E | (30) / (168) / (322) / (430) | (38) / (141) / (297) / (405) | |
| Headwind 2025 / 2026E / 2027E, bp | (81) / (79) / (51) | (60) / (80) / (51) | |

The 2026E and 2027E headwinds, the two that matter for the hold period, are unchanged. The 2025 headwind is smaller because the gross saving grew with US Premium revenue through 2025 and the hand-back is partial. The level of N is less negative throughout, and still negative in every year.

## 7. Litigation path and the MLC switch

- 16 May 2024: MLC sues Spotify USA Inc. in the Southern District of New York (1:24-cv-03809).
- 29 Jan 2025: dismissed with prejudice; Premium held to be a bundle under the Phonorecords IV definition.
- Sep 2025: reconsideration granted; 1 Oct 2025: amended complaint alleging Spotify used the $9.99 Audiobooks Access price to overvalue the audiobook component and under-report the music share, and that Audiobooks Access is itself a bundle; 8 Oct 2025: jury demand.
- 1 Sep 2026: interlocutory appeal of the bundle ruling denied; Spotify's "unclean hands" defence struck.
- 13 Mar 2027: fact discovery cutoff. No trial date set. Nothing resolves inside the hold period unless the parties settle.

The model's MLC switch zeroes the independents' share of the saving in 2027 (about €64M). It leaves the direct-deal publishers' un-restored share in place, since those terms are contractual. An MLC win on the amended complaint would also create a back-payment on the cumulative figure, which is outside N and would be a one-off below gross profit.

## 8. Verification list before the pitch

1. Open the Q2-26 6-K legal-proceedings note and confirm whether the cumulative figure is €437M or €473M, and whether the wording changed from the Q1-26 note.
2. Tie the other eight figures to the filings linked in `data/mlc_contingency.csv`.
3. Confirm the Billboard figures ($97.3M, $53.3M, per-stream rates) from the article "How Much Have Spotify Bundles Decreased the Mechanical Per-Stream Rate? (Analysis)".
4. Any Tegus transcript from a publisher-side licensing executive that puts a number on the direct-deal top-up relative to the standalone rate replaces the 75% restoration estimate.

## Sources

- Spotify Form 6-K Q2-24, Q3-24, Q1-25, Q2-25, Q3-25, Q1-26, Q2-26 and Form 20-F FY24, FY25: legal-proceedings notes (URLs in `data/mlc_contingency.csv`).
- Billboard, "How Much Have Spotify Bundles Decreased the Mechanical Per-Stream Rate? (Analysis)", 2026.
- NMPA annual meeting, June 2026: nearly $500M lost to Spotify and Amazon bundling since 2024; "nearly $480 million by Spotify's own admission."
- Music Business Worldwide: UMPG deal (26 Jan 2025); Warner Chappell deal (6 Feb 2025); Kobalt deal (13 Aug 2025); Sony Music Publishing deal (18 Sep 2025). Complete Music Update: BMG deal (9 Oct 2025).
- Music Ally, "Court issues mixed ruling in latest Spotify-MLC legal skirmish", 7 Sep 2026. Digital Music News on the discovery schedule.
