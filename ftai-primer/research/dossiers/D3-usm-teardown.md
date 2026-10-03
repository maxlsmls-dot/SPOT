# D3 — Used serviceable material (USM), teardown and part-out economics

Dossier for the FTAI Aviation deep primer. Written 2026-10-03. WebSearch calls used: 18 of 18
(WebFetch blocked; every figure below comes from search-returned page content, cited by publisher,
document, date and URL). Posture: explain, do not opine. Sources are labelled primary (SEC filing,
company document), appraiser, trade press, or market-research vendor. Where a source gives a range,
the range is reported, not a midpoint.

---

## 1. Summary

- **USM** (used serviceable material) is a part taken from a retired or torn-down aircraft or engine, inspected and if needed repaired to the manufacturer's manual, and released on an airworthiness tag (FAA 8130-3 or EASA Form 1) with full history, so it can be installed again. A part with a gap in its paperwork is scrap, whatever its physical condition.
- Teardown arithmetic (trade press, 2026): an exhausted CFM56 bought for $0.8–1.2M yields $1.6–2.2M of USM, a net $0.4–0.8M per engine (Safe Fly Aviation, 2026).
- Engine values (appraiser): CFM56-7B24 half-life market value $5.7M, CFM56-7B27 $6.4M for H2 2025 (IBA, Sept 2025). IBA's H1 2026 update says -5B and -7B values "levelled off" after about 18 months of increases.
- Lease rates (trade press, 2026): CFM56-7B $42,000–48,000 per month (about 34% above 2019), CFM56-5B $38,000–44,000 per month (Safe Fly Aviation, 2026). V2500-A5 $70,000–80,000 per month (IBA, Sept 2025).
- USM pricing versus new: 60–80% of a new part's price on average; up to 85% of OEM catalogue list price (CLP) for high-demand parts early in a life cycle; traders sell repaired USM at 70–75% of CLP; above CLP when the OEM cannot deliver (Aviation Week; Aircraft Commerce). CFM raised its catalogue list price in August 2023 (Aviation Week, 2024).
- Supply: aircraft retirements fell from 502 (2019) to 465, 333 and 325 in 2020–2022 (Cirium Fleets Analyzer); 2024–2026 retirement rates about 24% below the 2010–2019 norm; normal retirements (about 2.7% of the fleet a year) expected from 2028 (McKinsey). 1,190 A320ceo-family and 795 737NG aircraft are projected to be 35% of retirements over five years (Cirium).
- Market size 2025 (vendors disagree): $5.87B (The Business Research Company), $7.7B (Market.us), $8.55B (Fortune Business Insights).
- SEC filers: AerSale 2025 revenue $335.3M, USM $137.6M, flight-equipment sales $56.4M from 13 engines (AerSale, 5 Mar 2026). AAR FY2026 (year to 31 May 2026): Parts Supply about 45% of sales; USM activity up 32.1% (AAR 10-K).
- FTAI tears down engines it judges unserviceable for leasing, rebuilds salvageable components into modules, and sells serviceable used modules and parts "through an exclusive partnership" (FTAI FY2025 10-K).

---

## 2. Mechanics

### 2.1 What USM is and how a used part becomes "serviceable"

**Used serviceable material (USM)** is any aircraft or engine part that has been in service, has been removed, and has been inspected (and repaired if needed) so that it is legally fit to be installed again. The alternative sources of a replacement part are a **new OEM part** (made by the original equipment manufacturer, sold at **catalogue list price**, or **CLP**, the OEM's published price), a **PMA part** (a part made by a third party under an FAA Parts Manufacturer Approval; see dossier D4), or a **DER repair** (a repair scheme approved by an FAA Designated Engineering Representative rather than by the OEM manual; D4).

A part leaves service in one of three ways: it is removed at a **shop visit** (an engine's trip to a repair shop, D1/D2), it is removed from an aircraft at **retirement**, or the whole aircraft or engine is **torn down** (dismantled for parts, also called **part-out**). From there each part goes one of three ways:

1. **Serviceable as removed.** Inspected to the applicable manual and found within limits. Tagged and sold.
2. **Repairable.** Outside limits but repairable under the **Component Maintenance Manual (CMM)** for airframe components, or the **Engine Shop Manual (ESM)** for engine parts, or under an approved DER scheme. Sent to a repair shop, repaired, tested, then tagged and sold. The repair cost is the main cost of goods for a USM trader.
3. **Beyond economic repair (BER) or life-expired.** Scrapped. For a **life-limited part (LLP)** — a rotating part with a hard cycle limit set by the OEM, after which it must be retired regardless of condition (D1) — "life-expired" means the cycle limit has been reached; a life-expired LLP has no USM value and must be mutilated so it cannot re-enter the supply chain.

**The release tag.** A part becomes "serviceable" in the legal sense when an approved organisation signs it off. In the FAA system this is **FAA Form 8130-3**, the Authorized Release Certificate / Airworthiness Approval Tag, issued by an FAA-certificated repair station (14 CFR Part 145) for a repaired or inspected part, or by a production approval holder for a new one. In the EASA system the equivalent is **EASA Form 1**, issued by a Part-145 or Part-21 organisation. Both certify that the part complies with the applicable regulations and is safe for use (Rotabull, 8130-3 instructions; AJW/AviTrader, Aug–Oct 2025). Many repair stations hold both approvals and issue a **dual release** (one tag valid for both systems), which matters because a part tagged for one system only cannot be installed on an aircraft registered in the other without re-certification.

**Traceability.** A tag is necessary but not sufficient. The buyer also needs the part's documented history. The trade-press description of the regulatory position is blunt: no regulator allows "untraceable" used parts, and everything must be documented, certified and compliant (AJW/AviTrader, 2025). The documentation package differs by part class:

- **Hard-time (HT) parts** — parts with a fixed overhaul or replacement interval — and **LLPs** require complete records that tell the part's operating history and remaining life, plus evidence of compliance with **Airworthiness Directives (ADs)** (mandatory regulator-issued fixes) and **Service Bulletins (SBs)** (OEM-issued modifications) (AJW/AviTrader, 2025).
- For LLPs the standard is **back-to-birth traceability**: an unbroken record of every cycle the part has accumulated since new, on which engine serial numbers and under which operators. Remaining life is the OEM limit minus documented cycles consumed; any undocumented period cannot be assumed to be zero cycles, so a gap means the part cannot be shown to have life and has no value.
- Other standard documents in a USM package: the removal tag from the last operator, a **non-incident statement** (a declaration that the part was not on an aircraft involved in an accident, fire or immersion), the teardown report, and a certificate of conformance from the seller.

**What makes a part unsaleable.** From the sources read: missing documents mean the part will not be used; an unclear maintenance history or gaps in the paperwork are grounds for rejection; mismatched part or serial numbers, unusual formatting on a tag, or an unfamiliar issuing organisation trigger **quarantine** (the part is segregated pending investigation) (FL Technics; AJW/AviTrader, 2025). The same sources note that 8130-3 and Form 1 documents "can be easily generated", so buyers vet the supplier as well as the paperwork (AJW/AviTrader, 2025). Delta's supplier matrix for aftermarket parts (Delta, Mar 2024) is one example of an airline codifying which supplier categories and tag types it accepts.

### 2.2 Teardown and part-out economics

**Feedstock** is the trade term for the aircraft and engines bought (or taken on consignment) to be torn down. There are two commercial routes:

- **Purchase.** The teardown company buys the asset outright and owns the parts. It bears the capital cost and inventory risk and keeps the margin. AerSale, GA Telesis and AAR's trading arm do this; lessors such as Willis Lease and AerCap feed their own retired lease assets into their own material subsidiaries.
- **Consignment.** The owner (airline, lessor, bank, insurer) keeps title; the teardown company dismantles, certifies, stocks and sells the parts for a fee or commission. Willis Aero describes its business as "the acquisition or consignment of aircraft and engines" (Willis Lease FY2025 10-K); APOC's 737-800 teardown with Willis mentions "packages of parts available for sale and consignment" (Asian Aviation).

**Where the value sits.** The engines dominate the part-out value of a mature narrowbody; the engine-only figures below (two engines yielding $3.2–4.4M of USM) sit against a single airframe item, the landing gear, that fetches "over $1 million" fully overhauled (ISTAT Jetrader, Autumn 2020). A sourced percentage split between engines and airframe was not captured this session (Unknown U1). Within the airframe the high-value items are the landing gear, the **APU** (auxiliary power unit, the small turbine in the tail that supplies ground power and air), thrust reversers, avionics boxes, flight-control actuators, and wheels and brakes — all **rotables**, parts that are repaired and reused rather than consumed. Within an engine the value sits in (a) LLPs with remaining cycles — fan, booster and compressor disks, shafts and spools — because the next shop visit must replace any LLP without enough life for the following interval and a used disk with life is the direct substitute for a new one at CLP; (b) high-pressure turbine (HPT) blades and nozzles and high-pressure compressor (HPC) airfoils, the most expensive repairable parts; (c) fan blades; (d) cases and structural parts; and (e) accessories such as the **HMU** (hydro-mechanical unit, the engine's fuel-metering unit). Safe Fly's 2026 teardown report lists CFM56 fan disks, HMUs and structural engine parts as the most searched-for items (Safe Fly, 2026, trade/secondary).

**The teardown numbers (trade press, 2026).** Safe Fly Aviation's CFM56 Engine Market Report 2026 gives: an **exhausted** engine (one with no usable time left before a shop visit, i.e. **run-out**) purchased for $0.8–1.2M can yield $1.6–2.2M in USM, for a per-engine net margin of $0.4–0.8M (Safe Fly, 2026). Worked through:

| Case | Purchase | USM yield | Yield minus purchase | Stated net margin | Implied teardown, repair, certification and selling cost (inference, not stated by source) |
|---|---|---|---|---|---|
| Low | $0.8M | $1.6M | $0.8M | $0.4M | $0.4M |
| High | $1.2M | $2.2M | $1.0M | $0.8M | $0.2M |

The implied cost column is arithmetic on the source's endpoints, not a figure the source gives; it is included only to show that roughly a fifth to a quarter of gross USM proceeds is consumed by the repair, test, tagging and sales effort in that source's framing (Safe Fly is a trade/secondary source; see Tensions T3 on how its figures sit against appraiser values).

**Time to monetise.** A 737-800 teardown takes about three months, during which all parts are assessed by technical teams before being sent to specialist repair shops for overhaul, testing and re-certification; landing gear are among the first serviceable parts to become available; the APU is sold, and parts are offered as packages for sale and consignment (Asian Aviation / AirlinerGS, APOC–Willis 737-800 teardown). Sale proceeds therefore arrive in layers: whole modules and LLPs with life can be sold to an engine shop almost immediately; repaired rotables arrive after shop turnaround; the long tail of slow-moving airframe parts sells over years. A sourced figure for the total sell-through period was not captured (Unknown U2).

**Teardown as the end of a lease.** The APOC–Condor transaction shows the standard sequence for an engine lessor: APOC leased a CFM56-5A to Condor for twelve months on a **green-time lease**, with the engine "expected to return to APOC's portfolio for teardown and part-out next year after the lease concludes" (AviTrader, 28 Jul 2025; Aviation Business News). APOC acquired its first CFM56-5B for "up-cycling" (its term for teardown and material sale) in October 2021 (AviTrader, 7 Oct 2021), has disassembled two CFM56-7Bs (Aviation Business News), bought four "young" 737 airframes from a large US legacy carrier for teardown (Aviation Business News), and bought a 15-year-old A320-200 from FTAI for disassembly in May 2026 at Tarmac Aerosave's Toulouse-Francazal facility (ePlaneAI). That last item is a direct data point on FTAI as a feedstock seller as well as buyer.

### 2.3 Green time

**Green time** is the remaining usable life on an engine before its next mandatory shop visit. It is set by whichever of three clocks runs out first: (1) the LLP with the fewest cycles remaining — the engine must come off wing before any LLP reaches its limit; (2) **EGT margin**, the gap between the exhaust gas temperature the engine runs at and its red-line limit, which erodes as the engine deteriorates (D1); (3) any hard-time inspection or AD. A **green-time engine** is one that still has usable time but whose owner does not intend to pay for the next shop visit, either because the engine is near the end of its life or because the owner's fleet is leaving. It is sold or leased "as-is" to run down the remaining time, and is then torn down.

**How green-time engines are traded and leased.** A green-time lease is a short fixed-term operating lease (months to a few years) at a monthly rent, with the engine returned at or near run-out rather than restored. Because the lessee will not restore the engine, the rent is effectively the price of the time consumed. Current rents (trade press, 2026): CFM56-7B $42,000–48,000 per month, roughly 34% above 2019 levels and up 15–20% "in recent months"; CFM56-5B $38,000–44,000 per month (Safe Fly, 2026). IBA's September 2025 release describes the CFM56-7B market as having "a distinct lack of availability", with both market values and lease rates above long-term trend (IBA, Sept 2025).

Worked example — the owner's choice at the end of a lease. Take a CFM56-7B with twelve months of green time at $45,000 per month (the midpoint of the Safe Fly range, used only for illustration).

- Lease it out for twelve months: 12 × $45,000 = $540,000 of rent, then tear it down for $1.6–2.2M of USM (Safe Fly, 2026). Gross proceeds $2.14–2.74M, spread over roughly a year plus the sell-through period.
- Tear it down now: $1.6–2.2M, sooner but with no rent. The LLPs with twelve months of cycles left are worth slightly more in a teardown than they will be after another year of flying, since their remaining life is what a buyer pays for; the airfoils and cases are worth the same either way.

Which is chosen depends on the owner's cost of capital, the lease rate, and whether an engine shop will pay more for the LLP life now than a lessee will pay in rent. The rate at which green-time rent compares with the engine's value is the **lease rate factor** (monthly rent divided by value): $45,000 ÷ $6.4M (the IBA half-life market value of a -7B27) = 0.70% per month, or 8.4% a year before any maintenance reserve. That calculation mixes bases — the rent is for a green-time engine and the value is for a half-life engine — which is one reason appraisers quote both separately (see 2.4 and Tension T3).

### 2.4 Engine valuation conventions

Definitions as used by appraisers (the ISTAT definitions are the common reference; the search did not return the ISTAT text itself, so the definitions below follow the Cargo Facts / Aircraft Value News usage captured):

- **Full life**: all maintenance tasks are fresh and all LLPs have 100% of life remaining. "Theoretical, even on a new aircraft" (Mark Calver, Cargo Facts Session 3, Apr 2023), because a new engine has already consumed test cycles and a full-life engine would need every LLP at zero cycles.
- **Half life**: all scheduled maintenance events are at their mid-point and all life-limited components are at the mid-point of ultimate life (Calver, Apr 2023). Appraisers quote base and market values at half life so that values are comparable across engines of different maintenance status.
- **Base value**: the appraiser's opinion of the underlying economic value of the asset in an open, unrestricted, stable market with a balance of supply and demand, assuming half-life maintenance status unless stated.
- **Market value**: the appraiser's opinion of the most likely trading price in the actual current market between willing, informed parties, again at half life unless stated. Market value sits above base value in a tight market (as IBA says it does for CFM56 now) and below it in a soft one.
- **Maintenance-adjusted value**: the half-life value plus or minus the value of the engine's actual maintenance status. For an engine the adjustment has two parts: the performance-restoration clock (hours or cycles since the last restoration shop visit, relative to the expected interval, multiplied by the shop-visit cost) and the LLP clock (cycles remaining on each LLP, relative to half life, multiplied by the LLP's cost per cycle). An engine with full-life LLPs is worth the half-life value plus half the full-life LLP value; a run-out engine is worth the half-life value minus half the LLP value minus half a shop visit — which, for an old engine, is approximately the teardown value.

Worked LLP adjustment, using the figure captured: for an A320 with CFM56-5B engines, the engine LLP cost is $9,878,733 at full life and $4,939,366 at half life, in 2023 dollars (Calver, Apr 2023; the excerpt does not state whether this is per engine or for the aircraft's two engines — Unknown U3). Taking it as the pair, $4.94M per engine at full life and $2.47M at half life. An engine whose LLPs average 75% life remaining is worth 0.25 × $4.94M = $1.23M more than the half-life value; one at 25% is worth $1.23M less. The same arithmetic is what an engine shop uses to price a used LLP: a disk with 60% of its life left is worth roughly 60% of its CLP, less a discount for being used (see 2.5).

The 2013 reference captured for the CFM56-7B — "a full set of LLPs for a CFM56-7B has a list price of $1.7 million" (Aircraft Commerce, Issue 87, 2013) — is far below the 2023 figure for the -5B and should not be used for current arithmetic (Tension T4).

Two complications that appraisers themselves flag: Aircraft Value News argues that the half-to-full-life concept becomes "fluid" as aircraft pass mid-life, because the market stops paying for maintenance status it will never use on an aircraft nearing retirement (Aircraft Value News, "Concept of half to full life fluid as aircraft move past mid-life"); and that PMA parts "continue to undermine full-life maintenance adjustments" because an engine fitted with cheaper PMA parts carries less replacement value than the OEM-CLP-based adjustment implies (Aircraft Value News, "PMA continues to undermine full-life maintenance adjustments"; see D4).

**Current appraiser figures.** IBA's September 2025 engine-values release (its "2025B" set) gives half-life market values for H2 2025 of $5.7M for the CFM56-7B24 and $6.4M for the CFM56-7B27 (the suffix is the thrust rating in thousands of pounds: 24,000 lbf and 27,000 lbf; higher ratings are worth more because they serve the heavier 737-800/-900 and can be de-rated, while a -7B24 cannot be up-rated without paying the OEM). The same release gives V2500-A5 lease rates of $70,000–80,000 per month and says 2025 was a year of "both increased transaction pricing and lease rates" for the CFM56-5B/-7B and V2500-A5 (IBA, Sept 2025). IBA's H1 2026 update says values for the CFM56-5B and -7B "have levelled off after approximately 18 months of increases" (IBA, H1 2026). Earlier IBA commentary called it "a lessors' market" as engine lease rates and market values escalated (IBA / AviTrader, 25 Apr 2024), and a 2025 IBA-sourced article says engine shortages and the MRO backlog keep values and lease rates elevated (Aerospace Innovations, date not captured). Ishka's quarterly engine-price survey reported, for a Q2 whose year the result did not show, that V2500 lease rates dipped while CFM56-5B rates strengthened (Ishka). ePlaneAI reports CFM56 values up "as much as 50% over the past two years" and that traditional valuation benchmarks have become less reliable, with each engine's value shaped by component condition, maintenance history, utilisation and prevailing lease rates (ePlaneAI, date not captured). Ascend by Cirium figures captured concern retirements rather than values (2.6). No mba Aviation figures were returned (Unknown U4). No numeric CFM56-5B half-life value from an appraiser was returned (Unknown U5).

### 2.5 USM pricing relative to new OEM parts

USM is priced as a discount to the OEM's catalogue list price, so it inherits the OEM's annual escalation. The captured figures:

- On average a USM part is 60–80% of the price of a new part (Aviation Week, "MRO Memo: A Seller's Market for Used Parts").
- Early in a platform's life cycle, high-demand USM parts can be marketed at 85% of OEM CLP; if the OEM has supply-chain problems, USM "can sell for more than the catalog list price" (Aviation Week, same).
- A specialist engine trader will typically sell repaired USM to airlines at 70–75% of CLP (Aircraft Commerce, Issue 120 maintenance article).
- The upward pricing trend is "most evident on CFM56 and V2500 platforms", driven by rising demand, falling supply of both new parts and USM, and rising repair costs; CFM increased the catalogue list price in August 2023, "a notable shift in pricing strategy for this platform" (Aviation Week, "Magnetic expects CFM56 market challenges, opportunities 2024").

Worked example. A CFM56-7B HPT stage-1 disk (an LLP) at CLP of X (the actual CLP was not captured — Unknown U6) with 70% of its cycle life remaining: the life-proportional value is 0.70 × X; at the 70–75% trader discount the USM price is 0.49–0.53 × X. A buyer facing an OEM lead time of a year for the new disk may pay 0.70 × X or more, which is the "above CLP" case the trade press describes in life-adjusted terms. The mechanism matters more than the specific disk: the discount to CLP narrows when the OEM's own supply is constrained, and widens when retirements flood the market with used parts.

### 2.6 Why supply depends on retirements, and what happened 2023–2026

USM comes from aircraft and engines that leave service; the supply of USM is therefore a function of the retirement rate, lagged by the teardown and certification period. The decision to retire a CFM56 is itself an economic one: Aviation Week describes the rule of thumb that a CFM56 needs a shop visit roughly every eight years, so the 24-year mark becomes a de facto retirement date because a third full overhaul is "deemed too expensive"; 737NG deliveries began in 1997 and ran at about 230 a year in 1998–2002, with A320ceo deliveries at a similar rate, so from 2022 the aircraft and engines from that period began entering their prime retirement window (Aviation Week, "Retirement Uptick Will Restock Used Engine Parts").

The history and forecast captured:

- Cirium's Fleets Analyzer recorded 502 aircraft retirements in 2019, then 465, 333 and 325 in 2020, 2021 and 2022. Over 2010–2019 the average annual part-out volume was just under 540 aircraft, with a high of 694 in 2013 (Cirium / IATA MCC presentation by Aerodynamic Advisory).
- Retirement rates in 2024–2026 are about 24% lower than in 2010–2019; from 2028 retirements are expected to return to about 2.7% of the fleet a year as supply-chain problems ease and new-generation deliveries ramp up (McKinsey, "What does the future hold for commercial-aviation maintenance?").
- 1,190 A320ceo-family and 795 737NG aircraft are projected to account for 35% of retirements over the next five years; by 2040 about 72% of all 737NGs will be retired (Cirium / Ascend by Cirium; publication date not captured).
- The A320ceo, 737NG, 777 and A330 were projected to account for about half of all retirements through 2025 (Cirium / Informa Markets forecast page; date not captured).

The mechanism behind the 2023–2026 shortage, as the sources describe it: airlines kept CFM56-powered aircraft flying longer because new narrowbody deliveries slipped and new-generation engines spent time off wing (D9), so the expected post-2022 retirement wave did not arrive; retirements stayed well below the 2010–2019 norm; the engines that would have been feedstock were instead leased as green-time engines or overhauled; and teardown companies competed for a smaller pool. AerSale's management described a "hypercompetitive feedstock environment, marked by increased scrutiny and pressure on pricing as more companies enter the teardown sector" (as relayed in search results citing AerSale). The observable consequences in the figures captured: CFM56 values up as much as 50% in two years (ePlaneAI); CFM56-7B rents 34% above 2019 (Safe Fly); AerSale's whole-asset sales falling from 20 engines and one aircraft (2024) to 13 engines (2025) (AerSale, 5 Mar 2026). Oliver Wyman's July 2020 piece "A tsunami of used aircraft parts" forecast the opposite (a glut from pandemic retirements); only its title was captured, so its figures are not reported here.

### 2.7 The module as a unit of trade

A **module** is one of the pre-assembled sections an engine is designed to split into: for the CFM56-7B the major modules are the fan and booster (low-pressure compressor), the core (high-pressure compressor, combustor, high-pressure turbine), the low-pressure turbine, and the accessory gearbox (D1 has the full anatomy). The design allows a shop to remove one module and fit another without disassembling the rest of the engine, which is what makes a module a tradeable object.

A serviceable module from a torn-down engine is valued the same way a whole engine is, in miniature: the sum of its serviceable parts (airfoils, cases, bearings, seals, at USM discounts to CLP) plus the remaining life of the LLPs inside it, less the cost of any repair needed to make it serviceable as a unit. A core module with HPT disks at 80% life is worth far more than one at 20% life, because the next owner's shop visit will or will not have to open it to replace them. The module's documentation must show the history of every LLP inside it.

**Module exchange** is a transaction in which an engine shop or operator hands over a time-expired or damaged module and receives a serviceable one, paying an exchange fee plus the difference in LLP life between the two. The incoming module becomes feedstock: the exchange provider tears it down, salvages the serviceable parts and LLP life, rebuilds, and puts it back in the exchange pool. For the shop it converts a full shop visit (open the whole engine, replace parts, re-assemble, test) into a shorter module swap; for the provider it is a way to sell USM and LLP life at module prices, which carry the premium of avoided downtime.

FTAI's filings describe this model directly. The Aerospace Products segment "develops and manufactures, repairs/refurbishes, and sells aircraft engines and aftermarket components primarily for the CFM56-7B, CFM56-5B and V2500" through its facilities and joint ventures; the business "focuses on the manufacturing and sale of new assets through the use of inventory purchased from third parties and salvaged modules and parts from generally unserviceable engines"; engines are "transferred to inventory when determined to be unserviceable for leasing purposes with the intent to tear down the asset into salvageable components that would be manufactured into new modules and parts and sold"; and "serviceable used modules and parts are sold through an exclusive partnership responsible for the teardown, repair, marketing and sales of parts from the CFM56 engine pool" (FTAI Aviation FY2025 10-K). The company calls the combined offering its Maintenance, Repair and Exchange (MRE) business (D5). The identity of the exclusive partner is not named in the excerpt returned (Unknown U7).

### 2.8 Worked example: part-out of a 737-800 with two CFM56-7B engines

The sourced inputs are set out first; inputs that could not be sourced are marked and are not filled with guesses.

| Input | Figure | Source and date |
|---|---|---|
| Airframe purchase price (mid-life or older 737-800 bought for part-out) | not captured | Unknown U8 |
| Engine purchase price, run-out CFM56 (each) | $0.8–1.2M | Safe Fly, CFM56 Engine Market Report 2026 (trade/secondary) |
| Engine USM yield, run-out CFM56 (each) | $1.6–2.2M | Safe Fly, 2026 |
| Engine net margin after teardown (each) | $0.4–0.8M | Safe Fly, 2026 |
| Half-life market value, CFM56-7B24 / -7B27 (reference ceiling if the engine has life) | $5.7M / $6.4M | IBA, Engine Values 2025B, Sept 2025 (appraiser) |
| Green-time rent, CFM56-7B | $42,000–48,000 per month | Safe Fly, 2026 |
| Precedent green-time lease term | 12 months (CFM56-5A) | AviTrader, 28 Jul 2025 |
| CFM56-5B LLP value, full life / half life (A320; per engine or per pair unclear) | $9,878,733 / $4,939,366 (2023 $) | Calver, Cargo Facts, Apr 2023 |
| Landing gear, fully overhauled set | "over $1 million" | ISTAT Jetrader, Autumn 2020 |
| Landing gear overhaul cost | up to $400,000 | ISTAT Jetrader, Autumn 2020 |
| Airframe teardown duration | about 3 months | Asian Aviation / AirlinerGS, APOC–Willis 737-800 teardown |
| Teardown labour and facility cost | not captured | Unknown U9 |
| APU, avionics, thrust reverser and other rotable values | not captured | Unknown U10 |
| Total sell-through period | not captured | Unknown U2 |

Step 1 — engines, both run-out. Purchase 2 × $0.8–1.2M = $1.6–2.4M. USM yield 2 × $1.6–2.2M = $3.2–4.4M. Net margin per the source 2 × $0.4–0.8M = $0.8–1.6M. These are the Safe Fly ranges applied to a pair; they are not independent observations.

Step 2 — engines with green time. If one engine has twelve months of green time, the owner can lease it at $42,000–48,000 per month for $504,000–576,000 before tearing it down; the purchase price of such an engine would be higher than a run-out engine by roughly that rent stream, since that is what the seller is giving up. If an engine is close to half life (fresh restoration, LLPs around 50%), its $5.7–6.4M market value (IBA) is several times its teardown yield, and a rational owner sells or leases it whole rather than tearing it down — which is why only run-out or near-run-out engines become teardown feedstock, and why teardown feedstock dries up when half-life engines are scarce and expensive (2.6).

Step 3 — LLP life inside the modules. For each engine the LLP value at the time of teardown is the sum over LLPs of (cycles remaining ÷ life limit) × CLP, then discounted to the USM price. Using the only current LLP figure captured, $4.94M per engine at full life for the -5B if the Calver figure is per pair (Unknown U3), an engine torn down with 30% average LLP life would carry 0.30 × $4.94M = $1.48M of life-proportional LLP value; at 70–75% of CLP (Aircraft Commerce) that is $1.04–1.11M, which is most of the lower bound of the Safe Fly USM yield. The remainder of the yield is airfoils, cases and accessories. A -7B figure of the same vintage was not captured; the 2013 figure of $1.7M (Aircraft Commerce, Issue 87) is too old to use (Tension T4).

Step 4 — airframe. The only sourced item is the landing gear: over $1M for a fully overhauled set, or sold below half life to a buyer who wants to avoid an overhaul costing up to $400,000 (ISTAT Jetrader, Autumn 2020; a 2020 figure). The APU, avionics and remaining rotables are unsourced (Unknown U10).

Step 5 — timing. Three months to dismantle (APOC–Willis); then repair-shop turnaround for repairable items; whole modules and LLPs with life can be placed with an engine shop or a module-exchange provider at once, while the airframe rotable tail sells over an unsourced period (Unknown U2).

What the example shows even with the gaps: on a run-out airframe the two engines alone return $3.2–4.4M of USM on $1.6–2.4M of engine cost (Safe Fly), the single largest airframe item is about a quarter of one engine's yield (ISTAT Jetrader), and the engine proceeds arrive fastest because the buyers (engine shops, module-exchange pools) are ready-made.

---

## 3. Market structure and players

| Player | Listing | What it does in USM | Scale disclosed (source, date) |
|---|---|---|---|
| **AerSale Corp.** | NASDAQ: ASLE | Buys mid-life and end-of-life aircraft and engines ("flight equipment"); monetises them by leasing, whole-asset sale, or teardown into USM; also an MRO (TechOps). Two segments: Asset Management Solutions (AMS) and TechOps. | FY2025 revenue $335.3M (−2.8% vs $345.1M); Adjusted EBITDA $46.1M (13.8%) vs $33.4M (9.7%); AMS $211.6M vs $215.5M; TechOps $123.7M vs $129.6M; USM revenue $137.6M ($120.1M AMS + $17.6M TechOps); flight-equipment sales $56.4M from 13 engines vs $110.1M from 20 engines and one aircraft in 2024; revenue ex flight-equipment sales +18.7% (AerSale press release, 5 Mar 2026; FY2025 10-K). Q2 2026 results released 6 Aug 2026 (located, content not retrieved). |
| **AAR Corp.** | NYSE: AIR | Parts Supply segment = distribution of new OEM parts plus "sales and leasing of USM"; also whole-asset trading. | Parts Supply about 45% of FY2026 sales (year to 31 May 2026); segment sales +$388.1M y/y; new-parts Distribution +23.9%, USM activities +32.1%; whole-asset sales in parts trading +$27.8M in Q1 FY2026 (AAR FY2026 10-K). Total revenue not captured (Unknown U11). |
| **Willis Lease Finance** | NASDAQ: WLFC | Engine lessor (CFMI, GE, P&W, Rolls-Royce, IAE engines); subsidiary **Willis Aero** sells engine parts and materials "through the acquisition or consignment of aircraft and engines"; engines removed from the lease portfolio for part-out are carried in "equipment held for sale" and the investment is "recovered through the sale of spare parts". Also partnered with APOC on a 737-800 teardown. | Portfolio value and Willis Aero revenue not captured (Unknown U12) (Willis Lease FY2025 10-K; Asian Aviation). |
| **FTAI Aviation** | NASDAQ: FTAI | Transfers engines unserviceable for leasing into inventory for teardown; salvaged modules and parts are rebuilt into modules sold through Aerospace Products; serviceable used modules and parts sold through an exclusive partnership; also sells airframes for teardown (A320-200 to APOC, teardown May 2026). | Segment figures in D5 (FTAI FY2025 10-K; ePlaneAI). Partner identity not captured (Unknown U7). |
| **GA Telesis** | Private | Flight Solutions Group buys engines for disassembly and sells USM; also leasing, MRO. | Jan 2025: bought eight PW4000 engines from a major US airline for disassembly; Nov 2025: disassembled eight more (one CFM56-5B, two V2500-A5, two PW4000, three CF6-80C2); Oct 2025: bought an additional $25M of "OEM-aligned" USM engine inventory (GA Telesis press releases; Aviation Business News). 2018 CFM56-5B/-7B material agreement with Aero Engine Solutions (AviTrader, 31 Jan 2018). Revenue not disclosed. |
| **VAS Aero Services** | Private | Teardown management and USM redistribution, including large aircraft. | Appointed by Airbus to oversee dismantling and USM redistribution of three retiring A380s (ePlaneAI). Revenue not disclosed. |
| **AJW Group** | Private | Component support and USM; publishes on USM airworthiness. | Scale not captured (Unknown U13). Source of the Aug 2025 USM airworthiness article (AJW/AviTrader). |
| **Setna iO** | Private | USM trader; teardown of airframes and engine components, including new-generation. | Acquired a 2019-vintage A320neo airframe and two sets of PW1100G QEC (quick engine change — the mounts, plumbing and accessories that dress a bare engine for installation) components for teardown (AviTrader item). Revenue not disclosed. |
| **Unical Aviation** | Private | USM trader. | Nothing returned this session (Unknown U14). |
| **GE Aerospace used-material arm** | Part of NYSE: GE | OEM-owned used-material business. | Nothing substantive returned beyond a TrueEngine presentation URL (Unknown U15). |
| **AerCap Materials** | Part of NYSE: AER | Lessor-owned teardown and USM arm, formed when AerCap acquired GECAS in late 2021 (which had a parts business active in teardowns). Dismantles at Greenwood-Leflore County Airport, Mississippi; distribution centre in Memphis, Tennessee. | 2023: dismantled more than 300 aircraft, 15,000+ unique parts. 1Q 2026: 250,000+ items stocked, 850+ customers, dismantling "with tailored workscopes, competitive pricing and accelerated turnaround time" (AerCap Materials factsheets 2023 and 1Q 2026; Aviation Week, "Teardown providers expand business"). |
| **APOC Aviation** | Private | Engine and airframe trader/lessor; green-time leases; teardown ("up-cycling"). | Transactions listed in 2.2 (AviTrader; Aviation Business News; Asian Aviation; ePlaneAI). |
| **Tarmac Aerosave** | Private (Airbus/Safran/Suez JV) | Dismantling facilities (Toulouse-Francazal among them). | Site of the FTAI-sourced A320 teardown (ePlaneAI). |
| **Lessors' own part-out programmes** | — | Lessors (AerCap via AerCap Materials; Willis via Willis Aero) route end-of-lease assets into captive material arms rather than selling to third-party teardown companies. | As above. |

Market-structure notes from the sources: AerSale describes "more companies enter[ing] the teardown sector" and a hypercompetitive feedstock market (as relayed); AerCap's entry in 2021 and FTAI's exclusive-partnership structure are examples of lessors and engine specialists internalising the teardown step; GA Telesis's "OEM-aligned" inventory purchase shows OEM-sanctioned USM channels alongside independent ones (GA Telesis, Oct 2025).

---

## 4. Numbers

### 4.1 Engine values and lease rates

| Item | Figure | Basis | Source | Date |
|---|---|---|---|---|
| CFM56-7B24 market value | $5.7M | half life, H2 2025 | IBA, Engine Values Release 2025B | Sept 2025 |
| CFM56-7B27 market value | $6.4M | half life, H2 2025 | IBA, Engine Values Release 2025B | Sept 2025 |
| CFM56-7B "green-time value" | $2.8–3.4M | stated as "(new condition)" — basis unclear | Safe Fly, CFM56 Engine Market Report 2026 | 2026 |
| CFM56-7B lease rate | $42,000–48,000 / month; ~34% above 2019; +15–20% "in recent months" | green-time | Safe Fly | 2026 |
| CFM56-5B lease rate | $38,000–44,000 / month | green-time | Safe Fly | 2026 |
| V2500-A5 lease rate | $70,000–80,000 / month | typical | IBA 2025B | Sept 2025 |
| CFM56-5B/-7B value trend | levelled off after ~18 months of increases | — | IBA H1 2026 update | H1 2026 |
| CFM56 values | up "as much as 50%" over two years | — | ePlaneAI | date not captured |
| CFM56-7B market | "distinct lack of availability"; MV and lease rates above long-term trend | — | IBA 2025B | Sept 2025 |
| Q2 survey | V2500 lease rates dip, CFM56-5B strengthen | — | Ishka | Q2, year not captured |
| CFM56-7B active fleet | ~14,200 engines | 2026 | Safe Fly | 2026 |
| CFM56-7B shop visits | 2,300–2,400 / year through 2028 | — | Safe Fly | 2026 |

### 4.2 Teardown and part-out

| Item | Figure | Source | Date |
|---|---|---|---|
| Exhausted CFM56 purchase price | $0.8–1.2M | Safe Fly | 2026 |
| USM yield per exhausted CFM56 | $1.6–2.2M | Safe Fly | 2026 |
| Net margin per engine | $0.4–0.8M | Safe Fly | 2026 |
| 737-800 teardown duration | ~3 months | Asian Aviation / AirlinerGS (APOC–Willis) | 2025 |
| Overhauled landing-gear set | "over $1 million" | ISTAT Jetrader p.45 | Autumn 2020 |
| Landing-gear overhaul cost | up to $400,000 | ISTAT Jetrader p.45 | Autumn 2020 |
| CFM56-5B LLPs, A320 | $9,878,733 full life; $4,939,366 half life (2023 $) | Calver, Cargo Facts | Apr 2023 |
| CFM56-7B full LLP set list price | $1.7M | Aircraft Commerce Issue 87 | 2013 |
| Green-time lease precedent | 12 months, CFM56-5A, APOC to Condor; teardown after | AviTrader | 28 Jul 2025 |
| Residual value assigned to "alternative materials" | 60–70% of industry assigns 25% or less | Safe Fly (teardown report) | 2026 |

### 4.3 USM pricing versus OEM

| Item | Figure | Source | Date |
|---|---|---|---|
| USM as % of new-part price, average | 60–80% | Aviation Week, MRO Memo | date not captured |
| High-demand USM early in life cycle | up to 85% of CLP | Aviation Week, MRO Memo | date not captured |
| Trader sale price of repaired USM | 70–75% of CLP | Aircraft Commerce Issue 120 | date not captured |
| USM when OEM supply-constrained | can exceed CLP | Aviation Week, MRO Memo | date not captured |
| CFM catalogue list price increase | August 2023, "notable shift" | Aviation Week (Magnetic) | 2024 |

### 4.4 Retirements and feedstock

| Item | Figure | Source | Date |
|---|---|---|---|
| Aircraft retirements | 502 (2019); 465 (2020); 333 (2021); 325 (2022) | Cirium Fleets Analyzer via IATA/Aerodynamic presentation | 2023 |
| Average annual part-outs 2010–2019 | just under 540; peak 694 in 2013 | same | 2023 |
| Retirement rate 2024–2026 vs 2010–2019 | ~24% lower | McKinsey | date not captured (2024–25) |
| Normal retirement rate from 2028 | ~2.7% of fleet / year | McKinsey | same |
| A320ceo-family / 737NG retirements, next five years | 1,190 / 795 = 35% of total | Cirium | date not captured |
| 737NG retired by 2040 | ~72% | Ascend by Cirium | date not captured |
| Types ~half of retirements through 2025 | A320ceo, 737NG, 777, A330 | Cirium / Informa | date not captured |
| CFM56 shop-visit interval rule of thumb | ~8 years; 24-year de facto retirement | Aviation Week | date not captured |
| 737NG deliveries 1998–2002 | ~230 / year | Aviation Week | same |
| AerSale whole-asset sales | 13 engines (2025) vs 20 engines + 1 aircraft (2024) | AerSale | 5 Mar 2026 |

### 4.5 Market size

| Source | 2025 | Later year | CAGR | Notes |
|---|---|---|---|---|
| Fortune Business Insights (as relayed) | $8.55B | $12.93B (2034); $8.95B (2026) | 4.7% (2026–34) | URL not isolated in result |
| The Business Research Company (via GII) | $5.87B | $6.22B (2026) | 6.1% | "Air Transport USM Global Market Report" |
| Market.us | $7.7B | $12.3B (2035) | 4.8% (2026–35) | |
| SNS Insider | — | — | — | engine segment "dominated" the market |
| VAS / ePlaneAI | — | — | — | refers to a "$29 billion MRO market" without definition |
| Research and Markets; GM Insights | — | — | — | located, figures not retrieved |

### 4.6 SEC filers

| Company | Metric | Figure | Source |
|---|---|---|---|
| AerSale | FY2025 revenue | $335.3M (−2.8%) | PR 5 Mar 2026 |
| AerSale | FY2025 Adjusted EBITDA | $46.1M, 13.8% (vs $33.4M, 9.7%) | PR 5 Mar 2026 |
| AerSale | AMS revenue | $211.6M (vs $215.5M) | PR 5 Mar 2026 |
| AerSale | TechOps revenue | $123.7M (vs $129.6M) | PR 5 Mar 2026 |
| AerSale | USM revenue | $137.6M ($120.1M AMS + $17.6M TechOps; components sum to $137.7M, rounding) | PR 5 Mar 2026 |
| AerSale | Flight-equipment sales | $56.4M, 13 engines (vs $110.1M, 20 engines + 1 aircraft) | PR 5 Mar 2026 |
| AerSale | Revenue ex flight equipment | +18.7% | PR 5 Mar 2026 |
| AAR | Parts Supply share of sales | ~45% (FY2026) | 10-K FY2026 |
| AAR | Parts Supply sales growth | +$388.1M y/y | 10-K FY2026 |
| AAR | Distribution / USM growth | +23.9% / +32.1% | 10-K FY2026 |
| AAR | Whole-asset sales, Q1 FY2026 | +$27.8M y/y | 10-K FY2026 / 10-Q Aug 2025 |
| GA Telesis | USM engine inventory purchase | $25M (Oct 2025) | press release |
| AerCap Materials | Aircraft dismantled / parts | 300+ / 15,000 unique (2023); 250,000+ items, 850+ customers (1Q 2026) | factsheets |

---

## 5. Constraints and bottlenecks

- **Feedstock.** USM supply is a lagged function of retirements, and retirements in 2024–2026 are about 24% below the 2010–2019 norm (McKinsey). While half-life CFM56 values ($5.7–6.4M, IBA) are several times teardown yields ($1.6–2.2M, Safe Fly), owners of engines with life keep them flying or leasing rather than tearing them down, so only run-out engines reach the teardown market. AerSale's whole-asset sales fell by a third in units from 2024 to 2025 (AerSale).
- **Documentation.** A part without full traceability is worthless regardless of condition; LLPs need back-to-birth records (AJW/AviTrader). This caps the usable yield of a teardown at the documented fraction, and it is why buyers vet suppliers (the forms "can be easily generated").
- **Repair-shop capacity and cost.** Most USM is not serviceable as removed; it must go through a repair shop and be re-certified. Rising repair costs are cited alongside falling supply as a driver of CFM56 and V2500 part prices (Aviation Week, 2024). D2 covers shop capacity.
- **Regulatory jurisdiction.** A part released only on an 8130-3 or only on a Form 1 is restricted to the matching registry unless dual-released; cross-border trade depends on dual-release repair stations.
- **OEM pricing.** USM is priced off CLP, so OEM list increases (CFM's August 2023 increase) lift USM prices; conversely, OEM supply constraints push USM above CLP (Aviation Week).
- **Capital.** Teardown is a working-capital business: the asset is bought (or consigned), dismantled over about three months, and sold over an unsourced period. Lessor-owned arms (AerCap Materials, Willis Aero) and FTAI's captive pool avoid competing for third-party feedstock.
- **Thrust-rating and variant mismatch.** A -7B24 and a -7B27 differ in value ($5.7M vs $6.4M, IBA); module and LLP interchangeability across ratings and across -5B/-7B is governed by the OEM manual (D1), which limits which torn-down modules fit which exchange pools.
- **PMA interaction.** PMA parts erode the full-life adjustment appraisers apply (Aircraft Value News) and compete with USM for the same slot in a shop visit (D4).

---

## 6. Tensions

- **T1 — USM market size, 2025.** $5.87B (The Business Research Company) vs $7.7B (Market.us) vs $8.55B (Fortune Business Insights). The three vendors differ by 46% from lowest to highest; scope definitions were not retrieved. Growth rates also differ: 6.1% (TBRC) vs 4.7–4.8% (the other two).
- **T2 — Retirement outlook.** Oliver Wyman's July 2020 "A tsunami of used aircraft parts" (title only captured) framed a coming glut; McKinsey (2024–25) reports 2024–2026 retirements about 24% below the 2010–2019 norm and recovery only from 2028; Cirium's actual counts fell every year from 2019 (502) to 2022 (325). The forecast and the outturn point in opposite directions.
- **T3 — Engine value bases.** Safe Fly (2026) quotes a CFM56-7B "green-time value (new condition)" of $2.8–3.4M; IBA (Sept 2025) quotes half-life market values of $5.7M (-7B24) and $6.4M (-7B27). These are different bases (green-time near run-out vs half-life) and Safe Fly's "(new condition)" label is internally inconsistent with "green-time"; Safe Fly is a trade/secondary source. The lease rates Safe Fly gives for 2026 ($42–48K) are consistent with IBA's description of rates above trend, but IBA's own CFM56-7B lease-rate figure was not captured.
- **T4 — LLP set cost.** Aircraft Commerce (2013) gives a CFM56-7B full LLP set list price of $1.7M; Calver (2023) gives CFM56-5B engine LLPs at $9.88M full life for an A320 (per engine or per pair unstated). If the 2023 figure is per pair ($4.94M per engine), the 2013-to-2023 gap is far larger than catalogue escalation alone would explain; the 2013 excerpt may cover a subset of LLPs. Neither figure should be used without the original document.
- **T5 — USM discount to CLP.** Aviation Week's "60–80% of the price of a new part" is a general average; Aircraft Commerce's "70–75% of CLP" is a trader-to-airline price for repaired engine USM; Aviation Week also reports up to 85% and above-CLP cases. These are consistent as a range but not as a single number; which applies depends on part, platform and OEM supply at the time.
- **T6 — Who is squeezed by scarce feedstock.** AerSale describes a hypercompetitive feedstock market with pricing pressure on buyers (as relayed), while IBA calls it a "lessors' market" with escalating values (Apr 2024) and Aviation Week a "seller's market for used parts". These agree that asset owners have the upper hand and teardown buyers do not; they differ only in vantage point.
- **T7 — Direction of USM prices in 2024–2026.** Aviation Week headlines captured include both "Used parts market shows signs of stabilizing" and "North America sees upturn in USM market" (dates and bodies not captured); IBA says values "levelled off" in H1 2026 while Safe Fly says -7B lease rates rose 15–20% "in recent months". Without the article dates the sequence cannot be fixed.

---

## 7. Unknowns

- **U1** — Sourced split of a 737-800 part-out value between engines and airframe. Would be resolved by an appraiser part-out report or an AerSale/AAR investor presentation with a teardown waterfall.
- **U2** — Total sell-through period for teardown inventory (months to recover, say, 80% of proceeds). AerSale's 10-K inventory-turnover disclosure or a trade-press teardown case study would answer it.
- **U3** — Whether Calver's $9,878,733 / $4,939,366 CFM56-5B LLP figure is per engine or per aircraft (two engines). The original Cargo Facts presentation would settle it.
- **U4** — Any mba Aviation (or Ascend by Cirium) CFM56-5B/-7B value or lease-rate figure. None returned.
- **U5** — A current appraiser half-life value for the CFM56-5B (only trend commentary and a trade-press lease-rate range were captured).
- **U6** — Current CLP of representative CFM56-7B LLPs (e.g. HPT disk, fan disk) and of a full -7B LLP set. Needed for a precise module-value example.
- **U7** — The identity and terms of FTAI's "exclusive partnership" for teardown, repair, marketing and sale of CFM56 parts. The 10-K excerpt does not name it. The FTAI 10-K text or an FTAI press release would answer it.
- **U8** — Purchase price of a 737-800 bought for part-out in 2025–2026 (and of the airframe alone).
- **U9** — Teardown labour and facility cost per aircraft and per engine.
- **U10** — Values of a 737-800 APU, avionics suite, thrust reversers and other rotables.
- **U11** — AAR FY2026 total revenue and Parts Supply segment revenue in dollars (only the share and growth were captured).
- **U12** — Willis Lease portfolio value, number of engines, and Willis Aero spare-parts revenue for 2025.
- **U13** — AJW Group scale.
- **U14** — Unical Aviation: nothing returned.
- **U15** — GE Aerospace's used-material arm: name, scale and CFM56 role not captured (the only hit was a TrueEngine presentation URL whose content was not read).
- **U16** — Actual retirement counts for 2023, 2024 and 2025 from Cirium (only 2019–2022 counts and the 2024–26 shortfall percentage were captured).
- **U17** — Number of CFM56-5B and -7B engines torn down per year, 2023–2025.
- **U18** — Scope definitions behind the three USM market-size estimates (what counts as USM; whether engines, airframes and components are all included).
- **U19** — Oliver Wyman's 2020 forecast figures and any updated Oliver Wyman USM forecast (title only captured).
- **U20** — Pricing of a module exchange (exchange fee, LLP-life true-up) from any provider, including FTAI. D5 may hold FTAI's own disclosures.

---

## 8. Terms introduced

- **USM (used serviceable material)** — a previously installed part, inspected/repaired to the manual and released on an airworthiness tag for reinstallation.
- **OEM** — original equipment manufacturer; **CLP** — the OEM's catalogue list price for a new part.
- **PMA** — FAA Parts Manufacturer Approval; a third-party-made replacement part (D4).
- **DER repair** — a repair approved by an FAA Designated Engineering Representative rather than by the OEM manual (D4).
- **Shop visit** — an engine's removal to a repair shop for restoration or overhaul (D1/D2).
- **Teardown / part-out** — dismantling an aircraft or engine to sell its parts.
- **Feedstock** — aircraft and engines acquired for teardown.
- **Consignment** — teardown and sale on the owner's behalf for a fee, title retained by the owner.
- **CMM / ESM** — Component Maintenance Manual / Engine Shop Manual, the OEM documents that set inspection and repair limits.
- **BER** — beyond economic repair.
- **LLP (life-limited part)** — a rotating part with a hard OEM cycle limit, retired at the limit regardless of condition.
- **Life-expired** — an LLP at its cycle limit; no USM value; must be mutilated.
- **Hard-time (HT) part** — a part with a fixed overhaul or replacement interval.
- **FAA Form 8130-3** — US Authorized Release Certificate / Airworthiness Approval Tag.
- **EASA Form 1** — the European equivalent release certificate.
- **Dual release** — a single tag valid under both FAA and EASA systems.
- **Part 145 repair station** — an FAA- (or EASA-) certificated maintenance organisation permitted to issue release tags.
- **Back-to-birth traceability** — an unbroken record of an LLP's cycles since new.
- **AD / SB** — Airworthiness Directive (mandatory, regulator) / Service Bulletin (OEM modification).
- **Non-incident statement** — seller's declaration that a part was not involved in an accident, fire or immersion.
- **Quarantine** — segregation of a part whose documentation is suspect pending investigation.
- **Rotable** — a part that is repaired and reused rather than consumed.
- **APU** — auxiliary power unit; **HMU** — hydro-mechanical unit (engine fuel-metering unit); **QEC** — quick engine change kit (the dressing that readies a bare engine for installation).
- **HPT / HPC** — high-pressure turbine / high-pressure compressor.
- **Green time** — remaining usable time before the next mandatory shop visit; **green-time lease** — a short lease that consumes it; **run-out / exhausted** — no green time left.
- **EGT margin** — the gap between operating exhaust gas temperature and the limit (D1).
- **Full life / half life** — maintenance status with 100% / 50% of all intervals and LLP lives remaining.
- **Base value / market value** — appraiser's value in a balanced market / in the actual current market, both normally at half life.
- **Maintenance-adjusted value** — half-life value adjusted for actual shop-visit and LLP status.
- **Lease rate factor** — monthly rent divided by asset value.
- **Thrust rating (-7B24, -7B27)** — the engine's certified thrust in thousands of pounds; affects value.
- **Module** — a pre-assembled engine section that can be removed and replaced as a unit (D1).
- **Module exchange** — swapping a time-expired module for a serviceable one for a fee plus an LLP-life true-up.
- **MRE** — FTAI's Maintenance, Repair and Exchange offering (D5).
- **Up-cycling** — APOC's term for buying engines to tear down for material.

---

## 9. Sources

1. Sofema Aviation Services, "Consider the Challenges Related to the Aviation USM Market" (PDF), Aug 2024. https://sassofia.com/wp-content/uploads/2024/08/Consider-the-Challenges-Related-to-the-Aviation-USM-Used-Serviceable-Material-Market.pdf
2. AJW Group / AviTrader MRO, "Ensuring the airworthiness of USM: regulations, certification, traceability and authenticity", Aug 2025 (PDF). https://www.ajw-group.com/storage/downloads/1761651710_08.25_article_avitrader_mro_-_ensuring_airworthiness_of_usm.pdf
3. AviTrader, same article, 16 Oct 2025. https://avitrader.com/2025/10/16/ensuring-the-airworthiness-of-used-serviceable-materials-regulations-certification-traceability-and-authenticity-the-bedrock-of-the-usm-environment
4. FL Technics, "FL Technics' multilayered approach to used serviceable material" (undated). https://fltechnics.com/fl-technics-multilayered-approach-to-used-serviceable-material/
5. Rotabull, "FAA 8130-3 Form Airworthiness Approval Tag [Instructions]" (undated). https://rotabull.com/blog/8130-3-form
6. Delta TechOps, supplier matrix F-840-018-A, Mar 2024. https://dfp.delta.com/wp-content/uploads/2024/03/F-840-018-A-Supplier-matrix-1.pdf
7. AviTrader, "APOC secures engine lease agreement with Condor", 28 Jul 2025. https://avitrader.com/2025/07/28/apoc-secures-engine-lease-agreement-with-condor
8. Aviation Business News, "Condor secures APOC Aviation CFM56-5A lease to support A320 fleet", 2025. https://www.aviationbusinessnews.com/industry-news/condor-secures-apoc-aviation-cfm56-5a-lease-to-support-a320-fleet
9. Safe Fly Aviation, "CFM56 Engine Market Report 2026" (trade/secondary), 2026. https://safefly.aero/cfm56-engine-market-report-2026/
10. Safe Fly Aviation, "Aircraft Teardown Market Growth: USM Demand, Recycling & Forecast" (trade/secondary), 2026. https://safefly.aero/?p=15482
11. IBA, "Engine Values Release September 2025 (2025B)", Sept 2025. https://www.iba.aero/resources/articles/engine-values-2025b-release-september-2025/
12. IBA, "IBA Engine and Lease Rate Update – H1 2026", 2026. https://www.iba.aero/resources/articles/iba-engine-and-lease-rate-update-h1-2026/
13. IBA, "It's a 'Lessors' Market' says IBA, as engine lease rates and market values escalate", Apr 2024. https://www.iba.aero/about/news/itandrsquos-a-andldquolessorsandrsquo-marketandrdquo-says-iba-as-engine-lease-rates-and-market-values-escalate/
14. AviTrader, "IBA says it's a 'lessors' market'", 25 Apr 2024. https://avitrader.com/2024/04/25/iba-says-its-a-lessors-market/
15. IBA, "Engine values & lease rates: September 2024". https://www.iba.aero/resources/articles/engine-values-lease-rates-september-2024/
16. IBA, "IBA Engine Value and Lease Rate Update" (undated index). https://www.iba.aero/resources/articles/iba-engine-value-and-lease-rate-update/
17. Aerospace Innovations, "Engine shortages and MRO backlog keep values and lease rates elevated, says IBA" (date not captured). https://aerospace-innovations.com/engine-shortages-and-mro-backlog-keep-values-and-lease-rates-elevated-says-iba/
18. Ishka, "Q2 engine prices and lease rates: V2500 lease rates dip, but 5Bs strengthen" (year not captured). https://www.ishkaglobal.com/News/Article/7923/Q2-engine-prices-and-lease-rates-V2500-lease-rates-dip-but-5Bs-strengthen
19. ePlaneAI, "CFM56 engine values highlight investor opportunities and risks" (date not captured). https://www.eplaneai.com/news/cfm56-engine-values-highlight-investor-opportunities-and-risks
20. Mark Calver, Cargo Facts Session 3 presentation (PDF), Apr 2023. https://cargofactsevents.com/wp-content/uploads/2023/04/Mark-Calver-Session-3-Presentation.pdf
21. Aircraft Value News, "Concept of half to full life fluid as aircraft move past mid-life" (date not captured). https://www.aircraftvaluenews.com/concept-of-half-to-full-life-fluid-as-aircraft-move-pass-mid-life/
22. Aircraft Value News, "PMA continues to undermine full-life maintenance adjustments" (date not captured). https://www.aircraftvaluenews.com/pma-continues-to-undermine-full-life-maintenance-adjustments/
23. Aircraft Value News, "Part-out pricing collapses" (title only; date not captured). https://www.aircraftvaluenews.com/part-out-pricing-collapses/
24. Aircraft Commerce, Issue 87 maintenance article (PDF), 2013. https://www.aircraft-commerce.com/wp-content/uploads/aircraft-commerce-docs/Maintenance/2013/ISSUE87_MTCE_B.pdf
25. Aircraft Commerce, Issue 120 maintenance sample article (PDF), date not captured. https://www.aircraft-commerce.com/sample_article_folder/120_MTCE_B.pdf
26. Aircraft Commerce via AJW, "Narrowbody engine market activity", Feb 2023 (PDF; located, content not used). https://www.ajw-group.com/storage/downloads/1677591641_aircraft_commerce_narrowbody_engine_market_activity_feb_23.pdf
27. McKinsey & Company, "What does the future hold for commercial-aviation maintenance?" (date not captured; 2024–25). https://www.mckinsey.com/industries/aerospace-and-defense/our-insights/what-does-the-future-hold-for-commercial-aviation-maintenance
28. Cirium page (retirement projections; date not captured). https://www.cirium.com/?p=43293
29. Informa Markets / Aviation Week commercial fleet forecast page (date not captured). https://informamarkets.turtl.co/story/com-forecast/page/5
30. IATA Maintenance Cost Conference, "Retirements, part-outs, dismantling", Aerodynamic Advisory (Murby), PDF, 2023. https://www.iata.org/contentassets/3f8981eb437e4e16808639bc9d19d5c7/mcc202_day02_0915-0945_retirements-partouts-dismantling_aerodynamic_murby.pdf
31. Aviation Week, "Retirement Uptick Will Restock Used Engine Parts" (date not captured). https://aviationweek.com/air-transport/retirement-uptick-will-restock-used-engine-parts
32. Aviation Week, "Teardown Providers Expand Business Amid Continued Demand" (date not captured). https://aviationweek.com/mro/marketplace/teardown-providers-expand-business-amid-continued-demand
33. Aviation Week, "MRO Memo: A Seller's Market For Used Parts" (date not captured). https://aviationweek.com/mro/workforce-training/mro-memo-sellers-market-used-parts
34. Aviation Week, "Magnetic expects CFM56 market challenges, opportunities in 2024", 2024. https://m.aviationweek.com/mro/aircraft-propulsion/magnetic-expects-cfm56-market-challenges-opportunities-2024
35. Aviation Week, "Used Parts Market Shows Signs Of Stabilizing" (title only). https://aviationweek.com/shows-events/mro-americas/used-parts-market-shows-signs-stabilizing
36. Aviation Week, "North America Sees Upturn in USM Market" (title only). https://aviationweek.com/mro/supply-chain/north-america-sees-upturn-usm-market
37. Oliver Wyman, "A tsunami of used aircraft parts", Jul 2020 (title only). https://www.oliverwyman.com/our-expertise/insights/2020/jul/a-tsunami-of-used-aircraft-parts.html
38. ePlaneAI, "APOC Aviation to support USM stock through A320-200 teardown", 2026. https://www.eplaneai.com/zh/news/apoc-aviation-to-support-usm-stock-through-a320-200-teardown
39. The Business Research Company via GII, "Air Transport USM Global Market Report", 2026. https://www.gii.tw/report/tbrc1773717-air-transport-usm-global-market-report.html
40. Market.us, "Air Transport USM Market", 2025–26. https://market.us/report/air-transport-usm-market/
41. SNS Insider, "Used Serviceable Material Market – segmentation". https://www.snsinsider.com/reports/used-serviceable-material-market-8691/segmentation
42. Research and Markets, "Air Transport USM – Global Strategic Business Report" (located; figures not retrieved). https://www.researchandmarkets.com/reports/5140944/air-transport-usm-global-strategic-business
43. GM Insights, "Air Transport USM Market – market analysis" (located; figures not retrieved). https://www.gminsights.com/industry-analysis/air-transport-usm-market/market-analysis
44. Fortune Business Insights, USM market report — figures as relayed in search results; URL not isolated.
45. AerSale Corp., Form 10-K FY2025, filed 2026. https://www.sec.gov/Archives/edgar/data/1754170/000110465926025574/asle-20251231x10k.htm
46. AerSale Corp., press release (FY2025 results), 5 Mar 2026 (Ex. 99.1). https://www.sec.gov/Archives/edgar/data/1754170/000110465926024101/asle-20260305xex99d1.htm
47. AerSale Corp., press release (Q2 2026 results), 6 Aug 2026 (located; content not retrieved). https://www.sec.gov/Archives/edgar/data/1754170/000110465926091978/asle-20260806xex99d1.htm
48. AerSale Corp., Form 10-Q, quarter ended 30 Jun 2026. https://www.sec.gov/Archives/edgar/data/1754170/000110465926092710/asle-20260630x10q.htm
49. AAR Corp., Form 10-K FY2026 (year ended 31 May 2026). https://www.sec.gov/Archives/edgar/data/0000001750/000110465926085459/air-20260531x10k.htm
50. AAR Corp., Form 10-Q, quarter ended 31 Aug 2025. https://www.sec.gov/Archives/edgar/data/1750/000110465925092589/air-20250831x10q.htm
51. Willis Lease Finance Corp., Form 10-K FY2025. https://www.sec.gov/Archives/edgar/data/1018164/000101816426000036/wlfc-20251231x10k.htm
52. FTAI Aviation Ltd., Form 10-K FY2025. https://www.sec.gov/Archives/edgar/data/1590364/000162828026012940/ftai-20251231.htm
53. GA Telesis, "Flight Solutions Group continues USM market growth: purchase of eight PW4000 engines for disassembly", Jan 2025. https://www.gatelesis.com/ga-telesis-flight-solutions-group-continues-usm-market-growth-the-purchase-of-eight-8-pw4000-engines-for-disassembly/
54. GA Telesis, "GA Telesis strengthens leadership in engine disassembly and USM inventory growth", Nov 2025. https://gatelesis.com/ga-telesis-strengthens-leadership-engine-disassembly-usm-inventory-growth
55. Aviation Business News, "GA Telesis announces V2500, CFM56-7B, CF6-80C2 and PW4000 engine disassemblies". https://www.aviationbusinessnews.com/mro/ga-telesis-announces-v2500-cfm56-7b-cf6-80c2-and-pw4000-engine-disassemblies/
56. AviTrader, "GA Telesis and Aero Engine Solutions enter into CFM56-5B and CFM56-7B material agreement", 31 Jan 2018. https://avitrader.com/2018/01/31/ga-telesis-and-aero-engine-solutions-enter-into-cfm56-5b-and-cfm56-7b-material-agreement/
57. ePlaneAI, "VAS to oversee teardown of three Airbus A380 aircraft". https://www.eplaneai.com/es/news/vas-to-oversee-teardown-of-three-airbus-a380-aircraft
58. AviTrader item on Setna iO A320neo airframe and PW1100G QEC teardown (URL not isolated; appeared as https://avitrader.com/?p=163680 in results).
59. AerCap Materials, Factsheet 2023 (PDF). https://www.aercap.com/_assets/_95ac4c65fdc732db11562e8bc8c249f8/aercap/db/607/8027/fact_sheet/Materials_Factsheet+2023.pdf
60. AerCap Materials, Factsheet 1Q 2026 (PDF). https://www.aercap.com/_assets/_3b87087632d76febf90601f9b1fe7356/aercap/db/607/8027/fact_sheet/AerCap_Materials_Factsheet+1Q+2026.pdf
61. Asian Aviation, "APOC partners with Willis Lease for 737-800 teardown", 2025. https://asianaviation.com/apoc-partners-with-willis-lease-for-737-800-teardown/
62. AirlinerGS, "APOC partners with Willis Lease Finance Corporation for 737-800 teardown". https://airlinergs.com/apoc-partners-with-willis-lease-finance-corporation-for-737-800-teardown/
63. Aviation Business News, "APOC acquires four 737 airframes for teardown". https://www.aviationbusinessnews.com/mro/apoc-acquires-four-737-airframes-for-teardown
64. Aviation Business News, "Building capability for the future: APOC Aviation disassembles two CFM56-7B engines". https://www.aviationbusinessnews.com/mro/building-capability-for-the-future-apoc-aviation-disassembles-two-cfm56-7b-engines/
65. AviTrader, "APOC acquires first CFM56-5B for up-cycling as engine portfolio expands", 7 Oct 2021. https://avitrader.com/2021/10/07/apoc-acquires-first-cfm56-5b-for-up-cycling-as-engine-portfolio-expands/
66. ISTAT Jetrader, Autumn 2020, p.45. https://nxtbook.com/nxtbooks/ISTAT/jetrader_autumn2020/index.php?startid=45
67. GE Aerospace, TrueEngine presentation (PDF; located, content not retrieved). https://www.geaerospace.com/sites/default/files/trueengine-presentation.pdf
