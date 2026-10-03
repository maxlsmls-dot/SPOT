#!/usr/bin/env python3
"""Generate the compiled blocks of Part XII (glossary, chain-map row table, company index,
unknowns register, consolidated sources) and fill them into the Part XII template.
Usage: python3 gen12.py [--debug]
"""
import re, sys, os, html, collections

ROOT = "/home/user/SPOT/ftai-primer"
PARTS = ["part01-cfm56-machine.md", "part02-money-mechanics.md", "part03-context.md",
         "part04-shop-visit-market.md", "part05-usm-teardown.md", "part06-pma-der.md",
         "part07-aerospace-products.md", "part08-leasing-sci.md", "part09-ftai-power.md",
         "part10-company.md", "part11-markets-peers.md"]
ROMAN = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI"]
ROMAN_ORDER = {r: i for i, r in enumerate(ROMAN)}
DEBUG = "--debug" in sys.argv
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
os.makedirs(OUT, exist_ok=True)

def esc(s):
    return html.escape(s, quote=False)

# ---------------------------------------------------------------- Part files and sections
part_lines = {}
for i, fn in enumerate(PARTS):
    with open(os.path.join(ROOT, "parts", fn), encoding="utf-8") as f:
        part_lines[ROMAN[i]] = f.read().split("\n")

def section_index(lines):
    """Return list parallel to lines: section number (int), "U" for the unknowns list, or None."""
    cur = None
    out = []
    for ln in lines:
        m = re.match(r"^## (\d+)\.", ln)
        if m:
            cur = int(m.group(1))
        elif re.match(r"^## Unknowns", ln):
            cur = "U"
        elif re.match(r"^## (Tensions|Sources)", ln):
            cur = None
        out.append(cur)
    return out

part_secs = {r: section_index(part_lines[r]) for r in ROMAN}

def fmt_sections(secs):
    secs = sorted(set(secs))
    return ", ".join(f"§{s}" for s in secs)

# ---------------------------------------------------------------- Definition boxes
BoxDef = collections.namedtuple("BoxDef", "part section title text line")
boxes = []
box_re = re.compile(r'<div class="defn"><b>(.*?)</b>(.*?)</div>\s*$')
for r in ROMAN:
    for i, ln in enumerate(part_lines[r]):
        m = re.search(r'<div class="defn"><b>(.*?)</b>(.*)', ln)
        if m:
            title = html.unescape(m.group(1))
            body = m.group(2)
            # the box may run over several lines until </div></div> or </p></div>
            j = i
            while "</div>" not in body and j + 1 < len(part_lines[r]):
                j += 1
                body += " " + part_lines[r][j]
            body = re.sub(r'<span class="cite">.*?</span>', "", body)
            body = re.sub(r"<[^>]+>", " ", body)
            body = html.unescape(re.sub(r"\s+", " ", body)).strip()
            boxes.append(BoxDef(r, part_secs[r][i], title, body, i))

def norm(s):
    s = s.lower()
    s = re.sub(r"\(.*?\)", " ", s)
    s = s.replace("&amp;", "&").replace("’", "'")
    s = re.sub(r"[^a-z0-9&\- ]+", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

def pieces(s):
    """Split a term or box title into candidate name pieces."""
    s = html.unescape(s)
    parts = re.split(r"\s*/\s*|;\s*|,\s*|\s+and\s+|\s+or\s+|:\s*", s)
    out = []
    for p in parts:
        p = p.strip()
        if not p:
            continue
        out.append(norm(p))
        inner = re.findall(r"\((.*?)\)", p)
        for q in inner:
            for qq in re.split(r";\s*|,\s*|\s+or\s+", q):
                if qq.strip():
                    out.append(norm(qq))
        out.append(norm(re.sub(r"\(.*?\)", "", p)))
    out = [o for o in out if o and o not in ("the", "a")]
    return list(dict.fromkeys(out))

STOP = {"and", "the", "of", "or", "a", "in", "to", "per", "versus", "vs"}

def match_score(term_pieces, box_title):
    bp = pieces(box_title)
    best = 0
    for t in term_pieces:
        if len(t) < 3:
            continue
        for b in bp:
            if t == b:
                best = max(best, 3)
            elif len(t) >= 5 and (t in b or b in t) and len(min(t, b, key=len)) >= 4:
                best = max(best, 2)
    return best

# ---------------------------------------------------------------- Registry
reg_path = os.path.join(ROOT, "research", "term-registry.md")
reg = open(reg_path, encoding="utf-8").read().split("\n")
start = next(i for i, l in enumerate(reg) if l.startswith("## 1. The registry"))
end = next(i for i, l in enumerate(reg) if l.startswith("## 1b."))
rows = []
for ln in reg[start:end]:
    if not ln.startswith("| ") or ln.startswith("| Term |") or ln.startswith("|---"):
        continue
    cells = [c.strip() for c in ln.strip().strip("|").split("|")]
    if len(cells) < 7:
        continue
    term, alias, defn, owner, first, spine, box = cells[:7]
    rows.append(dict(term=term, alias=alias, defn=defn, owner=owner, first=first, spine=spine, box=box))

def clean_registry_def(d):
    d = re.sub(r"\s*\((?=[^()]*(?:\bD\d{1,2}\b\s*§|orchestrator|chain map|outline))[^()]*\)", "", d)
    d = re.sub(r"\s*\(see section \d\)", "", d)
    d = re.sub(r"\s*\((?:D\d+|see|section)[^()]*\)", "", d)
    d = re.sub(r"\.?\s*See (?:C-|section|C-shop)[^.]*\.?$", "", d)
    d = re.sub(r"\.?\s*See (?:C-|section)[^.;]*(?=[.;]|$)", "", d)
    d = re.sub(r"\s+", " ", d).strip()
    d = d.strip(" ;")
    if d and d[-1] not in ".!?":
        d += "."
    d = d[0].upper() + d[1:] if d else d
    return d

SENT_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9\"“(])")
ABBREV = re.compile(r"\b(Inc|Ltd|Corp|Co|No|approx|vs|U\.S|St|Jr|Mr|Ms|Dr|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec|cf|e\.g|i\.e)\.$")

def sentences(text):
    out, buf = [], ""
    for piece in SENT_SPLIT.split(text):
        if buf:
            buf = buf + " " + piece
        else:
            buf = piece
        if ABBREV.search(buf) or re.search(r"\b[A-Z]\.$", buf):
            continue
        out.append(buf)
        buf = ""
    if buf:
        out.append(buf)
    return out

XREF = re.compile(r"^(Part [IVX]+ §[\d.]+(,? (and |or )?Part [IVX]+ §[\d.]+)*|§\d+|Parts? [IVX]+( and [IVX]+)?( §[\d.]+)?)\b.*\b(carries?|carry|treats?|is the full treatment|owns?|covers?|gives?|states?|works?|carried|treated|sets out|explains?|answers?)\b")

def tighten(text, maxwords=70):
    ss = [s.strip() for s in sentences(text) if s.strip()]
    ss = [s for s in ss if not XREF.match(s)]
    if not ss:
        return ""
    out = [ss[0]]
    if len(ss) > 1 and len(ss[0].split()) < 45:
        out.append(ss[1])
    txt = " ".join(out)
    if len(txt.split()) > 62 and len(out) == 2:
        txt = out[0]
    return txt

# manual overrides: registry term -> (part, box title) or None to force the registry text
OVERRIDE = {
    "Lessor / lessee": None,
    "Up-cycling": None,
    "Peer set": None,
    "History timeline": None,
    "Shareholders": None,
    "Engine sale / outright module sale / exchange": ("VII", "Engine sale, outright module sale and exchange"),
    "Exchange fee / core (exchange sense)": ("VII", "Exchange fee and the returned core"),
    "Module exchange / engine exchange": ("I", "Module exchange"),
    "Hospital (quick-turn) visit": ("I", "Hospital visit (quick-turn visit)"),
    "Bypass / turbofan / high-bypass turbofan": ("I", "Turbofan, bypass and high-bypass turbofan"),
    "LP spool / HP spool; two-shaft (two-spool) design": ("I", "Two-shaft (two-spool) design; low-pressure and high-pressure spools"),
    "Base value": ("I", "Base value and market value"),
    "Market value": ("I", "Base value and market value"),
    "Core": ("I", "Core (gas generator)"),
    "Module": ("I", "Module"),
    "Module (FTAI Power usage)": ("IX", "Module (FTAI Power usage)"),
    "Major module / sub-module": ("I", "Major module and sub-module"),
    "Appraiser": ("I", "Appraiser"),
    "Mid-life narrowbody": ("I", "Mid-life narrowbody"),
    "Cycles since new": ("I", "Cycles remaining (CR) and cycles since new (CSN)"),
    "Cycles remaining": ("I", "Cycles remaining (CR) and cycles since new (CSN)"),
    "LLP stack": None,
    "LLP stagger": None,
    "Engine lease: short-term / long-term": ("I", "Engine lease, short-term and long-term"),
    "Return conditions": ("I", "Return conditions (redelivery conditions)"),
    "Spare engine / spare ratio": ("I", "Spare engine and spare ratio"),
    "Waterfall (ABS)": ("II", "Payment waterfall (ABS)"),
    "Installed base": ("I", "Installed base"),
    "Retirement rate": ("I", "Retirement rate"),
    "LEAP (LEAP-1A / LEAP-1B)": ("I", "LEAP (LEAP-1A and LEAP-1B)"),
    "Durability Improvement Package / LEAP durability kit": ("I", "LEAP durability kit (Durability Improvement Package)"),
    "Lease extension / extension share": ("III", "Lease extension and the extension share"),
    "Shop-visit forecast / first shop visit": ("III", "Shop-visit forecast and first shop visit"),
    "Shop-visit demand": None,
    "Fleet states: in service / parked (stored) / retired (withdrawn)": ("III", "Fleet states: in service, parked (stored), retired (withdrawn)"),
    "MRO market / engine MRO": ("III", "MRO market and engine MRO"),
    "Independent MRO / MRO": ("I", "MRO and independent MRO"),
    "OEM": ("I", "Original equipment manufacturer (OEM)"),
    "Catalogue list price": ("I", "Catalogue list price (CLP), or list price"),
    "Escalation (spare parts and LLPs)": ("I", "Escalation (catalogue escalation; LLP escalation)"),
    "Engine shop": ("I", "Engine shop"),
    "Engine stand": ("IV", "Engine stand"),
    "EngineWise": ("I", "EngineWise"),
    "TrueChoice (Flight Hour, Overhaul, Material, Transitions)": ("I", "TrueChoice"),
    "Turnaround time": ("I", "Turnaround time (TAT)"),
    "Induction / induction slot": ("IV", "Induction; induction slot"),
    "Long-term service agreement": ("IV", "Long-term service agreement (LTSA); also long-term agreement (LTA), rate-per-flight-hour (RPFH) or flight-hour agreement"),
    "Licensed / joint-venture shop": ("IV", "Licensed shop; joint-venture shop"),
    "Repair vendors / component repairs": ("IV", "Repair vendors; component repairs"),
    "Part 145 repair station": ("I", "Part 145 repair station"),
    "Airworthiness Directive / Service Bulletin": ("I", "Airworthiness Directive (AD) and Service Bulletin (SB)"),
    "Auxiliary power unit": ("V", "Auxiliary power unit (APU)"),
    "Feedstock": ("I", "Feedstock"),
    "Module as unit of trade": ("I", "Module as a unit of trade"),
    "Part-out / teardown": ("I", "Part-out and teardown"),
    "Release tag / serviceable tag": ("I", "Release tag (serviceable tag)"),
    "Run-out / exhausted engine": ("V", "Run-out (exhausted) engine"),
    "Used serviceable material": ("V", "Used serviceable material (USM)"),
    "Serviceable as removed": ("V", "Serviceable as removed"),
    "Hard-time part": ("V", "Hard-time (HT) part"),
    "Whole-asset sale": ("V", "Whole-asset sale (flight-equipment sale)"),
    "Designated Engineering Representative": ("VI", "Designated Engineering Representative (DER)"),
    "DER repair": ("VI", "DER repair"),
    "Production certificate / production approval": ("VI", "Production certificate (PC) and production approval"),
    "Type certificate / type-certificate holder": ("VI", "Type certificate (TC) and type-certificate holder (TCH)"),
    "Parts Manufacturer Approval": ("VI", "Parts Manufacturer Approval (PMA)"),
    "Supplemental Type Certificate": ("VI", "Supplemental Type Certificate (STC)"),
    "Part 21 Subpart K": ("VI", "14 CFR Part 21 Subpart K"),
    "Identicality (with / without a licensing agreement)": ("VI", "Identicality (without a licensing agreement; by licensing agreement)"),
    "Airworthiness Limitations Section / Instructions for Continued Airworthiness": ("VI", "Airworthiness Limitations Section (ALS) and Instructions for Continued Airworthiness (ICA)"),
    "Critical component / critical part": ("VI", "Critical component (critical part)"),
    "Technical Implementation Procedures": ("VI", "Technical Implementation Procedures (TIP)"),
    "FAA Form 8110-3": ("VI", "FAA Form 8110-3 (Statement of Compliance with Airworthiness Standards)"),
    "OEM-only clause": ("VI", "OEM-only clause (no-PMA / no-DER clause; TCH-configuration clause)"),
    "FTAI–Chromalloy joint venture": ("VI", "FTAI–Chromalloy joint venture (the PMA joint venture)"),
    "HEICO Flight Support Group": ("VI", "HEICO Flight Support Group (FSG)"),
    "Chromalloy": ("VI", "Chromalloy"),
    "Unapproved parts episode (AOG Technics, 2023)": None,
    "CFM materials agreement": ("VII", "CFM materials agreement"),
    "Maintenance, Repair and Exchange": ("VII", "Maintenance, Repair and Exchange (MRE)"),
    "Module Factory": ("I", "Module Factory"),
    "Modules produced / refurbished (count)": ("VII", "Modules produced (modules refurbished)"),
    "Muddy Waters report / short report / short seller": ("VII", "Short report, short seller and the Muddy Waters report"),
    "Audit Committee / Audit Committee review": ("VII", "Audit Committee and the Audit Committee review"),
    "Inventory (Module Factory working capital)": ("VII", "Inventory (the Module Factory's working capital)"),
    "Revenue and EBITDA per module (derived)": ("VII", "Revenue and Adjusted EBITDA per module (derived)"),
    "Lockheed Martin Commercial Engine Solutions": ("IV", "LMCES; Montréal"),
    "QuickTurn (Miami) / QuickTurn Europe (Rome)": ("IV", "QuickTurn; QuickTurn Europe"),
    "V2500 program (IAE EngineWise agreement)": ("I", "FTAI's V2500 program (the IAE EngineWise agreement)"),
    "V2500 / IAE": ("I", "V2500 and IAE"),
    "Prime Engine Accessories": None,
    "GMF AeroAsia / EgyptAir partnerships": None,
    "Orange / Lisbon": None,
    "Aerospace Products segment": ("I", "Aerospace Products segment"),
    "Aviation Leasing segment": ("I", "Aviation Leasing segment"),
    "Segment Adjusted EBITDA": ("VII", "Segment Adjusted EBITDA"),
    "Adjusted EBITDA (consolidated; the definition)": ("X", "Adjusted EBITDA (consolidated; the company's definition)"),
    "Cost of sales (segment versus consolidated)": ("VII", "Cost of sales (segment versus consolidated)"),
    "Stand-ready obligation": ("VII", "Stand-ready obligation"),
    "ASC 606 / noncash consideration": ("VII", "ASC 606 and noncash consideration"),
    "Equity method": ("VIII", "Equity method (equity-method investment; equity pick-up; equity in earnings of unconsolidated entities)"),
    "Profit elimination": ("VIII", "Profit elimination (intra-entity profit elimination)"),
    "2025 Partnership": ("VIII", "2025 Partnership (2025 SPV; FTAI SCI I; the inaugural Strategic Capital vehicle)"),
    "2026 SPV": ("VIII", "2026 SPV (SCI II; the second investment vehicle)"),
    "Servicer": ("VIII", "Servicer"),
    "Servicing fee": ("VIII", "Servicing fee"),
    "Strategic Capital Initiative": ("VIII", "Strategic Capital Initiative (SCI)"),
    "Seed Assets": ("VIII", "Seed Assets"),
    "Accordion": ("VIII", "Accordion"),
    "Deployment / fully committed / harvest phase": ("VIII", "Deployment, fully committed, and harvest phase"),
    "Equity commitment / hard cap": ("VIII", "Equity commitment and hard cap"),
    "Gain on sale of leased equipment / to the 2025 Partnership": ("VIII", "Gain on sale of leased equipment, and the gain on sale to the 2025 Partnership"),
    "Hurdle / preferred return": ("VIII", "Hurdle (preferred return)"),
    "Lease income / maintenance revenue / asset sales revenue": ("VIII", "Lease income, maintenance revenue and asset sales revenue"),
    "Limited partner / general partner": ("VIII", "Limited partner (LP) and general partner (GP)"),
    "Management fee / incentive fee / sales fee": ("VIII", "Management fee, incentive fee and sales fee"),
    "Promote / carried interest": ("VIII", "Promote (carried interest; carry)"),
    "Russia assets, impairment and insurance recoveries": ("VIII", "Russia assets, impairment and insurance recoveries (contingent cover)"),
    "Syndicated / structuring agent / lead arranger": ("VIII", "Syndicated loan, structuring agent and lead arranger"),
    "Variable interest entity / primary beneficiary": ("VIII", "Variable interest entity (VIE) and primary beneficiary"),
    "WestJet transaction / AEI collaboration": ("VIII", "WestJet transaction and AEI collaboration"),
    "Blackbird / Thunderbolt (Air Lease)": ("VIII", "Blackbird Capital I and II, and Thunderbolt (Air Lease)"),
    "Utilization (FTAI definition)": ("VIII", "Utilization (FTAI definition)"),
    "Net book value": ("XI", "Net book value (NBV)"),
    "Gas turbine / gas generator": ("IX", "Gas turbine; gas generator"),
    "Generator set": ("IX", "Generator set (genset)"),
    "Frame (heavy-duty) turbine": ("IX", "Frame (heavy-duty) gas turbine"),
    "Reciprocating engine / solid-oxide fuel cell": ("IX", "Reciprocating engine; solid-oxide fuel cell"),
    "Simple cycle / combined cycle; baseload / backup / peaking; PJM / ERCOT": ("IX", "Simple cycle and combined cycle; baseload, backup and peaking"),
    "Mobile genset": ("IX", "Mobile generator set"),
    "LHV / HHV": ("IX", "Lower heating value (LHV) and higher heating value (HHV)"),
    "NOx / selective catalytic reduction": ("IX", "Nitrogen oxides (NOx); selective catalytic reduction (SCR)"),
    "Mod-1": ("IX", "Mod-1 (FTAI Mod-1; CFM56 aeroderivative)"),
    "J&F Power Systems LLC": ("IX", "J&F Power Systems LLC (J&F)"),
    "Jereh Group": ("IX", "Jereh Group (Yantai Jereh Oilfield Services Group Co., Ltd.)"),
    "Master supply agreement / purchase order / milestone payments / performance adjustment mechanism": ("IX", "Master supply agreement; purchase order; milestone payments; performance adjustment mechanism"),
    "Interconnection agreement / interconnection queue": ("IX", "Interconnection agreement; interconnection queue"),
    "Balance of plant / packaging": ("IX", "Balance of plant; packaging"),
    "Behind-the-meter": ("IX", "Behind-the-meter (BTM) generation"),
    "Basic / diluted EPS; RSU / PSU": ("X", "Basic and diluted earnings per share; RSUs and PSUs"),
    "Cayman Islands exempted company / redomiciliation": ("X", "Cayman Islands exempted company and redomiciliation"),
    "Dividend (ordinary) / share repurchase program": ("X", "Ordinary dividend and share repurchase program"),
    "Employees": ("X", "Employees (headcount as the 10-K defines it)"),
    "External management / manager / management agreement / management fee / incentive allocation / Master GP": ("X", "External management: manager, management agreement, management fee, incentive allocation and Master GP"),
    "Fixed-to-floating / fixed-rate reset preferred": ("X", "Fixed-to-floating and fixed-rate reset preferred"),
    "Form 10-K / 10-Q / 8-K / DEF 14A / DEFM14A / S-4": ("X", "SEC filings: Form 10-K, 10-Q, 8-K, DEF 14A, DEFM14A and S-4"),
    "Fortress / FIG LLC / FTAI Infrastructure": ("X", "Fortress, FIG LLC and FTAI Infrastructure (FIP)"),
    "Guidance": ("X", "Guidance"),
    "Named executive officers and compensation": ("X", "Named executive officers (NEOs) and the proxy's pay disclosures"),
    "Net debt / leverage ratio": ("X", "Net debt and leverage ratio"),
    "Operating versus investing cash flow (inventory versus leasing equipment)": ("X", "Operating versus investing cash flow: inventory against leasing equipment"),
    "Preferred shares (cumulative, perpetual, redeemable; liquidation preference)": ("X", "Preferred shares: cumulative, perpetual, redeemable; liquidation preference"),
    "Revolving credit facility / SOFR": ("X", "Revolving credit facility and SOFR"),
    "Risk factors / auditor / securities class action / lead plaintiff": ("X", "Risk factors (Item 1A); auditor; securities class action; lead plaintiff"),
    "Senior unsecured notes / bullet / callable": ("X", "Senior unsecured notes; bullet; callable"),
    "Spin-off / record date": ("X", "Spin-off and record date"),
    "Form 20-F / Form 6-K": ("XI", "Form 20-F / Form 6-K"),
    "Shannon Engine Support": ("XI", "Shannon Engine Support (SES)"),
    "Center of Excellence": ("XI", "Center of Excellence (CoE)"),
    "Distribution (new parts)": ("XI", "Distribution (new parts)"),
    "Gross margin (AerSale Asset Management Solutions)": ("XI", "Gross margin (AerSale Asset Management Solutions)"),
    "Margin pool": ("XI", "Margin pool"),
    "Half-life (base) value": ("I", "Half-life (base) value"),
    "Full-life value": ("I", "Full-life value"),
    "Performance restoration": ("I", "Performance restoration (PR) and core PR"),
    "Overhaul (full disassembly; heavy or full shop visit)": ("I", "Overhaul (heavy or full shop visit; \"zero-time\")"),
    "Line-replaceable unit / quick-engine-change kit": ("I", "Line-replaceable unit (LRU) and quick-engine-change kit (QEC)"),
    "Booster": ("I", "Booster, or low-pressure compressor (LPC)"),
    "Borescope / boroblend": ("I", "Borescope and boroblend"),
    "Disk / spool": ("I", "Disk and spool"),
    "First run / mature run": ("I", "First run and mature run"),
    "Sum of modules / sum of parts": ("I", "Sum of modules (sum of parts)"),
    "Test cell / test-cell run": ("I", "Test cell (test-cell run)"),
    "Thrust / thrust rating": ("I", "Thrust and thrust rating"),
    "Serviceable / unserviceable": ("I", "Serviceable and unserviceable"),
    "Used LLPs": ("I", "Used LLPs (part-life LLPs; LLP package)"),
    "Mini-pack": ("I", "Mini-pack (records mini-pack)"),
    "Build standard": ("I", "Build standard (configuration)"),
    "Fan frame": ("I", "Fan frame"),
    "Engine flight cycle": ("I", "Engine flight cycle (EFC) and engine flight hour (EFH)"),
    "Engine flight hour": ("I", "Engine flight cycle (EFC) and engine flight hour (EFH)"),
    "Finance lease / sales-type lease": ("II", "Finance lease (sales-type lease)"),
    "Lease rate": ("II", "Lease rate (rent)"),
    "Residual value / residual-value risk": ("II", "Residual value and residual-value risk"),
    "Tranche: senior / mezzanine / equity": ("II", "Tranche: senior, mezzanine and equity"),
    "Freighter conversion": ("II", "Freighter conversion, or passenger-to-freighter (P2F)"),
    "Anticipated repayment date / legal final maturity": ("II", "Anticipated repayment date (ARD) and legal final maturity"),
    "Advance rate / borrowing base": ("II", "Advance rate and borrowing base"),
    "Green time / green-time engine / green-time lease": ("I", "Green time"),
    "Equity-method investment in Aviation Leasing": ("VIII", "Equity-method investment in Aviation Leasing"),
    "Aerospace products revenue (income-statement line)": ("VII", "Aerospace products revenue (income-statement line)"),
    "Cost build (shop visit)": None,
    "Gearbox (genset)": ("IX", "Gearbox (genset)"),
    "Half-life trade": ("V", "Half-life trade"),
    "Capacity (shop)": ("IV", "Capacity (shop)"),
    "Utilization (FTAI definition)": ("VIII", "Utilization (FTAI definition)"),
}

# custom glossary texts (pared from the registry or the owner box; no new facts)
TEXT_OVERRIDE = {
    "History timeline": "The dated sequence of corporate events that Part X assembles: the 2015 IPO of Fortress Transportation and Infrastructure Investors, the 2022 spin-off and redomiciliation, the 2023 QuickTurn and 2024 Montréal acquisitions, the 2024 internalization, the launch of the Strategic Capital Initiative and of FTAI Power, the 2025 short report, the 2026 CFM materials agreement, the J&F order, the 2026 SPV warehouse, the $500M buyback authorisation and the WestJet purchase of 28 September 2026. Part X §75 carries the table with each date and source.",
    "Peer set": "The companies Part XI sets beside FTAI from their own filings: Willis Lease Finance (engine lessor), AerCap and Air Lease (aircraft lessors), HEICO (PMA), AerSale (teardown and used material), StandardAero (independent engine MRO), AAR (distribution and used material) and GE Aerospace (OEM), with Safran, MTU Maintenance and Lufthansa Technik as non-SEC context. They were chosen so that each FTAI activity has a filing that isolates it.",
    "Lessor / lessee": "The lessor is the owner that rents out an aircraft or engine; the lessee is the operator that rents it. Plain words that need no box; Part II §12 uses them from its first paragraph.",
    "LLP stack": "Another name for the full set of life-limited parts in an engine, which Part I calls the full LLP set; its remaining life largely sets a used engine's value. A 2008 price table calls the same thing a shipset.",
    "LLP stagger": "The mismatch of remaining lives across an engine's life-limited parts: replacing only the limiting part brings the next LLP-forced removal sooner. It is the same mechanism Part I §4 treats as stub life.",
    "Shop-visit demand": "The market's size in visits a year: just above 2,000 CFM56 visits in 2019, and about 2,300 to 2,400 projected for each of 2026 to 2028 with the apex around 2027 to 2028 (GE and Safran). It is driven by the installed base, utilisation and the retirement assumption, which was over-forecast by 1.5 to 2.5 points in 2025 and 2026; Part III §23 carries the forecast curve and Part IV §26 the market reading.",
    "Prime Engine Accessories": "A 50/50 joint venture with Bauer, Inc. in Bristol, Connecticut, described by FTAI as an MRE repair facility for accessory parts expected to deliver up to $75,000 of average savings per shop visit. It is accounted for under the equity method and was expected to be operational at the end of 2025.",
    "Orange / Lisbon": "Two 100%-owned maintenance sites listed in the FY2025 10-K. Orange (California) has no retrieved description or date; Lisbon is described in the chain map as 113,000 sq ft and 300-plus modules a year, unverified against a primary source, and was still ramping in July 2026.",
    "GMF AeroAsia / EgyptAir partnerships": "Capacity partnerships referenced on the Q2 2026 call with Garuda Indonesia's MRO arm and with EgyptAir Maintenance & Engineering, adding module capacity in Indonesia and Egypt. Their terms, capacity and economics were not retrieved.",
    "Unapproved parts episode (AOG Technics, 2023)": "In 2023 parts with forged documentation from the supplier AOG Technics were found on CFM56 engines at Delta, United, Southwest and American. They are a different category from PMA parts, which are FAA-approved.",
    "Shareholders": "FTAI's largest reported holders per the 2026 proxy: Capital International Investors 13.51%, Capital World Investors 12.43%, The Vanguard Group 10.10% and FMR LLC 5.25%, with nine insiders at about 1.35%. About 102.6M shares are implied.",
    "Up-cycling": "APOC Aviation's own term for buying an engine in order to tear it down for material.",
    "Cost build (shop visit)": "The cost of a shop visit built up as the sum of labour, new OEM parts, component repairs, life-limited-part replacement (new or used) and the test-cell run, plus freight, consumables and the shop's margin. Material is about 60 to 70% of the total; Part I §7 works the example.",
}

def find_box(term, owner):
    key = term
    if key in OVERRIDE:
        ov = OVERRIDE[key]
        if ov is None:
            return None
        for b in boxes:
            if b.part == ov[0] and html.unescape(b.title) == ov[1]:
                return b
        print("OVERRIDE NOT FOUND:", term, ov, file=sys.stderr)
    tp = pieces(term)
    best, bestb = 0, None
    for b in boxes:
        if b.part != owner:
            continue
        s = match_score(tp, b.title)
        if s > best:
            best, bestb = s, b
    if best >= 2:
        return bestb
    best, bestb = 0, None
    for b in boxes:
        s = match_score(tp, b.title)
        if s > best:
            best, bestb = s, b
    if best >= 3:
        return bestb
    return None

glossary = []
for r in rows:
    b = find_box(r["term"], r["owner"])
    owner_label = f"Part {r['owner']}"
    if b is not None:
        text = tighten(b.text)
        where = f"Part {b.part} §{b.section}" if isinstance(b.section, int) else f"Part {b.part}"
        if b.part == r["owner"]:
            ownertxt = f"Owner: {where}."
        else:
            ownertxt = f"Owner: {owner_label}; boxed in {where}."
        src = "box"
    else:
        text = tighten(clean_registry_def(r["defn"]), maxwords=80)
        ownertxt = f"Owner: {owner_label}."
        src = "registry"
    if r["term"] in TEXT_OVERRIDE:
        text = TEXT_OVERRIDE[r["term"]]
        src = "custom"
    glossary.append(dict(term=r["term"], alias=r["alias"], text=text, owner=ownertxt, src=src, box=b))

def sort_key(name):
    n = name.lower()
    n = re.sub(r"^(the|a) ", "", n)
    n = n.replace("–", "-").replace("’", "'")
    n = re.sub(r"[^a-z0-9 ]", "", n)
    return n

glossary.sort(key=lambda g: sort_key(g["term"]))

gl_lines = ["<dl>"]
for g in glossary:
    dt = esc(g["term"])
    if g["alias"]:
        dt += f" ({esc(g['alias'])})"
    gl_lines.append(f"<dt>{dt}</dt>")
    gl_lines.append(f"<dd>{esc(g['text'])} <span class=\"cite\">{esc(g['owner'])}</span></dd>")
gl_lines.append("</dl>")
GLOSSARY = "\n".join(gl_lines)
n_glossary = len(glossary)

if DEBUG:
    with open(os.path.join(OUT, "glossary_debug.txt"), "w") as f:
        for g in glossary:
            bt = g["box"].title if g["box"] else "-"
            f.write(f"{g['src']:8} | {g['term']} | {g['alias']} | {bt} | {g['owner']}\n   {g['text']}\n")
    print(f"glossary entries: {n_glossary}; from boxes: {sum(1 for g in glossary if g['src']=='box')}")

# ---------------------------------------------------------------- Translation-table rows
row_map = collections.defaultdict(set)
for r in ROMAN[3:]:
    lines = part_lines[r]
    try:
        s = next(i for i, l in enumerate(lines) if l.startswith("### Translation-table rows answered"))
    except StopIteration:
        continue
    e = next(i for i in range(s + 1, len(lines)) if lines[i].startswith("## "))
    txt = " ".join(lines[s:e])
    for m in re.finditer(r"rows?\s+((?:T-\d+(?:,\s*)?)+)", txt):
        for t in re.findall(r"T-\d+", m.group(1)):
            row_map[t].add(r)
    for m in re.finditer(r"row T-(\d+)", txt):
        row_map[f"T-{m.group(1)}"].add(r)

ROW_LABELS = {
    "T-1": "Low CFM56 retirements", "T-2": "GTF powder-metal groundings",
    "T-3": "LEAP durability shortfall and the July 2026 kit", "T-4": "737 MAX production rate cap",
    "T-5": "Airbus delivery shortfall and the rate-75 deferral", "T-6": "Lessor extension behaviour",
    "T-7": "OEM parts-price escalation", "T-8": "MRO capacity shortfall and turnaround",
    "T-9": "Used-material and feedstock scarcity", "T-10": "Data-center power demand and the gas-turbine shortage",
    "T-11": "Freighter conversion", "T-12": "Higher utilisation of mature narrowbodies",
    "T-13": "GTF groundings easing", "T-14": "CFM56 plateau-then-decline and LEAP aftermarket parity",
}
row_lines = ["| Row | Driver (Part III §24, Exhibit 3.14) | Parts that open by naming the row |", "|---|---|---|"]
for i in range(1, 15):
    t = f"T-{i}"
    ps = sorted(row_map.get(t, []), key=lambda x: ROMAN_ORDER[x])
    cell = ", ".join(f"Part {p}" for p in ps) if ps else "none"
    row_lines.append(f"| {t} | {ROW_LABELS[t]} | {cell} |")
ROWTABLE = "\n".join(row_lines)
if DEBUG:
    print("row map:", {k: sorted(v, key=lambda x: ROMAN_ORDER[x]) for k, v in sorted(row_map.items(), key=lambda kv: int(kv[0][2:]))})

# ---------------------------------------------------------------- Company index
# (display name, ticker, role, regex)
COMPANIES = [
 # FTAI entities and vehicles
 ("FTAI Aviation Ltd.", "NASDAQ: FTAI", "The subject of the primer: Cayman-incorporated owner of the Aerospace Products and Aviation Leasing segments, the Strategic Capital Initiative and FTAI Power.", r"\bFTAI\b"),
 ("FTAI Infrastructure Inc.", "NASDAQ: FIP", "The infrastructure businesses spun off to shareholders on 1 August 2022; appears only as history.", r"FTAI Infrastructure|\bFIP\b"),
 ("FTAI Power", "", "FTAI's power platform launched 30 December 2025; builds the Mod-1 generator set around a CFM56 core.", r"FTAI Power"),
 ("FTAI Finance Holdco Ltd.", "", "FTAI finance subsidiary and note co-issuer named in SEC filings; role not fully retrieved.", r"FTAI Finance Holdco"),
 ("FTAI MRE 2026-1", "", "The 2025 Partnership's inaugural asset-backed securitization, priced 22 May 2026 ($612M of notes on 48 aircraft).", r"FTAI MRE 2026-1|Inaugural Asset-Backed Securitization|inaugural asset-backed securitization"),
 ("Fortress Transportation and Infrastructure Investors LLC", "", "FTAI's predecessor, listed on the NYSE in May 2015 and externally managed by Fortress.", r"Fortress Transportation"),
 ("Fortress Investment Group / FIG LLC", "", "FTAI's external manager until the internalization of 28 May 2024.", r"Fortress Investment|FIG LLC|\bFortress\b"),
 ("Master GP", "", "Fortress affiliate that received the incentive allocation under the pre-2024 management structure.", r"Master GP"),
 ("Strategic Capital Initiative (SCI)", "", "FTAI's asset-management arm, launched 30 December 2024, raising third-party vehicles that buy mid-life 737NG and A320ceo aircraft.", r"Strategic Capital Initiative|\bSCI\b"),
 ("2025 Partnership (FTAI SCI I)", "", "The first Strategic Capital vehicle: $2.0B equity hard cap, $2.5B asset-level debt, about $6B across 300-plus aircraft; FTAI is Servicer and 19% LP.", r"2025 Partnership|2025 SPV|SCI I\b|inaugural Strategic Capital vehicle"),
 ("2026 SPV (SCI II)", "", "The second Strategic Capital vehicle, with a $2.0B warehouse facility from 13 lenders closed 14 August 2026.", r"2026 SPV|SCI II\b|second investment vehicle|Second Investment Vehicle"),
 ("Module Factory (Montréal)", "", "FTAI's module repair and refurbishment programme and site; the operating heart of Aerospace Products.", r"Module Factory"),
 ("Lockheed Martin Commercial Engine Solutions (LMCES)", "", "The 526,000 sq ft Montréal engine shop FTAI bought from Lockheed Martin Canada on 9 September 2024 for $170.0M.", r"LMCES|Lockheed Martin Commercial Engine Solutions"),
 ("Lockheed Martin Corporation", "NYSE: LMT", "Seller of the Montréal shop through Lockheed Martin Canada.", r"Lockheed Martin\b(?! Commercial)"),
 ("QuickTurn (Miami)", "", "FTAI's Miami engine maintenance business, formed from iAero Thrust assets in 2023.", r"QuickTurn(?! Europe)"),
 ("QuickTurn Europe", "", "50%-owned, equity-method CFM56 shop at Rome Fiumicino (former IAG Engine Center), closed 5 June 2025.", r"QuickTurn Europe"),
 ("iAero Thrust", "", "The Miami engine business whose assets FTAI and Unical acquired on 4 January 2023.", r"iAero"),
 ("Unical Aviation", "", "USM trader; FTAI's former joint-venture partner in QuickTurn Miami (interest bought out 1 December 2023).", r"Unical"),
 ("Prime Engine Accessories", "", "50/50 accessory-repair joint venture with Bauer, Inc. in Bristol, Connecticut.", r"Prime Engine Accessories|Bristol"),
 ("Bauer, Inc.", "", "FTAI's partner in Prime Engine Accessories.", r"\bBauer\b"),
 ("Advanced Engine Repair JV", "", "A 25% equity-method investment ($22.4M carrying value at 31 Dec 2025); whether it is the Chromalloy PMA venture is unresolved.", r"Advanced Engine Repair"),
 ("FTAI–Chromalloy joint venture (PMA JV)", "", "The joint venture through which FTAI develops and manufactures PMA parts; terms not disclosed in retrieved filings.", r"FTAI[–-]Chromalloy|Chromalloy (JV|joint venture)|PMA (JV|joint venture)"),
 ("J&F Power Systems LLC", "", "FTAI's joint venture with Jereh Group for packaging and distribution of Mod-1; counterparty to the $1.465B order of 22 July 2026.", r"J&amp;F|J&F"),
 ("Jefferson Terminal", "", "Infrastructure business spun off with FTAI Infrastructure in 2022; history only.", r"Jefferson Terminal"),
 ("Repauno", "", "Infrastructure business spun off in 2022; history only.", r"Repauno"),
 ("Transtar", "", "Short-line railroad business spun off in 2022; history only.", r"Transtar"),
 ("Long Ridge", "", "Power and terminal business spun off in 2022; history only.", r"Long Ridge"),
 # OEMs and airframers
 ("CFM International", "", "50/50 joint venture of GE Aerospace and Safran; OEM and type-certificate holder of the CFM56 and LEAP.", r"CFM International|\bCFM\b"),
 ("GE Aerospace", "NYSE: GE", "CFM partner; builds the CFM56 core; Commercial Engines & Services segment; TrueChoice services. Formerly GE Aviation.", r"GE Aerospace|GE Aviation|General Electric|\bGE\b(?! Vernova)"),
 ("Safran SA", "Euronext Paris: SAF", "CFM partner through Safran Aircraft Engines; builds the fan, booster, LPT and gearbox; Propulsion services revenue carried in Part XI.", r"Safran"),
 ("IAE International Aero Engines", "", "Consortium (Pratt & Whitney, P&W Aero Engines International, JAEC, MTU) that is the OEM of the V2500.", r"\bIAE\b|International Aero Engines"),
 ("Pratt & Whitney", "", "RTX engine unit: GTF and V2500 maker; EngineWise aftermarket brand.", r"Pratt (&|&amp;|and) Whitney|P&amp;W|P&W"),
 ("RTX Corporation", "NYSE: RTX", "Parent of Pratt & Whitney; disclosed the GTF powder-metal issue in 2023.", r"\bRTX\b"),
 ("MTU Aero Engines AG", "Xetra: MTX", "IAE partner and independent MRO (MTU Maintenance); reports commercial maintenance on an adjusted EBIT basis.", r"MTU Aero Engines|\bMTU\b(?! Maintenance)"),
 ("MTU Maintenance", "", "MTU's engine MRO arm, independent on the CFM56; also MTU Maintenance Lease Services.", r"MTU Maintenance"),
 ("Japanese Aero Engines Corporation (JAEC)", "", "IAE consortium member.", r"JAEC|Japanese Aero"),
 ("Rolls-Royce", "LSE: RR", "Former IAE shareholder (32.5% per Aircraft Commerce, 2010) whose exit was not retrieved; parent of the engine lessor RRPF.", r"Rolls-Royce"),
 ("Boeing", "NYSE: BA", "Airframer of the 737NG and 737 MAX; subject of the FAA production rate cap; Boeing Converted Freighter programme.", r"Boeing"),
 ("Airbus SE", "Euronext Paris: AIR", "Airframer of the A320ceo and A320neo families; delivery shortfall and gliders treated in Part III.", r"Airbus"),
 ("Embraer", "NYSE: ERJ", "Airframer of the E2 family, powered by the GTF.", r"Embraer"),
 # Power
 ("GE Vernova", "NYSE: GEV", "Frame and aeroderivative gas-turbine maker; 116 GW backlog plus reservations at Q2 2026.", r"GE Vernova"),
 ("Siemens Energy", "Xetra: ENR", "Gas-turbine maker; lead times of three-plus years cited in Part IX.", r"Siemens Energy"),
 ("Mitsubishi Power", "", "Frame gas-turbine maker; 35 GW backlog cited in Part IX.", r"Mitsubishi"),
 ("Solar Turbines (Caterpillar)", "", "Industrial gas-turbine maker (Titan 350) named among competing supply.", r"Solar Turbines"),
 ("Caterpillar Inc.", "NYSE: CAT", "Gas-genset and reciprocating-engine maker named among competing supply.", r"Caterpillar"),
 ("Wärtsilä", "Nasdaq Helsinki: WRT1V", "Maker of large reciprocating gas engines competing for data-center power.", r"W[äa]rtsil[äa]"),
 ("Bloom Energy", "NYSE: BE", "Solid-oxide fuel-cell maker named among competing supply.", r"Bloom Energy"),
 ("ProEnergy", "", "Aeroderivative packager (PE6000 from CF6-80C2 cores) whose customers plan five to seven years of bridging power.", r"ProEnergy"),
 ("Baker Hughes", "NASDAQ: BKR", "Maker of the NovaLT small industrial turbine line, noted as not aeroderivative.", r"Baker Hughes"),
 ("Jereh Group", "SZSE: 002353", "Chinese oilfield-equipment maker and mobile gas-turbine packager; FTAI's partner in J&F Power Systems.", r"Jereh"),
 ("GenSystems", "", "Jereh subsidiary with $182M and $341M US data-center turbine orders.", r"GenSystems"),
 ("xAI", "", "Operator of the Memphis data center whose trailer-mounted turbines tested the nonroad-engine permitting question.", r"\bxAI\b"),
 # Shops and MROs
 ("StandardAero, Inc.", "NYSE: SARO", "Independent engine MRO; CFM56-7B Center of Excellence in Dallas; Engine Services and Component Repair Services segments.", r"StandardAero"),
 ("Lufthansa Technik", "", "MRO segment of Deutsche Lufthansa; engine services almost half of revenue; adjusted EBIT basis.", r"Lufthansa Technik|\bLHT\b"),
 ("Deutsche Lufthansa AG", "Xetra: LHA", "Parent of Lufthansa Technik.", r"Deutsche Lufthansa|Lufthansa\b(?! Technik)"),
 ("ST Engineering", "SGX: S63", "Singapore engineering group with an engine MRO arm named among independents.", r"ST Engineering"),
 ("GMF AeroAsia", "IDX: GMFI", "Garuda Indonesia's MRO arm; capacity partner of FTAI (Indonesia).", r"GMF AeroAsia|\bGMF\b"),
 ("Garuda Indonesia", "IDX: GIAA", "Parent of GMF AeroAsia.", r"Garuda"),
 ("EgyptAir Maintenance & Engineering", "", "Airline MRO; capacity partner of FTAI (Egypt); buyer of GE overhaul consulting.", r"EgyptAir"),
 ("Delta TechOps", "", "Delta Air Lines' MRO arm, named among airline shops.", r"Delta TechOps"),
 ("Delta Air Lines", "NYSE: DAL", "CFM56 operator affected by the AOG Technics unapproved-parts episode.", r"Delta Air Lines|\bDelta\b(?! TechOps)"),
 ("AFI KLM E&M", "", "Air France Industries KLM Engineering & Maintenance, named among airline MROs.", r"AFI KLM|Air France"),
 ("Turkish Technic", "", "Turkish Airlines' MRO arm, named among airline MROs.", r"Turkish Technic"),
 ("Turkish Airlines", "BIST: THYAO", "Parent of Turkish Technic; named for grounding more than 40 aircraft in the GTF episode.", r"Turkish Airlines"),
 ("SR Technics", "", "Independent MRO; its 2026 CFM56-7B price catalogue is cited as a possible source.", r"SR Technics"),
 ("Aero Norway", "", "Independent CFM56 shop; buyer of GE repair management.", r"Aero Norway"),
 ("Magnetic Group (Magnetic MRO)", "", "Independent MRO and trader quoted on CFM56 market conditions.", r"Magnetic"),
 ("FL Technics", "", "Independent MRO named in Part IV.", r"FL Technics"),
 ("IAG Engine Center (International Airlines Group)", "LSE: IAG", "Former operator of the Rome Fiumicino shop that became QuickTurn Europe.", r"\bIAG\b|International Airlines Group"),
 ("Tarmac Aerosave", "", "Storage and dismantling facility at Toulouse-Francazal.", r"Tarmac Aerosave"),
 # Parts, USM, PMA
 ("AAR Corp", "NYSE: AIR", "Distribution, USM and MRO company; exclusive Serviceable Engine Products partner for FTAI's CFM56 pool through 2030.", r"\bAAR\b"),
 ("AJW Group", "", "Parts and engine services company whose records mini-packs are cited.", r"\bAJW\b"),
 ("AerSale Corporation", "NASDAQ: ASLE", "Listed teardown and USM company; Asset Management Solutions gross margin.", r"AerSale"),
 ("GA Telesis", "", "USM, MRO and leasing group named among the players.", r"GA Telesis"),
 ("VAS Aero Services", "", "USM trader named among the players.", r"VAS Aero"),
 ("APOC Aviation", "", "Engine lessor and up-cycler named in Part V.", r"\bAPOC\b"),
 ("Setna iO", "", "USM trader named in Part V.", r"Setna"),
 ("Willis Aero", "", "The parts arm of Willis Lease Finance.", r"Willis Aero"),
 ("AerCap Materials", "", "AerCap's used-material arm; dismantled more than 300 aircraft in 2023.", r"AerCap Materials"),
 ("Aviation Fleet Support", "", "Parts dealer whose core LLP package listing is cited in Parts I and V.", r"Aviation Fleet Support"),
 ("HEICO Corporation (Flight Support Group)", "NYSE: HEI", "Largest independent PMA business; FSG operating margin carried in Part XI.", r"HEICO"),
 ("Wencor Group", "", "PMA and distribution company acquired by HEICO in 2023.", r"Wencor"),
 ("Chromalloy", "", "Turbine-part repair, casting and PMA company; holder of the only FAA PMA HPT blade for the CFM56-5B/-7B; FTAI's PMA partner.", r"Chromalloy(?! (JV|joint venture))"),
 ("BELAC", "", "Chromalloy's early hot-section PMA venture (CFM56-3 HPT blade).", r"BELAC"),
 ("Sequa Corporation", "", "Chromalloy's parent holding company.", r"Sequa"),
 ("Veritas Capital", "", "Private-equity owner of Chromalloy since December 2022.", r"Veritas"),
 ("Global Material Solutions", "", "Historical Pratt & Whitney CFM56-3 PMA venture, found only via headlines.", r"Global Material Solutions"),
 ("AOG Technics", "", "Supplier of parts with forged documentation found on CFM56s in 2023.", r"AOG Technics"),
 ("Howmet Aerospace", "NYSE: HWM", "Casting and forging supplier whose commentary could resolve lead-time unknowns.", r"Howmet"),
 ("Precision Castparts (PCC)", "", "Casting and forging supplier named with Howmet.", r"Precision Castparts|\bPCC\b"),
 # Lessors and capital
 ("Willis Lease Finance Corporation", "NASDAQ: WLFC", "Pure-play engine lessor; WEST securitizations; peer in Part XI.", r"Willis Lease|WLFC|\bWillis\b(?! Aero| Engine Structured)"),
 ("Willis Engine Structured Trust (WEST)", "", "Willis Lease's series of rated engine ABS vehicles (WEST VIII, WEST IX).", r"\bWEST\b|Willis Engine Structured Trust"),
 ("AerCap Holdings N.V.", "NYSE: AER", "Largest aircraft lessor; 20-F filer; peer in Part XI.", r"AerCap(?! Materials)"),
 ("Air Lease Corporation", "formerly NYSE: AL", "New-aircraft lessor taken private as Sumisho Air Lease Corporation on 8 April 2026; peer in Part XI.", r"Air Lease"),
 ("Sumisho Air Lease Corporation", "", "Surviving entity after Air Lease's take-private.", r"Sumisho"),
 ("GECAS", "", "GE's former aircraft-leasing arm; the 2019 GE Aviation and GECAS investor day is a source for fleet figures.", r"GECAS"),
 ("SMBC Aero Engine Lease", "", "Engine lessor named among the engine lessors whose scale was not retrieved.", r"SMBC"),
 ("Engine Lease Finance Corporation (ELFC)", "", "Engine lessor whose 2016 statement on PMA in return conditions is cited.", r"Engine Lease Finance|ELFC|\bELF\b"),
 ("Rolls-Royce & Partners Finance (RRPF)", "", "Engine lessor named among engine lessors.", r"RRPF|Rolls-Royce (&|&amp;|and) Partners"),
 ("GE Engine Leasing", "", "GE's engine-leasing arm named among engine lessors.", r"GE Engine Leasing"),
 ("Shannon Engine Support (SES)", "", "AerCap's 50% engine-leasing joint venture with Safran Aircraft Engines.", r"Shannon Engine Support|\bSES\b"),
 ("Avolon", "", "Aircraft lessor named in Part VI among those from which no current return-condition statement was retrieved.", r"Avolon"),
 ("Carlyle Aviation Partners (The Carlyle Group)", "NASDAQ: CG", "Aviation investment manager; fee comparable for the Strategic Capital vehicles.", r"Carlyle"),
 ("Castlelake", "", "Aviation investment manager named as a comparable not reached.", r"Castlelake"),
 ("Apollo Global Management / Merx Aviation", "NYSE: APO", "Apollo's structured-products business ATLAS SP led the 2025 Partnership's debt; Merx is its aviation platform.", r"Apollo|Merx"),
 ("ATLAS SP Partners", "", "Structuring agent and lead arranger of the $2.5B asset-level debt commitment (February 2025).", r"ATLAS SP"),
 ("Deutsche Bank AG", "NYSE: DB", "Co-lender on the 2025 Partnership's asset-level debt.", r"Deutsche Bank"),
 ("OneIM (One Investment Management)", "", "Partner on the inaugural Strategic Capital vehicle, announced 25 March 2025.", r"OneIM|One Investment Management"),
 ("Blackbird Capital I and II", "", "Air Lease's third-party-capital funds.", r"Blackbird"),
 ("Thunderbolt", "", "Air Lease's mid-life portfolio-sale platform.", r"Thunderbolt"),
 ("Onex", "", "Owner of WestJet.", r"\bOnex\b"),
 # Airlines
 ("Southwest Airlines", "NYSE: LUV", "CFM56-7B operator; TrueChoice Flight Hour reference customer.", r"Southwest"),
 ("Ryanair", "NASDAQ: RYAAY", "CFM56-7B operator with a TrueChoice Material agreement covering about 2,000 engines.", r"Ryanair"),
 ("United Airlines", "NASDAQ: UAL", "737NG operator retiring aircraft; affected by the AOG Technics episode.", r"United Airlines|\bUnited\b(?=,| Airlines| and | retire| has | began | is | was |'s|’s)"),
 ("American Airlines", "NASDAQ: AAL", "CFM56 operator affected by the AOG Technics episode.", r"American Airlines"),
 ("WestJet", "", "Canadian airline; sold 27 737-700s to FTAI and the 2026 SPV on 28 September 2026.", r"WestJet"),
 ("Copa Airlines", "NYSE: CPA", "737NG operator retiring aircraft, named as a counter-case.", r"\bCopa\b"),
 ("Spirit Airlines", "", "A320ceo operator whose 10-K language on maintenance reserves is quoted in Part II; its fleet plan is cited as a source not read.", r"Spirit Airlines|Spirit Aviation|Spirit's"),
 ("JetBlue Airways", "NASDAQ: JBLU", "Airline whose 10-K fleet plan is cited as a source not read.", r"JetBlue"),
 ("Frontier Airlines", "NASDAQ: ULCC", "Airline whose 10-K fleet plan is cited as a source not read.", r"Frontier\b"),
 ("Condor", "", "German airline; lessee of an APOC CFM56-5A engine.", r"\bCondor\b"),
 ("Wizz Air", "LSE: WIZZ", "GTF operator named for its A321ceo phase-out plan and its compensation agreement with Pratt & Whitney.", r"Wizz"),
 # Appraisers, data and trade bodies
 ("IBA", "", "Appraiser; engine values, lease rates and conversion-oversupply warning cited throughout.", r"\bIBA\b"),
 ("mba Aviation", "", "Appraiser named among value sources.", r"mba Aviation|\bmba\b"),
 ("Cirium (Ascend by Cirium)", "", "Fleet-data and appraisal provider; retirement counts, extension shares and the Global Replacement Ratio.", r"Cirium|Ascend"),
 ("AVITAS", "", "Appraiser named among value sources.", r"AVITAS"),
 ("ISTAT", "", "International Society of Transport Aircraft Trading; standardises appraisal terms such as half-life.", r"ISTAT"),
 ("Visual Approach Analytics", "", "Analytics firm forecasting the 2027 peak in CFM56 and V2500 first shop visits.", r"Visual Approach"),
 ("Acumen Aviation", "", "Consultancy cited on retirements and freighter conversion.", r"Acumen"),
 ("Aerodynamic Advisory", "", "Consultancy cited at the IATA Maintenance Cost Conference on retirements and part-outs.", r"Aerodynamic Advisory"),
 ("Forecast International", "", "Forecasting firm cited on shop-visit demand.", r"Forecast International"),
 ("Aviation Suppliers Association", "", "Trade association cited on parts documentation.", r"Aviation Suppliers Association"),
 ("IATA", "", "International Air Transport Association; complainant in the 2018 CFM Conduct Policies settlement; Maintenance Cost Conference.", r"\bIATA\b"),
 # Consultancies and market-research vendors
 ("Oliver Wyman", "", "Consultancy; MRO forecasts and labour-rate inflation figures.", r"Oliver Wyman"),
 ("Bain & Company", "", "Consultancy; slot-wait and capacity-shortfall figures.", r"\bBain\b"),
 ("McKinsey & Company", "", "Consultancy; retirement-rate normalisation from 2028.", r"McKinsey"),
 ("Safe Fly Aviation", "", "Consultancy blog; CFM56 market figures carried with that label throughout.", r"Safe Fly|SafeFly"),
 ("IMARC", "", "Market-research vendor; PMA market size.", r"IMARC"),
 ("Fortune Business Insights", "", "Market-research vendor; USM market size.", r"Fortune Business"),
 ("Market.us", "", "Market-research vendor; USM market size.", r"Market\.us"),
 ("The Business Research Company", "", "Market-research vendor; USM market size.", r"Business Research Company"),
 ("Global Industry Analysts", "", "Market-research vendor; PMA market size (2022).", r"Global Industry Analysts"),
 ("Global Information Inc. (GII)", "", "Report reseller listing an engine PMA and DER forecast.", r"\bGII\b"),
 ("Persistence Market Research", "", "Market-research vendor cited in Part VI.", r"Persistence Market"),
 ("Wood Mackenzie", "", "Energy consultancy; gas-turbine order and capacity comparison.", r"Wood Mackenzie"),
 ("Industrial Info Resources", "", "Industrial data provider cited in Part IX.", r"Industrial Info"),
 ("Argus Media", "", "Price-reporting agency cited in Part III.", r"Argus"),
 ("Crossroads Capital", "", "Investor whose letter on FTAI is cited in Parts VII and X.", r"Crossroads Capital"),
 ("Komodo Capital", "", "Investor blog cited on the Chromalloy PMA release.", r"Komodo Capital"),
 ("Kairos Research", "", "Investor blog cited on the Chromalloy PMA release.", r"Kairos Research"),
 ("Wolfe Research", "", "Sell-side firm quoted after the January 2025 short report.", r"Wolfe Research"),
 ("Bernstein", "", "Broker whose Strategic Decisions Conference hosted GE Aerospace's 27 May 2026 presentation.", r"Bernstein"),
 ("Muddy Waters Research", "", "Short seller that published the 15 January 2025 report on FTAI.", r"Muddy Waters"),
 # Regulators, courts, public bodies, exchanges
 ("Federal Aviation Administration (FAA)", "", "US regulator: type and production certificates, PMA, DER, Part 145, the 737 MAX rate cap.", r"\bFAA\b|Federal Aviation Administration"),
 ("European Union Aviation Safety Agency (EASA)", "", "EU regulator; Form 1; PMA acceptance under the bilateral.", r"\bEASA\b"),
 ("US Securities and Exchange Commission (SEC)", "", "Regulator receiving FTAI's filings; EDGAR is the primer's filing source.", r"\bSEC\b|Securities and Exchange Commission"),
 ("UK Civil Aviation Authority", "", "Regulator whose PMA acceptance is an open question.", r"UK CAA"),
 ("Transport Canada (TCCA)", "", "Regulator whose PMA acceptance is an open question.", r"TCCA|Transport Canada"),
 ("ANAC (Brazil)", "", "Regulator whose PMA acceptance is an open question.", r"\bANAC\b"),
 ("CAAC (China)", "", "Regulator whose PMA acceptance is an open question.", r"\bCAAC\b"),
 ("DGCA India", "", "Regulator whose PMA acceptance is an open question.", r"\bDGCA\b"),
 ("European Commission", "", "Recipient of IATA's 2018 complaint settled by CFM's Conduct Policies.", r"European Commission"),
 ("US District Court, Southern District of New York", "", "Court hearing the securities class action No. 25-cv-00541 (Judge Jeannette A. Vargas).", r"S\.D\.N\.Y|Southern District of New York"),
 ("Shelby County Health Department", "", "Tennessee permitting authority that accepted the nonroad-engine reading for xAI's Memphis turbines.", r"Shelby County"),
 ("PJM Interconnection", "", "Mid-Atlantic grid operator; interconnection queue.", r"\bPJM\b"),
 ("ERCOT", "", "Texas grid operator; interconnection queue.", r"ERCOT"),
 ("International Energy Agency (IEA)", "", "Source of the data-center electricity forecast (about 945 TWh by 2030).", r"\bIEA\b|International Energy Agency"),
 ("US Patent and Trademark Office", "", "Cited in Part IX.", r"Patent and Trademark|USPTO"),
 ("Nasdaq", "", "FTAI's listing exchange since the 2022 redomiciliation.", r"Nasdaq|NASDAQ"),
 ("New York Stock Exchange (NYSE)", "", "FTAI's predecessor's listing exchange (2015); several peers' exchange.", r"\bNYSE\b|New York Stock Exchange"),
 ("Southern Environmental Law Center", "", "Challenger of the nonroad-engine reading in Memphis.", r"Southern Environmental"),
 ("NAACP", "", "Challenger of the nonroad-engine reading in Memphis.", r"NAACP"),
 # Law firms, auditors, rating agencies, shareholders
 ("Kessler Topaz Meltzer & Check", "", "Plaintiffs' law firm whose case page is the source for the class-action status.", r"Kessler Topaz|ktmc"),
 ("Robbins Geller Rudman & Dowd", "", "Plaintiffs' law firm whose case page is the source for the class-action status.", r"Robbins Geller|rgrdlaw"),
 ("Bleichmar Fonti & Auld (BFA Law)", "", "Plaintiffs' law firm cited on the class action.", r"BFA Law|Bleichmar"),
 ("Ernst & Young LLP", "", "FTAI's auditor 2016 to 2025.", r"Ernst (&|&amp;|and) Young|\bEY\b"),
 ("KPMG LLP", "", "Engaged as FTAI's auditor for FY2025, effective 17 June 2025.", r"KPMG"),
 ("KBRA (Kroll Bond Rating Agency)", "", "Rating agency on the WEST deals and FTAI MRE 2026-1.", r"KBRA|Kroll"),
 ("Fitch Ratings", "", "Rating agency on FTAI MRE 2026-1.", r"Fitch"),
 ("Moody's", "NYSE: MCO", "Rating agency whose FTAI ratings were not retrieved.", r"Moody"),
 ("S&P Global", "NYSE: SPGI", "Rating agency whose FTAI ratings were not retrieved.", r"S&amp;P|S&P"),
 ("Capital Group (Capital International Investors; Capital World Investors)", "", "FTAI's two largest reported shareholders (13.51% and 12.43%).", r"Capital International|Capital World|Capital Group"),
 ("The Vanguard Group", "", "FTAI shareholder (10.10%).", r"Vanguard"),
 ("FMR LLC", "", "FTAI shareholder (5.25%).", r"\bFMR\b"),
 # Conversion houses
 ("AEI (Aeronautical Engineers, Inc.)", "", "Freighter-conversion house (625-plus conversions); July 2026 collaboration with FTAI.", r"\bAEI\b|Aeronautical Engineers"),
 ("Israel Aerospace Industries (IAI)", "", "Freighter-conversion house named with AEI and Boeing.", r"\bIAI\b|Israel Aerospace"),
 # Publishers and data services
 ("Aviation Week", "", "Trade publication; the most-cited press source in the primer.", r"Aviation Week"),
 ("Leeham News", "", "Trade publication covering OEM results and engine technology.", r"Leeham"),
 ("Aircraft Commerce", "", "Trade publication; maintenance analyses and owner's guides for the CFM56.", r"Aircraft Commerce"),
 ("Cargo Facts", "", "Trade publication on freighter conversion.", r"Cargo Facts"),
 ("AviTrader", "", "Trade publication.", r"AviTrader"),
 ("Aviation Business News", "", "Trade publication.", r"Aviation Business News"),
 ("Air Cargo Week", "", "Trade publication; shop-visit cost breakdown.", r"Air Cargo Week"),
 ("Aircraft Value News", "", "Trade publication on values and lease rates.", r"Aircraft Value News"),
 ("ePlaneAI", "", "Trade and market commentary site.", r"ePlaneAI"),
 ("FlightGlobal", "", "Trade publication.", r"Flight ?Global"),
 ("CAPA (Centre for Aviation)", "", "Trade publication and data provider.", r"\bCAPA\b|Centre for Aviation"),
 ("Air Data News", "", "Trade publication cited on Airbus deliveries.", r"Air Data News"),
 ("AVM Magazine", "", "Trade publication cited on used-material supply.", r"\bAVM\b"),
 ("Power Engineering", "", "Energy trade publication.", r"Power Engineering"),
 ("Gas Turbine World", "", "Energy trade publication and handbook.", r"Gas Turbine World"),
 ("Data Center Dynamics", "", "Data-center trade publication.", r"Data Center Dynamics"),
 ("Utility Dive", "", "Energy trade publication.", r"Utility Dive"),
 ("E&E News", "", "Energy and environment news service.", r"E&amp;E News|E&E News"),
 ("Oilprice.com", "", "Energy news site.", r"Oilprice"),
 ("Tennessee Lookout", "", "News site covering the Memphis turbine permitting dispute.", r"Tennessee Lookout"),
 ("In Practise", "", "Interview publisher; FTAI module-swap interviews located but not read.", r"In Practise"),
 ("GuruFocus", "", "Call-coverage aggregator; source of several call figures labelled as such.", r"GuruFocus"),
 ("MarketBeat", "", "Call-coverage aggregator; source of several call figures labelled as such.", r"MarketBeat"),
 ("Quartr", "", "Call and capital-markets-day summary service.", r"Quartr"),
 ("Barchart", "", "Financial news site carrying FTAI releases.", r"Barchart"),
 ("Finviz", "", "Financial news site carrying FTAI releases.", r"Finviz"),
 ("StreetInsider", "", "Financial news site carrying FTAI's CFO release.", r"StreetInsider"),
 ("Seeking Alpha", "", "Investment commentary site.", r"Seeking Alpha"),
 ("Motley Fool", "", "Investment commentary site; call transcripts.", r"Motley Fool"),
 ("Insider Monkey", "", "Investment commentary site; call transcripts.", r"Insider Monkey"),
 ("Hedge Fund Alpha", "", "Investment commentary site cited on the short report.", r"Hedge Fund Alpha"),
 ("TipRanks / The Fly", "", "Financial news service cited on the short report and sell-side reaction.", r"TipRanks|The Fly\b"),
 ("Benzinga", "", "Financial news site cited on the short report.", r"Benzinga"),
 ("Bloomberg", "", "Financial news service.", r"Bloomberg"),
 ("PR Newswire", "", "Press-release distributor (AAR, Chromalloy releases).", r"PR ?Newswire"),
 ("GlobeNewswire", "", "Press-release distributor for FTAI's releases.", r"GlobeNewswire"),
 ("Informa Markets", "", "Owner of Aviation Week and the MRO conference series.", r"Informa"),
 ("Asset Securitization Report", "", "Structured-finance publication cited in Part II.", r"Asset Securitization Report"),
 ("Yahoo Finance", "", "Financial news aggregator.", r"Yahoo"),
]

def company_hits(pattern):
    rx = re.compile(pattern)
    out = {}
    for r in ROMAN:
        secs = set()
        for i, ln in enumerate(part_lines[r]):
            if part_secs[r][i] is None:
                continue
            if rx.search(ln):
                secs.add(part_secs[r][i])
        if secs:
            out[r] = sorted([x for x in secs if x != "U"]) + (["U"] if "U" in secs else [])
    return out

def fmt_where(hits):
    chunks = []
    for r in ROMAN:
        if r not in hits:
            continue
        secs = hits[r]
        nums = [x for x in secs if x != "U"]
        if not nums:
            chunks.append(f"Part {r} (unknowns list only)")
        elif len(nums) > 7:
            chunks.append(f"Part {r} §{nums[0]}–§{nums[-1]} ({len(nums)} sections)")
        else:
            chunks.append(f"Part {r} " + ", ".join(f"§{s}" for s in nums))
    return "; ".join(chunks)

comp_rows = []
missing = []
for name, ticker, role, pat in COMPANIES:
    hits = company_hits(pat)
    if not hits:
        missing.append(name)
        continue
    if name.startswith("FTAI Aviation Ltd."):
        where = "Every Part; the company itself is Part X, Aerospace Products Part VII, Aviation Leasing and Strategic Capital Part VIII, FTAI Power Part IX"
    else:
        where = fmt_where(hits)
    nm = esc(name) + (f" ({esc(ticker)})" if ticker else "")
    comp_rows.append((sort_key(name), f"| {nm} | {esc(role)} | {where} |"))
comp_rows.sort()
COMPANIES_TABLE = "\n".join(["| Company, vehicle or institution (ticker where listed) | Role in the primer | Where it appears |", "|---|---|---|"] + [c[1] for c in comp_rows])
n_companies = len(comp_rows)
if DEBUG:
    print(f"company index: {n_companies} entries; missing (no hits): {missing}")

# ---------------------------------------------------------------- Unknowns register
rec = open(os.path.join(ROOT, "research", "reconciliation.md"), encoding="utf-8").read().split("\n")
d1s = next(i for i, l in enumerate(rec) if l.startswith("### D.1"))
d2s = next(i for i, l in enumerate(rec) if l.startswith("### D.2"))
d3s = next(i for i, l in enumerate(rec) if l.startswith("### D.3"))
d_end = next(i for i, l in enumerate(rec) if l.startswith("## E."))

entries = collections.OrderedDict()
for ln in rec[d1s:d2s]:
    m = re.match(r"- \*\*(U-D\d+-\d+)\*\* \((D\d+)\) — (.*)$", ln.strip())
    if m:
        entries[m.group(1)] = dict(id=m.group(1), dossier=m.group(2), text=m.group(3).strip())
n_unknowns = len(entries)

clusters = []
for ln in rec[d2s:d3s]:
    m = re.match(r"\*\*(K-\d+) — (.*?)\*\* Ids: (.*?)\. Verbatim: (.*)$", ln.strip())
    if m:
        kid, title, ids, rest = m.groups()
        ids = re.findall(r"U-D\d+-\d+", ids)
        raised = re.search(r"Raised by (.*?)\. Rationale:", rest)
        rationale = re.search(r"Rationale: (.*?)(?= Partly closed| Known:| Would resolve| Related, not merged:|$)", rest)
        partly = re.search(r"(Partly closed[^:]*:.*?)(?= Would resolve| Related, not merged:|$)", rest)
        known = re.search(r"(Known: .*?)(?= Would resolve| Related, not merged:|$)", rest)
        resolve = re.search(r"Would resolve(?: for the remainder)?: (.*?)(?= Related, not merged:|$)", rest)
        related = re.search(r"Related, not merged: (.*)$", rest)
        clusters.append(dict(id=kid, title=title.rstrip("."), ids=ids,
                             raised=raised.group(1) if raised else "", rationale=rationale.group(1).strip() if rationale else "",
                             partly=(partly.group(1).strip() if partly else (known.group(1).strip() if known else "")),
                             resolve=resolve.group(1).strip() if resolve else "", related=related.group(1).strip() if related else ""))
clustered_ids = {i for c in clusters for i in c["ids"]}

# which Parts carry each id
carried = collections.defaultdict(list)
for r in ROMAN:
    lines = part_lines[r]
    try:
        s = next(i for i, l in enumerate(lines) if l.startswith("## Unknowns carried in this Part"))
        e = next(i for i in range(s + 1, len(lines)) if lines[i].startswith("## "))
    except StopIteration:
        continue
    for ln in lines[s:e]:
        for uid in set(re.findall(r"U-D\d+-\d+", ln)):
            if r not in carried[uid]:
                carried[uid].append(r)

DOSSIER_PART = {"D1": "I", "D2": "IV", "D3": "V", "D4": "VI", "D5": "VII", "D6": "VIII", "D7": "VIII", "D8": "IX", "D9": "III", "D10": "X", "D11": "XI"}
PART_TITLE = {"I": "Part I, first principles: the CFM56 as a machine (dossier D1)",
              "II": "Part II, first principles: how money moves around an engine (D6 mechanics)",
              "III": "Part III, the context and the translation table (D9)",
              "IV": "Part IV, the shop-visit market and the OEM aftermarket (D2)",
              "V": "Part V, used serviceable material and teardown (D3)",
              "VI": "Part VI, PMA parts and DER repairs (D4)",
              "VII": "Part VII, FTAI Aerospace Products (D5)",
              "VIII": "Part VIII, FTAI Aviation Leasing and the Strategic Capital Initiative (D6 FTAI sections, D7)",
              "IX": "Part IX, FTAI Power (D8)",
              "X": "Part X, FTAI the company (D10)",
              "XI": "Part XI, markets and money: margin pools and peers (D11)"}

def owner_part(e):
    d = e["dossier"]
    p = DOSSIER_PART[d]
    if d == "D6":
        c = carried.get(e["id"], [])
        if "II" in c and "VIII" not in c:
            return "II"
    return p

def md_entry(e, with_carried=True):
    txt = e["text"]
    s = f"- **{e['id']}** ({e['dossier']}) — {txt}"
    if with_carried:
        c = carried.get(e["id"], [])
        if c:
            s += f" *Carried in {'Part' if len(c)==1 else 'Parts'} {', '.join(c)}.*"
        else:
            s += " *Not carried in any Part's unknowns list.*"
    return s

uk_lines = []
uk_lines.append("### 94.1 Clusters: entries that ask the same question")
uk_lines.append("")
uk_lines.append(f"The reconciliation found {len(clusters)} clusters covering {len(clustered_ids)} of the {n_unknowns} entries. Each cluster below gives the verbatim question of every entry in it, the dossiers that raised it, what the research already holds, and what would resolve it. The cluster titles and the resolution notes are the reconciliation's; nothing in the quoted entries has been altered.")
uk_lines.append("")
for c in clusters:
    uk_lines.append(f"#### {c['id']} — {c['title']}")
    uk_lines.append("")
    uk_lines.append(f"Raised by {c['raised']}. Rationale, as the reconciliation states it: {c['rationale']}")
    uk_lines.append("")
    for uid in c["ids"]:
        uk_lines.append(md_entry(entries[uid]))
    uk_lines.append("")
    tail = []
    if c["partly"]:
        tail.append(f"**What the research holds.** {c['partly']}")
    if c["resolve"]:
        tail.append(f"**What would resolve it.** {c['resolve']}")
    if c["related"]:
        tail.append(f"Related, not merged: {c['related']}")
    uk_lines.append(" ".join(tail))
    uk_lines.append("")

uk_lines.append("### 94.2 Singletons, by the Part that owns them")
uk_lines.append("")
single = [e for e in entries.values() if e["id"] not in clustered_ids]
uk_lines.append(f"The remaining {len(single)} entries stand alone. They are grouped by the Part whose dossier raised them (D6 entries on leasing mechanics sit under Part II and D6 entries on FTAI's own fleet under Part VIII, following the Parts' own unknowns lists). The note after each entry says which Parts carry it in their closing unknowns lists.")
uk_lines.append("")
by_part = collections.defaultdict(list)
for e in single:
    by_part[owner_part(e)].append(e)
for p in ROMAN:
    if p not in by_part:
        continue
    uk_lines.append(f"#### {PART_TITLE[p]}: {len(by_part[p])} entries")
    uk_lines.append("")
    for e in by_part[p]:
        uk_lines.append(md_entry(e))
    uk_lines.append("")
UNKNOWNS = "\n".join(uk_lines)
if DEBUG:
    print(f"unknowns: {n_unknowns} entries; clusters {len(clusters)} covering {len(clustered_ids)}; singletons {len(single)}")
    not_carried = [e["id"] for e in entries.values() if not carried.get(e["id"])]
    print("not carried anywhere:", not_carried)
    for c in clusters:
        if not c["resolve"]:
            print("cluster without resolve:", c["id"])

# ---------------------------------------------------------------- Consolidated sources
MONTHS = {m: i + 1 for i, m in enumerate(["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"])}
PUB_NORM = [
    (r"^FTAI Aviation(?: Ltd\.?)?(?: / .*)?$", "FTAI Aviation Ltd."),
    (r"^FTAI Aviation Ltd\.? ?/.*", "FTAI Aviation Ltd."),
    (r"^Willis Lease(?: Finance(?: Corp(?:oration|\.)?)?)?$", "Willis Lease Finance Corporation"),
    (r"^GE Aerospace.*", "GE Aerospace"),
    (r"^HEICO Corp.*", "HEICO Corporation"),
    (r"^AAR Corp.*", "AAR Corp"),
    (r"^Air Lease Corp.*", "Air Lease Corporation"),
    (r"^AerSale.*", "AerSale Corporation"),
    (r"^AerCap.*", "AerCap Holdings N.V."),
    (r"^StandardAero.*", "StandardAero, Inc."),
    (r"^Safran.*", "Safran"),
    (r"^Safe Fly Aviation.*", "Safe Fly Aviation (consultancy blog)"),
    (r"^Aviation Week.*", "Aviation Week"),
    (r"^Leeham News.*", "Leeham News"),
    (r"^FAA.*", "FAA"),
    (r"^FAA–EASA.*", "FAA–EASA"),
    (r"^CFM International.*", "CFM International"),
    (r"^Chromalloy.*", "Chromalloy"),
    (r"^Cargo Facts.*", "Cargo Facts"),
    (r"^IBA.*", "IBA"),
    (r"^MTU.*", "MTU Aero Engines"),
    (r"^Lufthansa Technik.*", "Lufthansa Technik"),
    (r"^PR ?Newswire.*", "PR Newswire"),
    (r"^Aircraft Commerce.*", "Aircraft Commerce"),
    (r"^SEC .*|^U\.?S\.? Securities.*", "SEC"),
    (r"^(Redomiciliation|Spin-off) documents: FTAI.*", "FTAI Aviation Ltd."),
    (r"^General Electric.*|^GE Aviation.*", "GE Aerospace"),
    (r"^RTX / Pratt.*", "RTX / Pratt & Whitney"),
    (r"^Visual Approach.*", "Visual Approach Analytics"),
    (r"^AVM Magazine.*|^Aviation Maintenance [Mm]agazine.*", "AVM Magazine (Aviation Maintenance)"),
    (r"^CAPA.*", "CAPA (Centre for Aviation)"),
    (r"^ISTAT.*", "ISTAT"),
    (r"^BFA Law.*", "BFA Law"),
    (r"^Komodo Capital.*", "Komodo Capital"),
    (r"^(Kessler Topaz|Law-firm case pages).*", "Kessler Topaz Meltzer & Check; Robbins Geller Rudman & Dowd (case pages)"),
    (r"^StockStory.*", "StockStory"),
    (r"^Bloomberg.*", "Bloomberg"),
    (r"^eCFR.*", "eCFR"),
    (r"^Air Cargo Week.*", "Air Cargo Week"),
    (r"^Aviation Business News.*", "Aviation Business News"),
    (r"^IATA.*", "IATA"),
    (r"^Spirit A.*", "Spirit Airlines"),
    (r"^AviTrader.*", "AviTrader"),
    (r"^Oilprice.*", "Oilprice"),
    (r"^Nasdaq\.com.*", "Nasdaq.com"),
]
INTERNAL_RE = re.compile(r"^(Dossier|Dossiers|Internal to the research|Orchestrator|Part I of this primer|Project research|Research dossiers)")

def norm_pub(p):
    p = p.strip().strip('"“”').strip()
    for pat, rep in PUB_NORM:
        if re.match(pat, p, flags=re.I):
            return rep
    return p

def norm_url(u):
    u = u.strip().rstrip(").,;]")
    u = re.sub(r"#.*$", "", u)
    u = re.sub(r"^https?://(www\.)?", "", u, flags=re.I)
    u = re.sub(r"/data/0+(\d+)/", r"/data/\1/", u)
    u = u.rstrip("/")
    return u.lower()

def date_key(text):
    t = text.lower()
    if "undated" in t or "date not" in t:
        return (9998, 13, 32)
    m = re.search(r"(\d{1,2})?\s*(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\.?\s+(20\d\d)", t)
    if m:
        d = int(m.group(1)) if m.group(1) else 0
        return (int(m.group(3)), MONTHS[m.group(2)], d)
    m = re.search(r"\b(20\d\d)[-–](\d\d)[-–](\d\d)\b", t)
    if m:
        return (int(m.group(1)), int(m.group(2)), int(m.group(3)))
    m = re.search(r"\bq([1-4])\s*(?:fy)?(20\d\d)", t)
    if m:
        return (int(m.group(2)), int(m.group(1)) * 3, 0)
    m = re.search(r"\bfy\s?(20\d\d)", t)
    if m:
        return (int(m.group(1)), 12, 31)
    m = re.search(r"\b(20\d\d)\b", t)
    if m:
        return (int(m.group(1)), 0, 0)
    m = re.search(r"\b(19\d\d)\b", t)
    if m:
        return (int(m.group(1)), 0, 0)
    return (9999, 0, 0)

sources = collections.OrderedDict()
for r in ROMAN:
    lines = part_lines[r]
    try:
        s = next(i for i, l in enumerate(lines) if l.startswith("## Sources"))
    except StopIteration:
        continue
    for ln in lines[s + 1:]:
        if ln.startswith("## "):
            break
        m = re.match(r"^\s*(\d+)\.\s+(.*)$", ln)
        if not m:
            continue
        text = m.group(2).strip()
        urls = re.findall(r"https?://[^\s<>\")\]]+", text)
        urls = [u.rstrip(".,;)") for u in urls]
        key = norm_url(urls[0]) if urls else "title:" + norm(re.sub(r"https?://\S+", "", text))[:120]
        desc = re.sub(r"\s*https?://[^\s<>\")\]]+", "", text)
        desc = re.sub(r"(\s*;\s*)+$", "", desc).strip()
        desc = re.sub(r"(\s*;\s*){2,}", "; ", desc)
        desc = re.sub(r"\s+;\s+", "; ", desc)
        desc = re.sub(r"\s{2,}", " ", desc)
        desc = re.sub(r"\(\s*;\s*", "(", desc)
        desc = re.sub(r"\s*;\s*\)", ")", desc)
        if key in sources:
            src = sources[key]
            if r not in src["parts"]:
                src["parts"].append(r)
            if len(desc) < len(src["desc"]) and len(desc) > 20:
                src["desc"] = desc
            for u in urls:
                if norm_url(u) not in [norm_url(x) for x in src["urls"]]:
                    src["urls"].append(u)
        else:
            sources[key] = dict(desc=desc, urls=urls, parts=[r])

for src in sources.values():
    pub = src["desc"].split(",")[0]
    pub = re.sub(r"\s*\(.*?\)\s*$", "", pub).strip() if len(pub) > 40 else pub
    src["pub"] = norm_pub(pub)
    src["date"] = date_key(src["desc"])

def pub_sort(p):
    p = p.lower()
    p = re.sub(r"^(the|a) ", "", p)
    return re.sub(r"[^a-z0-9]", "", p)

all_src = sorted(sources.values(), key=lambda s: (pub_sort(s["pub"]), s["date"], s["desc"].lower()))
internal_list = [s for s in all_src if INTERNAL_RE.match(s["desc"])]
src_list = [s for s in all_src if not INTERNAL_RE.match(s["desc"])]
int_lines = []
for s in internal_list:
    d = esc(s["desc"]).rstrip(".") + "."
    int_lines.append(f"- {d} <span class=\"cite\">Cited in Part{'s' if len(s['parts'])>1 else ''} {', '.join(s['parts'])}.</span>")
INTERNAL = "\n".join(int_lines)
src_lines = []
for i, s in enumerate(src_list, 1):
    d = esc(s["desc"])
    if d and d[-1] not in ".;":
        d += "."
    u = " ; ".join(s["urls"])
    parts = ", ".join(s["parts"])
    src_lines.append(f"{i}. {d} {u} <span class=\"cite\">Cited in Part{'s' if len(s['parts'])>1 else ''} {parts}.</span>")
SOURCES = "\n".join(src_lines)
n_sources = len(src_list)
if DEBUG:
    print(f"sources: {n_sources} unique from {sum(len(s['parts']) for s in src_list)} citations")
    pubs = collections.Counter(s["pub"] for s in src_list)
    with open(os.path.join(OUT, "sources_debug.txt"), "w") as f:
        for s in src_list:
            f.write(f"{s['pub']!r:50} {s['date']} | {s['desc'][:110]} | {s['parts']}\n")
        f.write("\n\nPUBLISHERS\n")
        for p, n in sorted(pubs.items()):
            f.write(f"{n:3} {p}\n")

# ---------------------------------------------------------------- Fill template
tmpl_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "part12-template.md")
if os.path.exists(tmpl_path):
    tmpl = open(tmpl_path, encoding="utf-8").read()
    filled = (tmpl.replace("{{GLOSSARY}}", GLOSSARY)
                  .replace("{{ROWTABLE}}", ROWTABLE)
                  .replace("{{COMPANIES}}", COMPANIES_TABLE)
                  .replace("{{UNKNOWNS}}", UNKNOWNS)
                  .replace("{{SOURCES}}", SOURCES)
                  .replace("{{INTERNAL}}", INTERNAL)
                  .replace("{{N_GLOSSARY}}", str(n_glossary))
                  .replace("{{N_COMPANIES}}", str(n_companies))
                  .replace("{{N_UNKNOWNS}}", str(n_unknowns))
                  .replace("{{N_CLUSTERS}}", str(len(clusters)))
                  .replace("{{N_CLUSTERED}}", str(len(clustered_ids)))
                  .replace("{{N_SINGLE}}", str(len(single)))
                  .replace("{{N_SOURCES}}", str(n_sources))
                  .replace("{{N_CITATIONS}}", str(sum(len(s['parts']) for s in src_list))))
    out_path = os.path.join(ROOT, "parts", "part12-reference.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(filled)
    print(f"wrote {out_path}")
    print(f"counts: glossary={n_glossary} companies={n_companies} unknowns={n_unknowns} (clusters={len(clusters)}, singletons={len(single)}) sources={n_sources}")
else:
    for name, blob in [("glossary.md", GLOSSARY), ("rowtable.md", ROWTABLE), ("companies.md", COMPANIES_TABLE), ("unknowns.md", UNKNOWNS), ("sources.md", SOURCES)]:
        open(os.path.join(OUT, name), "w", encoding="utf-8").write(blob)
    print("no template; wrote blocks to", OUT)
