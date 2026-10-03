# D1 — The CFM56 engine as a machine (functional mechanics)

Dossier for the FTAI Aviation deep primer. Written 2026-10-03. 18 WebSearch calls used (budget 18); WebFetch
unavailable, so every figure below comes from the text a search returned and is cited to the page the
search named. Where a figure the brief asked for was not reached, it is listed under Unknowns, not estimated.
Posture: explain, do not opine. Depth: the level that determines product and market outcomes.

---

## 1. Summary

The CFM56 is a two-shaft, high-bypass turbofan built by CFM International, the GE Aerospace / Safran Aircraft
Engines joint venture. More than 35,000 have been delivered since entry into service in 1982 and about 23,000
remain in service (CFM, undated page, accessed 2026-10-03) [1]. Two variants matter for FTAI: the CFM56-7B,
sole engine of the Boeing 737NG (>15,000 delivered; last engine for a commercial 737NG delivered 2019) [1][20],
and the CFM56-5B, which powers nearly 60% of A320ceo-family aircraft ordered (installed-engine production ended
2022; >4,100 -5B-powered aircraft delivered) [1][22]. The engine is built as separable modules (fan/booster,
core = HPC + combustor + HPT, LPT, accessory gearbox) that can be exchanged between engines if their records
travel with them [8][9]. Inside the rotating modules sit life-limited parts (LLPs): disks, spools and shafts
certified for a fixed number of flight cycles, 20,000 (HPC, HPT), 25,000 (LPT) and 30,000 (fan/booster) on the
-7B [3][4]; reaching a limit forces the engine open regardless of condition. A full -7B LLP set listed at $1.775M
in 2008, $3.4M in 2018, ~$4M in 2019 and $5.7M in mid-2025 (sources differ in scope, see Tensions) [11][12][13][16],
i.e. roughly 7% a year compounded. A performance-restoration shop visit without LLPs is quoted at $1.2–1.6M by
one 2026 source and $1.8–2.5M by another; a heavy visit with LLPs at $2.1–2.8M or ">$3.5M" [17]. Turnaround is
90–120 days for a full overhaul in 2025 against ~60 days pre-pandemic [23][24]. Mature engines reach a
performance visit at 10,000–15,000 cycles and an LLP-driven overhaul at 20,000–25,000 [7]. Engine value is
appraised as a half-life base value adjusted for actual LLP life and time since restoration [28][29][30].

---

## 2. Mechanics

### 2.1 What the machine is

A **turbofan** is a jet engine in which a large front fan pushes most of the air around the hot core (the
**bypass** stream) rather than through it; the core burns fuel to drive turbines that turn the fan. The CFM56 is a
**two-shaft** (two-spool) design: a **low-pressure (LP) spool** on which the fan and a small **booster**
compressor are driven by the **low-pressure turbine (LPT)**, and a concentric **high-pressure (HP) spool** on
which the **high-pressure compressor (HPC)** is driven by the **high-pressure turbine (HPT)**. The two shafts
spin at different speeds and are connected only by the air passing through.

On the CFM56-7B specifically: a 61-inch fan with 22 solid titanium wide-chord blades, a three-stage booster
(also called the low-pressure compressor), a nine-stage HPC, a single-stage HPT and a four-stage LPT (Aircraft
Commerce, CFM56-7B Owner's & Operator's Guide, Issue 58, 2008) [8]. Between HPC and HPT sits the
**combustor**, where fuel is burned. The **accessory gearbox (AGB)** is a box of gears driven off the HP spool
by a radial shaft; it turns the fuel pump, oil pumps, hydraulic pump and the aircraft's electrical generator.

**Thrust** is quoted in pounds-force (lbf). The same hardware is sold at several **thrust ratings**: the engine's
electronic control limits how hard it is allowed to run. A higher rating is the same metal working hotter, which
(section 2.4) means less temperature margin and shorter life between overhauls.

### 2.2 The family

| Variant | Airframe | Thrust class (lbf) | Production status | Delivered | Source |
|---|---|---|---|---|---|
| CFM56-3 | Boeing 737 Classic (-300/-400/-500); smaller fan for ground clearance | 18,500–23,500 | Last engine shipped 1999 | 3,974 engines on 1,987 aircraft | [1][21] |
| CFM56-5A | Airbus A320 (early) | 22,000–34,000 quoted jointly for -5A/-5B/-5C | ended (year not retrieved) | not retrieved | [1] |
| CFM56-5B | A318/A319/A320/A321 (A320ceo family); "nearly 60%" of A320ceo ordered | within 22,000–34,000 | Installed-engine production ended 2022 | >4,100 -5B-powered aircraft | [1][22] |
| CFM56-5C | A340-200/-300 (sole engine) | within 22,000–34,000 (upper end) | A340 out of production; end year not retrieved | not retrieved | [1][25] |
| CFM56-7B | Boeing 737NG (-600/-700/-800/-900ER), sole engine | 19,500–27,300 per [19]; "19,500–33,000" per [1] summary (see Tension T1) | Last engine for a commercially operated 737NG delivered by May 2019; 15,000th built 2019 | >15,000 engines; >7,000 aircraft | [1][19][20] |

CFM International is described by CFM as a joint venture between GE Aerospace and Safran Aircraft Engines
(formerly Snecma) [1]. The 50/50 split is how the company has always described itself; the search text did not
restate the percentage, so it is carried here as the widely published figure rather than a freshly verified one.

**Successor.** The LEAP (LEAP-1A on the A320neo, LEAP-1B on the 737 MAX) replaced the CFM56 on the re-engined
narrowbodies. By December 2017 CFM had orders and commitments for more than 14,270 LEAPs and had delivered 459 in
2017 (Safran press release, Feb 2018) [26]. Current LEAP delivery totals were not retrieved (D9 covers fleet
context). The CFM56 fleet of ~23,000 in-service engines [1] is the installed base that all CFM56 aftermarket
activity, FTAI's included, works on; no new CFM56 engines for commercial narrowbodies have been built since 2019
(-7B) and 2022 (-5B) [20][22], so every CFM56 that flies tomorrow is one that exists today.

### 2.3 Modules

A **module** is a section of the engine that was designed to be removed and replaced as a unit, bolted to its
neighbours at flanges, with its own part number, serial number and maintenance record. The purpose is to let a
shop fix the part of the engine that needs fixing without taking the whole engine down to piece parts.

The module list reached in this session:

- CFM56-5B, as described in CFM-derived training material: four modules, (1) fan and low-pressure compressor
  (booster), (2) high-pressure compressor, combustion chamber and high-pressure turbine, (3) low-pressure
  turbine and turbine rear frame, (4) accessory gearbox [9]. Item (2) is what the industry calls the **core**
  (or "gas generator"): the hot, fast, expensive middle of the engine.
- CFM56-7B: the same architecture (fan/booster, nine-stage HPC, combustor, one-stage HPT, four-stage LPT, AGB)
  [8]. Aircraft Commerce describes the **fan frame sub-module** as the structural front of the engine with four
  major assemblies: containment case, outlet guide vane assembly, fan frame assembly and radial drive shaft
  housing; it ducts both airflows, transmits thrust to the aircraft, carries the LP rotor bearings and supports
  accessories [8]. The word "sub-module" signals that CFM's manuals divide the engine into **major modules**
  (fan, core, LPT, and the accessory drive) which are themselves built from numbered sub-modules.

Unknown U1: the full CFM56-7B/-5B sub-module list (the manuals' numbered breakdown, commonly cited as 17
sub-modules) was not reached in this session's searches. The writer should not quote a count.

**What makes modules interchangeable.** Three things have to be true for a shop to take the fan module off
engine A and bolt it onto engine B:

1. **Mechanical and configuration compatibility.** The modules must be the same model and build standard (the
   OEM issues service bulletins that change hardware; two modules at different standards may not mate or may
   not be approved together). CFM's TRUEngine programme exists precisely to certify that an engine's
   configuration and material content conform to CFM's own definition, because "the engine's configuration,
   material content, maintenance history, and supportability impact overall value as it changes ownership"
   (CFM press release launching TRUEngine) [10].
2. **Serialization and records.** Each module and each LLP inside it carries a serial number and a record of
   cycles consumed. A module can only move if the receiving engine's records can absorb it, with every LLP's
   remaining life known and documented (section 2.9).
3. **Common part numbers.** The -5B and -7B share core hardware to the point that used-parts dealers advertise
   a single "CFM56-5B & -7B Core LLP Package" [15]. That commonality is what lets a shop building -7B cores
   draw on -5B feedstock and vice versa. The exact list of parts common to both variants was not retrieved
   (Unknown U2).

**Module exchange versus full disassembly.** A **module exchange** separates the engine at the major-module
flanges, removes one module and installs a serviceable one. StandardAero lists "engine module changes" among
its **quick-turn shop visit (QTSV)** services alongside borescope inspection, boroblend repair (grinding out
small blade damage), QEC/LRU removal and installation, and fan, top case, bottom case, hot section and LPT
repairs (StandardAero CFM56-7B brochure, 2022) [27]. A **full disassembly** (overhaul) strips each module to
piece parts, inspects and repairs or replaces each one, and rebuilds. The economic difference is time and
exposure: a module exchange is days to a few weeks and touches only the exchanged module; a full disassembly is
months and opens every module to inspection findings that then must be repaired. (Whether a test-cell run is
required after a given module change depends on the shop manual procedure for that module; not verified here.)

FTAI's business is built on this distinction. Its FY2025 10-K describes a "Module Factory", "a dedicated
commercial maintenance program designed to focus on modular and parts repair and refurbishment of CFM56-7B and
CFM56-5B engines", and says the company "targets assets which require maintenance repairs that can be performed
through [its] proprietary Module Factory process" [31]. D5 takes this further.

### 2.4 Life-limited parts

A **life-limited part (LLP)** is a rotating or pressure-bearing part whose failure the engine case cannot be
designed to contain. Its life is certified in **engine flight cycles (EFC)**: one cycle is one take-off and
landing, because the stress peak that counts is the spin-up and heat-up at take-off, not the hours in cruise.
At the certified limit the part must be removed and scrapped, whatever its condition. The parts are the disks
(the heavy wheels the blades attach to), spools (several disks machined as one piece), shafts, and certain
seals and pressure-balance components.

CFM's stated design policy is "target lives of 30,000 EFC in the fan/booster module, 20,000 EFC in the HPC and
HPT modules and 25,000 EFC in the LPT module" (Aircraft Commerce, Issue 34, 2004) [3]. Engine-specific
documents confirm the limits in service on the -7B. From a CFM56-7B26 records summary ("mini-pack") published by
AJW Group and a similar StandardAero pack [4][5]:

| CFM56-7B LLP | Module | Certified limit (EFC) |
|---|---|---|
| Fan disk | Fan/booster | 30,000 |
| Booster spool | Fan/booster | 30,000 |
| HPC stage 1–2 spool | Core (HPC) | 20,000 |
| HPC stage 3 disk | Core (HPC) | 20,000 |
| HPC stage 4–9 spool | Core (HPC) | 20,000 |
| HPT disk | Core (HPT) | 20,000 |
| LPT stage 1 disk | LPT | 25,000 |

The packs list further parts (shafts, remaining LPT disks, seals) whose individual limits were not in the
returned text. For the -5B, Leeham (Bjorn Fehrm, 2024) states that "a typical engine like the CFM56-5B has 18
different sets of LLPs with life limits varying between 20,000 and 30,000 flight cycles" [7]. A per-part -5B
table was not reached (Unknown U3).

**Why a limit forces the engine open.** The LLPs are the innermost parts: the HPT disk sits behind the
combustor with the HPT blades mounted on it; the HPC spools are buried in the core. To change the HPT disk the
core must be removed from the engine, the HPT module split from the HPC and combustor, the blades pulled, and
the disk replaced; the rotor is then rebalanced and rebuilt. There is no on-wing procedure. So when the lowest
remaining life among all installed LLPs reaches zero, the engine comes off the wing and goes into a shop
whether or not it is still performing. In practice the operator removes it earlier, at a planned shop visit,
and replaces LLPs that would otherwise run out before the next planned visit.

**Worked example A — the LLP clock.** A CFM56-7B26 with 18,500 cycles on its HPT disk (limit 20,000) has 1,500
cycles left. A 737-800 flying 1,500 short-haul cycles a year (the utilisation Aircraft Value News uses for a
mature narrowbody is 1,000–1,500 cycles per year [30]) will reach the limit in about one year. If the engine's
EGT margin (section 2.5) would otherwise let it fly another 5,000 cycles, that margin is worthless: the disk
sets the removal date.

**The stub-life problem.** **Stub life** is "the shortest life remaining of all LLPs installed in an engine"
and, in its pejorative sense, the "several thousand EFCs of remaining LLP life that will not be used and the
parts will be scrapped" (Aircraft Commerce, Issue 34, 2004) [3]. The mechanism: "shop visit input may occur at
a time when LLPs still have a few thousand EFCs remaining, and LLP replacement at this stage will be necessary if
remaining lives are not to limit the subsequent removal interval"; "if scrapped with excessive stub life the
amortised cost per EFC and EFH is increased" [3]. LLP cycles remaining "influence mid-life lease pricing,
redelivery conditions, and asset value protection for lessors" (AviTrader, April 2026) [14].

**Worked example B — stub life and amortised cost.** An engine arrives for a performance restoration at 12,000
cycles since new. Its core LLPs (20,000 limit) have 8,000 cycles left. The planned next run is 12,000 cycles.

- Keep the LLPs: the engine comes off again at 8,000 cycles, LLP-forced, with its restored performance only
  two-thirds used.
- Replace them now with new parts at list: 8,000 of 20,000 cycles (40%) of each part's life is scrapped. If a
  part lists at P, cost per cycle rises from P/20,000 to P/12,000, a 67% increase in LLP cost per cycle.
- Third option, which is the one the used-parts market exists for: install **used LLPs** with remaining life
  matched to the planned run, say 12,000–15,000 cycles. Dealers advertise exactly such packages — a
  "CFM56-7B27E/B1F Engine LLP Package ... 7,445 Cycles Remaining" (Salvex listing) [32] and a "CFM56-5B & -7B
  Core LLP Package 6235 CR" [15] (CR = cycles remaining). Prices of these packages were not shown (Unknown U4).
  D3 covers this market.

The stub problem is also why the lives are what they are: engines "whose inherent design includes LLPs with
high stub-lives will tend to experience lower rates of engine removals compared to engines with lower LLP
stub-lives" [3]. CFM's choice of 20,000 for the core and 30,000 for the fan means the fan LLPs can span a core
overhaul cycle and a half: at the first core LLP replacement (~20,000), the fan disk still has ~10,000 cycles.
That mismatch is one of the physical reasons a fan module and a core module from the same engine have
different values at the same point in time (section 2.8).

**LLP set price and escalation.** The figures reached, for a full new CFM56-7B set at OEM catalogue (list)
price:

| Year | Full -7B LLP set, list | Source |
|---|---|---|
| 2008 | $1.775M ("shipset") | Aircraft Commerce, Issue 58, CFM56-7B maintenance analysis [11] |
| 2018 | $3.4M | Aircraft Commerce, Issue 120, Oct/Nov 2018 [12] |
| Nov 2019 | "$4m for CFM56-7" (headline; article paywalled) | Aircraft Value News [13] |
| 2023 | CFM raised the catalogue in Aug 2023; -7B prices up 20–30% vs prior year (parts generally, not LLPs specifically) | Magnetic Group via Aviation Week [33] |
| Jun 2025 | "LLPC $m: 5.700" (LLP cost line in an engine-status table) | MyAirTrade engine status page [16] |

**Worked example C — escalation.** 2008 to 2018: $3.4M / $1.775M = 1.916 over ten years, which is
1.916^(1/10) − 1 = 6.7% a year compounded. 2018 to 2025: $5.7M / $3.4M = 1.676 over seven years, 7.7% a year.
Over the whole 2008–2025 span: 3.21x in 17 years, 7.1% a year. The 2019 point ($4.0M) would imply +18% in one
year, which is out of line with the trend and may reflect a rounded headline or a different scope (Tension T2).
Ishka reports that LLP escalation for the CFM56-5B and -7B rose by approximately 12% in one recent step and that
"engine OEMs calculate LLP escalation based on a formula which factors in labour costs, the price of raw
materials and energy costs" [34]; the year of that 12% was not in the returned text. Because an LLP set is
40–60% of the parts bill in a heavy shop visit [17], a 7% annual LLP escalation on its own lifts heavy
shop-visit cost by roughly 3–4% a year before any labour or repair inflation. D2 covers OEM pricing policy.

### 2.5 Exhaust-gas temperature margin

**Exhaust-gas temperature (EGT)** is the temperature of the gas leaving the turbine, measured by probes behind
the LPT. Every engine has a certified EGT **red line**; **EGT margin (EGTM)** is "the difference between the
maximum temperature limit on the engine and the actual temperature read at the time of take-off" (Jurnal
Teknik Mesin, June 2023) [35], measured on a hot day at full take-off thrust so that it is comparable between
engines.

**Why it defines time on wing.** As an engine wears, its compressor and turbine move less air per unit of fuel,
so the control system burns more fuel to make the same thrust and the gas runs hotter. EGT margin therefore
shrinks with use. When margin reaches zero the engine can no longer make rated take-off thrust within its
temperature limit on a hot day, and it must be removed. Time on wing is thus the smaller of two clocks: the LLP
clock (section 2.4) and the EGT clock. Aircraft Commerce's maintenance analyses state that "EGT margin erosion
is generally the most influential factor in maintenance removal intervals for short-haul engines, while the
effect of hardware deterioration is greater on engines used on medium-haul operations" [36]. For the latest
-5B and -7B at most ratings, however, "the exhaust gas temperature (EGT) margin is high enough ... for it to
remain on-wing up to the life-limited part (LLP) engine flight cycle (EFC) life limits", so that "it is possible
for certain engines to only come due their third planned removal and shop visit after more than 25 years of
operation" (Aircraft Commerce, CFM56-5A/-5B maintenance analysis, Issue 50) [6]. FlightGlobal reports the same
from the shops: "shop visits for the latest CFM56-5B/7B variants tended to be driven by life-limited parts
(LLPs) reaching their ceiling rather than a need to restore engine performance", and "especially first-run
engines have flown almost to LLP limit" [18].

**How it erodes.** "Rates of deterioration [are] highest in the first 1,000 EFC of operation as blade tips and
seals are worn and clearances increase. This leads to leakage around blade tips and causes EGT margin to
erode. EGT margin deterioration rates slow down after the first 1,000–2,000 EFC on-wing" [36]. A measured
CFM56-3C1 case: 26.2°C of margin lost since the last repair, of which rotor-tip clearance accounted for 58.1%
[35]. Operating environment matters: sand and salt erode blades faster, and higher thrust ratings start with
less margin.

**What restores it.** "Shop visit maintenance will restore hardware and clearances between blade tips and
engine casings, and most of the original EGT margin will therefore be restored" [36]. In practice this means
new or repaired HPT blades and vanes, new honeycomb seals and shroud segments, and restored HPC blade tips. The
HPT is where most margin is recovered, which is why "HPT blades and vanes" are the second-largest cost line in a
shop visit (15–25% of parts cost [17]) and why a PMA HPT blade (D4) matters so much.

Unknown U5: the as-new EGT margin for each -7B and -5B thrust rating, and the typical loss per 1,000 cycles,
were not retrieved. The writer should not quote degree figures.

### 2.6 Shop-visit types and workscopes

A **shop visit** is any removal of the engine from the aircraft for work in an engine shop. The **workscope**
is the list of modules opened and the depth of work in each. The main types, from lightest to heaviest:

- **Hospital (or quick-turn) visit.** Fix one thing and return the engine: a borescope finding, a damaged fan
  blade, a module exchange, an LRU (line-replaceable unit, an accessory) change. StandardAero's QTSV menu above
  [27] is the catalogue of such work. Aviation Week reports that "hospital repairs with smaller work scopes and
  quicker turnaround times are being used as an alternative to avoid substantial financial and time investments
  into full-performance shop visits" (Magnetic Group, 2024) [33]. Light work is quoted at around 45 days
  turnaround in 2025 [23].
- **Top-case repair.** The HPC case is split horizontally; the top half comes off to give access to HPC blades
  and vanes for repair or replacement without removing the rotor. StandardAero lists "top case" and "bottom
  case" repairs separately [27].
- **Performance restoration (PR).** The core is opened and the HPC, combustor and HPT are restored to recover
  EGT margin; the fan and LPT may be inspected but not fully disassembled. A **core PR** is this scope confined
  to the core module.
- **Overhaul (heavy or full shop visit).** All modules fully disassembled, inspected, repaired and rebuilt;
  LLPs due within the next run replaced. Done when the LLPs are due. Leeham: "a mature engine like the CFM56 has
  a performance shop visit at half the LLP flight cycle limit, and then a full engine overhaul is done when the
  LLPs are due for replacement" [7].

**Time on wing by run.** The **first run** is the interval from new to first shop visit; **mature runs** are
subsequent intervals, which are shorter because repaired hardware does not match new hardware and because
operators plan them to fit the LLP clock. Figures reached:

| Metric | Value | Source, date |
|---|---|---|
| Mature CFM56, short-haul, performance restoration interval | 10,000–15,000 FC | Leeham, Mar 2024 [7] |
| Mature CFM56, full overhaul with LLP replacement | 20,000–25,000 FC | Leeham, Mar 2024 [7] |
| First-run -5B/-7B (latest variants) | "almost to LLP limit" (i.e. approaching 20,000 EFC core limit) | FlightGlobal (MRO) [18] |
| -5B: third planned removal | possible after >25 years | Aircraft Commerce Issue 50 [6] |

Unknown U6: first-run and mature-run intervals by thrust rating (e.g. -7B24 vs -7B27, -5B4 vs -5B3) and by
region were not retrieved.

**Turnaround time (TAT).** The time from induction to redelivery.

| Metric | Value | Source, date |
|---|---|---|
| CFM56 full overhaul, pre-pandemic | ~60 days | Aviation Business News / AVM, 2025 [23] |
| CFM56 full overhaul, current | 90–120 days | same [23] |
| CFM56 light work, current | ~45 days | same [23] |
| CFM56 TAT, GE Aerospace shops | "sustaining ~90 days" | GE Aerospace, Bernstein conference deck, 27 May 2026 [24] |
| PR visit | 75–90 days | Safe Fly Aviation, 2026 [17] |
| Heavy visit + LLPs | 120–150 days | Safe Fly Aviation, 2026 [17] |

The 2025 trade press attributes the extension to "long turnaround times for material repairs ... primarily due
to parts scarcity issues in the MRO supply chain" [23]. Every extra day of TAT is a day the owner needs a spare
engine or a grounded aircraft, which is the economic hook for module exchange: swapping in a serviceable core
turns a 90–120-day event into a quick-turn.

### 2.7 Shop-visit cost build

The cost of a shop visit is the sum of: (1) **labour** (hours × shop rate) to disassemble, inspect, assemble and
test; (2) **new OEM parts** that are scrapped and replaced (blades, vanes, seals, bearings); (3) **repairs**,
i.e. work on parts that can be restored instead of replaced, done in-house or sent to specialist repair vendors,
some under OEM licence and some under independent approvals (D4); (4) **LLP replacement**, new or used; (5)
**test-cell run** to confirm thrust, EGT margin and vibration; plus freight, consumables and the shop's margin.

Ranges reached (all trade-press or secondary; no OEM figure):

| Item | Figure | Source, date |
|---|---|---|
| CFM56-7B performance restoration | $1.8–2.5M | Safe Fly Aviation, 2026 [17] |
| CFM56-7B performance restoration | $1.2–1.6M | Safe Fly Aviation, "2026 industry data", same site [17] |
| CFM56-7B full heavy overhaul with complete LLP replacement | ">$3.5M" | Safe Fly Aviation, 2026 [17] |
| CFM56-7B heavy shop visit + LLPs | $2.1–2.8M | Safe Fly Aviation, "2026 industry data" [17] |
| CFM56-5 light performance restoration | ~$300k, "up to the double for a more thorough visit" | Leeham, 2017 [37] |
| Cost shares: LLPs | 40–60% of parts cost | Safe Fly Aviation, 2026 [17] |
| Cost shares: HPT blades and vanes | 15–25% | same [17] |
| Cost shares: labour | 15–20% | same [17] |
| V2500 heavy shop visit (for contrast) | $2–3M "depending on the LLP profile" | LTAI via Aircraft Commerce Issue 70, 2010 [38] |

Tension T3 (below) records that the two Safe Fly ranges disagree with each other, and that none of the "with
LLPs" totals is consistent with a full new LLP set at 2025 list price. Unknown U7: labour hours per workscope
and shop labour rates (US$/hour) were searched for and not found; the brief's request for an hours × rate build
cannot be met from this session's evidence, so the labour line below is derived from the published share.

**Worked example D — a performance restoration with LLP replacement, CFM56-7B26, second shop visit, 2025 prices.**
Inputs are the sourced figures above; where a figure is a midpoint it says so.

1. Performance-restoration workscope excluding LLPs: take the midpoint of the $1.8–2.5M range, $2.15M [17].
   - Labour at 15–20%: $320k–$430k [17]. (Hours and rate: unknown, U7.)
   - HPT blades and vanes at 15–25%: $320k–$540k [17].
   - Remainder, $1.2–1.5M: other new parts (HPC blades, seals, bearings), repairs, test and consumables.
2. LLP replacement. The engine is at 12,000 cycles; its 20,000-cycle core LLPs have 8,000 left and would force
   the next removal early (worked example B). Options:
   - (a) Full new set at list, $5.7M (June 2025) [16]. Note this replaces fan/booster parts with 18,000 cycles
     still on them, so a shop would not do this; it is the ceiling case.
   - (b) New core LLPs only (HPC spools and disk, HPT disk, shafts). The core group's share of the $5.7M set
     was not retrieved (Unknown U8), so this line cannot be priced from evidence.
   - (c) Used core LLP package with ~12,000 cycles remaining, matched to the next run. Advertised, price not
     shown (U4).
3. Totals. Case (a): $2.15M + $5.7M = $7.85M. Case (a) at the 2018 list of $3.4M: $5.55M. The quoted
   "heavy shop visit + LLPs" figures of $2.1–2.8M and ">$3.5M" [17] are therefore only reachable with partial
   LLP replacement, used LLPs, or older price levels (Tension T3).
4. Cost per cycle over the next 12,000-cycle run. PR only: $2.15M / 12,000 = $179 per cycle. Full new LLP set
   amortised over its 20,000-cycle life: $5.7M / 20,000 = $285 per cycle; if scrapped after 12,000 cycles with
   8,000 of stub life, $475 per cycle. So the LLP decision moves the engine's maintenance cost per cycle by more
   than the entire PR workscope does. This is the arithmetic that creates a market for used LLPs and for cores
   whose LLP lives are matched to the buyer's planned run.
5. Time. PR: 75–90 days [17] or 90–120 days [23]; against that, a core module exchange from inventory is a
   quick-turn [27]. The owner's alternative cost is a spare-engine lease for the TAT; D6 gives lease rates.

### 2.8 Engine value as modules and remaining life

Appraisers (IBA, mba Aviation, Ascend/Cirium, AVITAS) value engines with three linked concepts, standardised
by ISTAT (the International Society of Transport Aircraft Trading):

- **Half-life (base) value.** "Half-life is a standard appraisal industry term to indicate that no value
  adjustment has been made for the actual maintenance status ... the assumption being that the airframe,
  engines (modules & LLPs), landing gear, and other major maintenance events are in half-life status. It does
  not indicate that the aircraft is half-way through its useful life" (Jetrader, ISTAT, Jul/Aug 2010) [28].
  For an engine: every module is assumed halfway between performance restorations and every LLP at half its
  certified life.
- **Full-life value.** "Full-life engines are brand new or in recently restored condition" with all LLPs at
  zero cycles [29]; the value is half-life plus half the cost of a full restoration and a full LLP set.
- **Maintenance-adjusted value.** "The fair market value of an Aircraft or Engine based on half-life values as
  adjusted by the relevant Aircraft Appraiser for the actual maintenance conditions and specifications" [30].
  The adjustment for each item is (actual remaining fraction − 0.5) × the cost to restore that item.

Because an engine's modules are separable (section 2.3) and carry their own LLP clocks that deliberately do not
align (fan 30,000 vs core 20,000, section 2.4), the maintenance adjustment is naturally computed module by
module. Engine value = base value + Σ over modules of (module's PR and LLP adjustments). This is also why a
"**sum of modules**" or "**sum of parts**" view can exceed the whole-engine value for an engine with mismatched
modules: a fan with 18,000 cycles of LLP life attached to a core with 1,500 is worth more as a fan module sold
to someone who needs a fan plus a core sold as LLP stubs than as one engine that must go into a shop. D3 covers
part-out economics. CFM's TRUEngine designation, which "is being embraced by industry's leading asset valuation
providers, including ... IBA, AVITAS, and Ascend" [10], is the OEM's lever on this calculation: appraisers can
treat non-OEM configuration as a discount.

**Worked example E — maintenance-adjusted value of a mid-life -7B26.** Inputs: full LLP set $5.7M (2025 list)
[16]; PR cost $2.15M (midpoint) [17]; PR interval 12,000 cycles (mature, within [7]). Half-life base value is
not a figure this session reached (Unknown U9) and is written as HLBV.

- LLP status: on average across the set, 65% of certified life remaining. Adjustment = (0.65 − 0.50) × $5.7M =
  +$0.855M.
- PR status: 3,000 cycles since last PR, so 9,000 of 12,000 remaining = 75%. Adjustment = (0.75 − 0.50) × $2.15M
  = +$0.54M.
- Maintenance-adjusted value = HLBV + $0.855M + $0.54M = HLBV + $1.4M.
- The same engine at 9,000 cycles since PR (25% remaining) and 35% LLP life: (0.35 − 0.5) × $5.7M = −$0.855M;
  (0.25 − 0.5) × $2.15M = −$0.54M; value = HLBV − $1.4M.
- Full-life value = HLBV + 0.5 × ($5.7M + $2.15M) = HLBV + $3.9M.

The swing between a fresh and a run-out engine of the same age is thus ~$2.8M on these inputs, driven mostly
by the LLP line. Aircraft Value News notes that for engines whose LLP lives outlast the economic life of the
airframe, the "half" reference is itself fluid: on the CFM56-3, 20,000 cycles at 1,000–1,500 cycles a year "equates
to more than 15 years, considerably longer than the envisaged economic life", so appraisers may not treat
10,000 cycles as half-life [30]. The same source records that PMA parts "continue to undermine full-life
maintenance adjustments" (D4) [39].

### 2.9 Records and airworthiness

An engine is only worth its paperwork. The documents that matter for module exchange:

- **Back-to-birth traceability**: a continuous record, for each LLP, of every cycle it has flown on every
  engine since manufacture, with no gaps. A gap means the part's remaining life cannot be proven and it is
  treated as unusable. Industry guidance on LLP management stresses exactly this cycles-remaining record as the
  determinant of lease pricing and redelivery acceptance [14]. (A formal definition from a regulator was not
  reached in this session; the term is used here as the industry uses it.)
- **Serviceable vs unserviceable**: a part or module is serviceable when it has been inspected and released by
  an approved organisation and is eligible for installation; unserviceable when it is removed pending repair,
  or scrapped. The release is evidenced by a tag.
- **FAA Form 8130-3, "Airworthiness Approval Tag"**: "may be used to constitute a statement from the FAA that a
  new product or article produced under Title 14 CFR Part 21 conforms to its design and is in a condition for
  safe operation" and, for used parts, a maintenance release by an FAA-approved repair station [40]. "Products
  and articles not produced under an FAA production approval are not eligible to receive an FAA Form 8130-3";
  "new articles produced under a European production organization approval (POA) are typically ineligible for an
  8130-3 tag and are more properly released on an **EASA Form 1**", the European equivalent [40]. A **dual
  release** is one tag signed under both FAA and EASA authority, which lets a part move between US- and
  EU-registered aircraft without re-certification. The "most commonly required traceability documents include
  FAA Form 8130-3 (or ... EASA Form 1), Certificates of Conformance, manufacturer certifications (PMA, PC, TC),
  ATA 106 Spec Sheets, and return-to-service records from operators or repair stations" (Aviation Business
  News) [41]. Incorrectly issued 8130-3 tags are a recurring compliance problem [42].
- **Engine Shop Manual (ESM)**: the OEM's manual that defines how the engine is disassembled, inspected,
  repaired and rebuilt. Regulators treat it as the reference: an Australian airworthiness directive on the CFM56
  cites that the "CFM56-7B ESM contains instructions for calculating remaining life of each engine stationary
  part within certain time frames and thresholds" [43]. Repairs beyond the ESM require separate approval (DER
  repairs, D4).
- **OEM-licensed vs third-party repair**: an engine maintained only with OEM parts and OEM-approved repairs can
  carry CFM's TRUEngine designation [10]; GE sells "TrueChoice" overhaul agreements to the same end [44]. For a
  module exchange, what matters is that the incoming module's records show which repairs were done under which
  approvals, because a lessor's return conditions (D6) may exclude non-OEM repairs.

---

## 3. Market structure and players (brief; D2 and D11 go deeper)

- **CFM International** (GE Aerospace, NYSE: GE; Safran, Euronext: SAF): OEM; sole source of new parts at
  catalogue price; sells its own shop visits through GE Aerospace and Safran Aircraft Engines shops and
  TrueChoice agreements [1][44]. Reports CFM56 TAT "sustaining ~90 days" (May 2026) [24].
- **IAE International Aero Engines** (Pratt & Whitney/RTX, NYSE: RTX; MTU Aero Engines, Xetra: MTX; JAEC): OEM
  of the V2500, the A320ceo's alternative engine. Aircraft Commerce (2010) gave shareholdings of PW 32.5%,
  Rolls-Royce 32.5%, JAEC 23%, MTU 12% [38]; Rolls-Royce has since exited (not retrieved here; Tension T5).
- **Independent engine shops with CFM56 capability** named in this session's sources: MTU Maintenance (largest
  V2500 shop, 38% of all V2500 shop visits in 2024, 7,000th V2500-A5 visit) [45]; StandardAero (CFM56-7B QTSV
  and full shop, DFW) [27]; SR Technics (CFM56-7B parts repair, fixed-price catalogue 2024) [46]; Lufthansa
  Technik Airmotive Ireland (V2500, since closed) [38]; AJW Group (engine trading, records packs) [4].
- **FTAI Aviation** (NASDAQ: FTAI): Module Factory for -7B and -5B modules; V2500 under an IAE EngineWise
  agreement [31] (chain map).
- **Appraisers**: IBA, AVITAS, Ascend (Cirium), mba Aviation [10][28].
- **Used-parts dealers** advertising LLP packages with cycles remaining: Salvex, Aviation Fleet Support [15][32].

---

## 4. Numbers

### 4.1 Fleet and production

| Figure | Value | Source | Date |
|---|---|---|---|
| CFM56 delivered, all variants | >35,000 | CFM website [1] | undated, accessed 2026-10-03 |
| CFM56 in service | 23,000 | CFM website [1] | undated |
| CFM56-7B delivered | >15,000 | CFM website [1]; GE article on 15,000th [20] | 2019 and later |
| 737NG aircraft delivered with -7B | >7,000 | ISTAT / GE [20][22] | 2019 |
| CFM56-7B last engine for commercial 737NG | delivered by May 2019 | GE Aerospace article [20] | May 2019 |
| CFM56-5B installed-engine production ended | 2022 | ISTAT [22] | 2022 |
| A320ceo aircraft delivered with -5B | >4,100 | ISTAT [22] | 2022 |
| -5B share of A320ceo orders | ~60% | CFM website [1] | undated |
| CFM56-3 last engine shipped | 1999 | CFM/GE press release [21] | 1999 |
| CFM56-3 total | 3,974 engines / 1,987 aircraft | CFM/GE press release [21] | 1999 |
| LEAP orders and commitments | >14,270 | Safran press release [26] | Dec 2017 |
| LEAP delivered in 2017 | 459 | Safran press release [26] | Feb 2018 |
| V2500 in service | 5,286 (5,260 -A5, 26 -A1) | Aviation Week 2023 Fleet & MRO Forecast [47] | 2023 |
| V2500 shop visits next 10 years | >7,800 overhaul + 3,142 LLP | Aviation Week data tool [47] | 2023 |

### 4.2 LLP limits and prices

See tables in 2.4. Summary: -7B limits 30,000 / 20,000 / 25,000 EFC by module [3][4][5]; -5B 18 LLP sets at
20,000–30,000 [7]; -7B set list $1.775M (2008) [11], $3.4M (2018) [12], ~$4M (2019) [13], $5.7M (Jun 2025)
[16]; V2500 set list $1.7M (2010) [38]; LLP escalation step ~12% for -5B/-7B (Ishka, year not shown) [34];
CFM catalogue raised Aug 2023, -7B parts +20–30% in 2023 (Magnetic via Aviation Week) [33].

### 4.3 Shop visits

See tables in 2.6 and 2.7.

### 4.4 EGT margin

| Figure | Value | Source | Date |
|---|---|---|---|
| Fastest margin loss | first 1,000 EFC; slows after 1,000–2,000 | Aircraft Commerce [36] | 2003/2008 |
| Measured CFM56-3C1 loss since last repair | 26.2°C, 58.1% from rotor clearance | Jurnal Teknik Mesin [35] | Jun 2023 |

---

## 5. Constraints and bottlenecks

1. **The LLP clock is non-negotiable.** No inspection, repair or margin can extend a certified cycle limit;
   only a new or lower-time used part resets it. This fixes a minimum shop-visit cadence for the fleet
   regardless of condition [3][4].
2. **New LLPs are single-source at escalating list price**, ~7% a year compounded over 2008–2025 on the figures
   reached [11][12][16]. PMA exists for HPT blades (D4) but not, in this session's evidence, for LLPs.
3. **Records are a hard gate.** A module or LLP without back-to-birth traceability cannot be installed, and a
   repair outside the ESM needs separate approval, so the usable supply of modules is the documented supply,
   not the physical one [14][40][43].
4. **Shop capacity and parts lead time** have pushed full-overhaul TAT from ~60 to 90–120 days [23], which
   itself raises demand for spare engines and for module exchange (D2).
5. **Stub life** wastes paid-for cycles unless the LLP replacement is matched to the planned run, which
   requires a liquid market in part-life LLP packages and the engineering to mix them [3][15][32].
6. **No new CFM56 supply.** Installed-engine production ended in 2019 (-7B) and 2022 (-5B) [20][22]; the fleet
   of ~23,000 [1] can only shrink, and its parts come from the OEM, PMA, or teardown of other CFM56s (D3).

---

## 6. Tensions

- **T1 — CFM56-7B thrust ceiling.** The CFM website summary returned by search gives the -7B range as
  "19,500–33,000 lbf" [1]; a secondary source gives 19,500–27,300 lbf [19]. The highest certified -7B rating in
  common use is the -7B27 (27,300 lbf); the 33,000 figure may be a transcription from the -5B family. Not
  resolved here.
- **T2 — LLP set price path.** $3.4M in Oct/Nov 2018 (Aircraft Commerce) [12] against "$4m" in Nov 2019
  (Aircraft Value News headline) [13] implies +18% in one year, versus a 6.7% a year trend 2008–2018 and 7.7% a
  year 2018–2025 [11][16]. The $5.7M June 2025 figure comes from an engine-status table ("LLPC $m: 5.700") whose
  methodology and exact scope (full set? which rating?) were not visible [16].
- **T3 — Shop-visit cost ranges.** The same 2026 secondary source gives PR at $1.8–2.5M and heavy-with-LLPs
  ">$3.5M" in one place and PR $1.2–1.6M, heavy-with-LLPs $2.1–2.8M in another [17]. Separately, a full new LLP
  set at $5.7M list [16] exceeds every quoted "with LLPs" total, so those totals must assume partial or used LLP
  replacement or older prices. Leeham's 2017 "$300k light PR" for the -5 series [37] is a different workscope
  and year and is not comparable.
- **T4 — Turnaround.** Trade press: 90–120 days for a full CFM56 overhaul in 2025 [23]; GE Aerospace: "~90 days
  sustaining" in May 2026 [24]; Safe Fly: 75–90 (PR) and 120–150 (heavy) [17]. Different workscopes and shops;
  all three are recorded.
- **T5 — IAE shareholding.** Aircraft Commerce (2010) lists Rolls-Royce at 32.5% [38]; Rolls-Royce sold its
  V2500 stake to Pratt & Whitney in 2012 (widely reported; not retrieved in this session). The 2010 table is
  stale.
- **T6 — What drives removals.** Older Aircraft Commerce analysis: EGT margin erosion is "the most influential
  factor" for short-haul removals [36]. Later Aircraft Commerce (-5B) and FlightGlobal: latest -5B/-7B removals
  are LLP-driven because margin lasts to the LLP limit [6][18]. Both are reported; they describe different
  variants, ratings and eras.

---

## 7. Unknowns

- **U1** Full numbered sub-module list for the -7B and -5B (the ESM breakdown). Resolve with the CFM56-7B/-5B
  Engine Shop Manual or a CFM training manual.
- **U2** Exact list of part numbers common to the -5B and -7B core (basis for cross-variant module and LLP
  interchange). Resolve with the Illustrated Parts Catalogues or a CFM commonality bulletin.
- **U3** Per-part LLP table for the -5B (only the 18-set, 20,000–30,000 range was reached). Resolve with a -5B
  records mini-pack (AJW, StandardAero publish them).
- **U4** Prices of used LLP packages with stated cycles remaining. Resolve with dealer quotes or D3's sources.
- **U5** As-new EGT margin by -7B/-5B thrust rating and typical loss per 1,000 cycles. Resolve with Aircraft
  Commerce Issue 58 (-7B) and Issue 50 (-5B) maintenance analyses in full.
- **U6** First-run and mature-run intervals by thrust rating and region. Same sources as U5.
- **U7** Labour hours per workscope and shop labour rates (US$/hour) for CFM56 visits. Resolve with an MRO
  price catalogue or Aircraft Commerce's maintenance budgets.
- **U8** Core-only LLP group price as a share of the full set. Resolve with a CFM catalogue extract.
- **U9** Current half-life base values for -7B and -5B by rating (IBA, mba, Cirium). Resolve with an appraiser
  publication; this session's searches returned definitions, not values.
- **U10** Years and amounts of each CFM LLP escalation step 2019–2025 (only "Aug 2023, +20–30% on -7B parts"
  and "~12% LLP escalation" without a year were reached) [33][34].
- **U11** Formal regulatory definition of back-to-birth traceability and of dual release; this session reached
  industry descriptions only [14][40][41].
- **U12** Current LEAP delivery total and the dates/years of -5A and -5C production end.
- **U13** V2500 module list and current per-visit cost (2010 figures only) [38].
- **U14** Whether a module exchange requires a test-cell run under the CFM56 ESM.

Found en route, for the orchestrator: the Q2 2026 earnings release is on EDGAR at
https://www.sec.gov/Archives/edgar/data/1590364/000162828026050622/ftai6302026earningsrelease.htm (not in
edgar-index.md), and the FY2022 10-K at
https://www.sec.gov/Archives/edgar/data/1590364/000159036423000007/ftai-20221231.htm.

---

## 8. Terms introduced

- **Turbofan**: jet engine in which a front fan pushes most air around the hot core.
- **Bypass**: the air the fan moves around, not through, the core.
- **Two-shaft (two-spool)**: two concentric rotating assemblies, LP and HP, mechanically independent.
- **LP spool / HP spool**: fan + booster + LPT on one shaft; HPC + HPT on the other.
- **Booster (low-pressure compressor)**: small compressor behind the fan on the LP shaft.
- **HPC**: high-pressure compressor, nine stages on the CFM56.
- **Combustor**: chamber where fuel burns between HPC and HPT.
- **HPT / LPT**: high- and low-pressure turbines that extract power to drive the HP and LP spools.
- **Accessory gearbox (AGB)**: gear train driven from the HP spool that powers pumps and generator.
- **Thrust rating**: the control-limited thrust level at which identical hardware is sold.
- **Module**: a designed-to-be-separable section of the engine with its own serial number and records.
- **Core (gas generator)**: HPC + combustor + HPT module.
- **Major module / sub-module**: the manual's hierarchy of separable sections.
- **Fan frame**: structural front assembly carrying thrust loads and LP bearings.
- **Build standard / configuration**: the set of service-bulletin states a module is built to.
- **Module exchange**: replacing one major module with a serviceable one at the flanges.
- **Full disassembly (overhaul)**: stripping every module to piece parts.
- **Life-limited part (LLP)**: part with a certified cycle limit, scrapped at the limit regardless of condition.
- **Engine flight cycle (EFC)**: one take-off and landing, the unit of LLP life.
- **Disk / spool**: the wheels, singly or machined as one, that carry blades.
- **Stub life**: shortest remaining life among installed LLPs; also the unused life scrapped at replacement.
- **Cycles remaining (CR)**: certified limit minus cycles consumed.
- **Used LLPs**: part-life LLPs removed from another engine with full records.
- **List (catalogue) price**: the OEM's published spare-part price.
- **LLP escalation**: the OEM's annual catalogue price increase on LLPs.
- **Exhaust-gas temperature (EGT)**: gas temperature behind the LPT.
- **EGT margin (EGTM)**: red-line EGT minus actual take-off EGT on a hot day.
- **Time on wing**: cycles or hours between installation and removal.
- **Shop visit**: removal of the engine for work in a shop.
- **Workscope**: which modules are opened and how deep.
- **Hospital / quick-turn visit (QTSV)**: minimal-scope visit to fix one finding.
- **Borescope / boroblend**: internal inspection by camera; blending out small blade damage.
- **LRU / QEC**: line-replaceable unit (accessory); quick-engine-change kit of external hardware.
- **Top-case repair**: opening the upper HPC case half for blade and vane work.
- **Performance restoration (PR) / core PR**: restoring EGT margin by rebuilding the core.
- **First run / mature run**: new-to-first-visit interval; subsequent intervals.
- **Turnaround time (TAT)**: induction to redelivery.
- **Test-cell run**: post-build run to confirm thrust, EGTM and vibration.
- **Half-life value**: value assuming every maintenance item is half-consumed.
- **Full-life value**: value with all items fresh and all LLPs at zero cycles.
- **Maintenance-adjusted value**: half-life value corrected for actual status.
- **Sum of modules / sum of parts**: engine value computed module by module, or as parts.
- **Back-to-birth traceability**: unbroken cycle record for an LLP since manufacture.
- **Serviceable / unserviceable**: released for installation / removed pending repair or scrap.
- **FAA Form 8130-3**: US airworthiness approval tag for new or released parts.
- **EASA Form 1**: the European equivalent release certificate.
- **Dual release**: a tag signed under both FAA and EASA authority.
- **Engine Shop Manual (ESM)**: OEM manual defining approved shop work and limits.
- **TRUEngine / TrueChoice**: CFM's OEM-configuration designation; GE's overhaul service agreements.
- **ISTAT**: International Society of Transport Aircraft Trading, which standardises appraisal terms.

---

## 9. Sources

1. CFM International, "The CFM56 engine family", https://www.cfmaeroengines.com/engines/cfm56 (undated; accessed 2026-10-03).
2. (reserved)
3. Aircraft Commerce, Maintenance & Engineering, Issue 34, 2004 (LLP policy, stub life), https://aircraft-commerce.com/wp-content/uploads/aircraft-commerce-docs/Maintenance/2004/ISSUE%2034-MTCE.pdf
4. AJW Group, ESN 889979 CFM56-7B26 mini-pack (LLP status), 2022, https://www.ajw-group.com/storage/downloads/1644847608_esn_889979_mini_pack_cfm56-7b26.pdf
5. StandardAero, ESN 892820 mini-pack, Mar 2025, https://standardaero.com/wp-content/uploads/2025/03/ESN-892820-Mini-Pack-PDF.pdf
6. Aircraft Commerce, CFM56-5A/-5B maintenance analysis, Issue 50, https://aircraft-commerce.com/wp-content/uploads/aircraft-commerce-docs/Aircraft%20guides/CFM56-5A-5B/ISSUE%2050-CFM56-5A-5B%20MTCE.pdf
7. Leeham News, Bjorn's Corner, "New aircraft technologies, Part 49: Engine maintenance", 8 Mar 2024, https://leehamnews.com/2024/03/08/bjorn-s-corner-new-aircraft-technologies-part-49-engine-maintenance/
8. Aircraft Commerce, CFM56-7B Owner's & Operator's Guide, Issue 58, 2008, https://www.aircraft-commerce.com/wp-content/uploads/aircraft-commerce-docs1/Aircraft%20guides/CFM56-7B/ISSUE58_CFM56_7B_GUIDE.pdf
9. CFM56 training material (four-module description), Scribd, https://www.scribd.com/doc/44756596/Engine-CFM56 (undated).
10. CFM International / GE Aerospace, "CFM International launches TRUEngine program", https://www.cfmaeroengines.com/press-articles/cfm-international-launches-truenginetrade-program
11. Aircraft Commerce, CFM56-7B maintenance analysis & budget, Issue 58, 2008, https://www.aircraft-commerce.com/wp-content/uploads/aircraft-commerce-docs1/Aircraft%20guides/CFM56-7B/ISSUE58_CFM56_7B_MTCE.pdf
12. Aircraft Commerce, Maintenance & Engineering, Issue 120, Oct/Nov 2018, https://www.aircraft-commerce.com/sample_article_folder/120_MTCE_B.pdf
13. Aircraft Value News, "Engine life limited parts pricing continues to rise: $4m for CFM56-7", Nov 2019, https://www.aircraftvaluenews.com/engine-life-limited-parts-pricing-continues-to-rise-4m-for-cfm56-7
14. AviTrader, "Effective engine LLP management", 23 Apr 2026, https://avitrader.com/2026/04/23/effective-engine-llp-management/
15. Aviation Fleet Support, "All CFM56-5B & -7B Core LLP Package 6235 CR", https://aviationfleetsupport.com/parts-category/cfm56-5b-7b-core-llp-package-6235-cr/ (undated listing).
16. MyAirTrade, Engine status resource (LLPC $m 5.700, June 2025), https://www.myairtrade.com/resources/enginestatus
17. Safe Fly Aviation, "What determines aircraft engine overhaul costs?" and "CFM56-7B engine availability report 2026", https://safefly.aero/blog-aircraft-engine-overhaul-cost-drivers/ ; https://safefly.aero/cfm56-7b-engine-availability-report/ (2026; secondary).
18. FlightGlobal, "CFM56 overhaulers see light at end of tunnel", https://www.flightglobal.com/mro/cfm56-overhaulers-see-light-at-end-of-tunnel/142974.article (date not shown).
19. ePlaneAI, "Behind the numbers: maintenance insights on the CFM56-7B engine", https://www.eplaneai.com/news/behind-the-numbers-maintenance-insights-on-the-cfm56-7b-engine (secondary).
20. GE Aerospace, "1 billion flight hours: 'World-class experience' builds 15,000th CFM56-7B engine", Paris Air Show 2019, https://www.geaerospace.com/news/articles/manufacturing-paris-airshow-people-product/1-billion-flight-hours-world-class-experience
21. CFM International / GE, "Last CFM56-3 rolls off production line", 1999, https://www.cfmaeroengines.com/press-articles/last-cfm56-3-rolls-off-production-line
22. ISTAT, "CFM International CFM56-5B/-7B" (Aircraft Supporting Assets), https://www.istat.org/ISTAT-Online/ISTAT-Online/Aircraft-Supporting-Assets/ArtMID/1205/ArticleID/1677/CFM-International-CFM56-5B-7B
23. Aviation Business News / AVM, "Inside the engine MRO supply chain: why repair delays are rising and what's driving them", 2025, https://www.aviationbusinessnews.com/mro/mro-interviews-comments-articles/inside-the-engine-mro-supply-chain-why-repair-delays-are-rising-and-whats-driving-them/
24. GE Aerospace, Bernstein Strategic Decisions Conference presentation, 27 May 2026, https://www.geaerospace.com/sites/default/files/geaerospace_bernstein_strategic_decisions_conference_presentation_052726.pdf
25. CFM International, "100th CFM56-5C-powered Airbus A340 delivered", https://www.cfmaeroengines.com/press-articles/100th-cfm56-5c-powered-airbus-a340-delivered
26. Safran, "2017 CFM orders surpass 3,300 engines", 6 Feb 2018, https://www.safran-group.com/pressroom/2017-cfm-orders-surpass-3300-engines-2018-02-06-0
27. StandardAero, CFM56-7B engine services brochure, Oct 2022, https://standardaero.com/wp-content/uploads/2022/10/StandardAero-CFM56-7B-Engine.pdf
28. ISTAT, Jetrader, Jul/Aug 2010, p.16 (half-life definition), https://www.nxtbook.com/nxtbooks/naylor/ISTS0410/index.php?startid=16
29. VREF, "How do engines affect airplane values", https://vref.com/news/how-do-engines-affect-airplane-values/
30. Aircraft Value News, "Concept of half to full life fluid as aircraft move past mid-life", https://www.aircraftvaluenews.com/concept-of-half-to-full-life-fluid-as-aircraft-move-pass-mid-life/ ; Law Insider, "Maintenance Adjusted CMV", https://lawinsider.com/dictionary/maintenance-adjusted-cmv
31. FTAI Aviation Ltd., Form 10-K FY2025, https://www.sec.gov/Archives/edgar/data/1590364/000162828026012940/ftai-20251231.htm
32. Salvex, "CFM56-7B27E/B1F engine LLP package, 7,445 cycles remaining", https://www.salvex.com/listings/listing_detail.cfm/aucid/183060698/
33. Aviation Week, "Magnetic expects CFM56 market challenges, opportunities in 2024", https://aviationweek.com/mro/aircraft-propulsion/magnetic-expects-cfm56-market-challenges-opportunities-2024 ; Magnetic Group, "The current state and future of CFM56 USM engine pricing", https://www.magneticgroup.co/the-current-state-and-future-of-cfm56-usm-engine-pricing/
34. Ishka, "Pratt & Whitney mulls further LLP escalation hike", https://www.ishkaglobal.com/News/Article/6978/Pratt-Whitney-mulls-further-LLP-escalation-hike
35. Jurnal Teknik Mesin (Mercu Buana), CFM56-3C1 EGT margin analysis, Jun 2023, https://publikasi.mercubuana.ac.id/index.php/jtm/article/download/16716/7018
36. Aircraft Commerce, Maintenance & Engineering, Issue 27, 2003 (EGT margin mechanics), https://aircraft-commerce.com/wp-content/uploads/aircraft-commerce-docs1/Maintenance/2003/ISSUE%2027-MTCE-A.pdf ; and Issue 58 -7B maintenance analysis [11].
37. Leeham News, Bjorn's Corner, "Aircraft engine maintenance, Part 3", 17 Mar 2017, https://leehamnews.com/2017/03/17/bjorns-corner-aircraft-engine-maintenance-part-3/
38. Aircraft Commerce, Maintenance & Engineering, Issue 70, 2010 (V2500 shop-visit costs, IAE shareholding), https://aircraft-commerce.com/wp-content/uploads/aircraft-commerce-docs/Maintenance/2010/ISSUE70_MTCE_B.pdf
39. Aircraft Value News, "PMA continues to undermine full-life maintenance adjustments", https://www.aircraftvaluenews.com/pma-continues-to-undermine-full-life-maintenance-adjustments/
40. Aviation Suppliers Association, J. Dickstein, 8130-3 workshop, 28 Jun 2016, https://www.aviationsuppliers.org/ASA/files/ccLibraryFiles/Filename/000000001650/2016-06-28WorkshopLrev2-JDickstein.pdf ; ASA Member Bulletin May 2016, https://www.aviationsuppliers.org/ASA-Member-Bulletin---May-2016---Aircraft-Articles-and-Eligibility-for-an-Export-8130-3-tag
41. Aviation Business News, "The evolution of airworthiness documentation for aircraft parts", https://www.aviationbusinessnews.com/in-depth/the-evolution-of-airworthiness-documentation-for-aircraft-parts/
42. Aviation Maintenance magazine, "8130-3 airworthiness approvals: identifying incorrectly issued tags", https://avm-mag.com/?p=39314
43. CASA (Australia), AD 2014-0130 (CFM56), https://services.casa.gov.au/airworth/airwd/ADfiles/TURBINE/CFM56/2014-0130.pdf
44. MRO Global, "Safair expands GE's TrueChoice overhaul agreement for CFM56 engines", https://www.mroglobal-online.com/safair-expands-ges-truechoice-overhaul-agreement-cfm56-engines/
45. MTU Aero Engines, "MTU Maintenance completes 7,000th shop visit for a V2500-A5 engine", 2025, https://www.mtu.de/newsroom/press/latest-press-releases/press-release-detail/mtu-maintenance-completes-7000th-shop-visit-for-a-v2500-a5-engine/
46. SR Technics, CFM56-7B engine parts repair services capabilities and fixed-prices catalogue, 24 Jun 2024, https://www.srtechnics.com/media/2xef3lpi/cfm-7b-sr-technics-capabilities-price-catalogue-24062024.pdf
47. Aviation Week, "Data tool: the future of IAE V2500 engine", 2023, https://ngstage.aviationweek.com/mro/aircraft-propulsion/data-tool-future-iae-v2500-engine
48. Leeham News, "GE's LEAP engines shipped today should match durability of the venerable CFM56, company says", 27 May 2026, https://leehamnews.com/2026/05/27/ges-leap-engines-shipped-today-should-match-durability-of-the-venerable-cfm56-company-says/
49. Visual Approach, "Wave of early LEAP-1A/1B shop visits frustrating operators", https://visualapproach.io/wave-of-early-leap-1a-1b-shop-visits-frustrating-operators/
50. InsideFlyer / ePlaneAI, "CFM upgrade doubles LEAP engine life in harsh climates" (LEAP-1A HPT durability kit certification), https://www.insideflyer.com/posts/cfm-upgrade-doubles-leap-engine-life-in-harsh-climates/
51. AJW Group / LARA, "CFM LEAP engine maintenance", Apr 2025, https://www.ajw-group.com/storage/downloads/1751451168_article_lara_-_cfm_leap_engine_maintenance_04.25.pdf
52. Aircraft Commerce, "Analysis and comparison of the CFM56-5B's, -7's and V2500-A5's maintenance costs", Issue 28, 2003, https://www.aircraft-commerce.com/wp-content/uploads/aircraft-commerce-docs1/Maintenance/2003/ISSUE%2028-MTCE-B.pdf (located; figures not read).
