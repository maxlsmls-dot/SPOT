# D4 — Parts Manufacturer Approval (PMA) parts and Designated Engineering Representative (DER) repairs

Dossier for the FTAI Aviation deep primer. Raw material for the writer; explains, does not opine.
Searches run 2026-10-03 (17 WebSearch calls; WebFetch unavailable, so filing and regulator text is
as returned by search, cited to the URL returned). Secondary sources are labelled as such. Investor
blogs and expert-interview transcripts are labelled "third-party commentary" and are never treated
as FTAI disclosure.

---

## 1. Summary

1. A **PMA (Parts Manufacturer Approval)** is the FAA's combined design-and-production approval under 14 CFR Part 21 Subpart K that lets a company other than the engine or airframe maker legally make and sell replacement parts for a type-certificated product. A **DER repair** is a repair whose engineering data was approved by an FAA-designated engineer (Form 8110-3) rather than taken from the OEM's shop manual. Both substitute for OEM new parts and OEM repairs in a shop visit's parts bill.
2. Reference PMA business: HEICO (NYSE: HEI) Flight Support Group, fiscal year to 31 Oct 2025: net sales $3,117.3M (+18% y/y), operating income $750.4M (+27%), implied operating margin 24.1%; HEICO adds roughly 300–500 new PMAs per year (HEICO 10-K FY2025, Q4 FY2025 release).
3. Hot-section PMA for the CFM56-5B/7B fleet (20,000+ engines) is new: Chromalloy announced FAA PMA for the CFM56-5B/7B high-pressure-turbine (HPT) blade on 30 Oct 2025, describing it as the only non-OEM alternative to the new OEM blade; a CFM56-5B/7B HPT stage-1 vane (the HPT nozzle) PMA followed in Nov 2025; an LPT vane PMA exists (date not retrieved).
4. Chromalloy: $1B+ revenue, ~4,000 employees, owned by Veritas Capital through parent Sequa since Dec 2022 (bought from Carlyle); repairs, coatings, castings and PMA.
5. FTAI's FY2025 10-K says it "develops and manufactures PMA parts through a joint venture"; FTAI's filings retrieved here do not name Chromalloy, disclose JV ownership, or quantify savings. Third-party commentary describes an exclusive, perpetual 2018 partnership covering five CFM56 hot-section parts supplied to FTAI "at cost", with claimed savings "up to $2 million per shop visit" — unverified against FTAI disclosure.
6. Market-size estimates conflict: commercial-aircraft PMA $11.8B in 2025 (IMARC) versus $14B by 2026 (Global Industry Analysts); engine PMA-plus-DER $2.95B in 2022 rising to $6.17B by 2032 (GII/market-research vendor); an older FlightGlobal piece put PMA's ceiling at ~21% of the engine-parts market.
7. Airline datapoint: Southwest used 341 PMA part numbers in 2022 and saved $54M (Aviation Week), i.e. ~$158k per part number per year.
8. OEM position: under CFM's 2018 agreement with IATA, installing non-CFM parts or repairs does not void CFM's warranty and CFM does not refuse service to engines containing them; CFM's commercial response has been a redesigned HPT blade (Oct 2023, "up to 25% longer life"), output up ~2.5x y/y with the 1,700th set shipped, ~400 industrialized repairs since 2023, and a multi-year materials agreement with FTAI itself (22 Jan 2026).
9. Lessor position: the retrieved sources (2009–2016) say operating lessors usually write OEM-only return conditions, that engine lessors "in the vast majority of cases" forbid PMA and DER, and that aircraft-lease clauses have been loosening. No 2024–2026 lessor survey was retrieved; current practice is an Unknown.
10. Worked example (section 2.8): a CFM56-7B HPT blade set at an interview-sourced $20,000 per new OEM blade is $1.6M per set at the commonly cited 80 blades; PMA savings scale linearly with the PMA discount, which no retrieved source discloses.

---

## 2. Mechanics

### 2.1 Why a PMA is needed at all

Every commercial jet engine is built under a **type certificate (TC)**, the FAA's approval of the design, held by the **type certificate holder (TCH)** — for the CFM56, CFM International (the 50/50 GE Aerospace–Safran Aircraft Engines joint venture). The FAA's production rules (14 CFR Part 21) say that a replacement or modification part for a type-certificated product may be installed only if it was produced under an FAA production approval (the TCH's own production certificate, a PMA, or a Technical Standard Order authorization), or falls into a narrow exception (standard parts such as AN/MS hardware, parts an owner or operator produces for its own aircraft, parts made in-house by a repair station as part of a repair). The OEM's own new spare parts are produced under its production certificate. For anyone else to sell a new part for the engine, the gate is a PMA (eCFR, 14 CFR Part 21 Subpart K [1]; FAA PMA design-approval page [5]).

**Used serviceable material (USM)** — parts removed from retired or torn-down engines, inspected and re-released — is the other non-OEM source of parts; it is covered in dossier D3. USM is OEM-made, so it is not subject to the PMA debate, but it competes for the same slot in the shop-visit parts bill.

### 2.2 What a PMA is and the four approval bases

A PMA is both a **design approval** (the FAA agrees the part's design meets the airworthiness standards that apply to the product it goes on) and a **production approval** (the FAA agrees the holder has a quality system able to make every unit to that design; 14 CFR 21.307 requires a quality system meeting 21.137, and 21.316 lists the holder's continuing obligations). The FAA issues the PMA as a letter with a supplement listing every approved part number and the engine or aircraft models it is eligible for; parts must be marked "FAA-PMA" with the maker's name and part number (14 CFR 45.15); each shipment is released on **FAA Form 8130-3**, the Authorized Release Certificate [1][4][5].

14 CFR 21.303 requires the applicant to provide "test reports and computations necessary to show that the design of the article meets airworthiness requirements, unless the applicant shows that the design is identical to an article covered under a type certificate," in which case, if the design was obtained by a licensing agreement, the applicant must provide evidence of that agreement [1]. FAA guidance (AC 21.303-3, AC 21.303-4, Order 8110.42D) turns this into four bases [2][3][4]:

1. **Test and computation (T&C).** The applicant has no OEM data. It reverse-engineers the part — measures OEM examples, determines material and coatings, writes its own drawings and process specifications — and then demonstrates by analysis and test that the part meets the applicable airworthiness standards (for an engine part, 14 CFR Part 33) and does not degrade the engine's compliance. This is the path for competing with the OEM on a part the OEM has not licensed. For engine and APU parts the FAA's product-specific guidance is AC 33-8 [6]. Chromalloy's CFM56 HPT blade is a T&C part (it is described as an alternative to the OEM new part, not a licensed copy) [26][27].
2. **Identicality without a licensing agreement.** The applicant shows that its design is identical to the TC-holder's design in every respect that matters, usually because it has the OEM drawings legitimately (for example, a former supplier). FAA Notice 8110.55 (1996) set the policy [7]. The FAA's guidance states that if a critical or life-limited article's basis is identicality, the applicant must show that its manufacturing processes, inspection and test procedures produce a part identical to the original [4].
3. **Identicality by licensing agreement.** The TC or STC holder licenses its design data; the licence is the evidence of identicality. This is how an OEM's subcontractor or a company the OEM has chosen to work with gets a PMA. Evidence of a licensing agreement is "a way to show identicality," the applicant using it to show that the data submitted are FAA-approved and identical to the original part [2][4].
4. **Supplemental Type Certificate (STC).** The part is the subject of a separate design approval (an STC — an FAA approval of a change to a type-certificated product), and the PMA is then the production approval for that STC's parts. This path matters for international acceptance (section 2.5).

In all four cases the FAA (through an Aircraft Certification Office for the design side and a Manufacturing Inspection District Office for the production side, or through delegated designees) checks conformity of test articles, the test and analysis reports, and the quality system before issuing the supplement [4][5].

### 2.3 "Critical" and "life-limited" parts and why hot-section PMA is the hard case

Two different definitions are in play.

- **Life-limited part (LLP)** (engine context): a rotating or major static part whose primary failure is likely to be hazardous to the engine, and which therefore has an approved life limit in flight cycles in the engine's Airworthiness Limitations Section; when the limit is reached the part must be scrapped, which forces the engine open (dossier D1). In the CFM56 these are the disks, spools, shafts, seals and similar rotating hardware. HPT blades and vanes, combustor liners and LPT blades are **not** LLPs; they are replaced on condition.
- **Critical component** (FAA–EASA bilateral definition): "a part identified as critical by the design approval holder during the product certification process or otherwise by the Authority for the State of Design. Typically, such components include parts for which a replacement time, inspection interval, or related procedure is specified in the Airworthiness Limitations section or certification maintenance requirements" [8][9]. All LLPs are critical components; whether a given blade or vane is a critical component depends on the TCH's designation, which is not public in the sources retrieved.

What changes for the applicant: for a critical or life-limited part approved via identicality, the FAA requires evidence that the manufacturing processes (casting, forging, heat treatment, coating) and inspection and test procedures, not just the geometry, are identical [4]. For T&C approval of a turbine part, AC 33-8 governs: the applicant must substantiate material properties, cooling and thermal behaviour, durability and the effect of the part on the engine's safety analysis by its own testing, because it has no access to the OEM's data [6]. That is why PMA historically concentrated in consumables and expendables (seals, bushings, fasteners, filters, brackets, non-rotating structural pieces) and why a T&C PMA for a cooled, single-crystal, coated HPT blade is treated in the trade as a milestone: Chromalloy's announcement calls the CFM56-5B/7B HPT blade "the only aftermarket alternative to the OEM manufactured new part" for a platform with over 20,000 engines in service [26][27][28].

No PMA for a CFM56 life-limited rotating part was found in this session (Unknown U7).

### 2.4 How long a PMA takes

Not disclosed by the FAA or by the companies in the material retrieved. Datapoints: third-party commentary dates the FTAI–Chromalloy partnership to 2018 and the FAA approval of the HPT blade came in Oct 2025 (about seven years; the application date is not public) [68][69][26]. HEICO adds 300–500 PMAs per year across a portfolio dominated by less complex parts, so simple PMAs are evidently a matter of months rather than years [15]. Record as Unknown U4.

### 2.5 EASA and other regulators' acceptance: the FAA–EASA bilateral

The United States and the European Union operate under a Bilateral Aviation Safety Agreement implemented by the **Technical Implementation Procedures (TIP)**, currently Revision 7 [8][9]. As returned by search, the TIP says EASA shall directly accept FAA PMA approvals, without further showing, for installation on EASA-certified or EASA-validated products when:

1. the PMA part is not a "critical component" and its design was approved via test and computation or identicality without a licensing agreement under 14 CFR 21.303 (the search summary rendered this clause as "identicality without a licensing agreement"; the writer should check the exact wording of TIP Rev 7 before quoting it); or
2. the PMA part conforms to design data obtained under a licensing agreement from the TC or STC holder and that TC or STC has been validated by EASA; or
3. the PMA part is a critical component and its design was approved via an FAA-issued STC that EASA has validated [8][9].

The practical consequence: a non-critical T&C PMA travels to the EU on its FAA 8130-3 (with the EASA-acceptance statement), while a critical T&C part needs the STC route plus EASA validation. **EASA Form 1** is the EU's equivalent release certificate, issued by an EASA production-organisation-approval holder [10]. Whether Chromalloy's CFM56 HPT blade or HPT vane is a "critical component" under this definition, and therefore which clause it falls under, was not found (Unknown U5). Acceptance by other regulators (UK CAA, Transport Canada, Brazil's ANAC, China's CAAC, etc.) is by separate bilaterals and national rules; none was retrieved (Unknown U6).

### 2.6 DER repairs

A **Designated Engineering Representative (DER)** is an individual engineer appointed by the FAA under 14 CFR Part 183 to examine engineering data and make findings of compliance on the FAA's behalf, within a delegated area (structures, powerplant, engines, systems, etc.). A **company DER** works for a manufacturer or repair station and may act only on that company's data; a **consultant DER** may act for any client. The governing document is FAA Order 8110.37 (the DER Handbook, currently revision F) [11].

A **repair** restores a part to an airworthy condition. The OEM publishes approved repairs in its **Engine Shop Manual (ESM)** and component manuals as part of the Instructions for Continued Airworthiness attached to the type certificate; a shop that follows the manual needs no further approval. When a shop wants to repair a part in a way the manual does not cover — or to repair a part the manual says must be scrapped — the repair is a **major repair** needing FAA-approved data, unless it qualifies as minor. A **DER repair** is such a repair whose data (the repair scheme, substantiation analysis, process specifications and any test) a DER has approved on **FAA Form 8110-3**, "Statement of Compliance with Airworthiness Standards" [11][12]. Mechanics as returned from the Order:

- A DER needs a specific authorization — "Special – Major Repairs" — from the managing Aircraft Certification Office to approve major-repair data; the authorization can be one-time or part of the DER's standing delegation [11].
- Major repairs "must be accomplished in accordance with technical data approved by the Administrator"; the DER may approve the design and substantiation data if authorized, but DER-approved data "may not be adequate to cover every aspect of the repair," so the repair station still performs it under its own repair-station certificate and releases the part on an 8130-3 that references the 8110-3 [11][12].
- The DER retains the original 8110-3 and sends copies to the FAA managing office and to the owner, operator or repair station that requested the approval [11].
- Approved repair data may be **one-time** (a specific serial-numbered part) or **multiple-use** (repeatable on any eligible part), which is what makes a DER repair a product a shop can sell.

How a DER repair differs from an OEM-manual repair: the data source (independent engineering versus the TCH), the approving authority (an FAA designee versus the FAA's approval of the TCH's manual), and acceptance by third parties (section 2.9). The repaired part is still the OEM's part; nothing is remanufactured. Who develops and uses them: independent engine-parts repair houses (Chromalloy's historic core business is turbine part repairs and coatings, and trade press describes it as positioned in the "PMA and designated engineering repair sector" [34][36]), airlines with in-house engineering (Southwest was reported as evaluating PMA and DER options for its CFM56-7B fleet [58]), and independent MROs. CFM's 2018 conduct policies, discussed in section 2.9, refer to "non-CFM parts and/or repairs," i.e. PMA and DER together [43][44][46]. EASA's equivalent is repair design approved by a Design Organisation Approval holder; how FAA DER repair data is accepted on EU-registered aircraft is governed by the TIP but was not verified in this session (Unknown U8).

### 2.7 Where PMA and DER change the shop-visit bill

A **performance-restoration shop visit** (dossier D1) opens the engine's core — HPT, combustor and high-pressure compressor — to restore exhaust-gas-temperature margin. Its bill is labour plus material, and material is parts replaced new plus parts repaired. The two mechanisms here attack material in different ways:

- **DER repair** saves money by repairing a part the OEM manual would scrap, or by repairing it more cheaply than the manual's repair, so no new part (OEM or PMA) is bought.
- **PMA** saves money when a part must be replaced new: the shop buys the PMA part at a discount to the OEM part.

An interview published by In Practise (third-party commentary) describes the cadence that determines which mechanism applies: at the first shop visit (around 20,000 cycles) airlines typically repair HPT blades rather than replace them; at the second (around 30,000 cycles) hot-section parts typically cannot be repaired again, so a new part is needed, and that is where a PMA blade is the cheaper alternative to a new OEM blade quoted at about $20,000 [66][67]. The same source says a new set of HPT blades and vanes "can cost up to a few million dollars" and that the HPT is "both the most expensive and the fastest wearing component" [66]. CFM's own repair work pushes the other way: it says it has industrialized about 400 CFM56 repairs since early 2023, including automated laser welding of HPT blades that cuts repair turnaround by about a third [40].

### 2.8 Worked example: CFM56-7B performance restoration, OEM-new versus PMA hot-section parts

Inputs and their provenance (all 2025–2026 unless noted):

| Input | Value | Source and status |
|---|---|---|
| New OEM CFM56 HPT blade, price per blade | ~$20,000 | In Practise expert interview, third-party commentary [66] |
| Alternative per-blade listing | ~€35,000 (≈$38–39k) | Page hosted on an ATU web host [72]; provenance weak; condition (new vs serviceable) unclear |
| HPT blades per CFM56-7B HPT rotor | 80 | Commonly cited; NOT confirmed by any source retrieved this session; treat as a parameter |
| New OEM HPT blade + vane set | "up to a few million dollars" | In Practise [66] |
| PMA discount to OEM price for the Chromalloy blade | not disclosed | No source; Chromalloy and FTAI did not publish a price |
| FTAI claimed saving from five hot-section PMA parts | "up to $2 million per shop visit" | Investor blogs (Komodo Capital, Kairos Research) [68][69]; not in FTAI filings retrieved |
| Total CFM56-7B performance-restoration shop-visit cost | not retrieved here | Dossier D1/D2 remit |

Step 1 — OEM blade set. 80 blades × $20,000 = **$1,600,000** at the interview price; 80 × $38,500 = **$3,080,000** at the listing price. The gap between the two is Tension T5.

Step 2 — PMA blade set at a discount d. Saving = $1.6M × d. Because d is undisclosed, show the function:

| Assumed PMA discount d | PMA set cost | Saving on blade set | Saving as % of blade set |
|---|---|---|---|
| 20% | $1,280,000 | $320,000 | 20% |
| 30% | $1,120,000 | $480,000 | 30% |
| 40% | $960,000 | $640,000 | 40% |

These discount rates are illustrative assumptions, not sourced figures (Unknown U2).

Step 3 — add the HPT vane (nozzle) set. If blades plus vanes are "up to a few million dollars" (taken here as $2.5–3.0M), the same discount range gives savings of $0.5–1.2M on the two HPT part families together.

Step 4 — compare with the claimed FTAI figure. The investor-blog claim is up to $2.0M per shop visit from five parts supplied "at cost." If "at cost" means FTAI pays roughly manufacturing cost rather than a market PMA price, then FTAI's saving per part is OEM price minus manufacturing cost, which is larger than the discount a third-party buyer of the same PMA part would get. On the $1.6M blade set alone, a $2.0M total saving across five parts would require the other four parts (HPT vane, LPT parts, and whatever else) to carry the remainder; at the $3.08M blade-set figure the $2.0M would be reachable from the blade set alone at a 65% effective discount. The arithmetic shows the claim is sensitive to which per-blade price is right (Tension T1, T5).

Step 5 — percentage of the shop visit. Not computed here because the shop-visit total is not sourced in this dossier; the writer should divide the dollar savings above by the D1/D2 performance-restoration cost. The savings apply mainly to shop visits where blades and vanes are scrapped rather than repaired (second and later visits per [66]), not to every visit.

Cross-check with an airline-level figure: Southwest's reported $54M saving across 341 PMA part numbers in 2022 is $158,358 per part number per year across a fleet of roughly 800 737s; it is a fleet-wide, mostly non-hot-section figure and cannot be converted to a per-shop-visit saving without the part mix [58].

### 2.9 Lease and OEM-contract mechanics that govern acceptance

**Return conditions.** An operating lease specifies the physical and documentary state the aircraft or engine must be in at redelivery. These conditions, not the rent, are what protect the lessor's next placement; one lease-management primer calls them "the most important part of any lease" [57]. An **OEM-only clause** (also "no PMA/no DER" clause) requires that at return the engine contain only TCH-produced parts and TCH-manual repairs; a lessee that used PMA during the term must then either remove the PMA parts at the last heavy check before return or pay a compensation. The sources describe both the clause and the workaround: "when permitted by the lease, lessees can ... use PMA throughout the term of the lease and ... remove PMA parts during the heavy check prior to the return" [55]; for engines, "returning a 'PMA-heavy' engine to strict TCH configuration carries significant financial burdens" [54].

**TRUEngine.** CFM's TRUEngine programme (GE Aerospace's TrueEngine presentation; expansion announced 2012 to cover subsequent buyers) designates an engine as maintained to CFM-approved configuration, i.e. CFM parts and CFM-approved repairs; CFM markets it as supporting residual value and resale, and lessors can require TRUEngine status in return conditions [48][49][50]. A TRUEngine requirement is an OEM-only clause by another name.

**Warranty and service.** Under the agreement CFM reached with IATA in 2018 (settling IATA's complaint to the European Commission about CFM's aftermarket conduct), CFM adopted published "Conduct Policies": installing non-CFM parts or repairs "does not in itself render the warranty void"; CFM honours warranty on its own parts and repairs in an engine containing non-CFM parts; and CFM "does not refuse to service engines because they contain non-OEM parts or repairs" [43][44][45][46][47]. The policies also cover CFM's licensing of its shop manual to third-party shops and sale of CFM parts to them; those clauses were not re-read in this session.

---

## 3. Market structure and players

**PMA makers**

- **HEICO Corp (NYSE: HEI), Flight Support Group (FSG).** The largest independent PMA business. FY2025 (to 31 Oct 2025) FSG net sales $3,117.3M, operating income $750.4M; the 10-K says FSG "uses proprietary technology to design and manufacture jet engine and aircraft component replacement parts for sale at lower prices than those manufactured by OEMs," that they are FAA-approved and "the functional equivalent" of OEM parts, and that HEICO has been adding "approximately 300 to 500" PMAs per year [15][16]. FSG also includes repair and distribution; the "aftermarket replacement parts" product line grew 15% organically in FY2025 (+$263.9M) [16]. HEICO acquired Wencor Group, the other large independent PMA/distribution business, in 2023 [19]. HEICO does not disclose its PMA discount to OEM prices in the filings retrieved, nor a split of its portfolio by part category (Unknown U9).
- **Chromalloy.** Palm Beach Gardens, Florida; "$1 billion-plus" revenue, about 4,000 employees; CEO Chris Celtruda appointed 2024 [34][36]. Owned by Sequa Corporation; Carlyle bought Sequa in 2007 and sold it to a Veritas Capital affiliate (announced Sept 2022, closed Dec 2022); Bloomberg reported Carlyle sought about $2B (July 2022) [34][35]. Scope: turbine-engine part repairs, coatings, PMA parts, with in-house investment casting, coating and machining [34][36][37]. Chromalloy was an early hot-section PMA maker through **BELAC LLC**, its joint venture with Lufthansa Technik and United Airlines, which made a CFM56-3 (military F108) stage-1 HPT blade PMA; the US Air Force awarded BELAC a one-year, $2.6M contract for F108 HPT blades [33]. It also announced an FAA-approved V2500 HPT blade PMA (Aviation Week, MRO Europe; date not captured) [32]. Distribution: AAR Corp (NYSE: AIR) signed an engine-parts supply agreement with Chromalloy (Nov 2024) and an exclusive PW4000 agreement (Mar 2025) [38][39].
- **FTAI Aviation (NASDAQ: FTAI) — PMA via joint venture.** FTAI's FY2025 10-K: FTAI "develops and manufactures Parts Manufacturer Approval ('PMA') parts through a joint venture," part of a "proprietary portfolio of products that enables it to provide cost savings and flexibility to airline, lessor, and maintenance, repair, and operations customers" [20]. The filings retrieved do not name the partner, the ownership split, the accounting treatment, or revenue from PMA. Third-party commentary (In Practise interviews; Komodo Capital and Kairos Research blogs) says: FTAI formed an "exclusive perpetual partnership" with Chromalloy in 2018 giving FTAI access to five CFM56 engine parts that Chromalloy manufactures under PMA once approved; FTAI receives them "at cost"; two parts had been FAA-approved as of the posts (described as HPT and LPT parts) with three awaiting; the HPT stage-1 vane was "the second of five planned CFM56 parts" and was certified "in November" [66][67][68][69][70]. See section 4 and Tensions T2–T3 for the inconsistencies among these descriptions.
- **Historical OEM-made PMA.** Pratt & Whitney ran a unit (Global Material Solutions) that obtained FAA PMA for CFM56-3 parts in the late 2000s, producing a public dispute with CFM at Farnborough; FlightGlobal covered P&W's PMA tests and the "spat" [51][52]. The dates and the unit's eventual wind-down were not re-verified in this session.

**OEMs**

- **CFM International** (GE Aerospace, NYSE: GE; Safran, EPA: SAF). Responses recorded in sources: (i) new CFM56-5B/7B HPT blade design introduced 16 Oct 2023 (increased wall thickness, optimized dovetail loading, tightened tolerances, "up to 25 percent longer life in certain operating environments") [42]; (ii) the 1,000th and later the 1,700th set shipped, output "almost two and a half times" year over year [40][41]; (iii) about 400 industrialized CFM56 repairs since early 2023 [40]; (iv) Jacey Welsh, CFM executive vice president for CFM56, quoted that the upgraded blades are "designed to keep customers flying with OEM parts they know and trust" and "can help extend time on-wing to optimize cost of ownership and enhance residual value" [40]; (v) the 2018 IATA Conduct Policies (section 2.9); (vi) the multi-year materials agreement with FTAI announced 22 Jan 2026, under which FTAI "secures OEM replacement part supply, thrust performance upgrades and component repair," described by both as strengthening "the open maintenance, repair, and overhaul (MRO) ecosystem" [23]. No CFM statement specifically about Chromalloy's HPT blade PMA was found (Unknown U10). GE also runs upgraded repair-warranty programmes for its own engine parts (Aviation Week; GE release) [not numbered: see sources 74–75].

**Airlines (adoption datapoints found)**

- Southwest Airlines (NYSE: LUV): 341 PMA parts in use in 2022, $54M saved that year; evaluating PMA and DER for the 737-700/CFM56-7B fleet as it is phased out (Aviation Week) [58].
- United Airlines (NASDAQ: UAL): launch customer for BELAC's CFM56-3 HPT blade PMA (2000s) [33 and search summary].
- Delta, American and others: no PMA-policy source retrieved (Unknown U11). Note that the 2023 "unapproved parts" episode (AOG Technics; CFM56 the most affected model; parts found at Delta, United, Southwest, American) involved forged documentation, not PMA parts, and is a different category [59].
- Chromalloy's HPT blade announcement said orders covered "all planned production for the rest of 2025" with "many customers now reserving manufacturing slots well into 2026," without naming customers [27][28].

**Lessors**

- Position statements retrieved are from trade and association sources dated 2009–2016: operating lessors "most often stipulated the use of OEM parts in the return conditions" (Aircraft Commerce, 2009) [56]; "most lessors permit PMA to be used on leased aircraft (with a few exceptions); the carrier just has to demand the right," and lessors "grow more willing to waive the 'no PMA' clauses" (MARPA, Nov 2015) [53]; for engines, "lessors, in the vast majority of cases support the OEMs by forbidding the installation of PMA and DER" (ELFC, mid-2016) [54]. No current (2024–2026) statement from AerCap, Air Lease, Avolon, SMBC, BOC Aviation, Willis Lease or any engine lessor was retrieved (Unknown U1). FTAI's 10-K lists lessors among the customers to whom its PMA portfolio offers cost savings [20].

---

## 4. Numbers

### 4.1 HEICO Flight Support Group (reference PMA business)

| Metric | Value | Period | Source |
|---|---|---|---|
| FSG net sales | $3,117.3M (+18%) | FY to 31 Oct 2025 | HEICO 10-K FY2025 [15]; Q4 FY25 release 18 Dec 2025 [16] |
| FSG net sales, prior year | $2,639.4M | FY2024 | [15][16] |
| FSG operating income | $750.4M (+27%) | FY2025 | [16] |
| FSG operating income, prior year | $593.1M | FY2024 | [16] |
| FSG operating margin (computed) | 24.1% FY2025; 22.5% FY2024 | | computed from [16] |
| FSG Q1 FY2025 operating margin | 23.3% | Q1 to 31 Jan 2025 | Q1 FY25 release [17] |
| Aftermarket replacement parts organic growth | +15%; +$263.9M | FY2025 | [16] |
| New PMAs added | ~300–500 per year | "in recent years" | HEICO 10-K [15] |
| Pricing statement | "lower prices than those manufactured by OEMs"; "functional equivalent" | 10-K | [15] |

### 4.2 Chromalloy and the CFM56 PMA roster

| Item | Value / date | Source |
|---|---|---|
| Revenue | "$1 billion-plus" | GovConWire Dec 2022 [34]; FlightGlobal [36] |
| Employees | ~4,000 | [34] |
| Ownership | Veritas Capital via Sequa (closed Dec 2022; from Carlyle, owner since 2007) | [34][35]; BusinessWire 15 Sept 2022 [not read] |
| CFM56-5B/7B HPT blade PMA | FAA approval announced 30 Oct 2025; "only aftermarket alternative" to OEM new blade; orders cover remaining 2025 output, slots reserved into 2026 | Chromalloy release [26]; Newswire [27]; AviTrader 31 Oct 2025 [28]; AVM [29] |
| CFM56-5B/7B HPT stage-1 vane (nozzle) PMA | FAA approval; Chromalloy release; third-party commentary dates it to Nov 2025 | Chromalloy [30]; Komodo [68] |
| CFM56 LPT vane "up-change" PMA | FAA approval; date not captured | Aeromorning [31] |
| V2500 HPT blade PMA | FAA-approved, unveiled at MRO Europe; date not captured | Aviation Week [32] |
| CFM56-3 (F108) HPT blade PMA via BELAC | USAF one-year contract $2.6M | PR Newswire [33] |
| -5B/-7B installed base cited | "over 20,000 engines" | [26][27] |

### 4.3 FTAI–Chromalloy (filing versus commentary)

| Item | FTAI filings | Third-party commentary | Source |
|---|---|---|---|
| Existence of PMA activity | "develops and manufactures PMA parts through a joint venture" | — | FTAI 10-K FY2025 [20]; 10-Q Q2 2026 [21] |
| Partner named | not in retrieved text | Chromalloy | [66]–[70] |
| Formation | not retrieved | 2018, "exclusive perpetual partnership" | Komodo [68]; Kairos [69] |
| Ownership / economics | not retrieved | parts supplied "at cost" | [68][69] |
| Parts covered | not retrieved | five CFM56 hot-section parts | [68][69] |
| Approved to date | not retrieved | "two approved (HPT, LPT), three pending" (blog); HPT vane 1 "second of five" (blog); separately Chromalloy announcements show HPT blade (Oct 2025), HPT vane 1 (Nov 2025), LPT vane (undated) | [68][69][26][30][31] |
| Savings claim | not quantified in retrieved filings | "up to $2 million per shop visit"; "5–10 percentage points of additional margin" | [68][69][70] |
| Customer uptake | not retrieved | Chromalloy: production sold out for 2025, slots into 2026 (customers unnamed) | [27][28] |
| FTAI–CFM materials agreement | announced 22 Jan 2026: OEM parts supply, thrust upgrades, component repair, multi-year | — | GlobeNewswire [23] |

### 4.4 Market size and penetration estimates

| Estimate | Value | Source (type) |
|---|---|---|
| Commercial aircraft PMA market | $11.8B (2025) → $16.1B (2034), 3.37% CAGR | IMARC (market-research vendor) [60] |
| Commercial aircraft PMA market | $14B by 2026 | Global Industry Analysts via PR Newswire, 2022 [62] |
| Engine PMA parts + DER repair market | $2,952.2M (2022) → $6,174.7M (2032) | GII Korea listing of a vendor report [61] |
| PMA share of engine parts market | "capped at around 21%" | FlightGlobal, undated older article [64] |
| Global aircraft aftermarket parts | $56.5B (2026) → $91.3B (2033); engine parts 34.8% | Persistence Market Research [63] |
| Southwest PMA saving | $54M from 341 PMA parts, 2022 | Aviation Week [58] |

### 4.5 Price inputs for the worked example

| Input | Value | Source |
|---|---|---|
| New OEM CFM56 HPT blade | ~$20,000 each | In Practise interview [66] |
| HPT blade listing | ~€35,000 each | ATU-hosted page [72] (weak) |
| HPT blade + vane set | "up to a few million dollars" | In Practise [66] |
| CFM56-7B fixed-price repair catalogue | exists, 3 June 2026 edition; prices not extracted | SR Technics [71] |
| CFM new-blade life claim | "up to 25% longer life in certain operating environments" | CFM/Safran 16 Oct 2023 [42] |
| CFM HPT blade output | 1,700th set shipped; output ~2.5x y/y | CFM story [40] |

---

## 5. Constraints and bottlenecks

1. **Regulatory approval of complex parts.** A T&C PMA for a cooled hot-section part requires the applicant to generate the material, durability and safety-analysis evidence itself (AC 33-8) [6]. The multi-year path to the Chromalloy HPT blade is the datapoint; the application-to-approval interval is unknown (U4).
2. **"Critical component" status and export of approval.** Under the TIP, a critical T&C PMA needs an EASA-validated STC to be installable on EU-registered engines without further showing [8][9]. Whether the CFM56 HPT blade and vane PMAs fall under the critical definition determines their addressable fleet (U5).
3. **Manufacturing capacity.** Chromalloy said HPT blade production was fully ordered for the rest of 2025 with slots reserved into 2026 [27][28]. Single-crystal casting and coating capacity is the limiting process; capacity figures were not disclosed (U12). CFM, for its part, reports raising OEM blade output ~2.5x y/y [40].
4. **Lease return conditions.** Engine leases forbidding PMA and DER "in the vast majority of cases" (2016) confine PMA to owned engines, to engines whose leases permit it, or to engines whose lessee will reconfigure before return [54][55]. Current prevalence is unknown (U1).
5. **Repair-versus-replace cadence.** Demand for new blades (OEM or PMA) arises mainly at shop visits where blades cannot be repaired again; CFM's industrialized repairs (laser welding) and new longer-life blade extend the repair window [40][42][66].
6. **Residual value and marketability.** Return-condition clauses, TRUEngine designation and the lessor statements above tie PMA content to perceived resale value [48][54][56]. Quantified residual-value effects were not found (U13).
7. **OEM parts supply to the independent.** FTAI's Jan 2026 agreement secures OEM replacement parts for FTAI's shop visits [23]; the terms (duration, volumes, pricing) are undisclosed (U14).
8. **Exclusivity.** If the FTAI–Chromalloy arrangement is exclusive for the five parts (commentary only), other MROs' access to those PMA parts, and at what price, is a constraint on market-wide penetration (U3).

---

## 6. Tensions

- **T1 — Size of FTAI's PMA saving.** Investor blogs: "up to $2 million per shop visit" from five parts supplied "at cost" [68][69]. FTAI's filings retrieved: qualitative "cost savings and flexibility" only [20][21]. The worked example (2.8) shows $2.0M requires either a per-blade price near the €35,000 listing or large savings on the four non-blade parts.
- **T2 — How many FTAI/Chromalloy parts are approved.** One blog: "two parts approved (HPT and LPT), three awaiting" [69]; another: the HPT stage-1 vane is "the second of five" approved [68]; Chromalloy's own announcements show at least three CFM56-5B/7B approvals (HPT blade Oct 2025, HPT vane 1 Nov 2025, LPT vane undated) [26][30][31]. Whether the LPT vane is one of the "five" is not stated.
- **T3 — Nature of the FTAI–Chromalloy relationship.** FTAI: a "joint venture" through which it "develops and manufactures" PMA parts [20]. Commentary: an "exclusive perpetual partnership" with parts bought "at cost" [68][69]. These describe different structures (equity JV versus supply agreement).
- **T4 — Market size.** $11.8B in 2025 (IMARC) vs $14B by 2026 (GIA) for commercial-aircraft PMA [60][62]; and an engine PMA-plus-DER market of only $2.95B in 2022 (GII) [61] against IMARC's statement that engines are the largest segment of the $11.8B. Different scope definitions are likely but not stated.
- **T5 — OEM HPT blade price.** ~$20,000 per new blade (In Practise interview) [66] vs ~€35,000 per blade (web listing of uncertain condition) [72]: a $1.6M vs $3.1M blade set at 80 blades.
- **T6 — Lessor stance.** "Most lessors permit PMA ... with a few exceptions" (MARPA 2015, aircraft context) [53] vs engine lessors "in the vast majority of cases ... forbidding the installation of PMA and DER" (ELFC 2016) [54]. Different asset classes and dates.
- **T7 — PMA ceiling.** FlightGlobal's "capped at around 21%" of engine parts [64] vs vendor forecasts of the engine PMA/DER market doubling 2022–2032 [61]; both are forecasts, neither sourced to disclosed data.
- **T8 — OEM support stance.** CFM's 2018 Conduct Policies (no warranty voiding, no service refusal) [43][44] alongside CFM's TRUEngine designation and residual-value messaging for OEM-only configuration [40][48][49]. Both are CFM positions; they address different levers (contractual support vs resale marketing).

---

## 7. Unknowns

- **U1 — Current lessor return-condition practice (2024–2026).** All lessor statements found are 2009–2016. Resolve with recent lessor 10-K/20-F lease descriptions (AerCap, Air Lease, Willis Lease), ISTAT or IBA surveys, or lessor conference remarks.
- **U2 — PMA price discount for the Chromalloy HPT blade and vane** (and HEICO's typical discount). Resolve with Chromalloy/FTAI pricing disclosure or MRO price catalogues (the SR Technics 2026 CFM56-7B catalogue may list PMA options [71]).
- **U3 — FTAI–Chromalloy JV terms:** formation date, ownership split, accounting (consolidated vs equity method), exclusivity, "at cost" pricing, revenue recognized. Resolve by reading FTAI's FY2018–FY2025 10-Ks for the JV footnote and any 8-K.
- **U4 — Time from PMA application to approval** for hot-section parts. Resolve via FAA PMA database (DRS) entries with dates, or company statements.
- **U5 — Whether the CFM56 HPT blade/vane PMAs are "critical components"** under the TIP and therefore which EASA acceptance clause applies; whether EASA acceptance has been obtained.
- **U6 — Acceptance by other regulators** (UK CAA, TCCA, ANAC, CAAC, DGCA India) of these PMAs.
- **U7 — Any PMA for CFM56 life-limited rotating parts.** None found.
- **U8 — How DER-approved repair data is accepted on EU-registered engines** under the TIP.
- **U9 — HEICO portfolio split** by part category (consumables vs rotating vs hot-section) and HEICO's PMA discount.
- **U10 — Any CFM/GE statement specifically on the Chromalloy HPT blade PMA**, and any GE "material" programme (e.g. TrueChoice Material) positioning against PMA. The brief's phrase "material solutions" was not matched to a current CFM/GE programme in this session; the historical P&W "Global Material Solutions" CFM56-3 PMA venture was found only via headlines [51][52].
- **U11 — PMA policies of Delta, American, United, Ryanair, and non-US CFM56 operators** for hot-section parts.
- **U12 — Chromalloy production capacity** (blade sets per year) and FTAI's share of it.
- **U13 — Quantified residual-value effect** of PMA/DER content on engine or aircraft appraisals.
- **U14 — Terms of the FTAI–CFM Jan 2026 materials agreement** (duration, volumes, pricing, whether it restricts FTAI's PMA use).
- **U15 — Customer uptake figures for the Chromalloy blade** (named airlines/MROs, sets delivered). Only "sold out for 2025" was found.
- **U16 — CFM56-7B HPT blade count per set** (80 is a recollection, unverified here) and the OEM list price for a full HPT blade and vane set.
- **U17 — Dates for the LPT vane PMA and the V2500 HPT blade PMA.**

---

## 8. Terms introduced

- **Type certificate (TC):** FAA approval of an aircraft, engine or propeller design; its holder is the **TCH**.
- **Supplemental type certificate (STC):** FAA approval of a change to a type-certificated design.
- **PMA (Parts Manufacturer Approval):** FAA design-plus-production approval under 14 CFR Part 21 Subpart K allowing a non-TCH to make and sell replacement or modification parts.
- **Test and computation (T&C):** PMA basis in which the applicant proves airworthiness by its own analysis and testing of a reverse-engineered design.
- **Identicality:** PMA basis in which the applicant shows its design is identical to the TCH's, with or without a licence from the TCH.
- **Life-limited part (LLP):** engine part with a mandatory retirement life in cycles, listed in the Airworthiness Limitations Section.
- **Critical component (TIP definition):** part designated critical by the design approval holder or state-of-design authority, typically with an airworthiness-limitation interval.
- **TIP (Technical Implementation Procedures):** the FAA–EASA document implementing the US–EU bilateral, including mutual acceptance rules for PMA parts.
- **FAA Form 8130-3 / EASA Form 1:** authorized release certificates accompanying a part.
- **DER (Designated Engineering Representative):** FAA-appointed engineer who approves or recommends approval of engineering data on the FAA's behalf.
- **FAA Form 8110-3:** the DER's statement of compliance approving repair or alteration data.
- **Major repair:** repair requiring FAA-approved data; a **DER repair** is one approved via a DER rather than taken from the OEM manual.
- **Engine Shop Manual (ESM):** the OEM's approved repair and overhaul instructions.
- **Used serviceable material (USM):** OEM parts removed from retired engines and re-released for use.
- **Performance-restoration shop visit:** core-focused shop visit to restore exhaust-gas-temperature margin (D1).
- **Return conditions / OEM-only clause:** lease terms specifying redelivery condition; an OEM-only clause bars PMA parts and DER repairs at return.
- **TRUEngine:** CFM programme designating engines maintained to CFM-approved parts and repairs.
- **Conduct Policies (CFM–IATA 2018):** CFM's published commitments on warranty, service and parts access for engines with non-CFM parts or repairs.
- **Hot section:** combustor, HPT blades and vanes (nozzles), and adjacent parts exposed to combustion gas; **HPT stage-1 vane** = HPT nozzle.

---

## 9. Sources

Regulatory
1. eCFR, 14 CFR Part 21 Subpart K — Parts Manufacturer Approvals (current). https://www.ecfr.gov/current/title-14/chapter-I/subchapter-C/part-21/subpart-K
2. FAA, Advisory Circular 21.303-4 (PMA application). https://www.faa.gov/documentLibrary/media/Advisory_Circular/AC_21_303-4.pdf
3. FAA, AC 21.303-3, Application for PMA via Tests and Computations or Identicality. https://www.faa.gov/regulations_policies/advisory_circulars/index.cfm/go/document.information/documentID/1023551
4. FAA, Order 8110.42D, Parts Manufacturer Approval Procedures (with change 1). https://www.faa.gov/documentLibrary/media/Order/FAA_Order_8110.42D_w-chg_1.pdf
5. FAA, Parts Manufacturer Approval — Design Approval (web page). https://www.faa.gov/aircraft/air_cert/design_approvals/pma/pma_des
6. FAA, AC 33-8, Guidance for PMA of Turbine Engine and APU Parts under Test and Computation. https://www.faa.gov/regulations_policies/advisory_circulars/index.cfm/go/document.information/documentID/99620
7. FAA, Notice N 8110.55, PMA by Identicality, 19 July 1996. https://www.faa.gov/documentLibrary/media/Order/N8110-55.pdf
8. FAA–EASA, Technical Implementation Procedures Rev 7 with Amendment 1. https://www.faa.gov/aircraft/air_cert/international/bilateral_agreements/eu/tip/tip_rev7_with_amdt1_incorporated
9. FAA–EASA, Technical Implementation Procedures Rev 6 with Amendments 1 and 2 (PDF). https://www.faa.gov/sites/faa.gov/files/EUTIP_Rev6_w_amdt1_amdt2.pdf
10. FAA, EASA Frequently Asked Questions (PDF). https://www.faa.gov/sites/faa.gov/files/aircraft/air_cert/international/easa/EASA_FAQ.pdf
11. FAA, Order 8110.37F, Designated Engineering Representative (DER) Handbook. https://www.faa.gov/documentLibrary/media/Order/FAA_Order_8110.37F.pdf
12. FAA, Documenting Compliance Findings (Form 8110-3 guidance). https://www.faa.gov/sites/faa.gov/files/other_visit/aviation_industry/designees_delegations/individual_designees/compliance_findings_8110-3.pdf
13. FAA, Order 8300.16, Major Repair and Alteration Data Approval (field approval process). https://www.faa.gov/documentLibrary/media/Order/8300_16.pdf
14. FAA, AC 20-154, Guide for Developing a Receiving Inspection System for Aircraft Parts. https://www.faa.gov/documentLibrary/media/Advisory_Circular/AC_20-154.pdf

HEICO (sec.gov)
15. HEICO Corp, Form 10-K for fiscal year ended 31 Oct 2025. https://www.sec.gov/Archives/edgar/data/46619/000004661925000082/hei-20251031.htm
16. HEICO Corp, Q4/FY2025 earnings release (Ex. 99.1 to 8-K), 18 Dec 2025. https://www.sec.gov/Archives/edgar/data/46619/000004661925000076/a10312025ex991earningsrele.htm
17. HEICO Corp, Q1 FY2025 earnings release (Ex. 99.1), Feb 2025. https://www.sec.gov/Archives/edgar/data/46619/000004661925000013/a01312025q1ex991earningsre.htm
18. HEICO Corp, Q3 FY2026 earnings release (Ex. 99.1), Aug 2026 (link only; not read). https://www.sec.gov/Archives/edgar/data/0000046619/000004661926000018/a07312026ex991earningsrele.htm
19. HEICO Corp, press release on acquisition of Wencor Group (Ex. 99.1), 2023. https://www.sec.gov/Archives/edgar/data/46619/000095014223001445/eh230358705_ex9901.htm

FTAI (sec.gov, GlobeNewswire, PR Newswire)
20. FTAI Aviation Ltd., Form 10-K for FY2025 (filed early 2026). https://www.sec.gov/Archives/edgar/data/1590364/000162828026012940/ftai-20251231.htm
21. FTAI Aviation Ltd., Form 10-Q for quarter ended 30 June 2026. https://www.sec.gov/Archives/edgar/data/0001590364/000162828026051412/ftai-20260630.htm
22. FTAI Aviation Ltd., Form 10-K for FY2024. https://www.sec.gov/Archives/edgar/data/1590364/000159036425000006/ftai-20241231.htm
23. FTAI Aviation, "FTAI Aviation Announces Multi-Year Materials Agreement with CFM International to Further Support CFM56 Engines," GlobeNewswire, 22 Jan 2026. https://www.globenewswire.com/news-release/2026/01/22/3223741/35538/en/FTAI-Aviation-Announces-Multi-Year-Materials-Agreement-with-CFM-International-to-Further-Support-CFM56-Engines.html
24. FTAI Aviation Ltd., Form 8-K Ex. 99.1 (FY2025; link only, not read). https://www.sec.gov/Archives/edgar/data/1590364/000114036125006099/ef20044380_ex99-1.htm
25. AAR Corp / FTAI, "AAR and FTAI Aviation extend their exclusive Serviceable Engine Products agreement ... through 2030," PR Newswire, 2025. https://www.prnewswire.com/news-releases/aar-and-ftai-aviation-extend-their-exclusive-serviceable-engine-products-agreement-providing-cfm56-engine-material-to-the-global-aviation-aftermarket-through-2030-302412621.html

Chromalloy and PMA roster
26. Chromalloy, "Chromalloy Secures FAA Approval of CFM56 High Pressure Turbine Blade PMA," 30 Oct 2025. https://www.chromalloy.com/chromalloy-secures-faa-approval-of-cfm56-high-pressure-turbine-blade-pma/
27. Newswire.com, same release, 30 Oct 2025. https://www.newswire.com/news/chromalloy-secures-faa-approval-of-cfm56-high-pressure-turbine-blade-22665618
28. AviTrader, "Chromalloy wins FAA approval for CFM56 HPT blade," 31 Oct 2025. https://avitrader.com/2025/10/31/chromalloy-wins-faa-approval-for-cfm56-hpt-blade/
29. Aviation Maintenance Magazine, "Chromalloy Secures FAA Approval of CFM56 High Pressure Turbine Blade PMA," 2025. https://avm-mag.com/chromalloy-secures-faa-approval-of-cfm56-high-pressure-turbine-blade-pma
30. Chromalloy, "Chromalloy Receives FAA Approval of CFM56-5B/7B HPT Turbine Vane 1 PMAs," 2025. https://www.chromalloy.com/chromalloy-receives-faa-approval-of-cfm56-5b-7b-hpt-turbine-vane-1-pmas/
31. Aeromorning, "Chromalloy Secures FAA Approval of CFM56 LPT Vane Up-Change PMA" (undated). https://aeromorning.com/en/chromalloy-secures-faa-approval-of-cfm56-lpt-vane/
32. Aviation Week, "Chromalloy Unveils FAA-Approved V2500 HPT Blade," MRO Europe (date not captured). https://aviationweek.com/shows-events/mro-europe/chromalloy-unveils-faa-approved-v2500-hpt-blade
33. PR Newswire, "U.S. Air Force Selects Chromalloy Joint Venture Company — BELAC LLC — to Provide High Pressure Turbine Blades for F108 Aircraft Engines" (2000s). https://www.prnewswire.com/news-releases/us-air-force-selects-chromalloy-joint-venture-company---belac-llc---to-provide-high-pressure-turbine-blades-for-f108-aircraft-engines-103934938.html
34. GovConWire, "Veritas Buys Sequa From Carlyle, Adds Chromalloy to Portfolio," Dec 2022. https://govconwire.com/2022/12/veritas-buys-sequa-from-carlyle-adds-chromalloy-to-portfolio
35. Bloomberg, "Carlyle Is Said to Explore $2 Billion Sale of Sequa Business," 19 July 2022. https://www.bloomberg.com/news/articles/2022-07-19/carlyle-is-said-to-explore-2-billion-sale-of-sequa-business
36. FlightGlobal, "The sum of the parts" (Chromalloy profile). https://www.flightglobal.com/the-sum-of-the-parts/96138.article
37. FlightGlobal, "Chromalloy PMA prospers under egregious economy." https://www.flightglobal.com/chromalloy-pma-prospers-under-egregious-economy/85397.article
38. PR Newswire, "AAR signs exclusive PW4000 agreement with Chromalloy," Mar 2025. https://www.prnewswire.com/news-releases/aar-signs-exclusive-pw4000-agreement-with-chromalloy-302392076.html
39. PR Newswire, "AAR signs new engine parts supply agreement with Chromalloy," Nov 2024. https://www.prnewswire.com/news-releases/aar-signs-new-engine-parts-supply-agreement-with-chromalloy-302301855.html

CFM / GE / IATA
40. CFM International, "CFM boosts HPT blade output and repair to meet extended demand for CFM56 engines" (2025–26; date not captured). https://www.cfmaeroengines.com/stories/cfm-boosts-hpt-blade-output-and-repair-to-meet-extended-demand-for-cfm56-engines (GE mirror: https://www.geaerospace.com/news/articles/cfm-boosts-hpt-blade-output-and-repair-meet-extended-demand-cfm56-engines)
41. CFM International, "Investing in Durability: CFM ships 1,000th set of new CFM56 HPT blades." https://www.cfmaeroengines.com/stories/investing-in-durability-cfm-ships-1000th-set-of-new-CFM56-HPT-blades
42. Safran / CFM, "CFM introduces upgraded HPT blade for CFM56 engines," 16 Oct 2023. https://www.safran-group.com/pressroom/cfm-introduces-upgraded-hpt-blade-cfm56-engines-2023-10-16 ; https://www.cfmaeroengines.com/press-articles/cfm-introduces-upgraded-hpt-blade-for-cfm56-engines-
43. IATA, "IATA–CFM Agreement on Engine Maintenance" (2018, PDF). https://www.iata.org/contentassets/b7fc716af6a94192b1889420c7d573ce/iata-cfm-agreement-on-engine-maintenance.pdf
44. IATA, "CFM Conduct Policies and Implementation Measures" (PDF). https://www.iata.org/contentassets/f03b1a4b79534b99802f10cd23b19ec2/cfm-conduct-policies-and-implementation-measures.pdf
45. CFM International, "CFM External Guidance" (Mar 2019, PDF). https://www.cfmaeroengines.com/wp-content/uploads/2019/03/CFM_External_Guidance.pdf
46. MARPA, "CFM agrees to permit the use of PMA parts and DER repairs," 1 Aug 2018. https://marpa.pmaparts.org/2018/08/01/cfm-agrees-to-permit-the-use-of-pma-parts-and-der-repairs/
47. Aviation Suppliers Association, Member Bulletin Oct 2018, "CFM Agrees to permit the use of PMA Parts and DER Repairs." https://www.aviationsuppliers.org/ASA-Member-Bulletin---Oct-2018---CFM-Agrees-to-permit-the-use-of-PMA-Parts-and-DER-Repairs
48. GE Aerospace, TrueEngine presentation (PDF). https://www.geaerospace.com/sites/default/files/trueengine-presentation.pdf
49. GE Aerospace / CFM, "CFM expands TRUEngine program; unique content assurance guarantee [for] subsequent [buyers]." https://geaerospace.com/news/press-releases/services/cfm-expands-truengine-program-unique-content-assurance-guarantee-subsequent
50. AIN, "CFM TRUEngine program to cover subsequent buyers," 12 Sept 2012. https://backend.ainonline.com/aviation-news/business-aviation/2012-09-12/cfm-truengine-program-cover-subsequent-buyers
51. FlightGlobal, "Farnborough: P&W parts display fuels CFM spat" (Guy Norris). https://www.flightglobal.com/farnborough-pandw-parts-display-fuels-cfm-spat/68616.article
52. FlightGlobal, "P&W to conclude PMA parts tests in six weeks." https://www.flightglobal.com/pandw-to-conclude-pma-parts-tests-in-six-weeks/77119.article

Lessors and airlines
53. MARPA, "Are leases getting looser?", 10 Nov 2015. https://marpa.pmaparts.org/2015/11/10/are-leases-getting-looser/
54. Engine Lease Finance Corp (ELFC), "An overview of the aircraft engine aftermarket in mid 2016." https://elfc.com/an-overview-of-the-aircraft-engine-aftermarket-in-mid-2016/
55. Aviation Suppliers Association (CAVU Café), "Airlines: now is the time to choose lessors who accommodate PMA and DER repairs." https://www.aviationsuppliers.org/airlines-now-is-the-time-to-chose-lessors-who-accommodate-pma-and-der-repairs
56. Aircraft Commerce, Issue 67 (2009), maintenance article on PMA and lessors (PDF). https://aircraft-commerce.com/wp-content/uploads/aircraft-commerce-docs/Maintenance/2009/ISSUE67_MTCE_A.pdf
57. Sofema Online, "Aircraft Lease Management — Continuing Airworthiness In-Service Considerations." https://legacy.sofemaonline.com/component/easyblog/aircraft-lease-management-continuing-airworthiness-in-service-considerations?Itemid=101
58. Aviation Week, "Southwest's 737-700 Engine Strategy As It Phases Out Fleet" (c. 2023). https://ngtest.aviationweek.com/mro/aircraft-propulsion/southwests-737-700-engine-strategy-it-phases-out-fleet
59. Fox Business, "Major US airlines find unapproved jet engine parts in some aircraft as alleged supplier faces lawsuit," 2023. https://www.foxbusiness.com/lifestyle/major-us-airlines-find-unapproved-jet-engine-parts-some-aircraft-alleged-supplier-faces-lawsuit

Market size (vendor and trade)
60. IMARC Group, "Commercial Aircraft Parts Manufacturer Approval Market" (2025 base). https://www.imarcgroup.com/report/en/commercial-aircraft-parts-manufacturer-approval-market
61. GII Korea listing, "Global Engine PMA Parts & DER Repair Market Research" (2022 base). https://www.giikorea.co.kr/report/marf1540758-global-engine-pma-parts-der-repair-market-research.html
62. PR Newswire / Global Industry Analysts, "...Commercial Aircraft PMA with the Market to Reach $14 Billion Worldwide by 2026," 2022. https://prnewswire.com/news-releases/new-analysis-from-global-industry-analysts-reveals-steady-growth-for-commercial-aircraft-pma-with-the-market-to-reach-14-billion-worldwide-by-2026-301488219.html
63. Persistence Market Research, "Aircraft Aftermarket Parts Market" (2026–2033). https://www.persistencemarketresearch.com/market-research/aircraft-aftermarket-parts-market.asp
64. FlightGlobal, "Aftermarket shocks" (PMA share capped ~21%; undated). https://flightglobal.com/aftermarket-shocks/73224.article
65. FlightGlobal, "Turning the tide" (Graham Warwick). https://flightglobal.com/turning-the-tide/51816.article

Third-party commentary on FTAI–Chromalloy (not FTAI disclosure)
66. In Practise, "FTAI, Chromalloy and CFM56 HPT Blade PMA" (expert interview). https://inpractise.com/articles/ftai-chromalloy-and-cfm56-hpt-blade-pma
67. In Practise, "FTAI & PMA Parts, ..." (interview digest). https://inpractise.com/articles/ftai-and-pma-parts-hermes-rolex-veralto-ccc-avon-cvna-lgi-w-didi
68. Komodo Capital (Substack), "Why FTAI Aviation ($FTAI) Presents a Rare Opportunity." https://komodocapital.substack.com/p/why-ftai-aviation-ftai-will-fly-in
69. Kairos Research (Substack), "Why I bought FTAI Aviation." https://kairosresearch.substack.com/p/why-i-bought-ftai-aviation
70. Yahoo Finance, "FTAI Aviation Ltd. (FTAI): A Bull Case Theory." https://finance.yahoo.com/news/ftai-aviation-ltd-ftai-bull-235824752.html

Price inputs
71. SR Technics, "CFM56-7B Capabilities & Price Catalogue," 3 June 2026 (PDF). https://www.srtechnics.com/media/zgcnmf3o/cfm56-7b-sr-technics-capabilitiesprice-catalogue-03062026.pdf
72. ATU-hosted page listing CFM56-7B HPT blade at ~€35,000 (provenance weak). https://g00431067.webhosting.atu.ie/?p=1313
73. AI Engineering Services Ltd (AIESL), bid document Part 2 (CFM56 material tender; PDF). https://www.aiesl.in/Doc/Tenders/bid-document-Part-2.pdf

GE repair warranties (referenced in section 3)
74. Aviation Week, "GE upgrades engine warranties for key models." https://aviationweek.com/air-transport/ge-upgrades-engine-warranties-key-models
75. GE Aerospace, "GE Aviation announces upgraded repair warranty programs [for] CF6 and ..." https://www.geaerospace.com/news/press-releases/commercial-engines/ge-aviation-announces-upgraded-repair-warranty-programs-cf6-and
