# D6 — Engine and aircraft leasing mechanics, and FTAI's Aviation Leasing segment

Dossier for the FTAI Aviation deep primer. Raw material for the writer; posture is explain-not-opine.
Searches: 17 WebSearch calls run on 2026-10-03 (an 18th was attempted and refused because the
session-wide search budget was exhausted). WebFetch unavailable; filing figures come from
sec.gov-restricted search and are cited to the EDGAR URL returned. Where a search result gave a
figure without the surrounding table, that is said. Where a figure was not retrieved, it is an
Unknown, not an estimate. Illustrative assumptions inside worked examples are tagged
"ASSUMED (illustrative)" and are not market data.

---

## 1. Summary

1. FTAI's Aviation Leasing segment owns aircraft and engines and rents them under operating leases, directly and through an equity-method investment; at 31 Dec 2025 it held 290 assets (47 aircraft, 243 engines), of which 8 aircraft and 17 engines are still in Russia, and 37 aircraft and 143 engines were on lease (FY2025 10-K).
2. Utilization was ~77% in Q4 2025 (days on lease, weighted by equity value, excluding airframes); weighted-average remaining lease term 44 months for aircraft and 38 months for engines on lease (FY2025 10-K).
3. Leasing equipment at cost fell from $2,963.5M (31 Dec 2024) to $2,057.6M (31 Dec 2025), net book value from $2,373.7M to $1,545.8M, as "Seed Assets" were sold to the 2025 Partnership (Strategic Capital vehicle); FY2025 gain on sale to the 2025 Partnership $46.4M (FY2025 10-K).
4. Lease income: FY2021 $173.9M; FY2022 $179.3M (FY2022 10-K); Q1 2025 $68.4M → Q1 2026 $39.9M; Q2 2025 $62.4M → Q2 2026 $27.8M (10-Q Q1 2026; Q2 2026 release). FY2023–FY2025 annual segment lines were not retrieved (Unknown).
5. 2026 Aviation Leasing Adjusted EBITDA guidance: $575M in the Feb 2026 release; one reading of the Jul 2026 release says it was cut to $475M "reflecting a continued shift to an asset-light business model"; another reading of the same release still shows $575M (Tension T1).
6. Russia: all Russian leases terminated in 2022; $120.0M impairment (net of maintenance deposits) wrote the assets to zero; insured value of the remaining Russia assets $210.7M; insurance recoveries $54.3M in 9M 2025 and $44.6M in Q1 2026 (10-K FY2022, 10-Q Q3 2025, FY2025 10-K, 10-Q Q1 2026).
7. Market: a 12-year-old 737-800 leased for ~$228K/month in July 2025 (−11% y/y) and a comparable A320-200 for ~$220K/month (−13%) (IBA); a CFM56-7B spare engine leased for ~$100K/month in 2024, up from ~$75K in 2019 (IBA); IBA's H1 2026 update reports narrowbody engine values "levelled off" after ~18 months of increases.
8. Willis Lease Finance (WLFC), the listed pure-play engine lessor: utilization 86.0% at 30 Sep 2025 (82.9% a year earlier); lease portfolio $2,888.5M; Q3 2025 lease rent $76.6M and maintenance reserve revenue $76.1M (WLFC Q3 2025 release / 10-Q).
9. Engine ABS: WEST VIII (2025, $596M, Series A rated A, Series B rated BBB, 64 assets) and WEST IX (Dec 2025, $392.9M, 49 assets, A/B notes, anticipated repayment Dec 2031, legal final Dec 2050) show the senior-subordinate template (KBRA; Asset Securitization Report).
10. WestJet (28 Sep 2026): 27 737-700s; the 2026 SPV bought 17 on sale-leaseback to WestJet, FTAI itself bought 10 off-lease for CFM56-7B engines and modules for its Maintenance, Repair and Exchange customers; price and lease terms not disclosed.

---

## 2. Mechanics

### 2.1 The operating lease, term by term

**Operating lease.** A contract under which the owner (the **lessor**) rents an aircraft or engine to an operator (the **lessee**) for a fixed term in exchange for periodic rent, while the lessor keeps title and keeps the **residual-value risk** — the risk that the asset is worth more or less than expected when it comes back. This distinguishes it from a **finance lease**, which transfers substantially all the economic risks and rewards of ownership to the lessee and is in substance a loan. Nearly all of FTAI's leases, and WLFC's, are operating leases; WLFC also reports a small book of "investments in sales-type leases" ($16.3M of its $2,888.5M portfolio at 30 Sep 2025), which are finance leases by another name (WLFC Q3 2025 release, [S14]).

**Lease rate.** The periodic rent, quoted per month. IBA quoted ~$228,000/month for a 12-year-old 737-800 and ~$220,000/month for a comparable A320-200 as of July 2025 ([S26],[S28]), and ~$100,000/month for a CFM56-7B spare engine in 2024 ([S20],[S21]).

**Lease-rate factor (LRF).** Monthly rent divided by the asset's current market value, expressed as a percentage. It is the leasing industry's gross-yield shorthand: an LRF of 1.0% means annual rent is 12% of value. LRF rises with asset age (older assets carry more residual and maintenance risk and depreciate faster in percentage terms) and with interest rates. Neither FTAI's 10-K nor the WLFC search results returned a stated portfolio LRF (Unknown U5). Algebraically: LRF = rent ÷ value, so an asset renting at $228,000/month on a value of V has LRF = $228,000 ÷ V; the same rent on a lower V is a higher LRF.

**Term.** Operating leases for mid-life narrowbodies typically run several years; FTAI reports a weighted-average remaining term of 44 months on aircraft and 38 months on engines currently on lease at 31 Dec 2025 ([S1]). Engine leases divide into **short-term** (a few months up to about three years, used to cover a shop visit or an AOG — "aircraft on ground" — event) and **long-term** (multi-year, used as a permanent spare) ([S36],[S39]).

**Security deposit.** Cash (or a letter of credit) the lessee posts at signing, held by the lessor against default and returned at redelivery if the lessee performs. It is a credit instrument, not a maintenance instrument. Amount: not retrieved from any source this session (Unknown U7); FTAI's 10-K balance sheet carries "security deposits" as a liability but the figure was not returned by search.

**Maintenance reserves (supplemental rent).** Periodic payments the lessee makes to the lessor, in addition to basic rent, "calculated with reference to the utilization of airframes, engines and other major life-limited components during the lease" (AerCap 20-F, [S31]). They are usually set per flight hour or per flight cycle and collected per component: airframe heavy checks, landing gear, auxiliary power unit (APU), each engine's performance restoration, and each engine's **life-limited parts (LLPs)** — rotating parts with a hard cycle limit after which they must be replaced (mba, [S35]; Maheshwari, [S34]). The mechanism: the lessee is "using up" maintenance life every hour it flies; the reserve pre-funds the eventual shop visit so that if the lessee defaults or returns the asset, the lessor already holds the cash equivalent of the life consumed. When the lessee performs the maintenance event, the lessor reimburses "the lesser of (1) the amount of the maintenance reserve held by the lessor associated with the specific maintenance event or (2) the qualifying costs related to the specific maintenance event" (Spirit Airlines 10-K FY2013, [S33]). Reserves are typically **non-refundable** beyond that reimbursement: any balance not claimed against a qualifying event stays with the lessor at lease end. For the lessor, reserve receipts are a liability (maintenance deposits) until the event or lease end, when they become revenue; WLFC books this as "maintenance reserve revenue" ($76.1M in Q3 2025, +52.8% y/y, [S14]).

**End-of-lease (EOL) compensation.** The alternative regime, used for stronger-credit lessees who do not pay reserves. The lessee must "re-deliver the aircraft in a similar maintenance condition (normal wear and tear excepted) as when accepted under the lease, with reference to major life-limited components," and "to the extent that such components are redelivered in a different condition than at acceptance, there is an end-of-lease compensation adjustment for the difference at redelivery" (AerCap 20-F, [S31]). Money flows in either direction: the lessee pays the lessor if the asset comes back with less life than delivered, and the lessor pays the lessee (or credits it) if more. In practice many leases combine both: reserves for some components, EOL adjustments for others.

**Return conditions.** The contractual minimum state of the asset at redelivery — for an engine, typically a minimum number of flight hours and cycles remaining to the next performance restoration and a minimum cycles-remaining on the LLPs, plus a borescope and a test-cell run; for an airframe, time remaining to the next heavy check, fresh paint or a paint credit, records in order. Return conditions, together with the reserve/EOL regime, decide who bears the cost of the maintenance life consumed during the lease.

**Half-life and full-life.** Industry conventions for stating an asset's value independent of its maintenance condition. **Full-life** means every major component is fresh from its overhaul and every LLP has its full cycle limit remaining. **Half-life** means each component is midway between overhauls and LLPs have half their cycles remaining. Appraisers quote base values at half-life; the actual trading price of a specific aircraft or engine is the half-life value plus or minus a **maintenance adjustment** for how its condition differs from half-life. Because a CFM56 shop visit and an LLP replacement are each multi-million-dollar events (see D1 and D2 for cost builds), the maintenance adjustment on a mid-life narrowbody can be a large fraction of its half-life value, and on an engine it can exceed the half-life value of the bare engine.

**Residual value.** The lessor's forecast of what the asset will be worth (or fetch in a part-out) at the end of its depreciation life. FTAI's 10-K depreciation policy for leasing equipment was not returned by search (Unknown U8).

**How a lessor's return decomposes.** Over the holding period, a lessor's economic return is:

  (a) rental yield — rent received, i.e., LRF × value, plus net maintenance-reserve retention;
  minus (b) depreciation — the fall in the asset's value from purchase to disposal (or the book charge, straight-line to residual);
  minus (c) financing cost — interest on the debt funding the asset (bank loan, warehouse line or ABS notes) and the cost of equity;
  plus or minus (d) end-of-life proceeds — the sale price or part-out proceeds versus the carrying residual, plus any EOL compensation collected.

The balance between (a) and (b) is what makes mid-life assets attractive to specialist lessors: an older asset has a higher LRF (more rent per dollar of value) and most of its depreciation is already behind it, but it has more maintenance exposure and a shorter remaining lease life, so (d) matters more. FTAI's structure routes (d) into its Aerospace Products segment: off-lease aircraft are a source of engines and modules (WestJet release: the 10 off-lease 737-700s "will support FTAI's Aerospace Products business by expanding the Company's supply of CFM56-7B engines and modules available to its Maintenance, Repair and Exchange customers", [S11]).

### 2.2 Worked example: a 12-year-old 737-800 on a six-year operating lease

Sourced inputs: rent $228,000/month for a 12-year-old 737-800 (IBA, July 2025, [S26]). Everything else below is ASSUMED (illustrative) to show the arithmetic; the real contract values are negotiated case by case and no source this session gave reserve rates or shop-visit costs (D1 and D2 carry the shop-visit cost build).

Assumptions (illustrative): term 72 months; utilization 250 flight hours (FH) and 140 flight cycles (FC) per month per engine; engine performance-restoration (PR) reserve $150/FH per engine; engine LLP reserve $100/FC per engine; one engine PR shop visit in month 48 costing $4.5M; at delivery both engines had 8,000 FH since their last PR and the return condition requires no more than 12,000 FH since PR at redelivery.

Step 1 — basic rent over the term: $228,000 × 72 = $16,416,000.

Step 2 — reserves accrued per engine over 72 months: PR $150 × 250 × 72 = $2,700,000; LLP $100 × 140 × 72 = $1,008,000. Two engines: $5,400,000 PR + $2,016,000 LLP = $7,416,000. Reserve receipts are therefore 45% of basic rent in this example — maintenance cash flow is not a side-show; it is comparable in size to rent.

Step 3 — the month-48 shop visit on engine 1: PR reserve balance for engine 1 at month 48 = $150 × 250 × 48 = $1,800,000. Qualifying cost $4,500,000. Lessor reimburses the lesser: $1,800,000. The lessee funds the remaining $2,700,000 itself. (This is the typical "reserves rarely cover a full visit" outcome: the reserve covers life consumed since the lease began, not the life consumed by prior operators, unless the asset was delivered fresh from overhaul.) After month 48, engine 1 accrues PR reserves again from zero.

Step 4 — lease-end on engine 2 (no shop visit during the lease). Delivered at 8,000 FH since PR; flew 250 × 72 = 18,000 FH; would be at 26,000 FH since PR — but the return condition caps redelivery at 12,000 FH since PR, so the lessee must either perform a PR before redelivery (and claim up to its $2,700,000 reserve balance against the cost) or negotiate a cash settlement. Under a pure reserve regime, if the lessee redelivers out of condition, the lessor keeps the $2,700,000 PR balance and $1,008,000 LLP balance and pursues the shortfall. Under an EOL-compensation regime (no reserves paid), the lessee would owe the lessor compensation for 18,000 FH of PR life consumed, priced at an agreed $/FH, plus compensation for 10,080 cycles of LLP life, so the money arrives in one lump at redelivery instead of monthly.

Step 5 — what the lessor saw in cash: rent $16.4M + reserves retained (engine 2: $3.7M; engine 1 post-visit accrual from month 49-72: $150×250×24 = $0.9M PR and residual LLP) less reimbursement $1.8M. Net reserve retention ≈ $7.4M − $1.8M = $5.6M, which is the lessor's compensation for the maintenance life that walked out of the asset, to be spent (or forgone) when the lessor or the next lessee opens the engines.

Step 6 — return decomposition in percentage terms (ASSUMED, illustrative): if the aircraft's value at purchase were V and LRF 1.0%/month, rent yield = 12% of V per year. Suppose straight-line depreciation of 3.5% of V per year toward a residual, debt at 70% of V costing 6.5% (= 4.55% of V per year), and equity funding the rest. Net cash return before maintenance ≈ 12.0 − 3.5 − 4.55 = 3.95% of V on total capital, or on the 30% equity slice ≈ 13%; maintenance-reserve retention and end-of-life engine proceeds add to this; EOL shortfalls, downtime between leases and remarketing costs subtract. None of these percentages are market data; they show where the return comes from.

### 2.3 Engine leasing specifically

**Why airlines lease spare engines.** An airline needs more engines than it has engine positions on its aircraft because engines come off wing for scheduled shop visits (performance restoration, LLP replacement — see D1) and for unscheduled removals. The **spare ratio** — spare engines as a percentage of installed engines — is the planning parameter. MTU's AEROREPORT states airlines "used to have about 15% of spare engines of their installed engines, but this figure is now down to 10% and is expected to further decrease to about 7–8% for newer engine types" ([S36]); Acumen Aviation argues the 10% rule "is no longer sufficient because engines are coming off wing more often and taking longer to repair" ([S37]). A spare engine is a multi-million-dollar asset that earns nothing while it sits; airlines "are less inclined to keep as many owned spare engines as they used to, mainly because of the significant investment involved in assets that generate very little return" ([S36]). Leasing converts that lumpy capital into a monthly cost and, in a pool, lets one spare serve several operators.

**Shop-visit cover.** A CFM56 performance-restoration shop visit takes an engine out of service for months (D2 covers turnaround times and the MRO backlog). During that window the airline needs a replacement engine on wing; this is the demand for **short-term engine leases**, "a period of a few months to a maximum of three years ... ideal if a replacement engine is required for the duration of a shop visit" ([S36]). When MRO slots are delayed "operators often turn to short-term or green-time engine leasing" ([S36]). A **green-time engine** is an engine with limited remaining life before its next shop visit, leased out to burn that remaining life rather than overhauled; its rent is lower and its value is close to the sum of its parts (see D3). FTAI's Maintenance, Repair and Exchange (MRE) proposition is a variant of shop-visit cover: rather than lease the airline a spare while its engine is in the shop, FTAI exchanges the engine or module for a serviceable one (D5).

**Lease-rate levels.** The sourced data points are in Table 4.4. Note the large gap between IBA's ~$100,000/month CFM56-7B rate (2024) and Safe Fly Aviation's 2026 range of $42,000–$48,000/month (Tension T4); Safe Fly also quotes "green-time values" of $2.6–3.2M for the CFM56-5B and $2.8–3.4M for the CFM56-7B, which — if the rates are for green-time engines — would explain the lower rents, but the source does not say so and is not a primary source. IBA reported in April 2024 that "due to smaller supply and higher demand, V2500-A5 lease rates are slightly higher than the CFM56-5B" ([S20]), that the CFM56-7B saw the largest market-value gain, "around 20% from 2023 to 2024" ([S20]), and in its H1 2026 update that "values for widely used narrowbody engines, including the CFM56-5B and CFM56-7B, have levelled off after approximately 18 months of increases" with "early signs of stabilisation in parts of the narrowbody segment" ([S23]).

**Engine value and maintenance status.** For an engine, the maintenance adjustment dominates: the same CFM56-7B serial number is worth very different amounts fresh from a shop visit with new LLPs versus near run-out. D3 covers the "engine as a sum of modules" view and part-out values; D1 covers LLP limits. The leasing consequence is that an engine lessor's return has three legs — rent, reserves, and the decision at each lease end whether to overhaul (and lease again at full-life rent), lease green-time, or part out.

### 2.4 Mid-life narrowbody economics

**Definitions.** A **mid-life** narrowbody is roughly 10–18 years old: a 737NG (737-700/-800/-900ER, built from the late 1990s to about 2019, powered only by the CFM56-7B) or an A320ceo family aircraft (A319/A320/A321 "current engine option", powered by the CFM56-5B or the IAE V2500). These fleets are being replaced by the 737 MAX and A320neo, so their values and lease rates are governed by (i) how long airlines keep them, which depends on new-aircraft delivery rates and new-engine reliability (D9), and (ii) the value of their engines.

**Values and lease rates 2023–2026 (sourced points, see Table 4.4).** IBA's view in early 2024 was that "values and leases would continue to soar throughout the year, attributed to tight supply driven by lease extensions, engine reliability issues, and a lack of new aircraft deliveries" ([S29] as summarised in search; [S26]). By July 2025 IBA reported 12-year-old 737-800 rents down ~11% to ~$228,000/month and A320-200 rents down ~13% to ~$220,000/month, with some 21-year-old 737-800s "less than $160,000 per month" and rates "comfortably sub-$200k" at the older end ([S26],[S28]). IBA expected "greater availability in the secondary market and softening operator demand" to keep pressing narrowbody lease rates down, while "strong demand for engines and component scarcity should support base aircraft values despite the weaker leasing environment" ([S26]). By September 2026 IBA was warning of "oversupply of narrowbody conversions and lease rate fall" ([S26] headline). Half-life market values for a 12-year-old 737-800 or A320ceo were not retrieved this session (Unknown U9).

**Why mid-life aircraft are bought on lease.** A buyer of a 12-year-old aircraft almost always buys it with a lease attached, either (i) in a **sale-leaseback**, where the operating airline sells its owned aircraft to the lessor and leases it straight back (the WestJet deal: "17 aircraft on lease to WestJet in a sale-leaseback", [S11]), or (ii) by **lease-attached trading**, buying it from another lessor with the existing lease transferred. The lease is what makes the asset financeable: lenders and ABS investors underwrite contracted rent from a known airline, and the lessor's return over the remaining term is (a) in Section 2.1. At the end of that term the buyer has a choice: re-lease, convert to freighter, or part out — and the value of that choice is mostly the engines.

**How the engines dominate a mid-life narrowbody's value.** Two sourced lease rates make the point without needing appraisal values: a CFM56-7B spare engine rented for ~$100,000/month in 2024 (IBA, [S20]), so two engines on standalone leases would command ~$200,000/month, against ~$228,000/month for a complete 12-year-old 737-800 in July 2025 (IBA, [S26]). On those figures the airframe, landing gear, APU and everything else together earn roughly $28,000/month, about 12% of the aircraft's rent, and the engines about 88%. (Caveat: the two figures are a year apart and from different IBA updates; engine rents may have moved by mid-2025 — Tension T5.) The same logic in values: Safe Fly's 2026 green-time range of $2.8–3.4M per CFM56-7B ([S24]) is a floor for engines with little life left; a full-life CFM56-7B is worth substantially more (D3 has part-out and full-life values), so a pair of fresh engines can account for most of a 15-year-old 737-800's trading price. This is why FTAI states it "owns and leases jet aircraft which often facilitates the acquisition of engines at attractive prices" (Q2 2026 release, [S4]), and why the SCI vehicles buy aircraft and FTAI does the engine work (D7).

**Freighter conversion as an end-of-life path.** A passenger 737-800 at 18–25 years can be converted to a freighter (**P2F**, passenger-to-freighter) under a **Supplemental Type Certificate (STC)**, a regulator-approved modification design owned by a conversion house: a main-deck cargo door, strengthened floor, 9g rigid barrier, cargo loading system. Conversion costs several million dollars (not retrieved this session, Unknown U10) and extends the airframe's revenue life by 10–15 years at low cycles per year, which is why cargo operators want engines "customized for cargo" — lower-cycle, lower-cost workscopes. On 7 July 2026 FTAI and AEI (Aeronautical Engineers Inc.) announced a collaboration to deliver "a more cost-effective Boeing 737-800 freighter solution": FTAI "can build and maintain lower cycle engines customized for cargo, enabling FTAI and AEI to deliver aircraft at a significantly lower operating cost, while extending the CFM56 engine's lifecycle across passenger, cargo and power applications"; AEI has "625+ aircraft modified using AEI's STCs" over 60-plus years, and the release notes "almost 6,000" 737-800s delivered ([S12]). The counter-signal is IBA's September 2026 warning of "oversupply of narrowbody conversions" ([S26]); an earlier IBA note reported freighter values rising while narrowbody passenger lease rates receded ([S28]). Record both.

### 2.5 Financing: ABS and warehouse facilities

**Asset-backed securitization (ABS).** A lessor sells a portfolio of leased aircraft or engines to a bankruptcy-remote **special-purpose vehicle (SPV)** — a company that exists only to own those assets — which issues notes to investors secured on the assets and their lease cash flows. The lessor usually keeps the equity (the residual claim) and acts as **servicer**, managing the leases for a fee. The notes are **tranched**: the **senior** (Class/Series A) notes are paid first, carry the lowest coupon and the highest rating; the **mezzanine** (Class B, and sometimes C) notes are paid after A and carry higher coupons and lower ratings; the **equity** (E-certificates) is paid last and absorbs first losses. **Loan-to-value (LTV)** is the note balance divided by the appraised value of the assets — the A notes might be sized to ~60–70% of appraised value, A+B to ~75–80%, so the equity is ~20–25% (these ranges are ASSUMED (illustrative); the deals retrieved this session did not return LTVs, Unknown U6). Each payment date, collections go down a **waterfall**: fees and expenses, then A interest, then B interest, then scheduled A and B principal, then (if issued) C, with any surplus to the equity. Notes have an **anticipated repayment date (ARD)**, after which excess cash is swept to pay principal faster and the coupon steps up, and a much later **legal final maturity**. Rating agencies (KBRA, Moody's, S&P, Fitch) test the structure against stressed assumptions for lease-rate declines, downtime, maintenance costs and residuals.

**Sourced template — Willis Engine Structured Trust VIII and IX.** WEST VIII (preliminary ratings 3 Jun 2025): Series A notes rated A and Series B notes rated BBB by KBRA; the ninth aviation ABS sponsored and serviced by WLFC; proceeds "to refinance the existing WEST IV transaction and acquire a portfolio of 64 assets"; total $596M per Asset Securitization Report ([S16],[S18]). WEST IX (preliminary ratings 10 Dec 2025): $392.9M financing leases on 49 aircraft assets; Series A rated A; "two tranches of class A and B notes, both of which have an anticipated repayment date of December 2031 and a legal final maturity date of December 2050"; "a senior-subordinate repayment structure, and if a series of C notes is issued, it will receive payments subordinate to payments to the series A and B" ([S17],[S19]). Note the ~19-year gap between ARD and legal final: the structure is designed to be refinanced or called at the ARD, with the legal final as a backstop. Coupons and LTVs for WEST VIII/IX were not in the retrieved text (Unknown U6).

**Illustrative tranching arithmetic (ASSUMED, illustrative — not WEST data).** Portfolio appraised value $500M of engines on lease. Class A $325M (65% LTV) at 5.5%; Class B $50M (cumulative 75% LTV) at 7.5%; Class C $25M (80%) at 10%; equity $100M (20%). Annual interest: A $17.9M + B $3.75M + C $2.5M = $24.1M. If the portfolio earns an LRF of 1.0%/month, gross rent = $60M/year; after $24.1M interest, say $8M of servicing, insurance, remarketing and downtime, and $15M of scheduled principal, about $13M reaches the equity — a 13% cash yield on $100M before maintenance-reserve retention and asset-sale proceeds. If lease rates fall 15%, rent drops to $51M and the equity's cash falls to ~$4M: the tranching concentrates both upside and downside in the equity, which is why the lessor keeps it and why rating agencies stress the A/B notes to lease-rate and value declines.

**Warehouse facility.** A revolving bank loan to an SPV, secured on whatever assets the SPV buys during an **availability period**, with an advance rate (a percentage of each asset's value the banks will lend), a borrowing base recomputed as assets are added, and a term after which the balance must be repaid or refinanced — commonly by issuing an ABS, which is why it is called a warehouse: assets are accumulated in it until there are enough to securitize. Lessors use warehouses to fund acquisitions one aircraft at a time without going to the bond market for each. FTAI's 2026 SPV closed a $2.0B warehouse facility from 13 lenders with an accordion to $3.0B on 14 Aug 2026 (edgar-index; chain map) — the vehicle itself belongs to D7; the instrument is the one just described.

**How lessors use them together.** Buy on the warehouse → season the leases → securitize into an ABS, releasing warehouse capacity → keep the equity and the servicing fee. The 2025 SCI vehicle followed the same shape ($2.5B asset-level debt commitment Feb 2025, $2.0B equity Oct 2025; D7). The lessor's incentive to sell assets into such vehicles (as FTAI did with the Seed Assets, Section 2.6) is to recycle equity: the lessor books a gain on sale, keeps a management/servicing stream and, in FTAI's case, keeps the engine maintenance work.

### 2.6 FTAI's Aviation Leasing segment

**What it is.** The FY2025 10-K describes the segment as owning and managing aviation assets — commercial aircraft and engines — and leasing and selling them, directly and through an equity-method investment ([S1]; chain map). FTAI "owns and maintains commercial jet engines with a focus on CFM56 and V2500 engines" and "also owns and leases jet aircraft which often facilitates the acquisition of engines at attractive prices" ([S4]). Revenue lines in the segment are lease income, maintenance revenue (the recognition of maintenance reserves and EOL compensation), asset sales revenue (sales of aircraft and engines, with cost of sales), and other revenue; the segment also records gains on sale of leasing equipment and the equity pick-up from its unconsolidated investment. Segment Adjusted EBITDA adds back depreciation and includes gains and the equity-method pick-up (D10 holds the non-GAAP definitions).

**Fleet.** 31 Dec 2025: 290 assets — 47 aircraft and 243 engines — including 8 aircraft and 17 engines in Russia; 37 aircraft and 143 engines on lease ([S1]). Arithmetic: by count, aircraft on lease are 37 of 47 (79%), or 37 of the 39 outside Russia (95%); engines on lease are 143 of 243 (59%), or 143 of the 226 outside Russia (63%). The 10-K's own utilization metric is different: ~77% for Q4 2025, "based on the percent of days on-lease in the quarter weighted by the monthly average equity value of aviation leasing equipment, excluding airframes" ([S1]) — i.e., an engine-value-weighted figure. Comparable disclosed readings: ~79% for the nine months ended 30 Sep 2024 ([S10]) and ~77% for Q4 2023 ([S8] as returned). Fleet counts at 31 Dec 2021–2024 and 30 Jun 2026 were not retrieved (Unknown U1). At 31 Dec 2022 the Russia/Ukraine exposure was 4 aircraft and 1 engine in Ukraine plus 8 aircraft and 17 engines in Russia ([S7]).

**Lease terms.** Weighted-average remaining lease term 44 months (aircraft) and 38 months (engines on lease) at 31 Dec 2025 ([S1]).

**Lease income.** FY2021 $173.864M; FY2022 $179.314M, +$5.450M, despite the termination in 2022 of Russian leases that had produced "approximately $39.8 million" of basic lease revenue in 2021 ([S7]). Q1 2025 $68.440M → Q1 2026 $39.892M (−$28.5M, "primarily due to decreases in aircraft lease revenue of $24.9 million, driven by the sale of Seed Assets to the 2025 Partnership", [S2]). Q2 2025 $62.439M → Q2 2026 $27.765M ([S4],[S5]). 1H 2025 $130.879M → 1H 2026 $67.657M (−48%, arithmetic). FY2023, FY2024 and FY2025 annual lease income were not retrieved (Unknown U2); the FY2025 10-K and the Q4/FY2025 release ([S6]) contain them.

**Asset sales and gains.** FY2025 gain on sale to the 2025 Partnership $46.380M ([S1]). Q1 2026 asset sales revenue fell $8.8M y/y "primarily due to an overall decrease in the number of sales transactions" ([S2]). Annual asset-sales revenue and gains for 2021–2025 not retrieved (Unknown U2).

**Impairments.** None (transactional) in 2025; $1.0M, net of redelivery compensation, in 2024 ([S1]). Russia write-off 2022: $120.0M net of maintenance deposits ([S7]).

**Balance sheet.** Leasing equipment at cost $2,963.452M → $2,057.624M; accumulated depreciation $589.722M → $511.820M; net $2,373.730M → $1,545.804M (31 Dec 2024 → 31 Dec 2025, [S1]). The $905.8M (−31%) fall in gross cost is the footprint of the Seed Asset sales into the 2025 Partnership plus ordinary sales, net of purchases; accumulated depreciation fell because the sold assets took their depreciation with them.

**Segment Adjusted EBITDA.** Guidance: 2026 Business Segment Adjusted EBITDA raised from $1.525B to $1.625B in the FY2025 release (25 Feb 2026), "comprised of $1.05 billion from Aerospace Products and $575 million from Aviation Leasing" ([S6]). An earlier guidance step (quoted in the Q1 2026 10-Q search return) had 2026 segment Adjusted EBITDA "from $1.4 billion to $1.525 billion ... approximately $1.0 billion from Aerospace Products and $525 million from Aviation Leasing" ([S2]). One reading of the Q2 2026 release says the company "updated 2026 Aviation Leasing Adjusted EBITDA guidance from $575 million to $475 million, reflecting a continued shift to an asset-light business model" ([S5]); another reading of the same release returned $1.625B/$575M ([S4]) — Tension T1. Reported quarterly segment Adjusted EBITDA: the chain map records Q2 2026 Aviation Leasing Adjusted EBITDA of $88.2M; this session's searches did not return that line (Unknown U3). Consistency check (arithmetic): consolidated Q2 2026 Adjusted EBITDA $291.444M ([S4]); Aerospace Products $249.7M ([S4]); if Aviation Leasing were $88.2M the two segments would sum to $337.9M, implying Corporate and Other of about −$46.5M, which is a plausible sign and magnitude for corporate costs plus FTAI Power start-up but is not confirmed. Annual segment Adjusted EBITDA for 2021–2025: not retrieved (Unknown U2). A search return stated "Adjusted EBITDA increased by $220.6 million" for FY2025 without identifying the level (consolidated or segment) — recorded as ambiguous.

**Relationship between lease income and segment EBITDA.** Even on the higher guidance, 2026 Aviation Leasing Adjusted EBITDA of $475–575M against 1H 2026 lease income of $67.7M (annualizing to ~$135M) means most of the segment's Adjusted EBITDA must come from lines other than rent: gains and margins on asset sales (including sales into the Strategic Capital vehicles), maintenance revenue, and the equity-method pick-up. The writer should source the composition from the FY2025 10-K segment note (Unknown U2).

**Russia.** Timeline from filings: 2021 — Russian lessees generated ~$39.8M of basic lease revenue ([S7]). 2022 — sanctions after the invasion of Ukraine; FTAI "terminated all lease agreements with Russian airlines"; $120.0M impairment "net of maintenance deposits, to write-off the entire carrying value of leasing equipment assets that the company did not expect to recover from Ukraine and Russia"; at 31 Dec 2022, 4 aircraft and 1 engine in Ukraine and 8 aircraft and 17 engines in Russia ([S7]). The "net of maintenance deposits" phrase means the write-off was reduced by the maintenance reserves and security deposits FTAI already held from those lessees, which it kept. 2025 — $54.3M of insurance recoveries for the nine months ended 30 Sep 2025 ([S9]). FY2025 10-K — 8 aircraft and 17 engines "still located in Russia"; "the insured value of the aircraft and engines that remain in Russia is $210.7 million"; lessees must insure the leased assets with FTAI named as insured for total loss, and FTAI buys contingent cover for off-lease periods or where a lessee's policy fails to indemnify ([S1]). Q1 2026 — $44.6M "in insurance recoveries in connection with the settlement of claims related to the aircraft and engines located in Russia" ([S2]). Recoveries in 2023 and 2024, the status of the Ukraine assets, and whether the $210.7M insured value is before or after the recoveries were not retrieved (Unknown U4). Arithmetic: recoveries disclosed so far ($54.3M + $44.6M = $98.9M) are 82% of the $120.0M net write-off and 47% of the $210.7M insured value; the 2022 write-off was net of deposits, so recoveries plus deposits retained versus gross carrying value cannot be computed from what was retrieved.

**Equity-method investment.** The segment description says it leases "directly and through an equity-method investment" (chain map, [S1]); the counterparty, FTAI's ownership percentage, the assets inside it and the pick-up by year were not returned (Unknown U11). Note that the 2025 Partnership (SCI) is itself a vehicle in which FTAI holds an interest — D7 should establish whether that interest is the equity-method investment inside this segment or sits elsewhere.

**Movement of assets to the Strategic Capital vehicles.** The 10-Qs attribute the fall in aircraft lease revenue to "the sale of Seed Assets to the 2025 Partnership" ([S2]) — Seed Assets being the on-lease aircraft FTAI contributed or sold from its own book to start the 2025 vehicle. Effects visible in the filings: gross leasing equipment −$906M in 2025; lease income −42% (Q1) and −56% (Q2) y/y in 1H 2026; a $46.4M gain on sale to the 2025 Partnership in FY2025; and the shift in guidance language to "asset-light" ([S1],[S2],[S5]). The number and type of Seed Assets, their sale price and the date(s) of transfer were not retrieved (Unknown U12). WestJet shows the forward pattern: on-lease aircraft go to the SPV (17 aircraft), off-lease aircraft go to FTAI for engines (10 aircraft) ([S11]).

**WestJet 27 × 737-700 (28 Sep 2026).** "FTAI's 2026 SPV acquiring 17 aircraft on lease to WestJet in a sale-leaseback, and FTAI acquiring 10 off-lease aircraft"; "one of FTAI's largest aircraft transactions to date"; the 10 off-lease aircraft "will support FTAI's Aerospace Products business by expanding the Company's supply of CFM56-7B engines and modules available to its Maintenance, Repair and Exchange customers"; the 2026 SPV "was formed to acquire on-lease, mid-life 737NG and A320ceo aircraft and follows the 2025 SPV ... which raised $2.0 billion of equity commitments and has committed approximately $6.0 billion of total capital across more than 300 aircraft" ([S11]). Purchase price, lease term and rent on the 17 leased-back aircraft, and which FTAI entity (the Leasing segment or Aerospace Products inventory) holds the 10 off-lease aircraft: not disclosed in the release (Unknown U13). A 737-700 carries two CFM56-7B engines, so 10 off-lease aircraft are 20 engines (arithmetic).

### 2.7 Worked example: FTAI's implied leasing yield

Definition used: gross leasing yield = lease income for the period ÷ average leasing equipment at cost over the period. "At cost" removes the effect of depreciation policy; a net-book-value yield is also shown.

Balance-sheet inputs (FY2025 10-K, [S1]): leasing equipment at cost $2,963.452M (31 Dec 2024) and $2,057.624M (31 Dec 2025); net $2,373.730M and $1,545.804M.

Average 2025 cost base = ($2,963.452M + $2,057.624M) ÷ 2 = $2,510.538M. Average 2025 net base = ($2,373.730M + $1,545.804M) ÷ 2 = $1,959.767M.

Income input: FY2025 lease income was not retrieved (Unknown U2), so two bounded calculations are shown and the writer should substitute the 10-K figure.

(a) Using 1H 2025 lease income annualized: ($68.440M + $62.439M) × 2 = $261.758M. Gross yield = $261.758M ÷ $2,510.538M = 10.4% on cost; $261.758M ÷ $1,959.767M = 13.4% on net book value. This overstates FY2025 because 2H 2025 rent fell after the Seed Asset sales (Q1 2026 was already down 42% y/y).

(b) Using 1H 2026 lease income against the 31 Dec 2025 base (no 30 Jun 2026 balance sheet retrieved): ($39.892M + $27.765M) × 2 = $135.314M. Gross yield = $135.314M ÷ $2,057.624M = 6.6% on cost; ÷ $1,545.804M = 8.8% on net. This understates the yield if the cost base kept falling in 1H 2026, which the guidance language implies.

Interpretation of the spread: the on-cost yield is depressed by (i) the Russia assets, which sit in the asset count at zero net book value but may still sit in gross cost (unclear — Unknown U4), (ii) off-lease engines (utilization 77%), and (iii) aircraft purchased for their engines and parked or in work rather than leased. A simple lease-rate-factor cross-check: 10.4% per year on cost is an LRF of 0.87%/month on cost; 13.4% on net is 1.1%/month on net — in the range one would expect for a mixed mid-life aircraft and engine book, though no external LRF benchmark was retrieved (Unknown U5). The equity-value-weighted utilization suggests the yield on assets actually on lease is roughly 1/0.77 ≈ 1.3× the portfolio figure.

---

## 3. Market structure and players

**Aircraft lessors with large narrowbody books (context for the mid-life market).** AerCap (NYSE: AER) — the largest aircraft lessor; also runs an engine leasing business (the former GECAS engine portfolio came with the 2021 GECAS acquisition); its 20-F is the source for the maintenance-reserve and EOL-compensation language above ([S31],[S32]). Air Lease (NYSE: AL), SMBC Aviation Capital, Avolon, BOC Aviation, and the mid-life specialists (Castlelake, Carlyle Aviation Partners, Aergo, etc.) trade the 737NG/A320ceo assets FTAI and the SCI vehicles buy. Scale metrics for these belong to D11.

**Engine lessors.**
- **Willis Lease Finance Corporation (NASDAQ: WLFC).** The listed pure-play. Lease portfolio $2,888.5M at 30 Sep 2025 ($2,700.4M equipment held in operating lease portfolio, $144.8M notes receivable, $27.0M maintenance rights, $16.3M investments in sales-type leases); $3,302.6M including assets in joint ventures; utilization 86.0% at 30 Sep 2025 vs 82.9% a year earlier; Q3 2025 lease rent revenue $76.6M (+17.9% y/y, a record) and maintenance reserve revenue $76.1M (+52.8%, a record) ([S14],[S15]). Funds itself through the WEST ABS series (nine aviation ABS to WEST VIII, ten to WEST IX, [S16],[S17]). FY2025 10-K located ([S13]) but engine count, lease-rate factor and FY2025 totals not returned (Unknown U5).
- **GE Engine Leasing** (GE Aerospace, NYSE: GE). The OEM's captive; a 2019 trade report noted GE Engine Leasing "has seen an explosion of financing based on spare engines" ([S38]). Engine leasing is "a key part of full-service package deals from General Electric, Pratt & Whitney and Rolls-Royce" ([S38]).
- **SMBC Aero Engine Lease** (Sumitomo Mitsui / SMBC Aviation Capital group) — engine lessor affiliated with the aircraft lessor; scale not retrieved.
- **Engine Lease Finance (ELF)** (Mitsubishi HC Capital) — Shannon-based engine lessor; scale not retrieved.
- **AerCap Engines** (AerCap) — the engine business built on the former GECAS engine portfolio; scale not retrieved.
- **Rolls-Royce & Partners Finance (RRPF)** — joint venture of Rolls-Royce and GATX; Rolls-Royce engines plus some others; a 2019 report attributes the market's expansion to "airlines becoming more open to spare engine leasing, driven by lower lease rentals in an increasingly competitive market" ([S38]).
- **MTU Maintenance Lease Services** — the MRO's leasing arm: "short-term leasing, stand-by arrangements, engine pooling, as well as asset management" ([S36],[S38]).
- **FTAI Aviation** — 243 engines at 31 Dec 2025 ([S1]), making it one of the larger independent CFM56/V2500 engine owners by count.
- Scale of the group: a 2019 trade estimate had "the top five engine leasing companies ... over 1,000 powerplants with a book value in excess of $5 billion" ([S38]) — dated; current figures not retrieved (Unknown U14).

**Conversion houses (end-of-life path).** AEI — "625+ aircraft modified using AEI's STCs", FTAI's partner ([S12]). Boeing Converted Freighter (BCF) programme — Boeing's own 737-800BCF (a Boeing/GECAS announcement for 35 737-800BCFs surfaced in search, [S44]; date not verified this session). Also IAI/Bedek (737-800BDSF), not sourced this session.

**Appraisers and data providers.** IBA, mba, Cirium (Ascend) publish the half-life values and lease rates the market trades on; IBA is the source for most rate points here.

---

## 4. Numbers

### 4.1 FTAI Aviation Leasing — fleet and operating metrics

| Metric | Value | As of | Source |
|---|---|---|---|
| Assets owned/managed | 290 (47 aircraft, 243 engines) | 31 Dec 2025 | FY2025 10-K [S1] |
| Of which in Russia | 8 aircraft, 17 engines | 31 Dec 2025 | FY2025 10-K [S1] |
| On lease | 37 aircraft, 143 engines | 31 Dec 2025 | FY2025 10-K [S1] |
| Utilization (days on lease, equity-value weighted, ex-airframes) | ~77% | Q4 2025 | FY2025 10-K [S1] |
| Utilization | ~79% | 9M 2024 | 10-Q Q3 2024 [S10] |
| Utilization | ~77% | Q4 2023 | FY2023 10-K [S8] (as returned) |
| Weighted-avg remaining lease term, aircraft | 44 months | 31 Dec 2025 | FY2025 10-K [S1] |
| Avg remaining lease term, engines on lease | 38 months | 31 Dec 2025 | FY2025 10-K [S1] |
| Assets in Ukraine / Russia | 4 aircraft + 1 engine / 8 aircraft + 17 engines | 31 Dec 2022 | FY2022 10-K [S7] |

### 4.2 FTAI Aviation Leasing — income statement lines retrieved

| Line | Period | $ thousands | Source |
|---|---|---|---|
| Lease income | FY2021 | 173,864 | FY2022 10-K [S7] |
| Lease income | FY2022 | 179,314 | FY2022 10-K [S7] |
| Basic lease revenue from Russian lessees | FY2021 | ~39,800 | FY2022 10-K [S7] |
| Lease income | Q1 2025 | 68,440 | 10-Q Q1 2026 [S2] |
| Lease income | Q1 2026 | 39,892 | 10-Q Q1 2026 [S2] |
| Lease income | Q2 2025 | 62,439 | Q2 2026 release [S4],[S5] |
| Lease income | Q2 2026 | 27,765 | Q2 2026 release [S4],[S5] |
| Lease income (arithmetic) | 1H 2025 / 1H 2026 | 130,879 / 67,657 | derived |
| Decrease in aircraft lease revenue, Q1 2026 vs Q1 2025 | Q1 2026 | (24,900) "driven by the sale of Seed Assets to the 2025 Partnership" | 10-Q Q1 2026 [S2] |
| Decrease in asset sales revenue y/y | Q1 2026 | (8,800) | 10-Q Q1 2026 [S2] |
| Gain on sale to 2025 Partnership | FY2025 | 46,380 | FY2025 10-K [S1] |
| Transactional impairment | FY2025 / FY2024 | 0 / 1,000 (net of redelivery compensation) | FY2025 10-K [S1] |
| Russia/Ukraine impairment, net of maintenance deposits | FY2022 | 120,000 | FY2022 10-K [S7] |
| Insurance recoveries (Russia) | 9M 2025 | 54,300 | 10-Q Q3 2025 [S9] |
| Insurance recoveries (Russia) | Q1 2026 | 44,600 | 10-Q Q1 2026 [S2] |
| Insured value of assets remaining in Russia | FY2025 10-K | 210,700 | FY2025 10-K [S1] |
| Consolidated Adjusted EBITDA | Q2 2026 | 291,444 | Q2 2026 release [S4] |
| Aerospace Products Adjusted EBITDA | Q2 2026 | 249,700 | Q2 2026 release [S4] |
| Aviation Leasing Adjusted EBITDA | Q2 2026 | 88,200 (chain map; not confirmed this session) | chain-map.md |
| "Adjusted EBITDA increased by $220.6 million" (level not identified) | FY2025 | 220,600 | FY2025 10-K [S1] |

### 4.3 FTAI Aviation Leasing — balance sheet and guidance

| Item | 31 Dec 2024 | 31 Dec 2025 | Source |
|---|---|---|---|
| Leasing equipment, at cost ($K) | 2,963,452 | 2,057,624 | FY2025 10-K [S1] |
| Accumulated depreciation ($K) | 589,722 | 511,820 | FY2025 10-K [S1] |
| Leasing equipment, net ($K) | 2,373,730 | 1,545,804 | FY2025 10-K [S1] |

| Guidance item | Figure | Date | Source |
|---|---|---|---|
| 2026 Business Segment Adj. EBITDA | $1.4B → $1.525B (~$1.0B AP, $525M AL) | step quoted in Q1 2026 10-Q return | [S2] |
| 2026 Business Segment Adj. EBITDA | $1.525B → $1.625B ($1.05B AP, $575M AL) | 25 Feb 2026 | FY2025 release [S6] |
| 2026 Aviation Leasing Adj. EBITDA | $575M → $475M ("asset-light") | 29 Jul 2026 (one reading) | Q2 2026 release [S5] |
| 2026 Business Segment Adj. EBITDA | $1.625B ($1.05B AP, $575M AL) | 29 Jul 2026 (other reading) | Q2 2026 release [S4] |

### 4.4 Market lease rates and values

| Asset | Metric | Figure | Date | Source |
|---|---|---|---|---|
| 737-800, 12 years old | monthly lease rate | ~$228,000 (−11% y/y) | Jul 2025 | IBA via [S26],[S28] |
| A320-200, comparable age | monthly lease rate | ~$220,000 (−13% y/y) | Jul 2025 | IBA via [S26],[S28] |
| 737-800, 21 years old | monthly lease rate | < $160,000; older end "comfortably sub-$200k" | Jul 2025 | IBA via [S26] |
| CFM56-7B spare engine | monthly lease rate | ~$75,000 (2019) → ~$100,000 (2024) | Apr 2024 | IBA via [S20],[S21] |
| CFM56-7B | market value change | ~+20%, 2023→2024 | Apr 2024 | IBA via [S20] |
| V2500-A5 vs CFM56-5B | lease rates | V2500-A5 "slightly higher" | Apr 2024 | IBA via [S20] |
| CFM56-5B / -7B | values | "levelled off after approximately 18 months of increases" | H1 2026 | IBA via [S23] |
| CFM56-7B | monthly lease rate | $42,000–$48,000 | 2026 | Safe Fly Aviation [S24] (non-primary) |
| CFM56-5B | monthly lease rate | $38,000–$44,000 | 2026 | Safe Fly Aviation [S24] (non-primary) |
| CFM56-5B | "green-time value" | $2.6M–$3.2M | 2026 | Safe Fly Aviation [S24] |
| CFM56-7B | "green-time value" | $2.8M–$3.4M | 2026 | Safe Fly Aviation [S24] |
| Narrowbody conversions | market signal | IBA "warns of oversupply of narrowbody conversions and lease rate fall" | 6 Sep 2026 | [S26] |
| Spare-engine ratio | % of installed engines | ~15% historically → ~10% → 7–8% expected for new types | undated (MTU) | [S36] |
| Short-term engine lease | duration | "a few months to a maximum of three years" | undated (MTU) | [S36] |
| Top-five engine lessors | fleet / book value | >1,000 engines, >$5B | Jul 2019 | AviTrader [S38] |

### 4.5 Willis Lease Finance (WLFC)

| Metric | Figure | As of | Source |
|---|---|---|---|
| Portfolio utilization | 86.0% (vs 82.9% prior year) | 30 Sep 2025 | Q3 2025 release [S14] |
| Lease portfolio | $2,888.5M | 30 Sep 2025 | [S14],[S15] |
| — equipment held in operating lease portfolio | $2,700.4M | 30 Sep 2025 | [S14] |
| — notes receivable | $144.8M | 30 Sep 2025 | [S14] |
| — maintenance rights | $27.0M | 30 Sep 2025 | [S14] |
| — investments in sales-type leases | $16.3M | 30 Sep 2025 | [S14] |
| Lease assets incl. JVs | $3,302.6M | 30 Sep 2025 | [S14] |
| Lease rent revenue | $76.6M (+17.9% y/y, record) | Q3 2025 | [S14] |
| Maintenance reserve revenue | $76.1M (+52.8% y/y, record) | Q3 2025 | [S14] |
| FY2025 10-K | located, figures not returned | FY2025 | [S13] |

### 4.6 Engine ABS

| Deal | Size | Assets | Tranches / ratings | Dates | Source |
|---|---|---|---|---|---|
| WEST VIII | $596M | 64 assets; refinances WEST IV | Series A rated A; Series B rated BBB (KBRA prelim.) | prelim. 3 Jun 2025 | [S16],[S18] |
| WEST IX | $392.9M | 49 aircraft assets | Class A rated A; Class B; optional subordinate C | prelim. 10 Dec 2025; ARD Dec 2031; legal final Dec 2050 | [S17],[S19] |
| FTAI 2026 SPV warehouse | $2.0B, accordion to $3.0B, 13 lenders | mid-life 737NG/A320ceo | warehouse (bank) | closed 14 Aug 2026 | edgar-index / D7 |

### 4.7 WestJet and AEI transactions

| Item | Detail | Source |
|---|---|---|
| WestJet, 28 Sep 2026 | 27 × 737-700: 17 on sale-leaseback to WestJet into FTAI's 2026 SPV; 10 off-lease bought by FTAI for CFM56-7B engines/modules for MRE customers; price and lease terms not disclosed | [S11] |
| 2025 SPV scale (as restated in WestJet release) | $2.0B equity commitments; ~$6.0B total capital across 300+ aircraft | [S11] |
| AEI collaboration, 7 Jul 2026 | 737-800 freighter solution: FTAI lower-cycle cargo-customized engines + AEI conversion STCs; AEI 625+ conversions; ~6,000 737-800s delivered | [S12] |

---

## 5. Constraints and bottlenecks

- **Supply of mid-life assets.** Mid-life 737NG/A320ceo aircraft reach the market through airline fleet renewals, lessor portfolio sales and sale-leasebacks; new-aircraft delivery shortfalls (D9) keep airlines flying them longer, which supports values but reduces the flow of off-lease aircraft available to buy for engines. IBA's 2025–26 commentary describes "greater availability in the secondary market and softening operator demand" pressing lease rates while "strong demand for engines and component scarcity" supports base values ([S26]) — the two forces pull a mid-life lessor's rent and its engine-exit value in opposite directions.
- **Engine shop capacity.** Long shop-visit turnaround times (D2) raise demand for short-term spare-engine leases and green-time engines ([S36]) and push utilization up at engine lessors (WLFC 86.0%, [S14]); the same backlog slows the lessor's own re-marketing of off-lease engines that need a shop visit before they can be leased again.
- **Maintenance condition as a gate.** An engine cannot be leased (or sold at full-life value) without the shop visit and LLP replacement that its records require; the lessor's capital is tied up in the engine during the visit; reserves collected may fall short of the cost (Section 2.2 step 3).
- **Capital.** Lease yields of roughly 10–13% on cost/net (Section 2.7) leave limited spread over debt costs for a leveraged lessor; ABS execution depends on ratings, which depend on lease-rate and value stress tests; rate cuts that "level off" engine values ([S23]) and narrowbody lease-rate declines of 11–13% ([S26]) feed straight into those tests. For FTAI, the move to an asset-light model shifts the capital constraint to the third-party vehicles (D7).
- **Jurisdiction and insurance.** The Russia episode shows that assets leased into jurisdictions that stop honouring repossession become uninsured-until-settled receivables: $120.0M written off in 2022, $98.9M recovered by Q1 2026, against $210.7M of insured value ([S1],[S2],[S7],[S9]).
- **Return conditions and documentation.** Redelivery disputes over records, LLP traceability and borescope findings delay an asset's next lease; a mid-life narrowbody with incomplete back-to-birth LLP records is worth materially less (D3).
- **Conversion-slot and feedstock balance.** Freighter conversion houses have finite line capacity and the market can oversupply: IBA's September 2026 warning ([S26]) versus FTAI–AEI's expansion ([S12]).

---

## 6. Tensions

- **T1 — 2026 Aviation Leasing Adjusted EBITDA guidance.** One reading of the 29 Jul 2026 release: "updated 2026 Aviation Leasing Adjusted EBITDA guidance from $575 million to $475 million, reflecting a continued shift to an asset-light business model" ([S5]). Another reading of the same release (8-K exhibit) returned "$1.625 billion, comprised of $1.05 billion from Aerospace Products and $575 million from Aviation Leasing" ([S4]). The 25 Feb 2026 release is unambiguous at $575M ([S6]). The release text itself must be read to resolve.
- **T2 — Guidance history.** The Q1 2026 10-Q return quotes a step "from $1.4 billion to $1.525 billion ... approximately $1.0 billion from Aerospace Products and $525 million from Aviation Leasing" ([S2]), while the Feb 2026 release quotes the next step as "$1.525 billion to $1.625 billion" with $575M for leasing ([S6]). Consistent as a sequence ($525M → $575M → $475M?) but the date of the $525M step was not returned.
- **T3 — Q2 2026 segment Adjusted EBITDA.** Chain map: Aviation Leasing Q2 2026 Adjusted EBITDA $88.2M. This session: the Q2 2026 release searches returned consolidated $291.444M and Aerospace Products $249.7M but no leasing segment line ([S4],[S5]). The implied Corporate and Other of about −$46.5M is plausible but unverified.
- **T4 — CFM56-7B lease rates.** IBA (Apr 2024): ~$100,000/month, up from ~$75,000 in 2019 ([S20],[S21]). Safe Fly Aviation (2026): $42,000–$48,000/month for the -7B and $38,000–$44,000 for the -5B ([S24]). The Safe Fly figures sit alongside "green-time values" and may describe green-time engines, but the source does not say so; it is a non-primary website. Both are recorded; neither is averaged.
- **T5 — Engines-dominate-value arithmetic.** The comparison of 2 × $100,000 (engine rent, 2024) with $228,000 (aircraft rent, mid-2025) mixes dates; IBA's H1 2026 update says engine values "levelled off", so 2025 engine rents may differ from the 2024 figure. The ratio (engines ≈ 88% of rent) is therefore indicative, not measured.
- **T6 — Utilization by count vs by value.** By count, 143 of 243 engines (59%) and 37 of 47 aircraft (79%) were on lease at 31 Dec 2025; the 10-K's equity-value-weighted, airframe-excluded utilization is ~77% ([S1]). The gap is consistent with the off-lease engines being low-value (run-out, in shop, or in Russia at zero book), but the 10-K definition should be quoted rather than the count ratio.
- **T7 — Freighter conversion demand.** FTAI–AEI (Jul 2026) build capacity for 737-800 freighters ([S12]); IBA (Sep 2026) warns of "oversupply of narrowbody conversions" ([S26]); an earlier IBA note had freighter values rising ([S28]).
- **T8 — Russia write-off versus insured value.** $120.0M net write-off (2022, net of maintenance deposits) versus $210.7M insured value (FY2025 10-K). The difference reflects deposits netted in 2022 and insured values above carrying value; the gross carrying value in 2022 and the deposits retained were not returned, so the reconciliation cannot be completed.

---

## 7. Unknowns

- **U1 — Fleet by year.** Aircraft and engine counts at 31 Dec 2021, 2022, 2023, 2024 and 30 Jun 2026. Resolve: "Our Aviation Leasing segment" paragraphs in each 10-K/10-Q ([S7],[S8],[S3]).
- **U2 — Annual segment lines 2023–2025.** Lease income, maintenance revenue, asset sales revenue and cost, gain on sale of leasing equipment, equity-method pick-up, and segment Adjusted EBITDA for FY2023, FY2024, FY2025 and each 2025 quarter. Resolve: segment note and MD&A of the FY2025 10-K ([S1]) and the Q4/FY2025 release ([S6]). (The 18th search aimed at this and was refused on budget.)
- **U3 — Q1 and Q2 2026 segment Adjusted EBITDA.** The Q2 2026 release ([S4]) and Q2 2026 10-Q ([S3]) contain them; the $88.2M chain-map figure needs confirmation.
- **U4 — Russia detail.** Insurance recoveries in FY2023 and FY2024; whether any recoveries occurred in 2022; the status of the 4 aircraft and 1 engine in Ukraine; whether the Russia assets remain in gross leasing-equipment cost; the gross (pre-deposit) carrying value written off in 2022; the number of claims settled versus outstanding. Resolve: "Russia" / "insurance" paragraphs in FY2023 and FY2024 10-Ks and the FY2025 10-K.
- **U5 — Lease-rate factors.** No stated LRF for FTAI or WLFC; WLFC engine count, average lease term and FY2025 totals. Resolve: WLFC FY2025 10-K ([S13]) Item 1 and Item 7.
- **U6 — ABS coupons and LTVs.** WEST VIII and IX note coupons, initial LTVs, and E-certificate sizes. Resolve: KBRA pre-sale reports ([S16],[S17]) and WLFC 8-Ks.
- **U7 — Security deposit and maintenance deposit balances.** FTAI's balance-sheet "security deposits" and "maintenance deposits" liabilities by year, and the reserve rates in its leases. Resolve: FY2025 10-K balance sheet and revenue-recognition note.
- **U8 — Depreciation policy.** Useful lives and residual assumptions for FTAI's aircraft and engines. Resolve: FY2025 10-K summary of significant accounting policies.
- **U9 — Half-life market values** for 12–15-year-old 737-800 and A320ceo aircraft, and full-life CFM56-7B/-5B/V2500 values, 2023–2026. Resolve: IBA/Cirium/mba published updates (D3 may hold engine values).
- **U10 — Conversion cost and slot availability** for 737-800 P2F (AEI, Boeing BCF, IAI). Resolve: conversion-house releases, trade press.
- **U11 — Equity-method investment** in the Leasing segment: counterparty, ownership, assets, income by year. Resolve: FY2025 10-K "Investments" note.
- **U12 — Seed Assets.** Number, type, sale price and transfer dates of assets sold to the 2025 Partnership; the $46.4M gain's cost basis. Resolve: FY2025 10-K related-party / Strategic Capital note; D7.
- **U13 — WestJet transaction terms.** Purchase price, lease term and rent for the 17 leased-back aircraft, the holding entity for the 10 off-lease aircraft, and whether the 10 are booked as leasing equipment or Aerospace Products inventory. Resolve: Q3 2026 10-Q (not yet filed) and D7.
- **U14 — Current engine-lessor scale.** Portfolio size and value for GE Engine Leasing, SMBC Aero Engine Lease, ELF, AerCap Engines, RRPF, MTU Maintenance Lease Services. Resolve: company websites and parent filings (D11 for the listed ones).
- **U15 — Average lease terms over time** (new-lease term at signing versus remaining term) and the mix of short- versus long-term engine leases in FTAI's book. Resolve: 10-K MD&A by year.

---

## 8. Terms introduced

- **Operating lease** — rental of an asset for a fixed term; lessor keeps title and residual-value risk.
- **Finance lease / sales-type lease** — lease that transfers substantially all ownership risks and rewards; economically a loan.
- **Lessor / lessee** — owner renting out the asset / operator renting it.
- **Residual-value risk** — risk that the asset's value at lease end differs from forecast.
- **Lease rate** — periodic rent, quoted monthly.
- **Lease-rate factor (LRF)** — monthly rent ÷ current asset value, in percent.
- **Short-term / long-term engine lease** — months to ~3 years to cover a shop visit or AOG / multi-year as a permanent spare.
- **AOG** — aircraft on ground; an unscheduled grounding awaiting a part or engine.
- **Security deposit** — cash or letter of credit held against lessee default; returned on performance.
- **Maintenance reserves (supplemental rent)** — per-hour/per-cycle payments pre-funding major maintenance; reimbursed up to the lesser of balance or qualifying cost; generally non-refundable otherwise.
- **Life-limited part (LLP)** — rotating engine part with a hard cycle limit requiring replacement.
- **Performance restoration (PR)** — the engine shop visit that restores exhaust-gas-temperature margin (D1).
- **End-of-lease (EOL) compensation** — cash adjustment at redelivery for the difference in maintenance condition versus delivery.
- **Return conditions** — contractual minimum maintenance state at redelivery.
- **Half-life / full-life** — valuation conventions: components midway between overhauls with half LLP life / all components fresh with full LLP life.
- **Maintenance adjustment** — difference between an asset's actual value and its half-life value due to maintenance condition.
- **Residual value** — forecast end-of-life value for depreciation.
- **Spare ratio** — spare engines as a percentage of installed engines.
- **Green-time engine** — engine with limited life to next shop visit, leased to consume that life.
- **Mid-life narrowbody** — roughly 10–18-year-old 737NG or A320ceo.
- **Sale-leaseback** — airline sells an aircraft to a lessor and leases it back.
- **Lease-attached trading** — buying an aircraft with its existing lease transferred.
- **P2F / STC** — passenger-to-freighter conversion / Supplemental Type Certificate, the approved modification design.
- **ABS** — asset-backed securitization; notes issued by an SPV secured on leased assets and their cash flows.
- **SPV** — special-purpose vehicle; bankruptcy-remote company owning the securitized assets.
- **Tranche (senior / mezzanine / equity)** — layered claims paid in order of seniority.
- **LTV** — loan-to-value; note balance ÷ appraised asset value.
- **Waterfall** — the ordered allocation of collections on each payment date.
- **ARD / legal final maturity** — anticipated repayment date after which cash is swept and coupons step up / the last date by which notes must be repaid.
- **Servicer** — party managing the leases for the SPV for a fee.
- **Warehouse facility** — revolving secured bank line used to accumulate assets ahead of an ABS take-out.
- **Advance rate / borrowing base** — the lendable percentage of each asset's value / the resulting total available credit.
- **Seed Assets** — FTAI's term for on-lease aircraft sold from its own book to start the 2025 Partnership.
- **MRE** — FTAI's Maintenance, Repair and Exchange offering (D5).
- **Utilization (FTAI definition)** — percent of days on lease, weighted by monthly average equity value of aviation leasing equipment, excluding airframes.

---

## 9. Sources

- [S1] FTAI Aviation Ltd., Form 10-K for FY2025 (period ended 31 Dec 2025; filed early 2026). https://www.sec.gov/Archives/edgar/data/1590364/000162828026012940/ftai-20251231.htm
- [S2] FTAI Aviation Ltd., Form 10-Q for the quarter ended 31 Mar 2026. https://www.sec.gov/Archives/edgar/data/1590364/000162828026029335/ftai-20260331.htm
- [S3] FTAI Aviation Ltd., Form 10-Q for the quarter ended 30 Jun 2026 (located; not read). https://www.sec.gov/Archives/edgar/data/0001590364/000162828026051412/ftai-20260630.htm
- [S4] FTAI Aviation Ltd., Q2 2026 earnings release, 8-K exhibit 99.1, 29 Jul 2026. https://www.sec.gov/Archives/edgar/data/1590364/000162828026050622/ftai6302026earningsrelease.htm
- [S5] FTAI Aviation Ltd., "Reports Second Quarter 2026 Results, Increases Dividend to $0.50 per Ordinary Share", GlobeNewswire, 29 Jul 2026. https://www.globenewswire.com/news-release/2026/07/29/3335598/35538/en/FTAI-Aviation-Ltd-Reports-Second-Quarter-2026-Results-Increases-Dividend-to-0-50-per-Ordinary-Share.html
- [S6] FTAI Aviation Ltd., Q4/FY2025 earnings release, 8-K exhibit 99.1, 25 Feb 2026. https://www.sec.gov/Archives/edgar/data/1590364/000162828026011685/ftai123125earningsrelease.htm
- [S7] FTAI Aviation Ltd., Form 10-K for FY2022. https://www.sec.gov/Archives/edgar/data/1590364/000159036423000007/ftai-20221231.htm
- [S8] FTAI Aviation Ltd., Form 10-K for FY2023 (located; utilization figure returned). https://www.sec.gov/Archives/edgar/data/1590364/000159036424000003/ftai-20231231.htm
- [S9] FTAI Aviation Ltd., Form 10-Q for the quarter ended 30 Sep 2025. https://www.sec.gov/Archives/edgar/data/1590364/000159036425000041/ftai-20250930.htm
- [S10] FTAI Aviation Ltd., Form 10-Q for the quarter ended 30 Sep 2024. https://www.sec.gov/Archives/edgar/data/1590364/000159036424000021/ftai-20240930.htm
- [S11] FTAI Aviation Ltd., "FTAI Acquires 27 Boeing 737-700 Aircraft from WestJet", GlobeNewswire, 28 Sep 2026. https://www.globenewswire.com/news-release/2026/09/28/3369685/35538/en/ftai-acquires-27-boeing-737-700-aircraft-from-westjet.html
- [S12] FTAI Aviation Ltd. and AEI, "Strategic Collaboration to Meet Growing Demand for Boeing 737-800 Freighters", GlobeNewswire, 7 Jul 2026. https://www.globenewswire.com/news-release/2026/07/07/3323001/0/en/FTAI-Aviation-and-AEI-Announce-Strategic-Collaboration-to-Meet-Growing-Demand-for-Boeing-737-800-Freighters.html
- [S13] Willis Lease Finance Corp., Form 10-K for FY2025. https://www.sec.gov/Archives/edgar/data/1018164/000101816426000036/wlfc-20251231x10k.htm
- [S14] Willis Lease Finance Corp., Q3 2025 earnings release, 8-K exhibit 99.1 (Nov 2025). https://www.sec.gov/Archives/edgar/data/1018164/000101816425000130/q32025ex991.htm
- [S15] Willis Lease Finance Corp., Form 10-Q for the quarter ended 30 Sep 2025. https://www.sec.gov/Archives/edgar/data/1018164/000101816425000134/wlfc-20250930.htm
- [S16] KBRA, "Assigns Preliminary Ratings to Willis Engine Structured Trust VIII", BusinessWire, 3 Jun 2025. https://www.businesswire.com/news/home/20250603065296/en/KBRA-Assigns-Preliminary-Ratings-to-Willis-Engine-Structured-Trust-VIII
- [S17] KBRA, "Assigns Preliminary Ratings to Willis Engine Structured Trust IX", BusinessWire, 10 Dec 2025. https://www.businesswire.com/news/home/20251210561858/en/KBRA-Assigns-Preliminary-Ratings-to-Willis-Engine-Structured-Trust-IX
- [S18] Asset Securitization Report (American Banker), "Willis Engine Structured Trust raises $596 million in aircraft ABS", 2025. https://asreport.americanbanker.com/news/willis-engine-structured-trust-raises-596-million-in-aircraft-abs
- [S19] Asset Securitization Report, "Willis Engine floats $392.9 million in aircraft-related ABS", Dec 2025. https://asreport.americanbanker.com/news/willis-engine-floats-392-9-million-in-aircraft-related-abs
- [S20] AviTrader, "IBA says it's a lessor's market" (IBA engine value and lease rate update), 25 Apr 2024. https://avitrader.com/2024/04/25/iba-says-its-a-lessors-market
- [S21] AJOT, "It's a lessor's market says IBA as engine lease rates and market values escalate", Apr 2024. https://www.ajot.com/news/its-a-lessors-market-says-iba-as-engine-lease-rates-and-market-values-escalate
- [S22] Aerospace Innovations, "Engine shortages and MRO backlog keep values and lease rates elevated, says IBA", 2025. https://aerospace-innovations.com/engine-shortages-and-mro-backlog-keep-values-and-lease-rates-elevated-says-iba/
- [S23] Air Cargo Update, "IBA reflects on overall stability of the engine market" (IBA H1 2026 Engine Value and Lease Rate Update), 2026. https://aircargoupdate.com/?p=8449
- [S24] Safe Fly Aviation, "CFM56 Engine Market Report 2026" (non-primary trade website). https://safefly.aero/cfm56-engine-market-report-2026/
- [S25] mba Aviation, "CFM56-5B Market Insight" (undated PDF). https://www.mba.aero/wp-content/uploads/CFM56-5B-Market-Insight.pdf
- [S26] India Seatrade News, "IBA warns of oversupply of narrowbody conversions and lease rate fall", 6 Sep 2026 (carrying IBA's July 2025 and 2026 narrowbody lease-rate commentary). https://indiaseatradenews.com/iba-warns-of-oversupply-of-narrowbody-conversions-and-lease-rate-fall/
- [S27] India Seatrade News, IBA commentary, 26 May 2026. https://indiaseatradenews.com/?p=88549
- [S28] Aeroin (Portuguese), "Valores de aviões cargueiros disparam enquanto taxas de leasing de narrowbodies recuam, aponta IBA", 2025. https://aeroin.net/valores-de-avioes-cargueiros-disparam-enquanto-taxas-de-leasing-de-narrowbodies-recuam-aponta-iba/
- [S29] IBA, "Aircraft values and lease rates update, February 2024". https://www.iba.aero/insight/aircraft-values-lease-rates-update-february-2024/
- [S30] IBA, "Historical lease rate performance: A320ceo v 737-800", Dec 2019. https://www.iba.aero/news/historical-lease-rate-performance-a320ceo-v-737-800-december-2019/
- [S31] AerCap Holdings N.V., Form 20-F for FY2013 (maintenance rents and EOL compensation definitions). https://www.sec.gov/Archives/edgar/data/0001378789/000104746914002538/a2219001z20-f.htm
- [S32] AerCap Holdings N.V., Form 6-K exhibit 99.1, 2021. https://www.sec.gov/Archives/edgar/data/1378789/000119312521302041/d234063dex991.htm
- [S33] Spirit Airlines, Inc., Form 10-K for FY2013 (lessee-side maintenance reserve accounting). https://www.sec.gov/Archives/edgar/data/0001498710/000149871014000019/save-20131231x10kxmaster.htm
- [S34] Maheshwari & Co., "Aircraft maintenance reserve clauses" (law-firm blog, undated). https://www.maheshwariandco.com/blog/aircraft-maintenance-reserve-clauses/
- [S35] mba Aviation, "Maintenance Matters in Aircraft ABS Deals, Part 1" (PDF, undated). https://mba.aero/wp-content/uploads/Maintenance-Matters-in-Aircraft-ABS-Deals-Part-1-1.pdf
- [S36] MTU Aero Engines, AEROREPORT, "How airlines benefit from engine leasing" (undated). https://aeroreport.de/en/aviation/how-airlines-benefit-from-engine-leasing
- [S37] Acumen Aviation, "Spare Engines as Strategy: The Asset Class Inside the Asset Class" (blog, undated). https://www.acumen.aero/blogs/spare-engines-as-strategy-the-asset-class-inside-the-asset-class
- [S38] AviTrader MRO e-magazine, July 2019 (engine-lessor market feature; dated). https://www.ajw-group.com/storage/downloads/1563886266_avitrader_monthly_mro_e-magazine_2019-07.pdf
- [S39] FlightGlobal, "Freedom to be flexible" (engine leasing feature, undated). https://flightglobal.com/freedom-to-be-flexible/47182.article
- [S40] Aviation Week, "IBA predicts 40 per cent increase in shop visits from 2024 to 2025". https://aviationweek.com/mro/iba-predicts-40-cent-increase-shop-visits-2024-2025
- [S41] Aviation Week (via megaproject.com), "Beautech's new 10-year deal highlights shift in spare engine planning", 23 Jun 2026. https://megaproject.com/news/airport/beautechs-new-10-year-deal-highlights-shift-in-spare-engine-planning
- [S42] Aviation Finance, "It's time to Uberize the spare engine market". https://www.aviationfinance.aero/article.php?i=17877
- [S43] FTAI Aviation Ltd., "FTAI Closes $2.0 Billion Warehouse Financing Facility for Strategic Capital's Second Investment Vehicle", GlobeNewswire, 17 Aug 2026 (from edgar-index; not opened this session). https://www.globenewswire.com/news-release/2026/08/17/3345919/35538/en/ftai-closes-2-0-billion-warehouse-financing-facility-for-strategic-capital-s-second-investment-vehicle.html
- [S44] Boeing / GECAS, "Boeing, GECAS Announce Agreement for 35 737-800 Boeing Converted Freighters", PRNewswire (date not verified). https://www.prnewswire.com/news-releases/boeing-gecas-announce-agreement-for-35-737-800-boeing-converted-freighters-300682223.html
- Project files: /home/user/SPOT/ftai-primer/research/chain-map.md; /home/user/SPOT/ftai-primer/research/edgar-index.md.
