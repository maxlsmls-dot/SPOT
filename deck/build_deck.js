// FTAI long pitch deck — Global Platinum Securities styling (TATT-inspired minimalism)
// Note: pptxgenjs text margin arrays are ordered [left, right, bottom, top] (pt).
const path = require("path");
const pptxgen = require("pptxgenjs");
const { applyTheme } = require(process.env.PPTX_SKILL + "/scripts/apply_theme.js");

const LOGO = path.join(__dirname, "gps_logo.jpeg");
const OUT = path.join(__dirname, "FTAI_Long_Pitch.pptx");

// Global Platinum Securities palette, sampled from the GPS logo
const NAVY = "0A1C58";
const PLAT = "847C7A";      // platinum gray (logo "PLATINUM" wordmark)
const PLAT_LT = "DCD8D3";   // light platinum (globe highlights) — card fill
const PLAT_XLT = "EFEDEA";  // banner fill

const THEME = {
  name: "Global Platinum Securities",
  headFontFace: "Garamond",
  bodyFontFace: "Garamond",
  colors: {
    dk1: "1A1A1A", lt1: "FFFFFF", dk2: NAVY, lt2: PLAT_XLT,
    accent1: NAVY, accent2: PLAT, accent3: PLAT_LT, accent4: "3B4C82",
    accent5: "B5AEA9", accent6: "5A5350", hlink: NAVY, folHlink: PLAT,
  },
};

const pres = new pptxgen();
pres.defineLayout({ name: "GPS_4x3", width: 10, height: 7.5 });
pres.layout = "GPS_4x3";
pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
pres.title = "FTAI Aviation — Long Recommendation";
pres.company = "Global Platinum Securities";
const C = pres.SchemeColor;

// ---------- Layouts ----------
pres.defineSlideMaster({
  title: "GPS Title",
  background: { color: "FFFFFF" },
  objects: [],
});

const contentFrame = () => [
  { line: { x: 0.35, y: 0.95, w: 9.3, h: 0, line: { color: NAVY, width: 1.25 } } },
  { image: { path: LOGO, x: 8.88, y: 6.72, w: 0.68, h: 0.62 } },
  {
    placeholder: {
      options: {
        name: "title", type: "title", x: 0.35, y: 0.2, w: 7.8, h: 0.7,
        fontSize: 32, bold: true, color: C.text2, valign: "middle", align: "left", margin: 0,
      },
      text: "",
    },
  },
];
const slideNum = () => ({ x: 8.35, y: 6.92, w: 0.45, h: 0.3, fontSize: 11, bold: true, color: "1A1A1A", align: "right" });

pres.defineSlideMaster({
  title: "GPS Content",
  background: { color: "FFFFFF" },
  margin: [0.4, 0.4, 0.6, 0.4],
  objects: contentFrame(),
  slideNumber: slideNum(),
});

// Content slide with a one-line navy subtitle under the rule (TATT "Opportunity (n/3)" frame)
pres.defineSlideMaster({
  title: "GPS Content Subtitle",
  background: { color: "FFFFFF" },
  margin: [0.4, 0.4, 0.6, 0.4],
  objects: [
    ...contentFrame(),
    {
      placeholder: {
        options: {
          name: "subtitle", type: "body", x: 0.35, y: 1.02, w: 9.3, h: 0.62,
          fontSize: 17, bold: true, color: C.text2, valign: "top", align: "left", margin: 0,
        },
        text: "",
      },
    },
  ],
  slideNumber: slideNum(),
});

// ---------- Slide 1: Title ----------
pres.addSection({ title: "Introduction" });
{
  const s = pres.addSlide({ masterName: "GPS Title", sectionTitle: "Introduction" });

  s.addText(
    [
      { text: "FTAI Aviation", options: { bold: true, color: C.text2, fontSize: 34, breakLine: true } },
      { text: "(NASDAQ: FTAI)", options: { color: C.text2, fontSize: 30 } },
    ],
    { x: 0.6, y: 0.35, w: 7, h: 1.25, margin: 0, valign: "top", isTextBox: true, objectName: "Company name" }
  );
  s.addText("Long Recommendation", {
    x: 0.6, y: 1.65, w: 7, h: 0.55, margin: 0, fontSize: 28, bold: true, color: C.accent2,
    isTextBox: true, objectName: "Recommendation",
  });

  // Key-figure strip
  const stats = [
    ["$167", "Current Price"],
    ["$308", "Target Price"],
    ["84%", "Upside"],
    ["3.4x", "Reward / Risk"],
  ];
  const sx = 0.6, colW = 8.8 / 4, sy = 2.75;
  stats.forEach(([big, lab], i) => {
    const x = sx + i * colW;
    s.addText(big, {
      x, y: sy, w: colW, h: 0.95, margin: 0, align: "center", valign: "bottom",
      fontSize: 48, bold: true, color: C.text2, isTextBox: true, objectName: `Stat ${i + 1} value`,
    });
    s.addText(lab, {
      x, y: sy + 1.0, w: colW, h: 0.4, margin: 0, align: "center", valign: "top",
      fontSize: 16, color: C.accent2, isTextBox: true, objectName: `Stat ${i + 1} label`,
    });
    if (i > 0) {
      s.addShape(pres.shapes.LINE, {
        x, y: sy + 0.2, w: 0, h: 1.15, line: { color: PLAT_LT, width: 1 }, objectName: `Stat divider ${i}`,
      });
    }
  });

  // Quote banner
  s.addText("“Be fearful when others are greedy and greedy when others are fearful.”", {
    x: 0.45, y: 4.6, w: 9.1, h: 0.8, fill: { color: PLAT_XLT }, align: "center", valign: "middle",
    fontSize: 19, bold: true, color: "1A1A1A", margin: [10, 10, 4, 4], isTextBox: true, objectName: "Quote",
  });
  s.addText("— Warren Buffett", {
    x: 0.45, y: 5.5, w: 9.1, h: 0.4, align: "center", margin: 0, fontSize: 19, bold: true, italic: true,
    color: "1A1A1A", isTextBox: true, objectName: "Quote attribution",
  });

  // Bottom-left details
  s.addText(
    [
      { text: "Date: October 2026", options: { breakLine: true } },
      { text: "Current Price: $167.03 (10/2/26)", options: { breakLine: true } },
      { text: "Target Price: $308.03 (84% upside, 3.4x R/R)" },
    ],
    { x: 0.6, y: 6.3, w: 5.2, h: 0.95, margin: 0, fontSize: 15, color: "1A1A1A", valign: "top",
      paraSpaceAfter: 2, isTextBox: true, objectName: "Pitch details" }
  );

  // GPS logo | presenter
  s.addImage({ path: LOGO, x: 6.45, y: 6.05, w: 1.35, h: 1.24, objectName: "GPS logo" });
  s.addShape(pres.shapes.LINE, { x: 8.05, y: 6.1, w: 0, h: 1.2, line: { color: PLAT, width: 1 }, objectName: "Logo divider" });
  s.addText([{ text: "Presenter", options: { breakLine: true } }, { text: "Name" }], {
    x: 8.15, y: 6.2, w: 1.55, h: 0.95, margin: 0, fontSize: 18, bold: true, color: C.accent2,
    align: "center", valign: "middle", isTextBox: true, objectName: "Presenter",
  });

  s.addNotes(
    "Price as of 10/2/26. Target is the base-case blended DCF: 50% perpetuity growth ($281) and 50% exit multiple ($335). " +
    "R/R = 132% bull blended upside vs. 39% bear blended downside."
  );
}

// ---------- Slide 2: The Opportunity ----------
pres.addSection({ title: "The Opportunity" });
{
  const s = pres.addSlide({ masterName: "GPS Content", sectionTitle: "The Opportunity" });
  s.addText("The Opportunity", { placeholder: "title" });

  const rows = [
    "1Q26 margins compressed 500 bps, and management guided EBITDA margins down from 40% to 30% for two years.",
    "A fraud overhang from the 2025 short report leaves the market doubting this is the bottom: it still sees FTAI as over-earning.",
    "We believe FTAI has reached steady state: margins have bottomed and share gains will drive volume growth.",
  ];
  const boxX = 1.75, boxW = 7.25, boxH = 1.0, circ = 0.95;
  rows.forEach((t, i) => {
    const y = 1.3 + i * 1.22;
    s.addText(t, {
      x: boxX, y, w: boxW, h: boxH, fill: { color: PLAT_LT }, align: "center", valign: "middle",
      fontSize: 15, bold: true, color: C.text2, margin: [44, 10, 2, 2], isTextBox: true, objectName: `Point ${i + 1}`,
    });
    s.addText(String(i + 1), {
      shape: pres.shapes.OVAL, x: boxX - circ / 2 - 0.05, y: y + boxH / 2 - circ / 2, w: circ, h: circ,
      fill: { color: "FFFFFF" }, line: { color: NAVY, width: 2 }, align: "center", valign: "middle",
      fontSize: 26, bold: true, color: C.text2, margin: 0, objectName: `Point ${i + 1} number`,
    });
  });

  // Funnel into the conclusion
  s.addShape(pres.shapes.ISOSCELES_TRIANGLE, {
    x: 1.3, y: 4.98, w: 7.7, h: 0.45, fill: { color: PLAT_LT }, line: { type: "none" },
    flipV: true, objectName: "Funnel",
  });
  s.addText(
    "The market is pricing a trough as a cliff. We see 84% upside, with Power as a free call option.",
    {
      x: 1.3, y: 5.6, w: 7.7, h: 0.85, fill: { color: NAVY }, align: "center", valign: "middle",
      fontSize: 17, bold: true, color: C.background1, margin: [10, 10, 2, 2], isTextBox: true, objectName: "Conclusion",
    }
  );
  s.addText([{ text: "Source: ", options: { bold: true } }, { text: "Company filings, earnings calls, GPS estimates" }], {
    x: 0.35, y: 6.95, w: 6, h: 0.3, margin: 0, fontSize: 11, color: "1A1A1A", isTextBox: true, objectName: "Source",
  });
}


// ---------- Shared chart / slide helpers ----------
const INK = "1A1A1A";
const chartFrame = (extra) => Object.assign({
  catAxisLabelColor: INK, catAxisLabelFontFace: "+mn-lt", catAxisLabelFontSize: 12,
  catAxisLineShow: true, catAxisLineColor: "BFBFBF",
  valAxisHidden: true, valGridLine: { style: "none" }, catGridLine: { style: "none" },
  showValue: true, dataLabelColor: INK, dataLabelFontFace: "+mn-lt", dataLabelFontSize: 13,
  dataLabelFontBold: true, showLegend: false, barGapWidthPct: 45,
}, extra);

const sectionHeader = (s, text, x, y, w, name) => {
  s.addText(text, {
    x, y, w, h: 0.4, margin: 0, align: "center", valign: "bottom", fontSize: 16, bold: true,
    color: INK, isTextBox: true, objectName: name,
  });
  s.addShape(pres.shapes.LINE, { x, y: y + 0.46, w, h: 0, line: { color: INK, width: 1 }, objectName: name + " rule" });
};

const takeaway = (s, text) => s.addText(text, {
  x: 0.35, y: 6.02, w: 9.3, h: 0.62, fill: { color: NAVY }, align: "center", valign: "middle",
  fontSize: 17, bold: true, color: C.background1, margin: [8, 8, 2, 2], isTextBox: true, objectName: "Takeaway",
});

const source = (s, text) => s.addText([{ text: "Source: ", options: { bold: true } }, { text }], {
  x: 0.35, y: 6.95, w: 7.8, h: 0.3, margin: 0, fontSize: 11, color: INK, isTextBox: true, objectName: "Source",
});

// ---------- Slide 3: The Opportunity (1/3) — margin compression ----------
{
  const s = pres.addSlide({ masterName: "GPS Content Subtitle", sectionTitle: "The Opportunity" });
  s.addText("The Opportunity (1/3)", { placeholder: "title" });
  s.addText("In one quarter, Aerospace margins fell ~470 bps, and management guided ~30% for two years.", { placeholder: "subtitle" });

  // Left: quarterly margin history + guide
  sectionHeader(s, "Aerospace Products Adj. EBITDA Margin", 0.35, 1.7, 5.75, "Margin chart header");
  const cats = ["Q1'25", "Q2'25", "Q3'25", "Q4'25", "Q1'26", "Q2'26", "FY26E", "FY27E"];
  s.addChart(pres.charts.BAR, [
    { name: "Reported", labels: cats, values: [0.359, 0.336, 0.348, 0.346, 0.299, 0.285, null, null] },
    { name: "Mgmt. guide", labels: cats, values: [null, null, null, null, null, null, 0.30, 0.30] },
  ], chartFrame({
    x: 0.35, y: 2.3, w: 5.75, h: 3.5, barDir: "col", barGrouping: "stacked",
    chartColors: [NAVY, "B5AEA9"], valAxisMinVal: 0, valAxisMaxVal: 0.54,
    dataLabelFormatCode: "0.0%", dataLabelPosition: "inEnd", dataLabelColor: "FFFFFF", dataLabelFontSize: 11, barGapWidthPct: 30,
    objectName: "Margin chart",
  }));
  s.addText("Mgmt. guide", {
    x: 4.6, y: 3.05, w: 1.45, h: 0.3, margin: 0, align: "center", fontSize: 12, italic: true, bold: true,
    color: C.accent2, isTextBox: true, objectName: "Guide label",
  });
  s.addText([{ text: "–470", options: { fontSize: 20, bold: true, breakLine: true } }, { text: "bps q/q", options: { fontSize: 11, bold: true } }], {
    shape: pres.shapes.OVAL, x: 2.85, y: 2.3, w: 1.2, h: 1.2, fill: { color: NAVY }, line: { color: NAVY },
    align: "center", valign: "middle", color: C.background1, margin: 0, objectName: "Compression callout",
  });

  // Right: management's mix explanation
  sectionHeader(s, "Management: “It's Mix”", 6.45, 1.7, 3.2, "Mix chart header");
  s.addChart(pres.charts.BAR, [
    { name: "Margin", labels: ["Light", "Heavy", "Blended"], values: [0.417, 0.25, 0.306] },
  ], chartFrame({
    x: 6.45, y: 2.3, w: 3.2, h: 2.4, barDir: "col", chartColors: ["B5AEA9", NAVY, "5A5350"],
    valAxisMinVal: 0, valAxisMaxVal: 0.5, dataLabelFormatCode: "0%", dataLabelPosition: "outEnd",
    objectName: "Mix chart",
  }));
  s.addText([
    { text: "Light: ", options: { bold: true } }, { text: "$6M sale, $2.5M profit", options: { breakLine: true } },
    { text: "Heavy: ", options: { bold: true } }, { text: "$12M sale, $3.0M profit" },
  ], {
    x: 6.45, y: 4.78, w: 3.2, h: 0.62, margin: 0, fontSize: 12, color: INK, valign: "top",
    isTextBox: true, objectName: "Mix detail",
  });
  s.addText("Lower margin, more dollars per job", {
    x: 6.45, y: 5.45, w: 3.2, h: 0.35, margin: 0, fontSize: 13, italic: true, bold: true, color: C.text2,
    isTextBox: true, objectName: "Mix kicker",
  });

  takeaway(s, "The drop is real. Is ~30% the floor, or just a waypoint?");
  source(s, "FTAI filings and earnings calls, GPS model");
  s.addNotes("Reported quarterly Aerospace Products Adj. EBITDA margins from the RPM tab. Q4'25 34.6% to Q1'26 29.9% = -470 bps. " +
    "Mix example is management's: a 6,000-cycle engine sold for ~$6M earns ~$2.5M; a 10,000-cycle engine sold for ~$12M earns ~$3M; one of each blends to ~30%.");
}

// ---------- Slide 4: The Opportunity (2/3) — the fraud overhang ----------
{
  const s = pres.addSlide({ masterName: "GPS Content Subtitle", sectionTitle: "The Opportunity" });
  s.addText("The Opportunity (2/3)", { placeholder: "title" });
  s.addText("A 2025 short report gave the market a darker explanation, and it stuck.", { placeholder: "subtitle" });

  // Left: the short thesis as a flow
  sectionHeader(s, "The Short Thesis (Jan. 2025)", 0.35, 1.7, 5.0, "Short thesis header");
  const steps = [
    ["Leasing engines sit on the books at depreciated value", PLAT_LT, C.text2],
    ["They are moved into Aerospace Products as inventory", PLAT_LT, C.text2],
    ["Sold at market prices, the low cost basis inflates AP margins", NAVY, C.background1],
  ];
  steps.forEach(([t, fill, col], i) => {
    const y = 2.35 + i * 1.18;
    s.addText(t, {
      x: 0.6, y, w: 4.5, h: 0.8, fill: { color: fill }, align: "center", valign: "middle",
      fontSize: 15, bold: true, color: col, margin: [10, 10, 2, 2], isTextBox: true, objectName: `Short step ${i + 1}`,
    });
    if (i < steps.length - 1) {
      s.addShape(pres.shapes.DOWN_ARROW, {
        x: 2.62, y: y + 0.83, w: 0.46, h: 0.32, fill: { color: PLAT }, line: { type: "none" }, objectName: `Short arrow ${i + 1}`,
      });
    }
  });

  // Right: valuation implies the market doesn't trust the earnings
  sectionHeader(s, "…So the Market Won't Pay Up", 5.75, 1.7, 3.9, "Multiple header");
  s.addChart(pres.charts.BAR, [
    { name: "EV / EBITDA", labels: ["FY26E", "FY27E", "FY28E"], values: [15.9, 9.8, 6.8] },
  ], chartFrame({
    x: 5.75, y: 2.3, w: 3.9, h: 3.0, barDir: "col", chartColors: [NAVY],
    valAxisMinVal: 0, valAxisMaxVal: 19, dataLabelFormatCode: '0.0"x"', dataLabelPosition: "outEnd",
    objectName: "Multiple chart",
  }));
  s.addShape(pres.shapes.RECTANGLE, {
    x: 8.36, y: 3.7, w: 1.12, h: 1.62, fill: { type: "none" }, line: { color: C.accent2, width: 2, dashType: "dash" },
    objectName: "FY28 highlight",
  });
  s.addText("EV / Adj. EBITDA (Jefferies estimates)", {
    x: 5.75, y: 5.58, w: 3.9, h: 0.3, margin: 0, align: "center", fontSize: 12, italic: true, color: C.accent2,
    isTextBox: true, objectName: "Multiple caption",
  });

  takeaway(s, "The market reads the margin reset as the short thesis unwinding, and prices FTAI as if it's still over-earning.");
  source(s, "Muddy Waters Research (Jan. 2025), Jefferies (8/2/26), FTAI filings, GPS analysis");
  s.addNotes("EV of $20.56B at $167.03 (10/2/26) over Jefferies Adj. EBITDA of $1,289M (FY26E), $2,099M (FY27E) and $3,023M (FY28E).");
}

// ---------- Slide 5: The Opportunity (3/3) — Power is free ----------
{
  const s = pres.addSlide({ masterName: "GPS Content Subtitle", sectionTitle: "The Opportunity" });
  s.addText("The Opportunity (3/3)", { placeholder: "title" });
  s.addText("The market assigns no value to Power: the stock trades below the core business alone.", { placeholder: "subtitle" });

  sectionHeader(s, "FY27E Sum of the Parts ($ / Share)", 0.35, 1.7, 5.75, "SOTP header");
  const cats = ["Current Price", "Core ex-Power", "Power", "SOTP"];
  s.addChart(pres.charts.BAR, [
    { name: "Base", labels: cats, values: [0, 0, 224.75, 0] },
    { name: "Value", labels: cats, values: [167.03, 224.75, 0, 276.65] },
    { name: "Power", labels: cats, values: [0, 0, 51.9, 0] },
  ], chartFrame({
    x: 0.35, y: 2.3, w: 5.75, h: 3.5, barDir: "col", barGrouping: "stacked", barGapWidthPct: 35,
    chartColors: ["FFFFFF", NAVY, PLAT], valAxisMinVal: 0, valAxisMaxVal: 330,
    dataLabelFormatCode: '"$"0;;;', dataLabelPosition: "inEnd", dataLabelColor: "FFFFFF", dataLabelFontSize: 15,
    objectName: "SOTP chart",
  }));
  s.addText([{ text: "26%", options: { fontSize: 20, bold: true, breakLine: true } }, { text: "below core", options: { fontSize: 11, bold: true } }], {
    shape: pres.shapes.OVAL, x: 0.6, y: 2.35, w: 1.15, h: 1.15, fill: { color: NAVY }, line: { color: NAVY },
    align: "center", valign: "middle", color: C.background1, margin: 0, objectName: "Discount callout",
  });
  s.addText("Free call option", {
    x: 3.25, y: 2.5, w: 1.45, h: 0.3, margin: 0, align: "center", fontSize: 12, italic: true, bold: true,
    color: C.accent2, isTextBox: true, objectName: "Power label",
  });

  // Right: Power at a glance
  sectionHeader(s, "FTAI Power at a Glance", 6.45, 1.7, 3.2, "Power stats header");
  const stats = [
    ["$1.465B", "First hyperscaler order, via the J&F JV"],
    ["$450–750M", "FY27 Power EBITDA guide"],
    ["25 MW", "Per unit, built from CFM56 cores"],
  ];
  stats.forEach(([big, lab], i) => {
    const y = 2.35 + i * 1.18;
    s.addText(big, {
      x: 6.45, y, w: 3.2, h: 0.58, margin: 0, align: "center", valign: "bottom", fontSize: 30, bold: true,
      color: C.text2, isTextBox: true, objectName: `Power stat ${i + 1}`,
    });
    s.addText(lab, {
      x: 6.45, y: y + 0.6, w: 3.2, h: 0.35, margin: 0, align: "center", valign: "top", fontSize: 13,
      color: C.accent2, isTextBox: true, objectName: `Power stat ${i + 1} label`,
    });
  });

  takeaway(s, "Even with Power at zero, FTAI is cheap. Power is a free call option on top.");
  source(s, "FTAI filings and earnings calls, GPS SOTP (FY27E EBITDA × segment multiples)");
  s.addNotes("SOTP on FY27E EBITDA: Aerospace Products $1,541M at 16x ($237/sh), Power $450M at 12x ($52/sh, low end of guide), " +
    "Aviation Leasing + SCI $455M at 9x ($39/sh), less corporate (-$28/sh), net debt (-$23/sh) and preferred (-$1/sh) = $277/sh. " +
    "Ex-Power = $225/sh vs. $167.03 current (10/2/26), a 26% discount.");
}

// ---------- Slide 6: Business Overview ----------
pres.addSection({ title: "Business Overview" });
{
  const s = pres.addSlide({ masterName: "GPS Content Subtitle", sectionTitle: "Business Overview" });
  s.addText("Business Overview", { placeholder: "title" });
  s.addText("FTAI keeps the world's best-selling jet engine flying, and turns old ones into power.", { placeholder: "subtitle" });

  const cols = [
    ["cfm56.png", "Aerospace Products", "Restores and swaps CFM56 engine modules, so airlines get engines back in days, not months.", "757 → 1,200", "Modules, 2025 → 2026E"],
    ["power.png", "FTAI Power", "Converts CFM56 cores into 25 MW mobile gas turbines that power data centers.", "$450–750M", "FY27 EBITDA guide"],
    ["aircraft.png", "Leasing + SCI", "Leases jets and engines. The SCI partnership buys mid-life jets and sends all engine work to FTAI.", "316", "SCI aircraft, YE26E"],
  ];
  const colW = 2.9, gap = 0.3, x0 = 0.35;
  cols.forEach(([img, name, desc, big, lab], i) => {
    const x = x0 + i * (colW + gap);
    s.addImage({ path: path.join(__dirname, "img", img), x: x + 0.15, y: 1.75, w: 2.6, h: 1.47, objectName: `${name} illustration` });
    s.addText(name, {
      x, y: 3.32, w: colW, h: 0.4, margin: 0, align: "center", fontSize: 18, bold: true, color: C.text2,
      isTextBox: true, objectName: `${name} name`,
    });
    s.addText(desc, {
      x, y: 3.75, w: colW, h: 1.0, margin: 0, align: "center", valign: "top", fontSize: 13, color: INK,
      isTextBox: true, objectName: `${name} description`,
    });
    s.addText([{ text: big, options: { fontSize: 22, bold: true, color: C.text2, breakLine: true } }, { text: lab, options: { fontSize: 12, color: C.accent2 } }], {
      x: x + 0.2, y: 4.85, w: colW - 0.4, h: 0.95, fill: { color: PLAT_XLT }, align: "center", valign: "middle",
      margin: 0, isTextBox: true, objectName: `${name} stat`,
    });
    if (i > 0) {
      s.addShape(pres.shapes.LINE, { x: x - gap / 2, y: 1.85, w: 0, h: 3.9, line: { color: PLAT_LT, width: 1 }, objectName: `Column divider ${i}` });
    }
  });

  takeaway(s, "One engine, three ways to earn: fix it, power with it, and own the planes it flies on.");
  source(s, "FTAI filings and earnings calls, GPS model. Illustrations are schematic.");
}

(async () => {
  await pres.writeFile({ fileName: OUT });
  await applyTheme(OUT, THEME);
  console.log("Wrote", OUT);
})();
