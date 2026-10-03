# D5 — FTAI Aviation's Aerospace Products segment

Dossier for the FTAI Aviation deep primer. Raw material for the writer; not the primer. Posture: explain, do
not opine. Research date: 2026-10-03. Most recent reported quarter: Q2 2026 (released 29 July 2026).

Sourcing note for the writer. This session had a hard cap of 18 web searches and no direct page access
(WebFetch blocked; the proxy returns 403 for sec.gov and globenewswire.com). Thirteen searches completed;
the session-wide search budget was then exhausted by other agents, so five planned searches (securities
litigation status; trade-press exchange pricing; facility purchase prices and the 2026 partnership terms; the
10-K's customer-concentration, inventory and capex notes; 2022–2024 module counts) did not run. Those gaps
are recorded in section 7 rather than filled. Every figure below is tagged to the document the search
returned it from. Figures marked **derived** are arithmetic on reported figures and carry the arithmetic.

---

## 1. Summary

Aerospace Products is the FTAI segment that "develops and manufactures, repairs/refurbishes, and sells
aircraft engines and aftermarket components primarily for the CFM56-7B, CFM56-5B, and V2500" engines, with
sales "facilitated through a dedicated commercial maintenance program designed to focus on modular and
parts repair and refurbishment" — the Module Factory [S1]. The numbers that bind it:

- FY2025 segment revenue $1,936.2M, of which "Aerospace products revenue" $1,600.5M and "MRE Contract
  Revenue" $335.8M; FY2025 segment Adjusted EBITDA $671.3M (+76% y/y) [S1, S6].
- Q2 2026 segment revenue $875.0M (+78% y/y), Adjusted EBITDA $249.7M (+51% y/y) [S4].
- CFM56 modules refurbished: 184 in Q2 2025, 228 in Q4 2025, 757 in FY2025 (target was 750), 296 in Q2
  2026 (+61% y/y), 566 in 1H 2026 [S10, S31/S33, S4/chain map].
- 2026 module target: 1,050 set in February 2026 (+39%); the orchestrator's chain map records a raise to
  1,200 at Q2 2026 (see Tension T1) [S31, S33, chain map].
- Stated capacity 3,000 modules per year, supporting a stated goal of 25% of CFM56 shop visits [S35, S36].
- Guidance: 2026 segment Adjusted EBITDA $1,050M (reaffirmed July 2026); 2027 $1.4B [S4, S6].
- Footprint: 100%-owned Montréal (ex-Lockheed Martin Commercial Engine Solutions, closed 9 Sep 2024),
  Miami, Lisbon and Orange; 50% of QuickTurn Europe (Rome, 200,000 sq ft, closed June 2025); 50% of Prime
  Engine Accessories (Bristol, with Bauer); "over one million square feet" in total [S1, S13, S14, S34].
- V2500: five-year IAE EngineWise agreement (6 June 2024), 100+ performance-restoration shop visits,
  fleet of 140+ engines with a stated 200 target [S27].
- Muddy Waters short report 15 Jan 2025; Audit Committee review with independent legal and forensic
  advisors began 18 Jan 2025 and concluded the allegations "without merit" (Feb 2025); FY2024 10-K filed
  on time per the company [S17, S18, S19].

---

## 2. Mechanics

### 2.1 What the segment sells, in FTAI's words

The FY2025 Form 10-K (the annual report filed with the US Securities and Exchange Commission) describes the
segment as follows: it "develops and manufactures, repairs/refurbishes, and sells aircraft engines and
aftermarket components primarily for the CFM56-7B, CFM56-5B, and V2500 commercial aircraft engines. Engine,
module, and parts sales are facilitated through a dedicated commercial maintenance program designed to focus
on modular and parts repair and refurbishment of CFM56-7B and CFM56-5B engines" [S1].

Three terms carry that sentence:

- **CFM56-7B / CFM56-5B.** The two main variants of the CFM56 turbofan built by CFM International (a
  50/50 company of GE Aerospace and Safran). The -7B powers the Boeing 737 Next Generation (737-600/700/
  800/900); the -5B powers the Airbus A320ceo family. Chromalloy's October 2025 release puts the combined
  in-service fleet at "over 20,000 engines" [S29]. D1 covers the engine itself.
- **V2500.** The competing A320ceo-family engine built by the IAE consortium (Pratt & Whitney, Pratt &
  Whitney Aero Engines International GmbH, Japanese Aero Engines Corporation and MTU Aero Engines) [S27].
- **Module.** A CFM56 is assembled from a small number of major sub-assemblies that can be separated and
  re-mated at defined flanges: the fan and booster, the high-pressure compressor, the combustor and
  high-pressure turbine (together the "core"), and the low-pressure turbine, plus the accessory gearbox. Each
  carries its own set of life-limited parts (LLPs — rotating parts with a fixed, certificated cycle limit
  after which they must be removed regardless of condition) and its own state of wear, so an engine's
  modules are rarely "due" at the same time. That mismatch is the opening the Module Factory exploits.

### 2.2 The Module Factory

FTAI's own filing language, first used when the concept was launched with a third-party partner in 2022 and
still returned by search against the FY2025 10-K, is: "The Module Factory is a dedicated commercial engine
maintenance center focused on modular repair and refurbishment of CFM56-7B and CFM56-5B engines, based at
Lockheed Martin Commercial Engine Solutions' 500,000 square foot facility in Montreal, Canada with a
capacity for up to 300 shop visits per year" [S1; the same language appears in the FY2022 10-K, S19b].
FTAI bought that facility outright in September 2024 (section 2.6).

What it does, functionally. A conventional **shop visit** — the industry's term for taking an engine
off the aircraft and sending it to a maintenance shop — on a mid-life CFM56 is typically a **performance
restoration**: the engine is disassembled to the module or piece-part level, the hot-section parts are
inspected, repaired or replaced, expired LLPs are replaced with new ones, the engine is rebuilt, and it is
run in a **test cell** (an instrumented enclosure where the engine is run at power to confirm it meets its
certificated thrust and temperature limits) before release. The customer waits for its own engine the
whole time. D1 and D2 cover why that visit costs what it costs.

The Module Factory inverts the sequence. Rather than restoring a customer's engine part by part while the
customer waits, FTAI builds and holds an inventory of already-serviceable modules. When a customer engine
arrives, the module (or modules) that triggered the visit is removed and a serviceable module from
inventory is installed; the engine is tested and returned. The removed module then enters FTAI's own
production flow, is repaired and refurbished on FTAI's schedule, and goes back into inventory for a future
customer. FTAI's name for this offer is **MRE — Maintenance, Repair and Exchange** — a deliberate contrast
with the industry's **MRO — Maintenance, Repair and Overhaul**. The FY2025 10-K uses the phrase when it
describes the Rome joint venture as created "to meet increasing demand for MRE services" [S1].

Operationally, for the customer, the exchange therefore means:

1. What the customer sends: the engine (or, in some arrangements, the unserviceable module alone) at the
   point its condition or LLP status forces it off-wing.
2. What the customer receives: the same engine with one or more different, serviceable modules installed,
   or a different engine of the same type — "engine, module, and parts sales" are all listed as outputs of
   the same program [S1].
3. Downtime: the time to swap and test, not the time to repair; FTAI's acquired Miami business is branded
   "QuickTurn", and the Rome JV "QuickTurn Europe" [S14]. The actual turnaround times FTAI quotes were not
   retrieved in this session (Unknown U3).
4. What FTAI does with the unserviceable module: it becomes feedstock. Its repairable parts are repaired;
   its expired LLPs are replaced; parts with remaining life are retained as used serviceable material (USM
   — parts removed from one engine and re-certified for installation on another, covered in D3); and the
   restored module returns to inventory. Because FTAI also owns a leasing fleet of CFM56 engines and
   aircraft (D6) and manages the Strategic Capital Initiative vehicles (D7), it has a captive flow of
   engines for teardown and a captive flow of customers for exchanges.

Consequence for the economics: the exchange converts a customer's long, lumpy maintenance event into a
shorter transaction, and converts FTAI's maintenance activity from a service performed to order into a
manufacturing-like flow run from inventory — which is why FTAI counts "modules produced" per quarter the
way a factory reports units [S10, S31].

### 2.3 How exchanges, module sales and engine sales are priced and recognized

What FTAI states publicly, and what this session could and could not confirm:

- Outputs are described as "engine, module, and parts sales" [S1]. The 10-K's segment revenue is presented
  in two lines in FY2025: "Aerospace products revenue" ($1,600.5M) and "MRE Contract Revenue" ($335.8M)
  [S1]. The second line first appears in FY2025 — the Strategic Capital Initiative, whose vehicles contract
  FTAI to maintain the engines on the aircraft they own, launched on 30 December 2024 (chain map; S12).
- The structure of an exchange price in the industry is an **exchange fee** (the cash price for receiving
  a serviceable module in return for an unserviceable one) plus the **core** — the unserviceable module the
  customer hands over, which has value to the exchanger as feedstock. Under US revenue-recognition rules
  (ASC 606), noncash consideration received from a customer is measured at fair value and included in the
  transaction price, so an exchange typically records revenue equal to the fee plus the fair value of the
  core received, and cost of sales equal to the carrying value of the module delivered. An **outright
  module sale** records the cash price as revenue with no core coming back. An **engine sale** records the
  whole-engine price. In all three cases revenue is recognized at the point in time control transfers.
  This is the standard framework; the exact wording of FTAI's revenue-recognition note, and whether FTAI
  separately quantifies exchange fees versus core values, was not retrieved (Unknown U1).
- The Muddy Waters dispute (section 2.9) turns precisely on the boundary between the first and third
  categories: whether whole-engine sales were presented in a way that made them look like recurring module
  or aftermarket revenue. FTAI's filings present a single "Aerospace products revenue" line for products;
  this session found no 10-K table disaggregating that line into engines, modules and parts for 2023–2025
  (Unknown U2).

### 2.4 Volumes, capacity and the share target

Modules refurbished, as reported or derived (all CFM56):

| Period | Modules | How known |
|---|---|---|
| Q4 2024 | ≈136 **derived** | Q4 2025's 228 was "+68% y/y" → 228 / 1.68 = 135.7 [S31, S33] |
| Q2 2025 | 184 | Q2 2025 earnings release [S10] |
| Q4 2025 | 228 | Q4 2025 call summaries [S31, S33] |
| FY2025 | 757 (target 750) | Q4 2025 call summaries [S31, S33] |
| Q1 + Q3 2025 | 345 **derived** | 757 − 184 − 228; the split was not retrieved (Unknown U4) |
| Q1 2026 | 270 **derived** | 566 (1H 2026) − 296 (Q2 2026) [chain map, S4] |
| Q2 2026 | 296 (+61% y/y) | Q2 2026 release and call [S4, S35]; 296 / 1.61 = 183.9 ≈ Q2 2025's 184 ✓ |
| 1H 2026 | 566 | chain map (Q2 2026 release) |
| FY2026 target | 1,050 (Feb 2026); 1,200 per chain map (Jul 2026) | [S31, S33]; Tension T1 |

Context on how the target moved: the 30 December 2024 guidance release said 2025 guidance "reflects an
average of 100 modules per quarter produced at the Company's Montreal facility in fiscal year 2025" — about
400 for the year from Montréal alone [S12]. The year closed at 757 against a later target of 750 [S31].

Capacity and share: on the Q2 2026 call FTAI said it had increased CFM56 module production capacity to
3,000 per year, "supporting its 25% market share goal and 100 Mod-1 units annually" [S35, S36]. The "25%"
is a share of CFM56 shop visits; the denominator FTAI uses (annual CFM56 shop visits industry-wide, and
whether counted as visits or modules) was not retrieved (Unknown U5). Mod-1 is the FTAI Power generator
set built around a CFM56 core (D8), which draws on the same module production.

Scale check on the 300-visit figure versus 3,000 modules. Montréal's "up to 300 shop visits per year" is a
2022-era statement about one building operated as a conventional shop [S1, S19b]. A CFM56 has four to five
major modules, so 300 complete engines a year is 1,200–1,500 module-equivalents at one site; add Miami,
Rome, Lisbon and the Indonesia and Egypt partnerships and 3,000 modules a year is a different measure of a
different footprint rather than a contradiction. The two figures should not be compared directly (Tension
T2 records the framing issue).

Engine sales counts, V2500 modules and V2500 shop-visit counts: not disclosed in anything this session
retrieved (Unknown U6).

### 2.5 The V2500 program

On 6 June 2024 FTAI and IAE International Aero Engines AG announced a five-year EngineWise maintenance
services agreement covering "over 100 full-performance restoration shop visits" on V2500 engines
[S27, S28]. **EngineWise** is Pratt & Whitney's brand for its aftermarket service agreements; under it the
OEM's network performs the shop visits. The release states FTAI "currently owns and is committed to over
140 V2500 engines and looks to grow its portfolio to 200 by 2025", and describes the deal as "one of IAE's
largest engine maintenance agreements by number of engines with a non-airline customer" [S27].

Functionally, this is a different model from the CFM56 Module Factory: on the V2500, FTAI is a large
engine owner buying OEM-network restorations at a negotiated price for a committed volume, then leasing
or selling the restored engines and selling V2500 material. Whether FTAI performs any V2500 module work
in-house, and the current V2500 fleet count against the 200 target, were not retrieved (Unknown U6). The
Chromalloy V2500 HPT blade (an FAA-approved alternative part unveiled at MRO Europe) is a parts input that
could bear on V2500 restoration cost; FTAI's statements on it were not retrieved [S30].

### 2.6 Facilities and partners

| Site | What it is | Ownership | Dates and figures | Source |
|---|---|---|---|---|
| Montréal, Canada | Former Lockheed Martin Commercial Engine Solutions (LMCES); 500,000 sq ft; "up to 300 shop visits per year" (2022 statement); home of the Module Factory | 100% | Acquisition closed 9 Sep 2024. Purchase price not retrieved (Unknown U7). The chain map says "acquired 2023" — see Tension T3 | [S1, S13] |
| Miami, Florida | "QuickTurn" engine maintenance business | 100% | Acquisition date and price not retrieved (Unknown U7) | [S1, S14 (brand)] |
| Orange | Listed as a 100%-owned maintenance facility in the FY2025 10-K; nature (component repair, test, etc.) and acquisition date not retrieved (Unknown U7) | 100% | — | [S1] |
| Lisbon, Portugal | Listed as a 100%-owned maintenance facility in the FY2025 10-K; the chain map records a "planned 113,000 sq ft" site at "300+ modules/yr" — not independently verified (Unknown U7) | 100% | On the Q2 2026 call Lisbon was described as "still ramping" | [S1, S36] |
| Rome Fiumicino, Italy | QuickTurn Europe, a 200,000 sq ft CFM56 engine MRO facility at Rome Fiumicino Airport; JV "established to expand the Company's global engine maintenance capabilities and meet increasing demand for MRE services" | 50% equity method | Agreement announced with the Q4 2024 results (26 Feb 2025); closing announced 5 Jun 2025. The orchestrator's brief gives "50% for $10.5M" — not independently verified here | [S1, S9, S14] |
| Bristol, Connecticut | Prime Engine Accessories, a 50/50 JV with Bauer, Inc., "an industry-leading MRE repair facility for accessory parts"; "expected to deliver up to $75,000 in average savings per shop visit"; expected operational "by the end of this year" (said on the Q3 2025 call, i.e., end-2025) | 50% | — | [S1, S34] |
| Indonesia | Partnership with GMF AeroAsia (Garuda's MRO arm) referenced on the Q2 2026 call as a capacity partnership; terms not retrieved (Unknown U8) | partnership | 2026 | [S35, S36] |
| Egypt | Partnership with EgyptAir referenced on the Q2 2026 call; terms not retrieved (Unknown U8) | partnership | 2026 | [S35, S36] |

The 10-K's summary sentence: "The Company conducts engine maintenance at its 100% owned facilities in
Montréal, Miami, Lisbon, and Orange, as well as through its 50% equity ownership in QuickTurn Europe,
located in Rome, and 50% equity ownership in Prime Engine Accessories, located in Bristol. Collectively,
these facilities span over one million square feet and are equipped with advanced tooling, engine test
cells, and engineering capabilities to support a wide range of component repairs and service requirements"
[S1]. Test-cell count and employee counts by site were not disclosed in anything retrieved (Unknown U9).
A caution for the writer: one search summary attributed "approximately 7,800 people across over 50
facilities" to FTAI; that is StandardAero's profile (its S-1 appeared in the same results) and is not an
FTAI figure.

**Equity method** (used for Rome and Bristol): FTAI records its share of the JV's profit as one line and
does not consolidate the JV's revenue, so Rome's shop-visit revenue is not inside the $1,936M segment
revenue; only FTAI's share of its earnings is. Module counts FTAI reports may or may not include modules
produced at Rome (Unknown U10).

### 2.7 PMA within the segment

**PMA (Parts Manufacturer Approval)** is the FAA's approval for a company other than the OEM to make a
replacement part; the mechanics, approvals and market are D4's subject. What belongs here is what FTAI
reports:

- FTAI has "teamed up with Chromalloy to develop several CFM56 hot-section parts" through a joint venture
  (chain map; S29). In October 2025 Chromalloy received FAA PMA for the CFM56-5B/7B high-pressure turbine
  (HPT) blade, which Chromalloy describes as "the only aftermarket alternative to the OEM manufactured new
  part". Chromalloy now offers four PMA parts on the CFM56-5B/7B: the HPT blade, the HPT nozzle guide vane,
  the LPT stage-1 nozzle guide vane and the HPT shroud. Chromalloy said order backlog would consume all
  production for the remainder of 2025 with customers "seeking to reserve production slots into 2026" [S29].
- On the Q4 2025 call (26 Feb 2026), asked how segment margins would move from the mid-30s toward 40%,
  CEO Joe Adams "cited approval of a PMA high-pressure turbine blade as a key factor, along with expanded
  access to lower-cost parts supply, including used serviceable material and a materials agreement with
  CFM that includes parts and repairs" [S33]. FTAI said it "can approach 40% aerospace margins in 2026 via
  parts approvals, lower-cost supply and expanded repair capabilities" [S33].
- FTAI's quantification of the JV's contribution (dollars of savings per module, PMA share of parts
  consumed, JV earnings line) was not retrieved (Unknown U11). The one FTAI-quantified savings lever found
  is the Bristol accessories JV at "up to $75,000 in average savings per shop visit" [S34].

The HPT blade matters mechanically because the HPT module is the hottest, shortest-lived and most
expensive module to restore, and its blades are among the highest-value non-LLP consumables in a CFM56
shop visit; an approved non-OEM blade changes the parts bill of exactly the module that most often drives
a visit. D4 has the numbers.

### 2.8 Segment financials — how the pieces fit

Reported (R) and derived (D) figures; full tables in section 4.

- FY2025 segment revenue $1,936.2M (R) = products $1,600.5M + MRE contract $335.8M [S1]. Segment Adjusted
  EBITDA $671.3M (R) [S6] → margin 34.7% (D).
- FY2024 products revenue $1,079.8M (D: the 10-K says 2025 products revenue rose $520.6M) [S1]; FY2024
  Adjusted EBITDA ≈ $381M (D: $671.3M / 1.76) [S6] → margin ≈ 35% (D).
- Q4 2025: Adjusted EBITDA "$195 million at a 35% margin (up approximately 66% year-over-year)" (R) [S33]
  → revenue ≈ $557M (D).
- Q1 2026: products $522.6M + MRE contract $221.2M (R) = $743.8M (D, if those are the only two lines)
  [S2]; Adjusted EBITDA $222.6M (R) [S8] → margin ≈ 29.9% (D).
- Q2 2026: revenue $875.0M, Adjusted EBITDA $249.7M (R) [S4] → margin 28.5% (D). Products revenue for
  1H 2026 $1,214.8M (R) [S3] → Q2 products $692.2M (D) → implied MRE contract and other $182.8M (D).
- MRE contract revenue as a share of segment revenue: 17.3% in FY2025, 29.7% in Q1 2026, ≈20.9% in Q2 2026
  (all D). The segment margin moved from 35% (Q4 2025) to ≈29–30% (1H 2026) over the same period. The
  reader should not infer a causal link from this dossier; the 10-K does not, in anything retrieved,
  disclose margin by revenue line (Unknown U2).
- **Adjusted EBITDA** is FTAI's non-GAAP profit measure; D10 carries the definition. It is reported by
  segment in the earnings releases and 10-K segment note.
- Cost of sales: $1,240.4M for FY2025 [S1] and $1,160.1M for 1H 2026 [S3]. Whether these are segment
  figures or the consolidated income-statement line (which in FTAI's statements has historically also
  carried the cost of aircraft and engines sold by the Leasing segment) could not be confirmed (Tension
  T5). If segment: FY2025 gross margin = (1,936.2 − 1,240.4) / 1,936.2 = 35.9%; 1H 2026 = (1,618.8 −
  1,160.1) / 1,618.8 = 28.3%.
- Inventory, net: $1,364.3M at 31 March 2026 [S2/S3]. Inventory is where the Module Factory's working
  capital sits — serviceable modules and parts awaiting exchange. The 31 December 2025 and 30 June 2026
  balances and the segment's capital expenditure were not retrieved (Unknown U12).
- Guidance: 2026 segment Adjusted EBITDA $1,050M, set in February 2026 (when total segment guidance moved
  from $1.525B to $1.625B) and reaffirmed in July 2026; 2027 "Business Segment" guidance $2.3B of which
  Aerospace Products $1.4B, FTAI Power $450M, Aviation Leasing $450M [S4, S6]. Tension T4 records a
  conflicting guidance attribution in one search summary.

### 2.9 The Muddy Waters report and the review

**Muddy Waters Research** is a short-selling research firm (it publishes a report after taking a position
that profits if the share price falls). On 15 January 2025 it published a report on FTAI. As the sources
retrieved describe the allegations:

- FTAI "has been recording one-time engine sales as Maintenance Repair & Overhaul (MRO) revenue in its
  Aerospace Products (AP) segment", producing a growth story that Muddy Waters said was "lower quality
  than investors give the company credit for" [S22, S21].
- Muddy Waters "estimates that the majority of FTAI Aviation's adjusted EBITDA in the Aerospace Products
  segment comes from gains on sales, which is less recurring in nature" [S22].
- The report alleged "misrepresentation of sales, inflation of Maintenance, Repair, and Overhaul (MRO)
  margins (and margins in general), channel stuffing, and a few other accounting red flags" [S23].
- The orchestrator's brief also lists an allegation about expense classification between the Leasing and
  Aerospace Products segments (costs of engines whose parts were sold in Aerospace Products being carried
  as Leasing depreciation). The sources retrieved summarize this only as "inflation of … margins"; the
  report's own wording was not retrieved (Unknown U13). **Channel stuffing** means recognizing sales to
  intermediaries or related parties ahead of end demand; the specific counterparty Muddy Waters named was
  not retrieved (Unknown U13).

FTAI's stated position and process:

- FTAI said it "strongly disagrees with the assertions" in the report [S21].
- "On January 18, 2025, the company's Audit Committee of the Board determined to begin a review, which
  included engaging independent advisors, in response to the assertions alleged in the January 15, 2025
  report issued by Muddy Waters Research" [S21, S18]. The **Audit Committee** is the board committee of
  independent directors that oversees financial reporting and the external auditor.
- Outcome, from the company's February 2025 8-K exhibit: "After a thorough and comprehensive review with
  the support of independent legal and forensic accounting advisors, the Audit Committee determined that
  the allegations made against the Company are without merit. The Company expects to file its Form 10-K
  timely" [S17]. Trade coverage dated 20 February 2025 reported the shares rising on the announcement
  [S26], which dates the announcement to on or about 19 February 2025. The FY2024 10-K was filed under
  accession 0001590364-25-000006 [S19]; the company's statement is that it was timely. The exact filing
  date was not captured (Unknown U14).
- Auditor: Ernst & Young LLP, ratified as independent registered public accounting firm for FY2024 [S9].
- Restatement: none was found or referenced in anything retrieved. Reporting change: the FY2025 10-K
  presents "MRE Contract Revenue" as a separate line from "Aerospace products revenue" [S1]; this coincides
  with the Strategic Capital Initiative's first full year and this session found no statement linking it
  to the review. Whether FTAI began disclosing engine versus module sales after the review was not
  determined (Unknown U2).
- An SEC correspondence file dated 27 November 2024 exists on EDGAR [S20]; its subject was not retrieved
  (Unknown U15).

Securities litigation: law-firm releases show an investigation announced 15 January 2025 [S24] and a
securities-fraud class action with a lead-plaintiff deadline of 18 March 2025 [S25]. (A **lead plaintiff**
is the investor a court appoints to direct a class action; the deadline is the statutory 60 days after
notice of the first-filed complaint.) The court, docket, and current procedural status (motion to dismiss,
settlement, or dismissal) were not retrieved because the search budget was exhausted (Unknown U16).

Both positions are reported above as stated; this dossier does not adjudicate them.

### 2.10 Worked example 1 — one CFM56-7B module exchange versus a full shop visit

The inputs this session can source are limited, so the example is set up as an explicit calculation with
labelled inputs; D1/D2 supply the shop-visit cost and downtime, and Unknowns U1/U3 record what FTAI has
not disclosed.

Situation. A 737-800 operator has a CFM56-7B whose HPT module has consumed its exhaust-gas-temperature
margin (the headroom between the engine's actual exhaust temperature and its certificated limit; when it
is used up the engine must come off-wing) while the fan, booster and low-pressure turbine have substantial
LLP life left.

Option A — conventional performance-restoration shop visit:
- Cost to operator = S (labor + OEM parts + LLP replacement + test), to be taken from D1/D2.
- Downtime = T_A days; cost of downtime = T_A × c, where c is the daily cost of a spare engine or lost
  aircraft availability (D6 for spare-engine lease rates).
- The operator keeps every part of its own engine, including the remaining life in the untouched modules.

Option B — module exchange with FTAI:
- Cost to operator = exchange fee F plus the value it gives up in the unserviceable HPT core (C_core).
- Downtime = T_B days, the swap-and-test interval rather than the repair interval; cost = T_B × c.
- The operator receives a serviceable HPT module of known remaining LLP life, which may be more or less
  than new; any mismatch in remaining life is reflected in F.

The operator is indifferent when F + C_core + T_B × c = S + T_A × c, i.e., when the exchange premium
(F + C_core − S) equals the downtime saving (T_A − T_B) × c. If the right-hand side is positive and the
left-hand side smaller, the exchange is cheaper all-in.

What FTAI's numbers can say about F. FTAI does not publish an exchange price list in anything retrieved.
The only observable is the segment's products revenue per module produced: $1,600.5M / 757 = $2.11M in
FY2025 and $692.2M / 296 = $2.34M in Q2 2026 (section 2.11). That figure is an upper bound on the average
cash fee for a module, because the numerator also contains whole-engine and parts sales and the value of
cores received, while the denominator counts only CFM56 modules. The one FTAI-quantified cost lever found
— "up to $75,000 in average savings per shop visit" from the Bristol accessories JV [S34] — illustrates
the magnitude of a single component-repair lever against a multi-million-dollar event.

For FTAI, the same transaction is: revenue = F + fair value of the core; cost of sales = carrying value
of the module delivered (its acquisition cost plus parts, labor and overhead to make it serviceable);
margin = the difference. The Q4 2025 segment EBITDA margin of 35% [S33] applied to a $2.11M average
revenue per module implies about $1.37M of cost per module (D), with the same mixing caveat.

### 2.11 Worked example 2 — revenue and margin per module implied by the segment, and its limits

| Period | Products revenue | Modules | Revenue / module (D) | Segment Adj. EBITDA | EBITDA / module (D) |
|---|---|---|---|---|---|
| FY2025 | $1,600.5M [S1] | 757 [S31] | $2.11M | $671.3M [S6] | $0.887M |
| Q1 2026 | $522.6M [S2] | 270 (D) | $1.94M | $222.6M [S8] | $0.824M |
| Q2 2026 | $692.2M (D) [S3] | 296 [S4] | $2.34M | $249.7M [S4] | $0.844M |

Arithmetic: FY2025, 1,600.5 / 757 = 2.114; 671.3 / 757 = 0.887. Q1 2026, 522.6 / 270 = 1.936; 222.6 /
270 = 0.824. Q2 2026, 692.2 / 296 = 2.339; 249.7 / 296 = 0.844.

Limits, each of which can move the result by a large fraction:
1. The numerator includes whole-engine sales, spare-parts sales, USM sales and V2500 activity; the
   denominator counts only CFM56 modules. Revenue per module is therefore overstated by an unknown amount.
2. Modules "produced" in a quarter are not the modules sold in that quarter; a produced module may sit in
   inventory, be used in an FTAI-owned leasing engine, or go into a Mod-1 generator set (D8).
3. Segment Adjusted EBITDA includes MRE contract revenue ($335.8M in 2025; $221.2M in Q1 2026) and the
   equity-method share of Rome and Bristol, none of which is a module sale; EBITDA per module is therefore
   also overstated.
4. Exchange revenue includes the fair value of cores received, which is not cash.
5. Module mix (an HPT module is worth multiples of a fan module) is not disclosed.

A proper unit economics would need the disaggregation that Unknown U2 describes.

---

## 3. Market structure and players

Within the segment's world, the counterparties are:

- **Customers.** Airlines (operators of 737NG and A320ceo aircraft), aircraft and engine lessors (who must
  return or redeliver engines in contracted condition), and other MROs buying modules or material. The
  Strategic Capital Initiative vehicles — third-party-capital partnerships that buy mid-life 737NG and
  A320ceo aircraft and contract FTAI for maintenance (D7) — are the counterparties behind "MRE Contract
  Revenue" [S1, S12]. FTAI's own Leasing segment is an internal customer. Named external customers,
  long-term agreements and concentration disclosures were not retrieved (Unknown U17). Geography by
  revenue, FY2025: North America $1,133.0M (58.5%), Europe $415.1M (21.4%), Asia $274.6M (14.2%), Africa
  $71.5M (3.7%), South America $42.0M (2.2%) [S1; percentages D].
- **Competing shop-visit providers** (D2): CFM's own network (GE Aerospace, NYSE: GE; Safran, EPA: SAF),
  independent MROs (MTU Aero Engines, ETR: MTX; Lufthansa Technik; StandardAero, NYSE: SARO; ST
  Engineering), and airline MROs including the two FTAI has partnered with, GMF AeroAsia and EgyptAir.
- **OEM.** CFM International. Adams referred on the Q4 2025 call to "a materials agreement with CFM that
  includes parts and repairs" [S33]; its terms were not retrieved (Unknown U18). IAE (Pratt & Whitney,
  RTX, NYSE: RTX; MTU) is the V2500 counterparty under EngineWise [S27].
- **Parts suppliers** (D3, D4): OEM new parts; PMA via the Chromalloy JV; USM from teardowns including
  FTAI's own and the SCI vehicles' retired assets.
- **Capacity partners.** Lockheed Martin (seller of LMCES, 2024), the QuickTurn Europe partner in Rome,
  Bauer, Inc. (Bristol), GMF AeroAsia, EgyptAir [S13, S14, S34, S35].
- **FTAI Power** (D8) is a new internal demand sink for CFM56 modules: the stated 3,000-module capacity
  is described as supporting both the 25% share goal and 100 Mod-1 units a year [S35].

---

## 4. Numbers

### 4.1 Segment revenue and Adjusted EBITDA

| Period | Products revenue | MRE contract revenue | Segment revenue | Segment Adj. EBITDA | Margin | Source |
|---|---|---|---|---|---|---|
| FY2023 | not retrieved | — | not retrieved | not retrieved | — | Unknown U19 |
| FY2024 | $1,079.8M (D) | nil / not shown | ≈$1,079.8M (D) | ≈$381M (D) | ≈35% (D) | [S1] (2025 up $520.6M); [S6] (+76%) |
| Q2 2025 | — | — | ≈$491.6M (D) | ≈$165.4M (D) | ≈33.6% (D) | [S4] (Q2 2026 +78% / +51%) |
| Q4 2025 | — | — | ≈$557M (D) | $195M | 35% (stated) | [S33] |
| FY2025 | $1,600.5M | $335.8M | $1,936.2M | $671.3M (+76%) | 34.7% (D) | [S1, S6, S7] |
| Q1 2026 | $522.6M | $221.2M | $743.8M (D) | $222.6M | 29.9% (D) | [S2, S8] |
| Q2 2026 | $692.2M (D) | ≈$182.8M (D) | $875.0M (+78%) | $249.7M (+51%) | 28.5% (D) | [S3, S4, S5] |
| 1H 2026 | $1,214.8M | ≈$404.0M (D) | ≈$1,618.8M (D) | ≈$472.3M (D) | ≈29.2% (D) | [S3, S4, S8] |

Derivations: Q2 2025 revenue = 875.0 / 1.78 = 491.6; Q2 2025 EBITDA = 249.7 / 1.51 = 165.4. Q4 2025 revenue
= 195 / 0.35 = 557. FY2024 EBITDA = 671.3 / 1.76 = 381.4. Q2 2026 products = 1,214.8 − 522.6 = 692.2;
Q2 2026 MRE/other = 875.0 − 692.2 = 182.8.

### 4.2 Cost of sales, inventory, guidance

| Item | Figure | Period / date | Source |
|---|---|---|---|
| Cost of sales | $1,240.4M | FY2025 | [S1]; segment vs consolidated unclear (T5) |
| Cost of sales | $1,160.1M | 1H 2026 | [S3]; same caveat |
| Inventory, net | $1,364.3M | 31 Mar 2026 | [S2, S3] |
| 2026 segment Adj. EBITDA guidance | $1,050M | set Feb 2026; reaffirmed 29 Jul 2026 | [S6, S4] |
| 2026 total segment guidance | $1.525B → $1.625B ($1.05B AP + $575M Leasing) | 25 Feb 2026 | [S6] |
| 2026 Leasing guidance | $575M → $475M | 29 Jul 2026 | [S4] |
| 2027 segment guidance | $2.3B: AP $1.4B, FTAI Power $450M, Leasing $450M | 29 Jul 2026 | [S4] |
| 2026 margin aspiration | "approach 40%" | 26 Feb 2026 call | [S33] |
| Consolidated Q4 2025 Adj. EBITDA | $277.2M | Q4 2025 | [S6] |
| Consolidated Q2 2026 net income attributable; EPS | $117.6M; $1.15 basic / $1.13 diluted | Q2 2026 | [S4] |
| Dividend | $0.40 (Q4 2025) → $0.50 (Q2 2026) per ordinary share | | [S6, S4] |

### 4.3 Volumes

See the table in section 2.4. Headline: 757 modules in FY2025; 566 in 1H 2026; 2026 target 1,050 (Feb)
and 1,200 per the chain map (Jul); capacity 3,000/yr; share goal 25% of CFM56 shop visits.

### 4.4 Facilities

See section 2.6. Headline square footage: Montréal 500,000 [S1]; Rome 200,000 [S1]; total "over one
million" [S1]; Lisbon 113,000 per chain map (unverified).

### 4.5 Geography (FY2025 segment revenue)

| Region | $ thousands | Share (D) |
|---|---|---|
| North America | 1,132,995 | 58.5% |
| Europe | 415,145 | 21.4% |
| Asia | 274,618 | 14.2% |
| Africa | 71,452 | 3.7% |
| South America | 42,034 | 2.2% |
| Total | 1,936,244 | 100% |

Source: FY2025 10-K segment geographic table [S1].

### 4.6 Management named on the Q2 2026 call

Joe Adams, CEO; David Moreno, President; Nicholas McAleese, CFO; Stacy Kuperus, COO [S35]. A CFO
transition was announced 6 March 2026 [S16].

---

## 5. Constraints and bottlenecks

Stated or evident in the sources; no ranking implied.

- **Feedstock.** Every exchange needs a serviceable module in inventory, and every serviceable module
  starts as an unserviceable one — from a customer core, an FTAI leasing-fleet engine, an SCI-vehicle
  engine, or a bought teardown engine (D3). Inventory of $1.36B at March 2026 [S2] is the visible cost of
  holding that pipeline.
- **Parts supply and price.** Adams named three levers for the move from mid-30s to ~40% margins: the PMA
  HPT blade, more USM, and the CFM materials agreement [S33]. Each is a supply constraint in reverse:
  Chromalloy's PMA production was sold out through 2025 with slots being reserved into 2026 [S29]; USM
  supply depends on retirements (D9); OEM parts prices escalate (D2).
- **Physical capacity and ramp.** Rome and Lisbon were "still ramping" in July 2026 [S36]; Bristol was
  expected operational at end-2025 [S34]; the Indonesia and Egypt partnerships are 2026 additions whose
  capacity is undisclosed. Capacity of 3,000 modules is a stated ceiling against 566 produced in 1H 2026.
- **Test cells and skilled labor.** The 10-K cites "engine test cells" as part of the footprint [S1]; counts
  and labor headcount by site are not disclosed (U9).
- **Regulatory acceptance.** The PMA lever depends on FAA (and EASA) approval of each part and on lessor
  and airline acceptance of PMA in return conditions (D4).
- **Internal competition for modules.** FTAI Power's Mod-1 program (100 units/yr target) draws on the same
  module production as the aftermarket [S35]; the allocation rule is not disclosed.
- **Demand side.** The 25% share target is a share of CFM56 shop visits, a number that peaks and then
  declines as the fleet retires (D9); the horizon over which FTAI expects 25% was not retrieved (U5).
- **Scrutiny.** The segment's revenue classification is the subject of the short report and of securities
  litigation (section 2.9); the company's position is that the allegations are without merit.

---

## 6. Tensions

- **T1 — 2026 module target.** Q4 2025 call summaries give 1,050 (set February 2026) [S31, S33]; a Q2 2026
  call summary also says "2026 goal is 1,050 modules" [S36]; the orchestrator's chain map records the Q2 2026
  release raising the forecast to 1,200. Resolution: the 29 July 2026 release text [S4/S5].
- **T2 — Capacity framing.** "Up to 300 shop visits per year" at Montréal (2022-era filing language, still
  in the filings) [S1, S19b] versus "3,000 modules per year" of capacity (July 2026) [S35]. Different units
  (visits vs modules), different footprints (one site vs all sites and partners), different dates.
- **T3 — Montréal acquisition date.** Chain map: "acquired 2023". GlobeNewswire: "FTAI Aviation Closes the
  Acquisition of LMCES", 9 September 2024 [S13]. Announcement and closing may differ by months; the price is
  unretrieved (U7).
- **T4 — Guidance attribution.** One search summary attributed to the Q1 2026 10-Q a 2026 guidance of
  "$1.525 billion … approximately $1.0 billion from Aerospace Products and $525 million from Aviation
  Leasing" [S2 summary]. The Q4 2025 release (25 Feb 2026) states guidance was updated "from $1.525 billion
  to $1.625 billion, comprised of $1.05 billion from Aerospace Products and $575 million from Aviation
  Leasing" [S6], and the Q2 2026 release reaffirmed $1,050M for Aerospace Products [S4]. The $1.525B figure
  is most likely the earlier (October 2025) 2026 guidance quoted in a comparison; the sequence should be
  confirmed from the releases.
- **T5 — Cost of sales scope.** Search returned "cost of sales $1,240,368 thousand" for FY2025 against an
  Aerospace Products query [S1]. FTAI's consolidated statement of operations has a single "Cost of sales"
  line that, in prior years, also carried the cost of aircraft and engines sold by Leasing. If the figure
  is consolidated, the 35.9% "gross margin" in section 2.8 is not a segment margin.
- **T6 — Allegations as summarized.** Sources summarize Muddy Waters' allegations differently: [S22]
  stresses engine sales booked as MRO revenue and EBITDA from gains on sales; [S23] lists "misrepresentation
  of sales, inflation of MRO margins … channel stuffing". The brief adds an inter-segment expense
  allegation. None of the retrieved sources is the report itself.
- **T7 — Employee count.** A search summary gave "approximately 7,800 people across over 50 facilities";
  this matches StandardAero's S-1 (which appeared in the same result set), not FTAI. FTAI's headcount is
  unretrieved (U9).

---

## 7. Unknowns

- **U1 — Revenue-recognition text for exchanges.** The 10-K's exact policy for exchange transactions (how
  the core is valued, whether exchange fees are separately quantified). Resolves with the 10-K revenue note
  [S1].
- **U2 — Disaggregation of "Aerospace products revenue."** Engines vs modules vs parts vs repairs for 2023,
  2024, 2025 and each 2025–2026 quarter; margin by line; whether disclosure changed after the February 2025
  review. Resolves with the 10-K and 10-Q revenue notes [S1–S3] or with the Q2 2026 release [S5].
- **U3 — Exchange turnaround time and exchange pricing.** FTAI's quoted turnaround and any published
  exchange-fee ranges. Trade press (e.g., the In Practise interview [S38]) likely has estimates; not read.
- **U4 — Module counts for 2022, 2023, 2024 and Q1/Q3 2025.** Only Q4 2024 (≈136) is derivable. Resolves
  with the Q4 2024 release [S43], the Q1 2025 release [S42], the Q3 2025 release [S11] and the FY2023
  release.
- **U5 — Denominator of the 25% share goal** and the year by which it is targeted.
- **U6 — Engine sales counts; V2500 shop visits completed; current V2500 fleet vs 200 target; whether any
  V2500 module work is done in-house.**
- **U7 — Facility deal terms.** LMCES purchase price; QuickTurn Miami date and price; what and where
  "Orange" is and when acquired; Lisbon's size, capacity and opening date (chain map: 113,000 sq ft, 300+
  modules/yr); verification of Rome at $10.5M for 50%.
- **U8 — GMF AeroAsia and EgyptAir terms** (capacity committed, economics, duration).
- **U9 — Test-cell count; employees by site and in total.**
- **U10 — Whether Rome's modules are counted in FTAI's module totals**, given equity-method accounting.
- **U11 — Chromalloy JV contribution in FTAI's numbers**: equity-method earnings line, PMA share of parts,
  FTAI-stated savings per module.
- **U12 — Inventory at 31 Dec 2025 and 30 Jun 2026; segment capex; the cost of building module inventory.**
- **U13 — Muddy Waters' own wording** on expense classification, channel stuffing and the "other red
  flags".
- **U14 — Exact FY2024 10-K filing date** (accession 0001590364-25-000006; company says timely).
- **U15 — Subject of the 27 Nov 2024 SEC correspondence** [S20].
- **U16 — Securities litigation status** (court, docket, motion to dismiss outcome, any settlement).
- **U17 — Named customers, long-term agreements, customer concentration** (any customer ≥10% of revenue),
  and whether SCI-vehicle revenue is disclosed as related-party.
- **U18 — Terms of the CFM materials agreement** mentioned on the Q4 2025 call.
- **U19 — FY2023 segment revenue and Adjusted EBITDA**, and the FY2022 baseline (the segment began
  ramping in 2022–2023 per the 10-Q language [S10 summary]).

---

## 8. Terms introduced

- **Form 10-K / 10-Q / 8-K** — US SEC annual report, quarterly report, and current report (used for press
  releases and material events).
- **CFM56-7B / -5B** — the CFM International turbofan variants on the 737NG and A320ceo respectively.
- **V2500** — the IAE consortium's A320ceo-family engine.
- **Module** — a separable major sub-assembly of the engine (fan/booster, HP compressor, core, LP turbine,
  gearbox), each with its own wear state and LLPs.
- **Life-limited part (LLP)** — a rotating part with a certificated cycle limit; must be removed at the limit
  regardless of condition.
- **Shop visit** — removal of an engine for maintenance at a shop.
- **Performance restoration** — a shop visit that restores exhaust-gas-temperature margin by repairing or
  replacing hot-section parts, typically with LLP replacement.
- **EGT margin** — headroom between actual exhaust gas temperature and the certificated limit; its exhaustion
  forces a shop visit.
- **Test cell** — instrumented enclosure for running an engine at power to confirm it meets limits.
- **MRO** — Maintenance, Repair and Overhaul, the industry's generic term.
- **MRE** — Maintenance, Repair and Exchange, FTAI's term for restoring an engine by exchanging modules and
  parts from inventory.
- **Module Factory** — FTAI's production-line approach to building and holding serviceable CFM56 modules
  for exchange.
- **Exchange fee / core** — the cash price of an exchange and the unserviceable unit the customer hands over.
- **USM** — used serviceable material: parts removed from one engine and re-certified for another.
- **PMA** — FAA Parts Manufacturer Approval for a non-OEM replacement part.
- **HPT** — high-pressure turbine, the hottest, most expensive module to restore.
- **EngineWise** — Pratt & Whitney/IAE's brand of aftermarket service agreements.
- **Equity method** — accounting for a 20–50% owned entity by recording a share of its profit, not its
  revenue.
- **Adjusted EBITDA** — FTAI's non-GAAP segment profit measure (definition in D10).
- **Strategic Capital Initiative (SCI)** — FTAI-managed third-party-capital vehicles that own mid-life
  aircraft and contract FTAI for maintenance (D7).
- **Mod-1** — FTAI Power's 25 MW generator set built around a CFM56 core (D8).
- **Short report / short seller** — research published by a firm positioned to profit from a share-price
  fall.
- **Audit Committee** — board committee of independent directors overseeing financial reporting and the
  external auditor.
- **Forensic accounting** — investigative accounting review of transactions and records.
- **Channel stuffing** — recognizing sales to intermediaries or related parties ahead of end demand.
- **Lead plaintiff** — the court-appointed investor who directs a securities class action.

---

## 9. Sources

Filings (via sec.gov-restricted search; URLs are EDGAR):
- S1. FTAI Aviation Ltd., Form 10-K for FY2025 (filed early 2026).
  https://www.sec.gov/Archives/edgar/data/1590364/000162828026012940/ftai-20251231.htm
- S2. Form 10-Q, quarter ended 31 Mar 2026.
  https://www.sec.gov/Archives/edgar/data/1590364/000162828026029335/ftai-20260331.htm
- S3. Form 10-Q, quarter ended 30 Jun 2026.
  https://www.sec.gov/Archives/edgar/data/0001590364/000162828026051412/ftai-20260630.htm
- S5. Q2 2026 earnings release, 8-K ex. 99.1 (29 Jul 2026).
  https://www.sec.gov/Archives/edgar/data/0001590364/000162828026050622/ftai6302026earningsrelease.htm
- S7. Q4/FY2025 earnings release, 8-K ex. 99.1 (25 Feb 2026).
  https://www.sec.gov/Archives/edgar/data/1590364/000162828026011685/ftai123125earningsrelease.htm
- S8. Q1 2026 earnings release, 8-K ex. 99.1 (29 Apr 2026).
  https://www.sec.gov/Archives/edgar/data/1590364/000162828026028390/ftai3312026earningsrelease.htm
- S17. 8-K ex. 99.1, Audit Committee conclusion (Feb 2025).
  https://www.sec.gov/Archives/edgar/data/1590364/000114036125005179/ef20043996_ex99-1.htm
- S18. 8-K, January 2025 (review commencement).
  https://www.sec.gov/Archives/edgar/data/1590364/000114036125001452/ef20041894_8k.htm
- S19. Form 10-K for FY2024 (accession 0001590364-25-000006).
  https://www.sec.gov/Archives/edgar/data/1590364/000159036425000006/ftai-20241231.htm
- S19b. Form 10-K for FY2022.
  https://www.sec.gov/Archives/edgar/data/1590364/000159036423000007/ftai-20221231.htm
- S20. SEC correspondence, 27 Nov 2024.
  https://www.sec.gov/Archives/edgar/data/1590364/000114036124047965/filename1.htm
- S42. Q1 2025 earnings release, 8-K ex. 99.1.
  https://www.sec.gov/Archives/edgar/data/1590364/000114036125016712/ef20048218_ex99-1.htm
- S43. Q4/FY2024 earnings release, 8-K ex. 99.1 (26 Feb 2025).
  https://www.sec.gov/Archives/edgar/data/1590364/000114036125006099/ef20044380_ex99-1.htm
- S44. Q2 2025 earnings release, 8-K ex. 99.1.
  https://www.sec.gov/Archives/edgar/data/1590364/000114036125027877/ef20052914_ex99-1.htm
- S45. Q3 2025 earnings release, 8-K ex. 99.1.
  https://www.sec.gov/Archives/edgar/data/1590364/000159036425000038/ftai93025earningsrelease.htm
- 10-Qs for Q1–Q3 2025 and Q2–Q3 2024 as listed in the EDGAR index (module-count references).

Company press releases (GlobeNewswire):
- S4. Q2 2026 results, 29 Jul 2026.
  https://www.globenewswire.com/news-release/2026/07/29/3335598/35538/en/FTAI-Aviation-Ltd-Reports-Second-Quarter-2026-Results-Increases-Dividend-to-0-50-per-Ordinary-Share.html
- S6. Q4/FY2025 results, 25 Feb 2026.
  https://www.globenewswire.com/news-release/2026/02/25/3245051/35538/en/FTAI-Aviation-Ltd-Reports-Fourth-Quarter-and-Full-Year-2025-Results-Increases-Dividend-to-0-40-per-Ordinary-Share.html
- S9. Q4/FY2024 results and QuickTurn Europe agreement, 26 Feb 2025.
  https://www.globenewswire.com/news-release/2025/02/26/3033379/35538/en/FTAI-Aviation-Ltd-Reports-Fourth-Quarter-and-Full-Year-2024-Results-Declares-Dividend-of-0-30-per-Ordinary-Share-Announces-Agreement-to-Expand-Maintenance-Capacity-with-QuickTurn-E.html
- S10. Q2 2025 results, 29 Jul 2025.
  https://www.globenewswire.com/news-release/2025/07/29/3123626/35538/en/FTAI-Aviation-Ltd-Reports-Second-Quarter-2025-Results-Declares-Dividend-of-0-30-per-Ordinary-Share.html
- S11. Q3 2025 results, 27 Oct 2025.
  https://www.globenewswire.com/news-release/2025/10/27/3174978/0/en/FTAI-Aviation-Ltd-Reports-Third-Quarter-2025-Results-Increases-Dividend-to-0-35-per-Ordinary-Share.html
- S12. SCI launch and 2025 guidance, 30 Dec 2024.
  https://www.globenewswire.com/news-release/2024/12/30/3002893/35538/en/FTAI-Aviation-Launches-Strategic-Capital-Initiative-and-Announces-2025-Financial-Guidance.html
- S13. LMCES acquisition closing, 9 Sep 2024.
  https://www.globenewswire.com/news-release/2024/09/09/2943296/35538/en/FTAI-Aviation-Closes-the-Acquisition-of-LMCES.html
- S14. QuickTurn Europe JV closing, 5 Jun 2025.
  https://www.globenewswire.com/news-release/2025/06/05/3094782/0/en/ftai-aviation-ltd-announces-closing-of-quickturn-europe-joint-venture.html
- S15. FTAI Power launch, 30 Dec 2025.
  https://www.globenewswire.com/news-release/2025/12/30/3211297/35538/en/FTAI-Aviation-Announces-the-Launch-of-FTAI-Power-FTAI-Adapts-the-World-s-Largest-Aircraft-Engine-Platform-to-Meet-AI-Driven-Power-Demand.html
- S16. CFO transition, 6 Mar 2026.
  https://www.globenewswire.com/news-release/2026/03/06/3250943/0/en/FTAI-Aviation-Announces-CFO-Transition.html

OEM and partner statements:
- S27. RTX / Pratt & Whitney newsroom, "IAE AG and FTAI Aviation Sign Strategic V2500 Engine Maintenance
  Services Agreement", 6 Jun 2024.
  https://www.rtx.com/en/prattwhitney/newsroom/news/2024/06/06/iae-ag-and-ftai-aviation-sign-strategic-v2500-engine-maintenance-services-agreem
- S28. AviTrader, 7 Jun 2024. https://avitrader.com/2024/06/07/ftai-aviation-and-iae-sign-v2500-engine-maintenance-agreement
- S29. Chromalloy, "Chromalloy Secures FAA Approval of CFM56 High Pressure Turbine Blade PMA", Oct 2025.
  https://www.newswire.com/news/chromalloy-secures-faa-approval-of-cfm56-high-pressure-turbine-blade-22665618
- S30. Aviation Week, "Chromalloy Unveils FAA-Approved V2500 HPT Blade" (MRO Europe).
  https://aviationweek.com/shows-events/mro-europe/chromalloy-unveils-faa-approved-v2500-hpt-blade

Call transcripts and summaries (management statements; secondary):
- S31. Motley Fool, FTAI Q4 2025 earnings call transcript, 26 Feb 2026.
  https://www.fool.com/earnings/call-transcripts/2026/02/26/ftai-ftai-q4-2025-earnings-call-transcript/
- S32. Motley Fool, FTAI Q1 2026 earnings call transcript, 30 Apr 2026.
  https://www.fool.com/earnings/call-transcripts/2026/04/30/ftai-ftai-q1-2026-earnings-transcript/
- S33. MarketBeat, "FTAI Aviation Q4 earnings call highlights", 26 Feb 2026.
  https://www.marketbeat.com/instant-alerts/ftai-aviation-q4-earnings-call-highlights-2026-02-26/
- S34. Insider Monkey, FTAI Q3 2025 earnings call transcript (Oct 2025).
  https://www.insidermonkey.com/blog/ftai-aviation-ltd-nasdaqftai-q3-2025-earnings-call-transcript-1635931/
- S35. GuruFocus, FTAI Q2 2026 call transcript (30 Jul 2026).
  https://www.gurufocus.com/stock/FTAIN.PFD/transcripts/8991621
- S36. Quartr, FTAI Q2 2026 earnings summary. https://quartr.com/events/ftai-aviation-ltd-ftai-q2-2026_ozdaN73d
- S37. StockStory via Barchart, "FTAI Q3 Deep Dive", 28 Oct 2025.
  https://www.barchart.com/story/news/35738184/ftai-q3-deep-dive-strategic-capital-partnerships-drive-asset-light-growth-transition
- S38. In Practise, "FTAI Aviation CFM56 Module Swap Offering & Addressable Market" (expert interview;
  surfaced, not read). https://inpractise.com/articles/ftai-module-swap-offering-and-addressable-market
- S39. FTAI IR, Q2 2026 call page (blocked in this session). https://ftandi.gcs-web.com/node/13056/html
- S40. FTAI IR, IAE agreement release PDF (blocked). https://ftandi.gcs-web.com/node/11676/pdf

Short report, response and litigation (secondary):
- S21. Seeking Alpha news, "FTAI Aviation says it strongly disagrees with assertions in Muddy Waters short
  report (update)", Jan 2025.
  https://seekingalpha.com/news/4395677-ftai-aviation-says-it-strongly-disagrees-with-assertions-in-muddy-waters-short-report
- S22. Benzinga, "What's Going On With FTAI Aviation Stock Today", 15 Jan 2025.
  https://benzinga.com/25/01/43103333/whats-going-on-with-ftai-aviation-stock-today
- S23. Hedge Fund Alpha, Crossroads Capital letter on FTAI (summarizing the report's allegations).
  https://hedgefundalpha.com/strategies/crossroads-capital-long-ftai-aviation-ftai/
- S24. BFA Law (GlobeNewswire), investigation announcement, 15 Jan 2025.
  https://www.globenewswire.com/news-release/2025/01/15/3010482/0/en/FTAI-BREAKING-NEWS-BFA-Law-is-Investigating-FTAI-Aviation-Ltd-after-Short-Seller-Report-Reveals-Potential-Fraud-Contact-the-Firm-if-You-Lost-Money-NASDAQ-FTAI.html
- S25. BFA Law (GlobeNewswire), class action notice, lead-plaintiff deadline 18 Mar 2025, 12 Feb 2025.
  https://www.globenewswire.com/news-release/2025/02/12/3025046/0/en/ftai-class-action-report-ftai-aviation-ltd-is-being-sued-for-securities-fraud-investors-are-urged-to-contact-bfa-law-by-march-18-deadline-nasdaq-ftai.html
- S26. StockStory via Wedbush, "Why FTAI Aviation (FTAI) Stock Is Trading Up Today", 20 Feb 2025.
  https://investor.wedbush.com/wedbush/article/stockstory-2025-2-20-why-ftai-aviation-ftai-stock-is-trading-up-today
- S9 (above) also: proxy ratification of Ernst & Young LLP for FY2024 (via sec.gov search summary).

Orchestrator inputs: /home/user/SPOT/ftai-primer/research/chain-map.md and edgar-index.md (figures labelled
"chain map" above were supplied by the orchestrator, not re-verified in this session).
