# Chain map — FTAI Aviation and the narrowbody engine aftermarket

Phase 1 chain-mapping pass. Built from current evidence (searches run 2026-10-03), not from a prior
about what governs the industry. The purpose is to fix the segment list the dossier agents are
commissioned against, and to note where money changes hands. Nothing here is ranked.

## Scope settled in Phase 0

- Subject: FTAI Aviation Ltd. (NASDAQ: FTAI). FTAI Infrastructure (FIP) appears only as history.
- Depth register: functional mechanics. The level that determines product and market outcomes
  (what a module is, why a shop visit costs what it costs, what a life-limited part is, how a lease
  and a securitization work). Not thermodynamics or metallurgy.
- Emphasis: Aerospace Products deepest. Leasing, Strategic Capital and FTAI Power get full but
  shorter treatment.
- Sourcing: filings for FTAI and key peers. Constraint: this session cannot reach sec.gov directly
  (network policy). Filing figures are reached through search restricted to sec.gov and cited to
  the EDGAR URL the search returns.

## What FTAI is, as of mid-2026 (evidence so far)

Two reportable segments per the FY2025 10-K, plus a new platform launched 30 Dec 2025:

1. **Aerospace Products.** Develops and manufactures, repairs and refurbishes, and sells aircraft
   engines and aftermarket components, primarily for the CFM56-7B, CFM56-5B and V2500. Q2 2026
   revenue $875.0M (+78% y/y), Adjusted EBITDA $249.7M (+51%). 296 CFM56 modules refurbished in
   Q2 2026 (+61% y/y); 566 in 1H 2026; 2026 forecast raised to 1,200 modules; stated capacity
   3,000 modules/yr. 2026 segment Adjusted EBITDA guidance $1,050M. Sites: Montreal (ex-Lockheed
   Martin Commercial Engine Solutions, acquired 2023), Miami (QuickTurn), Rome NY, a planned
   113,000 sq ft Lisbon site (300+ modules/yr), plus capacity partnerships with GMF Indonesia and
   EgyptAir. PMA parts via a joint venture with Chromalloy; Chromalloy holds the only FAA-approved
   PMA high-pressure turbine blade for CFM56-5B/7B. V2500: five-year IAE EngineWise agreement
   (June 2024) covering 100+ full performance-restoration shop visits.
2. **Aviation Leasing.** Owns and manages aircraft and engines and leases and sells them, directly
   and through an equity-method investment. At 31 Dec 2025: 290 assets, 47 aircraft and 243
   engines, including 8 aircraft and 17 engines in Russia. Q2 2026 Adjusted EBITDA $88.2M.
3. **Strategic Capital Initiative (SCI).** Third-party capital vehicles that buy mid-life 737NG and
   A320ceo aircraft; FTAI manages them and performs the engine maintenance through its
   Maintenance, Repair and Exchange business. 2025 SPV: $2B equity (Oct 2025), $2.5B asset-level
   debt commitment (Feb 2025), ~$6B committed across 300+ aircraft, now in "harvest phase". 2026
   SPV: $2B warehouse facility from 13 lenders, accordion to $3B, closed 14 Aug 2026. Earlier
   partnership with OneIM ($4B, Mar 2025). WestJet 27 737-700 purchase.
4. **FTAI Power.** Launched 30 Dec 2025. "Mod-1": a 25 MW mobile gas-turbine generator set built
   around a CFM56 core, for data-center power. J&F Power Systems LLC, a JV with Jereh Group,
   signed a five-year master supply agreement with an international cloud provider and an initial
   $1.465B purchase order, deliveries in batches through Nov 2027, milestone payments. First units
   targeted Q4 2026; 100 units targeted in 2027; stated ability to deliver 100+ units/yr.

Corporate history that shapes the structure: Fortress Transportation and Infrastructure Investors
(IPO 2015) → FTAI Infrastructure spun off (Aug 2022) → redomiciled to Cayman as FTAI Aviation Ltd.
(Nov 2022) → internalization of Fortress management (28 May 2024: $150M cash plus 1,866,949 shares
to FIG LLC) → Muddy Waters short report (15 Jan 2025: alleged whole-engine sales booked as module
sales, expense reclassification; audit committee review with independent advisors) → SCI.

## The chain: where money changes hands

```
 Engine OEM (CFM = GE+Safran; IAE = P&W+MTU+JAEC)
   │  new engines bundled with airframes; new spare parts (list price, escalating);
   │  OEM MRO networks and long-term service agreements (TrueChoice, EngineWise)
   ▼
 Engine owners: airlines, aircraft lessors, engine lessors ──────────────┐
   │  pay for shop visits; pay maintenance reserves; buy/sell/lease engines │
   ▼                                                                       │
 Shop visit providers: OEM shops, independent MROs (MTU, LHT, StandardAero, │
   ST Engineering, GMF, EgyptAir...), and FTAI's Module Factory            │
   │  buy parts (new OEM, PMA, USM) + labor + repairs (OEM, DER)           │
   ▼                                                                       │
 Parts supply: OEM new parts │ PMA makers (HEICO, Chromalloy/FTAI JV) │     │
   USM from teardowns (AerSale, GA Telesis, VAS, lessors' part-outs)       │
   ▲                                                                       │
   └─── teardown feedstock comes from retired aircraft/engines ◄───────────┘
                                                                           
 Capital layer: ABS, warehouse lines, SPVs (SCI), bank debt, preferred shares
 New demand sink: FTAI Power converts CFM56 cores into 25 MW generator sets for data centers
```

## Segments commissioned (one dossier agent each)

| # | Dossier | What it must explain |
|---|---------|----------------------|
| D1 | The CFM56 as a machine | Modules, life-limited parts, EGT margin, performance restoration vs overhaul, workscopes, shop-visit cost build, V2500 and LEAP contrasts. Functional mechanics only. |
| D2 | Shop-visit market and OEM aftermarket | Who performs shop visits, capacity, demand forecasts, OEM parts pricing and escalation, OEM service programs, labor and parts lead times. |
| D3 | Used serviceable material and teardown | Part-out economics, green time, engine value as sum of modules, teardown supply, players, pricing vs new. |
| D4 | PMA and DER repairs | FAA/EASA mechanics, PMA market, acceptance by lessors and airlines, OEM pushback, FTAI–Chromalloy JV, savings per shop visit. |
| D5 | FTAI Aerospace Products | Module Factory mechanics, module vs engine sales, production and capacity, facilities, partnerships, V2500 program, MRE, customers, segment financials, the Muddy Waters allegations and review outcome, guidance. **Deepest.** |
| D6 | Engine and aircraft leasing mechanics and FTAI Leasing | Operating leases, maintenance reserves, return conditions, lessor models, mid-life narrowbody economics, ABS, FTAI's fleet and segment financials, Russia. |
| D7 | Strategic Capital Initiative | Vehicle structures, capital raised, fee and maintenance streams to FTAI, accounting, harvest phase, comparables. |
| D8 | FTAI Power and data-center power | Mod-1 mechanics, J&F JV, order, competition (GE Vernova, Siemens Energy, ProEnergy, aeroderivatives), unit economics, timeline. |
| D9 | Demand context | Fleet counts, retirements, new-generation engine durability issues, airframer delivery shortfalls, airline maintenance decisions, the translation table inputs. |
| D10 | FTAI the company | History, structure, management, governance, capital structure, consolidated financials 2021–1H26, non-GAAP definitions, dividends, risk factors, major customers. |
| D11 | Peers from their own filings | WLFC, AER, AL, HEI, ASLE, SARO, AIR, GE Aerospace: scale, margins, the comparable metrics. |
