# Orchestrator notes — facts gathered outside the dossiers

Each entry: fact, source URL, date gathered. These feed reconciliation and the writers; they are
not a dossier.

## MRE Contract revenue with the 2025 Partnership (Strategic Capital)
- Q2 2026: $182.8M of "MRE Contract revenue for the sale and purchase of engines to and from the
  2025 Partnership" (vs $69.6M in Q2 2025). 1H 2026: $404.0M (vs $170.2M in 1H 2025).
- The 10-Q defines MRE Contract revenue as the transaction price for sales of CFM56-5B, CFM56-7B
  and V2500 engines and related modules to the SPVs of the first SCI partnership.
- Source: FTAI 10-Q for the quarter ended 2026-06-30,
  https://www.sec.gov/Archives/edgar/data/0001590364/000162828026051412/ftai-20260630.htm
  (gathered 2026-10-03 via sec.gov-restricted search).
- Bears on: D5 (share of Aerospace Products revenue that is related-party), D7 (unknown U6 on MRE
  volumes to the Partnership), and the reconciliation tension on profit eliminations.

## Search budget
- Subagents share a pool capped at 200 WebSearch calls; it was exhausted during the first wave.
  The orchestrator's own searches still work. Later gap-filling must be done by the orchestrator
  and kept small.

## Gap-fill queue (for the orchestrator's own searches after all dossiers land)
Priority order; each is a single sec.gov-restricted query unless noted.
1. D10 U-1: FY2025 10-K income statement below cost of sales (opex lines, D&A, interest, net income
   attributable) and the Adjusted EBITDA reconciliation for 2023-2025.
2. D10 U-2: FY2021 and FY2022 totals (revenue, net income, Adjusted EBITDA) from the FY2022 10-K
   (https://www.sec.gov/Archives/edgar/data/1590364/000159036423000007/ftai-20221231.htm).
3. D10 U-15/16: Item 1A risk-factor headings; auditor name and ICFR conclusion; class-action status.
4. D10 U-17: employee headcount and properties (Item 2).
5. D7 U1/U2: servicing agreement exhibits (Q2 2026 10-Q ex10.8/10.9) for fee terms, if searchable.
6. D1 U9: current half-life base values for CFM56-7B/-5B (IBA/mba/Cirium).
7. D10 T-4: whether MRE contract revenue sits inside the Aerospace Products segment (segment note).
8. D11 U16: GE Aerospace CFM56 shop-visit and spare-parts pricing statements (2026 calls).
Found en route: FY2022 10-K URL above; Q2 2026 earnings release
https://www.sec.gov/Archives/edgar/data/1590364/000162828026050622/ftai6302026earningsrelease.htm
