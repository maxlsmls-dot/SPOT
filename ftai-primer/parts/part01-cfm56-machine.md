---
title: Part I — First principles: the CFM56 as a machine
header: FTAI Deep Primer — Part I
as_of: Research as of 3 October 2026
subtitle: Descriptive reference. Sources are cited inline and listed at the end. Takes no view.
toc: true
---

<div class="part-divider"><div class="pn">Part I</div><h1>First principles: the CFM56 as a machine</h1><p>This Part explains the engine that the whole FTAI Aviation story is built on: how it works, how it comes apart, what wears out, what is scrapped on a clock, what a repair costs and what the engine is worth at any point in its life. A reader who finishes it will be able to read a shop-visit quote, an engine records summary and an appraiser's value with every term understood.</p></div>

### Where this Part sits in the build

The primer is built in layers. Parts I and II are first principles: Part I is the engine as a physical and economic object, and Part II is how money moves around that object through leases, reserves and financing. Part III is the context, meaning the fleet, the retirements that did not happen, the new engines that arrived late, and a translation table that turns each of those facts into a requirement on the aftermarket. Parts IV to IX are the segments, three for the market around FTAI and three for FTAI's own businesses, and each of them opens by naming the translation-table rows it answers. Parts X and XI cover the company and the money, and Part XII is reference. Nothing in this Part depends on anything written later; everything written later depends on this Part.

## 1. What a turbofan does, functionally

A jet engine takes in air, squeezes it, burns fuel in it and lets the hot gas rush out of the back. The rush of gas pushes the engine forward. A turbofan is a jet engine with a large fan bolted on the front. The fan pushes most of the air around the outside of the hot central part of the engine, not through it. Only a small share of the air goes through the middle, where the fuel is burned. That burning drives turbines, and the turbines turn the fan. So the hot middle of the engine exists mainly to spin the fan, and the fan does most of the pushing.

<div class="defn"><b>Turbofan, bypass and high-bypass turbofan</b><p>A turbofan is a jet engine in which a large front fan pushes most of the incoming air around the hot core rather than through it. The air that goes around is the bypass stream. A high-bypass turbofan is one in which the bypass stream is several times larger than the core stream; the CFM56 is one. <span class="cite">[D1 §2.1]</span></p></div>

The split between the two streams has a name. The bypass ratio is the mass of air the fan pushes around the core divided by the mass of air that passes through the core. A ratio of five means five kilograms of air go around for every kilogram that goes through. A higher ratio moves more air more slowly, which is the efficient way to make thrust at airliner speeds. The research for this primer classified the CFM56 as a high-bypass design but did not retrieve its bypass ratio as a figure, so none is quoted here.

<div class="defn"><b>Core (gas generator)</b><p>The core is the hot, fast, expensive middle of the engine: the high-pressure compressor, the combustor and the high-pressure turbine, treated as one module. The industry also calls it the gas generator. In Part VII the same word has a second meaning, the unserviceable unit a customer hands back in an exchange; that Part flags the double meaning where it arises. <span class="cite">[D1 §2.3; registry C-6]</span></p></div>

Thrust is the push. It is quoted in pounds-force, written lbf. A CFM56-7B is sold at ratings between 19,500 and 27,300 lbf according to one secondary source, and the CFM website summary returned by search gave a ceiling of 33,000 lbf; the dossier records that the higher figure may be a transcription from the -5B family and did not resolve it. <span class="cite">[ePlaneAI, undated; CFM website, undated; D1 T1]</span> The important point about thrust for this Part is that one set of hardware is sold at several ratings.

<div class="defn"><b>Thrust and thrust rating</b><p>Thrust is the engine's forward push, in pounds-force (lbf). A thrust rating is the thrust level at which a given set of hardware is sold; the engine's electronic control limits how hard it may run, and the model suffix gives the rating in thousands of lbf (a -7B24 is rated at 24,000 lbf, a -7B27 at 27,300). A higher rating is the same metal working hotter, so it has less temperature margin and a shorter life between overhauls, and it is worth more because it can serve heavier aircraft and be turned down to a lower rating; a low-rated engine cannot be turned up without paying the manufacturer. <span class="cite">[D1 §2.1; IBA (an appraiser), Sept 2025, via D3 §2.4]</span></p></div>

The CFM56 has two rotating assemblies, one inside the other, and they are not geared together. The outer assembly carries the fan at the front and a turbine at the back. The inner assembly carries the main compressor and a smaller, hotter turbine. The two spin at different speeds. The only thing that connects them is the air passing from one to the other.

<div class="defn"><b>Two-shaft (two-spool) design; low-pressure and high-pressure spools</b><p>A spool is a rotating assembly of compressor and turbine stages on one shaft. The CFM56 has two, one inside the other. The low-pressure (LP) spool carries the fan, a small booster compressor and the rear turbine on the outer shaft. The high-pressure (HP) spool carries the main compressor and the front turbine on a shorter inner shaft. The two are mechanically independent and connected only by the air flowing through them. <span class="cite">[D1 §2.1]</span></p></div>

Two units of time govern everything that follows. The first is the flight cycle: one take-off and one landing. The second is the flight hour: one hour with the engine running. They are not interchangeable. A short-haul aircraft flies many cycles per hour of operation; a long-haul aircraft flies few. The parts that wear by heat and rotation count hours. The parts that are certified to a life limit count cycles, because the stress that matters is the spin-up and heat-up at take-off, not the steady hours in cruise.

<div class="defn"><b>Engine flight cycle (EFC) and engine flight hour (EFH)</b><p>An engine flight cycle (EFC), or simply a flight cycle (FC) or "cycle", is one take-off and landing. An engine flight hour (EFH), or flight hour (FH), is one hour of engine operation. Life limits on rotating parts are certified in cycles, because the stress peak that consumes their life is the spin-up and heat-up at take-off. Maintenance reserves and cost-per-unit arithmetic (Part II §13) use both units. A mature short-haul narrowbody flies roughly 1,000 to 1,500 cycles a year. <span class="cite">[D1 §2.4; Aircraft Value News, undated]</span></p></div>

Everything in Part I follows from four physical facts. The engine is built as separable sections. Inside those sections sit parts certified to a fixed number of cycles. The hot section loses temperature margin as it wears. And the engine is only as usable as its paperwork says it is. Sections 3 to 9 take those facts in turn. Section 10 sets two other engines beside the CFM56 for contrast, and section 11 gives a first map of where money is made along the chain, which Part XI §86 treats in full.

## 2. The CFM56 family and its fleet

The CFM56 is built by a company owned equally by two others. That matters because the owner of an engine's design is the only party allowed to make new parts for it, and it controls the manual that says how the engine may be repaired.

<div class="defn"><b>Original equipment manufacturer (OEM)</b><p>The OEM is the company that holds the type certificate for the engine, meaning the regulator's approval of its design, and that built it. It is the sole source of new parts at its published catalogue price, it runs its own network of repair shops and branded service agreements, and GE states that it is also the largest supplier of used material for its own products. Part IV §25 carries the full treatment. <span class="cite">[D2 §2.2–2.3; D4 §2.1]</span></p></div>

<div class="defn"><b>CFM International (CFM)</b><p>CFM International is the joint venture of GE Aerospace and Safran Aircraft Engines (formerly Snecma) that is the OEM and type-certificate holder of the CFM56 and of its successor, the LEAP (CFM's new-generation engine, treated in §10). CFM describes itself as a joint venture; the 50/50 split is how it has always been described and is carried here as the widely published figure, not one the research re-verified. Within the venture GE builds the core and Safran the fan, booster, low-pressure turbine and gearbox. Part IV §25 carries the OEM network. <span class="cite">[CFM website, undated; D1 §2.2; D2 §3.1; D4 §2.1]</span></p></div>

The family has five commercial members. Two of them matter for FTAI: the -7B, which is the only engine ever fitted to the Boeing 737 Next Generation, and the -5B, which powers about six in ten of the Airbus A320 family's current-engine-option aircraft. The other three are older or belong to aircraft types that have largely left service.

<div class="defn"><b>CFM56 family (-3, -5A, -5B, -5C, -7B)</b><p>The CFM56 is a two-shaft, high-bypass turbofan of which more than 35,000 have been delivered since entry into service in 1982, with roughly 23,000 to 24,000 in service depending on the source (§2.2). The -7B is the sole engine of the 737NG, with more than 15,000 built and the last engine for a commercial 737NG delivered in 2019. The -5B powers about 60% of A320ceo-family aircraft, and production of installed -5B engines ended in 2022. No new CFM56 is being built for an airframe, so every CFM56 that flies tomorrow is one that exists today. <span class="cite">[CFM website, undated; GE Aerospace, 2019; ISTAT (the International Society of Transport Aircraft Trading), undated]</span></p></div>

<div class="defn"><b>737NG and A320ceo</b><p>The 737NG (Next Generation) is the Boeing 737-600, -700, -800 and -900ER, built from about 1997 to 2019 and powered only by the CFM56-7B. The A320ceo (current engine option) is the Airbus A318, A319, A320 and A321 family built from about 1988 to 2020, powered by either the CFM56-5B or the V2500 (the alternative engine from the IAE consortium, §10). These two airframe families are what the whole chain described in this primer serves. <span class="cite">[D1 §2.2; D6 §2.4]</span></p></div>

### 2.1 The variants

<div class="exh"><div class="exh-title">Exhibit 1.1 — The CFM56 family: airframes, thrust, production status and deliveries</div>

| Variant | Airframe | Thrust class (lbf) | Production status | Delivered | Source |
|---|---|---|---|---|---|
| CFM56-3 | Boeing 737 Classic (-300/-400/-500); smaller fan for ground clearance | 18,500–23,500 | Last engine shipped 1999 | 3,974 engines on 1,987 aircraft | CFM/GE release, 1999 |
| CFM56-5A | Airbus A320 (early build) | 22,000–34,000, quoted jointly for -5A/-5B/-5C | Ended; year not retrieved | Not retrieved | CFM website, undated |
| CFM56-5B | A318/A319/A320/A321 (A320ceo); "nearly 60%" of A320ceo ordered | Within 22,000–34,000 | Installed-engine production ended 2022 | >4,100 -5B-powered aircraft | CFM website; ISTAT, undated |
| CFM56-5C | Airbus A340-200/-300 (sole engine) | Upper end of 22,000–34,000 | A340 out of production; end year not retrieved | Not retrieved | CFM website; CFM release on the 100th A340 |
| CFM56-7B | Boeing 737NG (-600/-700/-800/-900ER), sole engine | 19,500–27,300 per a secondary source; "19,500–33,000" per the CFM website summary (D1 T1) | Last engine for a commercial 737NG delivered by May 2019; 15,000th built 2019 | >15,000 engines; >7,000 aircraft | CFM website; GE Aerospace, 2019; ePlaneAI |

<cite>Source: CFM International, "The CFM56 engine family", undated, accessed 2026-10-03; CFM/GE, "Last CFM56-3 rolls off production line", 1999; GE Aerospace, "1 billion flight hours", Paris Air Show 2019; ISTAT, "CFM International CFM56-5B/-7B", undated; ePlaneAI, "Behind the numbers", undated. Compiled in D1 §2.2 and §4.1.</cite></div>

Two dates in that table do most of the work in this primer. The last -7B for a commercial 737NG was delivered by May 2019, and installed-engine production of the -5B ended in 2022. <span class="cite">[GE Aerospace, 2019; ISTAT, undated]</span> From those dates onward the number of CFM56 engines in the world can only fall. Every engine retired, torn down for parts, or converted to some other use leaves the pool, and nothing enters it. Part III §18 and §19 treat the consequences.

### 2.2 How many there are

Counting the fleet sounds simple and is not. The sources disagree, and the disagreement is partly about what is being counted.

<div class="defn"><b>Installed base</b><p>The installed base is the population of engines fitted to aircraft in the operating fleet. Published figures for the CFM56 "in service" range from about 23,000 to about 24,000 and may include spare and stored engines as well as installed ones, since none of the sources states its basis. Because no new -5B or -7B is being built, the base falls by exactly the number of engines retired or converted each year. Part III §18 carries the full treatment. <span class="cite">[D9 §2.1–2.2; registry C-11]</span></p></div>

<div class="exh"><div class="exh-title">Exhibit 1.2 — CFM56 fleet counts, by source, basis and date</div>

| Figure | What it counts | Source and level | Date |
|---|---|---|---|
| >35,000 | CFM56 delivered, all variants | CFM website (OEM web page) | Undated, accessed 2026-10-03 |
| ~23,000 | CFM56 "in service" | CFM website (OEM web page) | Undated |
| ~24,000 | CFM56 "in service", of >35,000 delivered | Aviation Business News (trade press) | September 2025 |
| >22,800 | CFM56 in Safran's civil installed base | Safran FY2025 results presentation (OEM investor material) | 13 February 2026 (end-2025 figure) |
| "over 20,000" | CFM56-5B and -7B in service | Chromalloy press release (parts maker) | 30 October 2025 |
| >19,000 | CFM56 "flying" | Safe Fly Aviation (consultancy blog) | 2026 |
| ~14,200 | "active" CFM56, read by one dossier as all variants (≈6,200 -5B, ≈7,500 -7B) and by another as the -7B fleet alone | Safe Fly Aviation (consultancy blog) | 2026 |
| "in excess of 8,000" | CFM56-7B "currently installed in 737NGs" | CFM product page (OEM web page) | Undated |
| >15,000 | CFM56-7B delivered | CFM website; GE Aerospace article on the 15,000th engine | 2019 and later |

<cite>Source: CFM International, "The CFM56 engine family" and "CFM56-5B & CFM56-7B" product page, undated; Aviation Business News, "CFM56 turbofan aircraft engine", Sept 2025; Safran, FY2025 Results & Investor Update, 13 Feb 2026; Chromalloy, release of 30 Oct 2025; Safe Fly Aviation, "CFM56 Engine Market Report 2026"; GE Aerospace, 2019. Reconciliation R-001, R-002, R-003 and R-069.</cite></div>

The three OEM-level figures sit close together: about 23,000 on CFM's own page, about 24,000 in trade press citing September 2025, and more than 22,800 in Safran's end-2025 count. <span class="cite">[CFM website, undated; Aviation Business News, Sept 2025; Safran, 13 Feb 2026]</span> None of them says whether spare engines in warehouses and engines on parked aircraft are included. The research recorded that question as open. <span class="cite">[D9 U3; reconciliation R-001]</span> The two Safe Fly Aviation figures come from a consultancy blog and are labelled as such wherever they appear in this primer; the 14,200 figure was read by one dossier as the whole active CFM56 fleet and by another as the -7B fleet alone, and this Part reports both readings without choosing. <span class="cite">[Safe Fly Aviation, 2026; reconciliation R-002]</span>

The -7B count has its own puzzle. CFM's product page says "in excess of 8,000 CFM56-7Bs are currently installed in 737NGs", with no date visible, while the same company reports more than 15,000 -7B engines delivered and more than 7,000 737NG aircraft, each carrying two. <span class="cite">[CFM product page, undated; GE Aerospace, 2019; reconciliation R-003]</span> Two 737NGs per 8,000 engines would be 4,000 aircraft, far fewer than were delivered; the statement may be old, or may count only one subset. The research did not resolve it. Total deliveries are given as more than 35,000 by CFM and the trade press, and as "well over 30,000" in one dossier's unsourced general statement; the OEM figure is the one carried. <span class="cite">[reconciliation R-069]</span>

### 2.3 Why the fleet only shrinks

An engine leaves the base in one of three ways. It is retired with its aircraft and torn down for parts (Part V §32). It is sold on as a whole engine to another operator, which does not reduce the base. Or it is converted to a non-aviation use, which FTAI's power business has begun to do with CFM56 cores (Part IX). The rate at which engines leave is the retirement rate.

<div class="defn"><b>Retirement rate</b><p>The retirement rate is the share of a fleet withdrawn from service in a year. GE's planning assumption for CFM56 retirements in 2026 moved from 3–4% of the installed base, to 2–3%, to 1.5–2%; GE reported about 1.5% retired in 2025 and expected about 2% in 2026, and first-quarter 2026 retirements ran "below 1%". Other sources use other denominators (all commercial aircraft, or the active-plus-stored passenger fleet), so every figure must carry its base. Part III §19 is the full treatment. <span class="cite">[GE CFO via Aviation Week, 2026; GE Q4 2025 results via Leeham, 22 Jan 2026; GE Aerospace investor-relations page, 2026; registry C-10]</span></p></div>

The arithmetic that connects the base to the rest of this primer is short. On a base of about 24,000 engines, a retirement rate of 1.75% removes about 420 engines a year, and a rate of 3.5% removes about 840. <span class="cite">[D9 §2.2, illustrative arithmetic on sourced figures]</span> Every engine that does not retire keeps flying, keeps accumulating cycles, and will need the work described in sections 4 to 7. Every engine that does not retire is also one that is not torn down, so its parts do not reach the used-material market described in Part V. The same number sits on both sides of the aftermarket at once, which is why Part III makes so much of it.

## 3. Modules: how the engine comes apart, and why modules are interchangeable

The CFM56 was designed to be taken apart at a few large joints rather than stripped to its last bolt every time something inside it needs attention. The sections between those joints are modules.

<div class="defn"><b>Module</b><p>A module is a section of the engine designed to be removed and replaced as a unit. It is bolted to its neighbours at flanges, and it carries its own part number, its own serial number and its own maintenance record. A module can move from one engine to another when its configuration, its records and its part numbers allow. Section 3.2 sets out the conditions. <span class="cite">[D1 §2.3; D3 §2.7]</span></p></div>

<div class="defn"><b>Major module and sub-module</b><p>The manufacturer's shop manual arranges the engine as a hierarchy. The major modules (the fan and booster, the core, the low-pressure turbine, and the accessory gearbox) are each built from numbered sub-modules. The full numbered sub-module list for the -7B and -5B was not reached by the research, which recorded the commonly cited count of 17 as unverified; this primer does not quote a count. <span class="cite">[D1 §2.3, U1]</span></p></div>

### 3.1 The modules and what each one does

Air enters at the fan and leaves at the back of the low-pressure turbine. The modules sit in that order along the engine, with the gearbox hung beneath.

<div class="defn"><b>Booster, or low-pressure compressor (LPC)</b><p>The booster is a small three-stage compressor mounted directly behind the fan on the low-pressure shaft. It gives the air bound for the core a first squeeze before the main compressor takes over. The fan and booster together form the first major module. <span class="cite">[Aircraft Commerce Issue 58, 2008; D1 §2.1]</span></p></div>

<div class="defn"><b>Fan frame</b><p>The fan frame is the structural front assembly of the engine, built from four main pieces: the containment case that would catch a released fan blade, the outlet guide vanes that straighten the fan's airflow, the frame itself, and the housing for the radial shaft that drives the gearbox. It ducts both airstreams, passes the engine's thrust to the aircraft, and carries the bearings of the low-pressure rotor. It is the manual's example of a numbered sub-module. <span class="cite">[Aircraft Commerce Issue 58, 2008]</span></p></div>

<div class="defn"><b>High-pressure compressor (HPC)</b><p>The high-pressure compressor is the nine-stage compressor on the high-pressure spool, driven by the high-pressure turbine behind it. It raises the core airflow to the pressure at which fuel can be burned efficiently. Its spools and disks are life-limited parts with a 20,000-cycle limit on the -7B (§4). <span class="cite">[Aircraft Commerce Issue 58, 2008; D1 §2.4]</span></p></div>

<div class="defn"><b>Combustor</b><p>The combustor is the chamber between the high-pressure compressor and the high-pressure turbine in which fuel is sprayed into the compressed air and burned. It is part of the core module. <span class="cite">[D1 §2.1]</span></p></div>

<div class="defn"><b>High-pressure turbine (HPT)</b><p>The high-pressure turbine is the single-stage turbine immediately behind the combustor. It takes power from the hottest gas in the engine and uses it to drive the high-pressure compressor. It is the hottest, fastest-wearing and most expensive module to restore: its blades and vanes are 15–25% of a shop visit's parts cost, and most of the engine's lost temperature margin is recovered there (§5). Its disk is a 20,000-cycle life-limited part. <span class="cite">[Safe Fly Aviation, 2026; D1 §2.5]</span></p></div>

<div class="defn"><b>Low-pressure turbine (LPT)</b><p>The low-pressure turbine is the four-stage turbine at the rear of the engine. It takes the remaining energy from the gas after the high-pressure turbine and drives the fan and booster through the long low-pressure shaft. With the turbine rear frame it forms the third major module. Its disks are 25,000-cycle life-limited parts. <span class="cite">[Aircraft Commerce Issue 58, 2008; D1 §2.4]</span></p></div>

<div class="defn"><b>Accessory gearbox (AGB)</b><p>The accessory gearbox is a train of gears driven off the high-pressure spool by a radial shaft running out through the fan frame. It turns the fuel pump, the oil pumps, the hydraulic pump and the aircraft's electrical generator. It is the fourth module in the manual's hierarchy and sits outside the gas path. <span class="cite">[D1 §2.1, §2.3]</span></p></div>

<div class="exh"><div class="exh-title">Exhibit 1.3 — The CFM56-7B modules: contents, function and life-limit clock</div>

| Major module | Contents on the -7B | What it does | Life-limited parts and limit (EFC) | Source |
|---|---|---|---|---|
| Fan and booster | 61-inch fan with 22 solid titanium wide-chord blades; three-stage booster; fan frame sub-module | Moves the bypass air that produces most of the thrust; booster pre-compresses the core air; fan frame carries thrust and the LP bearings | Fan disk and booster spool, 30,000 | Aircraft Commerce Issue 58, 2008; AJW (AJW Group, an engine trader) and StandardAero mini-packs |
| Core (HPC, combustor, HPT) | Nine-stage HPC; combustor; single-stage HPT | Compresses, burns, and extracts the power that drives the HPC; the hottest and most expensive section | HPC stage 1–2 spool, stage 3 disk, stage 4–9 spool, HPT disk, all 20,000 | Same |
| Low-pressure turbine | Four-stage LPT and turbine rear frame | Drives the fan and booster through the LP shaft | LPT stage 1 disk, 25,000 (other LPT disks and shafts listed in the packs without limits in the returned text) | Same |
| Accessory gearbox | Gear train driven by a radial shaft from the HP spool | Powers fuel, oil and hydraulic pumps and the generator | None appears in the records packs the research reached | D1 §2.1, §2.3 |

<cite>Source: Aircraft Commerce, CFM56-7B Owner's & Operator's Guide, Issue 58, 2008; CFM56 training material (four-module description), Scribd, undated; AJW Group mini-pack for ESN (engine serial number) 889979, 2022; StandardAero mini-pack for ESN 892820, Mar 2025. Compiled in D1 §2.1, §2.3 and §2.4.</cite></div>

The -5B is described in CFM-derived training material as the same four modules: the fan and low-pressure compressor; the high-pressure compressor, combustion chamber and high-pressure turbine; the low-pressure turbine and turbine rear frame; and the accessory gearbox. <span class="cite">[CFM56 training material, Scribd, undated]</span> The -7B has the same architecture. <span class="cite">[Aircraft Commerce Issue 58, 2008]</span>

### 3.2 How many modules an engine has, and why the sources disagree

The dossiers behind this primer describe the CFM56 as having three, four, four to five, or six modules. The disagreement is not about the hardware. It is about which level of the hierarchy is being counted and whether the gearbox is included.

<div class="exh"><div class="exh-title">Exhibit 1.4 — "How many modules?": each source's list and the level it counts at</div>

| Count | List as given | Where it comes from | What the count includes |
|---|---|---|---|
| 4 | Fan and booster; core (HPC + combustor + HPT); LPT; accessory gearbox | D1 (CFM-derived training material and Aircraft Commerce); D3 §2.7 uses the same four | Three gas-path major modules plus the gearbox |
| 3 (+1) | Fan/booster, core and LPT "as the three major modules, with the accessory gearbox as a fourth" | D2 §2.1 | The gas-path modules, gearbox set aside |
| 3 per engine | "450 modules (150 engines)"; "1,800 modules (600 engines)" | FTAI release on QuickTurn Europe, 26 Feb 2025; stated as FTAI's convention in D8 | FTAI's counting convention: fan, core, LPT |
| 4 to 5 | Fan and booster; HPC; combustor plus HPT ("the core"); LPT; plus the gearbox | D5 §2.1, §2.4; D9 §2.1 ("four to five major sub-assemblies") | Splits the HPC out of the core; gearbox optional |
| 5 | Fan; HPC; HPT; LPT; plus accessory gearbox | D7 §2.4 | Counts compressor and turbine of the core separately |
| 4 | Fan; HPC; HPT; LPT | D10 §2.4 | Same as D7 without the gearbox |
| 6 | Fan; booster; HPC; combustor; HPT; LPT | D11 §2.3 | Every gas-path component counted separately, no gearbox |

<cite>Source: dossiers D1, D2, D3, D5, D7, D8, D9, D10 and D11 as cited in each row; FTAI Aviation / GlobeNewswire release of 26 Feb 2025 on QuickTurn Europe (via orchestrator notes). Reconciliation R-035 and B-3; registry C-5.</cite></div>

Read down the fourth column and the pattern is plain. Every list contains the same hardware. The six-module list names each gas-path component; the four-module list groups three of them into the core; the three-module list leaves out the gearbox because it carries no life-limited parts and is not part of the gas path. FTAI's own releases convert modules to engines at three per engine, which matches the gas-path count: 450 modules for 150 engines and 1,800 modules for 600 engines. <span class="cite">[FTAI release, 26 Feb 2025, via orchestrator notes; D8 §2.10; reconciliation B-3]</span> This Part uses four major modules, the three gas-path modules plus the accessory gearbox, each built from sub-modules. Whenever a later Part converts a module count into engines it names the convention it is using, because 1,200 modules is 400 engines at three per engine and 300 at four. <span class="cite">[reconciliation R-035; E.1 rule 7]</span>

### 3.3 What has to be true for a module to move

Three things must hold before a shop can take the fan module off engine A and bolt it onto engine B.

The first is mechanical and configuration compatibility. The two modules must be the same model and at compatible build standards.

<div class="defn"><b>Build standard (configuration)</b><p>The build standard is the set of service-bulletin states a module has been built to. The manufacturer issues service bulletins that change hardware over the years, and two modules at different standards may not mate, or may not be approved to run together. <span class="cite">[D1 §2.3]</span></p></div>

<div class="defn"><b>Airworthiness Directive (AD) and Service Bulletin (SB)</b><p>A Service Bulletin is a manufacturer's instruction to modify or inspect; an Airworthiness Directive is a regulator's order making a fix or inspection mandatory. Compliance records for both must travel with life-limited and hard-time parts. Part V §31 carries the full treatment. <span class="cite">[D3 §2.1; D1 §2.3]</span></p></div>

CFM's TRUEngine programme exists to certify exactly this kind of conformity, on the stated ground that "the engine's configuration, material content, maintenance history, and supportability impact overall value as it changes ownership". <span class="cite">[CFM International, TRUEngine launch release]</span>

<div class="defn"><b>TRUEngine</b><p>TRUEngine is CFM's designation for an engine whose configuration and material content conform to CFM's own definition: OEM parts and OEM-approved repairs. CFM states that the designation "is being embraced by industry's leading asset valuation providers", so appraisers can treat a non-conforming configuration as a discount (§8). A lease clause requiring TRUEngine status is an OEM-only clause by another name (Part VI §42). <span class="cite">[CFM International, TRUEngine launch release; D1 §2.3, §2.9]</span></p></div>

The second condition is serialisation and records. Each module, and each life-limited part inside it, carries a serial number and a record of the cycles it has consumed. A module can only move if the receiving engine's records can absorb it, with every life-limited part's remaining life known and documented. This is the reason records travel with the module rather than with the engine. An engine is an assembly whose parts have different histories; the history belongs to the part. Section 9 sets out the documents. The practical consequence is that a module with a gap in its records is physically present but commercially absent: it cannot be installed, so it does not count as supply. <span class="cite">[D1 §2.3, §2.9, §5]</span>

The third condition is common part numbers. The -5B and -7B share core hardware to the point that used-parts dealers advertise a single "CFM56-5B & -7B Core LLP Package". <span class="cite">[Aviation Fleet Support, undated listing]</span> That commonality is what lets a shop building -7B cores draw on -5B material and vice versa. The exact list of parts common to both variants was not retrieved. <span class="cite">[D1 U2]</span>

<div class="defn"><b>Feedstock</b><p>Feedstock is the trade's word for the aircraft and engines bought, or taken on consignment, to be torn down for parts. Later Parts extend it to the unserviceable module a customer returns in an exchange and to engine inventory held for module production, and say so when they do. Part V §33 carries the full treatment. <span class="cite">[D3 §2.2; registry C-14]</span></p></div>

### 3.4 Module exchange against full disassembly

A module exchange separates the engine at the major-module flanges, removes one module and installs a serviceable one. A full disassembly strips every module to piece parts, inspects and repairs or replaces each one, and rebuilds the engine. The difference is time and exposure. An exchange takes days to a few weeks and touches only the module exchanged. A full disassembly takes months and opens every module to inspection findings that must then be repaired. <span class="cite">[D1 §2.3]</span>

<div class="defn"><b>Module exchange</b><p>A module exchange separates the engine at the major-module flanges, removes a time-expired or damaged module and installs a serviceable one from a pool, so the aircraft returns to service in days to weeks instead of months. The incoming unserviceable module becomes the provider's feedstock. The industry prices an exchange as a fee plus the difference in life-limited-part life between the module handed over and the module received, adjusted for the condition of the other hardware. Part VII §46 and §47 carry the full treatment; GE sells the same thing under its TrueChoice Transitions offering (§9). <span class="cite">[D1 §2.3; D2 §2.1, §2.5; D5 §2.3]</span></p></div>

StandardAero, an independent engine shop, lists "engine module changes" among its quick-turn shop-visit services, beside borescope inspection, blending out small blade damage, removal and installation of accessories, and fan, top-case, bottom-case, hot-section and low-pressure-turbine repairs. <span class="cite">[StandardAero CFM56-7B brochure, Oct 2022]</span> Whether a given module change requires a run in a test cell depends on the shop manual's procedure for that module, and the research did not verify it. <span class="cite">[D1 U14]</span>

FTAI's business is built on this distinction. Its annual report describes a "Module Factory", "a dedicated commercial maintenance program designed to focus on modular and parts repair and refurbishment of CFM56-7B and CFM56-5B engines", and says the company "targets assets which require maintenance repairs that can be performed through [its] proprietary Module Factory process". <span class="cite">[FTAI 10-K FY2025]</span>

<div class="defn"><b>Module Factory</b><p>The Module Factory is FTAI's name for the CFM56-7B and -5B modular repair and refurbishment programme quoted above from its FY2025 annual report, based at its Montréal shop. Functionally it is a production-line approach that builds and holds an inventory of serviceable modules for exchange. Part VII §46 carries the full treatment. <span class="cite">[FTAI 10-K FY2025; D5 §2.2]</span></p></div>

<div class="box"><div class="h">Why the module is the unit</div><p>Four facts make the module, not the engine, the natural unit of this market. The engine is designed to split at the module flanges. Each module carries its own serial number and records, so it can be valued and traded on its own. The life-limit clocks inside the modules were deliberately set at different lengths (30,000 cycles in the fan, 20,000 in the core, 25,000 in the turbine, §4), so a fan and a core from the same engine are never at the same point in their lives. And a shop can install a serviceable module without stripping the rest of the engine. Put together, these mean that an engine at a shop visit is really three or four assets with three or four different remaining lives, and that the quickest way to return it to service is often to replace the one that has run out rather than to restore all of them. <span class="cite">[D1 §2.3, §2.4, §2.8]</span></p></div>

## 4. Life-limited parts: limits, prices, escalation, stub life

Most parts in an engine are replaced when inspection finds them worn. A small number are replaced on a clock, whatever their condition, because the consequence of their failing is a disk fragment the engine casing cannot contain. These are the life-limited parts, and much of the economics of the CFM56 aftermarket turns on them.

<div class="defn"><b>Life-limited part (LLP)</b><p>A life-limited part is a rotating or pressure-bearing part (a disk, a spool, a shaft, certain seals) whose failure the engine case cannot be designed to contain. It is certified for a fixed number of flight cycles and must be removed and scrapped at that limit regardless of its condition. On the -7B the limits are 20,000 cycles in the high-pressure compressor and turbine, 25,000 in the low-pressure turbine and 30,000 in the fan and booster. Reaching a limit forces the engine open. <span class="cite">[Aircraft Commerce Issue 34, 2004; AJW mini-pack, 2022; StandardAero mini-pack, Mar 2025]</span></p></div>

<div class="defn"><b>Disk and spool</b><p>A disk is the heavy wheel to which a row of blades attaches. A spool is several disks machined as a single piece. Together with the shafts and certain seals, these are the life-limited parts. <span class="cite">[D1 §2.4]</span></p></div>

### 4.1 The limits, module by module

CFM's stated design policy is "target lives of 30,000 EFC in the fan/booster module, 20,000 EFC in the HPC and HPT modules and 25,000 EFC in the LPT module". <span class="cite">[Aircraft Commerce Issue 34, 2004]</span> Engine-specific documents confirm those limits in service on the -7B. The documents in question are records summaries that engine traders publish for engines they are selling.

<div class="defn"><b>Mini-pack (records mini-pack)</b><p>A mini-pack is an engine records summary that lists each life-limited part with its certified limit and the cycles it has consumed. Traders publish them so that a buyer can see the engine's remaining life part by part before asking for the full records. <span class="cite">[AJW Group mini-pack, 2022; StandardAero mini-pack, Mar 2025]</span></p></div>

<div class="exh"><div class="exh-title">Exhibit 1.5 — CFM56-7B life-limited parts and certified limits, by module</div>

| Life-limited part | Module | Certified limit (EFC) | Source |
|---|---|---|---|
| Fan disk | Fan and booster | 30,000 | AJW mini-pack ESN 889979 (-7B26), 2022; StandardAero mini-pack ESN 892820, Mar 2025 |
| Booster spool | Fan and booster | 30,000 | Same |
| HPC stage 1–2 spool | Core (HPC) | 20,000 | Same |
| HPC stage 3 disk | Core (HPC) | 20,000 | Same |
| HPC stage 4–9 spool | Core (HPC) | 20,000 | Same |
| HPT disk | Core (HPT) | 20,000 | Same |
| LPT stage 1 disk | LPT | 25,000 | Same |
| Shafts, remaining LPT disks, seals | Various | Listed in the packs; individual limits not in the returned text | Same |
| CFM56-5B, whole engine | All | "18 different sets of LLPs with life limits varying between 20,000 and 30,000 flight cycles"; per-part table not reached (D1 U3) | Leeham News, 8 Mar 2024 |

<cite>Source: AJW Group, ESN 889979 CFM56-7B26 mini-pack, 2022; StandardAero, ESN 892820 mini-pack, Mar 2025; Leeham News, Bjorn's Corner Part 49, 8 Mar 2024; CFM design policy per Aircraft Commerce Issue 34, 2004. Compiled in D1 §2.4.</cite></div>

Why does a limit force the engine open? Because the life-limited parts are the innermost parts. The high-pressure turbine disk sits behind the combustor with the turbine blades mounted on it; the compressor spools are buried in the core. To change the turbine disk the core must come out of the engine, the turbine module must be split from the compressor and combustor, the blades must be pulled, and the disk replaced; the rotor is then rebalanced and rebuilt. There is no procedure for doing any of this on the wing. <span class="cite">[D1 §2.4]</span> So when the lowest remaining life among all installed life-limited parts reaches zero, the engine comes off and goes to a shop whether or not it is still performing well. In practice the operator removes it earlier, at a planned shop visit, and replaces the parts that would otherwise run out before the next planned visit.

<div class="worked"><div class="h">Worked example 1.1 — The life-limit clock sets the removal date</div>
<p>Inputs: a CFM56-7B26 whose high-pressure turbine disk has consumed 18,500 cycles against a 20,000-cycle limit (limit sourced: mini-packs; cycles consumed assumed for illustration). The aircraft flies 1,500 cycles a year (sourced as the upper end of Aircraft Value News's 1,000–1,500 cycles a year for a mature narrowbody). The engine's temperature margin (§5) would otherwise allow another 5,000 cycles (assumed).</p>
<div class="eqblock">cycles remaining = 20,000 − 18,500 = 1,500
time to limit = 1,500 ÷ 1,500 per year = about one year</div>
<p>So the disk sets the removal date at about one year, and the 5,000 cycles of temperature margin the engine still has are worth nothing to this owner: the engine must come off when the disk runs out. Limits of the example: the cycles consumed and the margin are assumed; the point is the mechanism, which is that the shorter of the two clocks always governs. <span class="cite">[D1 §2.4, example A]</span></p></div>

### 4.2 Stub life, and why it creates a market for used parts

An engine rarely arrives at a shop with all of its life-limited parts at exactly zero. It arrives with some parts near their limits and others with thousands of cycles left. The shortest of those remaining lives has a name.

<div class="defn"><b>Stub life</b><p>Stub life is "the shortest life remaining of all LLPs installed in an engine". In its pejorative sense it is the "several thousand EFCs of remaining LLP life that will not be used and the parts will be scrapped" when life-limited parts are replaced early so that they do not cut short the next run. Scrapping unused cycles raises the amortised cost per cycle of the part. <span class="cite">[Aircraft Commerce Issue 34, 2004]</span></p></div>

The mechanism, in Aircraft Commerce's words: "shop visit input may occur at a time when LLPs still have a few thousand EFCs remaining, and LLP replacement at this stage will be necessary if remaining lives are not to limit the subsequent removal interval"; and "if scrapped with excessive stub life the amortised cost per EFC and EFH is increased". <span class="cite">[Aircraft Commerce Issue 34, 2004]</span> The remaining cycles on an engine's life-limited parts "influence mid-life lease pricing, redelivery conditions, and asset value protection for lessors". <span class="cite">[AviTrader, 23 Apr 2026]</span>

<div class="defn"><b>Mid-life narrowbody</b><p>A mid-life narrowbody is a 737NG or A320ceo roughly 10 to 18 years old, or more loosely one in the middle of a 25-to-30-year economic life, when an increasing share of the aircraft's value sits in its engines and those engines are approaching or past a shop visit. Part II §15 carries the full treatment. <span class="cite">[D6 §2.4; D7 §2.4; registry C-13]</span></p></div>

<div class="defn"><b>Cycles remaining (CR) and cycles since new (CSN)</b><p>Cycles remaining is a life-limited part's certified limit minus the cycles it has consumed; used-part packages are advertised on it ("6235 CR"). Cycles since new is the number of cycles an engine or part has flown since manufacture. Part IV §30 uses the second term in a table. <span class="cite">[D1 §2.4; D2 §4.6]</span></p></div>

<div class="defn"><b>Used LLPs (part-life LLPs; LLP package)</b><p>Used LLPs are life-limited parts removed from another engine with full records and remaining life, sold as packages with a stated number of cycles remaining and chosen to match the buyer's planned next run. Dealers advertise them as such: "CFM56-7B27E/B1F Engine LLP Package ... 7,445 Cycles Remaining" and "CFM56-5B & -7B Core LLP Package 6235 CR". Prices of these packages were not shown in the listings the research reached. <span class="cite">[Salvex listing, undated; Aviation Fleet Support listing, undated; D1 U4]</span></p></div>

<div class="worked"><div class="h">Worked example 1.2 — Stub life and amortised cost per cycle</div>
<p>Inputs: an engine arrives for a performance restoration (§6) at 12,000 cycles since new (assumed). Its core life-limited parts have a 20,000-cycle limit (sourced: mini-packs), so 8,000 cycles remain. The operator plans a next run of 12,000 cycles (assumed; inside Leeham's 10,000–15,000-cycle mature interval, §6). A part lists at price P.</p>
<p>Option one, keep the parts. The engine comes off again after 8,000 cycles, forced by the life limit, with its restored performance only two-thirds used.</p>
<p>Option two, replace them now with new parts at list. Then 8,000 of each part's 20,000 cycles (40%) are scrapped unused.</p>
<div class="eqblock">cost per cycle, full life used = P ÷ 20,000
cost per cycle, scrapped at 12,000 = P ÷ 12,000
increase = (20,000 ÷ 12,000) − 1 = 67%</div>
<p>Option three, which is the option the used-parts market exists to supply: install used life-limited parts with 12,000 to 15,000 cycles remaining, matched to the planned run, from a package of the kind the dealers advertise above. The arithmetic for how such a part is priced is in §4.4 and Part V §34. Limits of the example: the cycles consumed and the planned run are assumed; the limit and the listings are sourced; the package price is unknown (D1 U4). <span class="cite">[D1 §2.4, example B]</span></p></div>

The stub problem also explains why the limits are what they are. Engines "whose inherent design includes LLPs with high stub-lives will tend to experience lower rates of engine removals compared to engines with lower LLP stub-lives". <span class="cite">[Aircraft Commerce Issue 34, 2004]</span> CFM's choice of 20,000 cycles for the core and 30,000 for the fan means the fan's parts span a core overhaul cycle and a half. At the first core replacement, near 20,000 cycles, the fan disk still has about 10,000 cycles left. That mismatch is one of the physical reasons a fan module and a core module from the same engine have different values at the same moment, which §8 takes up. <span class="cite">[D1 §2.4]</span>

### 4.3 What a full set costs, year by year

New life-limited parts come from one source, at a published price that is revised upward on a schedule.

<div class="defn"><b>Catalogue list price (CLP), or list price</b><p>The catalogue list price is the manufacturer's published price for every new spare part, repriced at least annually. A shop passes it through at list plus a handling margin, and used and alternative parts are priced as discounts to it. Part IV §28 carries the full treatment. <span class="cite">[D2 §2.2–2.3; D3 §2.1]</span></p></div>

<div class="defn"><b>Escalation (catalogue escalation; LLP escalation)</b><p>Escalation is the manufacturer's annual increase in catalogue list prices. Trade press put new spare-parts price increases at around 10% a year in 2022–23 (a double-digit increase on 1 November 2022 and a high-single-digit increase in August 2023), and Safran's chief executive described a rule of pricing "above inflation by 3 to 4 points". On the figures in Exhibit 1.6, a full -7B life-limited-part set compounded at about 7% a year from 2008 to 2025. Because 60–70% of a shop visit is OEM-priced material, escalation flows into every visit whoever performs it. Part IV §28 carries the full treatment. <span class="cite">[Aviation Week, late 2023; Air Cargo Week, 2025/26; D1 example C]</span></p></div>

<div class="exh"><div class="exh-title">Exhibit 1.6 — Full life-limited-part set for a CFM56-7B at list price, by year, with sources and caveats</div>

| Year | Figure | Scope as the source gives it | Source and level | Caveat |
|---|---|---|---|---|
| 2008 | $1.775M | Full -7B set, "shipset" (the source's word for one engine's complete set) | Aircraft Commerce Issue 58 (trade press) | None |
| 2013 | $1.7M | "A full set of LLPs for a CFM56-7B has a list price of $1.7 million" | Aircraft Commerce Issue 87 (trade press) | Below the same publisher's 2008 figure; D3 T4 says the excerpt may cover a subset; not used for arithmetic |
| 2017 | "north of $3m" | Whole-engine CFM56 LLP stack; HPT exchange "easily $0.5m"; fan/booster "$0.5m–$0.7m" | Leeham News, 3 Mar 2017 (trade press) | Rounded; variant not stated |
| Oct/Nov 2018 | $3.4M | Full -7B set | Aircraft Commerce Issue 120 (trade press) | None |
| Nov 2019 | "$4m for CFM56-7" | Headline; article paywalled | Aircraft Value News (trade press) | Implies +18% in one year against the 2018 figure (D1 T2); Part IV uses this figure in its option arithmetic |
| Aug 2023 | -7B parts +20–30% in 2023 | Parts generally, after CFM's catalogue revision; not LLPs specifically | Magnetic Group via Aviation Week, 2024 (trade press) | Not a set price |
| Jun 2025 | $5.7M | "LLPC $m: 5.700" (LLPC is the table's label for LLP cost) in an engine-status table | MyAirTrade (market-data site) | Methodology, rating and exact scope not visible (D1 T2); this Part uses it as its current case |
| Apr 2023 | $9,878,733 full life; $4,939,366 half life | CFM56-5B engine LLPs for an A320, 2023 dollars | Mark Calver, Cargo Facts (conference presentation) | Per engine or per aircraft (two engines) unstated (D3 U3) |

<cite>Source: Aircraft Commerce Issues 58 (2008), 87 (2013) and 120 (Oct/Nov 2018); Leeham News, Bjorn's Corner, 3 Mar 2017; Aircraft Value News, Nov 2019; Aviation Week, "Magnetic expects CFM56 market challenges", 2024; MyAirTrade engine-status resource, June 2025; Mark Calver, Cargo Facts Session 3, Apr 2023. Reconciliation R-016; E.2 "LLP full set".</cite></div>

The sources disagree, and the primer carries the disagreement rather than resolving it. <span class="cite">[reconciliation R-016]</span> The 2013 figure of $1.7M sits below the 2008 figure from the same publisher, which cannot both be full-set prices at list unless the scope differed; it is quoted here only with that caveat. The current figure is either about $4M (Aircraft Value News, November 2019, as used by Part IV) or $5.7M (MyAirTrade, June 2025, as used by this Part), and the two are never mixed in one calculation. Where this Part computes with $5.7M it shows $4M as the alternative case and says what changes. <span class="cite">[E.1 rule 5]</span> The Calver figure for the -5B is carried only with the statement that the presentation does not say whether it covers one engine or an aircraft's two.

<div class="worked"><div class="h">Worked example 1.3 — Deriving the escalation rate from the price series</div>
<p>Inputs: $1.775M in 2008 (sourced: Aircraft Commerce Issue 58); $3.4M in late 2018 (sourced: Issue 120); $5.7M in mid-2025 (sourced: MyAirTrade, scope not visible). Periods taken as ten years, seven years and seventeen years (assumed, from the publication dates).</p>
<div class="eqblock">2008 to 2018: 3.4 ÷ 1.775 = 1.916; 1.916^(1/10) − 1 = 6.7% a year
2018 to 2025: 5.7 ÷ 3.4 = 1.676; 1.676^(1/7) − 1 = 7.7% a year
2008 to 2025: 5.7 ÷ 1.775 = 3.21; 3.21^(1/17) − 1 = 7.1% a year</div>
<p>The 2019 point of $4.0M would imply an 18% rise in one year, which is out of line with the trend and may reflect a rounded headline or a different scope (D1 T2). Ishka reports that one recent escalation step on -5B/-7B life-limited parts was about 12%, without showing the year, and that "engine OEMs calculate LLP escalation based on a formula which factors in labour costs, the price of raw materials and energy costs". Because a life-limited-part set is 40–60% of the parts bill in a heavy shop visit (Safe Fly Aviation, consultancy blog, 2026), a 7% annual escalation on the set alone lifts the cost of a heavy visit by roughly 3–4% a year before any labour or repair inflation; that last figure is derived, not sourced. Limits of the example: the dates are publication dates, the 2025 scope is not visible, and the years of each catalogue step between 2019 and 2025 were not retrieved (D1 U10; D2 U1). <span class="cite">[D1 example C; Ishka, undated; Safe Fly Aviation, 2026]</span></p></div>

Two readings of escalation sit side by side in the research. One is life-limited-part specific: about 7% a year compounded on the set prices above, a 12% single step reported by Ishka without a year, and a 20–30% rise in -7B parts prices generally after CFM's August 2023 catalogue revision. <span class="cite">[D1 example C; Ishka, undated; Magnetic Group via Aviation Week, 2024]</span> The other covers all spares: around 10% a year, a double-digit increase on 1 November 2022, a high-single-digit increase in August 2023, and Safran's stated rule of inflation plus three to four points "at least for some years". <span class="cite">[Aviation Week, late 2023]</span> They cover different parts, years and bases, and the primer reports both. <span class="cite">[reconciliation R-018]</span>

### 4.4 What the escalation does to the cost of a cycle

Dividing a set price by the cycles it buys gives the life-limited-part cost of each take-off and landing. The research produced two such figures from two set prices, and both are shown.

<div class="eqblock">at $5.7M: 5,700,000 ÷ 20,000 = $285 per cycle (D1)
at $4.0M: 4,000,000 ÷ 20,000 = $200 per cycle (D2)
at $5.7M, scrapped after 12,000 cycles: 5,700,000 ÷ 12,000 = $475 per cycle
at $4.0M, scrapped after 12,000 cycles: 4,000,000 ÷ 12,000 = $333 per cycle</div>

The first two lines inherit the disagreement over the set price; the second two show the stub-life penalty of worked example 1.2 in dollars. <span class="cite">[D1 example D; D2 §2.5; reconciliation R-017]</span> At 1,500 cycles a year the $200-per-cycle figure is $300,000 per engine per year, which is D2's statement of it. <span class="cite">[D2 §2.5]</span>

This arithmetic is what creates a market for used life-limited parts and for engine cores whose remaining lives match a buyer's planned run. A part with 60% of its life left is worth roughly 60% of its list price, less a discount for being used; that is how an engine shop prices a used part, and how an appraiser adjusts an engine's value for its life-limited parts (§8). <span class="cite">[D3 §2.4]</span> Used material in general trades at 60–80% of a new part's price on average, or at 70–75% of catalogue list price when a specialist trader sells repaired engine material to an airline; Part V §34 sets out those figures and their tension. <span class="cite">[Aviation Week, undated; Aircraft Commerce Issue 120; reconciliation R-022]</span> No alternative manufacturer makes a life-limited part for the CFM56: the research found approvals for turbine blades and vanes but none for a disk or spool, so new life-limited parts remain a single-source purchase at the escalating list price (Part VI §38). <span class="cite">[D4 U7; D1 §5]</span>

## 5. Exhaust-gas temperature margin and time on wing

The life-limit clock of §4 is one of two clocks that take an engine off the wing. The other is a thermometer. An engine that has worn cannot make its rated thrust without running hotter, and there is a temperature it may not exceed. The gap between the two is the margin, and the margin is spent a little on every flight.

<div class="defn"><b>Exhaust-gas temperature (EGT)</b><p>Exhaust-gas temperature is the temperature of the gas leaving the turbine, measured by probes behind the low-pressure turbine. Every engine has a certified EGT red line that it may not exceed. <span class="cite">[D1 §2.5]</span></p></div>

<div class="defn"><b>EGT margin (EGTM)</b><p>EGT margin is "the difference between the maximum temperature limit on the engine and the actual temperature read at the time of take-off", measured at full take-off thrust on a hot day so that engines can be compared. It shrinks as the engine wears, fastest in the first 1,000 to 2,000 cycles after a shop visit. At zero margin the engine can no longer make rated thrust within its limit and must come off the wing. A performance restoration (§6) recovers most of it. <span class="cite">[Jurnal Teknik Mesin, June 2023; Aircraft Commerce Issue 27, 2003]</span></p></div>

<div class="defn"><b>Hot section</b><p>The hot section is the combustor, the high-pressure turbine blades and vanes (the vanes are also called nozzles; the stage-1 vane is the HPT nozzle), and the adjacent parts that combustion gas touches directly. It is where margin is lost and where most of it is recovered. <span class="cite">[D1 §2.5; D4 §8]</span></p></div>

### 5.1 Why margin erodes and how it is restored

As the engine wears, its compressor and turbine move less air for each unit of fuel. The control system burns more fuel to make the same thrust, and the gas runs hotter, so the margin shrinks. The wear is concentrated at the blade tips and the seals they run against. "Rates of deterioration [are] highest in the first 1,000 EFC of operation as blade tips and seals are worn and clearances increase. This leads to leakage around blade tips and causes EGT margin to erode. EGT margin deterioration rates slow down after the first 1,000–2,000 EFC on-wing." <span class="cite">[Aircraft Commerce Issue 27, 2003]</span> A measured case on an older CFM56-3C1 found 26.2°C of margin lost since the last repair, of which the gap between the rotor blade tips and the casing accounted for 58.1%. <span class="cite">[Jurnal Teknik Mesin, June 2023]</span> Sand and salt in the operating environment erode blades faster, and a higher thrust rating starts with less margin to begin with. <span class="cite">[D1 §2.5]</span>

Restoration reverses the same wear. "Shop visit maintenance will restore hardware and clearances between blade tips and engine casings, and most of the original EGT margin will therefore be restored." <span class="cite">[Aircraft Commerce Issue 27, 2003]</span> In practice that means new or repaired high-pressure turbine blades and vanes, new honeycomb seals (the soft rub-in rings that blade tips run against), new shroud segments (the ring pieces that surround the turbine blade tips) and restored compressor blade tips. The high-pressure turbine is where most of the margin comes back, which is why its blades and vanes are the second-largest cost line in a shop visit at 15–25% of parts cost, and why an approved alternative to the manufacturer's turbine blade matters as much as it does. <span class="cite">[Safe Fly Aviation, 2026; D1 §2.5]</span>

<div class="defn"><b>Parts Manufacturer Approval (PMA)</b><p>A Parts Manufacturer Approval is the US Federal Aviation Administration's (FAA) combined design-and-production approval that lets a company other than the type-certificate holder legally make and sell a replacement part for a certificated engine. Historically PMA covered consumables and simple parts; an approved alternative to the CFM56 high-pressure turbine blade, announced on 30 October 2025, is treated in the trade as a milestone because that blade sits where most of a shop visit's margin and cost are. No PMA exists for any CFM56 life-limited part. Part VI §37 carries the full treatment. <span class="cite">[D4 §2.1–2.3; Chromalloy release, 30 Oct 2025]</span></p></div>

The research did not retrieve the as-new margin for each -7B and -5B thrust rating, or the typical loss per thousand cycles, so this Part quotes no figures in degrees beyond the single measured case above. <span class="cite">[D1 U5]</span>

### 5.2 Which clock sets the removal

Time on wing is the shorter of the two clocks.

<div class="defn"><b>Time on wing</b><p>Time on wing is the number of cycles or hours between an engine's installation on an aircraft and its removal. It is the smaller of the life-limit clock (§4) and the EGT-margin clock (§5), or, less often, a hard inspection falling due. Shortfalls in time on wing for the new-generation engines are Part III's subject (§10 gives the figures). <span class="cite">[D1 §2.5; D9 §2.7]</span></p></div>

The sources disagree about which clock usually governs, and the disagreement is partly about era and variant. Aircraft Commerce's maintenance analyses of 2003 and 2008 state that "EGT margin erosion is generally the most influential factor in maintenance removal intervals for short-haul engines, while the effect of hardware deterioration is greater on engines used on medium-haul operations". <span class="cite">[Aircraft Commerce Issue 27, 2003, and Issue 58, 2008]</span> The same publisher's later analysis of the -5B finds that for the latest variants at most ratings "the exhaust gas temperature (EGT) margin is high enough ... for it to remain on-wing up to the life-limited part (LLP) engine flight cycle (EFC) life limits", so that "it is possible for certain engines to only come due their third planned removal and shop visit after more than 25 years of operation". <span class="cite">[Aircraft Commerce Issue 50]</span> The shops report the same thing: "shop visits for the latest CFM56-5B/7B variants tended to be driven by life-limited parts (LLPs) reaching their ceiling rather than a need to restore engine performance", and "especially first-run engines have flown almost to LLP limit". <span class="cite">[FlightGlobal, undated]</span> The primer carries both statements; they describe different variants, ratings and eras, and the reconciliation records them as an unresolved tension. <span class="cite">[reconciliation R-011, B-7]</span> Part III's translation table reaches the same place from the fleet side: a fleet kept flying past its planned retirement date is a fleet that hits its life limits next.

<div class="worked"><div class="h">Worked example 1.4 — Turning cycles on wing into years on wing</div>
<p>Inputs: a mature CFM56's performance-restoration interval of 10,000 to 15,000 cycles and a life-limit-driven overhaul at 20,000 to 25,000 cycles (sourced: Leeham News, 8 Mar 2024); utilisation of 1,000 to 1,500 cycles a year for a mature short-haul narrowbody (sourced: Aircraft Value News); a core life limit of 20,000 cycles (sourced: mini-packs).</p>
<div class="eqblock">restoration interval in years = 10,000 ÷ 1,500 to 15,000 ÷ 1,000 = 6.7 to 15 years
first core life limit in years = 20,000 ÷ 1,500 to 20,000 ÷ 1,000 = 13.3 to 20 years</div>
<p>So a mature engine flying 1,200 cycles a year reaches a restoration roughly every 8 to 12 years and its first core life limit at about 17 years. Two other readings exist. Aviation Week's rule of thumb is that a CFM56 needs a shop visit "roughly every eight years", which makes 24 years a de facto retirement age. And 2,300 shop visits a year on a base of about 24,000 engines is 9.6% of the base, which, if every engine were on a regular cycle, would imply an average interval of about ten years; the dossier that made that calculation records that the base figure may include spare and stored engines and does not resolve the gap. A third dossier assumed one restoration every six years and labelled it an assumption to be replaced. Limits of the example: utilisation varies by operator; first-run intervals run longer than mature ones (§6); the three readings are reported, not reconciled. <span class="cite">[Leeham News, 8 Mar 2024; Aircraft Value News, undated; Aviation Week via D3; D9 §2.2; D7 §5.2; reconciliation R-008]</span></p></div>

## 6. Shop visits: types, workscopes, intervals, turnaround

When either clock runs out, or something breaks, the engine comes off the aircraft and goes to a shop. Everything that happens there has a name, and the names are not interchangeable.

<div class="defn"><b>Shop visit (SV)</b><p>A shop visit is any removal of the engine from the aircraft for work in an engine shop, from a visit to fix one finding to a complete rebuild. Part VIII uses one dossier's phrase "teardown and restoration" for the same event; this primer reserves "teardown" for dismantling an engine to sell its parts (Part V §32). <span class="cite">[D1 §2.6; D2 §2.1; registry C-8]</span></p></div>

<div class="defn"><b>Engine shop</b><p>An engine shop is a facility holding a regulatory repair-station approval (§9) and, in practice, the manufacturer's technical data and tooling. It disassembles engines on stands, cleans and inspects every piece, replaces or repairs what is out of limits, reassembles the engine and runs it in a test cell before release. Part IV §25 carries the full treatment. <span class="cite">[D2 §2.1]</span></p></div>

<div class="defn"><b>MRO and independent MRO</b><p>MRO is the industry's generic term for maintenance, repair and overhaul work and for the companies that do it. An independent MRO is an engine shop not owned by the engine's manufacturer: a stand-alone company such as StandardAero, an airline's maintenance subsidiary that sells to third parties, or an engine maker's shop that is independent on the CFM56, such as MTU (Germany's MTU Aero Engines) through its MTU Maintenance arm (§10). Part IV §25 carries the full treatment. <span class="cite">[D2 §3.2]</span></p></div>

<div class="defn"><b>Workscope</b><p>The workscope is the specification of what a shop visit will do: which modules are opened, how deep the work goes in each, and which parts are replaced new, repaired, or swapped for used material. It runs from a light quick-turn to a full overhaul. <span class="cite">[D1 §2.6; D2 §2.1]</span></p></div>

### 6.1 The types, from lightest to heaviest

<div class="defn"><b>Hospital visit (quick-turn visit)</b><p>A hospital or quick-turn visit fixes one thing and returns the engine: a borescope finding, a damaged fan blade, a module exchange, an accessory change. Trade press reports that such visits "are being used as an alternative to avoid substantial financial and time investments into full-performance shop visits", at about 45 days' turnaround. The lower-case term is a workscope; the capitalised "QuickTurn" is the brand of FTAI's Miami and Rome businesses (Part VII §50). Part VII §46 carries the module exchange as the quick-turn. <span class="cite">[Aviation Week, 2024; Aviation Business News, 2025; registry C-20]</span></p></div>

<div class="defn"><b>Borescope and boroblend</b><p>A borescope inspection looks inside the engine with a camera passed through ports in the casing, on wing or in a shop. A boroblend repair grinds out small blade damage found that way, through the same ports, without disassembly. <span class="cite">[D1 §2.3, §2.6]</span></p></div>

<div class="defn"><b>Line-replaceable unit (LRU) and quick-engine-change kit (QEC)</b><p>A line-replaceable unit is an accessory that can be changed on the flight line without opening the engine. The quick-engine-change kit is the set of mounts, plumbing and accessories that dresses a bare engine for installation on a particular aircraft. <span class="cite">[D1 §2.3, §8]</span></p></div>

<div class="defn"><b>Top-case repair</b><p>In a top-case repair the high-pressure compressor case is split horizontally and the upper half lifted off, giving access to the compressor blades and vanes for repair or replacement without removing the rotor. StandardAero lists top-case and bottom-case repairs as separate services. <span class="cite">[D1 §2.6; StandardAero brochure, Oct 2022]</span></p></div>

<div class="defn"><b>Performance restoration (PR) and core PR</b><p>A performance restoration is a shop visit in which the core is opened and the high-pressure compressor, combustor and high-pressure turbine are restored to recover EGT margin; the fan and low-pressure turbine may be inspected but are not fully disassembled. A core PR is this scope confined to the core module. Replacing life-limited parts is a separate decision, which a life-limit-driven removal combines with the restoration; one dossier describes a PR as "typically with LLP replacement", and this primer keeps the two decisions distinct. <span class="cite">[D1 §2.6; D2 §2.1; registry C-7]</span></p></div>

<div class="defn"><b>Overhaul (heavy or full shop visit; "zero-time")</b><p>An overhaul disassembles every module to piece parts, inspects, repairs and rebuilds, and replaces the life-limited parts that would fall due within the next run. It is done when the life limits are due, at roughly 20,000 to 25,000 cycles. "Zero-time" is one source's term for an overhaul with a complete new set of life-limited parts. <span class="cite">[D1 §2.6; D2 §2.1; Leeham News, 8 Mar 2024]</span></p></div>

<div class="exh"><div class="exh-title">Exhibit 1.7 — Shop-visit types: what is opened, what is done, and typical turnaround</div>

| Type | What is opened | What is done | Life-limited parts | Turnaround | Source |
|---|---|---|---|---|---|
| Hospital / quick-turn | Limited; one module or an access port | One finding fixed: borescope finding, fan blade, module exchange, accessory | None | ~45 days (trade press, 2025) | D1 §2.6; Aviation Business News, 2025; StandardAero, 2022 |
| Top-case repair | Upper half of the HPC case | HPC blades and vanes repaired or replaced, rotor in place | None | Not retrieved | D1 §2.6; StandardAero, 2022 |
| Performance restoration | Core (HPC, combustor, HPT); fan and LPT inspected | Hot-section rebuild to recover EGT margin | Separate decision; combined when a limit is near | 75–90 days (Safe Fly, consultancy blog, 2026) | D1 §2.6; Safe Fly, 2026 |
| Heavy visit with LLPs | Core plus whichever modules hold parts at or near limit | PR plus replacement of the parts at or near limit | Those at or near limit | 120–150 days (Safe Fly, 2026) | D2 §2.1; Safe Fly, 2026 |
| Full overhaul ("zero-time") | Every module, to piece parts | All modules to overhaul standard | Full new set | 90–120 days for a full overhaul (trade press, 2025); ~60 pre-pandemic | D1 §2.6; D2 §2.1; Aviation Business News, 2025 |

<cite>Source: D1 §2.6 and D2 §2.1; StandardAero, CFM56-7B engine services brochure, Oct 2022; Aviation Business News, "Inside the engine MRO supply chain", 2025; Safe Fly Aviation, "Engine Shop Visit Costs Worldwide 2026" and "CFM56-7B engine availability report 2026" (consultancy blog). The cost of each type is in Exhibit 1.9.</cite></div>

### 6.2 Intervals: first run and mature runs

<div class="defn"><b>First run and mature run</b><p>The first run is the interval from new to the first shop visit. Mature runs are the later intervals, which are shorter because repaired hardware does not match new hardware and because operators plan them around the life-limit clock. On the latest -5B and -7B variants the first run reaches the life limit before the margin runs out. <span class="cite">[D1 §2.6; FlightGlobal, undated]</span></p></div>

Leeham's description of the cadence is the cleanest: "a mature engine like the CFM56 has a performance shop visit at half the LLP flight cycle limit, and then a full engine overhaul is done when the LLPs are due for replacement". <span class="cite">[Leeham News, 8 Mar 2024]</span> Intervals by thrust rating and by region were not retrieved. <span class="cite">[D1 U6]</span>

### 6.3 Turnaround, and the wait before it

<div class="defn"><b>Turnaround time (TAT)</b><p>Turnaround time is the calendar time from an engine's induction into a shop to its release. For a full CFM56 overhaul it was about 60 days before the pandemic and 90 to 120 days in 2025; light work takes about 45 days. Every extra day needs a spare engine or grounds an aircraft, which is the economic hook for a module exchange. Part IV §27 carries the full treatment, including the wait for an induction slot, which is additional to the turnaround. <span class="cite">[Aviation Business News, 2025; D2 §2.1]</span></p></div>

<div class="exh"><div class="exh-title">Exhibit 1.8 — Intervals and turnaround: the figures and their sources</div>

| Metric | Value | Source and level | Date |
|---|---|---|---|
| Mature CFM56, performance-restoration interval | 10,000–15,000 cycles | Leeham News (trade press) | 8 Mar 2024 |
| Mature CFM56, overhaul with LLP replacement | 20,000–25,000 cycles | Leeham News | 8 Mar 2024 |
| First-run -5B/-7B, latest variants | "almost to LLP limit" | FlightGlobal (trade press) | Undated |
| -5B third planned removal | Possible after more than 25 years | Aircraft Commerce Issue 50 (trade press) | Undated |
| Rule of thumb | A shop visit "roughly every eight years"; 24 years a de facto retirement age | Aviation Week (trade press), via D3 | Undated |
| Implied average interval | ~10 years (2,300 visits a year on ~24,000 engines, 9.6%) | D9 derived; base may include spares and stored engines | 2026 |
| Reserve-model assumption | One restoration every six years, labelled an assumption | D7 §5.2 | 2026 |
| Full overhaul TAT, pre-pandemic | ~60 days | Aviation Business News (trade press) | 2025 |
| Full overhaul TAT, current | 90–120 days | Aviation Business News | 2025 |
| Light work TAT | ~45 days | Aviation Business News | 2025 |
| CFM56 TAT in GE shops | "sustaining ~90 days" | GE Aerospace, Bernstein conference deck (OEM) | 27 May 2026 |
| TAT for LEAP, CFM56 and GE90 (a widebody engine) | Improved by more than 10% year on year in 4Q 2025 | GE 10-K FY2025 (OEM filing) | Feb 2026 |
| PR visit TAT | 75–90 days | Safe Fly Aviation (consultancy blog) | 2026 |
| Heavy visit with LLPs TAT | 120–150 days | Safe Fly Aviation | 2026 |
| Wait for an induction slot | Up by two to three months, up to six | Bain (consultancy) | 2024 |

<cite>Source: Leeham News, 8 Mar 2024; FlightGlobal, undated; Aircraft Commerce Issue 50; Aviation Week via D3 §2.6; D9 §2.2; D7 §5.2; Aviation Business News, 2025; GE Aerospace, 27 May 2026; GE 10-K FY2025; Safe Fly Aviation, 2026; Bain, 2024. Reconciliation R-008 and R-019.</cite></div>

The turnaround figures come from different shops and workscopes and the primer records all of them without choosing. <span class="cite">[reconciliation R-019]</span> The 2025 trade press attributes the lengthening since the pandemic to "long turnaround times for material repairs ... primarily due to parts scarcity issues in the MRO supply chain". <span class="cite">[Aviation Business News, 2025]</span> Bain adds that the wait for a slot, before the turnaround even begins, had grown by two to three months and in some cases six. <span class="cite">[Bain, 2024]</span>

### 6.4 What the downtime costs: spare engines

While an engine is in a shop, the aircraft needs another engine or it does not fly. Airlines hold or lease spares for this.

<div class="defn"><b>Spare engine and spare ratio</b><p>A spare engine is one held or leased to replace an installed engine while it is in the shop. The spare ratio is spares as a percentage of installed engines: airlines "used to have about 15% of spare engines of their installed engines, but this figure is now down to 10% and is expected to further decrease to about 7–8% for newer engine types" (MTU). Longer turnarounds tie up more spares. Part II §14 carries the full treatment. <span class="cite">[MTU AEROREPORT, undated; D6 §2.3]</span></p></div>

<div class="defn"><b>Engine lease, short-term and long-term</b><p>A short-term engine lease runs from a few months to about three years and covers a shop visit or an aircraft grounded for want of an engine. A long-term engine lease runs for years and provides a permanent spare. Part II §14 carries the full treatment. <span class="cite">[D6 §2.1, §2.3]</span></p></div>

<div class="worked"><div class="h">Worked example 1.5 — The rent paid while an engine is away</div>
<p>Inputs: turnaround of 90 days (sourced: GE Aerospace, May 2026, "sustaining ~90 days") or 120 days (sourced: trade press upper figure, 2025), taken as three or four months (assumed rounding). A CFM56-7B spare engine rent of about $100,000 a month in 2024 (sourced: IBA, an appraiser, April 2024, up from about $75,000 in 2019) or $42,000 to $48,000 a month in 2026 (sourced: Safe Fly Aviation, consultancy blog; the figure sits beside green-time values and may describe a green-time engine, which the source does not say). A slot wait of two to three months (sourced: Bain, 2024).</p>
<div class="eqblock">at $100,000 a month: 3 months = $300,000; 4 months = $400,000
at $42,000–48,000 a month: 3 months = $126,000–144,000; 4 months = $168,000–192,000
slot wait of 2–3 months adds: $200,000–300,000 (IBA rate) or $84,000–144,000 (Safe Fly rate)</div>
<p>So the rent for the downtime of one restoration is somewhere between about $126,000 and $700,000 depending on which rent, which turnaround and whether a slot wait is included. The two rents are not averaged: they may price different engines (a full-life spare against a green-time engine) and come from different source levels, and Part II §14 carries them as a pair. A quick-turn of about 45 days, which is what a module exchange from inventory aims to achieve, would cut the three-to-four-month figures by roughly half to two-thirds at either rent. Limits of the example: the turnaround and rent inputs are each contested; an owned spare carries a capital cost rather than a rent; and the aircraft's own lost flying is not counted. <span class="cite">[GE Aerospace, 27 May 2026; Aviation Business News, 2025; IBA, Apr 2024; Safe Fly Aviation, 2026; Bain, 2024; reconciliation R-019, R-028]</span></p></div>

<div class="defn"><b>Test cell (test-cell run)</b><p>A test cell is an instrumented enclosure in which a rebuilt engine is run at power to confirm its thrust, EGT margin and vibration before release. Test-cell hours are a physical capacity limit for a shop: FTAI's releases quote capacity in engine tests a year alongside modules (Part VII §49). <span class="cite">[D1 §2.7; D2 §2.1]</span></p></div>

## 7. The cost of a shop visit: the build and a worked example

A shop visit's bill has five lines, and the mix among them decides most of what later Parts discuss.

<div class="defn"><b>Cost build (shop visit)</b><p>The cost of a shop visit is the sum of labour (hours times the shop's rate) to disassemble, inspect, assemble and test; new OEM parts that are scrapped and replaced (blades, vanes, seals, bearings); repairs, meaning work on parts that can be restored rather than replaced, done in-house or by specialist vendors under the manufacturer's manual or under separately approved repair schemes (Part VI §40); life-limited-part replacement, new or used; and the test-cell run; plus freight, consumables and the shop's margin. Material is 60–70% of the total. <span class="cite">[D1 §2.7; Air Cargo Week, 2025/26]</span></p></div>

### 7.1 The ranges, and why they disagree

Every cost figure the research reached is from trade press or a consultancy blog. No manufacturer or shop price list was read; one shop's fixed-price catalogue was located and not read. <span class="cite">[D1 U7; reconciliation R-013]</span> Safe Fly Aviation, a consultancy blog, publishes two sets of ranges on different pages, and the research carries both.

<div class="exh"><div class="exh-title">Exhibit 1.9 — CFM56 shop-visit cost ranges, by labelled scope, with both consultancy sets and the other figures reached</div>

| Scope as labelled by the source | Range | Source and level | Date | Note |
|---|---|---|---|---|
| Light / quick-turn: limited opening, targeted repair, no LLPs | $650k–900k | Safe Fly Aviation, "Engine Shop Visit Costs Worldwide 2026" (consultancy blog) | 2026 | Carried by D2 only |
| Performance restoration: hot-section rebuild; "may replace some LLPs if convenient" | $1.2–1.6M | Safe Fly Aviation, same page ("2026 industry data") | 2026 | Part IV's option arithmetic uses this range |
| Performance restoration, excluding LLPs | $1.8–2.5M | Safe Fly Aviation, "What determines aircraft engine overhaul costs?" and "CFM56-7B availability report 2026" | 2026 | This Part's worked example uses the midpoint, $2.15M |
| Heavy shop visit with LLPs: PR plus replacement of parts at or near limit | $2.1–2.8M | Safe Fly Aviation ("2026 industry data") | 2026 | None |
| Full heavy overhaul with complete LLP replacement | ">$3.5M" | Safe Fly Aviation (other page) | 2026 | None |
| Full overhaul ("zero-time"): all modules to overhaul standard, full LLP stack | $3.5–4.2M | Safe Fly Aviation, "Engine Shop Visit Costs Worldwide 2026" | 2026 | Carried by D2 only |
| CFM56-5 light performance restoration | ~$300k, "up to the double for a more thorough visit" | Leeham News (trade press) | 17 Mar 2017 | Different workscope and year; not comparable |
| V2500 heavy shop visit (contrast) | $2–3M "depending on the LLP profile" | Aircraft Commerce Issue 70 (trade press) | 2010 | Fifteen years old; §10 |
| Performance restoration, reserve-model input | $4.5M | D6 §2.2, labelled "ASSUMED (illustrative)" | 2026 | Sits above every sourced range |
| A shop visit | "costed in the single-digit millions" | D7 §2.4, description | 2026 | Not a figure |

<cite>Source: Safe Fly Aviation, "Engine Shop Visit Costs Worldwide 2026", "What determines aircraft engine overhaul costs?" and "CFM56-7B engine availability report 2026" (2026, consultancy blog); Leeham News, Bjorn's Corner Part 3, 17 Mar 2017; Aircraft Commerce Issue 70, 2010; D6 §2.2; D7 §2.4. Reconciliation R-013; E.1 rule 4.</cite></div>

Two things stand out in that table. The first is that the two consultancy sets disagree with each other on the same scope: a restoration is $1.2–1.6M on one page and $1.8–2.5M on another, and a heavy visit with life-limited parts is $2.1–2.8M on one and more than $3.5M on the other. <span class="cite">[Safe Fly Aviation, 2026; D1 T3]</span> The second is that none of the "with LLPs" totals is consistent with a full new set of life-limited parts at 2025 list. A full set is $5.7M on the figure this Part uses (or about $4M on Part IV's); a restoration at $1.4M plus a full set at $4M is already $5.4M, above every quoted "with LLPs" range. <span class="cite">[D2 §2.1; D1 T3]</span> So the quoted totals must assume partial replacement, used parts, or older price levels. The primer does not pick a range. Part I's worked example uses the $1.8–2.5M midpoint and Part IV's option arithmetic uses $1.2–1.6M, and each names the other. <span class="cite">[E.1 rule 4]</span>

### 7.2 The shares: material, labour, repairs

<div class="exh"><div class="exh-title">Exhibit 1.10 — Where a shop visit's cost sits: two share breakdowns and the turbine-blade tension</div>

| Item | Figure | Source and level | Date |
|---|---|---|---|
| Material share of a visit | 60–70% | Air Cargo Week (trade press) | 2025/26 |
| Labour share of a visit | 20–30% | Air Cargo Week | 2025/26 |
| Repairs and other shop activities | 10–20% | Air Cargo Week | 2025/26 |
| LLPs as share of parts cost (CFM56) | 40–60% | Safe Fly Aviation (consultancy blog) | 2026 |
| HPT blades and vanes as share of parts cost | 15–25% | Safe Fly Aviation | 2026 |
| Labour share (CFM56) | 15–20% | Safe Fly Aviation | 2026 |
| HPT blades and vanes in dollars, at the Safe Fly share applied to the visit total as an approximation | $0.18–0.40M on a $1.2–1.6M visit; $0.27–0.63M on a $1.8–2.5M visit | Derived from the two rows above | 2026 |
| New OEM HPT blade, price each | About $20,000 | In Practise expert interview (interview digest), via D4 | Undated |
| New OEM HPT blade, alternative listing | About €35,000 | Web page of weak provenance, condition unclear, via D4 | Undated |
| HPT blades per set | 80, an unverified recollection (D4 U16) | D4 | Not dated |
| Implied HPT blade set | $1.6M at $20,000; $3.08M at about $38,500 | Derived in D4 §2.8 | Not dated |
| HPT blade and vane set | "up to a few million dollars" | In Practise, via D4 | Undated |
| Labour-rate inflation, 2025 | 5.5–6.0% | Oliver Wyman MRO survey (consultancy) | Apr 2026 |
| Labour hours per workscope; shop rate per hour | Not found | D1 U7 | Not dated |

<cite>Source: Air Cargo Week, "The true cost of engine maintenance", 2025/26; Safe Fly Aviation, 2026 (consultancy blog); In Practise, "FTAI, Chromalloy and CFM56 HPT Blade PMA", undated; web listing of weak provenance (D4 [72]); Oliver Wyman, "The new MRO supply paradigm", Apr 2026. Reconciliation R-014 and R-015.</cite></div>

The two share breakdowns come from different secondary sources and neither names a shop-level data set. <span class="cite">[reconciliation R-014]</span> One dossier reads them as consistent, since life-limited parts and turbine airfoils together are the bulk of material and material is the bulk of the visit. <span class="cite">[D2 §2.2]</span> The turbine-blade line is a direct contradiction at the level of one cost item. Priced per blade from an interview and a listing, a set of 80 blades is $1.6M to $3.1M, which is close to or above the whole restoration; priced as 15–25% of parts cost from the consultancy shares, the blades and vanes together are $0.2M to $0.6M. <span class="cite">[D4 §2.8; Safe Fly Aviation, 2026; reconciliation R-015]</span> The blade count is a recollection and the list price of a full blade-and-vane set was not retrieved, so the primer reports both sides and stops. <span class="cite">[D4 U16]</span>

### 7.3 A worked example, input by input

<div class="worked"><div class="h">Worked example 1.6 — A performance restoration with life-limited-part replacement, CFM56-7B26, second shop visit, 2025 prices</div>
<p>Every input is labelled. The engine is at 12,000 cycles since new (assumed); its core life-limited parts have a 20,000-cycle limit (sourced: mini-packs) and so 8,000 cycles left; the planned next run is 12,000 cycles (assumed, inside Leeham's 10,000–15,000-cycle range).</p>
<p>Step 1, the restoration workscope excluding life-limited parts. Take the midpoint of the $1.8–2.5M range, $2.15M (sourced: Safe Fly Aviation, consultancy blog, 2026; midpoint is this Part's choice under E.1 rule 4). The alternative range is $1.2–1.6M, midpoint $1.4M (sourced: Safe Fly Aviation, other page; used by Part IV). Within the $2.15M: labour at 15–20% is $320,000–430,000 (sourced share; hours and rate unknown, D1 U7); turbine blades and vanes at 15–25% are $320,000–540,000 (sourced share); the remainder of $1.2–1.5M is other new parts, repairs, test and consumables (derived).</p>
<p>Step 2, the life-limited parts. Three options. (a) A full new set at list, $5.7M (sourced: MyAirTrade, June 2025, scope not visible). This would replace fan and booster parts with 18,000 cycles still on them, so a shop would not do it; it is the ceiling case. (b) New core parts only (compressor spools and disk, turbine disk, shafts). The core group's share of the set was not retrieved (D1 U8), so this line cannot be priced. (c) A used core package with about 12,000 cycles remaining, matched to the next run. Such packages are advertised; their prices were not shown (D1 U4).</p>
<div class="eqblock">case (a) at $5.7M: 2,150,000 + 5,700,000 = $7,850,000
case (a) at the $4.0M alternative set price: 2,150,000 + 4,000,000 = $6,150,000
case (a) at the 2018 list of $3.4M: 2,150,000 + 3,400,000 = $5,550,000
restoration alone at the alternative midpoint: $1,400,000</div>
<p>Step 3, what the totals say about the quoted ranges. The "heavy shop visit with LLPs" figures of $2.1–2.8M and more than $3.5M (sourced: Safe Fly Aviation) are reachable only with partial replacement, used parts or older prices; a full new set at either current figure puts the visit above $6M.</p>
<p>Step 4, cost per cycle over the next 12,000-cycle run.</p>
<div class="eqblock">restoration only: 2,150,000 ÷ 12,000 = $179 per cycle (alternative: 1,400,000 ÷ 12,000 = $117)
full set over its 20,000-cycle life: 5,700,000 ÷ 20,000 = $285 (alternative set: $200)
full set scrapped after 12,000 cycles: 5,700,000 ÷ 12,000 = $475 (alternative set: $333)</div>
<p>So the life-limited-part decision moves the engine's maintenance cost per cycle by more than the whole restoration workscope does, on either set price. That is the arithmetic that creates a market for used life-limited parts and for cores whose remaining lives match the buyer's planned run (Part V §34 and §36).</p>
<p>Step 5, time. The restoration takes 75–90 days (sourced: Safe Fly) or 90–120 days (sourced: trade press); against that, a core module from inventory is a quick-turn (sourced: StandardAero's menu). The owner's alternative cost is the spare-engine rent of worked example 1.5. Limits of the example: both consultancy ranges are contested; the set price has two readings; the core-only and used-package prices are unknown; labour hours and rates are unknown. <span class="cite">[D1 example D; Safe Fly Aviation, 2026; MyAirTrade, June 2025; Aircraft Value News, Nov 2019; Aircraft Commerce Issue 120; reconciliation R-013, R-016, R-017]</span></p></div>

Who collects each of those lines is the subject of Part IV §29, and §11 of this Part gives a first map. For now the structure is enough: 60–70% of the bill is material, most material is priced off the manufacturer's catalogue, and the catalogue is repriced upward every year, so escalation flows into every shop visit regardless of who performs it. <span class="cite">[Air Cargo Week, 2025/26; D2 §2.2]</span> The levers a shop other than the manufacturer has are all on the material line: used parts instead of new, approved alternative parts instead of the manufacturer's, repair instead of replacement, and exchange instead of overhaul. Parts V, VI and VII take those four levers in turn.

## 8. What an engine is worth: half-life, full-life, maintenance-adjusted value

An engine's value depends on how much life is left in it, and the trade has a standard way of saying so. Independent valuers publish figures for a reference condition and then adjust them for the engine in front of them.

<div class="defn"><b>Appraiser</b><p>An appraiser is an independent valuer that publishes base and market values and lease rates for aircraft and engines, at half-life unless stated; the four this primer cites are IBA, mba Aviation, Ascend by Cirium and AVITAS (a US appraisal firm). The market trades on their figures, and securitisation rating agencies test deals against them. Part II §12 carries the full treatment. <span class="cite">[D1 §2.8; D3 §2.4]</span></p></div>

<div class="defn"><b>ISTAT</b><p>ISTAT, the International Society of Transport Aircraft Trading, is the trade body whose definitions standardise appraisal terms such as half-life and full-life. <span class="cite">[D1 §2.8]</span></p></div>

### 8.1 The three value concepts

<div class="defn"><b>Half-life (base) value</b><p>Half-life is an appraisal convention, not a physical midpoint. In ISTAT's words it is "a standard appraisal industry term to indicate that no value adjustment has been made for the actual maintenance status ... the assumption being that the airframe, engines (modules & LLPs), landing gear, and other major maintenance events are in half-life status. It does not indicate that the aircraft is half-way through its useful life." For an engine it assumes every module halfway between restorations and every life-limited part at half its certified life. One source defines it as every scheduled event at its mid-point and every life-limited part at the mid-point of its ultimate life; another as each component midway between overhauls with half its cycles remaining. Two caveats recur: full life is "theoretical, even on a new aircraft", and the concept becomes "fluid" as aircraft pass mid-life because the market stops paying for maintenance status it will never use. <span class="cite">[ISTAT Jetrader, Jul/Aug 2010; Calver, Apr 2023; D6 §2.1; Aircraft Value News, undated; registry C-1]</span></p></div>

<div class="defn"><b>Full-life value</b><p>Full-life value is the value with every maintenance item fresh and every life-limited part at zero cycles: "full-life engines are brand new or in recently restored condition". It equals the half-life value plus half the cost of a full restoration and a full set of life-limited parts. It is theoretical even for a new engine, which has already consumed test cycles. <span class="cite">[VREF (an aircraft valuation service), undated; Calver, Apr 2023; D1 §2.8]</span></p></div>

<div class="defn"><b>Maintenance-adjusted value</b><p>Maintenance-adjusted value is "the fair market value of an Aircraft or Engine based on half-life values as adjusted by the relevant Aircraft Appraiser for the actual maintenance conditions and specifications". For each item the adjustment is (actual remaining fraction − 0.5) multiplied by the cost to restore that item, summed module by module. On this Part's inputs the swing between a fresh and a run-out -7B of the same age is about $2.8M (worked example 1.7). <span class="cite">[Law Insider, "Maintenance Adjusted CMV (current market value)"; D1 §2.8]</span></p></div>

<div class="defn"><b>Base value and market value</b><p>Base value is an appraiser's opinion of an asset's underlying economic value in an open, unrestricted, stable market with balanced supply and demand. Market value is the appraiser's opinion of the most likely trading price in the actual current market between willing, informed parties; it sits above base value in a tight market and below it in a soft one. Both are quoted at half-life unless stated. The research reached market values for the -7B (below) and no base values (D1 U9). Part II §12 carries the full treatment. <span class="cite">[D3 §2.4]</span></p></div>

Because the modules are separable (§3) and carry clocks that deliberately do not align (§4), the adjustment is naturally computed module by module. Engine value equals the reference value plus the sum over modules of each module's restoration and life-limited-part adjustments. <span class="cite">[D1 §2.8]</span>

<div class="defn"><b>Sum of modules (sum of parts)</b><p>Sum of modules is the engine's value computed module by module, or as parts. It can exceed the whole-engine value when the modules' remaining lives are mismatched: a fan with 18,000 cycles of life attached to a core with 1,500 is worth more as a fan module sold to someone who needs a fan plus a core sold for its stub life than as one engine that must go into a shop. <span class="cite">[D1 §2.8]</span></p></div>

<div class="defn"><b>Module as a unit of trade</b><p>A serviceable module from a dismantled engine is valued like a whole engine in miniature: its serviceable parts at a discount to list, plus the remaining life of the life-limited parts inside it, less the repair needed to make it serviceable. It is tradeable because the design lets a shop fit it without disassembling the rest, and because its records travel with it. Part V §36 carries the full treatment. <span class="cite">[D3 §2.7]</span></p></div>

<div class="defn"><b>Part-out and teardown</b><p>Part-out is the owner's decision to dismantle a retired aircraft or engine and sell its components individually; teardown is the physical disassembly. A run-out CFM56 bought for $0.8–1.2M is reported to yield $1.6–2.2M of used material, net $0.4–0.8M before repair cost (consultancy blog, 2026). Part V §32 carries the full treatment. <span class="cite">[D3 §2.2; Safe Fly Aviation, 2026]</span></p></div>

### 8.2 The published values, and the bases they sit on

<div class="defn"><b>Green time</b><p>Green time is the remaining usable life on an engine or module before its next mandatory shop visit, set by whichever runs out first: the life-limited part with the fewest cycles remaining, the EGT margin, or a hard inspection or directive. A green-time engine is one the owner will not restore, flown or leased "as-is" to use up that life and then torn down. Part II §16 carries the full treatment. <span class="cite">[D3 §2.3; D2 §2.3; registry C-2]</span></p></div>

<div class="exh"><div class="exh-title">Exhibit 1.11 — CFM56-7B values and lease rates: each figure with its basis, source level and date</div>

| Quantity | Figure | Basis | Source and level | Date |
|---|---|---|---|---|
| CFM56-7B24 market value | $5.7M | Half-life, H2 2025 | IBA, Engine Values Release 2025B (appraiser) | Sept 2025 |
| CFM56-7B27 market value | $6.4M | Half-life, H2 2025 | IBA, 2025B (appraiser) | Sept 2025 |
| CFM56-7B value change | "Around 20% from 2023 to 2024", the largest gain among engines covered | Market value | IBA (appraiser) | Apr 2024 |
| CFM56-5B/-7B value trend | "Have levelled off after approximately 18 months of increases" | Market value | IBA H1 2026 update (appraiser) | H1 2026 |
| CFM56-7B "green-time value" | $2.8–3.4M | Labelled "(new condition)", which the research notes is internally inconsistent with "green-time" | Safe Fly Aviation (consultancy blog) | 2026 |
| CFM56-5B "green-time value" | $2.6–3.2M | Same label | Safe Fly Aviation | 2026 |
| Low-life engine as teardown feedstock | $0.8–1.2M acquisition; $1.6–2.2M of used serviceable material (USM) recovered; net $0.4–0.8M | Run-out engine | Safe Fly Aviation | 2026 |
| CFM56 values | Up "as much as 50% over the past two years" | Not stated | ePlaneAI (trade press) | Date not captured |
| LLP life as share of a used engine's value | 60–80%; two -7Bs at 10,000 cycles since new differ by $1.6M on LLP life alone | Used engine | Safe Fly Aviation | 2026 |
| CFM56-7B spare-engine lease rate | ~$100,000 a month in 2024, from ~$75,000 in 2019 | Spare engine | IBA (appraiser) | Apr 2024 |
| CFM56-7B lease rate | $42,000–48,000 a month; "about 34% above 2019"; up 15–20% "in recent months" | Quoted beside green-time values; basis not stated | Safe Fly Aviation | 2026 |
| CFM56-5B lease rate | $38,000–44,000 a month | Same | Safe Fly Aviation | 2026 |
| V2500-A5 lease rate | $70,000–80,000 a month | Typical | IBA, 2025B | Sept 2025 |
| CFM56-5B LLP value | $9,878,733 full life; $4,939,366 half life (2023 dollars) | Per engine or per aircraft unstated (D3 U3) | Calver, Cargo Facts (conference presentation) | Apr 2023 |

<cite>Source: IBA, "Engine Values Release September 2025 (2025B)"; IBA, "Engine and Lease Rate Update H1 2026"; IBA, "It's a lessors' market", Apr 2024 (and AviTrader, 25 Apr 2024); Safe Fly Aviation, "CFM56 Engine Market Report 2026" (consultancy blog); ePlaneAI, "CFM56 engine values highlight investor opportunities and risks", date not captured; Mark Calver, Cargo Facts Session 3, Apr 2023. Reconciliation R-028 and R-029; E.1 rule 6.</cite></div>

The exhibit holds a conflict the primer does not resolve. On one side, the appraiser: IBA gives half-life market values of $5.7M for the -7B24 and $6.4M for the -7B27 for the second half of 2025, describes the -7B market as having "a distinct lack of availability" with values and lease rates above long-term trend, recorded a rise of about 20% from 2023 to 2024, and in its first-half 2026 update says -5B and -7B values "have levelled off after approximately 18 months of increases". <span class="cite">[IBA, Sept 2025; IBA, Apr 2024; IBA, H1 2026]</span> On the other, a consultancy blog gives a -7B "green-time value (new condition)" of $2.8–3.4M and a teardown value of $0.8–1.2M, and reports rents still rising by 15–20% "in recent months", while a trade-press item has values up by as much as 50% over two years. <span class="cite">[Safe Fly Aviation, 2026; ePlaneAI, date not captured]</span> The figures sit on different bases: a half-life market value is not a green-time value, and neither is a teardown value. The label "(new condition)" on a green-time figure is internally inconsistent, as the research noted. And the sources disagree on direction, levelled off against still rising. <span class="cite">[D3 T3; reconciliation R-029]</span> Both sides are carried; the primer takes no view on which describes the market better. The same is true of the two lease rates, $100,000 a month from the appraiser in 2024 and $42,000–48,000 from the blog in 2026, which may price different engines. <span class="cite">[reconciliation R-028]</span> One dossier divided the $45,000 midpoint by the $6.4M value to get 0.70% a month and noted that the calculation mixes a green-time rent with a half-life value; no lease rate factor is stated as a single number anywhere in this primer, and Part II §14 carries the derived figures with their bases. <span class="cite">[D3 §2.3; E.1 rule 6]</span>

### 8.3 A valuation example

The dossier that built the valuation arithmetic wrote it against a half-life base value, which the research never reached; what it reached later was IBA's half-life market value, a different quantity. The arithmetic is identical and the reference point differs, so the example below uses the market value and says so. <span class="cite">[D1 U9; reconciliation C.1 item 2]</span>

<div class="worked"><div class="h">Worked example 1.7 — Maintenance-adjusted value of a mid-life CFM56-7B27</div>
<p>Inputs: half-life market value $6.4M for a -7B27, H2 2025 (sourced: IBA, Sept 2025; used here as the half-life reference). Full set of life-limited parts $5.7M (sourced: MyAirTrade, June 2025, scope not visible; alternative $4.0M, Aircraft Value News, Nov 2019). Restoration cost $2.15M (sourced midpoint of Safe Fly Aviation's $1.8–2.5M; alternative $1.4M from the other range). Restoration interval 12,000 cycles (assumed, within Leeham's range). The engine's life-limited parts average 65% of life remaining (assumed), and it has flown 3,000 cycles since its last restoration, so 9,000 of 12,000 remain, 75% (assumed).</p>
<div class="eqblock">LLP adjustment = (0.65 − 0.50) × 5.7M = +$0.855M   (alternative set: (0.15) × 4.0M = +$0.60M)
PR adjustment  = (0.75 − 0.50) × 2.15M = +$0.54M   (alternative PR: (0.25) × 1.4M = +$0.35M)
maintenance-adjusted value = 6.4M + 0.855M + 0.54M = $7.8M   (alternative inputs: 6.4M + 0.95M = $7.35M)</div>
<p>The same engine at 9,000 cycles since restoration (25% remaining) and 35% life-limited-part life:</p>
<div class="eqblock">(0.35 − 0.50) × 5.7M = −$0.855M;  (0.25 − 0.50) × 2.15M = −$0.54M;  value = 6.4M − 1.4M = $5.0M
swing between the two states = $2.8M   (alternative inputs: $1.9M)
full-life value = 6.4M + 0.5 × (5.7M + 2.15M) = $10.3M   (alternative inputs: 6.4M + 2.7M = $9.1M)</div>
<p>So the maintenance adjustment is driven mostly by the life-limited-part line, and the swing between a fresh and a run-out engine of the same model and age is about $2.8M on this Part's inputs, or about $1.9M on Part IV's. For comparison, the consultancy blog's statement that two -7Bs at 10,000 cycles since new can differ by $1.6M on life-limited-part life alone falls between the two LLP swings here ($1.71M and $1.20M); the figures are reported side by side, not reconciled. A -5B version of the same arithmetic exists in the research: on the Calver figure read as a pair of engines, $4.94M of life-limited parts per engine at full life, an engine at 75% life is worth 0.25 × $4.94M = $1.23M more than half-life and one at 25% is worth $1.23M less, with the per-engine-or-per-aircraft caveat attached. Limits of the example: the reference is a market value standing in for a base value; the set price and restoration cost each have two readings; the remaining-life fractions are assumed; and the -7B24 at $5.7M would shift every total down by $0.7M. <span class="cite">[D1 example E; IBA, Sept 2025; Calver, Apr 2023, via D3 §2.4; Safe Fly Aviation, 2026]</span></p></div>

Two further caveats come from the appraisers themselves. For engines whose life limits outlast the aircraft, the "half" reference is fluid: on the CFM56-3, 20,000 cycles at 1,000 to 1,500 cycles a year "equates to more than 15 years, considerably longer than the envisaged economic life", so appraisers may not treat 10,000 cycles as half-life. <span class="cite">[Aircraft Value News, undated]</span> And the full-life adjustment assumes the manufacturer's list price for every part, which is why the same publisher records that approved alternative parts "continue to undermine full-life maintenance adjustments" (Part VI §42), and why CFM's TRUEngine designation, "embraced by industry's leading asset valuation providers", is the manufacturer's lever on this calculation. <span class="cite">[Aircraft Value News, undated; CFM International, TRUEngine release]</span>

## 9. Records, release tags and the shop manual

An engine is only worth its paperwork. A module with a gap in its records cannot be installed, however good its metal. This section is brief because Part V owns what makes a used part serviceable and Part VI owns alternative parts and repairs; what belongs here is the set of documents a module carries and why each exists.

<div class="defn"><b>Back-to-birth traceability (BTB)</b><p>Back-to-birth traceability is a continuous record, for each life-limited part, of every cycle it has flown on every engine since manufacture, with no gaps. A gap means the part's remaining life cannot be proven and it is treated as unusable. The research reached industry descriptions of the term and no formal regulatory definition. <span class="cite">[D1 §2.9, U11; AviTrader, 23 Apr 2026]</span></p></div>

<div class="defn"><b>Serviceable and unserviceable</b><p>A part or module is serviceable when an approved organisation has inspected and released it and it is eligible for installation. It is unserviceable when it has been removed pending repair, or scrapped. The release is evidenced by a tag. <span class="cite">[D1 §2.9; D3 §2.1]</span></p></div>

<div class="defn"><b>Release tag (serviceable tag)</b><p>The release tag is the signed airworthiness release, on FAA Form 8130-3 or on the European Union Aviation Safety Agency (EASA) Form 1, by which an approved organisation makes a part legally serviceable. It is necessary and not sufficient: the buyer also needs the part's documented history, and because the forms "can be easily generated" buyers vet the supplier too. Part V §31 carries the full treatment. <span class="cite">[D3 §2.1; D1 §2.9]</span></p></div>

### 9.1 The two release forms

<div class="defn"><b>Production certificate (PC) and type certificate (TC)</b><p>A type certificate is the regulator's approval of an engine's design; its holder is the manufacturer (CFM International for the CFM56). A production certificate, or production approval, is the regulator's approval under which the type-certificate holder, or a PMA holder, manufactures parts. A replacement part may be installed only if it was produced under one, or under narrow exceptions. Part VI §37 carries the full treatment. <span class="cite">[D4 §2.1]</span></p></div>

<div class="defn"><b>Part 145 repair station</b><p>A Part 145 repair station is a maintenance organisation certificated by the FAA, or its European equivalent under the European Union Aviation Safety Agency (EASA), to perform maintenance and to issue release tags. It is the approval an engine shop or a component repair shop holds. Part IV §25 carries the full treatment. <span class="cite">[D2 §2.1; D3 §2.1]</span></p></div>

<div class="defn"><b>FAA Form 8130-3 (Airworthiness Approval Tag; Authorized Release Certificate)</b><p>Form 8130-3 is the US tag. For a new part it states that the part, produced under an FAA production approval, conforms to its design and is in a condition for safe operation; for a used part it is the maintenance release by an FAA-approved repair station. "Products and articles not produced under an FAA production approval are not eligible to receive an FAA Form 8130-3." <span class="cite">[Aviation Suppliers Association, 2016]</span></p></div>

<div class="defn"><b>EASA Form 1</b><p>EASA Form 1 is the European agency's authorised release certificate, the equivalent of Form 8130-3, issued by an EASA-approved maintenance or production organisation. New parts made under a European production organisation approval (POA) "are typically ineligible for an 8130-3 tag and are more properly released on an EASA Form 1". <span class="cite">[Aviation Suppliers Association, 2016; D1 §2.9]</span></p></div>

<div class="defn"><b>Dual release</b><p>A dual release is one tag signed under both FAA and EASA authority, so that a part can move between US- and EU-registered aircraft without re-certification. The research reached industry descriptions only. <span class="cite">[D1 §2.9, U11]</span></p></div>

The trade press lists the documents a buyer most commonly requires: the release form, "Certificates of Conformance, manufacturer certifications (PMA, PC, TC)", ATA (Air Transport Association) Specification 106 sheets, "and return-to-service records from operators or repair stations". <span class="cite">[Aviation Business News, undated]</span> Incorrectly issued 8130-3 tags are a recurring compliance problem in the parts trade, which is why buyers check the issuing organisation and not only the form. <span class="cite">[Aviation Maintenance magazine, undated]</span>

### 9.2 The manuals and who may go beyond them

<div class="defn"><b>Engine Shop Manual (ESM)</b><p>The Engine Shop Manual is the manufacturer's manual defining how the engine is disassembled, inspected, repaired and rebuilt, including the limits a part must meet to stay in service. Regulators treat it as the reference: an Australian airworthiness directive notes that the "CFM56-7B ESM contains instructions for calculating remaining life of each engine stationary part within certain time frames and thresholds". A repair the manual does not cover needs separate approval. <span class="cite">[Civil Aviation Safety Authority (CASA) of Australia, AD 2014-0130; D1 §2.9]</span></p></div>

<div class="defn"><b>Component Maintenance Manual (CMM)</b><p>The Component Maintenance Manual is the manufacturer's document that sets inspection and repair limits for an individual component; the Engine Shop Manual is the engine-level equivalent. Part V §31 carries the full treatment. <span class="cite">[D3 §2.1]</span></p></div>

<div class="defn"><b>Designated Engineering Representative (DER) and DER repair</b><p>A Designated Engineering Representative is an engineer appointed by the FAA to examine engineering data and make compliance findings on the FAA's behalf. A DER repair is a major repair whose data a DER approved rather than being taken from the manufacturer's manual; the part stays the manufacturer's part, and the repair saves money by restoring what the manual would scrap or restoring it more cheaply. Part VI §40 carries the full treatment. <span class="cite">[D4 §2.6; D2 §2.2]</span></p></div>

Who performed a repair, and under which approval, is recorded on the module and matters when the module changes hands. An engine maintained only with the manufacturer's parts and manual repairs can carry the TRUEngine designation (§3), and GE sells service agreements to the same end. <span class="cite">[CFM International, TRUEngine release; MRO Global, Safair TrueChoice agreement]</span>

<div class="defn"><b>TrueChoice</b><p>TrueChoice is GE Aerospace's branded menu of CFM56 and LEAP services: Flight Hour (a rate-per-flight-hour agreement), Overhaul (time-and-materials shop visits in GE's network), Material (new and used OEM parts and repairs sold to third-party shops and airlines) and Transitions (green-time leases, exchanges, material buy-back and shorter builds using more used material). Part IV §28 carries the full treatment. <span class="cite">[D2 §2.3; GE Aerospace releases]</span></p></div>

<div class="defn"><b>Return conditions (redelivery conditions)</b><p>Return conditions are the contractual minimum state of a leased engine at redelivery: minimum hours and cycles to the next restoration, minimum cycles remaining on each life-limited part, a borescope and a test-cell run, and records in order. They may exclude parts and repairs that are not the manufacturer's. Part II §13 carries the full treatment and Part VI §42 the clause on alternative parts. <span class="cite">[D6 §2.1; D4 §2.9]</span></p></div>

<div class="exh"><div class="exh-title">Exhibit 1.12 — The documents a module carries: what each proves and who issues it</div>

| Document | Who issues it | What it proves | Why a module exchange needs it |
|---|---|---|---|
| Back-to-birth trace for each life-limited part | Every operator and shop in the part's history | Every cycle flown since manufacture, without gaps | Remaining life cannot be proven without it; the part is treated as unusable |
| FAA Form 8130-3 | Production-approval holder (new part) or FAA-approved repair station (used part) | Conformity to design, or maintenance release | Makes the part legally serviceable in the US system |
| EASA Form 1 | EASA-approved production or maintenance organisation | The European equivalent | Needed for EU-registered aircraft; a dual release serves both |
| Service-bulletin and airworthiness-directive compliance records | Operator or shop | Build standard and mandatory inspections complied with | Two modules at different standards may not mate or be approved together |
| Repair records with their approval basis | Shop | Whether a repair followed the manual or a separately approved scheme | A lessor's return conditions may exclude non-manufacturer repairs |
| Certificates of conformance; manufacturer certifications; ATA 106 sheets; return-to-service records | Seller, manufacturer, operator, repair station | Provenance and release history | Standard elements of a used-part documentation package |

<cite>Source: D1 §2.9; Aviation Suppliers Association, 8130-3 workshop, 28 Jun 2016, and member bulletin, May 2016; Aviation Business News, "The evolution of airworthiness documentation for aircraft parts", undated; D3 §2.1. Part V §31 carries the full treatment.</cite></div>

The practical conclusion for the rest of the primer is the one §3 reached from the other direction. The usable supply of modules is the documented supply, not the physical one. <span class="cite">[D1 §5]</span>

## 10. The V2500 and the LEAP, for contrast

Two other engines frame the CFM56. One is its contemporary and competitor on the A320ceo. The other is its replacement. Part III §20 owns what each did to demand for CFM56 work; this section sets out the machines and the figures the research reached.

### 10.1 The V2500

<div class="defn"><b>V2500 and IAE</b><p>The IAE V2500-A5 is the A320ceo family's alternative engine, a two-shaft modular turbofan built by the IAE consortium, IAE International Aero Engines. Aircraft Commerce in 2010 gave the shareholders as Pratt & Whitney 32.5%, Rolls-Royce 32.5%, the Japanese Aero Engines Corporation (JAEC) 23% and MTU (Germany's MTU Aero Engines) 12%; a 2024 RTX (Pratt & Whitney's parent) release names the current members as Pratt & Whitney, Pratt & Whitney Aero Engines International, JAEC and MTU Aero Engines. Rolls-Royce's exit was widely reported and not retrieved by the research; the 2010 table is stale. <span class="cite">[Aircraft Commerce Issue 70, 2010; RTX release, 6 Jun 2024; reconciliation R-070]</span></p></div>

The V2500 pool is smaller than the CFM56 pool. About 5,286 V2500s were in service in 2023, of which 5,260 were -A5s, against roughly 23,000 to 24,000 CFM56s of all variants, so the V2500 pool is about a quarter the size and a smaller fraction still of the A320ceo-only pool. <span class="cite">[Aviation Week 2023 Fleet & MRO Forecast; D1 §2.10]</span> A market-research page gives ">13,000 units" in service in mid-2026; the research flagged that page as low grade and the primer cites it only as such. <span class="cite">[MarketIntelo, 2026; reconciliation R-010]</span> The research did not retrieve the V2500's module list or a current shop-visit cost. The one cost source reached is fifteen years old: a heavy visit at $2–3M "depending on the life limited part (LLP) profile required" and a full set of life-limited parts at $1.7M list, both as of 2010, which should not be set beside the 2025 CFM56 figures in §7. <span class="cite">[Aircraft Commerce Issue 70, 2010; D1 U13]</span>

Shop-visit counts for the V2500 disagree. Aviation Week's data tool projected a spike to about 1,400 V2500 shop visits in 2025 and more than 7,800 overhaul visits plus 3,142 life-limited-part visits over the ten years from 2023; RTX's chief financial officer, reported by the same publication in 2026, put 2025 at "slightly more than 800" with 2026 expected within about 20 of that. <span class="cite">[Aviation Week data tool, 2023; Aviation Week, 2026; reconciliation R-009]</span> A forecast and a reported outturn, both via one publication; the primer carries both. MTU Maintenance, an engine maker's shop that is independent on this engine, performed 38% of all V2500 shop visits in 2024 and marked its 7,000th V2500-A5 visit in 2025. <span class="cite">[MTU Aero Engines, 2025]</span>

<div class="defn"><b>EngineWise</b><p>EngineWise is Pratt & Whitney's aftermarket services brand, under which IAE's network performs V2500 shop visits. Part IV §28 carries the full treatment. <span class="cite">[RTX release, 6 Jun 2024; D2 §2.3]</span></p></div>

<div class="defn"><b>FTAI's V2500 program (the IAE EngineWise agreement)</b><p>On 6 June 2024 IAE and FTAI signed a five-year EngineWise agreement covering more than 100 full performance-restoration shop visits on V2500 engines in IAE's network, described by RTX as "one of IAE's largest engine maintenance agreements by number of engines with a non-airline customer". It is a different model from the Module Factory: a large engine owner buying manufacturer-network restorations at a committed volume. Part VII §51 carries the full treatment. <span class="cite">[RTX release, 6 Jun 2024; D5 §2.5]</span></p></div>

### 10.2 The LEAP

<div class="defn"><b>LEAP (LEAP-1A and LEAP-1B)</b><p>The LEAP is CFM's new-generation engine: the LEAP-1A is one of two options on the Airbus A320neo family, and the LEAP-1B is the sole engine of the Boeing 737 MAX (the re-engined 737). About 5,500 were in service at the date of one trade-press piece, with about 50% under long-term service agreements against about 15% of the CFM56 fleet. Part III §20 carries the full treatment. <span class="cite">[Aviation Week, undated; D9 §2.5]</span></p></div>

The LEAP's durability sets the CFM56's remaining working life, because an airline that cannot keep a new aircraft flying keeps its old one in service instead. Operators have reported "a wave of early LEAP-1A/1B shop visits", with removals between 2,000 and 6,000 cycles and "a planning base of 4,000", against a mature CFM56's restoration interval of 10,000 to 15,000 cycles. <span class="cite">[Visual Approach, undated; Leeham News, 8 Mar 2024]</span> The problems concentrate in hot and harsh environments and in the high-pressure turbine blade and the fuel nozzles. <span class="cite">[D9 §2.5]</span>

<div class="defn"><b>LEAP durability kit (Durability Improvement Package)</b><p>The durability kit is CFM's package of hardware changes to lengthen the LEAP's time on wing: a new high-pressure turbine stage-1 blade and nozzle and a forward inner nozzle support, "designed to more than double time on wing, especially in hot and harsh environments". The LEAP-1A kit is certified and "now incorporated into all deliveries and shop visits". For the LEAP-1B, one source reached by the research gave certification as targeted for the first half of 2026; CFM then announced FAA and EASA certification on 18 July 2026, with full production cutover expected in early 2027. Part III §20 carries the full treatment. <span class="cite">[InsideFlyer / ePlaneAI, undated; CFM International release, 18 Jul 2026; D1 §2.10; D9 §2.5]</span></p></div>

By May 2026 GE Aerospace was stating that LEAPs "being shipped now will match the durability of the venerable CFM56". <span class="cite">[Leeham News, 27 May 2026]</span> Both the problem and the claimed fix are recorded here; whether delivered LEAPs reach CFM56-level time on wing is Part III's question, not this Part's. <span class="cite">[D1 §2.10]</span>

Scale is the other contrast. By December 2017 CFM had orders and commitments for more than 14,270 LEAPs and had delivered 459 in 2017; GE's annual report gives 1,802 LEAP deliveries in 2025 against 1,407 in 2024; Safran reported a LEAP backlog of more than 12,900 units. The cumulative total delivered was not retrieved. <span class="cite">[Safran release, 6 Feb 2018; GE 10-K FY2025; Safran, 13 Feb 2026; D1 U12]</span> The other engine on the A320neo, Pratt & Whitney's geared turbofan, had its own durability problem; Part III §20 carries it.

<div class="exh"><div class="exh-title">Exhibit 1.13 — Three engines side by side: the figures the research reached</div>

| Item | CFM56 (-5B, -7B) | V2500-A5 | LEAP-1A / -1B |
|---|---|---|---|
| Airframes | A320ceo (-5B, ~60%); 737NG (-7B, sole) | A320ceo (alternative) | A320neo (one of two); 737 MAX (sole) |
| Maker | CFM International (GE Aerospace and Safran) | IAE (Pratt & Whitney, P&W Aero Engines International, JAEC, MTU) | CFM International |
| In service | ~23,000 (CFM, undated); ~24,000 (trade press, Sept 2025); >22,800 (Safran, end-2025) | 5,286 in 2023 (Aviation Week); ">13,000" mid-2026 (low-grade vendor page) | ~5,500 (Aviation Week, undated) |
| Production for airframes | Ended 2019 (-7B) and 2022 (-5B) | A320ceo out of production | 1,802 delivered in 2025 (GE 10-K); backlog >12,900 (Safran) |
| Mature restoration interval | 10,000–15,000 cycles (Leeham, 2024) | Not retrieved | Early removals at 2,000–6,000 cycles, planning base 4,000 (Visual Approach) |
| Shop visits a year | 2,300–2,400 in 2026–28 (GE via Aviation Week, 2026); ~2,500 peak 2025–26 (Safran, c. 2023/24) | >800 in 2025 (RTX CFO via Aviation Week, 2026); ~1,400 forecast (Aviation Week data tool) | Not retrieved |
| Share under long-term agreements | ~15% | Not retrieved | ~50% |
| Heavy shop visit cost | Exhibit 1.9 (2026 ranges) | $2–3M (2010) | Not retrieved |
| Full LLP set at list | $5.7M (2025) or ~$4M (2019); see Exhibit 1.6 | $1.7M (2010) | Not retrieved |

<cite>Source: D1 §2.2, §2.10 and §4.1; Aviation Week 2023 Fleet & MRO Forecast and V2500 data tool; Aviation Week, "Pratt & Whitney sees high-single-digit MRO growth", 2026; Aviation Week, "CFM56 overhaul demand remains strong", 2026; Aviation Week, "Safran sees Leap aftermarket emerging by mid-decade", c. 2023/24; Aviation Week, "Leap aftermarket poised for growth", undated; MarketIntelo, 2026; Aircraft Commerce Issue 70, 2010; GE 10-K FY2025; Safran, 13 Feb 2026; Visual Approach, undated. Reconciliation R-006, R-007, R-009, R-010.</cite></div>

## 11. Orientation: where the money sits in this chain

This section is a first map, not an analysis. Part XI §86 carries the full treatment of the margin pool with every figure on its own basis; here the reader needs only to see the links of the chain and a few indicative numbers, so that the segment Parts have a frame. Nothing is ranked.

<div class="defn"><b>Margin pool</b><p>The margin pool is this primer's term for how the profit earned in keeping an engine type flying is distributed across the links of the chain: the manufacturer's new parts and services, the shop's labour, the component repairers, the makers of approved alternative parts, the traders in used material and teardown, the lessors of engines and aircraft, and the servicers of third-party capital. No dossier uses the phrase; its inputs are the slice-by-slice capture of a shop visit (D2 §2.2) and the peers' reported margins on their own bases (D11). Part XI §86 is the full treatment. <span class="cite">[registry 1c]</span></p></div>

Start from the shop visit of §7. Material is 60–70% of it, labour 20–30%, repairs and other shop work 10–20%. <span class="cite">[Air Cargo Week, 2025/26]</span> Each slice has a different collector. New parts go to the manufacturer at catalogue list price, whoever runs the shop; life-limited parts, 40–60% of parts cost when replaced, go to the manufacturer alone because no alternative exists. <span class="cite">[D2 §2.2; Safe Fly Aviation, 2026]</span> Used serviceable material (USM, parts recovered from dismantled engines and re-released) substitutes for new parts and is sold by teardown traders and by the manufacturer itself, which states that "GE and CFM are the largest used serviceable material provider for their products". <span class="cite">[GE Aerospace, 2026, via D2 §2.2]</span> Approved alternative parts (PMA, §5) substitute for the manufacturer's blades and vanes and are sold by their makers. Component repairs go to repair vendors, some under the manufacturer's licence and some under separately approved schemes. Labour and test go to the shop. And the CFM56 aftermarket is mostly transactional: Safran describes about 85% of its revenue as spare parts and time-and-materials work, against about 40% for the LEAP, so on this engine the manufacturer's main capture is parts rather than contracts. <span class="cite">[Safran via Aviation Week, c. 2023/24; D2 §2.3]</span>

Around the shop visit sit the owners. Lessors own engines and aircraft and collect rent and maintenance reserves (Part II). FTAI's two reportable segments sit on both sides of this picture.

<div class="defn"><b>Aerospace Products segment</b><p>FTAI's reportable segment that develops, repairs and sells CFM56 and V2500 engines, modules and parts through the Module Factory; FY2025 segment revenue $1,936.2M and segment Adjusted EBITDA (FTAI's adjusted earnings measure) $671.3M; Adjusted EBITDA is earnings before interest, taxes, depreciation and amortisation as the company adjusts them, defined in Part X §80. Part VII §45 carries the full treatment. <span class="cite">[FTAI 10-K FY2025, via orchestrator notes]</span></p></div>

<div class="defn"><b>Aviation Leasing segment</b><p>FTAI's reportable segment that owns, leases and sells aircraft and engines, directly and through an equity-method investment; 290 assets at 31 Dec 2025 and segment Adjusted EBITDA $608.9M for FY2025. Part VIII §58 carries the full treatment. <span class="cite">[FTAI 10-K FY2025, via D6 and orchestrator notes]</span></p></div>

<div class="exh"><div class="exh-title">Exhibit 1.14 — Indicative margin figures along the chain, each on its own stated basis</div>

| Link in the chain | Company and segment | Margin figure | Basis | Source and date |
|---|---|---|---|---|
| Shop visit, by slice | Any CFM56 shop visit | Material 60–70%; labour 20–30%; repairs 10–20% of the bill | Share of cost, not a margin | Air Cargo Week, 2025/26 |
| Manufacturer, new engines, parts and services | GE Aerospace, Commercial Engines & Services (CES) | 26.6% on $33,314M; services $25,010M of revenue | GE segment profit (GE's own measure) | GE 10-K FY2025 |
| Approved alternative parts | HEICO (a PMA manufacturer), Flight Support Group (FSG) | 24.1% on $3,117.3M | Segment operating income, derived | HEICO 10-K FY2025 (year to 31 Oct 2025) |
| Independent engine shop | StandardAero, Engine Services | 13.2% on $5,354.0M | Segment Adjusted EBITDA, StandardAero's definition | StandardAero 10-K FY2025 |
| Independent engine shop (context, non-SEC) | MTU Aero Engines, commercial MRO | 8.0% on €6.0B | Adjusted EBIT (after depreciation; not comparable with an EBITDA margin) | MTU, 24 Feb 2026 |
| Independent engine shop (context, non-SEC) | Lufthansa Technik | 7.5% on €8.049B | Adjusted EBIT | Lufthansa Technik, FY2025 results |
| Teardown and used material | AerSale, Asset Management Solutions (AMS) | 35.0% on $211.6M | Gross margin, derived | AerSale 10-K FY2025 |
| Module exchange and engine sales | FTAI, Aerospace Products | 34.7% on $1,936.2M (FY2025, derived); 28.5% on $875.0M (Q2 2026, derived) | Segment Adjusted EBITDA (FTAI's definition; includes MRE (Maintenance, Repair and Exchange) Contract revenue to a related party, Part VII §48) | FTAI 10-K FY2025; FTAI release, 29 Jul 2026 |

<cite>Source: Air Cargo Week, "The true cost of engine maintenance", 2025/26 (D2 §2.2); GE 10-K FY2025; HEICO 10-K FY2025; StandardAero 10-K FY2025; MTU Aero Engines, FY2025 results, 24 Feb 2026; Lufthansa Technik, FY2025 results release; AerSale 10-K FY2025; FTAI 10-K FY2025 (segment table via orchestrator notes) and Q2 2026 release (D11 §1 and §4.2). Adjusted EBITDA is earnings before interest, taxes, depreciation and amortisation as each company adjusts it; the five margin bases in this table are not interchangeable, since an EBITDA margin exceeds an EBIT margin by the depreciation share of revenue, and the fiscal years differ (December, October). Part XI §88.</cite></div>

Three cautions travel with the table into Part XI. The margins are on five different bases and are not comparable with each other without adjustment. <span class="cite">[D11 §2.3, §2.5; E.1 rule 35]</span> FTAI's segment figure is a derived ratio of two filed numbers and includes revenue from sales to a partnership in which FTAI holds a 19% stake, which Part VII §48 and Part VIII §63 treat. <span class="cite">[reconciliation R-043, R-047]</span> And a share of cost is not a margin: the first row says where the bill goes, not what anyone earns on it. Part XI §86 builds the pool link by link from these inputs and from the teardown and alternative-parts economics of Parts V and VI.

## Tensions carried in this Part

| Id | The two (or more) figures | Where in this Part |
|---|---|---|
| R-001 | CFM56 in service: ~23,000 (CFM, undated); ~24,000 (Aviation Business News, Sept 2025); >22,800 (Safran, end-2025); "over 20,000" -5B/-7B (Chromalloy); >19,000 and ~14,200 (Safe Fly, consultancy blog) | §2.2, Exhibit 1.2 |
| R-002 | Safe Fly's ~14,200 read as the -7B fleet (D3) or all CFM56 (D8) | §2.2, Exhibit 1.2 |
| R-003 | -7B: "in excess of 8,000" installed (CFM product page) against >15,000 delivered and >7,000 aircraft | §2.2 |
| R-069 | Deliveries >35,000 (CFM) against "well over 30,000" (unsourced) | §2.2 |
| D1 T1 | -7B thrust ceiling 27,300 lbf (secondary) against "33,000" (CFM website summary) | §1, Exhibit 1.1 |
| R-035 | Module count: 4 (D1, D3); 3 plus gearbox (D2); 3 per engine (FTAI release, D8); 4–5 (D5, D9); 5 (D7); 4 (D10); 6 (D11) | §3.2, Exhibit 1.4 |
| R-016 | Full -7B LLP set: $1.775M (2008), $1.7M (2013, caveat), $3.4M (2018), ~$4M (2019), $5.7M (2025); Calver -5B $9.88M (basis unstated) | §4.3, Exhibit 1.6 |
| R-017 | LLP cost per cycle: $200 (D2, $4M set) and $285 (D1, $5.7M set); $333 and $475 with stub life | §4.4, worked example 1.6 |
| R-018 | Escalation: LLP set ~7%/yr compounded, Ishka ~12% step, -7B parts +20–30% (2023) against spares ~10%/yr, double-digit Nov 2022, high-single-digit Aug 2023, inflation +3–4 points | §4.3 |
| R-011 | Removal driver: EGT margin "most influential" (Aircraft Commerce 2003/2008) against LLP-driven for latest -5B/-7B (Aircraft Commerce Issue 50; FlightGlobal) | §5.2 |
| R-008 | Interval: 10,000–15,000 cycles PR, 20,000–25,000 overhaul (Leeham) against "every eight years" (Aviation Week), ~10 years implied (D9), six years assumed (D7) | §5.2, worked example 1.4; Exhibit 1.8 |
| R-019 | Turnaround: 90–120 days (trade press, 2025); ~90 sustaining (GE, May 2026); PR 75–90, heavy 120–150 (Safe Fly); slot wait +2–3 months (Bain) | §6.3, Exhibit 1.8 |
| R-028 | -7B lease rate: ~$100,000/month (IBA, Apr 2024) against $42,000–48,000 (Safe Fly, 2026, may be green-time) | §6.4, worked example 1.5; Exhibit 1.11 |
| R-013 | Shop-visit cost: PR $1.2–1.6M and $1.8–2.5M; heavy with LLPs $2.1–2.8M and ">$3.5M"; full overhaul $3.5–4.2M; light $650–900k (all Safe Fly); D6's $4.5M assumed | §7.1, Exhibit 1.9; worked example 1.6 |
| R-014 | Cost shares: material 60–70% / labour 20–30% / repairs 10–20% (Air Cargo Week) against LLPs 40–60% of parts / HPT blades and vanes 15–25% / labour 15–20% (Safe Fly) | §7.2, Exhibit 1.10 |
| R-015 | HPT blade set $1.6M or $3.08M (per-blade prices × 80, unverified) against $0.2–0.6M implied by the 15–25% share | §7.2, Exhibit 1.10 |
| R-029 | -7B value: half-life market value $5.7M/$6.4M, levelled off (IBA) against green-time $2.8–3.4M, teardown $0.8–1.2M, rents up 15–20% (Safe Fly) and values +50% in two years (ePlaneAI) | §8.2, Exhibit 1.11 |
| R-009 | V2500 shop visits 2025: >800 (RTX CFO via Aviation Week) against ~1,400 forecast (Aviation Week data tool) | §10.1, Exhibit 1.13 |
| R-010 | V2500 in service: 5,286 (Aviation Week, 2023) against ">13,000" (low-grade vendor page) | §10.1, Exhibit 1.13 |
| R-070 | IAE shareholders: 2010 table with Rolls-Royce against the 2024 RTX release without it | §10.1 |

## Unknowns carried in this Part

- **U-D1-01** (D1): **U1** Full numbered sub-module list for the -7B and -5B (the ESM breakdown). Resolve with the CFM56-7B/-5B Engine Shop Manual or a CFM training manual.
- **U-D1-02** (D1): **U2** Exact list of part numbers common to the -5B and -7B core (basis for cross-variant module and LLP interchange). Resolve with the Illustrated Parts Catalogues or a CFM commonality bulletin.
- **U-D1-03** (D1): **U3** Per-part LLP table for the -5B (only the 18-set, 20,000–30,000 range was reached). Resolve with a -5B records mini-pack (AJW, StandardAero publish them).
- **U-D1-04** (D1): **U4** Prices of used LLP packages with stated cycles remaining. Resolve with dealer quotes or D3's sources.
- **U-D1-05** (D1): **U5** As-new EGT margin by -7B/-5B thrust rating and typical loss per 1,000 cycles. Resolve with Aircraft Commerce Issue 58 (-7B) and Issue 50 (-5B) maintenance analyses in full.
- **U-D1-06** (D1): **U6** First-run and mature-run intervals by thrust rating and region. Same sources as U5.
- **U-D1-07** (D1): **U7** Labour hours per workscope and shop labour rates (US$/hour) for CFM56 visits. Resolve with an MRO price catalogue or Aircraft Commerce's maintenance budgets.
- **U-D1-08** (D1): **U8** Core-only LLP group price as a share of the full set. Resolve with a CFM catalogue extract.
- **U-D1-09** (D1): **U9** Current half-life base values for -7B and -5B by rating (IBA, mba, Cirium). Resolve with an appraiser publication; this session's searches returned definitions, not values.
- **U-D1-10** (D1): **U10** Years and amounts of each CFM LLP escalation step 2019–2025 (only "Aug 2023, +20–30% on -7B parts" and "~12% LLP escalation" without a year were reached) [33][34].
- **U-D1-11** (D1): **U11** Formal regulatory definition of back-to-birth traceability and of dual release; this session reached industry descriptions only [14][40][41].
- **U-D1-12** (D1): **U12** Current LEAP delivery total and the dates/years of -5A and -5C production end.
- **U-D1-13** (D1): **U13** V2500 module list and current per-visit cost (2010 figures only) [38].
- **U-D1-14** (D1): **U14** Whether a module exchange requires a test-cell run under the CFM56 ESM.
- **U-D2-01** (D2): **U1. Catalog escalation 2024, 2025, 2026.** Only the Nov 2022 (double-digit) and Aug 2023 (high-single-digit) increases and Safran's "inflation + 3–4 points" rule were found. Resolve with Aviation Week/Aircraft Commerce coverage of each year's CFM price revision, or GE/Safran earnings call Q&A on "price".
- **U-D3-03** (D3): **U3** — Whether Calver's $9,878,733 / $4,939,366 CFM56-5B LLP figure is per engine or per aircraft (two engines). The original Cargo Facts presentation would settle it.
- **U-D3-05** (D3): **U5** — A current appraiser half-life value for the CFM56-5B (only trend commentary and a trade-press lease-rate range were captured).
- **U-D3-06** (D3): **U6** — Current CLP of representative CFM56-7B LLPs (e.g. HPT disk, fan disk) and of a full -7B LLP set. Needed for a precise module-value example.
- **U-D4-16** (D4): **U16 — CFM56-7B HPT blade count per set** (80 is a recollection, unverified here) and the OEM list price for a full HPT blade and vane set.
- **U-D9-03** (D9): **U3 — Definition of the ~24,000 CFM56 "in service" figure [S78]** (installed only, or installed plus spares plus stored) and its split between -5B, -7B and the older -3/-5A/-5C variants. Resolve: GE Aerospace or CFM investor materials with a fleet breakdown; the GE Bernstein presentation (27 May 2026) [S6] may contain it but its content did not surface.

## Sources

1. CFM International, "The CFM56 engine family", undated, accessed 2026-10-03. https://www.cfmaeroengines.com/engines/cfm56
2. CFM International, "CFM56-5B & CFM56-7B" product page, undated. https://www.cfmaeroengines.com/cfm56/CFM56-5B-CFM56-7B
3. Aircraft Commerce, Maintenance & Engineering, Issue 34, 2004 (LLP policy, stub life). https://aircraft-commerce.com/wp-content/uploads/aircraft-commerce-docs/Maintenance/2004/ISSUE%2034-MTCE.pdf
4. AJW Group, ESN 889979 CFM56-7B26 mini-pack (LLP status), 2022. https://www.ajw-group.com/storage/downloads/1644847608_esn_889979_mini_pack_cfm56-7b26.pdf
5. StandardAero, ESN 892820 mini-pack, March 2025. https://standardaero.com/wp-content/uploads/2025/03/ESN-892820-Mini-Pack-PDF.pdf
6. Aircraft Commerce, CFM56-5A/-5B maintenance analysis, Issue 50. https://aircraft-commerce.com/wp-content/uploads/aircraft-commerce-docs/Aircraft%20guides/CFM56-5A-5B/ISSUE%2050-CFM56-5A-5B%20MTCE.pdf
7. Leeham News, Bjorn's Corner, "New aircraft technologies, Part 49: Engine maintenance", 8 March 2024. https://leehamnews.com/2024/03/08/bjorn-s-corner-new-aircraft-technologies-part-49-engine-maintenance/
8. Aircraft Commerce, CFM56-7B Owner's & Operator's Guide, Issue 58, 2008. https://www.aircraft-commerce.com/wp-content/uploads/aircraft-commerce-docs1/Aircraft%20guides/CFM56-7B/ISSUE58_CFM56_7B_GUIDE.pdf
9. CFM56 training material (four-module description), Scribd, undated. https://www.scribd.com/doc/44756596/Engine-CFM56
10. CFM International / GE Aerospace, "CFM International launches TRUEngine program", undated. https://www.cfmaeroengines.com/press-articles/cfm-international-launches-truenginetrade-program
11. Aircraft Commerce, CFM56-7B maintenance analysis & budget, Issue 58, 2008. https://www.aircraft-commerce.com/wp-content/uploads/aircraft-commerce-docs1/Aircraft%20guides/CFM56-7B/ISSUE58_CFM56_7B_MTCE.pdf
12. Aircraft Commerce, Maintenance & Engineering, Issue 120, October/November 2018. https://www.aircraft-commerce.com/sample_article_folder/120_MTCE_B.pdf
13. Aircraft Value News, "Engine life limited parts pricing continues to rise: $4m for CFM56-7", November 2019. https://www.aircraftvaluenews.com/engine-life-limited-parts-pricing-continues-to-rise-4m-for-cfm56-7
14. AviTrader, "Effective engine LLP management", 23 April 2026. https://avitrader.com/2026/04/23/effective-engine-llp-management/
15. Aviation Fleet Support, "All CFM56-5B & -7B Core LLP Package 6235 CR", undated listing. https://aviationfleetsupport.com/parts-category/cfm56-5b-7b-core-llp-package-6235-cr/
16. MyAirTrade, Engine status resource (LLPC $m 5.700, June 2025). https://www.myairtrade.com/resources/enginestatus
17. Safe Fly Aviation (consultancy blog, 2026): "What determines aircraft engine overhaul costs?" https://safefly.aero/blog-aircraft-engine-overhaul-cost-drivers/ ; "CFM56-7B engine availability report 2026" https://safefly.aero/cfm56-7b-engine-availability-report/ ; "Engine Shop Visit Costs Worldwide 2026" https://safefly.aero/?p=15606 ; "CFM56 Engine Market Report 2026" https://safefly.aero/cfm56-engine-market-report-2026/
18. FlightGlobal, "CFM56 overhaulers see light at end of tunnel", date not shown. https://www.flightglobal.com/mro/cfm56-overhaulers-see-light-at-end-of-tunnel/142974.article
19. ePlaneAI, "Behind the numbers: maintenance insights on the CFM56-7B engine", undated. https://www.eplaneai.com/news/behind-the-numbers-maintenance-insights-on-the-cfm56-7b-engine
20. GE Aerospace, "1 billion flight hours: 'World-class experience' builds 15,000th CFM56-7B engine", Paris Air Show 2019. https://www.geaerospace.com/news/articles/manufacturing-paris-airshow-people-product/1-billion-flight-hours-world-class-experience
21. CFM International / GE, "Last CFM56-3 rolls off production line", 1999. https://www.cfmaeroengines.com/press-articles/last-cfm56-3-rolls-off-production-line
22. ISTAT, "CFM International CFM56-5B/-7B" (Aircraft Supporting Assets), undated. https://www.istat.org/ISTAT-Online/ISTAT-Online/Aircraft-Supporting-Assets/ArtMID/1205/ArticleID/1677/CFM-International-CFM56-5B-7B
23. Aviation Business News / AVM (Aviation Maintenance magazine), "Inside the engine MRO supply chain: why repair delays are rising and what's driving them", 2025. https://www.aviationbusinessnews.com/mro/mro-interviews-comments-articles/inside-the-engine-mro-supply-chain-why-repair-delays-are-rising-and-whats-driving-them/
24. GE Aerospace, Bernstein Strategic Decisions Conference presentation, 27 May 2026. https://www.geaerospace.com/sites/default/files/geaerospace_bernstein_strategic_decisions_conference_presentation_052726.pdf
25. CFM International, "100th CFM56-5C-powered Airbus A340 delivered", undated. https://www.cfmaeroengines.com/press-articles/100th-cfm56-5c-powered-airbus-a340-delivered
26. Safran, "2017 CFM orders surpass 3,300 engines", 6 February 2018. https://www.safran-group.com/pressroom/2017-cfm-orders-surpass-3300-engines-2018-02-06-0
27. StandardAero, CFM56-7B engine services brochure, October 2022. https://standardaero.com/wp-content/uploads/2022/10/StandardAero-CFM56-7B-Engine.pdf
28. ISTAT, Jetrader, July/August 2010, p.16 (half-life definition). https://www.nxtbook.com/nxtbooks/naylor/ISTS0410/index.php?startid=16
29. VREF, "How do engines affect airplane values", undated. https://vref.com/news/how-do-engines-affect-airplane-values/
30. Aircraft Value News, "Concept of half to full life fluid as aircraft move past mid-life", undated. https://www.aircraftvaluenews.com/concept-of-half-to-full-life-fluid-as-aircraft-move-pass-mid-life/ ; Law Insider, "Maintenance Adjusted CMV (current market value)". https://lawinsider.com/dictionary/maintenance-adjusted-cmv
31. FTAI Aviation Ltd., Form 10-K for FY2025, filed 27 February 2026. https://www.sec.gov/Archives/edgar/data/1590364/000162828026012940/ftai-20251231.htm
32. Salvex, "CFM56-7B27E/B1F engine LLP package, 7,445 cycles remaining", undated listing. https://www.salvex.com/listings/listing_detail.cfm/aucid/183060698/
33. Aviation Week, "Magnetic expects CFM56 market challenges, opportunities in 2024", 2024. https://aviationweek.com/mro/aircraft-propulsion/magnetic-expects-cfm56-market-challenges-opportunities-2024 ; Magnetic Group, "The current state and future of CFM56 USM engine pricing". https://www.magneticgroup.co/the-current-state-and-future-of-cfm56-usm-engine-pricing/
34. Ishka, "Pratt & Whitney mulls further LLP escalation hike", undated. https://www.ishkaglobal.com/News/Article/6978/Pratt-Whitney-mulls-further-LLP-escalation-hike
35. Jurnal Teknik Mesin (Mercu Buana), CFM56-3C1 EGT margin analysis, June 2023. https://publikasi.mercubuana.ac.id/index.php/jtm/article/download/16716/7018
36. Aircraft Commerce, Maintenance & Engineering, Issue 27, 2003 (EGT margin mechanics). https://aircraft-commerce.com/wp-content/uploads/aircraft-commerce-docs1/Maintenance/2003/ISSUE%2027-MTCE-A.pdf
37. Leeham News, Bjorn's Corner, "Aircraft engine maintenance, Part 3", 17 March 2017. https://leehamnews.com/2017/03/17/bjorns-corner-aircraft-engine-maintenance-part-3/
38. Aircraft Commerce, Maintenance & Engineering, Issue 70, 2010 (V2500 shop-visit costs, IAE shareholding). https://aircraft-commerce.com/wp-content/uploads/aircraft-commerce-docs/Maintenance/2010/ISSUE70_MTCE_B.pdf
39. Aircraft Value News, "PMA continues to undermine full-life maintenance adjustments", undated. https://www.aircraftvaluenews.com/pma-continues-to-undermine-full-life-maintenance-adjustments/
40. Aviation Suppliers Association, J. Dickstein, 8130-3 workshop, 28 June 2016. https://www.aviationsuppliers.org/ASA/files/ccLibraryFiles/Filename/000000001650/2016-06-28WorkshopLrev2-JDickstein.pdf ; Aviation Suppliers Association (ASA) Member Bulletin, May 2016. https://www.aviationsuppliers.org/ASA-Member-Bulletin---May-2016---Aircraft-Articles-and-Eligibility-for-an-Export-8130-3-tag
41. Aviation Business News, "The evolution of airworthiness documentation for aircraft parts", undated. https://www.aviationbusinessnews.com/in-depth/the-evolution-of-airworthiness-documentation-for-aircraft-parts/
42. Aviation Maintenance magazine, "8130-3 airworthiness approvals: identifying incorrectly issued tags", undated. https://avm-mag.com/?p=39314
43. Civil Aviation Safety Authority (Australia), AD 2014-0130 (CFM56). https://services.casa.gov.au/airworth/airwd/ADfiles/TURBINE/CFM56/2014-0130.pdf
44. MRO Global, "Safair expands GE's TrueChoice overhaul agreement for CFM56 engines", undated. https://www.mroglobal-online.com/safair-expands-ges-truechoice-overhaul-agreement-cfm56-engines/
45. MTU Aero Engines, "MTU Maintenance completes 7,000th shop visit for a V2500-A5 engine", 2025. https://www.mtu.de/newsroom/press/latest-press-releases/press-release-detail/mtu-maintenance-completes-7000th-shop-visit-for-a-v2500-a5-engine/
46. Aviation Week, "Data tool: the future of IAE V2500 engine", 2023. https://ngstage.aviationweek.com/mro/aircraft-propulsion/data-tool-future-iae-v2500-engine
47. Leeham News, "GE's LEAP engines shipped today should match durability of the venerable CFM56, company says", 27 May 2026. https://leehamnews.com/2026/05/27/ges-leap-engines-shipped-today-should-match-durability-of-the-venerable-cfm56-company-says/
48. Visual Approach, "Wave of early LEAP-1A/1B shop visits frustrating operators", undated. https://visualapproach.io/wave-of-early-leap-1a-1b-shop-visits-frustrating-operators/
49. InsideFlyer / ePlaneAI, "CFM upgrade doubles LEAP engine life in harsh climates" (LEAP-1A HPT durability kit certification), undated. https://www.insideflyer.com/posts/cfm-upgrade-doubles-leap-engine-life-in-harsh-climates/
50. Aviation Week, "Parts Price Hikes Help Boost Safran, GE Aftermarket Sales", late 2023. https://ngtest.aviationweek.com/mro/aircraft-propulsion/parts-price-hikes-help-boost-safran-ge-aftermarket-sales
51. Air Cargo Week, "The true cost of engine maintenance", 2025/26. https://aircargoweek.com/the-true-cost-of-engine-maintenance/
52. Leeham News, Bjorn Fehrm, "Bjorn's Corner: Aircraft engine maintenance, Part 1", 3 March 2017. https://leehamnews.com/2017/03/03/bjorns-corner-aircraft-engines-maintenance-part-1/
53. Bain & Company, "Get a step ahead of the engine maintenance capacity crunch", 2024. https://bain.com/globalassets/noindex/2024/bain_brief_get_a_step_ahead_of_the_engine_maintenance_capacity_crunch.pdf
54. General Electric Co. (GE Aerospace), Form 10-K for FY2025, filed February 2026. https://www.sec.gov/Archives/edgar/data/40545/000004054526000008/ge-20251231.htm
55. Oliver Wyman, "The new MRO supply paradigm", April 2026. https://www.oliverwyman.com/our-expertise/insights/2026/apr/aviation-mro-labor-and-material-supply-chain-paradigm.html
56. RTX / Pratt & Whitney, release for IAE AG (IAE's Swiss corporate entity), "IAE AG and FTAI Aviation Sign Strategic V2500 Engine Maintenance Services Agreement", 6 June 2024. https://www.rtx.com/prattwhitney/newsroom/news/2024/06/06/iae-ag-and-ftai-aviation-sign-strategic-v2500-engine-maintenance-services-agreem
57. Aviation Week, "CFM56 Overhaul Demand Remains Strong, GE Aerospace Says", 2026. https://aviationweek.com/mro/aircraft-propulsion/cfm56-overhaul-demand-remains-strong-ge-aerospace-says
58. Aviation Week, "CFM Aftermarket Shifting To Long-term Agreements, Safran Says", c. 2023/24. https://aviationweek.com/mro/aircraft-propulsion/cfm-aftermarket-shifting-long-term-agreements-safran-says
59. Aviation Week, "Safran Sees Leap Aftermarket Emerging By Mid-Decade", c. 2023/24. https://ngtest.aviationweek.com/mro/aircraft-propulsion/safran-sees-leap-aftermarket-emerging-mid-decade
60. GE Aerospace Investor Relations, "Recent events: your questions answered", 2026. https://www.geaerospace.com/news/investor-relations/ir-updates/recent-events-your-questions-answered
61. IBA, "Engine Values Release September 2025 (2025B)", September 2025. https://www.iba.aero/resources/articles/engine-values-2025b-release-september-2025/
62. IBA, "IBA Engine and Lease Rate Update – H1 2026", 2026. https://www.iba.aero/resources/articles/iba-engine-and-lease-rate-update-h1-2026/
63. IBA, "It's a 'Lessors' Market' says IBA, as engine lease rates and market values escalate", April 2024. https://www.iba.aero/about/news/itandrsquos-a-andldquolessorsandrsquo-marketandrdquo-says-iba-as-engine-lease-rates-and-market-values-escalate/ ; AviTrader, "IBA says it's a lessor's market", 25 April 2024. https://avitrader.com/2024/04/25/iba-says-its-a-lessors-market/ ; AJOT (American Journal of Transportation), same, April 2024. https://www.ajot.com/news/its-a-lessors-market-says-iba-as-engine-lease-rates-and-market-values-escalate
64. Mark Calver, Cargo Facts Session 3 presentation, April 2023. https://cargofactsevents.com/wp-content/uploads/2023/04/Mark-Calver-Session-3-Presentation.pdf
65. Aircraft Commerce, Issue 87 maintenance article, 2013. https://www.aircraft-commerce.com/wp-content/uploads/aircraft-commerce-docs/Maintenance/2013/ISSUE87_MTCE_B.pdf
66. Aviation Week, "MRO Memo: A Seller's Market For Used Parts", date not captured. https://aviationweek.com/mro/workforce-training/mro-memo-sellers-market-used-parts
67. ePlaneAI, "CFM56 engine values highlight investor opportunities and risks", date not captured. https://www.eplaneai.com/news/cfm56-engine-values-highlight-investor-opportunities-and-risks
68. Aviation Business News, "CFM56 turbofan aircraft engine" (24,000 in service, September 2025). https://www.aviationbusinessnews.com/low-cost/cfm56-turbofan-aircraft-engine/
69. Leeham News, "GE Aerospace FY and Q4 2025 Earnings Thrust Higher Propelled by Services Growth, LEAP Volume and Expanding Margins", 22 January 2026. https://leehamnews.com/2026/01/22/ge-aerospace-fy-and-q4-2025-earnings-thrust-higher-propelled-by-services-growth-leap-volume-and-expanding-margins/
70. Aviation Week, "Pratt & Whitney Sees High-Single-Digit MRO Growth This Year", 2026. https://aviationweek.com/mro/aircraft-propulsion/pratt-whitney-sees-high-single-digit-mro-growth-year
71. MarketIntelo, "V2500 MRO Market Research Report 2034" (low-grade market-research page). https://marketintelo.com/report/v-mro-market
72. CFM International / Safran / GE Aerospace, "CFM secures certification for LEAP-1B durability upgrades", 18 July 2026. https://www.cfmaeroengines.com/press-articles/cfm-secures-certification-for-leap-1b-durability-upgrades
73. Aviation Week, "Leap Aftermarket Poised For Growth", date not visible. https://aviationweek.com/mro/supply-chain/leap-aftermarket-poised-growth
74. Safran, FY2025 Results & Investor Update presentation, 13 February 2026. https://www.safran-group.com/download/media/450393
75. HEICO Corporation, Form 10-K for FY ended 31 October 2025, filed December 2025. https://www.sec.gov/Archives/edgar/data/46619/000004661925000082/hei-20251031.htm
76. StandardAero, Inc., Form 10-K for FY2025, filed 2026. https://www.sec.gov/Archives/edgar/data/2025410/000119312526072618/saro-20251231.htm
77. AerSale Corporation, Form 10-K for FY2025, filed 2026. https://www.sec.gov/Archives/edgar/data/1754170/000110465926025574/asle-20251231x10k.htm
78. MTU Aero Engines, "Figures for 2025: MTU stays on course for growth", 24 February 2026. https://www.mtu.de/newsroom/press/latest-press-releases/press-release-detail/figures-for-2025-mtu-stays-on-course-for-growth/
79. Lufthansa Technik, "Lufthansa Technik stable on course for growth" (FY2025 results), early 2026. https://www.lufthansa-technik.com/en/lufthansa-technik-stable-on-course-for-growth-2601a780f4c4031c
80. Chromalloy, "Chromalloy Secures FAA Approval of CFM56 High Pressure Turbine Blade PMA", 30 October 2025. https://www.chromalloy.com/chromalloy-secures-faa-approval-of-cfm56-high-pressure-turbine-blade-pma/
81. In Practise, "FTAI, Chromalloy and CFM56 HPT Blade PMA" (expert interview), undated. https://inpractise.com/articles/ftai-chromalloy-and-cfm56-hpt-blade-pma
82. Web page of weak provenance listing a CFM56-7B HPT blade at about €35,000 (condition unclear), undated. https://g00431067.webhosting.atu.ie/?p=1313
83. MTU Aero Engines, AEROREPORT, "How airlines benefit from engine leasing", undated. https://aeroreport.de/en/aviation/how-airlines-benefit-from-engine-leasing
84. FTAI Aviation Ltd., Q4 and FY2024 results release (QuickTurn Europe capacity, "450 modules (150 engines)"), GlobeNewswire, 26 February 2025. https://www.globenewswire.com/news-release/2025/02/26/3033379/35538/en/
85. FTAI Aviation Ltd., Q2 2026 earnings release (8-K exhibit), 29 July 2026. https://www.sec.gov/Archives/edgar/data/1590364/000162828026050622/ftai6302026earningsrelease.htm
86. Aviation Week, "Retirement Uptick Will Restock Used Engine Parts" (the "roughly every eight years" rule of thumb), date not captured. https://aviationweek.com/air-transport/retirement-uptick-will-restock-used-engine-parts
