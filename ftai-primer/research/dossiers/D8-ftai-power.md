# D8 — FTAI Power, the Mod-1 generator set, and the data-center power market it sells into

Research date: 2026-10-03. Searches used: 18 of 18. WebFetch unavailable; all content reached through
web search, including sec.gov-restricted search for filings. Where a figure came through a secondary
summary (call-highlight services, a repost of a press release, an X post summarising a call) rather
than the primary document, that is said in the row. Nothing here is a view on the stock.

---

## 1. Summary

FTAI Power is a platform, launched 30 December 2025, that converts retired or mid-life CFM56 jet
engines into "Mod-1" 25 MW trailer-mounted natural-gas generator sets for data centers. FTAI
states capacity for over 100 units a year, first delivery by Q4 2026 and 100 units in 2027.
Packaging and distribution run through J&F Power Systems LLC, a joint venture with China's Jereh
Group (SZSE: 002353), which on 22 July 2026 signed a five-year master supply agreement with an
unnamed "leading international cloud service provider" and an initial $1.465 billion purchase
order, delivered in batches through November 2027, paid in milestones from an advance at signing
to commissioning, with a performance adjustment capped at 10%. The unit count and price are not
disclosed; at 100 units the order would imply $14.65M per unit, or $586/kW. Management guided 2027
Power EBITDA at $450M (one summary says $450–750M). Mod-1 is described as 35–40% efficient at a
heat rate of about 9,000 Btu/kWh, deployable in about two weeks. It sells into a market where the
IEA expects global data-center electricity use to more than double to ~945 TWh by 2030, where
GE Vernova's gas-turbine backlog plus reservations reached 116 GW at Q2 2026 with slots being
sold for 2031, Siemens Energy's backlog 69 GW with lead times of three-plus years, and where
behind-the-meter gas generation is forecast at roughly 4.5 GW a year in the US to 2030.

---

## 2. Mechanics

### 2.1 What a gas-turbine generator set is

A **gas turbine** is a rotating engine that compresses air, burns fuel in it, and expands the hot
gas through turbine stages. The compressor-combustor-turbine assembly that produces hot pressurised
gas is the **gas generator** (also called the **core**). In a jet engine the hot gas leaves through a
nozzle and the reaction pushes the aircraft. In a power plant the hot gas is instead expanded
through an additional turbine that turns a shaft; that shaft turns an **electrical generator**. The
engine, the output turbine, a **gearbox** (if the turbine shaft speed differs from the speed the
generator needs), the generator, and the surrounding fuel, air-intake, exhaust, lubrication,
fire-protection and control systems together form a **generator set** (**genset**).

Three families of prime mover compete for on-site power at data centers:

- **Frame (heavy-duty) gas turbines**: purpose-built stationary machines, typically 50–600 MW per
  unit, heavy, installed on foundations. The large F-, H- and J-class frames from GE Vernova,
  Siemens Energy and Mitsubishi Power are the machines whose multi-year order books are described
  in section 5. (Classification and size ranges: general industry knowledge, not separately
  sourced in this session.)
- **Aeroderivative gas turbines**: aircraft engines adapted for stationary use, typically 5–100 MW,
  light, modular, fast to start and fast to install, and more efficient than frames in that size
  class in simple cycle. The patent literature describes the concept as "two basic components: an
  aircraft-derivative gas generator and a free-power turbine" and notes that the aero gas generator
  "is more efficient and this benefit leads to increasing the gas turbine cycle efficiency ...
  aero derivative gas turbine is more efficient in mid-range power than heavy-duty gas turbine"
  (USPTO patents 11053891 and 5160080, via search [33][34]).
- **Reciprocating (piston) engines**: large natural-gas piston engines of roughly 1–23 MW each,
  arranged in halls of many units. Wärtsilä describes its data-center plants as built from 10–23 MW
  engines reaching over 450 MW per site, with electrical efficiency that "can exceed 50%" and
  "20–35% less fuel than gas turbines" (vendor claim; Wärtsilä product page [67]).

A fourth option, the **solid-oxide fuel cell** (Bloom Energy, NYSE: BE), converts natural gas to
electricity electrochemically without combustion; Bloom's FY2024 10-K positions it against
reciprocating engines on power density and emissions [69]. No MW or price figures for Bloom were
captured within the search budget (Unknown U9).

### 2.2 How a turbofan becomes an aeroderivative, at functional level

The CFM56 is a **high-bypass turbofan**: a large front **fan** moves most of the air around the core
(the "bypass" flow) to produce thrust; a smaller fraction goes through the core. The engine has two
concentric shafts (**spools**): the **low-pressure spool** (fan plus a low-pressure "booster"
compressor at the front, driven by the low-pressure turbine at the back) and the **high-pressure
spool** (the high-pressure compressor, driven by the high-pressure turbine, with the combustor
between them). FTAI's aerospace business already handles the engine as three **modules** along these
lines (fan, core, low-pressure turbine); D1 and D5 cover that.

To make an aeroderivative, the published conversion recipe (described generically in USPTO
11053891, "Method for converting a turbofan engine" [33]) is:

1. **Remove the fan and the bypass duct.** Thrust is no longer wanted; the fan absorbs most of the
   low-pressure turbine's work and would be dead weight. "In case of fan jet designs, the fan is
   removed and a couple of stages of compression are added in front of the existing low-pressure
   compressor, these additional stages usually known as stage 00 and stage 0" [33]. In other words,
   the fan is replaced by a small extra compressor so the core still receives air at the pressure it
   was designed for. (This is how GE's LM2500 and LM6000 were made from the TF39/CF6-6 and CF6-80C2;
   the LM6000's low-pressure spool itself drives the generator. Lineage: general industry knowledge.)
2. **Replace the exhaust nozzle with a power turbine.** "The conventional approach ... is to replace
   the exhaust nozzle with an aerodynamically coupled power turbine, which generates shaft power
   which in turn can be used to drive an electrical power generator" [33]. A **free power turbine**
   is a turbine on its own shaft, not mechanically connected to the gas generator; it is driven only
   by the gas stream ("aerodynamically coupled"), so the gas generator can run at whatever speed
   suits it while the output shaft holds the fixed speed a generator needs. An alternative is to use
   the engine's own low-pressure turbine as the output turbine (the LM6000 approach). Which
   arrangement Mod-1 uses is not disclosed (Unknown U3).
3. **Add a gearbox where needed.** A 60 Hz grid needs a two-pole generator to turn at 3,600 rpm (or a
   four-pole at 1,800 rpm). Aeroderivative output shafts commonly spin faster. "A gearbox is
   preferably used to reduce the output speed of the turbine engine to a predetermined value ... an
   external gearbox is typically required to obtain the proper input speed to a generator" (USPTO
   6895325 [35]).
4. **Add the generator**: "the output shaft of the gearbox is connected to the input shaft of an
   electric power generator, and rotation of the generator's input shaft and windings produces
   electric power" [35].
5. **Add the stationary systems**: a natural-gas fuel system (the aircraft engine burns kerosene;
   the combustor's fuel nozzles and the fuel-control software are changed for gas), an air-inlet
   filter house (aircraft engines ingest clean air at altitude; ground air is dirtier), an exhaust
   stack and silencing, any **emissions after-treatment** (section 2.6), a lubrication and cooling
   package, fire suppression, and a control system that governs start-up, load-following and
   protection. This "balance of plant" and the enclosure that holds it all is what the industry calls
   **packaging**, and it is the part Jereh brings to J&F (section 2.7). (System list: general
   industry knowledge; FTAI has not published a Mod-1 bill of materials — Unknown U3/U5.)

**Prior CFM56 industrial derivative.** Searched for and not found in this session. GE's commercial
aeroderivative line descends from other GE cores: the LM2500 from the TF39/CF6-6, the LM6000 from the
CF6-80C2 (the same core ProEnergy uses for its PE6000 [64][65]), the LM9000 from the GE90. The search
returned no production stationary derivative of the CFM56 (Unknown U13). Trade press frames FTAI's
Mod-1 as the CFM56's first such role ("CFM56 finds a new role as an AI data-center power source",
AvioRadar [22]; "FTAI unveils CFM56 Power platform", AviTrader, 2 Jan 2026 [21]).

### 2.3 Mod-1 as FTAI describes it

From the launch release (GlobeNewswire, 30 Dec 2025 [1]):

- A platform "focused on converting CFM56 engines to power turbines built to provide the most
  flexible, cost efficient and scaled solution for delivering reliable energy to data centers
  globally."
- "The aeroderivative adapted from the CFM56 engine will provide the market with a 25-megawatt unit
  that offers grid operators greater flexibility and finer output control than larger units."
- FTAI positions itself "as one of the largest aftermarket maintenance providers and owners of the
  CFM56 engine," with "production expected to begin in 2026."
- "FTAI Power is expected to have the capacity to deliver over 100 units annually and provide
  service support solutions that maximize uptime by applying its modular maintenance model to power
  turbines."

From the Q4 2025 earnings call (26 Feb 2026), as summarised by a third party (X post by TheValueist
[19]) and Aviation Week's MRO Memo [20] — primary transcript not reached:

- 25 MW, trailer-mounted; about **two weeks to deploy on site**; usable for **baseload, backup or
  peaking**.
- **35–40% efficiency**, **heat rate about 9,000** (Btu/kWh implied), "comparable to other
  aeroderivatives sold over the past 30 to 40 years."
- A **10–20 year second life** for the engine in power service.
- The stated cost advantage is "an unmatched turbine input cost, given access to near-fully
  depreciated CFM56 assets" — FTAI already owns and trades CFM56 engines, so its input is an engine
  carried at a low book value rather than a new-build core.
- Which CFM56 variant (-5B or -7B) is used is not disclosed [20]; FTAI's aerospace business
  concentrates on both (10-K FY2025 [6]).

From filings and later releases: "Development of FTAI Power continues on-track with first
Aeroderivative product, FTAI Mod-1, expected to be delivered by Q4 2026 with planned production of
100 units in 2027" (Q4/FY2025 earnings release, 8-K ex. 99.1 [7]; repeated in Q1 2026 release [8]).
The 10-K FY2025 records the 30 Dec 2025 launch in its business description [6].

**Worked example — what a 9,000 heat rate means.** The **heat rate** is the fuel energy needed per
unit of electricity, in Btu per kWh. One kWh is 3,412 Btu, so efficiency = 3,412 / heat rate.
At 9,000 Btu/kWh: 3,412 / 9,000 = 37.9%, inside the stated 35–40% band (whether the figure is on a
lower- or higher-heating-value basis is not stated; LHV is the usual turbine convention and gives
a figure a few points higher than HHV — Unknown U5). Fuel burn for one Mod-1 at full load:
25 MW × 9,000 Btu/kWh = 225 MMBtu per hour. Over a year at a 90% capacity factor: 25 MW × 8,760 h
× 0.90 = 197,100 MWh; × 9 MMBtu/MWh = 1.77 million MMBtu, which at roughly 1,000 Btu per cubic
foot of pipeline gas is about 1.77 Bcf a year, or 4.9 MMcf a day. At an illustrative $3.50/MMBtu
gas price (assumption, not a sourced forecast), fuel cost is 9 × $3.50 = $31.50 per MWh. A
50%-efficient reciprocating engine (Wärtsilä's claim [67]) has a heat rate of 3,412 / 0.50 = 6,824
Btu/kWh and a fuel cost of 6.8 × $3.50 = $23.90 per MWh at the same gas price. The gap, about
$7.60/MWh, is the fuel penalty the turbine's buyer accepts in exchange for a smaller footprint,
fewer units per MW, and faster delivery — a trade the Enverus and EIA figures in section 4 suggest
buyers are currently making.

### 2.4 "Mobile" and what it buys

A **mobile generator set** is one built onto a road trailer or skid so it can be driven to a site,
connected to gas and to the customer's switchgear, and commissioned in days or weeks, and later
moved. The J&F order describes "Mod-1 mobile gas turbine generator sets" [2]; FTAI cites about two
weeks to deploy [19]. Mobility matters in two ways: (a) **speed** — the unit arrives finished and
tested, so site work is a pad, gas line and electrical tie-in rather than a construction project;
(b) **regulatory treatment** — US air rules distinguish stationary sources (which need a
construction/operating air permit before running) from "nonroad engines", which are mobile or
temporary (generally at one location under 12 months). Whether trailer-mounted turbines at a data
center are "nonroad" is contested: in Memphis, Shelby County accepted that xAI's temporary turbines
were "nonroad engines" exempt from permitting, an interpretation the Southern Environmental Law
Center and the NAACP contest as allowing an operator to "install and operate any number of new
polluting turbines at any time without any written approval ... without pollution controls"
(DCD [72][73]; Tennessee Lookout [74]; E&E News [71]). See section 2.8.

### 2.5 Second life and modular service

FTAI's aerospace model (D5) is to hold inventories of serviceable **modules** and swap them into a
customer's engine so the engine returns to service quickly instead of waiting for its own parts to
be repaired. The launch release says FTAI will "provide service support solutions that maximize
uptime by applying its modular maintenance model to power turbines" [1]. Functionally: when a Mod-1
gas generator reaches its inspection or overhaul point, FTAI would exchange the core (or a module of
it) rather than overhaul it in place, which is how aeroderivative operators already achieve high
availability — an aircraft-derived core is light enough to be swapped in a day, whereas a frame
turbine is overhauled on its foundation over weeks. Maintenance intervals, service pricing and the
contractual form (long-term service agreement or time-and-materials) are not disclosed (Unknown U12).

### 2.6 Emissions treatment

Gas turbines burning natural gas emit nitrogen oxides (NOx), carbon monoxide and CO2. Permits set
NOx limits; meeting them uses low-NOx combustors, water or steam injection, or **selective catalytic
reduction (SCR)**, a catalyst box in the exhaust that converts NOx to nitrogen using ammonia or urea.
Shelby County's July 2025 permit allowed xAI "to operate 15 Solar SMT-130 generators with certain
emissions controls" (TechCrunch, 3 Jul 2025 [70]). FTAI has not published Mod-1's NOx level or
after-treatment (Unknown U5). The Jereh JV's packaging scope presumably includes whatever
after-treatment the customer's permits require; not confirmed.

### 2.7 The J&F structure: what "packaging and distribution" means

FTAI describes J&F Power Systems LLC as "FTAI's joint venture with Jereh Group for packaging and
distribution of its Mod-1 aeroderivative gas turbine" [2], and Jereh as "a global leader in gas
turbine mobile packaging" (Q1 2026 release [8]). The division of labour implied by those words:

- **FTAI** supplies the converted turbine — the CFM56 gas generator plus power-turbine arrangement
  — drawing on its engine inventory, its module factories and its parts supply (including the
  multi-year CFM materials agreement signed 22 Jan 2026 [14] and the AAR serviceable-material
  agreement extended to 2030 [81]).
- **Jereh** packages the turbine: builds the trailer or skid, enclosure, generator, gearbox, inlet,
  exhaust, fuel skid and controls around it, tests the complete genset, and distributes and
  commissions it. Jereh's packaging experience comes from oilfield power: its R&D on gas-turbine
  gensets began in 2018 and "in 2020, the first 6MW gas turbine genset in China was successfully
  applied in the well site" (Jereh company history [28]); it ships trailer-mounted electric
  hydraulic-fracturing fleets, whose power comes from gas turbines on trailers, to US oilfield
  customers (PRNewswire, 2024 and 2025 [31][32]). Jereh's subsidiary GenSystems Power Solutions
  separately won a $182M (Feb 2026) and a $341M order for gas-turbine generators for US data
  centers, deliverable by end-2027 (Yicai Global [26]) — whether those use Mod-1 or other turbines is
  not stated (Unknown U8).
- **J&F** is the contracting party to the customer: the master agreement and purchase order are
  J&F's [2].

Ownership split, board control, and which party consolidates J&F are not disclosed in anything
reached. FTAI calls J&F "FTAI's joint venture"; Jereh's Shenzhen exchange disclosure, as reported by
FilingReader, calls J&F "its subsidiary" (FilingReader, 22 Jul 2026 [27]). The two descriptions are
compatible only if Jereh holds a controlling stake or if "subsidiary" is used loosely (Tension T3;
Unknown U2). This matters for revenue recognition: if Jereh consolidates J&F, FTAI's Power revenue
would be its sales of turbines into J&F plus its share of J&F's profit, not the $1.465B face value.

### 2.8 Permitting and interconnection, functionally

A behind-the-meter generator needs: (1) a **gas supply** — a pipeline lateral and metering sized for
the plant (one Mod-1 burns about 4.9 MMcf/d at 90% load, section 2.3; S&P Global reports pipeline
operators striking deals as "data centers turn to colocated generation", 27 May 2026 [43]);
(2) an **air permit** from the state or county agency implementing the Clean Air Act, unless an
exemption applies (section 2.4) — the xAI case shows a timeline of roughly a year from first
operation (mid-2024) to permit application (winter 2024) to permit (July 2025) [70][74], during
which the operator ran up to 35 units against a permit eventually written for 15 [73]; (3) if the
site also connects to the grid, an **interconnection agreement** with the utility or grid operator —
the long queues for which are the reason behind-the-meter generation exists. ProEnergy's customers
describe their turbine plants as "bridging power for five to seven years, which is when they expect
to have grid interconnection" [64]. Enverus attributes the behind-the-meter share to "grid
interconnection congestion and long development timelines" [42]. Specific queue durations from PJM
or ERCOT were not captured (Unknown U14).

### 2.9 Worked example — implied unit price and $/kW

The order value is $1.465 billion; the unit count is not disclosed, only that the order "will
account for a substantial number of FTAI Power's targeted 2027 Mod-1 ... deliveries" and that the
2027 target is 100 units [2][7].

| Assumed units in order | Implied price per unit | Per kW at 25 MW |
|---|---|---|
| 100 (the whole 2027 target) | $14.65M | $586/kW |
| 80 | $18.3M | $733/kW |
| 60 | $24.4M | $977/kW |

Arithmetic: $1,465M / 100 = $14.65M; $14.65M / 25,000 kW = $586/kW. These are not disclosed
figures; the real price also depends on what the order includes (commissioning, spares,
after-treatment, service) — Unknown U1.

Benchmarks for comparison (different scopes, see Tension T5):

- Gas Turbine World: equipment-only simple-cycle gas turbine prices range from about $1,150/kW at
  1 MW to $171/kW at ~600 MW, and "a 100 MW simple cycle aeroderivative genset is priced at $1,175
  $/kW installed" (GTW cost articles [57][58]; edition dates not captured — pre-2024 pricing).
- 2026 regulatory filings: "gas capacity that regulators approved at $1,100–1,400 per kW two years
  ago is now being filed at $2,000–2,500" (Power Engineering, 2026 [56]) — plant-level,
  predominantly large frame/combined-cycle.
- Wood Mackenzie: gas-turbine prices "projected to reach $600/kW by the end of 2027, nearly tripling
  from 2019 levels" (via Oilprice [47]) — turbine equipment only.
- Power Engineering headline: "Gas turbine prices climb 195% as supply crunch reshapes power
  development" (2026 [56]).

Against these, an implied $586–977/kW for a delivered mobile genset sits below current plant-level
filings and above or near the turbine-only WoodMac figure; the comparison is loose because the
scopes differ.

**Implied EBITDA per unit.** Management's 2027 Power EBITDA figure is $450M (Quartr/MarketBeat
summaries of the Q2 2026 call [16][17]) or "$450 million to $750 million" (GuruFocus summary
[15]) on 100 units: $4.5M–$7.5M per unit. If FTAI's recognised revenue per unit were the full
$14.65M (i.e., if 100 units and full consolidation), the margin would be 31–51%; if FTAI's
revenue is only its turbine sale into J&F, the margin on that smaller base is higher and the
figure cannot be derived. Both inputs are undisclosed (Unknown U1, U2).

### 2.10 Worked example — CFM56 cores consumed

FTAI has not said how many CFM56 engines go into one Mod-1 (Unknown U3). The simplest reading is one
gas generator per 25 MW unit: other single-core aeroderivatives in this class use one core (the
LM2500 is one TF39/CF6-6 core for 25–35 MW; the LM2500XPRESS is rated 35 MW [60]). On that
assumption:

- 100 units in 2027 = **100 CFM56 engines a year**; "over 100 units annually" at capacity [1].
- Against the active fleet: one market-research source puts the active CFM56 fleet at about 14,200
  engines (≈6,200 -5B and ≈7,500 -7B) with retirements "near 2% per year" (SafeFly CFM56 market
  report 2026 [75]; see Tension T7 — D9 should supply the authoritative count). 2% of 14,200 ≈ 284
  retirements a year; 100 engines would be about **35% of annual retirements** on that base, and
  about 0.7% of the active fleet.
- Against FTAI's own inventory: FTAI owned 243 engines in its leasing fleet at 31 Dec 2025 (chain
  map, from 10-K FY2025) and plans 1,200 module refurbishments in 2026 at a capacity of 3,000 a
  year (chain map). Since FTAI counts three modules per engine, 100 engines are roughly 300
  module-equivalents a year of feedstock that would otherwise flow to the aerospace business or to
  teardown (D3). FTAI's Q2 2026 call linked the 3,000-module capacity to "100 Mod-1 units annually"
  [15].
- Against total production: CFM has delivered well over 30,000 CFM56s since 1982 (general industry
  knowledge; not separately sourced here), so the stock of parked and retired engines is large
  relative to 100 a year; what limits feedstock is the condition and price of retired cores, which
  D3 covers.
- Capacity output: 100 units × 25 MW = **2.5 GW a year**. For scale: GE Vernova's gas backlog and
  reservations were 116 GW at Q2 2026 [46]; EIA/S&P-attributed forecasts put US behind-the-meter
  generation at industrial sites at 22.5 GW over 2026–2030, or 4.5 GW a year, 88% of it for data
  centers (search-returned summary; attribution to be verified between EIA Today in Energy #67344
  [40] and S&P Global [43]).

---

## 3. Market structure and players

**FTAI Power (FTAI Aviation Ltd., NASDAQ: FTAI).** Converter of CFM56 engines to Mod-1 turbines;
supplier to J&F. Target 100 units in 2027; first unit Q4 2026 [7]. 2027 Power EBITDA guided $450M
within $2.3B total segment EBITDA (Aerospace Products $1.4B, Aviation Leasing $450M, Power $450M)
per Q2 2026 call summaries [16][17]; a GuruFocus summary gives $450–750M [15].

**J&F Power Systems LLC.** JV of FTAI and Jereh for packaging and distribution; counterparty to the
master agreement and $1.465B order [2]. Ownership not disclosed (U2).

**Jereh Group — Yantai Jereh Oilfield Services Group Co., Ltd. (SZSE: 002353).** Chinese oilfield
equipment maker: drilling and oil-and-gas field engineering equipment, equipment maintenance and
parts, oilfield engineering services, natural-gas compressors and gas-turbine gensets (PitchBook
profile [30]; Jereh history [28]). Gas-turbine genset R&D from 2018; first 6 MW unit at a well site
in 2020 [28]. Subsidiary GenSystems Power Solutions: $182M (Feb 2026) and $341M US data-center
gas-turbine generator orders, delivery by end-2027 [26]. Jereh's shares rose on both the GenSystems
and J&F announcements [26][27].

**The customer.** "A leading international cloud service provider" in the FTAI release [2]; "a U.S.
hyperscaler" in Q2 2026 call summaries [15][16] (Tension T1). Not named.

**Frame-turbine OEMs (the capacity-constrained incumbents):**
- GE Vernova (NYSE: GEV): gas power equipment backlog plus slot reservation agreements 83 GW at
  end-2025, 100 GW at Q1 2026, 116 GW at Q2 2026; expects at least 125 GW under contract by Dec
  2026; taking reservations for 2031 delivery, more than half of 2031 expected contracted by
  end-2026 (Power Engineering, Jul 2026 [46]; Industrial Info [50]). Earlier reports: 50 GW
  (Yahoo Finance, 2025 [51]); "booking turbine orders for 2028 and 2029, with 2026 and 2027 largely
  sold out" (Oilprice [47]). Raised multi-year outlook 9 Dec 2025 [49].
- Siemens Energy (XETRA: ENR): gas-turbine backlog 69 GW at fiscal Q3 ended 30 Jun 2026, after
  booking 15 GW and shipping 6 GW in the quarter; lead times "three years or more" [47][52].
- Mitsubishi Power (Mitsubishi Heavy Industries, TSE: 7011): 35 GW large-frame backlog; orders
  booked in the quarter for delivery 2028–2030; "selective in the projects we contract" [47].
- Industry-level: combined-cycle lead time rose to five years in 2025 from 3.5 in 2023 [47]; global
  gas-turbine orders 110 GW at end-2025 against manufacturing capacity of 60–70 GW (Wood Mackenzie
  via Oilprice [47][55]).

**Aeroderivative and small-turbine suppliers (Mod-1's direct comparables):**
- GE Vernova LM2500XPRESS: 35 MW per unit (GE Vernova release, 22 Jul 2025 [60]); Crusoe ordered 10
  units in Dec 2024 and 19 in Jun 2025, "nearly 1 GW" combined, for AI data centers; packages
  delivered (Turbomachinery International [61]). 29 units at ~1 GW implies ~34.5 MW each (Tension
  T6).
- GE Vernova LM6000: CF6-80C2-derived, ~48–50 MW class; "the waiting list is anywhere from three to
  five years" (EEPower / Data Centre Magazine [64][65]).
- ProEnergy (private) PE6000: 48 MW, built on CF6-80C2 cores from retired Boeing 747 engines — "the
  same engine core GE Vernova uses in its LM6000"; deliverable 2027; sold 21 turbines for two
  data-center projects totalling more than 1 GW, as 5–7-year bridging power until grid
  interconnection [64][65]. ProEnergy is the closest analogue to FTAI Power: a non-OEM reusing retired
  airline cores.
- Baker Hughes (NASDAQ: BKR) NovaLT: industrial (not aero-derived) small turbines; data-center order
  target doubled to $3B over 2025–2027; NovaLT capacity to double by 1H 2027 (Bloomberg Government
  [63]); order from Dynamis Power Solutions for 76 NovaLT16 units ≈1.3 GW (≈17 MW each) for data
  center and oil-and-gas power (World Oil, 29 Jul 2026 [62]).
- Solar Turbines (Caterpillar, NYSE: CAT): mobile Titan-class units appear in the xAI Memphis permit
  as 15 "Solar SMT-130 generators" totalling up to 247 MW (≈16.5 MW each) [70]. Titan 350 figures
  not captured (U9).
- Siemens Energy SGT-A65 (Rolls-Royce Trent-derived aeroderivative): not captured (U9).

**Reciprocating engines:**
- Wärtsilä (Nasdaq Helsinki: WRT1V): 10–23 MW engines, plants over 450 MW; claims 20–30% lower capex
  than turbines once reserve capacity is included, 20–35% less fuel, efficiency over 50% (vendor
  page [67]); 507 MW US data-center order, 20 Nov 2025 [68].
- Caterpillar (NYSE: CAT) gas gensets: figures not captured (U9).

**Fuel cells:** Bloom Energy (NYSE: BE): positioned against reciprocating engines for on-site power
including "the peak loads associated with AI data centers" (10-K FY2024 [69]); deal sizes and $/kW
not captured (U9).

**Deployers and intermediaries:** Crusoe (private; GE Vernova customer) [60]; Dynamis Power Solutions
(Baker Hughes customer) [62]; GenSystems Power Solutions (Jereh subsidiary) [26]; xAI (operator of
mobile turbines at Memphis) [70].

**Demand-side context providers:** IEA (Energy and AI report, April 2025) [36][37]; EIA (Short-Term
Energy Outlook and Today in Energy, 2026) [38][39][40]; Enverus ("Off the grid, on the gas") [42].

---

## 4. Numbers

### 4.1 FTAI Power and the J&F order

| Item | Figure | Source, date |
|---|---|---|
| Launch date | 30 Dec 2025 | FTAI PR [1]; 10-K FY2025 [6] |
| Unit output | 25 MW | FTAI PR [1] |
| Stated annual capacity | "over 100 units annually" | FTAI PR [1] |
| First delivery | by Q4 2026 | Q4/FY2025 earnings release [7]; Q1 2026 release [8] |
| 2027 production target | 100 units | [7][8]; Q2 2026 call summaries [15][16] |
| Efficiency | 35–40% | Q4 2025 call via TheValueist summary [19]; Aviation Week [20] |
| Heat rate | ~9,000 (Btu/kWh implied) | same [19][20] |
| Deployment time | ~2 weeks on site | same [19] |
| Second life | 10–20 years | same [19] |
| Form factor | trailer-mounted, mobile | [19]; J&F PR [2] |
| Applications | baseload, backup, peaking | [19] |
| Order value | $1.465B initial purchase order | J&F PR, 22 Jul 2026 [2] |
| Agreement term | five-year master supply agreement; customer may issue further POs | [2] |
| Delivery | in batches through Nov 2027 | [2] |
| Payment | milestone basis: advance at signing; progress payments through production, testing, on-site commissioning | [2] |
| Performance adjustment | "subject to a performance adjustment mechanism capped at 10%" | PR text as reposted by Barchart/Pulse2 [4][5]; primary [2] |
| Order's share of 2027 | "a substantial number" of targeted 2027 deliveries | [2] |
| Units in order | not disclosed | — |
| 2027 Power EBITDA | $450M (point) | Quartr, MarketBeat summaries of Q2 2026 call [16][17] |
| 2027 Power EBITDA | $450–750M (range) | GuruFocus summary of Q2 2026 call [15] |
| 2027 total segment EBITDA | $2.3B: Aerospace $1.4B, Leasing $450M, Power $450M | [16][17] |
| Module capacity linked to Power | 3,000 modules/yr "supporting ... 100 Mod-1 units annually" | GuruFocus [15] |
| Customer description | "leading international cloud service provider" / "U.S. hyperscaler" | [2] / [15][16] |
| Implied price per unit | $14.65M at 100 units ($586/kW); $18.3M at 80; $24.4M at 60 | derived, section 2.9 |
| Implied EBITDA per unit | $4.5M–$7.5M at 100 units | derived from [15][16] |

### 4.2 Jereh

| Item | Figure | Source, date |
|---|---|---|
| Listing | SZSE 002353, Yantai Jereh Oilfield Services Group | PitchBook [30]; szse.io |
| Genset history | R&D from 2018; first 6 MW gas-turbine genset in China at well site, 2020 | Jereh history [28] |
| GenSystems orders | $182M (Feb 2026) and $341M, US data centers, delivery by end-2027 | Yicai Global [26] |
| J&F description | "its subsidiary, J&F Power Systems" signed $1.465B contract | FilingReader on SZSE disclosure, 22 Jul 2026 [27] |
| US oilfield deliveries | 7,000 HP electric frac fleet to US customer (2024); TITAN frac units to BJ Energy Solutions (2025) | PRNewswire [31][32] |

### 4.3 Demand

| Item | Figure | Source, date |
|---|---|---|
| Global data-centre electricity 2030 | more than doubles to ~945 TWh ("slightly more than Japan") | IEA Energy and AI, Apr 2025 [36][37] |
| AI-optimised data-centre demand | more than quadruples by 2030 | IEA [36] |
| US share | data centres ≈ half of US electricity demand growth to 2030 | IEA [36] |
| US load growth | +1.9% in 2026, +2.5% in 2027; largest four-year growth since 2000 | EIA STEO via DCD [38] |
| Regional load growth 2025–27 | ERCOT ~10%/yr, PJM ~3.2%/yr | EIA via DCD [38] |
| ERCOT price effect | data-center demand could drive a 79% ERCOT wholesale price rise in 2027 | EIA via Utility Dive [39] |
| Behind-the-meter share | ~40% of installed data-center capacity; ~1.3 Bcf/d incremental gas by 2030; half in ERCOT and PJM | Enverus [42] |
| Fuel of on-site generation | >80% of announced on-site generation is natural gas | Enverus/EIA-attributed summary [40][42] |
| BTM at industrial sites 2026–30 | 22.5 GW, 88% for data centers, ~4.5 GW/yr | EIA Today in Energy #67344 or S&P Global; attribution unverified [40][43] |

### 4.4 Turbine supply

| Item | Figure | Source, date |
|---|---|---|
| GE Vernova gas backlog + reservations | 83 GW end-2025; 100 GW Q1 2026; 116 GW Q2 2026; ≥125 GW expected Dec 2026 | Power Engineering, Jul 2026 [46]; Industrial Info [50] |
| GE Vernova slots | selling 2031; >50% of 2031 contracted by end-2026 expected | [46] |
| GE Vernova (earlier) | 50 GW backlog | Yahoo Finance, 2025 [51] |
| GE Vernova (earlier) | 2026–27 largely sold out; booking 2028–29 | Oilprice [47] |
| Siemens Energy | 69 GW backlog at 30 Jun 2026; +15 GW booked, 6 GW shipped in quarter; lead times 3+ years | [47][52] |
| MHI | 35 GW large-frame backlog; deliveries 2028–30 | [47] |
| Combined-cycle lead time | 5 years (2025) vs 3.5 years (2023) | [47] |
| Global orders vs capacity | 110 GW orders end-2025 vs 60–70 GW/yr manufacturing capacity | Wood Mackenzie via Oilprice [47][55] |
| Turbine price trajectory | $600/kW by end-2027, ~3x 2019 | Wood Mackenzie via Oilprice [47] |
| Price inflation headline | +195% | Power Engineering, 2026 [56] |
| Plant-level approvals | $1,100–1,400/kW two years ago → $2,000–2,500/kW now | Power Engineering [56] |
| Simple-cycle equipment-only | $1,150/kW at 1 MW to $171/kW at ~600 MW | Gas Turbine World [57][58], undated |
| 100 MW aero genset installed | $1,175/kW | Gas Turbine World [57][58], undated |

### 4.5 Comparable units and orders

| Unit | Output | Lead time / delivery | Notable order | Source |
|---|---|---|---|---|
| FTAI Mod-1 (CFM56) | 25 MW | first Q4 2026; 100 in 2027 | $1.465B, batches to Nov 2027 | [1][2][7] |
| GE Vernova LM2500XPRESS | 35 MW (GE); ~34.5 MW implied | delivered 2025–26 | Crusoe 29 units ≈1 GW | [60][61] |
| GE Vernova LM6000 (CF6-80C2) | ~48–50 MW class | 3–5 year wait | — | [64][65] |
| ProEnergy PE6000 (CF6-80C2) | 48 MW | 2027 | 21 units >1 GW, two projects | [64][65] |
| Baker Hughes NovaLT16 | ~17 MW (1.3 GW / 76) | capacity doubling by 1H 2027 | Dynamis 76 units ≈1.3 GW | [62][63] |
| Solar SMT-130 (mobile) | ~16.5 MW (247 MW / 15) | in service 2024–25 | xAI Memphis, 15 permitted (35 operated) | [70][73] |
| Wärtsilä engines | 10–23 MW each | — | 507 MW US order, Nov 2025 | [67][68] |
| Bloom Energy fuel cells | not captured | not captured | not captured | [69] |

### 4.6 CFM56 fleet inputs for the feedstock example

| Item | Figure | Source |
|---|---|---|
| Active CFM56 fleet | ~14,200 (≈6,200 -5B; ≈7,500 -7B) | SafeFly market report 2026 [75] — market-research site; see T7 |
| Shop visits | 2,300–2,400/yr through 2028 | [75] |
| Retirement rate | ~2%/yr | [75] |
| Removals | +10% in 1H 2027 vs 2026 expected | GE Aerospace via Aviation Week [76] |
| FTAI engines owned | 243 at 31 Dec 2025 | 10-K FY2025 via chain map |
| FTAI module plan | 1,200 in 2026; 3,000/yr capacity | chain map; [15] |

---

## 5. Constraints and bottlenecks

**Supply of frame turbines (the demand driver for Mod-1).** The three large OEMs are sold out for
several years: GE Vernova is selling 2031 slots and expects 125 GW contracted by end-2026 [46];
Siemens Energy quotes three-plus years [47]; MHI delivers 2028–30 [47]; global orders of 110 GW
against 60–70 GW of capacity [47]. A buyer that needs power in 2026–27 cannot get a new frame
turbine, which is the opening for aeroderivatives, reciprocating engines and fuel cells.

**Supply of aeroderivatives.** The OEM aeroderivative (LM6000) is itself quoted at 3–5 years
[64][65]. Non-OEM converters (ProEnergy on CF6 cores, FTAI on CFM56 cores) are limited by the
supply of suitable retired cores and by packaging capacity; ProEnergy quotes 2027 delivery [64],
FTAI Q4 2026 for the first unit and 100 units in 2027 [7]. Baker Hughes is doubling NovaLT
capacity by 1H 2027 [63].

**CFM56 core feedstock.** 100 engines a year is a small fraction of the active fleet but, on the
one market-research base found, about a third of annual retirements (section 2.10). FTAI's own
engine inventory and module factories compete for the same cores. The price of retired cores,
covered in D3, sets Mod-1's input cost; FTAI describes that input as "near-fully depreciated" [19].

**Packaging capacity and location.** Jereh's role is the packaging; where J&F builds — in China, the
US, or elsewhere — is not disclosed (U4). A Chinese build location would expose the gensets to US
tariff and trade-policy risk; a US location would require Jereh to stand up or expand a facility.
Neither is documented in the sources reached.

**Gas supply.** Each Mod-1 at 90% load needs about 4.9 MMcf/d (section 2.3); 100 units need about
0.49 Bcf/d, which is a large fraction of Enverus's 1.3 Bcf/d incremental behind-the-meter gas demand
by 2030 [42] — a reminder that pipeline laterals, not just turbines, gate deployments [43].

**Permitting.** Air permits take months to a year or more and are contested where operators run
units before permits (Memphis) [70]–[74]. The "nonroad engine" question — whether a mobile turbine
may run without a stationary-source permit — is unresolved in litigation and could either widen or
close the fast-deployment route Mod-1 is designed for.

**Interconnection.** Multi-year grid queues are why behind-the-meter exists; ProEnergy's customers
plan 5–7 years of bridging [64]. If queues shorten, the bridging market shrinks; if they lengthen,
turbines bought as bridges become long-term plant.

**Capital and working capital.** The J&F order pays in milestones from an advance at signing [2],
which FTAI's Q2 2026 call described as "derisking working capital" [16]. FTAI's capital
requirement for Power (packaging facilities, engine inventory dedicated to Power, test cells) is not
disclosed (U6).

**Performance risk.** The purchase price is "subject to a performance adjustment mechanism capped at
10%" [4][5]: if delivered units fall short on whatever metrics the contract specifies (output, heat
rate, availability, delivery timing — not disclosed, U11), up to 10% of value is at stake; the cap
also bounds the downside.

**Fuel efficiency.** At 35–40%, Mod-1 burns 25–35% more fuel per MWh than a 50%-efficient
reciprocating plant (section 2.3) — a cost the buyer bears over the unit's life and a lever for
competitors with better heat rates.

---

## 6. Tensions

- **T1. Who the customer is.** FTAI's release: "a leading international cloud service provider"
  [2]. Q2 2026 call summaries: "a U.S. hyperscaler" [15][16]. Not necessarily inconsistent (a US
  firm operating internationally), but the primary document does not say "US".
- **T2. 2027 Power EBITDA.** $450M as the guided point within $2.3B total (Quartr, MarketBeat
  [16][17]) versus "$450 million to $750 million" (GuruFocus [15]). Likely a base figure and an
  upside case stated on the same call; the primary transcript was not reached.
- **T3. Whose company J&F is.** "FTAI's joint venture with Jereh Group" (FTAI [2]) versus "its
  subsidiary, J&F Power Systems" (Jereh's SZSE disclosure via FilingReader [27]). Determines who
  consolidates the $1.465B.
- **T4. GE Vernova backlog.** 50 GW (Yahoo, 2025 [51]), 83 GW (end-2025), 100 GW (Q1 2026),
  116 GW (Q2 2026) [46][50]; "2026 and 2027 largely sold out, booking 2028–29" (Oilprice [47])
  versus "orders placed today won't arrive until 2031" (Power Engineering citing 22 Jul 2026 call
  [46]). The figures are a time series and the later ones include slot reservations as well as
  firm backlog; readers quoting one number should give its date and definition.
- **T5. What a turbine costs per kW.** $171–1,150/kW equipment-only and $1,175/kW installed for a
  100 MW aero genset (Gas Turbine World, undated [57][58]); $600/kW turbine-only by end-2027 (Wood
  Mackenzie [47]); $2,000–2,500/kW in current plant-level regulatory filings (Power Engineering
  [56]); $586–977/kW implied for Mod-1 under unit-count assumptions (section 2.9). Scopes differ
  (turbine vs genset vs plant; equipment vs installed), as do dates.
- **T6. LM2500XPRESS rating.** 35 MW in GE Vernova's release [60] versus ~34.5 MW implied by "29
  units ... nearly 1 GW" [60][61] and the 34 MW figure in the commissioning brief. Ratings vary with
  site conditions; "nearly" 1 GW is a rounded figure.
- **T7. CFM56 active fleet.** ~14,200 active engines (SafeFly market report [75]) is lower than
  figures commonly cited elsewhere (not sourced in this session). D9 should supply the authoritative
  count; the feedstock example in 2.10 scales linearly with it.
- **T8. Efficiency vs heat rate.** 35–40% and ~9,000 Btu/kWh are consistent (9,000 → 37.9%) only if
  on the same heating-value basis; the basis is not stated [19][20].
- **T9. Regulatory status of mobile turbines.** Shelby County: temporary turbines are "nonroad
  engines" exempt from permitting; SELC/NAACP: they are stationary sources needing permits and
  controls [72][73][74]. Unresolved.
- **T10. Reciprocating vs turbine fuel use.** Wärtsilä claims 20–35% less fuel than gas turbines and
  >50% efficiency (vendor claim [67]); FTAI's 35–40% figure [19] is consistent with the lower end of
  that gap but both are self-reported.

---

## 7. Unknowns

- **U1. Units and price in the $1.465B order.** Not disclosed. Would be resolved by FTAI's Q3 2026
  10-Q or call, or by Jereh's SZSE filing if it states quantities.
- **U2. J&F ownership, control and consolidation.** Percentages, board, which party consolidates,
  and how FTAI recognises Power revenue (sale of turbines into J&F, share of J&F profit, or
  consolidated genset sales). The Q2 2026 10-Q [10] is the document to read; its J&F note was not
  returned by search.
- **U3. Engines per unit and configuration.** How many CFM56 gas generators per 25 MW unit; -5B or
  -7B; whether the engine's own low-pressure turbine or a new free power turbine drives the
  generator; whether a booster stage replaces the fan.
- **U4. Where units are built.** Jereh packaging site(s); US vs China; tariff exposure; whether
  J&F has its own facility.
- **U5. Emissions and fuel.** NOx level, after-treatment (SCR or not), heating-value basis of the
  efficiency figure, dual-fuel capability.
- **U6. Capital required.** Power capex, engine inventory earmarked, test capacity; FTAI's engine
  input cost per unit.
- **U7. Segment reporting.** The 10-K FY2025 has two reportable segments [6]; call summaries speak
  of a "Power segment" for 2027. Whether Power is a third reportable segment from the Q2 2026 10-Q
  [10], or sits within Aerospace Products until first delivery, was not confirmed.
- **U8. Jereh's GenSystems orders.** MW count (to derive $/kW) and whether they use Mod-1 or other
  turbines; identity of the customer; relationship to J&F.
- **U9. Competitor figures not captured.** Siemens Energy SGT-A65 output/lead time; Solar Turbines
  Titan 350; Caterpillar gas gensets; Bloom Energy deal sizes and $/kW; published aeroderivative
  list prices in 2026.
- **U10. Milestone schedule.** Size of the advance payment and the percentage at each milestone.
- **U11. Performance adjustment.** Which metrics the 10% cap applies to (output, heat rate,
  availability, schedule) and whether it is symmetric (bonus as well as penalty).
- **U12. Service model.** Mod-1 inspection and overhaul intervals; service contract form and
  pricing; FTAI's expected service revenue per unit.
- **U13. Prior CFM56 stationary derivative.** None found; a definitive statement from GE/CFM or
  Gas Turbine World's handbook would settle whether Mod-1 is the first.
- **U14. Interconnection queue durations.** PJM and ERCOT queue statistics were not captured; they
  quantify the "bridging" window ProEnergy's customers describe as 5–7 years [64].
- **U15. Transcripts.** The Q4 2025 (26 Feb 2026) and Q2 2026 (29 Jul 2026) call transcripts were
  reached only through third-party summaries [15]–[19]; direct quotations on Power should be taken
  from the transcripts before publication.

---

## 8. Terms introduced

- **Gas turbine**: rotating engine that compresses air, burns fuel, expands hot gas through turbines.
- **Gas generator / core**: the compressor-combustor-turbine assembly producing hot pressurised gas.
- **Generator set (genset)**: prime mover plus generator plus supporting systems, as one unit.
- **Frame (heavy-duty) turbine**: purpose-built stationary gas turbine, typically 50–600 MW.
- **Aeroderivative**: an aircraft engine adapted to drive a shaft for stationary power.
- **Reciprocating engine**: piston engine; large natural-gas versions of 1–23 MW used in plants.
- **Solid-oxide fuel cell**: device converting fuel to electricity electrochemically, no combustion.
- **High-bypass turbofan**: jet engine in which a large fan moves most air around the core.
- **Spool**: a compressor-turbine pair on one shaft; the CFM56 has a low- and a high-pressure spool.
- **Booster / stage 00 and 0**: extra compressor stages added where the fan was, to feed the core.
- **Free power turbine**: output turbine on its own shaft, driven only by the gas stream.
- **Gearbox**: speed reducer between turbine shaft and generator.
- **Packaging / balance of plant**: enclosure, trailer, inlet, exhaust, fuel, controls around a turbine.
- **Mobile genset**: trailer- or skid-mounted unit movable between sites.
- **Nonroad engine**: US air-rule category for mobile/temporary engines exempt from stationary permits.
- **Heat rate**: fuel energy per kWh produced, Btu/kWh; efficiency = 3,412 / heat rate.
- **LHV / HHV**: lower/higher heating value, two bases for fuel energy content.
- **Capacity factor**: actual output over a period divided by output at full load for that period.
- **Behind-the-meter (BTM)**: generation on the customer's side of the utility meter.
- **Bridging power**: temporary on-site generation used until a grid interconnection is available.
- **Interconnection agreement / queue**: contract and waiting list to connect a plant to the grid.
- **Air permit**: Clean Air Act authorisation to construct and operate an emissions source.
- **NOx / SCR**: nitrogen oxides; selective catalytic reduction, exhaust catalyst reducing NOx.
- **Slot reservation agreement**: paid reservation of a future manufacturing slot, counted with backlog.
- **Master supply agreement / purchase order**: framework contract; binding order placed under it.
- **Milestone payments**: payments tied to events (signing, production, testing, commissioning).
- **Commissioning**: on-site testing and hand-over of installed equipment.
- **Performance adjustment mechanism**: contractual price change tied to measured performance, here capped at 10%.
- **Module (FTAI usage)**: one of three major CFM56 sections (fan, core, LPT) exchanged as a unit.
- **Hyperscaler**: very large cloud operator building its own data centers.

---

## 9. Sources

1. FTAI Aviation, "FTAI Aviation Announces the Launch of FTAI Power", GlobeNewswire, 30 Dec 2025. https://www.globenewswire.com/news-release/2025/12/30/3211297/35538/en/FTAI-Aviation-Announces-the-Launch-of-FTAI-Power-FTAI-Adapts-the-World-s-Largest-Aircraft-Engine-Platform-to-Meet-AI-Driven-Power-Demand.html
2. FTAI Aviation, "FTAI Announces $1.465 Billion Gas Turbine Generator Set Order Through J&F Power Systems", GlobeNewswire, 22 Jul 2026. https://www.globenewswire.com/news-release/2026/07/22/3331360/35538/en/ftai-announces-1-465-billion-gas-turbine-generator-set-order-through-j-f-power-systems.html
3. FTAI IR node for the same release (blocked in this environment). https://ftandi.gcs-web.com/node/13041
4. Barchart repost of the 22 Jul 2026 release. https://www.barchart.com/story/news/3402927/ftai-announces-1-465-billion-gas-turbine-generator-set-order-through-jf-power-systems
5. Pulse2, "FTAI Secures $1.465 Billion Gas Turbine Generator Order Through J&F Power Systems", Jul 2026. https://pulse2.com/ftai-secures-1-465-billion-gas-turbine-generator-order-through-jf-power-systems/
6. FTAI Aviation Ltd., Form 10-K FY2025 (filed early 2026). https://www.sec.gov/Archives/edgar/data/1590364/000162828026012940/ftai-20251231.htm
7. FTAI Aviation, Q4/FY2025 earnings release (8-K ex. 99.1), Feb 2026. https://www.sec.gov/Archives/edgar/data/1590364/000162828026011685/ftai123125earningsrelease.htm
8. FTAI Aviation, Q1 2026 earnings release (8-K ex. 99.1), filed 30 Apr 2026. https://www.sec.gov/Archives/edgar/data/1590364/000162828026028390/ftai3312026earningsrelease.htm
9. FTAI Aviation Ltd., Form 10-Q Q1 2026. https://www.sec.gov/Archives/edgar/data/1590364/000162828026029335/ftai-20260331.htm
10. FTAI Aviation Ltd., Form 10-Q Q2 2026 (quarter ended 30 Jun 2026). https://www.sec.gov/Archives/edgar/data/0001590364/000162828026051412/ftai-20260630.htm
11. FTAI Aviation Ltd., Form 8-K, 29 Jul 2026. https://www.sec.gov/Archives/edgar/data/1590364/000162828026050622/ftai-20260729.htm
12. FTAI Aviation, Q2 2026 results release, GlobeNewswire, 29 Jul 2026. https://www.globenewswire.com/news-release/2026/07/29/3335598/35538/en/FTAI-Aviation-Ltd-Reports-Second-Quarter-2026-Results-Increases-Dividend-to-0-50-per-Ordinary-Share.html
13. FTAI Aviation, Q1 2026 results release, GlobeNewswire, 29 Apr 2026. https://www.globenewswire.com/news-release/2026/04/29/3284285/35538/en/FTAI-Aviation-Ltd-Reports-First-Quarter-2026-Results-Increases-Dividend-to-0-45-per-Ordinary-Share.html
14. FTAI Aviation, "Multi-Year Materials Agreement with CFM International", GlobeNewswire, 22 Jan 2026. https://www.globenewswire.com/news-release/2026/01/22/3223741/35538/en/FTAI-Aviation-Announces-Multi-Year-Materials-Agreement-with-CFM-International-to-Further-Support-CFM56-Engines.html
15. GuruFocus, "FTAI Aviation Ltd (FTAI) Q2 2026 Earnings Call Highlights", 30 Jul 2026. https://www.gurufocus.com/news/8991870/ftai-aviation-ltd-ftai-q2-2026-earnings-call-highlights-record-module-production-and-power-business-breakthrough-drive-growth-amid-strategic-shifts
16. Quartr, "FTAI Aviation (FTAI) Q2 2026 earnings summary", Jul 2026. https://quartr.com/events/ftai-aviation-ltd-ftai-q2-2026_ozdaN73d
17. MarketBeat, "FTAI Aviation Q2 Earnings Call Highlights", 30 Jul 2026. https://www.marketbeat.com/instant-alerts/ftai-aviation-q2-earnings-call-highlights-2026-07-30/
18. Nasdaq, "FTAI Aviation Q2 Earnings Call Highlights", Jul 2026. https://www.nasdaq.com/articles/ftai-aviation-q2-earnings-call-highlights
19. TheValueist (X), summary of FTAI Q4 2025 call, 26 Feb 2026 (secondary). https://x.com/TheValueist/status/2027078155635503303
20. Aviation Week, "MRO Memo: FTAI Pitches CFM56 To Power AI Boom", early 2026. https://aviationweek.com/mro/emerging-technologies/mro-memo-ftai-pitches-cfm56-power-ai-boom
21. AviTrader, "FTAI unveils CFM56 Power platform", 2 Jan 2026. https://avitrader.com/2026/01/02/ftai-unveils-cfm56-power-platform/
22. AvioRadar, "CFM56 finds a new role as an AI data-center power source", 2026. https://avioradar.net/en/cfm56-finds-a-new-role-as-an-ai-data-center-power-source/
23. Distribution Strategy, "FTAI Aviation Moves into Data Center Power", 2026. https://distributionstrategy.com/ftai-aviation-moves-into-data-center-power-leveraging-engine-distribution-and-mro-platform/
24. ConstructConnect, "From Plane Power to Power Grid", 2026. https://news.constructconnect.com/from-plane-power-to-power-grid-repurposing-jet-engines-for-data-centers
25. ePlaneAI, "CFM56 Engine Repurposed to Power AI Data Centers", 2026. https://www.eplaneai.com/news/cfm56-engine-repurposed-to-power-ai-data-centers
26. Yicai Global, "China's Jereh Rises After Landing USD341 Million Gas Turbine Generator Order for US Data Centers", 2026. https://www.yicaiglobal.com/news/chinas-jereh-rises-after-landing-usd341-million-gas-turbine-generator-order-for-us-data-center
27. FilingReader, "Yantai Jereh subsidiary secures $1.47bn turbine contract" (SZSE disclosure), 22 Jul 2026. https://filingreader.com/news-wire/shenzhen/2026-07-22/yantai-jereh-subsidiary-secures-147bn-turbine-contract
28. Jereh Group, company history page. https://jereh.com/en/about/history
29. Jereh Group, news item. https://jereh.com/en/news/news-detail.jsp?id=614905
30. PitchBook, Yantai Jereh Oilfield Services Group profile. https://pitchbook.com/profiles/company/164739-43
31. PRNewswire, "Jereh Ships 7000 HP Electric Fracturing Fleet to Renowned US Oilfield Service Company", 2024. https://www.prnewswire.com/news-releases/jereh-ships-7000-hp-electric-fracturing-fleet-to-renowned-us-oilfield-service-company-302100418.html
32. PRNewswire, "BJ Energy Solutions takes delivery of fifth set of TITAN Hydraulic Fracturing Units from Jereh", 2025. https://www.prnewswire.com/news-releases/bj-energy-solutions-llc-takes-delivery-of-fifth-set-of-titan-hydraulic-fracturing-units-from-jereh-energy-equipment-and-technologies-corporation-302400515.html
33. USPTO, US 11,053,891 "Method for converting a turbofan engine". https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11053891
34. USPTO, US 5,160,080 "Gas turbine engine and method of operation for providing increased output shaft horsepower". https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5160080
35. USPTO, US 6,895,325 "Overspeed control system for gas turbine electric powerplant". https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6895325
36. IEA, "AI is set to drive surging electricity demand from data centres", news release, Apr 2025. https://www.iea.org/news/ai-is-set-to-drive-surging-electricity-demand-from-data-centres-while-offering-the-potential-to-transform-how-the-energy-sector-works
37. IEA, "Energy and AI", executive summary, Apr 2025. https://www.iea.org/reports/energy-and-ai/executive-summary
38. Data Center Dynamics, "EIA: US electricity use to see largest four-year growth period since 2000", 2026. https://www.datacenterdynamics.com/en/news/eia-us-electricity-use-to-see-largest-four-year-growth-period-since-2000-driven-primarily-by-data-center-demand/
39. Utility Dive, "Data center demand spike could drive 79% ERCOT price hike in 2027: EIA", 2026. https://www.utilitydive.com/news/data-center-demand-spike-could-drive-79-ercot-price-hike-in-2027-eia/814804/
40. EIA, Today in Energy #67344, 2026. https://www.eia.gov/todayinenergy/detail.php?id=67344
41. GridBeyond, "Data center power demand driving fossil generation, says EIA", 2026. https://gridbeyond.com/data-center-power-demand-driving-fossil-generation-says-eia/
42. Enverus, "Off the grid, on the gas", 2026. https://www.enverus.com/newsroom/off-the-grid-on-the-gas/
43. S&P Global Commodity Insights, "Pipeline operators strike deals as data centers turn to colocated generation", 27 May 2026. https://www.spglobal.com/energy/en/news-research/latest-news/natural-gas/052726-pipeline-operators-strike-deals-as-data-centers-turn-to-colocated-generation
44. Datacentres.com, "Behind-the-meter power: gas turbines and fuel cells emerge as data centres escape slot...", 19 Aug 2026. https://www.datacentres.com/news/behind-the-meter-power-gas-turbines-and-fuel-cells-emerge-as-data-centres-escape-slot1-2026-08-19
45. Latitude Media, "Is the gas turbine bottleneck solving itself?", 2026. https://www.latitudemedia.com/news/is-the-gas-turbine-bottleneck-solving-itself/
46. Power Engineering, "Data centers drive record surge in GE Vernova power equipment orders as turbine slots tighten through 2030", Jul 2026. https://www.power-eng.com/gas/turbines/data-centers-drive-record-surge-in-ge-vernova-power-equipment-orders-as-turbine-slots-tighten-through-2030/
47. Oilprice, "The Gas Turbine Shortage Just Became AI's Biggest Constraint", 2026. https://oilprice.com/Energy/Energy-General/The-Gas-Turbine-Shortage-Just-Became-AIs-Biggest-Constraint.amp.html
48. Utility Dive, GE Vernova investor update coverage. https://www.utilitydive.com/news/ge-vernova-gas-turbine-investor/807662/
49. GE Vernova, "GE Vernova raises multi-year financial outlook...", BusinessWire, 9 Dec 2025. https://www.businesswire.com/news/home/20251209799497/en/GE-Vernova-raises-multi-year-financial-outlook-doubles-dividend-and-increases-buyback-authorization
50. Industrial Info Resources, "GE Vernova's Global Natural Gas Turbine Reservations and Order Backlog Grows to 100 GW", 2026. https://www.industrialinfo.com/iirenergy/industry-news/article/ge-vernovas-global-natural-gas-turbine-reservations-and-order-backlog-grows-to-100-gw--356705
51. Yahoo Finance, "GE Vernova Backlog Hits 50 GW", 2025. https://finance.yahoo.com/news/ge-vernova-backlog-hits-50-082001096.html
52. Energy News Beat, "Siemens gas turbine backlog nears 70 GW as company expands manufacturing", 2026. https://energynewsbeat.co/electrical-generation/siemens-gas-turbine-backlog-nears-70-gw-as-company-expands-manufacturing/
53. Power Engineering, "Long lead times are dooming some proposed gas plant projects". https://www.power-eng.com/gas/turbines/long-lead-times-are-dooming-some-proposed-gas-plant-projects/
54. oEnergetice, "Gas turbine manufacturers expand capacity, but lead times continue to lengthen". https://oenergetice.cz/en/electricity/gas-turbine-manufacturers-expand-capacity-but-lead-times-continue-to-lengthen
55. Oilprice, "Global Gas Turbine Orders Hit Record High as Power Demand Surges". https://oilprice.com/Latest-Energy-News/World-News/Global-Gas-Turbine-Orders-Hit-Record-High-as-Power-Demand-Surges.amp.html
56. Power Engineering, "Gas turbine prices climb 195% as supply crunch reshapes power development", 2026. https://www.power-eng.com/gas/turbines/gas-turbine-prices-climb-195-as-supply-crunch-reshapes-power-development/
57. Gas Turbine World, "How much does it cost to build a Simple Cycle or Combined Cycle plant?" (undated). https://gasturbineworld.com/?p=6191
58. Gas Turbine World, "Capital Costs for Utility Scale Gas Turbine Plants" (undated). https://gasturbineworld.com/?p=2855
59. Northwest Power and Conservation Council, biennial gas turbine cost assessment (PDF). https://www.nwcouncil.org/sites/default/files/BiennialGasturbine.pdf
60. GE Vernova, "GE Vernova, Crusoe announce major 29-unit aeroderivative gas turbine deal to deliver AI data centers", 22 Jul 2025. https://www.gevernova.com/news/press-releases/ge-vernova-crusoe-announce-major-29-unit-aeroderivative-gas-turbine-deliver-ai-data-centers
61. Turbomachinery International, "GE Vernova delivers 29 LM2500XPRESS aeroderivative gas turbine packages to Crusoe AI data centers". https://www.turbomachinerymag.com/view/ge-vernova-delivers-29-lm2500xpress-aeroderivative-gas-turbine-packages-to-crusoe-ai-data-centers
62. World Oil, "Baker Hughes wins major gas turbine order for data center, oil and gas power", 29 Jul 2026. https://worldoil.com/news/2026/7/29/baker-hughes-wins-major-gas-turbine-order-for-data-center-oil-and-gas-power/
63. Bloomberg Government, "Baker Hughes Doubles Data Center Order Target to $3 Billion". https://news.bgov.com/texas-brief/baker-hughes-doubles-data-center-order-target-to-3-billion
64. Data Centre Magazine, "Can Old Aeroplane Engines Powering Data Centres Take Off?" https://datacentremagazine.com/news/can-old-aeroplane-engines-power-data-centres-take-off
65. EEPower, "Can repurposed jet engines solve AI data center power problems?" https://eepower.com/news/can-repurposed-jet-engines-solve-ai-data-center-power-problems/
66. IEEE Spectrum, AI data centers coverage. https://spectrum.ieee.org/ai-data-centers
67. Wärtsilä, data centre power solutions product page. https://www.wartsila.com/energy/solutions/flexible-baseload-power-plants/data-centre-power-solutions
68. Wärtsilä, "Wärtsilä continues growth in the data center segment with a 507 MW order in the US", 20 Nov 2025. https://www.wartsila.com/dnk/media/news/20-11-2025-wartsila-continues-growth-in-the-data-center-segment-with-a-507-mw-order-in-the-us-offering-engines-as-a-reliable-power-solution-3686573
69. Bloom Energy Corp., Form 10-K FY2024. https://www.sec.gov/Archives/edgar/data/1664703/000162828025008747/be-20241231.htm
70. TechCrunch, "xAI gets permits for 15 natural gas generators at Memphis data center", 3 Jul 2025. https://techcrunch.com/2025/07/03/xai-gets-permits-for-15-natural-gas-generators-at-memphis-data-center
71. E&E News, "Musk's xAI gets air permit for Memphis supercomputer", Jul 2025. https://www.eenews.net/articles/musks-xai-gets-air-permit-for-memphis-supercomputer/
72. Data Center Dynamics, "xAI facing lawsuit over use of gas turbines at Memphis supercomputer", 2025. https://datacenterdynamics.com/en/news/xai-facing-lawsuit-over-use-of-gas-turbines-at-memphis-supercomputer
73. Data Center Dynamics, "xAI doubles number of onsite gas turbines at Memphis data center in violation of permit limits", 2025. https://datacenterdynamics.com/en/news/xai-doubles-number-of-onsite-gas-turbines-at-memphis-data-center-in-violation-of-permit-limits
74. Tennessee Lookout, xAI permitting coverage, 2025. https://tennesseelookout.com/?p=27979
75. SafeFly Aviation, "CFM56 Engine Market Report 2026" (market-research site). https://safefly.aero/cfm56-engine-market-report-2026/
76. Aviation Week, "CFM56 Overhaul Demand Remains Strong, GE Aerospace Says". https://aviationweek.com/mro/aircraft-propulsion/cfm56-overhaul-demand-remains-strong-ge-aerospace-says
77. Air Cargo Week, "From PW1100G to CFM56: The engine maintenance trends shaping 2026". https://aircargoweek.com/from-pw1100g-to-cfm56-the-engine-maintenance-trends-shaping-2026/
78. Barchart, "Why FTAI Aviation (FTAI) stock is trading up today", Jul 2026. https://www.barchart.com/story/news/3406515/why-ftai-aviation-ftai-stock-is-trading-up-today
79. Stocktwits, "FTAI Stock Hits Record High After Launching New Power Division For Data Centers", Dec 2025. https://stocktwits.com/news-articles/markets/equity/ftai-stock-hits-record-high-after-launching-new-power-division-for-data-centers/cL7IIs0REyO
80. Stock Taper, FTAI Q1 2026 earnings call summary. https://www.stocktaper.com/earningsCallSummary/FTAI/2026/Q1
81. PRNewswire, "AAR and FTAI Aviation extend their exclusive Serviceable Engine Products agreement ... through 2030", 2025. https://www.prnewswire.com/news-releases/aar-and-ftai-aviation-extend-their-exclusive-serviceable-engine-products-agreement-providing-cfm56-engine-material-to-the-global-aviation-aftermarket-through-2030-302412621.html
