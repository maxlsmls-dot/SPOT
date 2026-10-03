---
title: Part IX — FTAI Power
header: FTAI Deep Primer — Part IX
as_of: Research as of 3 October 2026
subtitle: Descriptive reference. Sources are cited inline and listed at the end. Takes no view.
toc: true
---

<div class="part-divider"><div class="pn">Part IX</div><h1>FTAI Power</h1><p>This Part explains FTAI's newest business: the conversion of CFM56 engines into 25-megawatt generator sets for data centers. It covers how a jet engine becomes a stationary power plant, what FTAI has and has not said about its Mod-1 unit, the joint venture that sells it and the $1.465 billion order it has booked, the market and the turbine shortage it sells into, the competing machines, the permitting and grid-connection rules that govern deployment, and the arithmetic that connects all of it to the CFM56 fleet described in Parts I and III. A reader who finishes it will be able to read a gas-turbine order announcement, a heat-rate claim and a dollars-per-kilowatt comparison with every term understood.</p></div>

### Translation-table rows answered

Part III §24 turns each documented driver into a requirement on the aftermarket. This Part answers the rows that create a requirement for on-site electrical power rather than for engine maintenance: the row on data-center electricity demand (Part III §24, row: data-center power demand) and the row on the multi-year shortage of new gas turbines (Part III §24, row: gas-turbine shortage). It also bears on two rows it does not answer but draws from. The row on low CFM56 retirements (Part III §24, row: low CFM56 retirements) sets the supply of retired engines from which Mod-1 units are built, and the row on the CFM56 plateau and later decline (Part III §24, row: CFM56 plateau-then-decline) describes when that supply is expected to grow. FTAI Power is unusual in this primer. Every other segment turns the installed base into maintenance demand. This one removes engines from the installed base permanently, so it sits on the same side of the ledger as retirement and teardown (Part I §2.3; Part V §33).

## 68. Gas-turbine generator sets and the aeroderivative, functionally

Part I §1 explained what a turbofan does: it squeezes air, burns fuel in it, and uses the hot gas to spin turbines that turn a large fan, and the fan does most of the pushing. The hot middle of that engine, the core or gas generator (Part I §1), is a machine for making a stream of hot, high-pressure gas. In an aircraft the stream is spent on thrust. On the ground the same stream can be spent on turning a shaft at constant speed, and a shaft turning at constant speed is what an electrical generator needs. That is the whole idea of an aeroderivative, and this section builds it up one component at a time.

### 68.1 What a gas-turbine generator set is

<div class="defn"><b>Gas turbine; gas generator</b><p>A gas turbine is a rotating engine that compresses air, burns fuel in the compressed air and expands the hot gas through turbine stages. The compressor, the combustor and the turbine that drives the compressor together form the gas generator: the assembly whose only product is hot, pressurised gas. In a jet engine that gas leaves through a nozzle and the reaction pushes the aircraft. In a power plant it is expanded through a further turbine that turns a shaft. Part I §1 boxed the core of the CFM56; the core is the gas generator of this Part. <span class="cite">[D8 §2.1; Part I §1]</span></p></div>

<div class="defn"><b>Generator set (genset)</b><p>A generator set is the complete unit that turns fuel into electricity: the prime mover (a gas turbine or a piston engine), the output turbine where there is one, a gearbox if the shaft speed must be changed, the electrical generator itself, and the surrounding fuel, air-intake, exhaust, lubrication, fire-protection and control systems, assembled and tested as one product. The J&F order of July 2026 is for "Mod-1 mobile gas turbine generator sets", so the thing FTAI's venture sells is the whole unit, not a bare turbine. <span class="cite">[D8 §2.1; FTAI release, 22 Jul 2026]</span></p></div>

<div class="defn"><b>Units of power, energy and gas used in this Part</b><p>A watt is a rate of energy flow; a megawatt (MW) is a million watts and a gigawatt (GW) is a thousand megawatts. Mod-1 is rated at 25 MW and GE Vernova's order book is measured in gigawatts. A kilowatt-hour (kWh) is one kilowatt sustained for one hour, a megawatt-hour (MWh) is a thousand of those, and a terawatt-hour (TWh) is a billion kWh; electricity consumption is measured in these. A British thermal unit (Btu) is a unit of heat; a million Btu is written MMBtu, and natural gas is priced in dollars per MMBtu. Gas volumes are given in cubic feet: a million cubic feet is MMcf, a billion is Bcf, and a daily flow is MMcf/d or Bcf/d. Pipeline gas carries roughly 1,000 Btu per cubic foot, which is the conversion the fuel-burn example below uses. <span class="cite">[D8 §2.3; definitions from first principles]</span></p></div>

Three families of machine compete to supply on-site power at data centers, and a fourth that is not a machine in the same sense. The first is the purpose-built stationary gas turbine, which the industry calls a frame or heavy-duty machine.

<div class="defn"><b>Frame (heavy-duty) gas turbine</b><p>A frame turbine is a gas turbine designed from the start to sit on a foundation and make power, typically 50 to 600 MW per unit, heavy, and built in a factory for a delivery slot years ahead. The industry labels its generations by letter: the F-, H- and J-class machines of GE Vernova, Siemens Energy and Mitsubishi Power are the large frames whose order books are described in §71.3. The size range and the classification are general industry knowledge that the research did not separately source. <span class="cite">[D8 §2.1]</span></p></div>

The second family is the aeroderivative, which §68.2 builds up in detail. The third and fourth are the alternatives Mod-1 competes with in §72.

<div class="defn"><b>Reciprocating engine; solid-oxide fuel cell</b><p>A reciprocating engine is a piston engine. Large natural-gas versions of roughly 1 to 23 MW each are arranged in halls of many units; Wärtsilä describes data-center plants built from 10 to 23 MW engines reaching more than 450 MW per site, with electrical efficiency that "can exceed 50%" and "20–35% less fuel than gas turbines", both vendor claims. A solid-oxide fuel cell converts natural gas to electricity electrochemically, without combustion; Bloom Energy is the supplier the research reached, and its annual report positions the product against reciprocating engines on power density and emissions. No output or price figures for fuel cells were captured. <span class="cite">[Wärtsilä product page, undated; Bloom Energy 10-K FY2024; D8 §2.1, U9]</span></p></div>

Two more pairs of words recur in every turbine order announcement and need plain definitions before they are used.

<div class="defn"><b>Simple cycle and combined cycle; baseload, backup and peaking</b><p>A gas turbine run on its own, with its exhaust heat discarded, is in simple cycle. A combined-cycle plant adds a boiler that recovers the exhaust heat to raise steam for a second, steam-driven turbine, which raises the plant's efficiency but adds years to construction and is only built at frame scale. Mod-1 is a simple-cycle machine. Baseload duty means running continuously; backup means standing by for an outage; peaking means running only in the hours of highest demand. FTAI described Mod-1 as usable for all three. These definitions are from first principles; the research used the terms without defining them. <span class="cite">[D8 §2.1, §2.3; registry section 2]</span></p></div>

### 68.2 How a turbofan becomes an aeroderivative, functionally

The CFM56 is a high-bypass turbofan with two spools (Part I §1). The low-pressure spool carries the fan, a small booster compressor and the low-pressure turbine (LPT) at the back. The high-pressure spool carries the high-pressure compressor (HPC), the combustor and the high-pressure turbine (HPT), and it is the gas generator. On the aircraft, most of the low-pressure turbine's work goes into spinning the fan, and most of the fan's air goes around the core to make thrust. For a power plant, thrust is unwanted and the fan is dead weight. The published conversion recipe, described generically in a US patent on converting turbofans, has five steps. <span class="cite">[US patent 11,053,891, "Method for converting a turbofan engine"; D8 §2.2]</span>

<div class="exh"><div class="exh-title">Exhibit 9.1 — Turning a turbofan into an aeroderivative generator set: the five functional steps</div>

| Step | What is removed or added | Why | Source |
|---|---|---|---|
| 1 | Remove the fan and the bypass duct; add one or two compressor stages ("stage 00 and stage 0") in front of the existing booster | Thrust is no longer wanted; the small extra compressor replaces the fan's job of feeding the core with air at the pressure it was designed for | US patent 11,053,891 |
| 2 | Replace the exhaust nozzle with a power turbine, or use the engine's own low-pressure turbine as the output turbine | The hot gas must turn a shaft instead of pushing the aircraft; a free power turbine on its own shaft lets the gas generator run at its own speed while the output shaft holds generator speed | US patent 11,053,891; the LM6000 (GE's aeroderivative built on the CF6-80C2) uses its own low-pressure spool (general industry knowledge) |
| 3 | Add a gearbox where the output shaft spins faster than the generator needs | A 60 Hz grid needs a two-pole generator at 3,600 rpm or a four-pole at 1,800 rpm; aeroderivative shafts commonly spin faster | US patent 6,895,325 |
| 4 | Add the electrical generator | "Rotation of the generator's input shaft and windings produces electric power" | US patent 6,895,325 |
| 5 | Add the stationary systems: natural-gas fuel nozzles and controls, air-inlet filter house, exhaust stack and silencing, emissions after-treatment where required, lubrication and cooling, fire suppression, and a control system for start-up, load-following and protection, all inside an enclosure on a trailer or skid | The aircraft engine burned kerosene in clean air at altitude; the ground unit burns pipeline gas in dirty air and must meet an air permit | General industry knowledge; FTAI has published no Mod-1 bill of materials |

<cite>Source: US Patent and Trademark Office, US 11,053,891 "Method for converting a turbofan engine" and US 6,895,325 "Overspeed control system for gas turbine electric powerplant"; D8 §2.2. Which of the step-2 arrangements Mod-1 uses, and whether a booster stage replaces the fan, is undisclosed (D8 U3).</cite></div>

<div class="defn"><b>Aeroderivative</b><p>An aeroderivative is an aircraft engine adapted to drive a shaft for stationary use. The fan and bypass duct are removed and extra compressor stages replace the fan; the exhaust nozzle is replaced by a power turbine, or the engine's own low-pressure turbine is used; a gearbox and a generator are fitted; and the kerosene fuel system is changed for gas. Aeroderivatives are typically 5 to 100 MW, light, modular, fast to start and fast to install, and the patent literature describes the aero gas generator as "more efficient in mid-range power than heavy-duty gas turbine". The examples in this Part are GE's LM2500 (25 to 35 MW) and LM6000 (about 48 to 50 MW), ProEnergy's PE6000 (48 MW) and FTAI's Mod-1 (25 MW). The LM2500 was built on the TF39 (a GE military turbofan) and its civil relative the CF6-6, the LM6000 on the CF6-80C2, and the PE6000 on CF6-80C2 cores taken from retired 747 engines. <span class="cite">[US patents 11,053,891 and 5,160,080; D8 §2.1–2.2, §3]</span></p></div>

Step 1 deserves a sentence more. The patent's words are: "In case of fan jet designs, the fan is removed and a couple of stages of compression are added in front of the existing low-pressure compressor, these additional stages usually known as stage 00 and stage 0". <span class="cite">[US patent 11,053,891]</span> The core was designed to receive air that the fan had already compressed a little. Take the fan away and the core would be starved. So a small compressor goes where the fan was. It does a fraction of the fan's work, because it only has to feed the core and not push a bypass stream.

Step 2 is where the two established designs differ, and where Mod-1's design is unknown.

<div class="defn"><b>Free power turbine (FPT)</b><p>A free power turbine is an output turbine on its own shaft, not mechanically connected to the gas generator; it is driven only by the gas stream, which the patent calls "aerodynamically coupled". Because the two shafts are independent, the gas generator can speed up and slow down with load while the output shaft holds the fixed speed a generator needs. The alternative is to keep the engine's own low-pressure turbine and let its spool drive the generator, which is how the LM6000 works. FTAI has not said which arrangement Mod-1 uses. The acronym is this primer's, not FTAI's. <span class="cite">[US patent 11,053,891; D8 §2.2, U3]</span></p></div>

<div class="defn"><b>Gearbox (genset)</b><p>A genset gearbox is the speed reducer between the turbine's output shaft and the generator. A generator synchronised to a 60 Hz grid must turn at 3,600 rpm with two poles or 1,800 rpm with four, and aeroderivative output shafts commonly spin faster, so "an external gearbox is typically required to obtain the proper input speed to a generator". It is a different device from the engine's accessory gearbox boxed in Part I §3. <span class="cite">[US patent 6,895,325; D8 §2.2]</span></p></div>

Step 5 is the part of the recipe that is not engine work at all, and it is the part FTAI's partner brings.

<div class="defn"><b>Balance of plant; packaging</b><p>The balance of plant is everything around the turbine that a stationary power unit needs: the enclosure, the trailer or skid, the generator and gearbox, the air-inlet filter house, the exhaust and silencing, the gas fuel skid, lubrication and cooling, fire suppression and the control system. Building, integrating and testing all of that around a bare engine is what the industry calls packaging. FTAI describes its venture with Jereh Group as a "packaging and distribution" joint venture and Jereh as "a global leader in gas turbine mobile packaging", so this is the work Jereh contributes (§70). <span class="cite">[D8 §2.2, §2.7; FTAI Q1 2026 release, 29 Apr 2026; FTAI 10-Q Q2 2026]</span></p></div>

Two terms inside that list need a gloss. Load-following means changing output to track the customer's demand minute by minute; a data center's load is not constant, and the control system must raise and lower the turbine's fuel flow to match it. Switchgear is the customer's set of breakers and busbars into which the genset's electrical output is connected. Neither term is defined in the research; both are given here from first principles.

### 68.3 What "mobile" means

<div class="defn"><b>Mobile generator set</b><p>A mobile generator set is one built onto a road trailer or a skid so that it can be driven to a site, connected to a gas supply and to the customer's switchgear, commissioned in days or weeks, and later moved. The J&F order is for "mobile gas turbine generator sets", and FTAI has cited about two weeks to deploy a Mod-1 on site. Mobility matters twice: for speed, because the unit arrives finished and tested, so site work is a pad, a gas line and an electrical tie-in rather than a construction project; and for regulatory treatment, because US air rules distinguish stationary sources from "nonroad engines" (§73.2). <span class="cite">[FTAI release, 22 Jul 2026; TheValueist summary of the Q4 2025 call, 26 Feb 2026, call coverage; D8 §2.4]</span></p></div>

The connection to a gas supply is itself a project. A pipeline lateral is the branch line that runs from a transmission pipeline to the plant, with metering sized for the plant's flow; S&P Global reported in May 2026 that pipeline operators were striking deals "as data centers turn to colocated generation". <span class="cite">[S&P Global Commodity Insights, 27 May 2026]</span> The fuel-burn example below shows why the lateral matters: a single 25 MW unit at high load draws about 4.9 million cubic feet of gas a day.

### 68.4 Heat rate and efficiency

Every power-plant comparison in this Part runs through one number, and it is worth defining with care.

<div class="defn"><b>Heat rate</b><p>The heat rate is the fuel energy a plant needs to make one kilowatt-hour of electricity, in Btu per kWh. One kWh is 3,412 Btu of energy, so a plant's efficiency is 3,412 divided by its heat rate. A lower heat rate is better. FTAI's stated figure for Mod-1 is "about 9,000", which is 37.9% efficient and sits inside the 35–40% band FTAI also stated; a 50%-efficient reciprocating engine has a heat rate of about 6,824. The heat rate converts directly into fuel cost per MWh once a gas price is chosen. <span class="cite">[TheValueist summary of the Q4 2025 call, 26 Feb 2026, and Aviation Week's MRO Memo column (MRO means maintenance, repair and overhaul), early 2026, both call coverage; D8 §2.3]</span></p></div>

<div class="defn"><b>Lower heating value (LHV) and higher heating value (HHV)</b><p>A fuel's energy content can be stated on two bases. The higher heating value counts the heat recovered by condensing the water vapour in the exhaust; the lower heating value does not. Gas-turbine efficiencies are conventionally quoted on the lower basis, which gives a figure a few percentage points higher than the same machine on the higher basis. FTAI has not said which basis its 35–40% and 9,000 figures use, and they are mutually consistent only if both are on the same basis. <span class="cite">[D8 §2.3, T8, U5]</span></p></div>

<div class="defn"><b>Capacity factor</b><p>The capacity factor is a plant's actual output over a period divided by what it would have produced running at full load for the whole period. A unit that ran flat out all year would have a factor of 100%; the fuel-burn example below uses 90% as an assumption for a baseload data-center unit. <span class="cite">[D8 §2.3]</span></p></div>

<div class="worked"><div class="h">Worked example 9.1 — What a heat rate of 9,000 means in fuel</div>
<p>Inputs: heat rate about 9,000 Btu/kWh and efficiency 35–40% (sourced: call coverage of the Q4 2025 call, 26 Feb 2026, basis not stated); output 25 MW (sourced: FTAI launch release, 30 Dec 2025); capacity factor 90% (assumed); 1,000 Btu per cubic foot of pipeline gas (assumed, a standard approximation); gas price $3.50 per MMBtu (assumed, illustrative, not a forecast); reciprocating-engine efficiency "can exceed 50%" (sourced: Wärtsilä product page, a vendor claim).</p>
<div class="eqblock">efficiency = 3,412 ÷ 9,000 = 37.9%
fuel at full load = 25,000 kW × 9,000 Btu/kWh = 225,000,000 Btu/h = 225 MMBtu per hour
annual output = 25 MW × 8,760 h × 0.90 = 197,100 MWh
annual fuel = 197,100 MWh × 9 MMBtu/MWh = 1,773,900 MMBtu ≈ 1.77 million MMBtu
annual gas ≈ 1.77 Bcf; daily gas = 1.77 Bcf ÷ 365 ≈ 4.9 MMcf/d
fuel cost per MWh at $3.50 = 9 × 3.50 = $31.50
reciprocating engine at 50%: heat rate = 3,412 ÷ 0.50 = 6,824; fuel cost = 6.824 × 3.50 = $23.90 per MWh
gap = 31.50 − 23.90 = $7.60 per MWh; over 197,100 MWh ≈ $1.5 million a year per unit</div>
<p>So one Mod-1 at 90% load burns about 1.77 Bcf of gas a year, or 4.9 MMcf a day, and 100 units would draw about 0.49 Bcf/d, a figure §71.2 sets against the market-wide forecasts. The $7.60 per MWh gap is the fuel penalty a turbine buyer accepts against a 50%-efficient piston plant at this gas price, in exchange for a smaller footprint, fewer units per MW and faster delivery; at a higher gas price the gap widens in proportion. Limits of the example: the capacity factor and the gas price are assumptions; the heat rate comes from call coverage, not a filing, and its heating-value basis is unstated; the 50% figure is a vendor's claim; and the $1.5 million line is derived in this Part, not published. <span class="cite">[D8 §2.3; Wärtsilä product page, undated; reconciliation D8 T8, T10]</span></p></div>

### 68.5 Emissions treatment

Burning natural gas in a turbine produces nitrogen oxides, carbon monoxide and carbon dioxide. Air permits (§73.1) set limits on the nitrogen oxides in particular, because they form smog near the ground.

<div class="defn"><b>Nitrogen oxides (NOx); selective catalytic reduction (SCR)</b><p>Nitrogen oxides are the pollutant that air permits limit most tightly for gas turbines. A turbine can meet a limit three ways: with a combustor designed to burn at a lower flame temperature (a low-NOx combustor), by injecting water or steam into the combustor to cool the flame, or with selective catalytic reduction, a catalyst box in the exhaust that converts the oxides to nitrogen using ammonia or urea. The permit for xAI's Memphis turbines allowed them "with certain emissions controls". FTAI has not published Mod-1's NOx level or its after-treatment. <span class="cite">[TechCrunch, 3 Jul 2025; D8 §2.6, U5]</span></p></div>

Whatever after-treatment a customer's permit requires sits in the balance of plant, so it falls within the packaging scope that Jereh contributes; the research recorded this as a presumption from the division of labour, not a confirmed fact. <span class="cite">[D8 §2.6]</span>

### 68.6 The precedents, and the one that was not found

Converting an aircraft engine into a stationary power unit is an old practice, and the lineage matters because it tells the reader what has been done before with which cores.

<div class="exh"><div class="exh-title">Exhibit 9.2 — Aeroderivative lineage: which aircraft engine each stationary unit came from</div>

| Stationary unit | Maker | Aircraft engine it derives from | Output class | How the derivation is sourced |
|---|---|---|---|---|
| LM2500 | GE | TF39 (a GE military turbofan) and CF6-6 (the related civil engine) | 25–35 MW; the LM2500XPRESS variant is rated 35 MW | General industry knowledge in the research; the 35 MW rating from GE Vernova's release of 22 Jul 2025 |
| LM6000 | GE | CF6-80C2; the engine's own low-pressure spool drives the generator | About 48–50 MW | General industry knowledge; output class from EEPower and Data Centre Magazine |
| PE6000 | ProEnergy (private, non-OEM) | CF6-80C2 cores taken from retired Boeing 747 engines, "the same engine core GE Vernova uses in its LM6000" | 48 MW | Data Centre Magazine; EEPower |
| Mod-1 | FTAI Power (non-OEM) | CFM56; variant (-5B or -7B) not disclosed | 25 MW | FTAI launch release, 30 Dec 2025; Aviation Week MRO Memo, early 2026 |
| Prior production CFM56 stationary derivative | None found | The research searched for one and found none; trade press frames Mod-1 as the CFM56's first such role | — | D8 §2.2, U13; AvioRadar, 2026; AviTrader, 2 Jan 2026 |

<cite>Source: GE Vernova, Crusoe release, 22 Jul 2025; Data Centre Magazine, "Can Old Aeroplane Engines Powering Data Centres Take Off?", undated; EEPower, "Can repurposed jet engines solve AI data center power problems?", undated; FTAI Aviation, launch release, 30 Dec 2025; AvioRadar, 2026; AviTrader, 2 Jan 2026; D8 §2.2 and §3. Lineage rows marked "general industry knowledge" were not separately sourced in the research.</cite></div>

Two points in that table carry weight later. First, every established aeroderivative in the 25 to 50 MW class is built on one gas generator per unit; the research's feedstock arithmetic in §74.3 rests on the assumption that Mod-1 is too. Second, ProEnergy is the closest analogue to FTAI Power: a company outside the original equipment manufacturers (OEMs), the firms that hold the engine's design (Part I §2), that buys retired airline cores and packages them for data-center power, with 2027 delivery. <span class="cite">[Data Centre Magazine, undated; EEPower, undated; D8 §3]</span> The research found no production stationary derivative of the CFM56 before Mod-1 and recorded that a definitive statement from GE or CFM, or Gas Turbine World's handbook, would settle whether Mod-1 is the first. <span class="cite">[D8 U13]</span>

## 69. Mod-1 as FTAI describes it

This section gives FTAI's own description of the product, separates what came from a filing or release from what came from third-party coverage of an earnings call, and then lists what has not been said.

### 69.1 The launch release, 30 December 2025

FTAI announced FTAI Power on 30 December 2025 as a platform "focused on converting CFM56 engines to power turbines built to provide the most flexible, cost efficient and scaled solution for delivering reliable energy to data centers globally". <span class="cite">[FTAI release, 30 Dec 2025]</span> The release said that "the aeroderivative adapted from the CFM56 engine will provide the market with a 25-megawatt unit that offers grid operators greater flexibility and finer output control than larger units", that production was "expected to begin in 2026", and that FTAI Power "is expected to have the capacity to deliver over 100 units annually and provide service support solutions that maximize uptime by applying its modular maintenance model to power turbines". <span class="cite">[FTAI release, 30 Dec 2025]</span> It positioned FTAI "as one of the largest aftermarket maintenance providers and owners of the CFM56 engine", which is the Aerospace Products business of Part VII and the Leasing fleet of Part VIII. The FY2025 annual report records the launch in its business description. <span class="cite">[FTAI 10-K FY2025]</span>

### 69.2 The call descriptions, February 2026

The technical figures come from the fourth-quarter 2025 earnings call of 26 February 2026, which the research reached only through a third-party summary on X and through Aviation Week's coverage, not through a transcript. <span class="cite">[TheValueist, 26 Feb 2026, call coverage; Aviation Week MRO Memo, early 2026; D8 U15]</span> As summarised, management described Mod-1 as 25 MW and trailer-mounted, taking about two weeks to deploy on site, usable for baseload, backup or peaking; as 35–40% efficient at a heat rate of about 9,000, "comparable to other aeroderivatives sold over the past 30 to 40 years"; as giving the engine a second life of 10 to 20 years in power service; and as having "an unmatched turbine input cost, given access to near-fully depreciated CFM56 assets". <span class="cite">[TheValueist, 26 Feb 2026, call coverage; Aviation Week MRO Memo, early 2026]</span> Aviation Week noted that which CFM56 variant, the -5B or the -7B, is used was not disclosed; FTAI's aerospace business works on both. <span class="cite">[Aviation Week MRO Memo, early 2026; FTAI 10-K FY2025]</span>

<div class="defn"><b>Mod-1 (FTAI Mod-1; CFM56 aeroderivative)</b><p>Mod-1 is FTAI Power's 25 MW trailer-mounted natural-gas generator set built around a CFM56 core. FTAI launched the platform on 30 December 2025 and describes the unit as 35–40% efficient at a heat rate of about 9,000 Btu/kWh, deployable in about two weeks, usable for baseload, backup or peaking, and giving the engine a 10–20-year second life, with an input cost based on "near-fully depreciated" engines; the efficiency, heat rate, deployment time and second-life figures are from call coverage, not a filing. First delivery is targeted by the fourth quarter of 2026, production of 100 units in 2027, and capacity "over 100 units annually". If the $1.465 billion J&F order were 100 units it would imply $14.65 million per unit, or $586 per kW, but the unit count is undisclosed. FTAI's 2027 guidance puts Power's Adjusted EBITDA (earnings before interest, tax, depreciation and amortisation; Part X §80), as FTAI adjusts it, at $450 million; one call summary gives "$450 million to $750 million". Part III §18 glossed the term as a new non-aviation sink for the installed base. <span class="cite">[FTAI release, 30 Dec 2025; Q4/FY2025 release, 25 Feb 2026; Q1 2026 release, 29 Apr 2026; call coverage, 26 Feb 2026 and 30 Jul 2026; D8 §1, §2.3, §2.9]</span></p></div>

<div class="exh"><div class="exh-title">Exhibit 9.3 — Mod-1 as FTAI describes it: each statement, its date, its source and its level</div>

| Statement | Figure | Date | Source | Level |
|---|---|---|---|---|
| Platform launched | 30 Dec 2025 | 30 Dec 2025 | FTAI release; 10-K FY2025 | Release; filing |
| Unit output | 25 MW | 30 Dec 2025 | FTAI release | Release |
| Annual capacity | "over 100 units annually" | 30 Dec 2025 | FTAI release | Release |
| Production start | "expected to begin in 2026" | 30 Dec 2025 | FTAI release | Release |
| First delivery | "expected to be delivered by Q4 2026" | 25 Feb 2026; repeated 29 Apr 2026 | Q4/FY2025 release; Q1 2026 release (both 8-K exhibits) | Release filed as 8-K exhibit |
| 2027 production | "planned production of 100 units in 2027" | 25 Feb 2026; repeated 29 Apr 2026; 10-Q Q2 2026 "planned 2027 production target of 100 Mod-1 CFM56 aeroderivative units" | Same; 10-Q Q2 2026 | Release; filing |
| Form factor | trailer-mounted, mobile | 26 Feb 2026; 22 Jul 2026 | Q4 2025 call via TheValueist; J&F release | Call coverage; release |
| Deployment time | about two weeks on site | 26 Feb 2026 | Q4 2025 call via TheValueist | Call coverage |
| Duty | baseload, backup or peaking | 26 Feb 2026 | Same | Call coverage |
| Efficiency | 35–40% | 26 Feb 2026 | Q4 2025 call via TheValueist; Aviation Week MRO Memo | Call coverage; trade press |
| Heat rate | about 9,000 (Btu/kWh implied; heating-value basis not stated) | 26 Feb 2026 | Same | Call coverage; trade press |
| Second life | 10–20 years | 26 Feb 2026 | Q4 2025 call via TheValueist | Call coverage |
| Input cost | "near-fully depreciated CFM56 assets" | 26 Feb 2026 | Same | Call coverage |
| Service model | "applying its modular maintenance model to power turbines" | 30 Dec 2025 | FTAI release | Release |
| Module capacity linked to Power | 3,000 modules a year "supporting its 25% market share goal and 100 Mod-1 units annually" | 30 Jul 2026 | Q2 2026 call via GuruFocus, Quartr | Call coverage |
| 2027 Power Adjusted EBITDA | $450M within $2.3B; "$450 million to $750 million" in one summary | 29 Jul 2026 | Q2 2026 release (text confirms "$450 million"); Quartr, MarketBeat; GuruFocus | Release; call coverage |

<cite>Source: FTAI Aviation, "FTAI Aviation Announces the Launch of FTAI Power", GlobeNewswire, 30 Dec 2025; FTAI 10-K FY2025; Q4/FY2025 earnings release, 25 Feb 2026 (8-K ex. 99.1); Q1 2026 earnings release, 29 Apr 2026 (8-K ex. 99.1); FTAI 10-Q for the quarter ended 30 Jun 2026; FTAI release of 22 Jul 2026; TheValueist (X), 26 Feb 2026; Aviation Week, "MRO Memo: FTAI Pitches CFM56 To Power AI Boom", early 2026; GuruFocus, Quartr and MarketBeat summaries of the 29–30 Jul 2026 call; orchestrator notes. Reconciliation R-062 and E.1 rule 2.</cite></div>

The distinction in the last column is the one the reconciliation asks every Part to keep. Where a figure came from a release or a filing it is FTAI's statement. Where it came from a summary of a call, it is a third party's rendering of FTAI's statement, and the research recorded that direct quotations on Power "should be taken from the transcripts before publication". <span class="cite">[D8 U15; E.1 rule 2]</span>

### 69.3 Capacity, first delivery and the 2027 target

The dated sequence is short. The launch release of 30 December 2025 gave capacity for "over 100 units annually". <span class="cite">[FTAI release, 30 Dec 2025]</span> The fourth-quarter 2025 results release of 25 February 2026 said: "Development of FTAI Power continues on-track with first Aeroderivative product, FTAI Mod-1, expected to be delivered by Q4 2026 with planned production of 100 units in 2027", and the first-quarter 2026 release of 29 April 2026 repeated it. <span class="cite">[FTAI Q4/FY2025 release, 25 Feb 2026; Q1 2026 release, 29 Apr 2026]</span> The second-quarter 2026 report of 29 July 2026 added 2027 guidance with a Power line (§74.2) and, on the call the next day, coverage reported module capacity of 3,000 a year "supporting its 25% market share goal and 100 Mod-1 units annually". <span class="cite">[GuruFocus and Quartr, 30 Jul 2026, call coverage]</span> Part VII §49 treats that 3,000 figure as one of four dated capacity statements with different footprints, and this Part uses it only in §74.4 with that label. <span class="cite">[reconciliation R-037; E.1 rule 17]</span>

### 69.4 Second life, input cost and the modular service model

FTAI's aerospace model, described in Part VII §46, holds inventories of serviceable modules and swaps them into a customer's engine so that the engine returns to service quickly. The launch release says FTAI will "provide service support solutions that maximize uptime by applying its modular maintenance model to power turbines". <span class="cite">[FTAI release, 30 Dec 2025]</span> Functionally, when a Mod-1 gas generator reaches an inspection or overhaul point, FTAI would exchange the core, or a module of it, rather than overhaul it in place. That is how aeroderivative operators already achieve high availability: an aircraft-derived core is light enough to be swapped in about a day, whereas a frame turbine is overhauled on its foundation over weeks. <span class="cite">[D8 §2.5]</span> Maintenance intervals, service pricing and the contractual form of the service (a long-term agreement or time and materials) are not disclosed. <span class="cite">[D8 U12]</span>

<div class="defn"><b>Module (FTAI Power usage)</b><p>In this Part a module is counted as FTAI's releases count it: three per engine, the fan, the core and the low-pressure turbine, which is the convention evidenced by "450 modules (150 engines)" and "1,800 modules (600 engines)" in FTAI's release of 26 February 2025. On that convention, 100 Mod-1 units built from 100 whole engines are about 300 module-equivalents a year drawn from the same production as the aftermarket. Part I §3 counts four major modules anatomically, the three above plus the accessory gearbox, and §74.4 shows what the second convention changes. <span class="cite">[FTAI release, 26 Feb 2025, via orchestrator notes; D8 §2.10; reconciliation R-035, B-3; E.1 rule 7]</span></p></div>

The input-cost claim can be set beside the engine values Part I §8 and Part V §32 carry, without converting it into a figure FTAI has not given. "Near-fully depreciated" describes an engine's book value on FTAI's balance sheet, not its market price. The market anchors the research holds are a run-out CFM56-7B, meaning one at the end of its usable life, at $0.8–1.2 million (Safe Fly Aviation, 2026, a consultancy blog), and a half-life market value of $5.7 million for a -7B24 and $6.4 million for a -7B27 from the appraiser IBA (September 2025). <span class="cite">[Safe Fly Aviation, 2026; IBA, Sept 2025; reconciliation C.8 item 5; E.2]</span> FTAI's actual engine input cost per Mod-1, the engines it has earmarked for Power, and the capital the business requires are undisclosed. <span class="cite">[D8 U6]</span> FTAI owned 243 engines in its leasing fleet at 31 December 2025. <span class="cite">[FTAI 10-K FY2025; E.2]</span>

### 69.5 What FTAI has not said

<div class="exh"><div class="exh-title">Exhibit 9.4 — Mod-1: what is disclosed and what is not, with what would resolve each gap</div>

| Question | Disclosed | Not disclosed | What would resolve it | Research id |
|---|---|---|---|---|
| Which CFM56 variant | FTAI works on -5B and -7B (10-K) | Whether Mod-1 uses -5B, -7B or both | A product data sheet; a call statement | D8 U3 |
| Engines per unit | 25 MW per unit | How many gas generators make one unit; one is assumed by analogy with the LM2500 class | Same | D8 U3 |
| Output arrangement | "power turbines" (release) | Free power turbine or the engine's own low-pressure turbine; whether a booster stage replaces the fan | Same; a patent filing | D8 U3 |
| Emissions and fuel | None | NOx level; after-treatment (SCR or not); heating-value basis of the efficiency; dual-fuel capability | An air-permit application for a Mod-1 site | D8 U5 |
| Build location | Jereh is "a global leader in gas turbine mobile packaging" | Where J&F packages units: China, the United States or elsewhere; tariff exposure; whether J&F has its own facility | FTAI or Jereh filings; a site announcement | D8 U4 |
| Service model | "modular maintenance model" (release) | Inspection and overhaul intervals; contract form; service revenue per unit | A service agreement; a call statement | D8 U12 |
| Capital required | None | Power capital expenditure; engines earmarked; test capacity; engine input cost per unit | The 2026 10-Qs' segment and capital notes | D8 U6 |
| Segment reporting | FY2025 10-K has two reportable segments; 2027 guidance has three lines | Whether Power is a third reportable segment from the Q2 2026 10-Q or sits within Aerospace Products until first delivery | The segment note of the Q1 or Q2 2026 10-Q | D8 U7; D10 U-18; cluster K-10 |

<cite>Source: D8 §7 (unknowns U3–U7, U12); FTAI 10-K FY2025; FTAI Q1 2026 release, 29 Apr 2026; reconciliation D.1, D.2 (cluster K-10) and C.8. The orchestrator notes confirm that the FY2025 10-K has two segments and that the 2027 guidance has three lines; they do not resolve the segment question.</cite></div>

The build-location gap has a consequence the research stated plainly: a Chinese build location would expose the gensets to US tariff and trade-policy risk, and a US location would require Jereh to stand up or expand a facility; neither is documented in anything reached. <span class="cite">[D8 §5]</span>

## 70. J&F Power Systems and the $1.465B order

FTAI does not sell Mod-1 to the end customer itself. It sells through a venture with a Chinese oilfield-equipment maker, and the venture is the contracting party on the one order announced so far. This section describes the partner, the venture as each parent describes it, the order's terms, and the customer as each source describes it.

### 70.1 Jereh Group

<div class="defn"><b>Jereh Group (Yantai Jereh Oilfield Services Group Co., Ltd.)</b><p>Jereh is a Chinese maker of oilfield equipment listed on the Shenzhen Stock Exchange (SZSE) under code 002353: drilling and oil-and-gas field engineering equipment, equipment maintenance and parts, oilfield engineering services, natural-gas compressors and gas-turbine generator sets. Its gas-turbine genset research began in 2018, and "in 2020, the first 6MW gas turbine genset in China was successfully applied in the well site". It ships trailer-mounted electric hydraulic-fracturing fleets, whose power comes from gas turbines on trailers, to US oilfield customers. FTAI calls it "a global leader in gas turbine mobile packaging". Its subsidiary GenSystems Power Solutions won a $182 million order (February 2026) and a $341 million order for gas-turbine generators for US data centers, deliverable by end-2027; whether those use Mod-1 or other turbines is not stated. <span class="cite">[PitchBook profile; Jereh company history page; PRNewswire, 2024 and 2025; FTAI Q1 2026 release, 29 Apr 2026; Yicai Global, 2026; D8 §3, §4.2, U8]</span></p></div>

The oilfield lineage is the point. Electric hydraulic fracturing runs large pumps from gas turbines mounted on trailers at a well site, moved from site to site, started and stopped often, and fuelled from field gas. That is the same packaging problem as a mobile data-center genset: an enclosure, a trailer, a generator, a fuel skid, controls and a quick connection. <span class="cite">[D8 §2.7; PRNewswire, 2024 and 2025]</span> The two GenSystems orders show Jereh selling gas-turbine gensets into US data centers on its own account, in parallel with the venture. The megawatt count of those orders, which would give a dollars-per-kilowatt figure, their customer and their relationship to J&F were not captured. <span class="cite">[Yicai Global, 2026; D8 U8]</span>

### 70.2 J&F: two parents, two descriptions

<div class="defn"><b>J&F Power Systems LLC (J&F)</b><p>J&F Power Systems is the entity through which Mod-1 is packaged and sold. FTAI's release of 22 July 2026 calls it "FTAI's joint venture with Jereh Group for packaging and distribution of its Mod-1 aeroderivative gas turbine", and FTAI's 10-Q for the quarter ended 30 June 2026 calls it "a strategic packaging and distribution joint venture with Jereh Group, a global leader in gas turbine mobile packaging, to support the planned 2027 production target of 100 Mod-1 CFM56 aeroderivative units". Jereh's Shenzhen exchange disclosure, as reported by FilingReader on the same day, says "its subsidiary, J&F Power Systems" signed the contract. J&F is the counterparty to a five-year master supply agreement and an initial $1.465 billion purchase order with an unnamed cloud provider. Its ownership split, board control and which parent consolidates it are undisclosed. <span class="cite">[FTAI release, 22 Jul 2026; FTAI 10-Q Q2 2026, via orchestrator notes; FilingReader, 22 Jul 2026; D8 §2.7, U2; reconciliation R-061]</span></p></div>

The two descriptions are presented side by side, as the reconciliation requires, and neither is preferred. <span class="cite">[reconciliation R-061; E.1 rule 29]</span> On one side, FTAI's release and its quarterly filing describe J&F as FTAI's joint venture with Jereh. On the other, Jereh's exchange disclosure, reached through a secondary site rather than the Shenzhen filing itself, describes J&F as Jereh's subsidiary. The research observed that the two are compatible only if Jereh holds a controlling stake or if "subsidiary" is being used loosely. <span class="cite">[D8 §2.7, T3]</span> Nothing reached states a percentage.

<div class="box"><div class="h">Why the consolidation question decides what the $1.465 billion means in FTAI's accounts</div><p>A purchase order is placed on J&F, not on FTAI. What appears in FTAI's revenue depends on who consolidates J&F. If FTAI controls and consolidates it, J&F's genset sales to the customer are FTAI's revenue at their full value. If Jereh consolidates it, FTAI's Power revenue is its sales of converted turbines into J&F plus its share of J&F's profit under the equity method (Part VIII §64), and the $1.465 billion face value never appears as FTAI revenue. If neither controls it, the equity method applies to both. The division of labour FTAI describes, FTAI supplying the converted turbine and Jereh the packaging, is consistent with any of the three. The 10-Q's J&F note, which would settle it, was not returned by the research. <span class="cite">[D8 §2.7, U2; reconciliation R-061]</span></p></div>

The division of labour implied by FTAI's words is as follows, and it is an implication rather than a disclosed scope of work. FTAI supplies the converted turbine, the CFM56 gas generator with its power-turbine arrangement, drawing on its engine inventory, its module factories and its parts supply, which includes the multi-year materials agreement with CFM signed 22 January 2026 (Part VII §52) and the serviceable-material agreement with AAR (an aviation services company) extended to 2030. <span class="cite">[FTAI release, 22 Jan 2026; PRNewswire, 2025; D8 §2.7]</span> Jereh packages the turbine: the trailer or skid, enclosure, generator, gearbox, inlet, exhaust, fuel skid and controls, then tests, distributes and commissions the complete genset. J&F contracts with the customer. <span class="cite">[D8 §2.7]</span> Neither the CFM nor the AAR agreement's body was read by the research. <span class="cite">[reconciliation C.8 item 4]</span>

### 70.3 The master supply agreement and the initial order

<div class="defn"><b>Master supply agreement; purchase order; milestone payments; performance adjustment mechanism</b><p>A master supply agreement is a framework contract that fixes terms under which a buyer may place binding orders over its life; the orders themselves are purchase orders. Milestone payments tie the buyer's payments to events rather than to delivery alone: here an advance at signing, progress payments through production and testing, and a final payment at on-site commissioning, which FTAI's second-quarter 2026 call described as "derisking working capital". A performance adjustment mechanism is a contractual price change tied to measured performance of the delivered equipment; in this order it is "capped at 10%", and the metrics it applies to and whether it can raise as well as lower the price are undisclosed. <span class="cite">[FTAI release, 22 Jul 2026, as reposted by Barchart and Pulse2; Quartr summary of the Q2 2026 call, call coverage; D8 §2.9, §4.1, U10, U11]</span></p></div>

<div class="defn"><b>Commissioning</b><p>Commissioning is the on-site testing and hand-over of installed equipment: the unit is connected to gas and to the customer's switchgear, run, and shown to meet its specification before the customer accepts it. It is the last milestone payment under the J&F order. <span class="cite">[FTAI release, 22 Jul 2026; D8 §4.1]</span></p></div>

<div class="exh"><div class="exh-title">Exhibit 9.5 — The J&F master supply agreement and initial purchase order, term by term</div>

| Term | As disclosed | Source | Not disclosed |
|---|---|---|---|
| Date | 22 Jul 2026 | FTAI release; FilingReader on Jereh's SZSE disclosure | — |
| Contracting party | J&F Power Systems LLC | FTAI release | Ownership of J&F (R-061) |
| Counterparty | "a leading international cloud service provider" (FTAI release); "a U.S. hyperscaler" (Q2 2026 call summaries) | FTAI release; GuruFocus, Quartr | Name |
| Framework | Five-year master supply agreement; the customer may issue further purchase orders | FTAI release | Volume commitments beyond the initial order |
| Initial order | $1.465 billion purchase order for Mod-1 mobile gas turbine generator sets | FTAI release; FilingReader | Unit count; price per unit; scope (commissioning, spares, after-treatment, service) (U1) |
| Delivery | In batches through November 2027 | FTAI release | Batch sizes and dates |
| Share of 2027 | "a substantial number" of FTAI Power's targeted 2027 Mod-1 deliveries, the target being 100 units | FTAI release; Q4/FY2025 release | The number |
| Payment | Milestone basis: advance at signing; progress payments through production, testing and on-site commissioning | FTAI release | Size of the advance; percentage at each milestone (U10) |
| Price adjustment | "subject to a performance adjustment mechanism capped at 10%" | Release text as reposted by Barchart and Pulse2; primary release | Metrics; whether symmetric (U11) |
| Working capital | Described on the Q2 2026 call as "derisking working capital" | Quartr summary, call coverage | — |

<cite>Source: FTAI Aviation, "FTAI Announces $1.465 Billion Gas Turbine Generator Set Order Through J&F Power Systems", GlobeNewswire, 22 Jul 2026; Barchart and Pulse2 reposts of the same release, Jul 2026; FilingReader, "Yantai Jereh subsidiary secures $1.47bn turbine contract", 22 Jul 2026; GuruFocus and Quartr summaries of the 30 Jul 2026 call; FTAI Q4/FY2025 release, 25 Feb 2026; D8 §4.1 and §7. Reconciliation R-061; D8 T1.</cite></div>

Three mechanics in that table deserve a sentence each. The milestone structure means that cash arrives before delivery: an advance at signing funds the engines and packaging that must be bought before any unit is commissioned, which is why the call described it in working-capital terms. <span class="cite">[Quartr, 30 Jul 2026, call coverage]</span> The performance adjustment means that up to 10% of the order's value depends on whether delivered units meet whatever the contract measures, which could be output, heat rate, availability or schedule; the cap also bounds the exposure at 10%. <span class="cite">[D8 §5, U11]</span> The "substantial number" language ties the order to the 2027 target of 100 units without giving a count, and that one missing number is the input to every price and margin figure in §74.

### 70.4 The customer

<div class="defn"><b>Hyperscaler</b><p>A hyperscaler is a very large cloud-computing operator that builds and runs its own data centers at a scale of gigawatts. The research's sources describe the J&F customer two ways: FTAI's release of 22 July 2026 says "a leading international cloud service provider", and summaries of the second-quarter 2026 call say "a U.S. hyperscaler". The two are not necessarily inconsistent, since a US company can operate internationally, but the primary document does not say "US", and the customer is not named in anything reached. <span class="cite">[FTAI release, 22 Jul 2026; GuruFocus and Quartr, 30 Jul 2026, call coverage; D8 §3, T1]</span></p></div>

Both descriptions are carried wherever the customer is mentioned in this Part, with their sources, and the primer does not choose between them. <span class="cite">[D8 T1; E.1 rule 1]</span>

### 70.5 What is not disclosed about the order

The unit count and the price per unit are not disclosed. <span class="cite">[D8 U1]</span> Without them, every per-unit figure in §74 is a derivation under a stated assumption, not a fact. The research recorded that FTAI's third-quarter 2026 report or call, or Jereh's Shenzhen filing if it states quantities, would resolve it. Jereh's shares rose on both the GenSystems and the J&F announcements, which is recorded here as a reported market fact and not as evidence about the order's terms. <span class="cite">[Yicai Global, 2026; FilingReader, 22 Jul 2026]</span>

## 71. The market: data-center demand and the turbine shortage

Mod-1 sells into a market defined by two facts: electricity demand from data centers is growing faster than grids are adding supply, and the factories that make large gas turbines are sold out for years. This section gives the figures for each, with dates and sources, and then the behind-the-meter response that connects them.

### 71.1 Data-center electricity demand

<div class="exh"><div class="exh-title">Exhibit 9.6 — Data-center electricity demand: the figures the research reached, with date and source</div>

| Measure | Figure | Date | Source and level |
|---|---|---|---|
| Global data-centre electricity consumption by 2030 | More than doubles to about 945 TWh, "slightly more than" Japan's total consumption | April 2025 | International Energy Agency (IEA), "Energy and AI" (intergovernmental agency report) |
| Electricity demand from AI-optimised data centres by 2030 | More than quadruples | April 2025 | IEA, same |
| US share | Data centres account for about half of US electricity demand growth to 2030 | April 2025 | IEA, same |
| US electricity consumption growth | +1.9% in 2026 and +2.5% in 2027; the largest four-year growth period since 2000, driven primarily by data centers | 2026 | US Energy Information Administration (EIA) Short-Term Energy Outlook, via Data Center Dynamics (government statistics via trade press) |
| Regional load growth, 2025–27 | ERCOT (the Texas grid operator) about 10% a year; PJM (the mid-Atlantic grid operator) about 3.2% a year | 2026 | EIA via Data Center Dynamics |
| Price effect | Data-center demand could drive a 79% rise in ERCOT wholesale electricity prices in 2027 | 2026 | EIA via Utility Dive |

<cite>Source: IEA, "Energy and AI", executive summary and news release, April 2025; Data Center Dynamics, "EIA: US electricity use to see largest four-year growth period since 2000", 2026; Utility Dive, "Data center demand spike could drive 79% ERCOT price hike in 2027: EIA", 2026; D8 §4.3.</cite></div>

<div class="defn"><b>PJM and ERCOT</b><p>PJM (originally Pennsylvania-New Jersey-Maryland) is the grid operator for the mid-Atlantic region of the United States, and the Electric Reliability Council of Texas (ERCOT) is the grid operator for most of Texas. Both run the wholesale electricity markets and the queues for connecting new plants in their regions. The EIA's regional growth figures above and Enverus's finding that half of behind-the-meter data-center capacity sits in these two regions are why they appear in this Part. The definitions are from first principles; the research used the names without defining them. <span class="cite">[D8 §2.8, §4.3; registry section 2]</span></p></div>

The IEA's 945 TWh is a global figure for all data centres, not a figure for AI alone, and the agency separately says that demand from AI-optimised data centres more than quadruples over the same period. <span class="cite">[IEA, Apr 2025]</span> The EIA figures are national and regional load growth, in which data centers are the primary driver rather than the whole; the Texas growth rate of about 10% a year is several times the mid-Atlantic rate. <span class="cite">[EIA via Data Center Dynamics, 2026]</span> None of these sources forecasts how much of the demand will be met by on-site generation; that is Enverus's territory in §71.2.

### 71.2 Behind the meter: "bring your own power"

<div class="defn"><b>Behind-the-meter (BTM) generation</b><p>Behind-the-meter generation is electricity generated on the customer's side of the utility meter, at the customer's site, so that it never passes through the grid. Enverus estimates that about 40% of installed data-center capacity is behind the meter, that this adds about 1.3 Bcf/d of incremental gas demand by 2030, and that half of it sits in ERCOT and PJM. A separate forecast attributed to the EIA or to S&P Global puts behind-the-meter generation at US industrial sites at 22.5 GW over 2026–2030, about 4.5 GW a year, 88% of it for data centers, with more than 80% of announced on-site generation fuelled by natural gas; the research could not confirm which of the two sources the figure belongs to. The phrase "bring your own power" describes a data-center developer that arrives with its own generation rather than waiting for a grid connection. <span class="cite">[Enverus, "Off the grid, on the gas", 2026; EIA Today in Energy #67344 or S&P Global, 2026, attribution unverified; D8 §4.3]</span></p></div>

Enverus attributes the behind-the-meter share to "grid interconnection congestion and long development timelines", which §73.3 takes up. <span class="cite">[Enverus, 2026]</span> The scale of FTAI's planned output against these figures is a matter of arithmetic.

<div class="worked"><div class="h">Worked example 9.2 — 100 Mod-1 units a year against the market-wide figures</div>
<p>Inputs: 100 units a year in 2027 (sourced: FTAI Q4/FY2025 release, 25 Feb 2026); 25 MW per unit (sourced: launch release); behind-the-meter additions at US industrial sites of about 4.5 GW a year over 2026–2030, 88% for data centers (sourced: EIA or S&P Global, attribution unverified); GE Vernova backlog plus reservations 116 GW at the second quarter of 2026 (sourced: Power Engineering, Jul 2026); Enverus's 1.3 Bcf/d of incremental behind-the-meter gas demand by 2030 (sourced); 4.9 MMcf/d per unit at a 90% capacity factor (derived in worked example 9.1, with its assumptions).</p>
<div class="eqblock">annual output capacity = 100 × 25 MW = 2,500 MW = 2.5 GW
share of behind-the-meter additions = 2.5 ÷ 4.5 = 56% of one year's forecast additions
data-center share of those additions = 4.5 × 0.88 ≈ 4.0 GW a year; 2.5 ÷ 4.0 = 63%
share of GE Vernova's backlog plus reservations = 2.5 ÷ 116 = 2.2%
gas for 100 units = 100 × 4.9 MMcf/d = 490 MMcf/d ≈ 0.49 Bcf/d
share of Enverus's incremental gas = 0.49 ÷ 1.3 = 38%</div>
<p>So 100 units a year is a small fraction of what the frame-turbine makers have on order and a large fraction of one forecast of US behind-the-meter additions, and the gas those units would burn is a large share of one forecast of incremental on-site gas demand. The two forecasts are not the same population: the 4.5 GW figure covers industrial sites in the United States, and the J&F customer is "international" in FTAI's words. Limits of the example: the 4.5 GW figure's source is unverified; the Enverus gas figure is an estimate to 2030, not an annual flow; the gas per unit rests on worked example 9.1's assumed capacity factor; and the units' location is unknown. These percentages are derived in this Part and are not published by any source. <span class="cite">[D8 §2.10, §5; Enverus, 2026; Power Engineering, Jul 2026]</span></p></div>

### 71.3 The turbine shortage

The reason a buyer considers a 25 MW unit built from a used airline engine is that the machines it would otherwise buy are not available for years.

<div class="defn"><b>Slot reservation agreement</b><p>A slot reservation agreement is a paid reservation of a future turbine manufacturing slot, made before a firm order. GE Vernova counts reservations together with firm backlog in the figures it reports, so its 116 GW at the second quarter of 2026 and the 125 GW it expects by December 2026 are backlog plus reservations, and the company is selling slots for 2031 delivery. The term is distinct from a shop's induction slot (Part IV §27) and a parts maker's production slot (Part VI §41). <span class="cite">[Power Engineering, Jul 2026; Industrial Info Resources, 2026; D8 §3; registry C-18]</span></p></div>

<div class="exh"><div class="exh-title">Exhibit 9.7 — Gas-turbine order books and lead times: a dated series, by manufacturer</div>

| Manufacturer | Measure | Figure | As of | Source and level |
|---|---|---|---|---|
| GE Vernova | Gas backlog | 50 GW | 2025 | Yahoo Finance (financial press) |
| GE Vernova | Gas equipment backlog plus slot reservation agreements | 83 GW | End-2025 | Power Engineering, Jul 2026 (trade press) |
| GE Vernova | Same | 100 GW | Q1 2026 | Industrial Info Resources, 2026 (industry data vendor) |
| GE Vernova | Same | 116 GW | Q2 2026 | Power Engineering, Jul 2026, citing the 22 Jul 2026 call |
| GE Vernova | Same, expected | At least 125 GW | By Dec 2026 | Power Engineering, Jul 2026 |
| GE Vernova | Slots | Selling 2031 delivery slots; more than half of 2031 expected contracted by end-2026 | Jul 2026 | Power Engineering, Jul 2026 |
| GE Vernova | Earlier characterisation | "2026 and 2027 largely sold out"; booking 2028 and 2029 | 2026 (undated within year) | Oilprice (energy press) |
| GE Vernova | Outlook | Raised multi-year financial outlook | 9 Dec 2025 | GE Vernova release (company) |
| Siemens Energy | Gas-turbine backlog | 69 GW, after booking 15 GW and shipping 6 GW in the quarter | 30 Jun 2026 (fiscal Q3) | Oilprice; Energy News Beat, 2026 |
| Siemens Energy | Lead times | "three years or more" | 2026 | Oilprice |
| Mitsubishi Power (Mitsubishi Heavy Industries) | Large-frame backlog | 35 GW; quarter's orders for delivery 2028–2030; "selective in the projects we contract" | 2026 | Oilprice |
| Industry | Combined-cycle plant lead time | Five years in 2025, up from 3.5 years in 2023 | 2025 | Oilprice |
| Industry | Global gas-turbine orders against manufacturing capacity | 110 GW of orders at end-2025 against 60–70 GW a year of capacity | End-2025 | Wood Mackenzie via Oilprice (consultancy via energy press) |

<cite>Source: Yahoo Finance, "GE Vernova Backlog Hits 50 GW", 2025; Power Engineering, "Data centers drive record surge in GE Vernova power equipment orders as turbine slots tighten through 2030", Jul 2026; Industrial Info Resources, 2026; Oilprice, "The Gas Turbine Shortage Just Became AI's Biggest Constraint", 2026, and "Global Gas Turbine Orders Hit Record High as Power Demand Surges"; Energy News Beat, 2026; GE Vernova, BusinessWire release, 9 Dec 2025; D8 §3 and §4.4. Reconciliation D8 T4.</cite></div>

The GE Vernova rows are a time series, not a contradiction: 50 GW, then 83, 100 and 116 GW, with the later figures including slot reservations as well as firm orders. <span class="cite">[D8 T4]</span> The two characterisations of its sold-out horizon, "2028 and 2029" in one source and 2031 slots in another, sit at different dates in a year in which the book grew by a third, so a reader quoting either should give its date and its definition. <span class="cite">[Oilprice, 2026; Power Engineering, Jul 2026; D8 T4]</span> Wood Mackenzie's comparison of 110 GW of orders against 60 to 70 GW of annual capacity is the simplest statement of the shortage: at end-2025 the industry had taken orders for roughly a year and a half to two years of its output. <span class="cite">[Wood Mackenzie via Oilprice, 2026]</span> A buyer that needs power in 2026 or 2027 cannot get a new frame turbine, and that is the opening for aeroderivatives, reciprocating engines and fuel cells. <span class="cite">[D8 §5]</span>

## 72. Competing supply: aeroderivatives, frame turbines, reciprocating engines, fuel cells

This section takes each alternative to Mod-1 in turn, with output, lead time and price where published, and then collects the dollars-per-kilowatt benchmarks the research reached. The frame turbines themselves were covered in §71.3; their relevance here is that they are the machines a buyer would prefer at scale and cannot get.

**GE Vernova LM2500XPRESS.** GE Vernova's trailer-deliverable version of the LM2500 is rated 35 MW per unit in the company's release. Crusoe, a data-center developer, ordered 10 units in December 2024 and 19 in June 2025, "nearly 1 GW" combined, for AI data centers, and the packages have been delivered. <span class="cite">[GE Vernova release, 22 Jul 2025; Turbomachinery International, undated]</span> Twenty-nine units at about 1 GW implies about 34.5 MW each, and a commissioning brief gives 34 MW; ratings vary with site conditions and "nearly" 1 GW is rounded, so the research carries 35 MW as GE's figure and the lower numbers as implied. <span class="cite">[D8 T6]</span> No price or lead time was captured.

**GE Vernova LM6000.** The CF6-80C2-derived LM6000 is in the 48 to 50 MW class. Trade coverage quotes its waiting list at "anywhere from three to five years". <span class="cite">[EEPower, undated; Data Centre Magazine, undated]</span> That the manufacturer's own aeroderivative is itself sold out for years is the context for non-manufacturer converters such as ProEnergy and FTAI. <span class="cite">[D8 §5]</span>

**Siemens Energy SGT-A65.** The SGT-A65 is Siemens Energy's aeroderivative derived from the Rolls-Royce Trent. Its output and lead time were not captured by the research, and nothing is quoted here. <span class="cite">[D8 U9]</span>

**Solar Turbines (Caterpillar).** Solar's mobile Titan-class units appear in the public record through xAI's Memphis permit, which allowed 15 "Solar SMT-130 generators" totalling up to 247 MW, about 16.5 MW each. <span class="cite">[TechCrunch, 3 Jul 2025]</span> Figures for the larger Titan 350 were not captured. <span class="cite">[D8 U9]</span>

**ProEnergy PE6000.** ProEnergy, a private company, builds the PE6000 at 48 MW on CF6-80C2 cores taken from retired Boeing 747 engines, "the same engine core GE Vernova uses in its LM6000". It quotes 2027 delivery and has sold 21 turbines for two data-center projects totalling more than 1 GW, as bridging power for five to seven years until grid interconnection. <span class="cite">[Data Centre Magazine, undated; EEPower, undated]</span> It is the closest analogue to FTAI Power: a non-manufacturer reusing retired airline cores, limited by the supply of suitable cores and by packaging capacity. <span class="cite">[D8 §3, §5]</span> No price was captured.

**Baker Hughes NovaLT.** Baker Hughes's NovaLT line is a family of small industrial turbines, not aeroderivatives. Dynamis Power Solutions ordered 76 NovaLT16 units, about 1.3 GW, for data-center and oil-and-gas power, which implies about 17 MW each. <span class="cite">[World Oil, 29 Jul 2026]</span> Baker Hughes doubled its data-center order target to $3 billion over 2025–2027 and plans to double NovaLT capacity by the first half of 2027. <span class="cite">[Bloomberg Government, undated]</span> No price was captured.

**Wärtsilä and Caterpillar reciprocating engines.** Wärtsilä builds data-center plants from 10 to 23 MW gas piston engines reaching more than 450 MW per site, and claims electrical efficiency over 50%, 20–35% less fuel than gas turbines, and 20–30% lower capital cost than turbines once reserve capacity is included; all are vendor claims from a product page. <span class="cite">[Wärtsilä product page, undated]</span> It announced a 507 MW US data-center order on 20 November 2025. <span class="cite">[Wärtsilä release, 20 Nov 2025]</span> Caterpillar's gas gensets were not captured. <span class="cite">[D8 U9]</span> The efficiency claim and FTAI's 35–40% figure are consistent with each other at the lower end of Wärtsilä's stated gap, but both are self-reported and the research did not test either. <span class="cite">[D8 T10]</span>

**Bloom Energy fuel cells.** Bloom's annual report positions its solid-oxide fuel cells against reciprocating engines for on-site power, including "the peak loads associated with AI data centers". <span class="cite">[Bloom Energy 10-K FY2024]</span> Deal sizes and dollars per kilowatt were not captured, so no comparison is drawn. <span class="cite">[D8 U9]</span>

<div class="exh"><div class="exh-title">Exhibit 9.8 — Comparable units and orders: output, delivery and the largest published order for each</div>

| Unit | Type | Output per unit | Lead time or delivery | Notable order | Source |
|---|---|---|---|---|---|
| FTAI Mod-1 (CFM56) | Aeroderivative, non-OEM, mobile | 25 MW | First by Q4 2026; 100 in 2027 | $1.465B, batches to Nov 2027, unit count undisclosed | FTAI releases, 30 Dec 2025, 25 Feb 2026, 22 Jul 2026 |
| GE Vernova LM2500XPRESS | Aeroderivative, OEM, trailer-deliverable | 35 MW (GE); about 34.5 MW implied | Delivered 2025–26 | Crusoe, 29 units, nearly 1 GW | GE Vernova, 22 Jul 2025; Turbomachinery International |
| GE Vernova LM6000 (CF6-80C2) | Aeroderivative, OEM | About 48–50 MW | Waiting list three to five years | — | EEPower; Data Centre Magazine |
| ProEnergy PE6000 (CF6-80C2) | Aeroderivative, non-OEM | 48 MW | 2027 | 21 units, more than 1 GW, two projects | EEPower; Data Centre Magazine |
| Siemens Energy SGT-A65 (Trent) | Aeroderivative, OEM | Not captured | Not captured | — | D8 U9 |
| Baker Hughes NovaLT16 | Small industrial turbine | About 17 MW (1.3 GW over 76 units) | Capacity doubling by 1H 2027 | Dynamis, 76 units, about 1.3 GW | World Oil, 29 Jul 2026; Bloomberg Government |
| Solar Turbines SMT-130 (mobile) | Small industrial turbine, mobile | About 16.5 MW (247 MW over 15 units) | In service 2024–25 | xAI Memphis, 15 permitted (up to 35 operated) | TechCrunch, 3 Jul 2025; Data Center Dynamics, 2025 |
| Wärtsilä gas engines | Reciprocating | 10–23 MW each; plants over 450 MW | — | 507 MW US data-center order, 20 Nov 2025 | Wärtsilä product page and release |
| Caterpillar gas gensets | Reciprocating | Not captured | Not captured | — | D8 U9 |
| Bloom Energy fuel cells | Solid-oxide fuel cell | Not captured | Not captured | Not captured | Bloom Energy 10-K FY2024; D8 U9 |

<cite>Source: as listed in each row; compiled in D8 §4.5. Reconciliation D8 T6 (LM2500XPRESS rating). The per-unit figures marked "about" are divisions of a published total by a published unit count, done in the research.</cite></div>

### 72.1 What a turbine costs per kilowatt

Dollars per kilowatt is the industry's unit price for generating equipment: the cost divided by the rated output in kilowatts. The research reached four benchmarks, and they measure four different things.

<div class="exh"><div class="exh-title">Exhibit 9.9 — Dollars-per-kilowatt benchmarks reached by the research, with scope and date</div>

| Benchmark | $/kW | What it measures | Date | Source and level |
|---|---|---|---|---|
| Simple-cycle gas turbine, equipment only | About $1,150 at 1 MW falling to about $171 at about 600 MW | Bare turbine equipment; price per kW falls steeply with unit size | Undated; pre-2024 pricing | Gas Turbine World (trade publication) |
| 100 MW aeroderivative genset, installed | $1,175 | A complete installed aeroderivative genset of 100 MW | Undated; pre-2024 pricing | Gas Turbine World |
| Gas-turbine prices, projected | $600 by end-2027, "nearly tripling from 2019 levels" | Turbine equipment only | Projection to end-2027, made 2026 | Wood Mackenzie via Oilprice (consultancy via energy press) |
| Gas capacity in regulatory filings | $1,100–1,400 "two years ago"; $2,000–2,500 "now" | Whole plants as approved by utility regulators, predominantly large frame and combined-cycle | 2026 | Power Engineering (trade press) |
| Headline price inflation | +195% | Gas-turbine prices, scope as the headline gives it | 2026 | Power Engineering |
| Mod-1, implied | $586 at 100 units; $733 at 80; $977 at 60 | A delivered mobile genset, if the $1.465B order is the stated number of units; scope of the order unknown | Derived, 2026 | D8 §2.9; worked example 9.4 below |

<cite>Source: Gas Turbine World, "How much does it cost to build a Simple Cycle or Combined Cycle plant?" and "Capital Costs for Utility Scale Gas Turbine Plants", undated; Oilprice, "The Gas Turbine Shortage Just Became AI's Biggest Constraint", 2026, citing Wood Mackenzie; Power Engineering, "Gas turbine prices climb 195% as supply crunch reshapes power development", 2026; D8 §2.9 and §4.4. Reconciliation D8 T5.</cite></div>

The scopes do not line up, and the reconciliation asks that they never be collapsed into one figure. <span class="cite">[D8 T5; E.1 rule 1]</span> The Gas Turbine World figures are equipment-only for the turbine, or installed for a complete genset, at pre-2024 prices; Wood Mackenzie's is a projection for turbine equipment alone; Power Engineering's is for whole plants as regulators approve them, which includes site, civil works, interconnection and in most cases a steam cycle. A delivered mobile genset sits between a bare turbine and a plant: it includes the packaging and generator but not the site, the gas lateral or the grid connection. The Gas Turbine World size curve also matters on its own: a small unit costs several times more per kilowatt than a large one, and a 25 MW unit sits near the expensive end of that curve. <span class="cite">[Gas Turbine World, undated]</span>

<div class="worked"><div class="h">Worked example 9.3 — What each benchmark would imply for a 25 MW unit</div>
<p>Inputs: 25 MW = 25,000 kW (sourced: launch release); the five benchmark ranges in Exhibit 9.9 (sourced as shown, scopes differ).</p>
<div class="eqblock">Gas Turbine World equipment-only, small-unit end: 25,000 × $1,150 = $28.8 million
Gas Turbine World equipment-only, large-unit end: 25,000 × $171 = $4.3 million
Gas Turbine World 100 MW aero genset, installed: 25,000 × $1,175 = $29.4 million
Wood Mackenzie turbine-only, end-2027: 25,000 × $600 = $15.0 million
Power Engineering plant-level, current filings: 25,000 × $2,000 to $2,500 = $50.0 to $62.5 million</div>
<p>So the published benchmarks, applied to a 25 MW rating, span $4.3 million to $62.5 million per unit, and the spread is mostly a difference of scope and size rather than of price. The $171 figure is for a 600 MW frame and does not describe any 25 MW machine; the $1,150 and $1,175 figures are for small units and complete aero gensets at older prices; the $600 figure is the one turbine-only projection for the period in which Mod-1 units would be delivered; and the $2,000 to $2,500 figures include everything a mobile genset leaves out. §74.1 sets the implied Mod-1 price inside this range. Limits of the example: the benchmarks are undated or projected, the scopes differ, and none of them is for a 25 MW aeroderivative sold in 2026 or 2027, which the research listed as an unknown. <span class="cite">[Gas Turbine World, undated; Wood Mackenzie via Oilprice, 2026; Power Engineering, 2026; D8 T5, U9]</span></p></div>

## 73. Permitting and interconnection

A mobile genset can be built in weeks, but putting it to work at a data center runs through three processes that are not under the seller's control: gas supply, an air permit and, where the site also uses the grid, an interconnection agreement. The first was covered in §68.3. This section takes the other two, using the one documented US case the research reached.

### 73.1 The air permit

<div class="defn"><b>Air permit</b><p>An air permit is the authorisation, issued under the US Clean Air Act by the state or county agency that implements it, to construct and operate a source of air emissions. A stationary source needs a construction and operating permit before it runs, and the permit sets the emission limits and controls the source must meet. In the Memphis case the sequence ran roughly a year from first operation in mid-2024 to permit application in the winter of 2024 to a permit in July 2025. <span class="cite">[TechCrunch, 3 Jul 2025; Tennessee Lookout, 2025; D8 §2.4, §2.8]</span></p></div>

<div class="defn"><b>Interconnection agreement; interconnection queue</b><p>An interconnection agreement is the contract between a generator or a large customer and the utility or grid operator that governs its connection to the grid. The interconnection queue is the waiting list of projects seeking such agreements, which in the United States runs to years. The queue is the reason behind-the-meter generation exists: Enverus attributes the on-site share of data-center power to "grid interconnection congestion and long development timelines", and ProEnergy's customers plan on five to seven years before they expect a connection. Specific queue durations for PJM and ERCOT were not captured. <span class="cite">[Enverus, 2026; Data Centre Magazine, undated; D8 §2.8, U14]</span></p></div>

### 73.2 The Memphis precedent

The one deployment of mobile gas turbines at a data center that the research documented in detail is xAI's site in Memphis, Tennessee. It is carried here as a precedent for the process, not as a statement about FTAI, whose units have not yet been deployed.

<div class="exh"><div class="exh-title">Exhibit 9.10 — The xAI Memphis timeline: mobile turbines, permit, dispute</div>

| When | What happened | Source |
|---|---|---|
| Mid-2024 | xAI begins operating mobile gas turbines at its Memphis data center without a stationary-source air permit | TechCrunch, 3 Jul 2025; Tennessee Lookout, 2025 |
| Winter 2024 | Permit application filed with Shelby County | Tennessee Lookout, 2025 |
| 2025 (date within year not captured) | The number of turbines on site rises to as many as 35, "in violation of permit limits" per the headline, against a permit eventually written for 15 | Data Center Dynamics, 2025 |
| 2025 | The Southern Environmental Law Center and the NAACP (the National Association for the Advancement of Colored People) bring a Clean Air Act suit over the unpermitted turbines | Data Center Dynamics, 2025 |
| 3 Jul 2025 | Shelby County issues a permit allowing xAI "to operate 15 Solar SMT-130 generators with certain emissions controls", up to 247 MW | TechCrunch, 3 Jul 2025; E&E News, Jul 2025 |
| Ongoing | Dispute over whether the temporary turbines were "nonroad engines" exempt from permitting, which Shelby County accepted and the plaintiffs contest | Data Center Dynamics, 2025; Tennessee Lookout, 2025; E&E News, Jul 2025 |

<cite>Source: TechCrunch, "xAI gets permits for 15 natural gas generators at Memphis data center", 3 Jul 2025; E&E News, "Musk's xAI gets air permit for Memphis supercomputer", Jul 2025; Data Center Dynamics, "xAI facing lawsuit over use of gas turbines at Memphis supercomputer" and "xAI doubles number of onsite gas turbines at Memphis data center in violation of permit limits", 2025; Tennessee Lookout, 2025; D8 §2.4, §2.8. Reconciliation D8 T9.</cite></div>

<div class="defn"><b>Nonroad engine</b><p>A nonroad engine is a category in US air rules for engines that are mobile or temporary, generally meaning at one location for less than twelve months, and that are exempt from the permitting that applies to stationary sources. Whether trailer-mounted turbines at a data center qualify is contested. In Memphis, Shelby County accepted that xAI's temporary turbines were nonroad engines exempt from permitting. The Southern Environmental Law Center and the NAACP contest that reading as allowing an operator to "install and operate any number of new polluting turbines at any time without any written approval ... without pollution controls". The question is unresolved in litigation. <span class="cite">[Data Center Dynamics, 2025; Tennessee Lookout, 2025; E&E News, Jul 2025; D8 §2.4, T9]</span></p></div>

The two readings are carried without preference. <span class="cite">[D8 T9; E.1 rule 1]</span> On one side, a county air agency treated mobile turbines as exempt from stationary-source permitting while they were temporary. On the other, two organisations argue in court that they are stationary sources needing permits and controls. The research noted the consequence for Mod-1 in neutral terms: the outcome "could either widen or close the fast-deployment route Mod-1 is designed for". <span class="cite">[D8 §5]</span> A unit that must hold a stationary-source permit before it runs cannot be deployed in two weeks unless the permit was obtained in advance; a unit treated as a nonroad engine can.

### 73.3 Interconnection waits and bridging

<div class="defn"><b>Bridging power</b><p>Bridging power is temporary on-site generation used until a grid interconnection is available. ProEnergy's customers describe their turbine plants as "bridging power for five to seven years, which is when they expect to have grid interconnection". If queues shorten, the bridging market shrinks; if they lengthen, turbines bought as bridges become long-term plant. <span class="cite">[Data Centre Magazine, undated; EEPower, undated; D8 §2.8, §5]</span></p></div>

The five-to-seven-year figure is the only quantification of the interconnection wait the research reached, and it comes from one supplier's description of its customers' plans rather than from a grid operator's queue statistics. <span class="cite">[D8 U14]</span> It bears on Mod-1 in two ways. A 25 MW mobile unit with a stated second life of 10 to 20 years outlasts a five-to-seven-year bridge, so a buyer either keeps it as permanent plant, moves it to a new site, which is what mobility is for, or resells it. And the milestone payments and the five-year master agreement in §70.3 run on a shorter clock than the bridge, so the contract and the asset life are not the same length. These are descriptions of the time scales involved, not predictions.

## 74. Worked examples: implied unit price; CFM56 cores consumed

Everything quantitative that can be said about FTAI Power today is a derivation from a small set of disclosed numbers under stated assumptions, because the two numbers that would make it arithmetic rather than inference, the unit count in the order and the engines per unit, are undisclosed. This section does the derivations, labels every input, and shows each result under each base where the research holds more than one.

### 74.1 Implied unit price and dollars per kilowatt

<div class="worked"><div class="h">Worked example 9.4 — The implied price of a Mod-1 under three unit-count assumptions</div>
<p>Inputs: order value $1.465 billion (sourced: FTAI release, 22 Jul 2026); 2027 production target 100 units (sourced: Q4/FY2025 release, 25 Feb 2026); the order covers "a substantial number" of 2027 deliveries (sourced: FTAI release, 22 Jul 2026); unit count in the order (not disclosed; three assumptions used: 100, 80 and 60); output 25 MW = 25,000 kW (sourced: launch release).</p>
<div class="eqblock">at 100 units: 1,465,000,000 ÷ 100 = $14.65 million per unit; 14,650,000 ÷ 25,000 kW = $586/kW
at 80 units: 1,465,000,000 ÷ 80 = $18.3 million per unit; ÷ 25,000 = $733/kW
at 60 units: 1,465,000,000 ÷ 60 = $24.4 million per unit; ÷ 25,000 = $977/kW</div>
<p>Against the benchmarks in Exhibit 9.9 and worked example 9.3: $586 to $977 per kW for a delivered mobile genset sits below the $2,000 to $2,500 per kW of current plant-level regulatory filings, near or above Wood Mackenzie's $600 per kW turbine-only projection for end-2027, and below Gas Turbine World's $1,150 to $1,175 per kW for small units and installed aero gensets at older prices. The research called the comparison loose, because the scopes differ. Limits of the example: the unit count is the single undisclosed input and the result scales with it; the order's scope (commissioning, spares, after-treatment, service) is unknown, so the price may cover more than the genset; and 100 units is the whole 2027 target, whereas the release says only "a substantial number". <span class="cite">[D8 §2.9, U1; reconciliation D8 T5]</span></p></div>

<div class="exh"><div class="exh-title">Exhibit 9.11 — Implied Mod-1 unit price and $/kW by assumed unit count, beside the published benchmarks</div>

| Assumed units in the $1.465B order | Implied price per unit | Implied $/kW at 25 MW | Nearest published benchmarks (scope) |
|---|---:|---:|---|
| 100 (the whole 2027 target) | $14.65M | $586 | Wood Mackenzie $600 turbine-only, end-2027 projection |
| 80 | $18.3M | $733 | Between Wood Mackenzie turbine-only and Gas Turbine World small-unit equipment-only ($1,150) |
| 60 | $24.4M | $977 | Approaching Gas Turbine World small-unit equipment-only ($1,150) and installed 100 MW aero genset ($1,175), pre-2024 |
| Any | — | — | Plant-level filings $2,000–2,500 (whole plant, 2026) sit above every row |

<cite>Source: FTAI release, 22 Jul 2026 (order value); FTAI Q4/FY2025 release, 25 Feb 2026 (100 units); Gas Turbine World, undated; Wood Mackenzie via Oilprice, 2026; Power Engineering, 2026. Unit counts are assumptions; the implied figures are derived in D8 §2.9 and this Part and are not disclosed by FTAI or J&F. Reconciliation D8 T5.</cite></div>

### 74.2 Implied 2027 Power EBITDA per unit

FTAI's second-quarter 2026 report of 29 July 2026 guided 2027 business-segment Adjusted EBITDA (earnings before interest, taxes, depreciation and amortisation, as FTAI adjusts it; Part X §80) of $2.3 billion: Aerospace Products $1.4 billion, FTAI Power $450 million and Aviation Leasing $450 million. The release text confirms $1.4 billion and "$450 million"; the three-way split is as the dossiers and the orchestrator notes carry it. <span class="cite">[FTAI Q2 2026 release, 29 Jul 2026; Quartr and MarketBeat, 30 Jul 2026, call coverage; orchestrator notes; D10 §4.8]</span> One summary of the same call, by GuruFocus, gives the Power figure as "$450 million to $750 million". <span class="cite">[GuruFocus, 30 Jul 2026, call coverage; reconciliation R-062]</span> The research took the two as likely a base figure and an upside case stated on the same call, with the transcript not reached, and both are carried here as the reconciliation requires. <span class="cite">[D8 T2; E.1 rule 30]</span> Part X §84 carries the guidance history.

<div class="worked"><div class="h">Worked example 9.5 — Implied 2027 Power Adjusted EBITDA per unit, and what it would mean as a margin</div>
<p>Inputs: 2027 Power Adjusted EBITDA $450 million (sourced: Q2 2026 release text per the orchestrator notes; Quartr and MarketBeat call coverage) or $450–750 million (sourced: GuruFocus call coverage); 2027 production 100 units (sourced: Q4/FY2025 release); implied revenue per unit $14.65 million if the order is 100 units and FTAI consolidates J&F (derived in worked example 9.4; both conditions undisclosed).</p>
<div class="eqblock">EBITDA per unit at $450M: 450,000,000 ÷ 100 = $4.5 million
EBITDA per unit at $750M: 750,000,000 ÷ 100 = $7.5 million
margin if revenue per unit were $14.65M: 4.5 ÷ 14.65 = 31%; 7.5 ÷ 14.65 = 51%</div>
<p>So the guided figure is $4.5 million of Adjusted EBITDA per unit if 100 units are delivered in 2027, or $7.5 million at the top of the one summary's range. The margin lines hold only if FTAI's recognised revenue per unit is the full order value per unit, which requires both that the order is 100 units and that FTAI consolidates J&F. If Jereh consolidates J&F, FTAI's revenue is its turbine sale into the venture plus its share of the venture's profit, a smaller base on which the same EBITDA is a higher margin, and the figure cannot be derived from anything disclosed. If fewer than 100 units are delivered in 2027, EBITDA per unit is higher than $4.5 million on the same guidance. Limits of the example: the unit count, the consolidation, the revenue recognition and whether Power is a reportable segment are all undisclosed; the $450M is a guidance figure, not an outturn; and the $450–750M range is one call summary. <span class="cite">[D8 §2.9, U1, U2, U7; reconciliation R-061, R-062]</span></p></div>

### 74.3 CFM56 cores consumed

The feedstock question connects this Part to Parts I, III and V. Each Mod-1 removes a CFM56 gas generator from the pool of engines that would otherwise fly, be torn down for parts or be rebuilt as modules. FTAI has not said how many CFM56 engines go into one unit. The simplest reading, and the one the research used, is one gas generator per 25 MW unit, by analogy with the other single-core aeroderivatives in this class: the LM2500 is one TF39 or CF6-6 core for 25 to 35 MW. <span class="cite">[D8 §2.10, U3; GE Vernova, 22 Jul 2025]</span> On that assumption, 100 units in 2027 is 100 CFM56 engines a year, and "over 100 units annually" at capacity is more than that. <span class="cite">[FTAI release, 30 Dec 2025; Q4/FY2025 release, 25 Feb 2026]</span>

The installed base and the retirement rate are the two denominators, and both are contested. Part III §18 and §19 carry the full treatment; the binding figures are repeated here. The installed base is about 23,000 in service (CFM website, undated), about 24,000 in service as of September 2025 (Aviation Business News, trade press), and more than 22,800 in Safran's civil installed base at end-2025 (Safran FY2025 results presentation, 13 February 2026), out of more than 35,000 delivered (CFM). <span class="cite">[CFM website, undated; Aviation Business News, Sept 2025; Safran, 13 Feb 2026; reconciliation R-001; E.2]</span> Safe Fly Aviation, a consultancy blog, gives about 14,200 "active" engines, which one dossier read as all variants (about 6,200 -5B and 7,500 -7B) and another as the -7B fleet alone; it is a consultancy figure and never the fleet figure in this primer. <span class="cite">[Safe Fly Aviation, 2026; reconciliation R-001, R-002; E.1 rule 14]</span> The research's own feedstock arithmetic used the Safe Fly base, and the reconciliation asks that the OEM-level bases be shown beside it. <span class="cite">[reconciliation C.8 item 1]</span> The research also described total deliveries as "well over 30,000" as general knowledge; the OEM figure of more than 35,000 is the one carried. <span class="cite">[reconciliation R-069]</span>

The retirement rate has its own sequence. GE's planning assumption for 2026 moved from 3–4% of the fleet, to 2–3%, to 1.5–2% (GE's chief financial officer via Aviation Week, 2026). GE reported about 1.5% retired in 2025, broadly the same as 2024, and expected about 2% in 2026, "below the 2–3% range previously anticipated" (GE fourth-quarter 2025 results via Leeham, 22 January 2026). Realised first-quarter 2026 retirements were "below 1%" (GE Aerospace investor-relations page, 2026). Safe Fly gives "near 2% per year" on its own base. <span class="cite">[GE CFO via Aviation Week, 2026; Leeham, 22 Jan 2026; GE Aerospace investor-relations page, 2026; Safe Fly Aviation, 2026; reconciliation R-004; E.2]</span>

<div class="worked"><div class="h">Worked example 9.6 — 100 CFM56 engines a year against each installed-base figure and each retirement rate</div>
<p>Inputs: 100 engines a year (derived: 100 units × one gas generator per unit, the engines-per-unit figure being undisclosed); installed base about 24,000 (Aviation Business News, Sept 2025), about 23,000 (CFM website, undated), more than 22,800 (Safran, end-2025), and about 14,200 (Safe Fly, consultancy blog, 2026, basis contested); retirement rates 1.5% (GE, 2025 actual), 2% (GE, 2026 expected; Safe Fly), and "below 1%" (GE, first quarter 2026 realised, taken here as 1%).</p>
<div class="eqblock">share of the base: 100 ÷ 24,000 = 0.42%; 100 ÷ 23,000 = 0.43%; 100 ÷ 22,800 = 0.44%; 100 ÷ 14,200 = 0.70%
retirements at 1.5%: 24,000 × 0.015 = 360; 23,000 × 0.015 = 345; 22,800 × 0.015 = 342
retirements at 2%: 24,000 × 0.02 = 480; 23,000 × 0.02 = 460; 22,800 × 0.02 = 456; 14,200 × 0.02 = 284
retirements at 1%: 24,000 × 0.01 = 240; 23,000 × 0.01 = 230
100 engines as a share of retirements, OEM-level bases: 100 ÷ 480 = 21% to 100 ÷ 342 = 29% at 1.5–2%; 100 ÷ 240 = 42% to 100 ÷ 228 = 44% at 1%
100 engines as a share of retirements, Safe Fly base at 2%: 100 ÷ 284 = 35%</div>
<p>So 100 engines a year is under half of one percent of the installed base on any OEM-level count, and between about a fifth and about three-tenths of a year's retirements at GE's 2025 actual and 2026 expected rates; it rises to about two-fifths of retirements if the first quarter of 2026's sub-1% rate were sustained for a year, and it is about 35% on the consultancy base the research itself used. The share scales inversely with the base and with the rate, which is why both are shown. Two cautions are in the mechanics. First, retirement is not the only source of cores: FTAI holds 243 engines in its leasing fleet (10-K FY2025), it buys engines and modules for its aerospace business, and the research states that what limits feedstock is the condition and price of retired cores, which Part V §33 covers. Second, if the 14,200 figure counts only -7B engines (one dossier's reading), the 35% share describes one variant and not the fleet. Limits of the example: engines per unit is undisclosed; the bases may include spare and stored engines; the retirement rates are GE's for its CFM56 fleet and Safe Fly's on its own count; and the sub-1% figure is one quarter annualised. <span class="cite">[D8 §2.10; reconciliation R-001, R-002, R-004, C.8 item 1; E.1 rules 13 and 14; FTAI 10-K FY2025]</span></p></div>

<div class="exh"><div class="exh-title">Exhibit 9.12 — 100 Mod-1 cores a year as a share of CFM56 retirements, under each base and rate</div>

| Installed-base figure (source, level) | Retirements at 1.5% (GE, 2025 actual) | Retirements at 2% (GE, 2026 expected) | Retirements at 1% (GE, 1Q 2026 "below 1%", annualised) | 100 cores as share at 1.5% / 2% / 1% |
|---|---:|---:|---:|---|
| ~24,000 (Aviation Business News, Sept 2025, trade press) | 360 | 480 | 240 | 28% / 21% / 42% |
| ~23,000 (CFM website, undated, OEM page) | 345 | 460 | 230 | 29% / 22% / 43% |
| >22,800 (Safran FY2025 results, 13 Feb 2026, OEM investor material) | 342 | 456 | 228 | 29% / 22% / 44% |
| ~14,200 (Safe Fly Aviation, 2026, consultancy blog; all variants per D8, -7B only per D3) | 213 | 284 (Safe Fly's own "near 2%") | 142 | 47% / 35% / 70% |

<cite>Source: installed-base figures per reconciliation E.2 (CFM International website, undated; Aviation Business News, Sept 2025; Safran FY2025 Results & Investor Update, 13 Feb 2026; Safe Fly Aviation, "CFM56 Engine Market Report 2026"); retirement rates per GE Q4 2025 results via Leeham, 22 Jan 2026, GE CFO via Aviation Week, 2026, and GE Aerospace investor-relations page, 2026. All products and shares are derived in this Part; one gas generator per unit is assumed (D8 U3). Reconciliation R-001, R-002, R-004, R-069.</cite></div>

Two further comparisons the research made are carried with their labels. First, GE Aerospace expected CFM56 removals in the first half of 2027 to be about 10% above 2026 (GE via Aviation Week), which bears on the supply of cores in the year Mod-1 production is planned to reach 100. <span class="cite">[Aviation Week, "CFM56 Overhaul Demand Remains Strong", undated within 2026]</span> Second, Part III §24's row on the CFM56 plateau and later decline describes retirements normalising later in the decade, which is the period in which the stock of retired cores would grow; the research recorded that the timing depends on a retirement rate the manufacturers revised three times in one year. <span class="cite">[D9 §5; reconciliation R-004]</span>

### 74.4 Module-equivalents: Power against the Module Factory

The last derivation puts Power's feedstock beside the aerospace business it shares production with. FTAI's releases count three modules per engine (§69.4), so 100 whole engines are about 300 module-equivalents a year. <span class="cite">[FTAI release, 26 Feb 2025, via orchestrator notes; D8 §2.10; reconciliation B-3]</span>

<div class="worked"><div class="h">Worked example 9.7 — 300 module-equivalents against the 2026 module plan and the stated capacity</div>
<p>Inputs: 100 engines a year (derived, as above); three modules per engine (sourced: FTAI's convention, release of 26 Feb 2025) or four major modules (Part I §3's anatomical count, including the accessory gearbox); 2026 module target 1,050 (sourced: Q4/FY2025 release and call, Feb 2026) raised to 1,200 (sourced: call coverage of the Jul 2026 call, GuruFocus and Quartr; not returned from the release text); module capacity 3,000 a year (sourced: call coverage, Jul 2026, "supporting its 25% market share goal and 100 Mod-1 units annually"); FY2025 modules produced 757 (sourced: Q4 2025 call summaries).</p>
<div class="eqblock">module-equivalents, FTAI convention: 100 × 3 = 300 a year
module-equivalents, anatomical count: 100 × 4 = 400 a year
against the filed 2026 target: 300 ÷ 1,050 = 29%
against the raised 2026 figure: 300 ÷ 1,200 = 25%
against FY2025 output: 300 ÷ 757 = 40%
against the stated 3,000 capacity: 300 ÷ 3,000 = 10%</div>
<p>So the engines Power would consume at 100 units a year are, in module terms, about a quarter to three-tenths of the aerospace business's 2026 plan, two-fifths of its 2025 output, and a tenth of the capacity management described in July 2026 as supporting both businesses. Part VII §49 treats those four capacity and volume figures as separate dated statements with different footprints, and this example does not compare the 3,000 figure with the 2026 targets except as management linked them on the call. One mechanical point changes the comparison and depends on an undisclosed design choice: if a Mod-1 uses only the core and discards or does not need the fan and the low-pressure turbine (§68.2), then each unit consumes one core module and releases a fan module and a low-pressure-turbine module as feedstock for the Module Factory, in which case the 300 figure overstates the drain on module production by two-thirds. If the engine's own low-pressure turbine is used as the output turbine, two of the three modules are consumed. Limits of the example: the 1,200 and 3,000 figures are call coverage; the module convention has two readings; and the design choice is unknown. <span class="cite">[D8 §2.10, U3; reconciliation R-035, R-036, R-037; E.1 rules 2, 7 and 17; E.2]</span></p></div>

The arithmetic of this section, taken together, is what the reconciliation calls for: every figure that bears on FTAI Power's scale is derived from a small number of disclosed inputs, each derivation is shown under each contested base, and the three undisclosed inputs that would turn the derivations into facts are the unit count in the order, the engines per unit, and who consolidates J&F.

## Tensions carried in this Part

| Id | The two (or more) figures | Where in this Part |
|---|---|---|
| R-061 | J&F is "FTAI's joint venture with Jereh Group" (FTAI release, 22 Jul 2026) and "a strategic packaging and distribution joint venture" (FTAI 10-Q Q2 2026) against "its subsidiary, J&F Power Systems" (Jereh's SZSE disclosure via FilingReader, 22 Jul 2026); ownership and consolidating party undisclosed | §70.2, Exhibit 9.5; worked example 9.5 |
| R-062 | 2027 FTAI Power Adjusted EBITDA $450M (Q2 2026 release text; Quartr, MarketBeat) against "$450 million to $750 million" (GuruFocus summary of the same call) | §74.2, worked example 9.5; Exhibit 9.3 |
| R-001 | CFM56 installed base ~23,000 (CFM website, undated); ~24,000 (Aviation Business News, Sept 2025); >22,800 (Safran, end-2025); ~14,200 and >19,000 (Safe Fly, consultancy blog) | §74.3, worked example 9.6, Exhibit 9.12 |
| R-002 | Safe Fly's ~14,200 read as all CFM56 variants (D8) or as the -7B fleet alone (D3); changes the 35% feedstock share | §74.3, Exhibit 9.12 |
| R-004 | Retirement rate: GE planning 3–4% → 2–3% → 1.5–2% (CFO via Aviation Week, 2026); 2025 actual ~1.5%, 2026 expected ~2% (GE via Leeham, 22 Jan 2026); 1Q 2026 "below 1%" (GE investor-relations page); Safe Fly "near 2%" | §74.3, worked example 9.6, Exhibit 9.12 |
| R-069 | CFM56 deliveries >35,000 (CFM) against "well over 30,000" (D8, unsourced) | §74.3 |
| R-035 | Module count: three per engine (FTAI's convention, release 26 Feb 2025; D8) against four major modules anatomically (Part I §3) | §69.4, worked example 9.7 |
| R-036 | 2026 module target 1,050 (Q4/FY2025 release, Feb 2026) against 1,200 (call coverage of the Jul 2026 call) | worked example 9.7 |
| R-037 | Module capacity 3,000 a year "supporting ... 100 Mod-1 units annually" (call coverage, Jul 2026) against the filed 1,350 and 1,800 figures (releases 2024 and 2025) | §69.3, worked example 9.7 |
| D8 T1 | Customer: "a leading international cloud service provider" (FTAI release) against "a U.S. hyperscaler" (call summaries) | §70.4, Exhibit 9.5 |
| D8 T4 | GE Vernova backlog 50 / 83 / 100 / 116 GW at successive dates, with later figures including slot reservations; "2028–29" against "2031" horizons | §71.3, Exhibit 9.7 |
| D8 T5 | $/kW: $171–1,150 equipment-only and $1,175 installed (Gas Turbine World, undated); $600 turbine-only end-2027 (Wood Mackenzie); $2,000–2,500 plant-level (Power Engineering, 2026); $586–977 implied for Mod-1 | §72.1, Exhibit 9.9, worked examples 9.3 and 9.4, Exhibit 9.11 |
| D8 T6 | LM2500XPRESS 35 MW (GE Vernova release) against ~34.5 MW implied by 29 units at nearly 1 GW and 34 MW in a commissioning brief | §72, Exhibit 9.8 |
| D8 T8 | Mod-1 35–40% efficiency and ~9,000 heat rate are consistent (37.9%) only on one heating-value basis; basis unstated | §68.4, worked example 9.1 |
| D8 T9 | Mobile turbines as "nonroad engines" exempt from permitting (Shelby County) against stationary sources needing permits and controls (Southern Environmental Law Center, NAACP); unresolved in litigation | §73.2, Exhibit 9.10 |
| D8 T10 | Reciprocating engines "20–35% less fuel" and >50% efficiency (Wärtsilä, vendor claim) against Mod-1's 35–40% (FTAI, call coverage); both self-reported | §68.4, §72 |

## Unknowns carried in this Part

- **U-D8-01** (D8): **U1. Units and price in the $1.465B order.** Not disclosed. Would be resolved by FTAI's Q3 2026 10-Q or call, or by Jereh's SZSE filing if it states quantities.
- **U-D8-02** (D8): **U2. J&F ownership, control and consolidation.** Percentages, board, which party consolidates, and how FTAI recognises Power revenue (sale of turbines into J&F, share of J&F profit, or consolidated genset sales). The Q2 2026 10-Q [10] is the document to read; its J&F note was not returned by search. The orchestrator notes add the 10-Q's description of J&F as "a strategic packaging and distribution joint venture with Jereh Group ... to support the planned 2027 production target of 100 Mod-1 CFM56 aeroderivative units"; ownership split and consolidation not returned.
- **U-D8-03** (D8): **U3. Engines per unit and configuration.** How many CFM56 gas generators per 25 MW unit; -5B or -7B; whether the engine's own low-pressure turbine or a new free power turbine drives the generator; whether a booster stage replaces the fan.
- **U-D8-04** (D8): **U4. Where units are built.** Jereh packaging site(s); US vs China; tariff exposure; whether J&F has its own facility.
- **U-D8-05** (D8): **U5. Emissions and fuel.** NOx level, after-treatment (SCR or not), heating-value basis of the efficiency figure, dual-fuel capability.
- **U-D8-06** (D8): **U6. Capital required.** Power capex, engine inventory earmarked, test capacity; FTAI's engine input cost per unit.
- **U-D8-07** (D8): **U7. Segment reporting.** The 10-K FY2025 has two reportable segments [6]; call summaries speak of a "Power segment" for 2027. Whether Power is a third reportable segment from the Q2 2026 10-Q [10], or sits within Aerospace Products until first delivery, was not confirmed. (Cluster K-10 with U-D10-18, "Whether FTAI Power is a third reportable segment in the 2026 10-Qs.")
- **U-D8-08** (D8): **U8. Jereh's GenSystems orders.** MW count (to derive $/kW) and whether they use Mod-1 or other turbines; identity of the customer; relationship to J&F.
- **U-D8-09** (D8): **U9. Competitor figures not captured.** Siemens Energy SGT-A65 output/lead time; Solar Turbines Titan 350; Caterpillar gas gensets; Bloom Energy deal sizes and $/kW; published aeroderivative list prices in 2026.
- **U-D8-10** (D8): **U10. Milestone schedule.** Size of the advance payment and the percentage at each milestone.
- **U-D8-11** (D8): **U11. Performance adjustment.** Which metrics the 10% cap applies to (output, heat rate, availability, schedule) and whether it is symmetric (bonus as well as penalty).
- **U-D8-12** (D8): **U12. Service model.** Mod-1 inspection and overhaul intervals; service contract form and pricing; FTAI's expected service revenue per unit.
- **U-D8-13** (D8): **U13. Prior CFM56 stationary derivative.** None found; a definitive statement from GE/CFM or Gas Turbine World's handbook would settle whether Mod-1 is the first.
- **U-D8-14** (D8): **U14. Interconnection queue durations.** PJM and ERCOT queue statistics were not captured; they quantify the "bridging" window ProEnergy's customers describe as 5–7 years [64].
- **U-D8-15** (D8): **U15. Transcripts.** The Q4 2025 (26 Feb 2026) and Q2 2026 (29 Jul 2026) call transcripts were reached only through third-party summaries [15]–[19]; direct quotations on Power should be taken from the transcripts before publication.
- **U-D9-03** (D9): **U3 — Definition of the ~24,000 CFM56 "in service" figure [S78]** (installed only, or installed plus spares plus stored) and its split between -5B, -7B and the older -3/-5A/-5C variants. Resolve: GE Aerospace or CFM investor materials with a fleet breakdown; the GE Bernstein presentation (27 May 2026) [S6] may contain it but its content did not surface.

## Sources

1. FTAI Aviation, "FTAI Aviation Announces the Launch of FTAI Power", GlobeNewswire, 30 Dec 2025. https://www.globenewswire.com/news-release/2025/12/30/3211297/35538/en/FTAI-Aviation-Announces-the-Launch-of-FTAI-Power-FTAI-Adapts-the-World-s-Largest-Aircraft-Engine-Platform-to-Meet-AI-Driven-Power-Demand.html
2. FTAI Aviation, "FTAI Announces $1.465 Billion Gas Turbine Generator Set Order Through J&F Power Systems", GlobeNewswire, 22 Jul 2026. https://www.globenewswire.com/news-release/2026/07/22/3331360/35538/en/ftai-announces-1-465-billion-gas-turbine-generator-set-order-through-j-f-power-systems.html
3. Barchart, repost of the 22 Jul 2026 FTAI release, Jul 2026. https://www.barchart.com/story/news/3402927/ftai-announces-1-465-billion-gas-turbine-generator-set-order-through-jf-power-systems
4. Pulse2, "FTAI Secures $1.465 Billion Gas Turbine Generator Order Through J&F Power Systems", Jul 2026. https://pulse2.com/ftai-secures-1-465-billion-gas-turbine-generator-order-through-jf-power-systems/
5. FTAI Aviation Ltd., Form 10-K for the year ended 31 Dec 2025, filed 27 Feb 2026. https://www.sec.gov/Archives/edgar/data/1590364/000162828026012940/ftai-20251231.htm
6. FTAI Aviation, Q4/FY2025 earnings release (8-K exhibit 99.1), 25 Feb 2026. https://www.sec.gov/Archives/edgar/data/1590364/000162828026011685/ftai123125earningsrelease.htm
7. FTAI Aviation, Q1 2026 earnings release (8-K exhibit 99.1), 29–30 Apr 2026. https://www.sec.gov/Archives/edgar/data/1590364/000162828026028390/ftai3312026earningsrelease.htm
8. FTAI Aviation Ltd., Form 10-Q for the quarter ended 30 Jun 2026. https://www.sec.gov/Archives/edgar/data/0001590364/000162828026051412/ftai-20260630.htm
9. FTAI Aviation, Q2 2026 results release, GlobeNewswire, 29 Jul 2026. https://www.globenewswire.com/news-release/2026/07/29/3335598/35538/en/FTAI-Aviation-Ltd-Reports-Second-Quarter-2026-Results-Increases-Dividend-to-0-50-per-Ordinary-Share.html
10. FTAI Aviation, Q2 2026 earnings release as filed (8-K exhibit), 29 Jul 2026. https://www.sec.gov/Archives/edgar/data/1590364/000162828026050622/ftai6302026earningsrelease.htm
11. FTAI Aviation, "FTAI Aviation Announces Multi-Year Materials Agreement with CFM International to Further Support CFM56 Engines", GlobeNewswire, 22 Jan 2026. https://www.globenewswire.com/news-release/2026/01/22/3223741/35538/en/FTAI-Aviation-Announces-Multi-Year-Materials-Agreement-with-CFM-International-to-Further-Support-CFM56-Engines.html
12. FTAI Aviation, QuickTurn Europe and Q4/FY2024 results release, GlobeNewswire, 26 Feb 2025 (three-modules-per-engine convention, via orchestrator notes). https://www.globenewswire.com/news-release/2025/02/26/3033379/35538/en/
13. GuruFocus, "FTAI Aviation Ltd (FTAI) Q2 2026 Earnings Call Highlights", 30 Jul 2026 (call coverage). https://www.gurufocus.com/news/8991870/ftai-aviation-ltd-ftai-q2-2026-earnings-call-highlights-record-module-production-and-power-business-breakthrough-drive-growth-amid-strategic-shifts
14. Quartr, "FTAI Aviation (FTAI) Q2 2026 earnings summary", Jul 2026 (call coverage). https://quartr.com/events/ftai-aviation-ltd-ftai-q2-2026_ozdaN73d
15. MarketBeat, "FTAI Aviation Q2 Earnings Call Highlights", 30 Jul 2026 (call coverage). https://www.marketbeat.com/instant-alerts/ftai-aviation-q2-earnings-call-highlights-2026-07-30/
16. TheValueist (X), summary of the FTAI Q4 2025 earnings call, 26 Feb 2026 (call coverage, secondary). https://x.com/TheValueist/status/2027078155635503303
17. Aviation Week, "MRO Memo: FTAI Pitches CFM56 To Power AI Boom", early 2026. https://aviationweek.com/mro/emerging-technologies/mro-memo-ftai-pitches-cfm56-power-ai-boom
18. AviTrader, "FTAI unveils CFM56 Power platform", 2 Jan 2026. https://avitrader.com/2026/01/02/ftai-unveils-cfm56-power-platform/
19. AvioRadar, "CFM56 finds a new role as an AI data-center power source", 2026. https://avioradar.net/en/cfm56-finds-a-new-role-as-an-ai-data-center-power-source/
20. Yicai Global, "China's Jereh Rises After Landing USD341 Million Gas Turbine Generator Order for US Data Centers", 2026. https://www.yicaiglobal.com/news/chinas-jereh-rises-after-landing-usd341-million-gas-turbine-generator-order-for-us-data-center
21. FilingReader, "Yantai Jereh subsidiary secures $1.47bn turbine contract" (Shenzhen Stock Exchange disclosure), 22 Jul 2026. https://filingreader.com/news-wire/shenzhen/2026-07-22/yantai-jereh-subsidiary-secures-147bn-turbine-contract
22. Jereh Group, company history page, undated. https://jereh.com/en/about/history
23. PitchBook, Yantai Jereh Oilfield Services Group profile, undated. https://pitchbook.com/profiles/company/164739-43
24. PRNewswire, "Jereh Ships 7000 HP Electric Fracturing Fleet to Renowned US Oilfield Service Company", 2024. https://www.prnewswire.com/news-releases/jereh-ships-7000-hp-electric-fracturing-fleet-to-renowned-us-oilfield-service-company-302100418.html
25. PRNewswire, "BJ Energy Solutions takes delivery of fifth set of TITAN Hydraulic Fracturing Units from Jereh", 2025. https://www.prnewswire.com/news-releases/bj-energy-solutions-llc-takes-delivery-of-fifth-set-of-titan-hydraulic-fracturing-units-from-jereh-energy-equipment-and-technologies-corporation-302400515.html
26. PRNewswire, "AAR and FTAI Aviation extend their exclusive Serviceable Engine Products agreement ... through 2030", 2025 (title located; body not read). https://www.prnewswire.com/news-releases/aar-and-ftai-aviation-extend-their-exclusive-serviceable-engine-products-agreement-providing-cfm56-engine-material-to-the-global-aviation-aftermarket-through-2030-302412621.html
27. US Patent and Trademark Office, US 11,053,891, "Method for converting a turbofan engine". https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11053891
28. US Patent and Trademark Office, US 5,160,080, "Gas turbine engine and method of operation for providing increased output shaft horsepower". https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/5160080
29. US Patent and Trademark Office, US 6,895,325, "Overspeed control system for gas turbine electric powerplant". https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6895325
30. International Energy Agency, "AI is set to drive surging electricity demand from data centres while offering the potential to transform how the energy sector works", news release, Apr 2025. https://www.iea.org/news/ai-is-set-to-drive-surging-electricity-demand-from-data-centres-while-offering-the-potential-to-transform-how-the-energy-sector-works
31. International Energy Agency, "Energy and AI", executive summary, Apr 2025. https://www.iea.org/reports/energy-and-ai/executive-summary
32. Data Center Dynamics, "EIA: US electricity use to see largest four-year growth period since 2000, driven primarily by data center demand", 2026. https://www.datacenterdynamics.com/en/news/eia-us-electricity-use-to-see-largest-four-year-growth-period-since-2000-driven-primarily-by-data-center-demand/
33. Utility Dive, "Data center demand spike could drive 79% ERCOT price hike in 2027: EIA", 2026. https://www.utilitydive.com/news/data-center-demand-spike-could-drive-79-ercot-price-hike-in-2027-eia/814804/
34. US Energy Information Administration, Today in Energy #67344, 2026. https://www.eia.gov/todayinenergy/detail.php?id=67344
35. Enverus, "Off the grid, on the gas", 2026. https://www.enverus.com/newsroom/off-the-grid-on-the-gas/
36. S&P Global Commodity Insights, "Pipeline operators strike deals as data centers turn to colocated generation", 27 May 2026. https://www.spglobal.com/energy/en/news-research/latest-news/natural-gas/052726-pipeline-operators-strike-deals-as-data-centers-turn-to-colocated-generation
37. Power Engineering, "Data centers drive record surge in GE Vernova power equipment orders as turbine slots tighten through 2030", Jul 2026. https://www.power-eng.com/gas/turbines/data-centers-drive-record-surge-in-ge-vernova-power-equipment-orders-as-turbine-slots-tighten-through-2030/
38. Oilprice, "The Gas Turbine Shortage Just Became AI's Biggest Constraint", 2026. https://oilprice.com/Energy/Energy-General/The-Gas-Turbine-Shortage-Just-Became-AIs-Biggest-Constraint.amp.html
39. Oilprice, "Global Gas Turbine Orders Hit Record High as Power Demand Surges", 2026. https://oilprice.com/Latest-Energy-News/World-News/Global-Gas-Turbine-Orders-Hit-Record-High-as-Power-Demand-Surges.amp.html
40. GE Vernova, "GE Vernova raises multi-year financial outlook, doubles dividend and increases buyback authorization", BusinessWire, 9 Dec 2025. https://www.businesswire.com/news/home/20251209799497/en/GE-Vernova-raises-multi-year-financial-outlook-doubles-dividend-and-increases-buyback-authorization
41. Industrial Info Resources, "GE Vernova's Global Natural Gas Turbine Reservations and Order Backlog Grows to 100 GW", 2026. https://www.industrialinfo.com/iirenergy/industry-news/article/ge-vernovas-global-natural-gas-turbine-reservations-and-order-backlog-grows-to-100-gw--356705
42. Yahoo Finance, "GE Vernova Backlog Hits 50 GW", 2025. https://finance.yahoo.com/news/ge-vernova-backlog-hits-50-082001096.html
43. Energy News Beat, "Siemens gas turbine backlog nears 70 GW as company expands manufacturing", 2026. https://energynewsbeat.co/electrical-generation/siemens-gas-turbine-backlog-nears-70-gw-as-company-expands-manufacturing/
44. Power Engineering, "Gas turbine prices climb 195% as supply crunch reshapes power development", 2026. https://www.power-eng.com/gas/turbines/gas-turbine-prices-climb-195-as-supply-crunch-reshapes-power-development/
45. Gas Turbine World, "How much does it cost to build a Simple Cycle or Combined Cycle plant?", undated. https://gasturbineworld.com/?p=6191
46. Gas Turbine World, "Capital Costs for Utility Scale Gas Turbine Plants", undated. https://gasturbineworld.com/?p=2855
47. GE Vernova, "GE Vernova, Crusoe announce major 29-unit aeroderivative gas turbine deal to deliver AI data centers", 22 Jul 2025. https://www.gevernova.com/news/press-releases/ge-vernova-crusoe-announce-major-29-unit-aeroderivative-gas-turbine-deliver-ai-data-centers
48. Turbomachinery International, "GE Vernova delivers 29 LM2500XPRESS aeroderivative gas turbine packages to Crusoe AI data centers", undated. https://www.turbomachinerymag.com/view/ge-vernova-delivers-29-lm2500xpress-aeroderivative-gas-turbine-packages-to-crusoe-ai-data-centers
49. World Oil, "Baker Hughes wins major gas turbine order for data center, oil and gas power", 29 Jul 2026. https://worldoil.com/news/2026/7/29/baker-hughes-wins-major-gas-turbine-order-for-data-center-oil-and-gas-power/
50. Bloomberg Government, "Baker Hughes Doubles Data Center Order Target to $3 Billion", undated. https://news.bgov.com/texas-brief/baker-hughes-doubles-data-center-order-target-to-3-billion
51. Data Centre Magazine, "Can Old Aeroplane Engines Powering Data Centres Take Off?", undated. https://datacentremagazine.com/news/can-old-aeroplane-engines-power-data-centres-take-off
52. EEPower, "Can repurposed jet engines solve AI data center power problems?", undated. https://eepower.com/news/can-repurposed-jet-engines-solve-ai-data-center-power-problems/
53. Wärtsilä, data centre power solutions product page, undated. https://www.wartsila.com/energy/solutions/flexible-baseload-power-plants/data-centre-power-solutions
54. Wärtsilä, "Wärtsilä continues growth in the data center segment with a 507 MW order in the US", 20 Nov 2025. https://www.wartsila.com/dnk/media/news/20-11-2025-wartsila-continues-growth-in-the-data-center-segment-with-a-507-mw-order-in-the-us-offering-engines-as-a-reliable-power-solution-3686573
55. Bloom Energy Corp., Form 10-K for the year ended 31 Dec 2024. https://www.sec.gov/Archives/edgar/data/1664703/000162828025008747/be-20241231.htm
56. TechCrunch, "xAI gets permits for 15 natural gas generators at Memphis data center", 3 Jul 2025. https://techcrunch.com/2025/07/03/xai-gets-permits-for-15-natural-gas-generators-at-memphis-data-center
57. E&E News, "Musk's xAI gets air permit for Memphis supercomputer", Jul 2025. https://www.eenews.net/articles/musks-xai-gets-air-permit-for-memphis-supercomputer/
58. Data Center Dynamics, "xAI facing lawsuit over use of gas turbines at Memphis supercomputer", 2025. https://datacenterdynamics.com/en/news/xai-facing-lawsuit-over-use-of-gas-turbines-at-memphis-supercomputer
59. Data Center Dynamics, "xAI doubles number of onsite gas turbines at Memphis data center in violation of permit limits", 2025. https://datacenterdynamics.com/en/news/xai-doubles-number-of-onsite-gas-turbines-at-memphis-data-center-in-violation-of-permit-limits
60. Tennessee Lookout, xAI permitting coverage, 2025. https://tennesseelookout.com/?p=27979
61. Safe Fly Aviation, "CFM56 Engine Market Report 2026" (consultancy blog), 2026. https://safefly.aero/cfm56-engine-market-report-2026/
62. Aviation Week, "CFM56 Overhaul Demand Remains Strong, GE Aerospace Says", 2026 (exact date not visible). https://aviationweek.com/mro/aircraft-propulsion/cfm56-overhaul-demand-remains-strong-ge-aerospace-says
63. Leeham News, "GE Aerospace FY and Q4 2025 Earnings Thrust Higher Propelled by Services Growth, LEAP Volume and Expanding Margins", 22 Jan 2026. https://leehamnews.com/2026/01/22/ge-aerospace-fy-and-q4-2025-earnings-thrust-higher-propelled-by-services-growth-leap-volume-and-expanding-margins/
64. GE Aerospace Investor Relations, "Recent events: your questions answered", 2026. https://www.geaerospace.com/news/investor-relations/ir-updates/recent-events-your-questions-answered
65. Aviation Business News, "CFM56 turbofan aircraft engine" (about 24,000 in service, Sept 2025). https://www.aviationbusinessnews.com/low-cost/cfm56-turbofan-aircraft-engine/
66. CFM International, "The CFM56 engine family", undated, accessed 2026-10-03. https://www.cfmaeroengines.com/engines/cfm56
67. Safran, FY2025 Results & Investor Update presentation, 13 Feb 2026. https://www.safran-group.com/download/media/450393
68. IBA, "Engine Values Release September 2025 (2025B)", Sept 2025. https://www.iba.aero/resources/articles/engine-values-2025b-release-september-2025/
69. Research dossiers and notes for this primer: D8 (FTAI Power), D9 §2.2 and §5 (installed base; translation table), D5 §2.4 (module capacity), D10 §4.8 (guidance history), D1 §2.1 (the machine); orchestrator notes (10-Q Q2 2026 wording on J&F; 2027 guidance split); reconciliation sections A.1, A.4, A.6, C.8, D and E. Cited only where the dossier itself produced a derived figure or a definition.
