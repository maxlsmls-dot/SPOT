# D2 — The CFM56 shop-visit market and the OEM aftermarket model

Dossier for the FTAI Aviation deep primer. Raw material for the writer; explain-not-opine posture;
functional-mechanics depth. Searches run 2026-10-03 (18 WebSearch calls, WebFetch unavailable).
Every figure carries its source and date. Where a source is a consultancy blog or a trade-press
summary rather than a primary document, it is labelled as such. Figures from FTAI itself are
taken from the Phase 1 chain map (which cites FTAI's Q2 2026 release and FY2025 10-K) and are
cross-referenced, not re-sourced here; D5 owns them.

---

## 1. Summary

The CFM56 shop-visit market is the business of taking a CFM56 engine off a Boeing 737NG or Airbus
A320ceo, disassembling it in a licensed shop, replacing or repairing worn and life-expired parts,
and returning it to service. It is the largest single engine aftermarket in the world by volume.
The numbers that bind it:

- **Demand**: GE Aerospace and Safran entered 2026 projecting about **2,300 CFM56 shop visits** in
  each of 2026 and 2027, then widened the range to **2,300–2,400** (and said "probably closer to
  2,400"), held that range **through 2028**, and place the **apex around 2027–2028** with a gradual
  fade after (Aviation Week, 2026). Safran's earlier view was a peak of **~2,500 in 2025–26**
  (Aviation Week, c. 2023/24). Pre-pandemic (2019) the figure was **just above 2,000**.
- **Retirements**: GE's 2026 assumption moved from **3–4%** of the fleet, to **2–3%**, to
  **1.5–2%**; actual 1Q 2026 retirements were **below 1%** (GE IR, 2026).
- **Installed base**: ~**23,000** CFM56 engines in service (2024), of which ~**70%** had seen zero
  or one shop visit; a consultancy source says **>19,000** flying (2026). Tension recorded.
- **Price**: new spare parts escalated ~**10%/year** (double-digit on 1 Nov 2022, high-single-digit
  in Aug 2023); Safran's stated rule is **inflation + 3–4 points** (Aviation Week, 2023). The CFM56
  aftermarket is **~85% spare parts and time-and-materials**, versus ~40% for LEAP (Safran).
- **Cost build**: material ~**60–70%** of a shop visit, labour **20–30%**, repairs **10–20%** (Air
  Cargo Week, 2025/26). A CFM56-7B LLP stack is quoted at **>$3M** (2017) to **~$4M** (Aircraft Value
  News, date not captured). Performance restoration **$1.2–1.6M**; full overhaul **$3.5–4.2M** (Safe
  Fly Aviation, 2026; consultancy blog).
- **Capacity**: slot wait times rose **2–3 months, up to 6** (Bain, 2024); **two-thirds** of MRO
  operators cannot find enough technicians; labour-rate inflation **5.5–6.0%** (Oliver Wyman,
  April 2026). StandardAero spent **>$100M** since 2022 to **more than double** CFM56-7B capacity
  (SARO 10-K FY2025).
- **OEM scale**: GE Aerospace Commercial Engines & Services revenue **$33.3B in 2025, 75% services**;
  internal shop-visit revenue **+24% (2025), +19% (2024), +27% (2023)** (GE 10-K FY2025). Safran
  civil spares revenue **+17.6%** in 2025, "driven primarily by the CFM56" (Safran, 13 Feb 2026).

---

## 2. Mechanics

### 2.1 What a shop visit is and why an engine comes off wing

A **shop visit** (SV) is a scheduled or unscheduled removal of an engine from the aircraft for
work that cannot be done on wing, performed at an **engine shop**: a facility holding regulatory
approval (an FAA Part 145 repair station or the EASA equivalent) and, in practice, OEM technical
data and tooling, that disassembles the engine on **engine stands** (the wheeled fixtures that
hold a 2.5-tonne engine or a module while it is worked on), cleans and inspects every piece,
replaces or repairs what is out of limits, reassembles, and runs the engine in a **test cell**
before releasing it.

Three things drive a CFM56 to the shop (D1 has the full treatment; this is what matters for the
market):

1. **Performance deterioration**, measured as **EGT margin**: the gap between the exhaust gas
   temperature the engine actually runs at on a hot-day takeoff and the certified limit. As
   hot-section hardware wears, EGT rises and margin shrinks; at zero margin the engine must come
   off. Restoring EGT margin is called a **performance restoration** (PR) and is primarily a
   hot-section (high-pressure turbine, combustor, high-pressure compressor) rebuild.
2. **Life-limited parts (LLPs)**: rotating discs, spools, shafts and seals that the certification
   authority limits to a fixed number of flight cycles (one takeoff and landing) regardless of
   condition, because their failure would not be contained by the casing. When any LLP reaches its
   limit the engine must be opened to the depth of that part. Because the most restrictive LLPs
   sit in the high-pressure turbine (HPT), an LLP-driven removal forces the engine open to the core
   and is almost always combined with a performance restoration.
3. **Hardware events**: foreign object damage, oil-system faults, inspection findings from an
   airworthiness directive.

The **workscope** is the specification of what will be done: which **modules** are opened, to what
depth, which parts are replaced new, which are repaired, which are swapped for **used serviceable
material (USM)**. A **module** is a mechanically self-contained section of the engine that can be
removed and replaced as a unit: on the CFM56 the industry treats the fan and booster (low-pressure
compressor), the core (high-pressure compressor, combustor and HPT) and the low-pressure turbine
as the three major modules, with the accessory gearbox as a fourth. Modularity is what makes a
**module exchange** possible: instead of overhauling the core, the shop installs a serviceable core
from inventory and the operator pays the difference in remaining life plus a fee. FTAI's "Module
Factory" is built on exactly this (D5).

Workscope tiers, with the trade-press cost ranges found (all for CFM56; see Section 4 for the
provenance of each):

| Tier | What it is | Cost range found (2026) |
|---|---|---|
| Light / quick-turn | Limited opening, targeted repair, no LLPs; **quick-turn** means a short-turnaround, minimum-scope repair | $650k–$900k |
| Performance restoration | Hot-section rebuild to recover EGT margin; may replace some LLPs if convenient | $1.2M–$1.6M |
| Heavy SV with LLPs | PR plus replacement of LLPs that are at or near limit | $2.1M–$2.8M |
| Full overhaul ("zero-time") | All modules to overhaul standard, full LLP stack | $3.5M–$4.2M |

Source for ranges: Safe Fly Aviation, "Engine Shop Visit Costs Worldwide 2026" (consultancy blog;
treat as indicative). A Leeham News engineering primer (Bjorn Fehrm, 3 Mar 2017) priced a CFM56
HPT LLP exchange at "easily $0.5m", fan/booster LLPs at "$0.5m–$0.7m", and the whole engine LLP
stack at "north of $3m" at 2017 list prices. Aircraft Value News headlined the CFM56-7 stack at
**$4M** ("Engine Life Limited Parts Pricing Continues to Rise: $4M for CFM56-7"; date not
captured). The Safe Fly "heavy SV with LLPs" range of $2.1–2.8M is therefore consistent only with
partial LLP replacement; a PR plus a full stack at current list would be roughly $1.4M + $4M =
$5.4M. Tension recorded in Section 6.

**Turnaround time (TAT)** is the calendar time from induction (the engine arriving at the shop and
being accepted into work) to release. **Induction slot** is the scheduled date a shop commits to
start; when shops are full, the wait for a slot is distinct from, and additional to, the TAT.

### 2.2 Where the money goes in a shop visit, and who captures it

Air Cargo Week ("The true cost of engine maintenance", trade press, 2025/26) gives the split:
**material 60–70%**, **labour 20–30%**, **repairs and other shop activities 10–20%**. Safe Fly
Aviation gives a finer CFM56 cut: **LLPs 40–60% of parts cost**, **HPT blades and vanes 15–25%**,
**labour 15–20%** (blog, 2026). The two are not inconsistent: LLPs and HPT airfoils together are
the bulk of material, and material is the bulk of the visit.

Who captures each slice:

| Slice | Share of SV | Who captures it | Mechanism |
|---|---|---|---|
| New OEM parts (non-LLP): blades, vanes, seals, hardware | Largest single slice | CFM International, i.e. GE Aerospace and Safran, at **catalog list price** (the OEM's published price list, repriced at least annually) | Sold through CFM's spares organisation to any shop; the shop passes through at list plus a handling margin, or the airline buys direct under a TrueChoice Material agreement |
| LLPs | 40–60% of parts cost when replaced | OEM only, in practice: no PMA LLPs exist for the CFM56 (D4) | Sold at list; LLP prices are the most visible escalator (the "$4M stack" headline) |
| Used serviceable material (USM) | Substitutes for new parts | Teardown and USM traders (AerSale, GA Telesis, VAS, lessors' part-outs) **and the OEM**: GE states that "GE and CFM are the largest used serviceable material provider for their products" (GE Aerospace, 2026) | Priced at a discount to new list, typically as a percentage of list; D3 |
| PMA parts | Alternative to new OEM parts | PMA makers: HEICO, Chromalloy (FTAI–Chromalloy JV) | D4 |
| Component repairs | 10–20% | **Repair vendors**: OEM repair shops (GE's "repair management" offering and Safran's) and independent repair specialists holding **DER repairs** (repairs approved via an FAA Designated Engineering Representative rather than OEM data) | A shop subcontracts airfoil, case and seal repairs; a repaired part costs a fraction of a new one |
| Labour and test | 20–30% | The engine shop (OEM, independent or airline) | Shop labour rate × hours; Oliver Wyman puts 2025 labour-rate inflation at 5.5–6.0% |
| Shop margin and risk | Embedded | The shop, or the OEM under a flight-hour agreement | Time-and-materials: airline bears the risk; rate-per-flight-hour: OEM bears it and prices it in |

Two consequences follow. First, because 60–70% of the visit is material and most material is
OEM-priced, the OEM's annual catalog escalation flows almost directly into the cost of every shop
visit regardless of who performs it. Second, the only levers a non-OEM shop has to cut the bill are
on the material line: USM instead of new, PMA instead of OEM, repair instead of replace, and
module exchange instead of overhaul. That is the entire commercial logic of FTAI's Aerospace
Products segment and of the independents' "material solutions" offerings.

### 2.3 How the OEM aftermarket model works

**Spare parts at list price, escalating.** The OEM publishes a catalog price for every part and
revises it periodically. Aviation Week ("Parts Price Hikes Help Boost Safran, GE Aftermarket
Sales", late 2023) reported that new engine spare-parts prices had been rising **around 10% per
year**; that GE and Safran, 50-50 partners in CFM International, "pushed through **high-single-digit**
spares price hikes in **August [2023]**", following a **double-digit increase on 1 November 2022**;
and that Safran's CEO said spare parts pricing had "always been above inflation by **3 to 4
points**" and "we'll continue on that path, I would say, at least for some years." GE's external
spares sales were up **35% year-over-year** and its spares shipment rate hit a record **$42.2 million
per day** in the quarter reported (same article). Specific percentages for the 2024, 2025 and 2026
catalog revisions were not found (Unknown U1).

**Time-and-materials versus long-term agreements.** Under **time-and-materials (T&M)** the airline
pays for each shop visit as it occurs: parts at list, labour by the hour. Under a **long-term service
agreement (LTSA)**, also called a **rate-per-flight-hour (RPFH)** or flight-hour agreement, the
airline pays a fixed amount per engine flight hour and the OEM commits to perform or pay for the
shop visits; the OEM thereby takes the volume and cost risk and controls the workscope, parts
sourcing and shop selection. Safran (Aviation Week, "CFM Aftermarket Shifting To Long-term
Agreements", c. 2023/24) described the **CFM56 aftermarket revenue profile as 85% spare parts and
T&M**, versus **about 40% for LEAP**, and sees the LEAP fleet reaching **60–70% long-term agreements
by 2030**. The CFM56 is, in other words, an open, transactional market in which the OEM's main
capture is parts, not contracts; the LEAP is being set up as a captive one.

**CFM TrueChoice.** GE Aerospace's branded CFM56 (and LEAP) services menu, as described in GE's own
press releases (Safair, TAAG, Southwest, 2019–2025):

- **TrueChoice Flight Hour**: "customized offerings that help optimize cost of ownership over the
  entire engine lifecycle with flexible risk transfer and payment options" — the RPFH product.
  Southwest Airlines' CFM56-7B fleet is the reference customer (GE press release, "GE expands
  TrueChoice Flight Hour agreement with Southwest Airlines").
- **TrueChoice Overhaul**: "time and material overhauls with tailored workscopes specific to shop
  visit objectives, economic priorities and ownership horizon — whether for one engine or an entire
  fleet" — T&M shop visits in GE's own network (Safair and TAAG signed these for CFM56).
- **TrueChoice Material**: "high-quality new and used OEM parts, advanced repairs and technology
  upgrades for airlines and MROs that enhance engine performance over the lifecycle and support
  higher engine residual value" — parts and repairs sold to third-party shops and to airlines that
  use third-party shops. This is where the OEM's own USM business sits. Ryanair's "long-term
  materials agreement" covering "their entire fleet of ~2,000 CFM56 and LEAP engines" (GE 10-K
  FY2025) is a TrueChoice Material-type contract.
- **TrueChoice Transitions**: "a broad range of options for changing ownership horizons, including
  green time leases, exchanges and material buy-back, plus custom workscopes with shorter builds and
  maximum used material." **Green time** is the remaining usable life on an engine or part before
  its next shop visit or LLP limit; a **green-time lease** rents that life. This offering is the
  OEM's direct competitor to FTAI's Module Factory and to the independents' end-of-life products:
  it sells shorter, cheaper, USM-heavy builds to operators who do not intend to keep the engine
  long.

GE also sells repair management as a service to independents (Aero Norway "awards repair management
contract to GE Aviation", GE press release) and overhaul consulting to airline MROs (EgyptAir
TrueChoice overhaul consulting agreement, Amwal Al Ghad). GE's stated posture is that "an open
network exists with multiple providers who compete and invest to win shop visits" (GE Aerospace,
2026) while GE "continue[s] to strengthen MRO access to OEM materials to support further CFM56
longevity" (same).

**IAE EngineWise and the V2500.** The V2500 (the CFM56's competitor on the A320ceo) is made by
IAE, a consortium of Pratt & Whitney (RTX), Pratt & Whitney Aero Engines International, Japanese
Aero Engines Corporation and MTU Aero Engines. **EngineWise** is Pratt & Whitney's services brand,
"a variety of aftermarket services to maximize engine performance and fleet availability" (RTX
press release, 6 June 2024). The same release announced the **five-year EngineWise agreement with
FTAI covering more than 100 full performance-restoration shop visits**, "one of IAE's largest
engine maintenance agreements by number of engines with a non-airline customer". Aviation Week's
V2500 data tool projected a **spike to ~1,400 V2500 shop visits in 2025**, and **more than 7,800
overhaul shop visits plus 3,142 LLP-driven visits over the next ten years**; IAE separately said it
expects **no V2500 retirement surge over the next five years** (Aviation Week). "FleetCare" was not
found as a current IAE product name in this session (Unknown U9).

### 2.4 How capacity is defined and why it is scarce

A shop's capacity is the number of inductions per year it can take, set by (i) floor space and
engine stands, (ii) licensed technicians, (iii) test-cell hours, and (iv) parts flow: a shop that
cannot get HPT blades or repaired cases on time fills up with half-built engines waiting on parts,
which consumes stands and floor without producing output. Each of these was reported as binding
between 2023 and 2026:

- **Slots and TAT**: Bain (2024) reported that "the wait times just to secure an MRO slot rose by
  two to three months and, in some cases, six months", and that engine MRO demand is projected to
  exceed available capacity by more than 17% before the end of the decade. AVM Magazine (2025)
  reported lead times "surpass[ing] more than 200 days in severe cases" on some new-generation
  programmes. Aero Norway said the long lead times for induction slots were driving interest in
  quick-turn services, "especially in the case of older-generation engines, such as the CFM56 and
  V2500" (AVM, May 2024).
- **Labour**: Oliver Wyman's 2026 MRO survey (>150 respondents; April 2026): "two-thirds of MRO
  operators struggle to find qualified technicians", labour-rate inflation "settled in at
  5.5–6.0%", and "more than half of survey respondents expect labor attrition to be worse in the
  coming year". StandardAero's Lewis Prebble and ST Engineering both named labour as the leading
  constraint (Aviation Week, "Narrowbody Engine Demand Drives MRO Capacity Additions").
- **Parts**: "Parts supply remains a capacity constraint with every OEM, due to the recovery in
  aircraft utilization and the associated growth in MRO demand coming at the same time that engine
  OEMs are ramping up production" (Aviation Week, same article). GE's own 10-K says its FLIGHT DECK
  operating system "increased material input from priority suppliers more than 40% year-over-year"
  in 2025, and that TAT for LEAP, CFM56 and GE90 improved by more than 10% y/y in 4Q 2025 (GE 10-K
  FY2025) — i.e. the OEM itself was parts-constrained through 2024 and reports easing in late 2025.
- **USM**: "The supply of used serviceable material remains thin, leaving shops more reliant on
  newly manufactured core parts" (AVM, 2025); Aviation Week ran "MRO Memo: A Seller's Market for
  Used Parts". Low retirements (1.5–2%) are the cause: fewer teardowns, less USM, more demand for
  new OEM parts, more OEM pricing power.

### 2.5 Worked example: an engine approaching an LLP limit

**Setup (assumptions stated; figures sourced in Section 4).** An airline operates a 737-800 with
two CFM56-7Bs. On one engine, the HPT disc (certified limit **20,000 cycles**; new price
**$420,000** — Safe Fly, 2026) has 1,200 cycles remaining. EGT margin is otherwise adequate for
about 3,000 more cycles (assumption). The aircraft flies about 1,500 cycles a year (assumption,
typical of a short-haul 737-800; not a sourced figure) and the airline plans to retire it in **24
months**, so it needs **~3,000 cycles** from this engine position. Because the limiting LLP is in
the HPT, any LLP action forces the core open.

Per-cycle cost of LLP life, to frame everything else: a full CFM56-7B LLP stack at **~$4M**
(Aircraft Value News) over a **20,000-cycle** life is **$4,000,000 ÷ 20,000 = $200 per cycle**; at
1,500 cycles a year that is **$300,000 per engine per year**, or **$600,000 per aircraft per year**,
accruing whether or not the engine ever goes to the shop. This is why lessors collect maintenance
reserves (D6) and why engine value is so sensitive to LLP status.

**Option A — full shop visit with LLP replacement.**
- Performance restoration workscope: **$1.2–1.6M** (Safe Fly, 2026); midpoint $1.4M.
- LLP stack: **>$3M** at 2017 list (Leeham) to **~$4M** (Aircraft Value News). Use $4M.
- Outlay: **$1.4M + $4.0M = $5.4M** for a full stack. If only the HPT LLP set is replaced ("easily
  $0.5m", Leeham 2017), outlay is **$1.4M + $0.5M = $1.9M**, but the other LLPs keep their own
  (lower) remaining lives, so the next LLP-forced visit comes sooner — the **LLP stagger** problem.
- Downtime: TAT plus slot wait of **2–6 months** (Bain 2024). Covering the position with a leased
  spare at **$42–48k/month** (Safe Fly, 2026) for 3 months ≈ **$135k**.
- Value effect: a low-life CFM56-7B trades as teardown feedstock at **$0.8–1.2M** (Safe Fly);
  a green-time CFM56-7B trades at **$2.8–3.4M** (Safe Fly, 2026); an engine fresh from a full-stack
  overhaul should be worth more than a green-time unit (no figure found; Unknown U8). Taking the
  green-time midpoint as a floor: value uplift ≈ $3.1M − $1.0M = **$2.1M**.
- Net economic cost over the horizon, if the engine is sold at exit:
  **$5.4M + $0.135M − $2.1M ≈ $3.4M** (full stack), with the true figure lower if the fresh-stack
  engine fetches more than a green-time price. The airline buys ~20,000 cycles of LLP life to use
  3,000 of them; the other 17,000 are recovered only through the resale price.

**Option B — module exchange.**
- Swap the HPT (or the whole core) module for a serviceable one carrying, say, 10,000 cycles of
  remaining LLP life; the fan/booster and LPT modules stay. The engine is opened only to the core
  split, so TAT is shorter and labour is lower than a full visit.
- Price structure: **exchange fee + value of LLP life transferred ± condition of the other core
  hardware**. LLP value transferred: 10,000 cycles × $200/cycle (stack-average, above) ≈ **$2.0M**
  if priced at new-list-per-cycle for a whole stack; for the HPT LLP set alone (≈$0.5M new over
  20,000 cycles = $25/cycle) ≈ **$250k** for 10,000 cycles. Safe Fly quotes "removal costs of
  $150,000–$400,000 per module" for LLP modules (meaning unclear; recorded in Unknown U7). The
  exchange fee itself — what FTAI, GE TrueChoice Transitions or MTU actually charge above the LLP
  value — was not found in any source (Unknown U7). The arithmetic therefore brackets Option B at
  roughly **$0.5–1.0M for an HPT-set exchange** and higher for a full core, versus $1.9–5.4M for
  Option A, with the operator receiving only the life it needs rather than 20,000 cycles.
- This is the product FTAI sells (chain map: 296 modules refurbished in Q2 2026; 1,200 forecast
  for 2026; 3,000/yr stated capacity) and that GE packages as TrueChoice Transitions.

**Option C — green-time engine lease.**
- Remove the LLP-limited engine, install a leased green-time CFM56-7B (typically **4,000–8,000
  cycles remaining**, Safe Fly) at **$42–48k per month** (Safe Fly, 2026): **24 × $45k = $1.08M**
  (range $1.008–1.152M), plus any per-cycle LLP and performance reserves the lessor charges
  (unknown here; D6), plus redelivery conditions.
- Sell the removed engine as feedstock: **+$0.8–1.2M**. Net cash over 24 months ≈ **−$1.08M +
  $1.0M ≈ −$0.1M** (range −$0.35M to +$0.19M) before reserves and redelivery costs.
- IBA's April 2024 commentary ("it's a lessor's market") said engine lease rates and market values
  were escalating; the $42–48k figure is a 2026 blog figure and should be treated as indicative.

**Option D — sell the engine.**
- Sell the LLP-limited engine for **$0.8–1.2M** (teardown value, Safe Fly) and buy a green-time
  unit at **$2.8–3.4M**: net outlay **$1.6–2.6M**, after which the airline owns an asset with
  4,000–8,000 cycles, resaleable after 3,000 cycles at a lower (unfound) price. Or sell the whole
  aircraft as-is and let the buyer price the deficit: Safe Fly says two otherwise identical
  CFM56-7Bs at 10,000 cycles since new "differ by $1.6 million based solely on LLP remaining life"
  and that 60–80% of a used engine's value is its remaining LLP life.

| Option | Cash out (24 months) | Cash/asset back | Indicative net | Downtime |
|---|---|---|---|---|
| A. Full SV, full LLP stack | $5.4M + $0.14M cover | Engine worth ≥$3.1M | ≈ −$3.4M or better | 2–6 month slot wait + TAT |
| A'. PR + HPT LLPs only | $1.9M + $0.14M | Engine worth more than today, less than A | not computable (U8) | same |
| B. HPT/core module exchange | fee (U7) + ~$0.25–2.0M LLP life | Engine with exactly the life needed | ≈ −$0.5 to −1.0M for HPT set | shorter than A |
| C. Green-time lease | $1.0–1.15M rent + reserves | +$0.8–1.2M from selling own engine | ≈ −$0.1M ± $0.3M before reserves | engine swap only |
| D. Sell, buy green-time | $2.8–3.4M | +$0.8–1.2M now, resale later | −$1.6 to −2.6M less resale | engine swap only |

The arithmetic is not a recommendation; the point is structural. Options B, C and D exist only
because the engine is modular and because a secondary market in modules, green time and USM
exists. Low retirements shrink the supply behind B, C and D (fewer teardowns, fewer green-time
engines) at exactly the moment the slot shortage makes A slow and the list-price escalation makes
A expensive.

---

## 3. Market structure and players

### 3.1 The OEM network

**CFM International** is the 50-50 joint venture of **GE Aerospace** (NYSE: GE) and **Safran Aircraft
Engines** (Euronext: SAF) that designs, sells and supports the CFM56 and LEAP. Each partner builds
its own modules (GE the core; Safran the fan, booster, LPT and gearbox — CFM programme structure,
background not re-sourced here) and each sells spare parts for its own content; both run shop
networks.

- **GE Aerospace, Commercial Engines & Services (CES)**: 2025 revenue **$33.3B, 75% services**
  (≈$25B). Internal shop-visit revenue growth **24% in 2025, 19% in 2024, 27% in 2023**. Commercial
  engine deliveries 2,386 (2025) vs 1,911 (2024); LEAP 1,802 vs 1,407. FLIGHT DECK raised priority
  supplier material input >40% y/y, enabling a **26% increase in CES services revenue**. TAT for
  LEAP, CFM56 and GE90 improved >10% y/y in 4Q 2025. Signed a long-term materials agreement with
  Ryanair for ~2,000 CFM56 and LEAP engines. (GE 10-K FY2025.) GE's 1Q 2026 release headlines
  "services revenue grew 39%" (GE 8-K, 1Q 2026). The share of CES services attributable to the
  CFM56 is not disclosed (Unknown U4).
- **Safran Aircraft Engines**: FY2025 group revenue **€31.3B (+14.7%)**, recurring operating income
  **€5.2B (16.6% margin, +150bp)**. Civil engine spare-parts revenue (in USD) **+17.6%**, "driven
  primarily by the CFM56", on "a higher number of shop visits" (mid-single-digit growth) "and a
  higher workscope content"; LEAP spares also grew "in line with the increasing number of shop
  visits performed by third-party MROs". 2026 guidance: revenue growth low-to-mid teens, ROI
  €6.1–6.2B. (Safran press release, 13 Feb 2026; Forecast International and Leeham summaries same
  day.) Safran raised civil aftermarket guidance twice in 2023 to "low-30% range" growth (Aviation
  Week, late 2023) and again in October 2025 on "booming engine aftermarket" (Leeham, 24 Oct 2025).
- **OEM shops**: GE's and Safran's own overhaul shops plus **licensed and joint-venture shops**
  (shops owned with airlines or in which the OEM holds a stake, operating under OEM licence and
  typically guaranteed OEM parts and data access). Specific CFM56 shop-visit counts for the OEM
  network were not found (Unknown U3).

### 3.2 Independents and airline MROs

An **independent MRO** is an engine shop not owned by the engine OEM. It may be a stand-alone
company (StandardAero, Aero Norway, Magnetic), an airline subsidiary that also sells to third
parties (Lufthansa Technik, AFI KLM E&M, Delta TechOps, Turkish Technic, GMF AeroAsia, EgyptAir
Maintenance & Engineering), or an OEM-adjacent company that is independent on the CFM56 (MTU
Maintenance, whose parent MTU Aero Engines is an IAE partner but not a CFM partner). What the
searches returned, with the gaps marked:

| Shop | Listed? | CFM56 role | Capacity / additions found | Source, date |
|---|---|---|---|---|
| **StandardAero** | NYSE: SARO | Largest independent US engine MRO; CFM56-7B Center of Excellence in Dallas; LEAP-1A/-1B line in San Antonio | ">$100 million since 2022 to expand ... and **more than double our shop visit capacity on the CFM56-7B**" via greenfield Dallas CoE; ">$100 million" on LEAP; LEAP and CFM56 DFW programs "reached profitability" in a 2025 quarter; Winnipeg 70,000 sq ft expansion (+~40% footprint) online 3 Sept 2025, adding CF34 and CFM56 capacity | SARO 10-K FY2025; SARO 10-Q 3Q 2025; GlobalAir, Sept 2025 |
| **MTU Maintenance** | parent MTU Aero Engines, Xetra: MTX | CFM56 and V2500 overhaul at Hannover and Zhuhai; Berlin-Brandenburg | "Invested heavily in ramping up capacity, with expansions ... at Hannover ... and Zhuhai, where it overhauls CFM56 and V2500 engines, along with its Berlin facility"; EME Aero (MTU–LHT JV, GTF only) targeting 500 interventions/yr from 2028 | Aviation Week, "Narrowbody Engine Demand Drives MRO Capacity Additions" (2025) |
| **Lufthansa Technik** | parent Deutsche Lufthansa, Xetra: LHA | Large airline-owned MRO with CFM56 engine shop (Hamburg) | No CFM56-specific capacity figure returned; EME Aero JV as above | Aviation Week (2025) |
| **ST Engineering** | SGX: S63 | Singapore-based MRO with CFM56 capability | Named skills shortages and supply chain as its biggest challenges; no capacity figure | Aviation Week (2025) |
| **Aero Norway** | private | CFM56 specialist, Stavanger | Moving to quick-turn services because induction-slot lead times are long; awarded repair-management contract to GE | AVM May 2024; GE press release |
| **FL Technics Engine Services** | parent Avia Solutions Group, private | Kaunas shop | Expanded Kaunas for CFM56 demand; ~70% of work CFM56-7B, remainder -5B and -3 | FL Technics release (2025) |
| **Magnetic MRO** | private | Tallinn-based | "Expects CFM56 market challenges, opportunities 2024" | Aviation Week (2024) |
| **SR Technics** | private (Mubadala) | Zurich; publishes a CFM56-7B capabilities and price catalogue | Catalogue dated 3 June 2026 exists (contents not read) | SR Technics PDF |
| **AFI KLM E&M**, **Delta TechOps**, **Turkish Technic**, **GMF AeroAsia**, **EgyptAir M&E**, **GA Telesis** | AF-KLM (Euronext: AF), Delta (NYSE: DAL), Turkish Airlines (BIST: THYAO), GMF (IDX: GMFI), EgyptAir (state), GA Telesis (private) | All operate CFM56 shops or related businesses; GMF and EgyptAir are FTAI capacity partners (chain map); EgyptAir holds a GE TrueChoice overhaul-consulting agreement; GA Telesis is primarily a USM trader with an engine shop | **No capacity or shop-visit figures returned for any of these** (Unknown U5) | Chain map; Amwal Al Ghad (EgyptAir–GE) |
| **Aviation AirWerks / Stratton Aviation** | private | Teardown and disassembly of CFM56-5B/-7B in North America | Expanded partnership for 2026 | ePlaneAI (2025/26) |

### 3.3 FTAI

From the chain map (D5 owns the detail): Montreal (ex-Lockheed Martin Commercial Engine Solutions),
Miami (QuickTurn), Rome NY, a planned 113,000 sq ft Lisbon site (300+ modules/yr), plus capacity
partnerships with GMF Indonesia and EgyptAir. 296 CFM56 modules refurbished in Q2 2026, 566 in
1H 2026, 1,200 forecast for 2026, 3,000/yr stated capacity. For scale only: if one CFM56 is three
major modules (an assumption about FTAI's counting convention that D5 must confirm), 1,200 modules
is about 400 engine-equivalents, or roughly **17% of a 2,350-visit year**; 3,000 modules would be
about 1,000 engine-equivalents, or **~43%**. Modules are sold individually and many go into engines
that also visit other shops, so these are not shop-visit shares; they size FTAI's material
throughput against the market.

### 3.4 OEM share versus independents

No source found gives the OEM network's share of CFM56 shop visits (Unknown U3). What the sources
do establish: the CFM56 aftermarket is ~85% spares and T&M (Safran), so most visits are not under
OEM flight-hour contracts; GE describes the CFM56 as "an open network ... with multiple providers
who compete and invest to win shop visits" (GE Aerospace, 2026); Safran attributes part of its LEAP
spares growth to "the increasing number of shop visits performed by third-party MROs" (13 Feb 2026),
which implies the OEM tracks and reports third-party share internally without disclosing it.

---

## 4. Numbers

### 4.1 Demand: CFM56 shop visits per year

| Period | Figure | Source | Date |
|---|---|---|---|
| 2019 (pre-downturn peak) | "just above 2,000" annual CFM shop visits, "almost all of them CFM56-5B and -7B" | Safran via Aviation Week, "Safran Sees Leap Aftermarket Emerging By Mid-Decade" | c. late 2023/early 2024 |
| 2020–2023 | Not found year by year | — | Unknown U2 |
| 2024 | Safran "sees total annual CFM shop visits topping 2,000 again in 2024, with some help from the Leap family" | same | same |
| 2024→2025 | IBA "predicts 40 per cent increase in shop visits from 2024 to 2025" (headline; scope — all engines or CFM56 — not captured) | Aviation Week | 2024 |
| 2025 | CFM56 shop visits grew "mid-single-digit" with a "higher proportion of full work scope shop visits" | Safran FY2025 release / Forecast International | 13 Feb 2026 |
| 2025–26 peak view | "CFM56-variant shop visits are expected to peak in the 2025-26 timeframe, at about 2,500 per year" | Safran via Aviation Week | c. 2023/24 |
| 2026 and 2027 | "entered the year projecting about 2,300"; "expanded the range to 2,300–2,400"; "probably closer to 2,400" | GE Aerospace via Aviation Week, "CFM56 Overhaul Demand Remains Strong" | 2026 |
| Through 2028 | "2,300–2,400 range through 2028" | same | 2026 |
| Apex | "around the 2027-2028 time period, followed by a gradual fade" | same | 2026 |
| First-shop-visit peak | CFM56 and V2500 first shop visits peak in 2027 | Visual Approach Analytics (headline) | 2025/26 |
| 2030 (all CFM) | "more than 4,000 shop visits annually, roughly split between Leaps and previous-generation models" | Safran via Aviation Week | c. 2023/24 |
| V2500 2025 | ~1,400 shop visits | Aviation Week V2500 data tool | 2024/25 |
| V2500 10-year | >7,800 overhaul SVs and 3,142 LLP SVs | same | same |

### 4.2 Retirements and installed base

| Item | Figure | Source | Date |
|---|---|---|---|
| CFM56 retirement rate, original 2026 guidance | 3–4% of fleet | GE via Aviation Week | 2026 |
| revised, start of 2026 | 2–3% | same | 2026 |
| current | 1.5–2% | same | 2026 |
| GE 2026 outlook assumption | ~2% of total fleet; 1Q 2026 actual "below 1%" | GE Aerospace IR, "Recent events: your questions answered" | 2026 |
| V2500 | "no retirement surge expected over next five years" | IAE via Aviation Week | 2024/25 |
| CFM56 in service | ~23,000 (2024); ~23,000 (2019) | GE Aviation & GECAS Investor Day (18 Jun 2019) and Safran media (2024) — attribution between the two not captured | 2019; 2024 |
| CFM56 in service | ">19,000 flying" | Safe Fly Aviation (blog) | 2026 |
| Fleet maturity 2019 | 57% no first SV; 21% one SV | GE Investor Day | Jun 2019 |
| Fleet maturity 2024 | 70% had 0 or 1 SV | Safran media | 2024 |
| Fleet maturity 2026 | "over half" no SV; "another quarter" one SV | Safe Fly Aviation (blog) | 2026 |

### 4.3 OEM financials

| Item | Figure | Source | Date |
|---|---|---|---|
| GE CES revenue 2025 | $33.3B, 75% services | GE 10-K FY2025 | Feb 2026 |
| GE internal shop-visit revenue growth | +24% (2025), +19% (2024), +27% (2023) | GE 10-K FY2025 | Feb 2026 |
| GE CES services revenue growth 2025 | +26% | GE 10-K FY2025 | Feb 2026 |
| GE commercial engine deliveries | 2,386 (2025) vs 1,911 (2024); LEAP 1,802 vs 1,407 | GE 10-K FY2025 | Feb 2026 |
| GE services revenue 1Q 2026 | +39% | GE 1Q 2026 release (8-K) | Apr 2026 |
| GE external spares | +35% y/y; record $42.2M/day shipped | Aviation Week | late 2023 |
| Safran revenue 2025 | €31.3B, +14.7% | Safran | 13 Feb 2026 |
| Safran recurring operating income 2025 | €5.2B, 16.6% | Safran | 13 Feb 2026 |
| Safran civil spares (USD) 2025 | +17.6%, "driven primarily by the CFM56" | Safran | 13 Feb 2026 |
| Safran LEAP deliveries 2025 | 1,802 (+28%); 4Q 562 (+49%) | Safran | 13 Feb 2026 |
| Safran 2026 guidance | revenue growth low-to-mid teens; ROI €6.1–6.2B | Safran | 13 Feb 2026 |
| Safran civil aftermarket 2023 | guidance raised twice to "low-30% range" growth | Aviation Week | late 2023 |
| CFM56 aftermarket mix | 85% spares and T&M (vs ~40% LEAP) | Safran via Aviation Week | c. 2023/24 |
| LEAP LTA penetration target | 60–70% by 2030 | same | same |

### 4.4 Spare-parts pricing

| Item | Figure | Source | Date |
|---|---|---|---|
| Trend | "around 10% per year" | Aviation Week | late 2023 |
| 1 Nov 2022 increase | "double-digit" | Aviation Week | late 2023 |
| Aug 2023 increase | "high-single-digit" (GE and Safran) | Aviation Week | late 2023 |
| Safran pricing rule | "above inflation by 3 to 4 points ... continue on that path at least for some years" | Safran CEO via Aviation Week | late 2023 |
| 2024, 2025, 2026 catalog increases | Not found | — | Unknown U1 |
| CFM56-7 LLP stack | "$4M" | Aircraft Value News (headline) | not captured |
| CFM56 LLP stack | "north of $3m"; HPT LLP exchange "easily $0.5m"; fan/booster $0.5–0.7m | Leeham News (Bjorn's Corner) | 3 Mar 2017 |
| CFM56-7B HPT disc | $420,000 new; 20,000-cycle limit | Safe Fly Aviation (blog) | 2026 |
| LLP module "removal costs" | $150,000–$400,000 per module (meaning unclear) | Safe Fly Aviation (blog) | 2026 |

### 4.5 Shop-visit cost build

| Item | Figure | Source | Date |
|---|---|---|---|
| Material share | 60–70% | Air Cargo Week | 2025/26 |
| Labour share | 20–30% | Air Cargo Week | 2025/26 |
| Repairs and other | 10–20% | Air Cargo Week | 2025/26 |
| LLP share of parts cost (CFM56) | 40–60% | Safe Fly (blog) | 2026 |
| HPT blades and vanes share | 15–25% | Safe Fly (blog) | 2026 |
| Labour share (CFM56) | 15–20% | Safe Fly (blog) | 2026 |
| Light SV | $650k–$900k | Safe Fly (blog) | 2026 |
| Performance restoration | $1.2M–$1.6M | Safe Fly (blog) | 2026 |
| Heavy SV with LLPs | $2.1M–$2.8M | Safe Fly (blog) | 2026 |
| Full overhaul | $3.5M–$4.2M | Safe Fly (blog) | 2026 |
| Widebody full LLP stack (for contrast) | $8M–$12M | Air Cargo Week | 2025/26 |

### 4.6 Asset values and lease rates (worked-example inputs)

| Item | Figure | Source | Date |
|---|---|---|---|
| CFM56-7B green-time lease rate | $42,000–$48,000/month | Safe Fly (blog) | 2026 |
| Green time, typical | 4,000–8,000 cycles remaining | Safe Fly (blog) | 2026 |
| CFM56-7B green-time value | $2.8M–$3.4M | Safe Fly (blog) | 2026 |
| Low-life engine as teardown feedstock | $0.8M–$1.2M acquisition; USM recovery $1.6–2.2M; net $0.4–0.8M before repair cost | Safe Fly (blog) | 2026 |
| USM market size | >$4B/yr, CFM56 largest segment | Safe Fly (blog) | 2026 |
| LLP life share of used-engine value | 60–80%; two CFM56-7Bs at 10,000 CSN differ by $1.6M on LLP life alone | Safe Fly (blog) | 2026 |
| Lease-rate direction | "lessor's market ... engine lease rates and market values escalate" | IBA via AJOT/AviTrader | 25 Apr 2024 |

### 4.7 Capacity constraints

| Item | Figure | Source | Date |
|---|---|---|---|
| MRO slot wait increase | +2–3 months, up to 6 months | Bain | 2024 |
| Demand vs capacity | demand to exceed capacity by >17% before 2030 | Bain | 2024 |
| Repair lead times, severe cases | >200 days (new-gen programmes) | AVM Magazine | 2025 |
| Technician shortage | two-thirds of MRO operators struggle to hire | Oliver Wyman MRO survey (>150 respondents) | Apr 2026 |
| Labour-rate inflation 2025 | 5.5–6.0% | Oliver Wyman | Apr 2026 |
| Attrition outlook | >50% expect worse next year | Oliver Wyman | Apr 2026 |
| Next-gen narrowbody shop costs vs expectation | two-thirds report +21% or more; a quarter +50% or more | Oliver Wyman | Apr 2026 |
| Global MRO market | >$136B (2025); ~$140B (2026) | Oliver Wyman | Apr 2026 |
| GE priority-supplier material input | +40% y/y | GE 10-K FY2025 | Feb 2026 |
| GE TAT (LEAP, CFM56, GE90) | >10% better y/y in 4Q 2025 | GE 10-K FY2025 | Feb 2026 |
| Engine stand shortage | Not found | — | Unknown U6 |
| HPT blade / casting / forging lead times | Not found as numbers; "parts supply remains a capacity constraint with every OEM" | Aviation Week | 2025 |

### 4.8 Independent capacity additions

| Shop | Addition | Source | Date |
|---|---|---|---|
| StandardAero Dallas | >$100M since 2022; CFM56-7B capacity more than doubled | SARO 10-K FY2025 | Feb 2026 |
| StandardAero San Antonio | >$100M LEAP-1A/-1B | SARO 10-K FY2025 | Feb 2026 |
| StandardAero Winnipeg | +70,000 sq ft (+~40%), CF34 and CFM56, online 3 Sept 2025 | GlobalAir | Sept 2025 |
| MTU Hannover, Zhuhai, Berlin | expansions (CFM56/V2500 at Zhuhai) | Aviation Week | 2025 |
| EME Aero (MTU–LHT, GTF) | 500 interventions/yr from 2028 | Aviation Week | 2025 |
| FL Technics Kaunas | expanded; ~70% CFM56-7B | FL Technics | 2025 |
| FTAI Lisbon | 113,000 sq ft, 300+ modules/yr (planned) | chain map (FTAI) | 2026 |
| FTAI stated capacity | 3,000 modules/yr | chain map (FTAI Q2 2026) | Jul 2026 |

---

## 5. Constraints and bottlenecks

1. **Induction slots.** Shops reported being at full capacity "over the past year" (Aviation Week,
   2025); slot waits rose 2–6 months (Bain, 2024). The slot, not the TAT, became the binding
   constraint on an operator's engine availability, which raised the value of anything that avoids
   a full induction: quick-turns, module exchanges, green-time leases.
2. **Labour.** Two-thirds of MROs cannot hire enough technicians; labour-rate inflation 5.5–6.0%;
   attrition expected to worsen (Oliver Wyman, Apr 2026). StandardAero and ST Engineering named it
   their top constraint (Aviation Week, 2025). Labour is 20–30% of a visit, so a 6% wage rise adds
   roughly 1.2–1.8 points to total visit cost per year on its own.
3. **New parts.** Parts supply constrained "every OEM" (Aviation Week, 2025); GE reports a >40%
   increase in priority-supplier input in 2025 and >10% TAT improvement in 4Q 2025 (GE 10-K), so
   the OEM's own view is that the worst of the parts constraint eased in late 2025. No numeric
   lead times for HPT blades, castings or forgings were found (Unknown U6).
4. **USM.** Thin supply because retirements are 1.5–2% rather than 3–4% (GE, 2026); "seller's
   market for used parts" (Aviation Week). This pushes shops back to new OEM parts at escalated
   list, and it is the central supply constraint on FTAI's and the independents' material-solutions
   model (D3).
5. **Engine stands and floor.** Capacity additions are measured in square feet (StandardAero
   Winnipeg +70,000; FTAI Lisbon 113,000) because stands and floor are the physical limit on
   work-in-progress; no engine-stand shortage data was found (Unknown U6).
6. **Price.** Spare-parts list escalation ~10%/yr (2022–23) with a stated policy of inflation +3–4
   points (Safran) means the cost of a given workscope rises every year independent of shop
   competition.
7. **Demand ceiling and timing.** The OEMs' own forecast caps the market at 2,300–2,400 visits
   through 2028 with a fade after; a shop or module factory adding capacity now is adding it into a
   plateau. Where the fade begins and how steep it is depends on retirements, which were
   over-forecast by 1.5–2.5 points in 2025–26.

---

## 6. Tensions

- **T1. Peak year and level.** Safran (c. 2023/24): CFM56 shop visits peak **2025–26 at ~2,500/yr**.
  GE (2026): **2,300–2,400 through 2028, apex 2027–28**. Visual Approach (2025/26): *first* shop
  visits peak in **2027**. The later GE view is both lower and later than Safran's earlier one.
- **T2. Installed base.** ~**23,000** CFM56 in service (GE 2019 / Safran 2024 materials) versus
  **>19,000** flying (Safe Fly Aviation, 2026). The gap may be in-service versus total, or dated
  versus current, or source quality; not resolvable from what was found.
- **T3. Retirement rate.** GE's own 2026 assumption moved from **3–4%** to **2–3%** to **1.5–2%**
  within roughly a year, with 1Q 2026 actuals **below 1%**: the same source disagreeing with itself
  over time, which is the mechanism behind the raised shop-visit range.
- **T4. LLP stack price.** Leeham (2017) **>$3M**; Aircraft Value News **$4M** for the CFM56-7 (date
  not captured); Safe Fly's "heavy SV with LLPs" **$2.1–2.8M all-in** cannot include a full stack at
  either price. Different scopes, not necessarily different facts, but the writer must not add them.
- **T5. Cost split.** Air Cargo Week: labour **20–30%**; Safe Fly: labour **15–20%** (CFM56). Both
  secondary; neither gives a shop-level data source.
- **T6. Shop visits 2024.** Safran forecast CFM shop visits "topping 2,000 again in 2024" *including*
  LEAP, while IBA headlined a **40% increase** 2024→2025 (scope not captured). If both are about the
  same population, 2025 would be ~2,800+; Safran's own 2025 report says CFM56 visits grew only
  mid-single digits. Most likely different populations; recorded because the writer will meet both.
- **T7. Fleet maturity.** 2024: 70% of fleet with 0–1 shop visits (Safran). 2026: "over half" with
  none plus "another quarter" with one, i.e. ~75% (Safe Fly). Directionally the same; the 2026
  figure comes from a weaker source.
- **T8. Parts constraint, easing or not.** GE 10-K (Feb 2026): TAT improved >10% in 4Q 2025, supplier
  input +40%. Oliver Wyman (Apr 2026) and AVM (2025): labour and material shortages remain the
  primary disruptors; two-thirds report next-gen shop costs running 21%+ over expectation. The OEM
  reports easing; the operator survey does not.

---

## 7. Unknowns

- **U1. Catalog escalation 2024, 2025, 2026.** Only the Nov 2022 (double-digit) and Aug 2023
  (high-single-digit) increases and Safran's "inflation + 3–4 points" rule were found. Resolve with
  Aviation Week/Aircraft Commerce coverage of each year's CFM price revision, or GE/Safran earnings
  call Q&A on "price".
- **U2. Shop-visit counts 2020–2023.** Only the 2019 level (~2,000+) and the 2024 forecast
  ("topping 2,000") were found. Resolve from Safran capital-markets-day decks (the
  safran-group.com media downloads 397180 / 448184 returned in search but not read) or the GE
  Aerospace Bernstein presentation of 27 May 2026.
- **U3. OEM versus independent share of CFM56 shop visits.** No estimate found. Resolve with
  Aviation Week/Cirium shop-visit-by-provider data or the Oliver Wyman fleet forecast's provider
  split.
- **U4. CFM56 share of GE CES services revenue.** Not disclosed in the 10-K. GE has historically
  described the CFM56 as the largest services contributor; a number would need an investor
  presentation or call transcript (the 22 Jan 2026 webcast transcript URL was returned, not read).
- **U5. Capacity of the named airline MROs.** AFI KLM E&M, Delta TechOps, Turkish Technic, GMF
  AeroAsia, EgyptAir M&E, GA Telesis, Lufthansa Technik and ST Engineering: no CFM56 inductions-
  per-year or expansion figures returned. Resolve via each company's annual report or trade-press
  shop profiles.
- **U6. Engine-stand shortages and HPT blade / casting / forging lead times.** No numbers found.
  Resolve via Aviation Week supply-chain coverage, PCC/Howmet commentary, or GE call Q&A.
- **U7. Module-exchange pricing.** No source gives the exchange fee or a worked price for a CFM56
  HPT or core exchange; Safe Fly's "$150,000–$400,000 removal cost per module" is ambiguous. D5
  may find it in FTAI's investor materials or the In Practise interview ("FTAI Aviation: CFM56
  repair and module swap", URL returned, not read).
- **U8. Value of a freshly overhauled full-stack CFM56-7B** versus a green-time unit. Needed to
  close the worked example. Resolve via IBA/Ascend/mba engine value tables.
- **U9. IAE "FleetCare".** Not found as a current product; only EngineWise. Resolve on the P&W
  services site.
- **U10. Dates.** Several Aviation Week articles were returned without publication dates (noted
  "c. 2023/24" or "2025"). The writer should confirm before quoting.

---

## 8. Terms introduced

- **Shop visit (SV)**: removal of an engine for off-wing work at an engine shop.
- **Engine shop**: Part 145-approved facility with OEM data and tooling that disassembles, repairs and tests engines.
- **Engine stand**: wheeled fixture that holds an engine or module during work; a physical capacity limit.
- **Test cell**: instrumented enclosure where a rebuilt engine is run to prove performance before release.
- **EGT margin**: gap between actual hot-day takeoff exhaust gas temperature and the certified limit; shrinks with wear.
- **Performance restoration (PR)**: hot-section rebuild to recover EGT margin.
- **Life-limited part (LLP)**: rotating disc, spool, shaft or seal with a fixed cycle limit regardless of condition.
- **Cycle**: one takeoff and landing.
- **LLP stack**: the full set of LLPs in an engine; its remaining life largely sets used-engine value.
- **LLP stagger**: the mismatch of remaining lives across LLPs that causes repeated LLP-forced removals if only the limiting part is replaced.
- **Workscope**: specification of what is opened, replaced, repaired or exchanged in a visit.
- **Module**: self-contained engine section (fan/booster, core, LPT, gearbox) that can be exchanged as a unit.
- **Module exchange**: replacing a module with a serviceable one from inventory, paying for life transferred plus a fee.
- **Quick-turn**: minimum-scope, short-TAT repair that avoids full disassembly.
- **Full overhaul / zero-time**: all modules to overhaul standard with a full LLP stack.
- **Turnaround time (TAT)**: induction to release.
- **Induction / induction slot**: acceptance of an engine into work; the scheduled date for it.
- **Used serviceable material (USM)**: parts recovered from torn-down engines, inspected and recertified.
- **Teardown / part-out**: disassembling a retired engine to sell its parts.
- **Green time**: remaining usable life before the next shop visit or LLP limit; a **green-time lease** rents it.
- **PMA**: FAA Parts Manufacturer Approval; a non-OEM part approved as a replacement (D4).
- **DER repair**: repair approved through an FAA Designated Engineering Representative rather than OEM data (D4).
- **Catalog list price**: the OEM's published spare-parts price, revised at least annually.
- **Time-and-materials (T&M)**: pay-per-visit; the operator carries cost and volume risk.
- **Long-term service agreement (LTSA) / rate-per-flight-hour (RPFH)**: fixed payment per flight hour; the OEM carries the risk and controls the workscope.
- **TrueChoice (Flight Hour, Overhaul, Material, Transitions)**: GE Aerospace's CFM/GE services menu, defined in 2.3.
- **EngineWise**: Pratt & Whitney / IAE services brand for the V2500 and other P&W engines.
- **Licensed / joint-venture shop**: shop operating under OEM licence or with OEM equity, with guaranteed parts and data access.
- **Independent MRO**: engine shop not owned by the engine OEM, including airline-owned third-party MROs.
- **Material solutions**: a shop's or OEM's package of USM, repaired parts and PMA to reduce the new-parts bill.
- **Maintenance reserve**: per-hour/per-cycle payments a lessee makes to a lessor against future shop-visit and LLP cost (D6).

---

## 9. Sources

1. Aviation Week, "CFM56 Overhaul Demand Remains Strong, GE Aerospace Says" (2026). https://aviationweek.com/mro/aircraft-propulsion/cfm56-overhaul-demand-remains-strong-ge-aerospace-says
2. GE Aerospace Investor Relations, "Recent events: your questions answered" (2026). https://www.geaerospace.com/news/investor-relations/ir-updates/recent-events-your-questions-answered
3. Visual Approach Analytics, "CFM56 and V2500 engines to reach peak in first shop visits in 2027" (2025/26). https://app.visualapproach.io/research/cfm56-and-v2500-engines-to-reach-peak-in-first-shop-visits-in-2027
4. Aviation Week, "Safran Sees Leap Aftermarket Emerging By Mid-Decade" (c. 2023/24). https://ngtest.aviationweek.com/mro/aircraft-propulsion/safran-sees-leap-aftermarket-emerging-mid-decade
5. Aviation Week, "CFM Aftermarket Shifting To Long-term Agreements, Safran Says" (c. 2023/24). https://aviationweek.com/mro/aircraft-propulsion/cfm-aftermarket-shifting-long-term-agreements-safran-says
6. Aviation Week, "Parts Price Hikes Help Boost Safran, GE Aftermarket Sales" (late 2023). https://ngtest.aviationweek.com/mro/aircraft-propulsion/parts-price-hikes-help-boost-safran-ge-aftermarket-sales
7. Aviation Week, "MRO Memo: A Seller's Market For Used Parts". https://aviationweek.com/mro/workforce-training/mro-memo-sellers-market-used-parts
8. Aviation Week, "Magnetic Expects CFM56 Market Challenges, Opportunities In 2024" (2024). https://m.aviationweek.com/mro/aircraft-propulsion/magnetic-expects-cfm56-market-challenges-opportunities-2024
9. Aircraft Value News, "Engine Life Limited Parts Pricing Continues to Rise: $4M for CFM56-7" (date not captured). https://www.aircraftvaluenews.com/engine-life-limited-parts-pricing-continues-to-rise-4m-for-cfm56-7
10. GE Aerospace press release, "Safair signed GE's TrueChoice Overhaul agreement for CFM56 engines". https://www.geaerospace.com/news/press-releases/services/safair-signed-ges-truechoice-overhaul-agreement-cfm56-engines
11. GE Aerospace press release, "TAAG signed GE's TrueChoice Overhaul agreement for CFM56 engines". https://geaerospace.com/news/press-releases/services/taag-signed-ges-truechoice-overhaul-agreement-cfm56-engines
12. GE Aerospace press release, "GE expands TrueChoice Flight Hour agreement with Southwest Airlines for CFM56-7B". https://www.geaerospace.com/news/press-releases/services/ge-expands-truechoice-flight-hour-agreement-southwest-airlines-cfm56-7b
13. GE Aerospace press release, "Aero Norway awards repair management contract to GE Aviation". https://www.geaerospace.com/press-release/services/aero-norway-awards-repair-management-contract-ge-aviation
14. GE Aerospace blog, "Overhauling services". https://blog.geaerospace.com/people/overhauling-services/
15. Amwal Al Ghad, "EgyptAir inks GE's TrueChoice agreement for overhaul consulting". https://en.amwalalghad.com/?p=50461
16. American Machinist, "GE Aviation Expands MRO with Southwest Airlines". https://www.americanmachinist.com/news/ge-aviation-expands-mro-southwest-airlines
17. Air Cargo Week, "The true cost of engine maintenance" (2025/26). https://aircargoweek.com/the-true-cost-of-engine-maintenance/
18. Leeham News, Bjorn Fehrm, "Bjorn's Corner: Aircraft engine maintenance, Part 1" (3 Mar 2017). https://leehamnews.com/2017/03/03/bjorns-corner-aircraft-engines-maintenance-part-1/
19. Safe Fly Aviation (consultancy blog, 2026): "Engine Shop Visit Costs Worldwide 2026" https://safefly.aero/?p=15606 ; "CFM56 Engine Market Report 2026" https://safefly.aero/cfm56-engine-market-report-2026/ ; "Aircraft Engine LLP Management" https://safefly.aero/engine-llp-management-explained/ ; "Life Limited Parts (LLP) in Aviation" https://safefly.aero/blog-life-limited-parts-llp-in-aviation/ ; "CFM56-7B Engine Availability Report 2026" https://safefly.aero/?p=15628 ; "What Determines Aircraft Engine Overhaul Costs?" https://safefly.aero/blog-aircraft-engine-overhaul-cost-drivers/
20. Aviation Week, "Narrowbody Engine Demand Drives MRO Capacity Additions" (2025). https://aviationweek.com/mro/aircraft-propulsion/narrowbody-engine-demand-drives-mro-capacity-additions
21. Aviation Week, "Engine Shops' Worldwide Investing To Boost Capacity". https://aviationweek.com/special-topics/asset-utilization/engine-shops-worldwide-investing-boost-capacity
22. Aviation Week, "Engine Shops Adjust Capacity, Strategies To Cater For Recovery". https://aviationweek.com/mro/engine-shops-adjust-capacity-strategies-cater-recovery
23. Aviation Week, "Fast 5: Where is the Engine Aftermarket Headed?". https://aviationweek.com/mro/aircraft-propulsion/fast-5-where-engine-aftermarket-headed
24. Bain & Company, "Get a step ahead of the engine maintenance capacity crunch" (2024). https://bain.com/globalassets/noindex/2024/bain_brief_get_a_step_ahead_of_the_engine_maintenance_capacity_crunch.pdf (also hosted at https://mroevents.aviationweek.com/wp-content/uploads/2025/10/v1_GetaStepAheadOfTheEngineMaintenance_AllPages.pdf)
25. AVM Magazine, "The Engines Capacity Crunch" (2025). https://avm-mag.com/the-engines-capacity-crunch
26. AVM Magazine, "Inside the Engine MRO Supply Chain: Why Repair Delays Are Rising" (2025). https://avm-mag.com/inside-the-engine-mro-supply-chain-why-repair-delays-are-rising-and-whats-driving-them
27. AVM Magazine / Air Cargo Week, "From PW1100G to CFM56: The Engine Maintenance Trends Shaping 2026". https://avm-mag.com/from-pw1100g-to-cfm56-the-engine-maintenance-trends-shaping-2026 ; https://aircargoweek.com/from-pw1100g-to-cfm56-the-engine-maintenance-trends-shaping-2026/
28. Air Cargo Week, "Engine Maintenance Trends and Capacity Outlook". https://aircargoweek.com/?p=105530
29. Aero Norway, editorial in AVM (May 2024). https://aeronorway.no/wp-content/uploads/2024/05/Aero-Norway-editorial-AVM-MAY-2024.pdf
30. General Electric Co., Form 10-K FY2025 (filed Feb 2026). https://www.sec.gov/Archives/edgar/data/40545/000004054526000008/ge-20251231.htm
31. GE Aerospace, 1Q 2026 earnings release (8-K exhibit, Apr 2026). https://www.sec.gov/Archives/edgar/data/40545/000004054526000026/ge1q2026earningsrelease.htm
32. GE Aerospace, 2Q 2026 earnings release (8-K exhibit, Jul 2026). https://www.sec.gov/Archives/edgar/data/40545/000004054526000047/ge2q2026earningsrelease.htm
33. GE Aerospace, 4Q 2025 webcast transcript (22 Jan 2026; returned, not read). https://www.geaerospace.com/sites/default/files/geaerospace_webcast_transcript_01222026.pdf
34. GE Aerospace, Bernstein Strategic Decisions Conference presentation (27 May 2026; returned, not read). https://www.geaerospace.com/sites/default/files/geaerospace_bernstein_strategic_decisions_conference_presentation_052726.pdf
35. GE Aerospace, "Much more service recovery, it's opportunity" and GE node 5288 (2026). https://geaerospace.com/news/articles/technology/much-more-service-recovery-its-opportunity ; https://www.geaerospace.com/node/5288
36. GE Aviation & GECAS Investor Day (18 Jun 2019). https://www.ge.com/sites/default/files/GE-Aviation-%26-GECAS-Investor-Day-061819.pdf
37. CFM International, Paris Air Show media briefing (Jun 2019). https://www.cfmaeroengines.com/wp-content/uploads/2019/06/CFM-Media-Briefing-2019-PAS-Final.pdf
38. Safran media downloads (returned, not read): https://www.safran-group.com/download/media/397180 ; https://www.safran-group.com/fr/download/media/448184 ; https://www.safran-group.com/fr/download/media/449895
39. Safran, "Safran reports excellent financial performance in 2025 and raises its 2028 ambitions" (13 Feb 2026). https://www.safran-group.com/pressroom/safran-reports-excellent-financial-performance-2025-and-raises-its-2028-ambitions-2026-02-13
40. Forecast International, "Safran Revenue Up 15% in 2025, LEAP Deliveries Surge 28%" (13 Feb 2026). https://flightplan.forecastinternational.com/2026/02/13/safran-revenue-up-15-in-2025-leap-deliveries-surge-28/
41. Leeham News, "Safran hails 'outstanding' 2025; prepares for Airbus ramp-up" (13 Feb 2026). https://leehamnews.com/2026/02/13/safran-hails-outstanding-2025-prepares-for-airbus-ramp-up/
42. Leeham News, "Safran raises full-year guidance on record LEAP output and booming engine aftermarket" (24 Oct 2025). https://leehamnews.com/2025/10/24/safran-raises-full-year-guidance-on-record-leap-output-and-booming-engine-aftermarket/
43. Leeham News, "GE sees 2,500 LEAP engine deliveries by 2028" (24 Feb 2025). https://leehamnews.com/2025/02/24/ge-sees-2500-leap-engine-deliveries-by-2028-enough-for-more-than-1000-a320neos-and-737-maxes/
44. AirInsight, "CFM56 and LEAP aftermarket sales are a boost for Safran". https://airinsight.com/cfm56-and-leap-aftermarket-sales-are-a-boost-for-safran/
45. StandardAero, Inc., Form 10-K FY2025 (filed Feb/Mar 2026). https://www.sec.gov/Archives/edgar/data/2025410/000119312526072618/saro-20251231.htm
46. StandardAero, Inc., Form 10-Q for quarter ended 30 Sep 2025. https://www.sec.gov/Archives/edgar/data/2025410/000119312525274305/saro-20250930.htm
47. StandardAero, Inc., earnings release exhibit 99.1 (2026). https://www.sec.gov/Archives/edgar/data/2025410/000202541026000007/saro-ex99_1.htm
48. StandardAero, Inc., IPO prospectus 424B4 (Oct 2024). https://www.sec.gov/Archives/edgar/data/2025410/000119312524231156/d838237d424b4.htm
49. GlobalAir, "StandardAero's Winnipeg expansion adds CF34 and CFM56 engine capacity" (Sept 2025). https://www.globalair.com/articles/standardaeros-winnipeg-expansion-adds-cf34-and-cfm56-engine-capacity/12646
50. StandardAero, CFM56-7B capability page. https://standardaero.com/engines/cfminternational/cfm567b
51. FL Technics, Kaunas engine-shop expansion release (2025). https://fltechnics.com/?p=194689
52. ePlaneAI, "Aviation AirWerks and Stratton expand engine partnership for 2026". https://www.eplaneai.com/de/news/aviation-airwerks-and-stratton-expand-engine-partnership-for-2026
53. RTX / Pratt & Whitney, "IAE AG and FTAI Aviation Sign Strategic V2500 Engine Maintenance Services Agreement" (6 Jun 2024). https://www.rtx.com/prattwhitney/newsroom/news/2024/06/06/iae-ag-and-ftai-aviation-sign-strategic-v2500-engine-maintenance-services-agreem
54. Aviation Week, "IAE: No V2500 Retirement Surge Expected Over Next Five Years". https://ngtest.aviationweek.com/mro/aircraft-propulsion/iae-no-v2500-retirement-surge-expected-over-next-five-years
55. Aviation Week, "Data Tool: The Future Of IAE V2500 Engine". https://ngstage.aviationweek.com/mro/aircraft-propulsion/data-tool-future-iae-v2500-engine
56. Oliver Wyman, "The new MRO supply paradigm" (Apr 2026). https://www.oliverwyman.com/our-expertise/insights/2026/apr/aviation-mro-labor-and-material-supply-chain-paradigm.html
57. ePlaneAI, "Survey highlights shortages and rising costs in aviation maintenance sector" (2026). https://www.eplaneai.com/de/news/survey-highlights-shortages-and-rising-costs-in-aviation-maintenance-sector
58. Aviation Week, "IBA predicts 40 per cent increase in shop visits from 2024 to 2025" (2024). https://aviationweek.com/mro/iba-predicts-40-cent-increase-shop-visits-2024-2025
59. AJOT / AviTrader, "It's a lessor's market, says IBA, as engine lease rates and market values escalate" (25 Apr 2024). https://www.ajot.com/news/its-a-lessors-market-says-iba-as-engine-lease-rates-and-market-values-escalate ; https://avitrader.com/2024/04/25/iba-says-its-a-lessors-market
60. SR Technics, CFM56-7B capabilities and price catalogue (3 Jun 2026; returned, not read). https://www.srtechnics.com/media/zgcnmf3o/cfm56-7b-sr-technics-capabilitiesprice-catalogue-03062026.pdf
61. In Practise, "FTAI Aviation: CFM56 repair and module swap" (returned, not read). https://inpractise.com/articles/ftai-aviation-cfm56-repair-and-module-swap
62. GE Aerospace press release, "Willis Lease CFM56 spare engine order valued at $540 million". https://www.geaerospace.com/news/press-releases/joint-ventures/willis-lease-cfm56-spare-engine-order-valued-540-million
63. MRO Management, "Vallair completes sale of two engines to TrueAero for teardown". https://www.aviationbusinessnews.com/mro/vallair-completes-sale-of-two-engines-to-trueaero-for-teardown/
64. Aviation Week, "Leap Aftermarket Poised For Growth". https://aviationweek.com/mro/supply-chain/leap-aftermarket-poised-growth
65. Motley Fool via AOL, "GE (GE) Q4 2025 Earnings Call Transcript" (Jan 2026). https://www.aol.com/articles/ge-ge-q4-2025-earnings-180029260.html
66. FTAI figures: Phase 1 chain map (/home/user/SPOT/ftai-primer/research/chain-map.md), citing FTAI Q2 2026 results release (29 Jul 2026) and FY2025 10-K.
