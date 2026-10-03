# D11 — The peer set, from their own filings

Dossier for the FTAI Aviation deep primer. Raw material for the writer; not the primer. Posture:
describe, do not opine. All figures carry their source. Searches were restricted to sec.gov for the
eight SEC filers and to the companies' own sites for the three non-SEC filers. WebFetch was blocked, so
each figure is what the search engine returned from the cited filing; where a figure is computed from
two filing figures it is marked **derived**. Nothing is averaged, nothing is chosen between.

Fiscal years in this dossier: WLFC, AER, AL, ASLE, SARO, GE, Safran, MTU, Lufthansa Technik all report
calendar 2025 (year ended 31 Dec 2025). HEICO's FY2025 ended 31 Oct 2025. AAR's FY2026 ended 31 May 2026.
Today is 2026-10-03.

---

## 1. Summary

The peer set spans every link of the chain FTAI sits in: engine lessors (Willis Lease, AerCap's engine
book and its Shannon Engine Support JV), aircraft lessors (AerCap, Air Lease), the parts makers (HEICO for
PMA, AerSale for used material, AAR for distribution), the independent engine MROs (StandardAero, MTU
Maintenance, Lufthansa Technik) and the OEM itself (GE Aerospace, with Safran as CFM partner). Numbers
that bind the set, each from the latest annual filing: Willis Lease owned 363 engines and 20 aircraft at
31 Dec 2025 with 84.9% average utilisation and $730.2M revenue; AerCap owned 470 engines (9% of its fleet)
and booked $7,369M of lease revenue, of which $690M was maintenance rents; Air Lease's 490 owned aircraft
averaged 4.9 years and it was taken private on 8 Apr 2026; HEICO's Flight Support Group earned $750.4M
operating income on $3,117.3M sales (24.1% derived) while adding 400–550 PMAs a year; AerSale's Asset
Management Solutions segment earned $74.1M gross profit on $211.6M; StandardAero's Engine Services
segment earned $706.9M adjusted EBITDA on $5,354.0M (13.2%); AAR's Parts Supply segment was about 45% of
$3,308.0M (derived) of sales; GE Aerospace's Commercial Engines & Services segment earned $8,861M
(26.6%) on $33,314M, of which services were $25,010M (75.1% derived). Non-SEC context: MTU's commercial
MRO ran at 8.0% adjusted EBIT margin on €6.0B, Lufthansa Technik at 7.5% on €8.049B, and Safran's
Propulsion services were 64.6% of segment revenue with a CFM56 installed base above 22,800 engines.

---

## 2. Mechanics: how to read a peer filing against FTAI

### 2.1 Mapping FTAI's activities to the peers

FTAI has two reportable segments and two newer platforms (chain-map, from the FY2025 10-K). The peer
set is chosen so that each FTAI activity has at least one company whose filing isolates the same
activity:

| FTAI activity | What money is made from | Peer whose filing isolates it |
|---|---|---|
| Aviation Leasing (243 engines, 47 aircraft at 31 Dec 2025) | Lease rent, maintenance reserves, gains on sale | Willis Lease (engines), AerCap and Air Lease (aircraft) |
| Aerospace Products: Module Factory, engine and module sales | Shop-visit work sold as refurbished modules and engines | StandardAero Engine Services, MTU Maintenance, Lufthansa Technik Engine Services, GE CES services |
| Aerospace Products: PMA via Chromalloy JV | Parts sold below OEM list | HEICO Flight Support Group |
| Aerospace Products: used material and part-out | Teardown and USM sales | AerSale Asset Management Solutions, AAR Parts Supply, AerCap Materials |
| Strategic Capital (third-party vehicles) | Fees and maintenance work on managed assets | Willis Lease third-party managed engines (116), AerCap managed fleet |
| FTAI Power (CFM56 cores as generator sets) | New demand sink for cores | No peer in this set; GE Vernova and others are covered in D8 |

### 2.2 Lessor metrics

**Lease rate factor (LRF)**: monthly rent divided by the asset's value, quoted as a percentage. It is
the single number lessors use to compare leases across assets of different value. A $8.0M engine at an
LRF of 1.0% earns $80,000 a month, $960,000 a year, which is a 12.0% gross annual yield before
depreciation, interest and maintenance cost. Willis Lease's 10-K was searched for its disclosed LRF;
the search did not return it (Unknown U1). What the filing does give is enough to work an implied
yield:

- Worked example (derived, illustration only). Willis Lease's 2025 lease rent revenue was $291.6M
  [S1]. Its operating-lease equipment at year-end was $2,801.7M [S1]. $291.6M / $2,801.7M = 10.4% on the
  year-end book. Average portfolio utilisation was 84.9% [S1], so on average 15.1% of the book earned
  no rent. 10.4% / 0.849 = 12.3% on the on-lease portion, which corresponds to an LRF of roughly 1.0%
  a month. This uses year-end rather than average book value, so it is only an approximation of the
  filing's own LRF.

**Utilisation**: the share of the lease portfolio, by book value, that is on lease over the period.
Willis Lease: 84.9% in 2025 against 82.9% in 2024 [S1]. The complement is engines in the shop, in
transition between lessees, or held for sale.

**Maintenance reserves and maintenance rents**: a lessee pays the lessor an amount per flight hour or
cycle, set so that by the next shop visit the accumulated reserve covers it. The lessor holds the cash
as a liability and recognises revenue when it determines the reserve will not be paid back (typically
when a lease ends with reserves unspent, or under a lease where reserves are non-reimbursable). AerCap
reports this as "maintenance rents and other receipts", $690M in 2025 against basic lease rents of
$6,679M [S4]. Willis Lease reports "core lease rent and maintenance reserve revenues" together,
$523.6M in 2025 [S1]; subtracting the $291.6M lease rent gives **$232.0M of maintenance reserve
revenue (derived)**, which is 44% of the combined line. For a mid-life engine lessor the maintenance
reserve line is large relative to rent because the assets are near shop visits.

**Gain on sale of leased equipment**: lessors sell engines and aircraft from the portfolio, and the
difference between sale price and net book value is a gain. Willis Lease: $54.0M in 2025, up 19.9%
[S1]. This line is where a lessor realises the value of the "sum of the modules" of a mid-life engine
(D3 covers part-out economics).

**Lease yield for aircraft lessors**: Air Lease discloses lease rental revenue of $2,615.4M for 2025 and
a net book value of flight equipment subject to operating lease of $29.1B at 31 Dec 2025 [S6].
$2,615.4M / $29,100M = **9.0% gross yield on year-end book (derived)**. New-technology aircraft leased
long carry lower LRFs than mid-life engines; this is why Air Lease's implied yield sits below the
Willis Lease figure worked above.

### 2.3 Engine MRO metrics

**Shop visit**: the removal of an engine from the wing and its induction into a repair shop, where it is
disassembled to the module level (fan, booster, high-pressure compressor, combustor, high-pressure
turbine, low-pressure turbine), inspected, repaired and reassembled. D1 and D2 cover the cost build. In
a peer filing a shop visit shows up as revenue when the engine is redelivered, with cost of revenue
dominated by material (OEM new parts, PMA, used serviceable material) and labour.

**Workscope**: the list of modules to be opened and the depth of work on each. GE's 10-K attributes its
2025 services growth to "internal shop visit volume and workscopes" [S14], meaning more visits and
deeper work per visit.

**Segment Adjusted EBITDA versus segment operating income versus adjusted EBIT**: the three MRO peers
report margin on three different bases. StandardAero reports Segment Adjusted EBITDA (before
depreciation and amortisation, and before items it defines as non-recurring). HEICO reports segment
operating income (after D&A). MTU and Lufthansa Technik report adjusted EBIT (after D&A, before
purchase-price-allocation effects and other adjustments). GE reports "segment profit", its own
definition, which excludes certain corporate and non-operating items. These are not interchangeable:
an EBITDA margin will always be higher than an EBIT margin for the same business by the D&A share of
revenue.

- Worked example. StandardAero Engine Services: $706.9M / $5,354.0M = 13.2% Adjusted EBITDA margin
  [S10]. MTU commercial MRO: €478M / €6.0B = 8.0% adjusted EBIT margin [S17]. Lufthansa Technik:
  €603M / €8.049B = 7.5% adjusted EBIT margin on the whole company [S19]. FTAI Aerospace Products,
  Q2 2026: $249.7M / $875.0M = 28.5% Adjusted EBITDA margin (chain-map, from the 29 Jul 2026 release).
  The StandardAero and FTAI figures are both EBITDA-based; the MTU and LHT figures are EBIT-based; and
  FTAI's segment sells refurbished modules and engines rather than labour-and-material shop visits
  priced to a customer, so even the EBITDA pair is not an identical activity.

**Long-term service agreement (LTSA)**: a contract under which an OEM or MRO is paid per flight hour
over many years to keep an engine serviceable. Revenue is recognised on an estimate of total contract
profitability, and a change in that estimate flows through current-period profit. GE's 2025 CES profit
was reduced by "an unfavorable change in estimated profitability of long-term service agreements,
primarily from the estimated impact from tariffs" [S14].

### 2.4 Parts metrics

**PMA (Parts Manufacturer Approval)**: an FAA approval that lets a company other than the OEM design and
make a replacement part. D4 covers the approval mechanics. In HEICO's filing the measure of PMA activity
is throughput of approvals: "approximately 400 to 550 Parts Manufacturer Approvals per year" [S8].
HEICO describes itself as "the largest independent supplier of non-OEM jet engine and aircraft
component replacement parts" and says the parts are "sold at lower prices than OEM-manufactured
parts" [S7, S8]. The 10-K was searched for a stated percentage discount and a total part count; the
search did not return either (Unknown U5).

**USM (used serviceable material)**: parts removed from retired or part-out engines, inspected and
re-certified as serviceable, sold at a discount to new. AerSale's Asset Management Solutions segment is
the cleanest listed example: it buys "feedstock" (whole aircraft and engines) and either leases or sells
them whole or disassembles them for USM [S11]. The economics are a gross-margin story:

- Worked example (derived). AerSale AMS 2025: gross profit $74.1M on sales of $211.6M = 35.0% gross
  margin. 2024: gross profit $82.5M ($74.1M + $8.4M) on sales of $215.5M ($211.6M + $3.9M) = 38.3%.
  The filing attributes the decline to "lower margin on USM sales resulting from changes in the product
  mix" [S11], and reports aircraft gross margin specifically at 33.2% in 2025 against 34.8% in 2024.

**Distribution**: selling new OEM parts under a distribution agreement, holding inventory and earning
a margin between OEM transfer price and sale price. AAR's Parts Supply segment combines distribution of
new OEM parts with USM sales and leasing [S13]. Distribution margins are structurally thinner than PMA
or USM margins because the OEM sets the cost of goods.

### 2.5 Cautions before comparing anything

1. Three fiscal calendars (Dec, Oct, May). AAR's FY2026 (to May 2026) overlaps FTAI's 2H 2025 and
   1H 2026.
2. Five margin definitions (Segment Adjusted EBITDA, segment operating income, adjusted EBIT, GE
   segment profit, gross profit).
3. Different units for "fleet": AerCap counts owned, managed and on-order assets together in one
   headline and owned engines separately; Willis Lease counts owned and third-party-managed engines
   separately. See Tension T1.
4. FTAI's own figures used for reference here are Q2 2026 (segment) and 31 Dec 2025 (fleet), from the
   chain-map; the peers are full-year 2025 unless stated.

---

## 3. Market structure and players

### 3.1 Willis Lease Finance Corporation (NASDAQ: WLFC)

**What it does in the chain.** Owns commercial jet engines, and a small number of aircraft, and leases
them to airlines and MROs; collects maintenance reserves; sells engines and parts out of the portfolio;
manages engines for third parties. It is the only US-listed company whose primary business is engine
leasing, which makes it the closest filing analogue to FTAI's Aviation Leasing segment.

**Latest 10-K (FY2025, year ended 31 Dec 2025)** [S1]:
- Total revenue $730.2M, up 28.3%; net income attributable to common shareholders $108.1M, up 3.5%.
- Adjusted EBITDA $459.1M, up 16.6%. $459.1M / $730.2M = 62.9% of revenue (derived; a lessor's EBITDA
  margin is high because depreciation and interest are the main costs and sit below EBITDA).
- Operating lease portfolio at 31 Dec 2025: $2,801.7M of equipment held for lease, $139.9M notes
  receivable, $30.6M maintenance rights, $16.6M investments in sales-type leases; representing 363
  engines, 20 aircraft, one marine vessel and other leased parts and equipment, with 69 lessees in 37
  countries.
- Third-party managed: 116 engines and related equipment at 31 Dec 2025.
- Average portfolio utilisation 84.9% (2024: 82.9%).
- Core lease rent and maintenance reserve revenues $523.6M, up 15.8% from $452.1M.
- Lease rent revenue $291.6M, up 22.4% from $238.2M.
- Gain on sale of leased equipment $54.0M, up 19.9%.
- A 10-K/A for FY2025 was also filed [S2]; its subject was not returned by the search.

**Most recent 10-Q.** The search returned the Q3 2025 10-Q [S3] and the Q1 2026 and Q2 2026 earnings-call
8-K exhibits by URL [S3a, S3b], but no figures from them. The Q2 2026 10-Q itself was not located
(Unknown U2).

**CFM56 and LEAP exposure, lease rate factor, maintenance services revenue.** Searched for in the 10-K;
not returned (Unknowns U1, U3). The filing's revenue lines that were returned (lease rent, maintenance
reserve, gain on sale) do not include a separately stated "maintenance services" or "spare parts and
equipment sales" figure for 2025, although the Q3 2025 10-Q's title text references "spare parts and
equipment sales" and "maintenance reserve revenue" as line items [S3].

**Comparable to FTAI.** Engines owned (363 WLFC vs 243 FTAI at 31 Dec 2025, chain-map), utilisation
(84.9% WLFC; FTAI's figure is in D6 if disclosed), maintenance reserve revenue (derived $232.0M WLFC),
third-party managed engines (116 WLFC vs FTAI's SCI vehicles, D7).

### 3.2 AerCap Holdings N.V. (NYSE: AER)

**What it does in the chain.** The largest aircraft lessor by fleet, and also a large engine lessor
directly and through Shannon Engine Support (SES), a 50% joint venture with Safran Aircraft Engines
that leases CFM engines [S5]. It also owns helicopters and runs AerCap Materials, its part-out and
used-material arm. AerCap files a Form 20-F (foreign private issuer), not a 10-K, and interim results
on Form 6-K.

**Latest 20-F (FY2025)** [S4] and Q4 2025 earnings release [S4a]:
- Total revenues and other income $8,517M (2024: $7,997M), up 7%.
- Net income attributable to AerCap $3.8B (2024: $2.1B). The drivers of the increase were not returned
  (Unknown U7).
- Total lease revenue $7,369M = basic lease rents $6,679M + maintenance rents and other receipts $690M.
- Portfolio at 31 Dec 2025: 3,500 aircraft, engines and helicopters owned, managed or on order.
- Owned engines at 31 Dec 2025: 470, stated as 9% of the fleet.
- Average age of owned passenger aircraft 7.3 years (new-technology 5.4 years; current-technology
  15.2 years); average remaining contracted lease term 7.1 years.
- Net book value mix of passenger and freighter aircraft at 31 Dec 2025: A320neo family 37%, 787 20%,
  A350 8%, 737NG 8%, A320ceo family 7%. The three narrowbody families listed sum to 52% of NBV
  (derived); the 737 MAX share was not among the returned lines (Unknown U8).
- Accounting note on extensions: when a lease is extended, remaining rentals are recorded straight-line
  over the remaining original term plus the extension [S4].

**Q3 2025 6-K (nine months to 30 Sep 2025)** [S5]:
- 1,988 aircraft owned, managed or on order; over 1,200 engines including engines owned and managed by
  SES; over 300 owned helicopters; total assets $72B at 30 Sep 2025.
- Lease rental income recognised from SES: $155M for the nine months.

**Most recent interim.** The Q1 2026 interim report (quarter ended 31 Mar 2026) was located by URL [S4b];
no figures were returned.

**Engine leasing, AerCap Materials, lease yields, mid-life values and extensions.** The 20-F was
searched for AerCap Materials revenue, an engine-leasing revenue split, a stated lease yield or net
spread, and statements on mid-life aircraft values or extension rates; the search returned none of
these (Unknowns U6, U7). The one hard statement on current-technology aircraft is the age split above:
AerCap's current-technology owned fleet averaged 15.2 years at 31 Dec 2025, which is the age band FTAI's
Strategic Capital vehicles buy (chain-map).

**Comparable to FTAI.** Owned engines (470 AER vs 243 FTAI), maintenance rents ($690M AER, which is
9.4% of lease revenue, derived), the SES structure as a model of OEM-partnered engine leasing, and the
current-technology fleet age.

### 3.3 Air Lease Corporation (formerly NYSE: AL; now Sumisho Air Lease Corporation)

**What it does in the chain.** Buys new aircraft directly from Airbus and Boeing and leases them to
airlines; its filing describes the strategy as purchasing "modern, fuel-efficient new technology
commercial jet aircraft" [S6]. It sits at the opposite end of the fleet-age spectrum from FTAI's
Leasing and Strategic Capital activities, which buy mid-life 737NG and A320ceo aircraft.

**Latest 10-K (FY2025)** [S6]:
- Owned fleet 490 aircraft; managed fleet 45 aircraft; weighted-average fleet age 4.9 years;
  weighted-average remaining lease term 7.2 years, all at 31 Dec 2025.
- Net book value of flight equipment subject to operating lease $29.1B at 31 Dec 2025.
- Lease rental revenue $2,615.4M (2024: $2,407.5M).
- Implied gross lease yield on year-end book: 9.0% (derived, see 2.2).

**Take-private.** The 10-K states that on 8 Apr 2026 Air Lease completed a merger under an Agreement
and Plan of Merger dated 1 Sep 2025, with the company becoming Sumisho Air Lease Corporation [S6]. A
10-K/A for FY2025 was filed afterwards [S6a]; its content was not returned. An 8-K from 2025 [S6b] and
an 8-K dated 1 Jul 2025 [S6c] were returned by URL only. The identity of the acquiring consortium
beyond the surviving name "Sumisho" was not returned by the search and is not stated here (Unknown U9).
The practical consequence for a peer set is that Air Lease's FY2025 10-K is likely its last annual
filing as a public registrant; any later comparison would need the acquirer's disclosures.

**Lease yields, fleet age policy, engine availability.** Fleet age is disclosed (4.9 years). A stated
lease yield and any statement on engine availability were searched for and not returned (Unknown U10).
Total revenues and pre-tax margin were not returned (Unknown U10).

**Comparable to FTAI.** Only loosely: the derived 9.0% yield on new aircraft is a reference point for
the yield on mid-life assets in D6; the fleet age (4.9 years) is the contrast case to AerCap's 15.2-year
current-technology fleet and FTAI's mid-life focus.

### 3.4 HEICO Corporation (NYSE: HEI)

**What it does in the chain.** Two groups: Flight Support Group (FSG), which "designs, manufactures,
repairs, overhauls and distributes jet engine and aircraft component replacement parts, which are
approved by the FAA", using "proprietary technology to design and manufacture jet engine and aircraft
component replacement parts for sale at lower prices than those manufactured by OEMs" [S7]; and the
Electronic Technologies Group, which is outside this chain. FSG is the listed proxy for the PMA business
FTAI runs through its Chromalloy joint venture.

**Latest 10-K (FY2025, year ended 31 Oct 2025)** [S7, S8] and Q4 FY2025 earnings release of 18 Dec 2025
[S7a]:
- FSG net sales $3,117.3M, up 18% from $2,639.4M.
- FSG operating income $750.4M, up 27% from $593.1M.
- FSG operating margin: $750.4M / $3,117.3M = 24.1% (derived); FY2024: $593.1M / $2,639.4M = 22.5%
  (derived).
- PMA throughput: "adding new products to its line at a rate of approximately 400 to 550 Parts
  Manufacturer Approvals per year".
- Customers: commercial airlines and air cargo carriers, repair and overhaul facilities, OEMs, and US
  and foreign governments.

**Most recent 10-Q.** The Q1 FY2026 earnings release (quarter ended 31 Jan 2026) was located by URL [S7b];
no figures were returned. The Q3 FY2026 10-Q (quarter ended 31 Jul 2026) was not located (Unknown U4).

**PMA pricing, part count, acceptance.** The 10-K was searched for a stated discount to OEM price, a
cumulative PMA count and statements about airline or lessor acceptance of PMA; the search returned
only the qualitative "lower prices" language and the 400–550 approvals-per-year rate (Unknown U5). The
consolidated HEICO totals (net sales, operating income) were not returned (Unknown U5).

**Comparable to FTAI.** FSG is a PMA, repair and distribution business combined; FTAI's PMA activity is a
joint venture whose revenue is not separately disclosed (D4, D5). The comparable metric is the FSG
operating margin (24.1% derived) as the margin a mature PMA-led parts business earns after D&A.

### 3.5 AerSale Corporation (NASDAQ: ASLE)

**What it does in the chain.** Two segments: Asset Management Solutions (AMS), "comprised of activities
that extract value from strategic asset acquisitions either as whole assets or by disassembling for
used serviceable material", and Technical Operations (TechOps), "MRO activities for aircraft and their
components, and product sales of internally developed engineered solutions" [S11]. AMS is the listed
proxy for the teardown and USM link of the chain (D3).

**Latest 10-K (FY2025)** [S11, S12] and FY2025 earnings release of 5 Mar 2026 [S12a]:
- Total revenue $335.3M, down 2.8% from $345.1M.
- AMS sales $211.6M, down $3.9M (1.8%). AMS gross profit $74.1M, down $8.4M (10.2%). AMS gross margin
  35.0% (derived) against 38.3% in 2024 (derived).
- Within AMS, aircraft gross margin 33.2% (2024: 34.8%), attributed to lower margin on USM sales from
  product-mix changes.
- Engine revenue rose on higher USM sales (+$34.0M) and higher leasing revenue (+$7.5M), "primarily
  attributable to greater activity in the PW4000 and CF6-80 product lines as the company continues to
  monetize its feedstock". These are widebody engines; the CFM56 is not named in the returned text.
- TechOps revenue: $89.7M for the nine months to 30 Sep 2025 [S12]. Full-year TechOps = $335.3M −
  $211.6M = $123.7M (derived, on the assumption the two segments sum to consolidated revenue without
  eliminations; the filing's own figure was not returned).
- Q4 2025: feedstock acquisitions $15.4M; flight equipment sales of four engines (Q4 2024: six).
- Net income: the 2024 figure was returned ($5.9M GAAP net income); the 2025 figure was not (Unknown U11).

**Most recent 10-Q.** The Q2 2026 10-Q (quarter ended 30 Jun 2026) was located by URL [S12b]; no figures
were returned (Unknown U11).

**Feedstock and retirement scarcity.** The filing language returned frames supply as "feedstock" that
the company "continues to monetize". A statement on retirement scarcity (fewer aircraft retiring, so
less feedstock) was searched for and not returned (Unknown U12). The Q4 feedstock figure ($15.4M) is the
only purchase-volume number returned; a full-year total was not (Unknown U12).

**Comparable to FTAI.** The AMS gross margin (35.0% derived) is the only listed margin for a pure
teardown-and-USM business. FTAI does not report a USM line; its used-material activity is inside
Aerospace Products (D5).

### 3.6 StandardAero, Inc. (NYSE: SARO)

**What it does in the chain.** An independent engine MRO with two segments: Engine Services (engine
shop visits across commercial, business-aviation and military platforms) and Component Repair Services
(CRS, piece-part repair). It IPO'd in Oct 2024 [S10c]. Engine Services is the listed proxy for the
shop-visit link (D2); its CFM56 Center of Excellence is a direct capacity competitor to FTAI's Module
Factory.

**Latest 10-K (FY2025)** [S10]:
- Engine Services revenue $5,354.0M, up $709.3M (15.3%) from $4,644.7M. Segment Adjusted EBITDA $706.9M,
  up $96.0M (15.7%) from $610.9M; margin 13.2% (2024: $610.9M / $4,644.7M = 13.2%, derived).
- CRS revenue $708.6M, up $116.2M (19.6%) from $592.4M. Segment Adjusted EBITDA $202.7M; margin 28.6%.
- Sum of segments: $6,062.5M revenue, $909.6M segment Adjusted EBITDA (derived; consolidated figures
  after eliminations and corporate costs were not returned, Unknown U13).
- Stated drivers of Engine Services growth: "ramping volumes from LEAP, CFM56 DFW Center of Excellence,
  and CF34 expansion investments", plus mid-size and super-mid-size business aviation and select
  military transport programs.

**Capacity statements in the 10-K** [S10]:
- A CFM56-dedicated Center of Excellence in Dallas, Texas, opened in the second half of 2024 "to service
  the growing demand on that platform".
- Industrialisation of a LEAP-dedicated overhaul line at the 810,000 sq ft San Antonio, Texas facility
  "is underway with significant progress to date".
- During 2024: test-cell correlations for LEAP-1A and LEAP-1B completed; CAAC maintenance organisation
  approval for LEAP; over 260 LEAP component repairs developed across CRS facilities; first LEAP engines
  inducted for shop visits.

**Most recent 10-Q (Q2 2026, six months to 30 Jun 2026)** [S10a]:
- Net income $177.2M; total revenue approximately $3.2B, up 8.8%; Adjusted EBITDA $433.0M, up 12.3%.
- Implied 1H 2026 Adjusted EBITDA margin: $433.0M / ~$3,200M ≈ 13.5% (derived, on a rounded revenue
  figure).
- Q1 2026 10-Q also located [S10b]; no figures returned.

**Revenue by platform.** Searched for; not returned. The filing names LEAP, CFM56 and CF34 as growth
drivers but the returned text does not give a CFM56 revenue share or shop-visit count (Unknown U13).

**Comparable to FTAI.** Engine Services Adjusted EBITDA margin (13.2%) against FTAI Aerospace Products
Adjusted EBITDA margin (28.5% in Q2 2026, chain-map), with the caveat in 2.3 that the two sell different
things. The CFM56 Dallas facility and LEAP San Antonio line are the capacity-addition data points.

### 3.7 AAR Corp (NYSE: AIR)

**What it does in the chain.** Four segments: Parts Supply (distribution of new OEM parts and sales and
leasing of USM), Repair & Engineering (airframe MRO, component repair, landing gear), Integrated
Solutions (supply-chain and fleet programmes, largely government) and Expeditionary Services [S13].
Parts Supply is the listed proxy for the distribution-plus-USM link.

**Latest 10-K (FY2026, year ended 31 May 2026)** [S13]:
- Sales to commercial customers $2,384.1M (72.1% of consolidated sales); sales to government and
  defense customers $923.9M (27.9%). Consolidated sales $3,308.0M (derived from the two).
- Commercial sales up $408.0M (20.6%) "primarily due to strong demand and volume growth in new parts
  Distribution activities, including from the recent ADI acquisition, which contributed sales of
  $82.2M".
- Parts Supply "accounted for approximately 45% of AAR's sales in fiscal 2026": approximately $1,489M
  (derived).
- Acquisition: American Distributors Holding Co., LLC (ADI), Sept 2025, $137.1M, in Parts Supply.
- Repair & Engineering: organic growth excluding Landing Gear of 8%; "Airframe MRO near capacity with
  strong production efficiency".
- A DEFA14A (additional proxy material) was filed in 2026 [S13b]; its subject was not returned
  (Unknown U14).

**Most recent 10-Q (Q1 FY2027, quarter ended 31 Aug 2026)** [S13a]: located by URL; no figures returned.

**Segment operating income, USM specifically.** Searched for; not returned. The 10-K's returned text
distinguishes "new parts Distribution" from "sales and leasing of USM" inside Parts Supply but gives no
split and no segment operating income (Unknown U14).

**Comparable to FTAI.** AAR's Parts Supply is the scale reference for a parts business that mixes
distribution with USM (~$1.49B derived); FTAI has no distribution business.

### 3.8 GE Aerospace (NYSE: GE)

**What it does in the chain.** The engine OEM. Through CFM International (50/50 with Safran) it makes
the CFM56 and LEAP; its Commercial Engines & Services (CES) segment sells new engines and spare parts
and performs shop visits in its own network and under LTSAs. It is the counterparty FTAI's PMA, USM and
module business competes with on parts and shop visits, and the supplier of the new parts FTAI's Module
Factory consumes.

**Latest 10-K (FY2025)** [S14, S15]:
- CES equipment revenue $8,304M; services revenue $25,010M; total segment revenue $33,314M. Services
  share 75.1% (derived).
- CES segment profit $8,861M; margin 26.6%. Revenue up $6.4B (24%); profit up $1.8B (26%).
- Revenue drivers: "increased spare parts volume, internal shop visit volume and workscopes, increased
  engine deliveries and pricing".
- Profit drivers: "increased spare parts volume, internal shop visit volume and workscopes and improved
  pricing", partially offset by "the impact of higher install engine deliveries, inflation, higher
  growth investment and an unfavorable change in estimated profitability of long-term service
  agreements, primarily from the estimated impact from tariffs".
- Internal shop visit revenue growth: 24%.
- Commercial engine deliveries 2,386 in 2025, including 1,802 LEAP. CES services revenue up 26%;
  commercial engine deliveries up 25%.
- GE Aerospace total: operating profit $9.1B, up 25%; free cash flow $7.7B, up 24% [S14]. Total company
  revenue was not returned (Unknown U15).
- Fleet statement: "The LEAP engine, which entered into service in 2016, is expected in the coming
  years to overtake the mature CFM56 as the industry's largest fleet. This is expected to drive a
  significant increase in shop visits and need for MRO capacity as LEAP engines come due for services."
- Operations: "~1,450 LEAP-1A durability kits" deployed across new production and overhaul shops since
  certification; turnaround times for LEAP, CFM56 and GE90 improved "by over 10% year-over-year in the
  fourth quarter of 2025".

**Most recent 10-Q.** The Q1 2026 earnings release (quarter ended 31 Mar 2026) was returned by URL with
the headline text "services revenue grew 39%" [S14a]. The Q2 2026 10-Q was not located (Unknown U15).

**CFM56 shop visits, spare-parts pricing, material solutions and used-serviceable programmes.** The
10-K text returned names "spare parts volume", "pricing" and "internal shop visit volume and workscopes"
as drivers but gives no CFM56 shop-visit count, no spare-parts price-increase percentage, and nothing on
a CFM56 "material solutions" or used-serviceable-material programme (Unknown U16).

**Comparable to FTAI.** CES services revenue ($25,010M) is the size of the aftermarket pool FTAI's
Aerospace Products ($875.0M in Q2 2026, chain-map) draws from; the 26.6% CES segment profit margin is
the OEM's blended equipment-plus-services margin.

### 3.9 Non-SEC filers, for context only

**Safran (Euronext: SAF).** CFM International's other half. Its FY2025 results presentation (13 Feb 2026)
and 2025 integrated report [S16, S16a] give: Propulsion services revenue €10,122M, 64.6% of Propulsion
revenue (2024: €8,430M, 61.7%), which implies Propulsion revenue of about €15.7B (derived: €10,122M /
0.646); LEAP deliveries 1,802 in 2025, up 28%, with a backlog of more than 12,900 units; an installed
base of around 29,900 civil engines at end-2025 "including more than 22,800 CFM56s", from which Safran
"can expect sustained aftermarket revenue from this fleet until 2030"; LEAP deliveries expected up
around 15% in 2026; and a new LEAP-1A high-pressure turbine blade certified Dec 2024 that "doubles the
on-wing service life of engines operating in harsh environments". Safran states that spare-parts and
services metrics are tracked in USD across CFM56, LEAP and high-thrust engines; the USD spare-parts
growth figure was not returned (Unknown U17). The 1,802 LEAP figure matches GE's 10-K [S14], as it
should, both being the CFM total.

**MTU Aero Engines (Xetra: MTX).** Its FY2025 release (24 Feb 2026) [S17, S17a]: commercial MRO adjusted
revenue €6.0B, up 18% from €5.1B; commercial MRO adjusted EBIT €478M, up 9% from €438M; margin 8.0%
(2024: 8.7%); group adjusted revenue €8.7B, adjusted EBIT €1.35B (margin 15.5%, 2024: 14.0%), adjusted
net income €968M. The margin decline is attributed to "the higher proportion of Geared Turbofan MRO as
well as the costs associated with the ramp-up of our Fort Worth site"; Geared Turbofan MRO was "around
40% of commercial maintenance in 2025". No CFM56 or V2500 share of MRO revenue was returned (Unknown
U17).

**Lufthansa Technik (unlisted; segment of Deutsche Lufthansa AG, Xetra: LHA).** Its FY2025 figures
[S18, S19, S19a]: revenue €8.049B, up 12%, first time above €8B; adjusted EBIT €603M, down 1%; margin
7.5% (2024: 8.5%); the decline attributed to US tariffs, "ongoing cost increases for materials and a
dollar devaluation that was unfavorable". Engine Services "generates almost half" of revenue and is
"set to be a strong growth driver over the next few years, in particular through its maintenance of the
new generation of engines"; Aircraft Component Services is "more than one third". New contracts signed
in 2025: €8.8B, "for the first time evenly distributed across all three regions". No shop-visit count
or CFM56/LEAP capacity figure was returned (Unknown U17).

---

## 4. Numbers

### 4.1 Per-company tables

**Willis Lease Finance (FY2025, 31 Dec 2025)** — source [S1] unless marked

| Item | Figure | Note |
|---|---|---|
| Total revenue | $730.2M (+28.3%) | |
| Net income attributable to common | $108.1M (+3.5%) | |
| Adjusted EBITDA | $459.1M (+16.6%) | 62.9% of revenue, derived |
| Lease rent revenue | $291.6M (+22.4% from $238.2M) | |
| Core lease rent + maintenance reserve revenue | $523.6M (+15.8% from $452.1M) | |
| Maintenance reserve revenue | $232.0M | derived: $523.6M − $291.6M |
| Gain on sale of leased equipment | $54.0M (+19.9%) | |
| Equipment held in operating lease portfolio | $2,801.7M | at 31 Dec 2025 |
| Notes receivable / maintenance rights / sales-type leases | $139.9M / $30.6M / $16.6M | |
| Owned engines / aircraft / other | 363 / 20 / 1 marine vessel | |
| Lessees / countries | 69 / 37 | |
| Third-party managed engines | 116 | |
| Average utilisation | 84.9% (2024: 82.9%) | |
| Implied gross yield on year-end book | 10.4%; 12.3% on-lease | derived, illustration (2.2) |

**AerCap (FY2025, 31 Dec 2025)** — sources [S4], [S4a], [S5]

| Item | Figure | Note |
|---|---|---|
| Total revenues and other income | $8,517M (2024: $7,997M; +7%) | [S4] |
| Net income attributable | $3.8B (2024: $2.1B) | [S4] |
| Total lease revenue | $7,369M | [S4a] |
| of which basic lease rents | $6,679M | [S4a] |
| of which maintenance rents and other | $690M | [S4a]; 9.4% of lease revenue, derived |
| Portfolio (owned, managed, on order) | 3,500 aircraft, engines, helicopters | at 31 Dec 2025 [S4] |
| Owned engines | 470 (9% of fleet) | at 31 Dec 2025 [S4] |
| Engines incl. SES owned and managed | >1,200 | at 30 Sep 2025 [S5] |
| Aircraft owned, managed, on order | 1,988 | at 30 Sep 2025 [S5] |
| Owned helicopters | >300 | at 30 Sep 2025 [S5] |
| Total assets | $72B | at 30 Sep 2025 [S5] |
| SES lease rental income | $155M | 9M 2025 [S5] |
| NBV mix: A320neo / 787 / A350 / 737NG / A320ceo | 37% / 20% / 8% / 8% / 7% | [S4] |
| Avg age owned passenger fleet | 7.3 yrs (new-tech 5.4; current-tech 15.2) | [S4] |
| Avg remaining lease term | 7.1 yrs | [S4] |

**Air Lease (FY2025, 31 Dec 2025)** — source [S6]

| Item | Figure | Note |
|---|---|---|
| Owned / managed aircraft | 490 / 45 | |
| Weighted-average fleet age | 4.9 yrs | |
| Weighted-average remaining lease term | 7.2 yrs | |
| NBV flight equipment on operating lease | $29.1B | |
| Lease rental revenue | $2,615.4M (2024: $2,407.5M) | |
| Implied gross yield on year-end NBV | 9.0% | derived |
| Merger completed | 8 Apr 2026; became Sumisho Air Lease Corporation | agreement dated 1 Sep 2025 |

**HEICO (FY2025, 31 Oct 2025)** — sources [S7], [S7a], [S8]

| Item | Figure | Note |
|---|---|---|
| FSG net sales | $3,117.3M (+18% from $2,639.4M) | |
| FSG operating income | $750.4M (+27% from $593.1M) | |
| FSG operating margin | 24.1% (FY2024: 22.5%) | derived |
| PMA approvals per year | ~400 to 550 | |

**AerSale (FY2025, 31 Dec 2025)** — sources [S11], [S12], [S12a]

| Item | Figure | Note |
|---|---|---|
| Total revenue | $335.3M (−2.8% from $345.1M) | |
| AMS sales | $211.6M (−1.8%) | |
| AMS gross profit | $74.1M (−10.2%) | |
| AMS gross margin | 35.0% (2024: 38.3%) | derived |
| AMS aircraft gross margin | 33.2% (2024: 34.8%) | |
| Engine USM sales change | +$34.0M | PW4000, CF6-80 |
| Engine leasing revenue change | +$7.5M | |
| TechOps revenue, 9M 2025 | $89.7M | [S12] |
| TechOps revenue, FY2025 | $123.7M | derived: $335.3M − $211.6M |
| Q4 2025 feedstock acquisitions | $15.4M | |
| Q4 2025 flight equipment sales | 4 engines (Q4 2024: 6) | |
| Net income 2024 | $5.9M | 2025 not returned |

**StandardAero (FY2025, 31 Dec 2025; 1H 2026)** — sources [S10], [S10a]

| Item | Figure | Note |
|---|---|---|
| Engine Services revenue | $5,354.0M (+15.3% from $4,644.7M) | |
| Engine Services Segment Adj. EBITDA | $706.9M (+15.7% from $610.9M); 13.2% | |
| CRS revenue | $708.6M (+19.6% from $592.4M) | |
| CRS Segment Adj. EBITDA | $202.7M; 28.6% | |
| Sum of segments | $6,062.5M revenue; $909.6M Adj. EBITDA | derived |
| 1H 2026 revenue | ~$3.2B (+8.8%) | [S10a] |
| 1H 2026 Adjusted EBITDA | $433.0M (+12.3%) | [S10a] |
| 1H 2026 net income | $177.2M | [S10a] |
| CFM56 Center of Excellence, Dallas | opened 2H 2024 | |
| LEAP line, San Antonio (810,000 sq ft) | industrialisation underway | |
| LEAP component repairs developed | >260 | during 2024 |

**AAR (FY2026, 31 May 2026)** — source [S13]

| Item | Figure | Note |
|---|---|---|
| Commercial sales | $2,384.1M (72.1%) | +$408.0M, +20.6% |
| Government and defense sales | $923.9M (27.9%) | |
| Consolidated sales | $3,308.0M | derived |
| Parts Supply share of sales | ~45% (~$1,489M) | share stated; dollar figure derived |
| ADI acquisition | Sept 2025, $137.1M; $82.2M sales contribution | Parts Supply |
| Repair & Engineering organic growth ex Landing Gear | 8% | airframe MRO "near capacity" |

**GE Aerospace (FY2025, 31 Dec 2025)** — source [S14]

| Item | Figure | Note |
|---|---|---|
| CES equipment revenue | $8,304M | |
| CES services revenue | $25,010M (+26%) | 75.1% of CES, derived |
| CES total revenue | $33,314M (+$6.4B, +24%) | |
| CES segment profit | $8,861M (+$1.8B, +26%); 26.6% | |
| Internal shop visit revenue growth | 24% | |
| Commercial engine deliveries | 2,386 incl. 1,802 LEAP (+25%) | |
| GE Aerospace operating profit | $9.1B (+25%) | total company |
| GE Aerospace free cash flow | $7.7B (+24%) | |
| LEAP-1A durability kits deployed | ~1,450 | since certification |
| TAT improvement (LEAP, CFM56, GE90) | >10% y/y | Q4 2025 |
| Q1 2026 services revenue growth | 39% | [S14a], headline only |

**Non-SEC (CY2025)** — sources [S16]–[S19a]

| Company | Item | Figure |
|---|---|---|
| Safran | Propulsion services revenue | €10,122M, 64.6% of segment (2024: €8,430M, 61.7%) |
| Safran | Propulsion revenue | ~€15.7B, derived |
| Safran | LEAP deliveries / backlog | 1,802 (+28%) / >12,900 |
| Safran | Civil installed base / CFM56 | ~29,900 / >22,800 |
| Safran | 2026 LEAP delivery outlook | +~15% |
| MTU | Commercial MRO adj. revenue / adj. EBIT / margin | €6.0B (+18%) / €478M (+9%) / 8.0% (2024: 8.7%) |
| MTU | Group adj. revenue / adj. EBIT / margin / adj. net income | €8.7B / €1.35B / 15.5% (2024: 14.0%) / €968M |
| MTU | GTF share of commercial MRO | ~40% |
| Lufthansa Technik | Revenue / adj. EBIT / margin | €8.049B (+12%) / €603M (−1%) / 7.5% (2024: 8.5%) |
| Lufthansa Technik | Engine Services share / Component Services share | "almost half" / "more than one third" |
| Lufthansa Technik | New contracts 2025 | €8.8B |

### 4.2 Comparison table

FTAI reference figures are from the chain-map (FY2025 10-K for fleet; 29 Jul 2026 release for Q2 2026
segment results) and are included only to anchor the columns.

| Company | Ticker | Fiscal year | Revenue | Comparable segment | Segment revenue | Segment margin (basis) | Metrics most comparable to FTAI |
|---|---|---|---|---|---|---|---|
| FTAI Aviation (reference) | FTAI | Q2 2026 / 31 Dec 2025 | $875.0M AP, Q2 2026 | Aerospace Products; Aviation Leasing | $875.0M (Q2) | 28.5% Adj. EBITDA (derived) | 296 modules Q2 2026; 243 engines + 47 aircraft owned |
| Willis Lease Finance | WLFC | 2025 (Dec) | $730.2M | Engine leasing (whole company) | $730.2M | 62.9% Adj. EBITDA (derived) | 363 engines; 84.9% utilisation; $232.0M maintenance reserve rev. (derived); 116 managed engines |
| AerCap | AER | 2025 (Dec) | $8,517M | Lease revenue; engine leasing (SES) | $7,369M lease revenue | not returned (U7) | 470 owned engines; $690M maintenance rents; $155M SES income (9M) |
| Air Lease | AL (delisted 8 Apr 2026) | 2025 (Dec) | not returned (U10) | Aircraft leasing (whole company) | $2,615.4M rental | not returned (U10) | 490 aircraft, 4.9 yrs; 9.0% implied yield (derived) |
| HEICO | HEI | FY2025 (Oct) | not returned (U5) | Flight Support Group | $3,117.3M | 24.1% operating income (derived) | 400–550 PMAs/yr |
| AerSale | ASLE | 2025 (Dec) | $335.3M | Asset Management Solutions | $211.6M | 35.0% gross (derived) | $15.4M Q4 feedstock; 4 engines sold Q4 |
| StandardAero | SARO | 2025 (Dec) | $6,062.5M (sum of segments, derived) | Engine Services | $5,354.0M | 13.2% Segment Adj. EBITDA | CFM56 CoE Dallas; LEAP line San Antonio; >260 LEAP repairs |
| AAR | AIR | FY2026 (May) | $3,308.0M (derived) | Parts Supply | ~$1,489M (derived from 45%) | not returned (U14) | distribution + USM; ADI $137.1M |
| GE Aerospace | GE | 2025 (Dec) | not returned (U15) | Commercial Engines & Services | $33,314M; services $25,010M | 26.6% segment profit | 1,802 LEAP delivered; shop-visit revenue +24%; TAT +10% |
| Safran (context) | SAF | 2025 (Dec) | — | Propulsion services | €10,122M | — | 22,800+ CFM56 installed base |
| MTU (context) | MTX | 2025 (Dec) | €8.7B adj. | Commercial MRO | €6.0B | 8.0% adj. EBIT | GTF ~40% of MRO |
| Lufthansa Technik (context) | — | 2025 (Dec) | €8.049B | Engine Services | "almost half" | 7.5% adj. EBIT (company) | €8.8B new contracts |

---

## 5. Constraints and bottlenecks, as the filings state them

- **Shop capacity.** StandardAero's 10-K describes the Dallas CFM56 Center of Excellence (opened 2H
  2024) and a LEAP line under industrialisation at San Antonio [S10]. GE reports LEAP, CFM56 and GE90
  turnaround times improved by more than 10% year over year in Q4 2025 [S14], a statement that only makes
  sense if turnaround time had been a constraint. AAR says its airframe MRO is "near capacity" [S13].
  MTU cites ramp-up costs at Fort Worth as a margin drag [S17]. Lufthansa Technik frames Engine Services
  as its growth driver "in particular through its maintenance of the new generation of engines" [S19a].
- **Platform mix shifting the margin of independent MROs.** MTU's commercial MRO margin fell from 8.7% to
  8.0% with GTF at about 40% of the work [S17]. Lufthansa Technik's margin fell from 8.5% to 7.5% on
  tariffs, material-cost increases and USD weakness [S19]. StandardAero's Engine Services margin held at
  13.2% in both years [S10].
- **Material cost and tariffs.** GE's CES profit was reduced by an unfavourable change in LTSA
  profitability estimates "primarily from the estimated impact from tariffs" [S14]; Lufthansa Technik
  names US tariffs and material-cost increases [S19].
- **Feedstock for used material.** AerSale's AMS revenue fell 1.8% and its gross margin fell about
  three points on USM mix; its Q4 feedstock purchases were $15.4M and it sold four engines in the quarter
  against six a year earlier [S11, S12a]. The filing's returned text does not make an explicit scarcity
  statement.
- **Installed base as the demand ceiling.** Safran puts the CFM56 installed base above 22,800 engines at
  end-2025 and expects "sustained aftermarket revenue from this fleet until 2030" [S16]. GE expects LEAP
  to overtake CFM56 as the largest fleet "in the coming years" and ties that to "a significant increase in
  shop visits and need for MRO capacity as LEAP engines come due" [S14]. Both set the horizon over which
  the CFM56 shop-visit pool is still growing or flat before it declines.
- **Lessor utilisation.** Willis Lease ran at 84.9% utilisation [S1], meaning roughly one dollar in six
  of its portfolio was off lease on average, which is the inventory a lessor must carry to serve
  short-term engine demand.
- **PMA throughput.** HEICO's 400–550 approvals a year [S8] is the rate at which one PMA maker can expand
  its catalogue; each approval is a separate FAA action (D4).
- **Capital access.** Air Lease's take-private removed one public lessor from the set [S6]; AAR funded a
  $137.1M acquisition into Parts Supply [S13]; AerCap carried $72B of assets at 30 Sep 2025 [S5]. None of
  the returned text gives cost-of-debt figures (Unknown U18).

---

## 6. Tensions

- **T1 — AerCap engine count: >1,200 versus 470.** The Q3 2025 6-K says "over 1,200 engines (including
  engines owned and managed by its Shannon Engine Support JV)" at 30 Sep 2025 [S5]. The FY2025 20-F says
  AerCap "owned 470 engines (9% of fleet)" at 31 Dec 2025 [S4]. The bases differ (owned versus owned plus
  managed plus JV) and the dates differ by a quarter. Both are recorded; neither is chosen. Any
  comparison with FTAI's 243 owned engines should use the 470 figure and say so.
- **T2 — Who is the engine-leasing comparable.** Willis Lease's whole company (363 owned engines) is an
  engine lessor; AerCap's engine book (470 owned) is larger than Willis Lease's yet is 9% of AerCap. The
  filings therefore give two different "largest engine lessor" readings depending on whether the measure
  is owned engines or share of business.
- **T3 — StandardAero margin flat; MTU and LHT margins down.** For the same year, the independent MROs
  moved differently: StandardAero Engine Services 13.2% to 13.2% (Adjusted EBITDA) [S10]; MTU commercial
  MRO 8.7% to 8.0% (adjusted EBIT) [S17]; Lufthansa Technik 8.5% to 7.5% (adjusted EBIT) [S19]. The
  bases differ (EBITDA versus EBIT) and the platform mixes differ (MTU names GTF; LHT names tariffs,
  materials and USD; StandardAero names LEAP, CFM56 and CF34 volume), so the figures cannot be read as
  one trend.
- **T4 — GE's two profit figures.** The 10-K text returned gives CES segment profit of $8,861M and GE
  Aerospace operating profit of $9.1B [S14]. The two are different levels (segment versus total after
  Defense & Propulsion Technologies and corporate items). They are both recorded; the reconciling items
  were not returned.
- **T5 — AerSale TechOps full-year figure.** The 9M 2025 TechOps revenue was $89.7M [S12]; the derived
  full-year figure ($123.7M) assumes the two segments sum exactly to consolidated revenue. The filing's
  own full-year TechOps line was not returned, so the derived figure may differ from it by any
  intersegment eliminations.
- **T6 — StandardAero's consolidated revenue.** The sum of segments is $6,062.5M [S10]; the 1H 2026 10-Q
  reports "approximately $3.2B" up 8.8%, implying 1H 2025 of about $2.94B and therefore 2H 2025 of about
  $3.12B if the FY total were $6,062.5M [S10a]. The consolidated FY2025 figure after eliminations was not
  returned, so this is consistent but unverified.
- **T7 — HEICO and AAR fiscal years versus the calendar-year peers.** HEICO's FY2025 ends 31 Oct 2025 and
  AAR's FY2026 ends 31 May 2026; neither matches the Dec-2025 year of the rest of the set. Growth rates
  across the table are therefore over different twelve-month windows.

---

## 7. Unknowns

Each entry says what was looked for, where, and what would resolve it.

- **U1 — Willis Lease lease rate factor and CFM56/LEAP portfolio split.** Searched the FY2025 10-K [S1].
  Not returned. Resolve: read the 10-K's "Lease Portfolio" and "Market" sections directly.
- **U2 — Willis Lease Q2 2026 10-Q figures.** The Q2 2026 earnings-call 8-K exhibit was located by URL
  [S3b] but no figures came back; the 10-Q itself was not located. Resolve: search "wlfc-20260630".
- **U3 — Willis Lease maintenance services and spare-parts revenue lines for FY2025.** The 10-K's
  revenue table was not returned beyond lease rent, the combined core line and gain on sale. Resolve:
  read the consolidated statement of income in [S1].
- **U4 — HEICO Q3 FY2026 10-Q (quarter ended 31 Jul 2026).** Not located; only the Q1 FY2026 release URL
  [S7b]. Resolve: search "hei-20260731".
- **U5 — HEICO consolidated FY2025 net sales and operating income; PMA cumulative count; stated discount
  to OEM; acceptance statements.** Searched [S7, S7a, S8]. Only FSG figures and the 400–550 PMA rate were
  returned. Resolve: read Item 1 and Item 7 of [S7].
- **U6 — AerCap Materials revenue and AerCap engine-leasing revenue.** Searched the 20-F [S4]. Not
  returned. Resolve: read the 20-F's business description and the segment or revenue note.
- **U7 — AerCap FY2025 net income drivers ($3.8B versus $2.1B) and any stated lease yield or net spread.**
  Not returned. Resolve: read the Q4 2025 earnings release [S4a] in full.
- **U8 — AerCap 737 MAX share of NBV and total narrowbody share.** The five NBV lines returned sum to 80%;
  the remainder was not itemised. Resolve: read the fleet table in [S4].
- **U9 — Air Lease acquiring consortium.** The 10-K text returned names only the surviving entity,
  Sumisho Air Lease Corporation, and the agreement date [S6]. Resolve: read the 1 Sep 2025 merger 8-K.
- **U10 — Air Lease FY2025 total revenues, pre-tax margin, stated lease yield, engine-availability
  statements.** Not returned. Resolve: read Item 7 of [S6].
- **U11 — AerSale FY2025 net income; Q2 2026 10-Q figures.** The Q2 2026 10-Q was located by URL [S12b].
  Resolve: read [S12a] and [S12b].
- **U12 — AerSale full-year feedstock purchases and any statement on retirement scarcity.** Only the Q4
  figure ($15.4M) was returned. Resolve: read the AMS discussion and cash-flow statement in [S11].
- **U13 — StandardAero FY2025 consolidated revenue, net income and Adjusted EBITDA; revenue by
  platform; CFM56 shop-visit count.** Not returned. Resolve: read Item 7 and the segment note of [S10].
- **U14 — AAR segment operating income; USM sales within Parts Supply; subject of the 2026 DEFA14A
  [S13b]; Q1 FY2027 10-Q figures [S13a].** Not returned. Resolve: read the segment note in [S13] and the
  DEFA14A.
- **U15 — GE Aerospace FY2025 total revenue; Q2 2026 10-Q.** Not returned or located. Resolve: read the
  consolidated statement in [S14]; search "ge-20260630".
- **U16 — GE CFM56 shop-visit count, spare-parts price increases, and any "material solutions" or
  used-serviceable-material programme wording.** Not returned from [S14]. Resolve: read the CES segment
  discussion in [S14] and the Q4 2025 and Q2 2026 earnings materials.
- **U17 — Safran USD spare-parts growth; MTU CFM56 and V2500 share of MRO; Lufthansa Technik shop-visit
  count and CFM56/LEAP capacity.** Not returned from [S16]–[S19a]. Resolve: read the Safran URD
  Propulsion section, MTU's annual report segment note, and LHT's annual report.
- **U18 — Cost of debt and funding terms for each lessor.** Not searched for within the budget. Resolve:
  D6 and D10 cover FTAI's; peers' are in their debt notes.

---

## 8. Terms introduced

- **Lease rate factor (LRF)**: monthly rent as a percentage of the asset's value.
- **Utilisation**: share of a lease portfolio, by book value, on lease over a period.
- **Maintenance reserve / maintenance rent**: usage-based payments from lessee to lessor that pre-fund
  the next shop visit; recognised as lessor revenue when determined non-reimbursable.
- **Gain on sale of leased equipment**: sale proceeds less net book value of an asset sold from the
  portfolio.
- **Net book value (NBV)**: cost less accumulated depreciation and impairments.
- **Shop visit**: removal of an engine from the wing and its induction, disassembly, repair and
  reassembly in a repair shop.
- **Module**: one of the engine's major sub-assemblies (fan, booster, HPC, combustor, HPT, LPT) that can
  be removed and replaced as a unit.
- **Workscope**: the list of modules to be opened and the depth of work in a shop visit.
- **Long-term service agreement (LTSA)**: a multi-year per-flight-hour maintenance contract whose
  revenue is recognised against an estimate of total contract profitability.
- **Segment Adjusted EBITDA**: segment profit before depreciation, amortisation and defined
  adjustments, as reported by StandardAero.
- **Adjusted EBIT**: operating profit after D&A, before defined adjustments, as reported by MTU and
  Lufthansa Technik.
- **GE segment profit**: GE Aerospace's segment-level profit measure, excluding certain corporate and
  non-operating items.
- **PMA (Parts Manufacturer Approval)**: FAA approval for a non-OEM company to design and manufacture a
  replacement part.
- **USM (used serviceable material)**: parts removed from retired or part-out engines, inspected and
  re-certified for sale.
- **Feedstock**: whole aircraft or engines bought for leasing, resale or disassembly into USM.
- **Part-out**: disassembly of a whole asset for sale of its parts.
- **Distribution**: resale of new OEM parts under a distribution agreement.
- **Form 20-F / Form 6-K**: the annual and interim SEC forms filed by foreign private issuers such as
  AerCap.
- **Shannon Engine Support (SES)**: AerCap's 50% engine-leasing joint venture with Safran Aircraft
  Engines.
- **Center of Excellence**: StandardAero's term for a single-platform-dedicated shop (Dallas, CFM56).
- **Turnaround time (TAT)**: elapsed time from engine induction to redelivery.
- **Durability kit**: GE's term for a package of upgraded LEAP-1A parts installed at production or in
  overhaul to extend time on wing.

---

## 9. Sources

All sec.gov URLs were returned by sec.gov-restricted WebSearch on 2026-10-03; non-SEC URLs by
company-site-restricted WebSearch on the same date.

- [S1] Willis Lease Finance Corp, Form 10-K for FY ended 31 Dec 2025 (filed early 2026).
  https://www.sec.gov/Archives/edgar/data/1018164/000101816426000036/wlfc-20251231x10k.htm
- [S2] Willis Lease Finance Corp, Form 10-K/A for FY2025.
  https://www.sec.gov/Archives/edgar/data/1018164/000101816426000041/wlfc-20251231.htm
- [S3] Willis Lease Finance Corp, Form 10-Q for quarter ended 30 Sep 2025.
  https://www.sec.gov/Archives/edgar/data/1018164/000101816425000134/wlfc-20250930.htm
- [S3a] Willis Lease Finance Corp, Q1 2026 earnings call 8-K exhibit (2026).
  https://www.sec.gov/Archives/edgar/data/1018164/000101816426000050/wlfcq12026earningscall5-.htm
- [S3b] Willis Lease Finance Corp, Q2 2026 earnings call press release 8-K exhibit (2026).
  https://www.sec.gov/Archives/edgar/data/1018164/000101816426000065/wlfcq22026earningscallpr.htm
- [S3c] Willis Lease Finance Corp, Q4 2025 earnings release 8-K exhibit (early 2026).
  https://www.sec.gov/Archives/edgar/data/1018164/000101816426000030/q42025ex991.htm
- [S4] AerCap Holdings N.V., Form 20-F for FY ended 31 Dec 2025 (filed 2026).
  https://www.sec.gov/Archives/edgar/data/1378789/000162828026007513/aer-20251231.htm
- [S4a] AerCap Holdings N.V., Q4 and FY2025 earnings release, Form 6-K exhibit (early 2026).
  https://www.sec.gov/Archives/edgar/data/1378789/000162828026005942/aercap2025fourthquarterear.htm
- [S4b] AerCap Holdings N.V., interim report for quarter ended 31 Mar 2026, Form 6-K.
  https://www.sec.gov/Archives/edgar/data/1378789/000162828026028212/aer-03312026xinterimreport.htm
- [S5] AerCap Holdings N.V., Form 6-K for quarter ended 30 Sep 2025.
  https://www.sec.gov/Archives/edgar/data/1378789/000162828025047012/aer-09302025x6k.htm
- [S6] Air Lease Corporation, Form 10-K for FY ended 31 Dec 2025 (filed 2026).
  https://www.sec.gov/Archives/edgar/data/1487712/000162828026007707/al-20251231.htm
- [S6a] Air Lease Corporation, Form 10-K/A for FY2025 (2026).
  https://www.sec.gov/Archives/edgar/data/1487712/000119312526197721/d147568d10ka.htm
- [S6b] Air Lease Corporation, Form 8-K (2025).
  https://www.sec.gov/Archives/edgar/data/1487712/000119312525052911/d893487d8k.htm
- [S6c] Air Lease Corporation, Form 8-K dated 1 Jul 2025.
  https://www.sec.gov/Archives/edgar/data/1487712/000162828025033782/al-20250701.htm
- [S6d] Air Lease Corporation, Q4 2025 earnings release exhibit 99.1 (early 2026).
  https://www.sec.gov/Archives/edgar/data/1487712/000162828026007701/ex-991q425.htm
- [S7] HEICO Corporation, Form 10-K for FY ended 31 Oct 2025 (filed Dec 2025).
  https://www.sec.gov/Archives/edgar/data/46619/000004661925000082/hei-20251031.htm
- [S7a] HEICO Corporation, Q4 FY2025 earnings release dated 18 Dec 2025.
  https://www.sec.gov/Archives/edgar/data/46619/000004661925000076/a10312025ex991earningsrele.htm
- [S7b] HEICO Corporation, Q1 FY2026 earnings release (quarter ended 31 Jan 2026).
  https://www.sec.gov/Archives/edgar/data/46619/000004661926000003/a01312026q1ex991earningsre.htm
- [S8] HEICO Corporation, Form 10-K FY2025, Item 1 text on PMA approval rate (same document as S7).
  https://www.sec.gov/Archives/edgar/data/46619/000004661925000082/hei-20251031.htm
- [S10] StandardAero, Inc., Form 10-K for FY ended 31 Dec 2025 (filed 2026).
  https://www.sec.gov/Archives/edgar/data/2025410/000119312526072618/saro-20251231.htm
- [S10a] StandardAero, Inc., Form 10-Q for quarter ended 30 Jun 2026.
  https://www.sec.gov/Archives/edgar/data/0002025410/000202541026000009/saro-20260630.htm
- [S10b] StandardAero, Inc., Form 10-Q for quarter ended 31 Mar 2026.
  https://www.sec.gov/Archives/edgar/data/0002025410/000119312526212553/saro-20260331.htm
- [S10c] StandardAero, Inc., prospectus 424B4 (Oct 2024 IPO).
  https://www.sec.gov/Archives/edgar/data/2025410/000119312524231156/d838237d424b4.htm
- [S11] AerSale Corporation, Form 10-K for FY ended 31 Dec 2025 (filed 2026).
  https://www.sec.gov/Archives/edgar/data/1754170/000110465926025574/asle-20251231x10k.htm
- [S12] AerSale Corporation, Form 10-Q for quarter ended 30 Sep 2025.
  https://www.sec.gov/Archives/edgar/data/1754170/000110465925108481/asle-20250930x10q.htm
- [S12a] AerSale Corporation, FY2025 results press release dated 5 Mar 2026.
  https://www.sec.gov/Archives/edgar/data/1754170/000110465926024101/asle-20260305xex99d1.htm
- [S12b] AerSale Corporation, Form 10-Q for quarter ended 30 Jun 2026.
  https://www.sec.gov/Archives/edgar/data/1754170/000110465926092710/asle-20260630x10q.htm
- [S13] AAR Corp, Form 10-K for FY ended 31 May 2026 (filed Jul 2026).
  https://www.sec.gov/Archives/edgar/data/1750/000110465926085459/air-20260531x10k.htm
- [S13a] AAR Corp, Form 10-Q for quarter ended 31 Aug 2026.
  https://www.sec.gov/Archives/edgar/data/1750/000110465926111786/air-20260831x10q.htm
- [S13b] AAR Corp, DEFA14A (2026).
  https://www.sec.gov/Archives/edgar/data/1750/000110465926093286/tm2622642d1_defa14a.htm
- [S14] General Electric Co (GE Aerospace), Form 10-K for FY ended 31 Dec 2025 (filed 2026).
  https://www.sec.gov/Archives/edgar/data/40545/000004054526000008/ge-20251231.htm
- [S14a] GE Aerospace, Q1 2026 earnings release (Apr 2026).
  https://www.sec.gov/Archives/edgar/data/40545/000004054526000026/ge1q2026earningsrelease.htm
- [S15] GE Aerospace, courtesy PDF of annual report (2026).
  https://www.sec.gov/Archives/edgar/data/40545/000004054526000018/ge-courtesy.pdf
- [S16] Safran, FY2025 Results & Investor Update presentation, 13 Feb 2026.
  https://www.safran-group.com/download/media/450393
- [S16a] Safran, 2025 Integrated Report.
  https://www.safran-group.com/download/media/450817
- [S17] MTU Aero Engines, press release "Figures for 2025: MTU stays on course for growth", 24 Feb 2026.
  https://www.mtu.de/newsroom/press/latest-press-releases/press-release-detail/figures-for-2025-mtu-stays-on-course-for-growth/
- [S17a] MTU Aero Engines, FY2025 results key figures PDF, 24 Feb 2026.
  https://www.mtu.de/fileadmin/DE/5_Investoren/Financial_Report/2025_Results/2026_02_24_MTU_FY_2025_Results_en.pdf
- [S18] Lufthansa Technik, Financial Data & Annual Report page.
  https://www.lufthansa-technik.com/en/financials
- [S19] Lufthansa Technik, press release "Lufthansa Technik stable on course for growth" (FY2025 results,
  early 2026).
  https://www.lufthansa-technik.com/en/lufthansa-technik-stable-on-course-for-growth-2601a780f4c4031c
- [S19a] Deutsche Lufthansa AG, Annual Report 2025, MRO business segment.
  https://report.lufthansagroup.com/2025/annual-report/en/combined-management-report/business-segments/mro-business-segment/
- [Internal] FTAI chain-map, /home/user/SPOT/ftai-primer/research/chain-map.md (FTAI reference figures:
  FY2025 10-K fleet; Q2 2026 release of 29 Jul 2026).

Searches used: 18 of 18.
