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

### D5 gaps (Aerospace Products, the deepest Part; highest priority)
9. D5 T1: the 29 Jul 2026 Q2 release text on the 2026 module target (1,050 vs 1,200) — one
   globenewswire-restricted search for "1,200 modules".
10. D5 U4: module counts for 2022, 2023, 2024 (Q4 2025 release or call: "757 modules in 2025 vs X in
    2024"); Q1 and Q3 2025 counts.
11. D5 U7/U8: Montréal (LMCES) price; QuickTurn Miami date and price (2021 8-K); what "Orange" is;
    Lisbon size, capacity and opening; GMF AeroAsia and EgyptAir terms (Q2 2026 release/call).
12. D5 U2: 10-K revenue note — any split of Aerospace products revenue (engines vs modules vs parts).
13. D5 U16: securities class action status (court, motion to dismiss) 2025-2026.
14. D5 T5: whether consolidated cost of sales includes Leasing asset-sale costs (10-K segment note).
Correction already applied to chain-map.md: Montréal closing 9 Sep 2024 (not 2023).

## Gap-fill results (orchestrator searches, 2026-10-03; all sec.gov-restricted unless noted)

### Segment table, FY2025 10-K (https://www.sec.gov/Archives/edgar/data/1590364/000162828026012940/ftai-20251231.htm)
| $ thousands | 2023 | 2024 | 2025 |
|---|---|---|---|
| Total revenues | 1,170,896 | 1,734,901 | 2,507,409 |
| Total Adjusted EBITDA | 597,282 | 862,050 | 1,190,922 |
| Aerospace products revenue | 454,970 | 1,079,821 | 1,600,456 |
| MRE Contract revenue | 0 | 0 | 335,788 |
| Aerospace Products Adjusted EBITDA | 160,009 | 380,636 | 671,252 |
| Lease income (Aviation Leasing) | n/r | 234,411 | 235,210 |
| Aviation Leasing Adjusted EBITDA | n/r | 500,062 | 608,912 |
TENSION: an earlier search of the same 10-K returned 2024 lease income of $255,338K; the segment-table
search returned $234,411K. Possibly different lines (total lease income vs segment lease income) or a
search-extraction error. Writers must present the figure with the 10-K as source and note the two readings.

### Consolidated statement of operations, FY2025 (same 10-K)
Revenues: Aerospace products 1,600,456; MRE Contract 335,788; Lease income 235,210; Maintenance
revenue 218,499; Asset sales revenue 106,945; Other 10,511; Total 2,507,409.
Expenses: Cost of sales 1,349,719; Operating expenses 152,541; General and administrative 9,478;
Depreciation and amortization 225,797; Interest expense 247,751. (Net income attributable, tax,
equity-method lines not returned; D10 has quarterly net income figures.)

### FY2022 10-K (https://www.sec.gov/Archives/edgar/data/1590364/000159036423000007/ftai-20221231.htm)
Segment revenues 2022 / 2021: Aviation Leasing 199,040 / 128,328; Aerospace Products 85,113 / 70,800;
Corporate and Other 26,948 / 14,161. Segment Adjusted EBITDA 2022 / 2021: Aviation Leasing 107,556 /
"70,800"; Aerospace Products 27,377 / "70,800"; Corporate and Other (7,277) / (6,356).
Net income (loss) attributable to shareholders: 2022 (220,374); 2021 (128,992) — these years include
the infrastructure businesses (spun off Aug 2022) in discontinued operations, so they are not
comparable with 2023+. CAUTION: the "70,800" repeated three times for 2021 is almost certainly a
search-extraction artefact; treat the 2021 Adjusted EBITDA by segment as NOT retrieved.

### People, auditor, controls, litigation (FY2025 10-K and law-firm case pages)
- 985 full-time employees and independent contractors at 31 Dec 2025; 494 full-time employees in
  Canada, about 71% of them covered by collective bargaining agreements.
- Auditor: Ernst & Young LLP 2016-2025; Audit Committee engaged KPMG LLP for FY2025 effective
  17 Jun 2025. Auditor's report dated 27 Feb 2026 (10-K filing date).
- Audit Committee internal investigation (outside counsel and forensic accountants) into the January
  2025 short-seller reports concluded the allegations of misconduct were "all without merit" (10-K).
- Securities class action: S.D.N.Y. No. 25-cv-00541, Judge Jeannette A. Vargas; class period
  23 Jul 2024 to 21 Jan 2025; defendants' motion to dismiss the amended complaint filed 20 Nov 2025,
  fully briefed and pending (law-firm case pages: ktmc.com, rgrdlaw.com; date of last update not
  visible). The 10-K text returned by search did not describe the case; writers should say the
  filing's own description was not retrieved.
- Allegations as the complaint states them: one-time engine sales reported as MRO revenue; whole
  engine sales presented as module sales; depreciation of engines not on lease lowering reported
  cost of goods sold.

### Facilities and deals (GlobeNewswire, Aviation Week, 10-K)
- LMCES, Montréal: acquired 9 Sep 2024 from Lockheed Martin Canada, total consideration $170.0M,
  526,000 sq ft (10-K says ~500,000 per D5). At closing, Montréal plus Miami gave capacity for 1,350
  CFM56 module overhauls and >500 engine tests per year (GlobeNewswire 9 Sep 2024;
  https://www.globenewswire.com/news-release/2024/09/09/2943296/0/en/FTAI-Aviation-Closes-the-Acquisition-of-LMCES.html;
  Aviation Week "FTAI Aviation Snaps Up LMCES For $170 Million").
- QuickTurn, Miami: assets of iAero Thrust acquired 4 Jan 2023 with Unical Aviation (JV); FTAI bought
  Unical's remaining interest 1 Dec 2023 for $30.3M cash (GlobeNewswire 1 Dec 2023; 10-K).
- QuickTurn Europe (ex-IAG Engine Center, Rome Fiumicino): announced with Q4 2024 results 26 Feb 2025;
  adds capacity for 450 modules (150 engines) per year, taking FTAI's total to 1,800 modules (600
  engines) and >600 engine tests per year; closed 5 Jun 2025, $10.5M for 50%; 200,000 sq ft.
- Orange (California) and Lisbon: 10-K lists both as 100%-owned maintenance sites; no deal terms,
  size or opening date returned. Lisbon "113,000 sq ft, 300+ modules/yr" (chain map, from call
  coverage) remains unverified against a primary source.
- Aviation Week ran "Daily Memo: Will Engine Module Swaps Endure In Leaner Times?" (date not
  returned) — relevant to Part VII framing of the module-exchange model; content not retrieved.

### Equity-method investments (10-K FY2025; 10-Q Q3 2025 note R13)
- Advanced Engine Repair JV: 25%; $15.0M invested Dec 2016, $13.5M more Aug 2019; carrying value
  $22,429K at 31 Dec 2025. UNKNOWN whether this is the Chromalloy PMA joint venture or a separate
  repair-development JV; the 10-K describes the PMA JV only as "a joint venture".
- 2025 Partnership: $151.6M invested in 9M 2025; described as 20% LP in the Q3 2025 10-Q and 19% in
  the FY2025 10-K (TENSION, probably dilution at the final close); carrying value $281,740K at
  31 Dec 2025. FTAI is Servicer.
- QuickTurn Europe: 50%, carrying value $9,987K at 31 Dec 2025.
- Prime Engine Accessories (Bristol, with Bauer): 50%; carrying value not returned.
- Subsidiary list: https://www.sec.gov/Archives/edgar/data/1590364/000162828026012940/ftai12312025exhibit211.htm

### FTAI Power / J&F (10-Q Q2 2026)
- The 10-Q describes "a strategic packaging and distribution joint venture with Jereh Group, a
  global leader in gas turbine mobile packaging, to support the planned 2027 production target of
  100 Mod-1 CFM56 aeroderivative units". Ownership split and consolidation not returned.

### Guidance (Q2 2026 release, 29 Jul 2026, https://www.sec.gov/Archives/edgar/data/1590364/000162828026050622/ftai6302026earningsrelease.htm)
- 2027 Business Segment Adjusted EBITDA guidance $2.3B: Aerospace Products $1.4B, FTAI Power $450M,
  Aviation Leasing $450M (the release text returned confirms $1.4B and "$450 million"; D10 gives
  the full split).
- The "1,200 modules" 2026 figure and the "$88.2M" Q2 2026 Leasing Adjusted EBITDA figure came from
  call-coverage summaries (GuruFocus, Quartr) in the first chain-mapping search; neither was
  returned from the release text. Writers: present 1,050 (Feb 2026 release) as the filed target and
  1,200 as reported by call coverage of the July 2026 call, and treat $88.2M as call coverage.

### Other filing URLs located
- FY2024 10-K: https://www.sec.gov/Archives/edgar/data/1590364/000159036425000006/ftai-20241231.htm
- FY2023 10-K: https://www.sec.gov/Archives/edgar/data/1590364/000159036424000003/ftai-20231231.htm
- DEF 14A 2025: https://www.sec.gov/Archives/edgar/data/1590364/000114036125014179/ny20044314x1_def14a.htm
- Q4/FY2024 release (GlobeNewswire 26 Feb 2025): https://www.globenewswire.com/news-release/2025/02/26/3033379/35538/en/
- Q4/FY2025 release (GlobeNewswire 25 Feb 2026): https://www.globenewswire.com/news-release/2026/02/25/3245051/35538/en/
- FTAI Power launch (30 Dec 2025): https://www.globenewswire.com/news-release/2025/12/30/3211297/35538/en/
