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
        name: "title", type: "title", x: 0.35, y: 0.2, w: 9.3, h: 0.7,
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

  // Right: two readings of the same margin drop
  sectionHeader(s, "Two Readings of the Drop", 5.75, 1.7, 3.9, "Readings header");
  const readings = [
    ["Management", "Heavier-scope work, new shops still ramping, and prices held below OEM to win share.", "Temporary: margins recover", PLAT_LT, C.text2, C.text2],
    ["The Bears", "The cheap, depreciated leasing engines that flattered margins are running out.", "Structural: margins keep falling", NAVY, C.background1, C.background1],
  ];
  readings.forEach(([who, why, verdict, fill, col, vcol], i) => {
    const y = 2.35 + i * 1.72;
    s.addText([
      { text: who, options: { fontSize: 15, bold: true, breakLine: true } },
      { text: why, options: { fontSize: 12, breakLine: true } },
      { text: "→ " + verdict, options: { fontSize: 13, bold: true, italic: true } },
    ], {
      x: 5.75, y, w: 3.9, h: 1.45, fill: { color: fill }, color: col, align: "center", valign: "middle",
      margin: [10, 10, 4, 4], paraSpaceAfter: 4, isTextBox: true, objectName: `${who} reading`,
    });
  });
  s.addText("vs.", {
    x: 7.35, y: 3.8, w: 0.7, h: 0.27, margin: 0, align: "center", valign: "middle", fontSize: 14, bold: true, italic: true,
    color: C.accent2, isTextBox: true, objectName: "Readings vs",
  });

  takeaway(s, "The market reads the margin reset as the short thesis unwinding, and prices FTAI as if it's still over-earning.");
  source(s, "Muddy Waters Research (Jan. 2025), FTAI filings and earnings calls, GPS analysis");
  s.addNotes("Both readings explain the same 1Q26 drop. Management cites heavier-scope work, new facilities and technician productivity still ramping, and pricing held below OEM escalators to take share. " +
    "The bear reading, following the short report, is that depreciated leasing inventory moved into Aerospace Products had been propping up margins and is running out.");}

// ---------- Slide 5: The Opportunity (3/3) — Power is free ----------
{
  const s = pres.addSlide({ masterName: "GPS Content Subtitle", sectionTitle: "The Opportunity" });
  s.addText("The Opportunity (3/3)", { placeholder: "title" });
  s.addText("Turbine makers are sold out for years, yet the market assigns no value to FTAI's Power.", { placeholder: "subtitle" });

  sectionHeader(s, "Combined Gas Turbine Backlog (GW)", 0.35, 1.7, 5.75, "Backlog header");
  const by = ["Mid-2025", "Mid-2026"];
  s.addChart(pres.charts.BAR, [
    { name: "GE Vernova", labels: by, values: [55, 116] },
    { name: "Siemens Energy", labels: by, values: [37, 69] },
    { name: "Mitsubishi", labels: by, values: [23, 35] },
  ], chartFrame({
    x: 0.35, y: 2.3, w: 5.75, h: 2.9, barDir: "col", barGrouping: "stacked", barGapWidthPct: 110,
    chartColors: [NAVY, "3B4C82", "B5AEA9"], valAxisMinVal: 0, valAxisMaxVal: 250, catAxisLabelFontSize: 13,
    dataLabelFormatCode: "0", dataLabelPosition: "ctr", dataLabelColor: "FFFFFF", dataLabelFontSize: 12, objectName: "Combined backlog chart",
  }));
  // Totals above bars and a connecting arrow
  s.addText("115 GW", { x: 1.2, y: 3.3, w: 1.3, h: 0.32, margin: 0, align: "center", fontSize: 16, bold: true, color: C.text2, isTextBox: true, objectName: "Total 2025" });
  s.addText("220 GW", { x: 4.1, y: 2.25, w: 1.3, h: 0.32, margin: 0, align: "center", fontSize: 16, bold: true, color: C.text2, isTextBox: true, objectName: "Total 2026" });
  s.addShape(pres.shapes.LINE, { x: 2.55, y: 2.6, w: 1.5, h: 0.85, flipV: true, line: { color: NAVY, width: 2.5, endArrowType: "triangle" }, objectName: "Backlog arrow" });
  s.addText("~1.9x", { x: 2.25, y: 2.55, w: 1.0, h: 0.34, margin: 0, align: "center", fontSize: 18, bold: true, color: C.text2, isTextBox: true, objectName: "Growth label" });
  s.addText([{ text: "■ ", options: { color: NAVY } }, { text: "GE Vernova  " }, { text: "■ ", options: { color: "3B4C82" } }, { text: "Siemens Energy  " }, { text: "■ ", options: { color: "B5AEA9" } }, { text: "Mitsubishi" }], {
    x: 0.35, y: 5.2, w: 5.75, h: 0.26, margin: 0, align: "center", fontSize: 11, color: INK, isTextBox: true, objectName: "Backlog legend",
  });
  s.addText("GE Vernova booking out to 2031; Siemens lead times 3+ years", {
    x: 0.35, y: 5.48, w: 5.75, h: 0.3, margin: 0, align: "center", fontSize: 10, italic: true, color: C.accent2, isTextBox: true, objectName: "Backlog caption",
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
  source(s, "GE Vernova, Siemens Energy and MHI results, mid-2025 vs. mid-2026 (via Utility Dive, Industrial Info); FTAI filings");
  s.addNotes("Combined backlog: GE Vernova gas backlog + slot reservations 55 GW (Q2'25) → 116 GW (Q2'26; ≥125 GW guided for YE26); Siemens Energy firm gas turbine backlog 37 GW (Q3 FY25) → 69 GW (Q3 FY26); " +
    "Mitsubishi large-frame backlog 23 GW → 35 GW. Definitions differ (GEV includes reservations; Siemens firm only; MHI large-frame only), so treat the total as indicative. End-2024 GW figures were not disclosed. ");
}

// ---------- Slide 6: Returns Summary (modeled on SPOT "Pitch Summary – Thesis 2") ----------
pres.addSection({ title: "Returns" });
{
  const s = pres.addSlide({ masterName: "GPS Content", sectionTitle: "Returns" });
  s.addText("Returns Summary", { placeholder: "title" });

  s.addText("At $167, the market prices the bear case. Our three theses add $110 of upside.", {
    x: 0.35, y: 1.12, w: 9.3, h: 0.56, fill: { color: NAVY }, align: "center", valign: "middle",
    fontSize: 17, bold: true, color: C.background1, margin: 0, isTextBox: true, objectName: "Headline banner",
  });
  s.addText("What Each Thesis Adds to the Target Price", {
    x: 0.35, y: 1.78, w: 9.3, h: 0.42, fill: { color: NAVY }, align: "center", valign: "middle",
    fontSize: 16, color: C.background1, margin: 0, isTextBox: true, objectName: "Sub banner",
  });

  // $/share contributions to the base-case FY27E SOTP: Shapley average over all orderings, starting from the bear case
  const rows = [
    ["Thesis 1a) Margins Have Bottomed", "PMA parts, OEM-linked pricing and technician productivity lift Aerospace margins from ~30% to ~32.5% by FY31.", "+$17", "+10% upside"],
    ["Thesis 1b) Volume Grows With Share", "New capacity, OEMs moving to LEAP and faster turnaround lift FTAI's CFM56 module share from ~12% to 20% by FY30.", "+$33", "+20% upside"],
    ["Thesis 2) Power Is a Call Option", "Mod-1 deliveries ramp from 45 units in FY27 to 110 by FY29 at ~40% EBITDA margins.", "+$55", "+33% upside"],
  ];
  const by0 = 2.38, bh = 0.94, bgap = 0.12;
  rows.forEach(([head, body, big, small], i) => {
    const y = by0 + i * (bh + bgap);
    s.addText([
      { text: head, options: { bold: true, fontSize: 15, color: C.text2, breakLine: true } },
      { text: body, options: { fontSize: 12, color: INK } },
    ], {
      x: 0.35, y, w: 6.15, h: bh, align: "center", valign: "middle", margin: [8, 8, 3, 3],
      line: { color: INK, width: 1, dashType: "dash" }, isTextBox: true, objectName: `Thesis ${i + 1} box`,
    });
    s.addText([
      { text: "Contribution:", options: { fontSize: 13, bold: true, color: INK, breakLine: true } },
      { text: big, options: { fontSize: 24, bold: true, color: C.text2, breakLine: true } },
      { text: small, options: { fontSize: 12, color: C.accent2 } },
    ], {
      x: 7.2, y, w: 2.45, h: bh, align: "center", valign: "middle", margin: 0, isTextBox: true, objectName: `Thesis ${i + 1} contribution`,
    });
  });
  s.addShape(pres.shapes.CHEVRON, {
    x: 6.62, y: by0, w: 0.46, h: 3 * bh + 2 * bgap, fill: { color: PLAT_LT }, line: { type: "none" }, objectName: "Chevron",
  });

  s.addText("Bear case (bear margins and share, no Power) is worth $172 on our SOTP, just above today's $167.", {
    x: 0.35, y: 5.6, w: 9.3, h: 0.3, margin: 0, align: "center", fontSize: 12, color: C.accent2,
    isTextBox: true, objectName: "Baseline note",
  });
  s.addText([
    { text: "$167 today + $5 to bear value + $17 margins + $33 volume + $55 Power = " },
    { text: "$277 SOTP", options: { bold: true } },
    { text: " (+66%)" },
  ], {
    x: 0.35, y: 5.98, w: 9.3, h: 0.56, fill: { color: PLAT_XLT }, line: { color: NAVY, width: 1.25 },
    align: "center", valign: "middle", fontSize: 13, color: INK, margin: 0, isTextBox: true, objectName: "Base case bridge",
  });
  source(s, "GPS model: base-case FY27E SOTP; thesis drivers switched Bear vs. Base (Power off = 0 units), Shapley average");
  s.addNotes(
    "Return math uses the base-case FY27E sum of the parts ($276.65/share): Aerospace 16x, Power 12x, Leasing + SCI 9x, less corporate, net debt and preferred. " +
    "Attribution re-runs the full model for all 8 on/off combinations of the three theses. Margins = OEM escalator, pass-through, Aerospace margin ex-PMA and PMA rows. " +
    "Volume = FTAI share of MRO and SCI aircraft rows. Power = Mod-1 units delivered (off = 0, i.e. what the market prices today). " +
    "Bear case with no Power = $171.86 vs. $167.03 today (+$4.83). Shapley contributions: margins +$17.04, volume +$32.66, Power +$55.08 " +
    "(the $51.90 SOTP value plus ~$3 of FY27 Power cash that lowers net debt). Total $276.64."
  );
}

// ---------- Slide 6: Business Overview ----------
pres.addSection({ title: "Business Overview" });
{
  const s = pres.addSlide({ masterName: "GPS Content Subtitle", sectionTitle: "Business Overview" });
  s.addText("Business Overview (1/2)", { placeholder: "title" });
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

// ---------- Slide 7: Business Overview (2/2) — the module exchange ----------
{
  const s = pres.addSlide({ masterName: "GPS Content Subtitle", sectionTitle: "Business Overview" });
  s.addText("Business Overview (2/2)", { placeholder: "title" });
  s.addText("FTAI swaps worn modules for restored ones from its own pool, so airlines skip the shop queue.", { placeholder: "subtitle" });

  // Left: the exchange loop
  sectionHeader(s, "How an Exchange Works", 0.35, 1.7, 4.3, "Loop header");
  const cx = 2.5, cy = 3.97, rx = 1.5, ry = 1.22;
  s.addShape(pres.shapes.OVAL, {
    x: cx - rx, y: cy - ry, w: 2 * rx, h: 2 * ry, fill: { type: "none" }, line: { color: "B5AEA9", width: 3 }, objectName: "Loop ring",
  });
  [45, 135, 225, 315].forEach((deg, i) => {
    const t = (deg * Math.PI) / 180, a = 0.24;
    s.addShape(pres.shapes.ISOSCELES_TRIANGLE, {
      x: cx + rx * Math.sin(t) - a / 2, y: cy - ry * Math.cos(t) - a / 2, w: a, h: a, rotate: deg + 90,
      fill: { color: PLAT }, line: { type: "none" }, objectName: `Loop arrow ${i + 1}`,
    });
  });
  s.addText([{ text: "Module", options: { breakLine: true } }, { text: "pool" }], {
    shape: pres.shapes.OVAL, x: cx - 0.55, y: cy - 0.55, w: 1.1, h: 1.1, fill: { color: NAVY }, line: { color: NAVY },
    align: "center", valign: "middle", fontSize: 13, bold: true, color: C.background1, margin: 0, objectName: "Module pool",
  });
  const nodes = [
    [0, "Engine needs a shop visit"],
    [90, "FTAI swaps in a restored module"],
    [180, "Engine back in service in days"],
    [270, "Worn module restored for the pool"],
  ];
  const nw = 1.32, nh = 0.8;
  nodes.forEach(([deg, t], i) => {
    const a = (deg * Math.PI) / 180;
    const nx = cx + rx * Math.sin(a) - nw / 2, ny = cy - ry * Math.cos(a) - nh / 2;
    s.addText(t, {
      x: nx, y: ny, w: nw, h: nh, fill: { color: PLAT_LT }, align: "center", valign: "middle",
      fontSize: 12, bold: true, color: C.text2, margin: [6, 4, 2, 2], isTextBox: true, objectName: `Loop step ${i + 1}`,
    });
    s.addText(String(i + 1), {
      shape: pres.shapes.OVAL, x: nx - 0.2, y: ny - 0.2, w: 0.34, h: 0.34, fill: { color: NAVY }, line: { color: "FFFFFF", width: 1.5 },
      align: "center", valign: "middle", fontSize: 12, bold: true, color: C.background1, margin: 0, objectName: `Loop step ${i + 1} number`,
    });
  });

  // Right: Module Factory before / after grids
  sectionHeader(s, "Why It Pays: The Module Factory", 4.95, 1.7, 4.7, "Factory header");
  const before = [["$2.0M", [7, 0, 4]], ["$2.5M", [4, 7, 0]], ["$2.0M", [0, 4, 7]]];
  const after = [["$8.5M", [7, 7, 7]], ["$6.0M", [4, 4, 4]], ["$1.5M", [0, 0, 0]]];
  const sq = 0.4, sg = 0.06, rowY0 = 2.62, rowH = 0.78, px = 0.76;
  const cell = (x, y, k, name) => {
    const style = k === 7 ? { fill: NAVY, col: "FFFFFF", line: NAVY } : k === 4 ? { fill: "B5AEA9", col: NAVY, line: "B5AEA9" } : { fill: "FFFFFF", col: PLAT, line: "B5AEA9" };
    s.addText(`${k}k`, {
      x, y, w: sq, h: sq, fill: { color: style.fill }, line: { color: style.line, width: 1.25 }, align: "center", valign: "middle",
      fontSize: 11, bold: true, color: style.col, margin: 0, objectName: name,
    });
  };
  const grid = (x0, rows, label, tag) => {
    s.addText(label, {
      x: x0, y: 2.2, w: 2.08, h: 0.3, margin: 0, align: "center", fontSize: 13, bold: true, italic: true, color: C.accent2,
      isTextBox: true, objectName: `${tag} label`,
    });
    rows.forEach(([price, ks], i) => {
      const y = rowY0 + i * rowH;
      s.addText(price, {
        x: x0, y, w: px - 0.04, h: sq, margin: 0, align: "left", valign: "middle", fontSize: 14, bold: true, color: C.text2,
        isTextBox: true, objectName: `${tag} engine ${i + 1} value`,
      });
      ks.forEach((k, j) => cell(x0 + px + j * (sq + sg), y, k, `${tag} engine ${i + 1} module ${j + 1}`));
    });
    ["Fan", "Core", "LPT"].forEach((m, j) => s.addText(m, {
      x: x0 + px + j * (sq + sg) - 0.05, y: rowY0 + 3 * rowH - 0.32, w: sq + 0.1, h: 0.25, margin: 0, align: "center",
      fontSize: 10, color: C.accent2, isTextBox: true, objectName: `${tag} ${m} caption`,
    }));
  };
  grid(4.95, before, "3 worn engines in", "Before");
  grid(7.57, after, "Engines out", "After");
  s.addShape(pres.shapes.RIGHT_ARROW, {
    x: 7.1, y: 3.4, w: 0.4, h: 0.36, fill: { color: PLAT }, line: { type: "none" }, objectName: "Factory arrow",
  });
  s.addText([{ text: "$6.5M", options: { fontSize: 18, bold: true, breakLine: true } }, { text: "engines + $3.5M of work", options: { fontSize: 11 } }], {
    x: 4.95, y: 5.08, w: 2.08, h: 0.72, fill: { color: PLAT_LT }, align: "center", valign: "middle", color: C.text2, margin: 0,
    isTextBox: true, objectName: "Before total",
  });
  s.addText([{ text: "$16.0M", options: { fontSize: 18, bold: true, breakLine: true } }, { text: "+$6.0M of value created", options: { fontSize: 11 } }], {
    x: 7.57, y: 5.08, w: 2.08, h: 0.72, fill: { color: NAVY }, align: "center", valign: "middle", color: C.background1, margin: 0,
    isTextBox: true, objectName: "After total",
  });

  takeaway(s, "FTAI sells speed to airlines and harvests cycles from engines no one else can use.");
  source(s, "FTAI investor materials (Module Factory example), GPS analysis");
  s.addNotes("Module Factory example (FTAI): three unserviceable engines worth $2.0M, $2.5M and $2.0M each still hold modules with life left " +
    "(cycles shown per Fan / Core / LPT). FTAI splits them into nine modules, adds $3.5M of MRO work, and reassembles two serviceable engines " +
    "($8.5M at 7k/7k/7k and $6.0M at 4k/4k/4k) plus one run-out core ($1.5M): $16.0M out vs. $10.0M in, $6.0M of value created.");
}

// ---------- Thesis 1a: Margins Have Bottomed (3 slides) ----------
pres.addSection({ title: "Thesis 1a" });

// 1a (1/3): the bear case is nearly exhausted
{
  const s = pres.addSlide({ masterName: "GPS Content Subtitle", sectionTitle: "Thesis 1a" });
  s.addText("Thesis 1a: Margin Floor (1/4)", { placeholder: "title" });
  s.addText("Even if the bears are right, too little cheap inventory is left to push margins lower.", { placeholder: "subtitle" });

  sectionHeader(s, "Cheap Stock Left in AP", 0.35, 1.7, 3.9, "Donut header");
  s.addChart(pres.charts.DOUGHNUT, [
    { name: "AP inventory", labels: ["Depreciated leasing stock", "Everything else"], values: [8, 92] },
  ], {
    x: 0.6, y: 2.3, w: 3.4, h: 3.1, holeSize: 68, chartColors: [NAVY, PLAT_LT], showLegend: false,
    showValue: false, showPercent: false, showLabel: false, dataBorder: { pt: 1, color: "FFFFFF" }, objectName: "Inventory donut",
  });
  s.addText([{ text: "<8%", options: { fontSize: 34, bold: true, color: C.text2, breakLine: true } }, { text: "left to unwind", options: { fontSize: 13, color: C.accent2 } }], {
    x: 1.3, y: 3.35, w: 2.0, h: 1.0, align: "center", valign: "middle", margin: 0, isTextBox: true, objectName: "Donut center",
  });

  sectionHeader(s, "Margin: Trough, Then Rebuild", 4.55, 1.7, 5.1, "Margin path header");
  const mc = ["FY25", "Q1'26", "Q2'26", "FY26E", "FY27E", "FY28E", "FY29E", "FY30E", "FY31E"];
  s.addChart(pres.charts.BAR, [
    { name: "Reported", labels: mc, values: [0.347, 0.299, 0.285, null, null, null, null, null, null] },
    { name: "GPS model", labels: mc, values: [null, null, null, 0.301, 0.299, 0.307, 0.314, 0.320, 0.325] },
  ], chartFrame({
    x: 4.55, y: 2.3, w: 5.1, h: 3.5, barDir: "col", barGrouping: "clustered", barOverlapPct: 100, barGapWidthPct: 30,
    chartColors: [NAVY, "B5AEA9"], valAxisMinVal: 0, valAxisMaxVal: 0.4, catAxisLabelFontSize: 10,
    dataLabelFormatCode: "0.0%", dataLabelPosition: "outEnd", dataLabelFontSize: 10,
    objectName: "Margin path chart",
  }));
  s.addText("Our model", {
    x: 7.4, y: 2.3, w: 1.6, h: 0.3, margin: 0, align: "center", fontSize: 12, italic: true, bold: true, color: C.accent2,
    isTextBox: true, objectName: "Model label",
  });

  takeaway(s, "With little cheap stock left, ~30% is the floor, and margins rebuild from here.");
  source(s, "FTAI filings, GPS analysis and model (Aerospace Adj. EBITDA margin incl. PMA)");
  s.addNotes("Depreciated leasing inventory remaining in Aerospace Products is under 8% (GPS analysis), so even on the short report's logic there is little left to compress margins. " +
    "Margin path: FY25 34.7%, Q1'26 29.9%, Q2'26 28.5% reported; GPS model 30.1% FY26E, 29.9% FY27E, then 30.7% / 31.4% / 32.0% / 32.5% FY28E–FY31E.");
}

// 1a (2/3): price catch-up and EBITDA per module
{
  const s = pres.addSlide({ masterName: "GPS Content Subtitle", sectionTitle: "Thesis 1a" });
  s.addText("Thesis 1a: Margin Floor (2/4)", { placeholder: "title" });
  s.addText("FTAI held price to win share while OEM list prices rose ~7% a year. It can now catch up.", { placeholder: "subtitle" });

  sectionHeader(s, "Price Index (2025 = 100)", 0.35, 1.7, 4.6, "Price header");
  const yrs = ["2025", "2026", "2027", "2028", "2029", "2030", "2031"];
  s.addChart(pres.charts.LINE, [
    { name: "OEM list price", labels: yrs, values: [100, 107.0, 114.0, 121.9, 130.5, 139.6, 149.4] },
    { name: "FTAI price", labels: yrs, values: [100, 100.0, 103.3, 106.9, 110.6, 114.5, 118.5] },
  ], chartFrame({
    x: 0.35, y: 2.3, w: 4.6, h: 3.1, chartColors: [NAVY, "B5AEA9"], lineSize: 3, lineDataSymbol: "circle", lineDataSymbolSize: 7,
    valAxisMinVal: 90, valAxisMaxVal: 160, showValue: false, objectName: "Price index chart",
  }));
  s.addText("OEM list (+7%/yr)", {
    x: 2.95, y: 2.35, w: 1.9, h: 0.3, margin: 0, align: "right", fontSize: 12, bold: true, color: C.text2, isTextBox: true, objectName: "OEM line label",
  });
  s.addText("FTAI (half of OEM)", {
    x: 2.95, y: 3.65, w: 1.9, h: 0.3, margin: 0, align: "right", fontSize: 12, bold: true, color: C.accent2, isTextBox: true, objectName: "FTAI line label",
  });
  s.addText("The gap is pricing room", {
    x: 0.35, y: 5.45, w: 4.6, h: 0.3, margin: 0, align: "center", fontSize: 12, italic: true, color: C.accent2, isTextBox: true, objectName: "Price caption",
  });

  sectionHeader(s, "EBITDA per Module ($K)", 5.35, 1.7, 4.3, "EPM header");
  const fy = ["FY25", "FY26E", "FY27E", "FY28E", "FY29E", "FY30E", "FY31E"];
  s.addChart(pres.charts.BAR, [
    { name: "Trough", labels: fy, values: [null, 876, null, null, null, null, null] },
    { name: "EBITDA / module", labels: fy, values: [887, null, 913, 969, 1027, 1084, 1139] },
  ], chartFrame({
    x: 5.35, y: 2.3, w: 4.3, h: 3.5, barDir: "col", barGrouping: "stacked", barGapWidthPct: 30, chartColors: ["B5AEA9", NAVY],
    valAxisMinVal: 0, valAxisMaxVal: 1300, catAxisLabelFontSize: 10, dataLabelFormatCode: "#,##0;;;", dataLabelPosition: "inEnd",
    dataLabelColor: "FFFFFF", dataLabelFontSize: 10, objectName: "EBITDA per module chart",
  }));

  takeaway(s, "Passing through just half of OEM increases, plus PMA, lifts EBITDA per module ~30% by FY31.");
  source(s, "GPS model (RPM tab: CFM escalator 7%/yr, FTAI pass-through 50% from 2027; EBITDA per module incl. PMA)");
  s.addNotes("OEM index compounds the CFM escalator (7% in 2026, 6.5% in 2027, 7% thereafter). FTAI index applies the model's pass-through: 0% in 2026, then 50% of the escalator. " +
    "EBITDA per module: $887K FY25, $876K FY26E trough, $913K FY27E, $969K FY28E, $1,027K FY29E, $1,084K FY30E, $1,139K FY31E (+30% vs. FY26E).");
}

// 1a (3/4): cohort build — light-scope work returns late in the cycle
{
  const s = pres.addSlide({ masterName: "GPS Content Subtitle", sectionTitle: "Thesis 1a" });
  s.addText("Thesis 1a: Margin Floor (3/4)", { placeholder: "title" });
  s.addText("Heavy second visits peak in 2027 while late-life, lighter visits keep rising, and they cross.", { placeholder: "subtitle" });

  sectionHeader(s, "Heavy vs. Late-Life Shop Visits", 0.35, 1.7, 4.75, "Cohort header");
  const cy = ["2025", "2026", "2027", "2028", "2029", "2030", "2031", "2032"];
  s.addChart([
    { type: pres.charts.LINE, data: [
        { name: "Second visits (heaviest)", labels: cy, values: [842, 891, 914, 908, 874, 832, null, null] },
        { name: "Third+ visits (late life, lighter)", labels: cy, values: [532, 597, 641, 679, 700, 720, null, null] },
      ], options: { chartColors: [NAVY, PLAT], lineSize: 3.5, lineDataSymbol: "circle", lineDataSymbolSize: 7 } },
    { type: pres.charts.LINE, data: [
        { name: "Second trend", labels: cy, values: [null, null, null, null, null, 832, 790, 748] },
        { name: "Third+ trend", labels: cy, values: [null, null, null, null, null, 720, 740, 760] },
      ], options: { chartColors: [NAVY, PLAT], lineSize: 2.5, lineDash: "dash", lineDataSymbol: "none" } },
  ], {
    x: 0.35, y: 2.3, w: 4.75, h: 3.1, showLegend: false,
    valAxisHidden: true, valAxisMinVal: 450, valAxisMaxVal: 1000, valGridLine: { style: "none" },
    catAxisLabelColor: INK, catAxisLabelFontFace: "+mn-lt", catAxisLabelFontSize: 11, catGridLine: { style: "none" },
    catAxisLineColor: "BFBFBF", objectName: "Cohort chart",
  });
  // Direct labels and annotations
  s.addText("Heavy 2nd visits peak", {
    x: 0.95, y: 2.3, w: 2.5, h: 0.28, margin: 0, align: "center", fontSize: 12, bold: true, color: C.text2,
    isTextBox: true, objectName: "Peak label",
  });
  s.addText("Late-life, lighter visits keep rising", {
    x: 0.95, y: 4.72, w: 3.3, h: 0.28, margin: 0, align: "left", fontSize: 11, bold: true, color: C.accent2,
    isTextBox: true, objectName: "Late-life label",
  });
  s.addShape(pres.shapes.OVAL, { x: 4.6, y: 3.44, w: 0.18, h: 0.18, fill: { color: NAVY }, line: { color: "FFFFFF", width: 1.5 }, objectName: "Crossover dot" });
  s.addText([{ text: "Light work", options: { breakLine: true } }, { text: "overtakes ~2032" }], {
    shape: pres.shapes.ROUNDED_RECTANGLE, rectRadius: 0.08, x: 3.55, y: 3.85, w: 1.5, h: 0.62, fill: { color: NAVY }, line: { color: NAVY },
    align: "center", valign: "middle", fontSize: 11, bold: true, color: C.background1, margin: 0, objectName: "Crossover callout",
  });
  s.addText("Model through 2030; dashed = trend", {
    x: 0.35, y: 5.42, w: 4.75, h: 0.3, margin: 0, align: "center", fontSize: 11, italic: true, color: C.accent2,
    isTextBox: true, objectName: "Cohort caption",
  });

  sectionHeader(s, "Margin vs. Light-Scope Mix", 5.35, 1.7, 4.3, "Mix header");
  const lx = ["30%", "40%", "50%", "60%", "70%", "80%"];
  s.addChart(pres.charts.LINE, [
    { name: "Blended margin", labels: lx, values: [0.279, 0.292, 0.306, 0.321, 0.340, 0.361] },
  ], chartFrame({
    x: 5.35, y: 2.3, w: 4.3, h: 3.0, chartColors: [NAVY], lineSize: 3, lineDataSymbol: "circle", lineDataSymbolSize: 7,
    valAxisMinVal: 0.24, valAxisMaxVal: 0.39, dataLabelFormatCode: "0%", dataLabelPosition: "t", dataLabelFontSize: 11,
    objectName: "Mix margin chart",
  }));
  s.addText("Light-scope share of jobs (management's job economics)", {
    x: 5.35, y: 5.35, w: 4.3, h: 0.45, margin: 0, align: "center", fontSize: 11, italic: true, color: C.accent2,
    isTextBox: true, objectName: "Mix caption",
  });

  takeaway(s, "When light work returns, every 10 pts of mix adds ~1.5–2 pts of margin, above today's ~30%.");
  source(s, "GPS model (CFM56 Data tab: cohort roll-forward, central case); FTAI earnings call (light vs. heavy job economics)");
  s.addNotes("Cohort roll-forward (central): first visits fall 976 → 598 (2025–2030) as the last 737NG / A320ceo deliveries pass their first run; " +
    "second visits, typically the heaviest, peak at 914 in 2027; third-and-later visits rise 532 → 720. Dashed lines extend the 2029–30 slopes (-42/yr and +20/yr), which cross around 2032. Late-life engines increasingly get green-time-only " +
    "restorations (model assumes 100% / 90% / 70% of due engines get a full visit at <20 / 20–25 / 25+ years). " +
    "Mix curve uses management's example: light job ~$6M revenue / ~$2.5M profit, heavy ~$12M / ~$3.0M; blended margin by share of jobs. " +
    "Caveat: the model's broader-work share still rises from 48% to 52% through 2030, so the light-scope return is a late-cycle (2030+) effect.");
}

// 1a (3/3): PMA parts
{
  const s = pres.addSlide({ masterName: "GPS Content Subtitle", sectionTitle: "Thesis 1a" });
  s.addText("Thesis 1a: Margin Floor (4/4)", { placeholder: "title" });
  s.addText("Cheaper PMA parts add a new margin lever, and our base case uses it sparingly.", { placeholder: "subtitle" });

  sectionHeader(s, "PMA Ramp in Our Model", 0.35, 1.7, 4.6, "PMA ramp header");
  const py = ["FY27E", "FY28E", "FY29E", "FY30E", "FY31E"];
  s.addText("Adoption (% of modules)", {
    x: 0.35, y: 2.28, w: 4.6, h: 0.25, margin: 0, align: "left", fontSize: 11, italic: true, color: C.accent2, isTextBox: true, objectName: "Adoption label",
  });
  s.addChart(pres.charts.LINE, [
    { name: "PMA adoption", labels: py, values: [0.9, 3, 5, 7, 9] },
  ], chartFrame({
    x: 0.35, y: 2.45, w: 4.6, h: 1.05, chartColors: ["B5AEA9"], lineSize: 3, lineDataSymbol: "circle", lineDataSymbolSize: 8,
    catAxisHidden: true, catAxisLineShow: false, valAxisMinVal: 0, valAxisMaxVal: 13, dataLabelFormatCode: "0.0", dataLabelPosition: "t",
    dataLabelColor: PLAT, dataLabelFontSize: 11, objectName: "PMA adoption chart",
  }));
  s.addText("EBITDA uplift ($M)", {
    x: 0.35, y: 3.5, w: 4.6, h: 0.25, margin: 0, align: "left", fontSize: 11, italic: true, color: C.text2, isTextBox: true, objectName: "Uplift label",
  });
  s.addChart(pres.charts.BAR, [
    { name: "PMA EBITDA uplift", labels: py, values: [6, 24, 42, 59, 77] },
  ], chartFrame({
    x: 0.35, y: 3.7, w: 4.6, h: 2.1, barDir: "col", chartColors: [NAVY], barGapWidthPct: 45, valAxisMinVal: 0, valAxisMaxVal: 92,
    dataLabelFormatCode: '"$"0"M"', dataLabelPosition: "outEnd", dataLabelFontSize: 11, objectName: "PMA uplift chart",
  }));

  sectionHeader(s, "Upside If Adoption Runs Faster", 5.35, 1.7, 4.3, "Sensitivity header");
  const ad = ["0%", "10%", "20%", "30%", "40%", "50%"];
  s.addChart(pres.charts.LINE, [
    { name: "AP EBITDA ($M)", labels: ad, values: [1132, 1225, 1318, 1411, 1504, 1597] },
  ], chartFrame({
    x: 5.35, y: 2.3, w: 4.3, h: 3.0, chartColors: [NAVY], lineSize: 3, lineDataSymbol: "circle", lineDataSymbolSize: 7,
    valAxisMinVal: 1000, valAxisMaxVal: 1700, dataLabelFormatCode: '"$"#,##0', dataLabelPosition: "t", dataLabelFontSize: 11,
    objectName: "PMA sensitivity chart",
  }));
  s.addText("FY26E Aerospace EBITDA ($M) at 1,200 modules vs. PMA adoption (Jefferies)", {
    x: 5.35, y: 5.35, w: 4.3, h: 0.45, margin: 0, align: "center", fontSize: 11, italic: true, color: C.accent2, isTextBox: true, objectName: "Sensitivity caption",
  });

  takeaway(s, "3 of 5 Chromalloy parts are approved, and every 5 pts of adoption adds ~$43M of EBITDA.");
  source(s, "GPS model (RPM tab: PMA penetration × $0.4M uplift per module); Jefferies estimates; FAA PMA data");
  s.addNotes("Our model: PMA penetration 0.9% FY27E rising to 9% FY31E at $0.4M EBITDA uplift per PMA module = $6M to $77M. " +
    "Jefferies estimates ~$0.8M uplift per PMA module and ~$43M of 2026E Aerospace EBITDA per 5 pts of adoption, so our case is conservative on both rate and uplift. " +
    "Chromalloy JV program: 3 of 5 parts approved (LPT stage 1 vane 2021, HPT stage 1 vane Oct 2024, HPT stage 1 blade Oct 2025), covering ~80% of targeted savings; 2 in FAA review.");
}

// ---------- Thesis 1b: Share Gains (5 slides) ----------
pres.addSection({ title: "Thesis 1b" });

// 1b (1/5): why FTAI can take share — TATT "How TATT Fits In" architecture
{
  const s = pres.addSlide({ masterName: "GPS Content", sectionTitle: "Thesis 1b" });
  s.addText("Thesis 1b: Share Gains (1/5)", { placeholder: "title" });
  const rows = [
    "OEM shops are moving their capacity to LEAP, leaving CFM56 work behind.",
    "Independent MROs are clogged: CFM56 overhauls now take 90–120 days.",
    "FTAI's module swap returns an engine in 5–25 days, not months.",
    "New sites in Jakarta, Cairo and Lisbon lift capacity to 3,000 modules.",
  ];
  const boxX = 1.75, boxW = 7.25, boxH = 0.78, circ = 0.86;
  rows.forEach((t, i) => {
    const y = 1.2 + i * 1.0;
    s.addText(t, {
      x: boxX, y, w: boxW, h: boxH, fill: { color: PLAT_LT }, align: "center", valign: "middle",
      fontSize: 15, bold: true, color: C.text2, margin: [44, 10, 2, 2], isTextBox: true, objectName: `Reason ${i + 1}`,
    });
    s.addText(String(i + 1), {
      shape: pres.shapes.OVAL, x: boxX - circ / 2 - 0.05, y: y + boxH / 2 - circ / 2, w: circ, h: circ,
      fill: { color: "FFFFFF" }, line: { color: NAVY, width: 2 }, align: "center", valign: "middle",
      fontSize: 24, bold: true, color: C.text2, margin: 0, objectName: `Reason ${i + 1} number`,
    });
  });
  s.addShape(pres.shapes.ISOSCELES_TRIANGLE, {
    x: 1.3, y: 5.15, w: 7.7, h: 0.4, fill: { color: PLAT_LT }, line: { type: "none" }, flipV: true, objectName: "Funnel",
  });
  s.addText("FTAI's share of CFM56 module work rises from ~12% to 20% by FY30, with every SCI aircraft as a contracted floor.", {
    x: 1.3, y: 5.68, w: 7.7, h: 0.85, fill: { color: NAVY }, align: "center", valign: "middle",
    fontSize: 16, bold: true, color: C.background1, margin: [10, 10, 2, 2], isTextBox: true, objectName: "Conclusion",
  });
  source(s, "GE Aerospace earnings calls (2026), Aviation Business News (2025), FTAI Q2'24 call and Q2'26 supplement, GPS model");
}

// 1b (2/5): then vs. now — MROs clogged, OEMs moving to LEAP
{
  const s = pres.addSlide({ masterName: "GPS Content Subtitle", sectionTitle: "Thesis 1b" });
  s.addText("Thesis 1b: Share Gains (2/5)", { placeholder: "title" });
  s.addText("Independent shops are clogged, and OEMs are pouring new capacity into LEAP, not CFM56.", { placeholder: "subtitle" });

  sectionHeader(s, "Independent Shops Are Clogged…", 0.35, 1.7, 4.4, "MRO header");
  s.addChart(pres.charts.BAR, [
    { name: "Pre-COVID", labels: ["Pre-COVID", "Today"], values: [60, null] },
    { name: "Today (low)", labels: ["Pre-COVID", "Today"], values: [null, 90] },
    { name: "Today (range)", labels: ["Pre-COVID", "Today"], values: [null, 30] },
  ], chartFrame({
    x: 0.6, y: 2.45, w: 2.5, h: 2.05, barDir: "col", barGrouping: "stacked", barGapWidthPct: 45,
    chartColors: ["B5AEA9", NAVY, "3B4C82"], valAxisMinVal: 0, valAxisMaxVal: 140, showValue: false, objectName: "Overhaul days chart",
  }));
  s.addText("~60", { x: 0.75, y: 3.2, w: 1.0, h: 0.3, margin: 0, align: "center", fontSize: 15, bold: true, color: INK, isTextBox: true, objectName: "Pre-COVID days" });
  s.addText("90–120", { x: 1.9, y: 2.3, w: 1.1, h: 0.3, margin: 0, align: "center", fontSize: 15, bold: true, color: C.text2, isTextBox: true, objectName: "Today days" });
  s.addText("CFM56 overhaul, days", { x: 0.6, y: 4.52, w: 2.5, h: 0.26, margin: 0, align: "center", fontSize: 11, italic: true, color: C.accent2, isTextBox: true, objectName: "Days caption" });
  s.addText([{ text: "+2–6", options: { fontSize: 24, bold: true, color: C.text2, breakLine: true } }, { text: "months just to get a shop slot", options: { fontSize: 11, color: INK } }], {
    x: 3.15, y: 2.75, w: 1.6, h: 1.3, align: "center", valign: "middle", margin: 0, isTextBox: true, objectName: "Slot wait stat",
  });

  sectionHeader(s, "…While OEMs Pivot to LEAP", 5.25, 1.7, 4.4, "OEM header");
  const ly = ["2025", "2030E"];
  s.addChart(pres.charts.BAR, [
    { name: "CFM56", labels: ly, values: [0.68, 0.49] },
    { name: "LEAP", labels: ly, values: [0.32, 0.51] },
  ], chartFrame({
    x: 5.35, y: 2.45, w: 2.45, h: 2.05, barDir: "col", barGrouping: "percentStacked", barGapWidthPct: 40,
    chartColors: ["B5AEA9", NAVY], valAxisHidden: true, dataLabelFormatCode: "0%", dataLabelPosition: "ctr", dataLabelColor: "FFFFFF",
    dataLabelFontSize: 13, objectName: "Shop visit mix chart",
  }));
  s.addText([{ text: "■ ", options: { color: "B5AEA9" } }, { text: "CFM56  " }, { text: "■ ", options: { color: NAVY } }, { text: "LEAP" }], {
    x: 5.35, y: 4.52, w: 2.45, h: 0.26, margin: 0, align: "center", fontSize: 11, color: INK, isTextBox: true, objectName: "Mix legend",
  });
  [["~1/2", "of GE's $1B+ MRO spend goes to LEAP"], ["+50%", "LEAP shop visits, y/y (GE, 2026)"]].forEach(([big, lab], i) => {
    s.addText([{ text: big, options: { fontSize: 22, bold: true, color: C.text2, breakLine: true } }, { text: lab, options: { fontSize: 11, color: INK } }], {
      x: 7.85, y: 2.45 + i * 1.1, w: 1.8, h: 1.0, align: "center", valign: "middle", margin: 0, isTextBox: true, objectName: `LEAP stat ${i + 1}`,
    });
  });

  // Expert quote banner (TATT style)
  s.addText([
    { text: "“The variability in capital investment required to capture the LEAP is extremely low versus what it took them to capture the CFM.”", options: { bold: true, breakLine: true } },
    { text: "— Former executive, engine MRO shop", options: { italic: true, fontSize: 12 } },
  ], {
    x: 0.35, y: 4.95, w: 9.3, h: 0.95, fill: { color: PLAT_XLT }, align: "center", valign: "middle", fontSize: 14, color: INK,
    margin: [12, 12, 4, 4], isTextBox: true, objectName: "Expert quote",
  });

  takeaway(s, "OEM slots shift to LEAP as independent shops clog. CFM56 owners need a faster option.");
  source(s, "Aviation Business News (2025); Bain (2024); GE Q4'25–Q2'26 calls; CFM LEAP forecast; GPS model; GPS expert call");
  s.addNotes("CFM56 full overhaul ~60 days pre-pandemic vs. 90–120 days now (Aviation Business News, 2025; secondary source). Slot waits up 2–6 months (Bain, 2024; 2025 market summaries). " +
    "GE: LEAP shop visits up >50% in Q1 and Q2 2026; LEAP installed base to roughly triple 2024–2030; ~$500M of >$1B MRO investment to LEAP, roughly doubling internal LEAP capacity. " +
    "Shop-visit mix: CFM56 2,350 (2025) and 2,150 (2030E) from GPS model; LEAP ~1,100 (2025) and ~2,200 (2030E) per CFM forecast that LEAP visits exceed CFM56 by 2030. " +
    "No source found showing OEMs cutting CFM56 capacity outright; the shift is in where new OEM capacity goes. " +
    "Former MRO executive: 'the variability in capital investment required to capture the LEAP is extremely low versus what it took them to capture the CFM.'");
}

// 1b (3/5): turnaround time walk-through
{
  const s = pres.addSlide({ masterName: "GPS Content Subtitle", sectionTitle: "Thesis 1b" });
  s.addText("Thesis 1b: Share Gains (3/5)", { placeholder: "title" });
  s.addText("A shop visit grounds an engine for months. FTAI's module swap gets it flying in weeks.", { placeholder: "subtitle" });

  // Day-scaled timelines: 180 days = full width
  const tx = 2.35, tw = 7.0, scale = tw / 180;
  s.addText("Days off wing", { x: tx, y: 1.68, w: tw, h: 0.26, margin: 0, align: "left", fontSize: 11, italic: true, color: C.accent2, isTextBox: true, objectName: "Timeline label" });
  [0, 30, 60, 90, 120, 150, 180].forEach((d) => {
    s.addShape(pres.shapes.LINE, { x: tx + d * scale, y: 1.95, w: 0, h: 1.65, line: { color: "E3E0DC", width: 0.75 }, objectName: `Grid ${d}` });
    s.addText(String(d), { x: tx + d * scale - 0.3, y: 3.6, w: 0.6, h: 0.22, margin: 0, align: "center", fontSize: 10, color: C.accent2, isTextBox: true, objectName: `Tick ${d}` });
  });
  s.addText([{ text: "Typical shop visit", options: { bold: true, breakLine: true } }, { text: "120–180 days", options: { fontSize: 12 } }], {
    x: 0.35, y: 2.0, w: 1.9, h: 0.6, margin: 0, align: "right", valign: "middle", fontSize: 14, color: INK, isTextBox: true, objectName: "Shop visit label",
  });
  const steps = [["Wait for slot", 40], ["Strip", 28], ["Wait for parts", 40], ["Repair", 32], ["Test", 10]];
  let cx = tx;
  steps.forEach(([name, d], i) => {
    const w = d * scale;
    s.addText(name, {
      shape: pres.shapes.CHEVRON, x: cx, y: 2.03, w: w + 0.12, h: 0.55, fill: { color: i % 2 ? "B5AEA9" : PLAT_LT }, line: { type: "none" },
      align: "center", valign: "middle", fontSize: 9, bold: true, color: C.text2, margin: 0, objectName: `Shop step ${i + 1}`,
    });
    cx += w;
  });
  s.addShape(pres.shapes.RECTANGLE, { x: cx, y: 2.11, w: 30 * scale, h: 0.39, fill: { type: "none" }, line: { color: "B5AEA9", width: 1.25, dashType: "dash" }, objectName: "Shop visit range" });
  s.addText([{ text: "FTAI module swap", options: { bold: true, breakLine: true } }, { text: "5–25 days", options: { fontSize: 12 } }], {
    x: 0.25, y: 2.8, w: 2.0, h: 0.6, margin: 0, align: "right", valign: "middle", fontSize: 13, color: C.text2, isTextBox: true, objectName: "Swap label",
  });
  s.addShape(pres.shapes.CHEVRON, { x: tx, y: 2.83, w: 25 * scale + 0.12, h: 0.55, fill: { color: NAVY }, line: { type: "none" }, objectName: "Swap bar" });
  s.addText("Swap a restored module from FTAI's pool, test, fly", {
    x: tx + 25 * scale + 0.25, y: 2.83, w: 3.6, h: 0.55, margin: 0, align: "left", valign: "middle", fontSize: 12, bold: true, color: C.text2,
    isTextBox: true, objectName: "Swap description",
  });
  s.addText([{ text: "~7x", options: { fontSize: 22, bold: true, breakLine: true } }, { text: "faster", options: { fontSize: 11, bold: true } }], {
    shape: pres.shapes.OVAL, x: 8.3, y: 2.65, w: 1.15, h: 0.95, fill: { color: NAVY }, line: { color: NAVY },
    align: "center", valign: "middle", color: C.background1, margin: 0, objectName: "Speed callout",
  });

  // Cost of downtime: spare-engine lease while grounded
  sectionHeader(s, "Lease Cost While Grounded", 0.35, 3.92, 4.55, "Cost header");
  // Two-bar comparison drawn to scale ($K); 493 → 2.2"
  const bx = 2.3, bmax = 1.9, bscale = bmax / 493;
  [["Shop visit, ~150 days", 493, NAVY], ["FTAI swap, ~20 days", 66, "B5AEA9"]].forEach(([lab, v, col], i) => {
    const y = 4.55 + i * 0.52;
    s.addText(lab, { x: 0.35, y, w: bx - 0.45, h: 0.38, margin: 0, align: "right", valign: "middle", fontSize: 11, color: INK, isTextBox: true, objectName: `Cost label ${i + 1}` });
    s.addShape(pres.shapes.RECTANGLE, { x: bx, y, w: v * bscale, h: 0.38, fill: { color: col }, line: { type: "none" }, objectName: `Cost bar ${i + 1}` });
    s.addText(`$${v}K`, { x: bx + v * bscale + 0.08, y, w: 0.8, h: 0.38, margin: 0, align: "left", valign: "middle", fontSize: 13, bold: true, color: C.text2, isTextBox: true, objectName: `Cost value ${i + 1}` });
  });
  s.addText("~$430K saved per visit (IBA lease rate, ~$100K/mo)", {
    x: 0.35, y: 5.62, w: 4.55, h: 0.28, margin: 0, align: "center", fontSize: 11, italic: true, color: C.accent2, isTextBox: true, objectName: "Cost caption",
  });

  // Expert quote
  s.addText([
    { text: "“FTAI's advantage is basically turnaround time and cheaper sourcing.”", options: { bold: true, fontSize: 16, breakLine: true } },
    { text: "— Industry expert, GPS expert call", options: { italic: true, fontSize: 12 } },
  ], {
    x: 5.15, y: 4.0, w: 4.5, h: 1.9, fill: { color: PLAT_XLT }, align: "center", valign: "middle", color: INK,
    margin: [14, 14, 6, 6], paraSpaceAfter: 6, isTextBox: true, objectName: "Turnaround expert quote",
  });

  takeaway(s, "Every day an engine is off wing costs the airline a jet. FTAI sells that time back.");
  source(s, "FTAI Q2'24 call via third-party analysis; IBA (2024) lease rates; GPS expert call; step lengths illustrative");
  s.addNotes("FTAI (Q2'24 call, as reported by third parties): average CFM56 engine turnaround ~120–180 days vs. 5–25 days for a module swap. Midpoints 150 vs. ~20 days = ~7x. " +
    "Step lengths within the shop visit are illustrative; slot waits of 2–6 months and HPT blade shortages drive most of the delay. " +
    "Caveat: the fastest swaps apply where the core does not need to be opened; roughly half of shop visits require core disassembly. " +
    "Cost chart: IBA puts CFM56-7B spare-engine lease rates at ~$100K/month in 2024 (up from ~$75K in 2019), ~$3.3K/day. 150 days = ~$493K vs. 20 days = ~$66K. " +
    "Lease cost only; lost flying revenue on a grounded jet (often $10K+ per day) would widen the gap.");
}

// 1b (4/5): new capacity
{
  const s = pres.addSlide({ masterName: "GPS Content Subtitle", sectionTitle: "Thesis 1b" });
  s.addText("Thesis 1b: Share Gains (4/5)", { placeholder: "title" });
  s.addText("FTAI built capacity ahead of demand. New sites leave room to keep taking share.", { placeholder: "subtitle" });

  sectionHeader(s, "Output vs. Capacity (Modules)", 0.35, 1.7, 4.6, "Capacity header");
  const cc = ["2025", "2026E", "2027E"];
  s.addChart(pres.charts.BAR, [
    { name: "Output", labels: cc, values: [757, 1200, 1700] },
    { name: "Unused capacity", labels: cc, values: [null, 1800, 1300] },
  ], chartFrame({
    x: 0.35, y: 2.3, w: 4.6, h: 3.2, barDir: "col", barGrouping: "stacked", barGapWidthPct: 45, chartColors: [NAVY, "B5AEA9"],
    valAxisMinVal: 0, valAxisMaxVal: 3300, dataLabelFormatCode: "#,##0;;;", dataLabelPosition: "inEnd", dataLabelColor: "FFFFFF",
    dataLabelFontSize: 13, objectName: "Capacity chart",
  }));
  s.addText("3,000 capacity", { x: 2.0, y: 2.3, w: 2.9, h: 0.3, margin: 0, align: "center", fontSize: 12, bold: true, italic: true, color: C.accent2, isTextBox: true, objectName: "Capacity label" });
  s.addText([{ text: "■ ", options: { color: NAVY } }, { text: "Output   " }, { text: "■ ", options: { color: "B5AEA9" } }, { text: "Unused capacity" }], {
    x: 0.35, y: 5.52, w: 4.6, h: 0.28, margin: 0, align: "center", fontSize: 11, color: INK, isTextBox: true, objectName: "Capacity legend",
  });

  sectionHeader(s, "The Network", 5.35, 1.7, 4.3, "Network header");
  const sites = [
    ["Montreal", "Flagship, up to 900", false], ["Miami", "~475 in 2026E", false], ["Rome", "Ramping", false],
    ["Lisbon", "Heading to 300+", true], ["Jakarta", "Heavy work, 300–450 (E)", true], ["Cairo", "Light work, 150–180 (E)", true],
  ];
  sites.forEach(([name, cap, isNew], i) => {
    const col = i % 2, row = Math.floor(i / 2);
    const x = 5.35 + col * 2.2, y = 2.3 + row * 1.08;
    s.addText([{ text: name, options: { fontSize: 15, bold: true, breakLine: true } }, { text: cap, options: { fontSize: 11 } }], {
      x, y, w: 2.1, h: 0.95, fill: { color: isNew ? NAVY : PLAT_LT }, color: isNew ? C.background1 : C.text2,
      align: "center", valign: "middle", margin: 4, isTextBox: true, objectName: `Site ${name}`,
    });
  });
  s.addText([{ text: "■ ", options: { color: NAVY } }, { text: "New sites   " }, { text: "■ ", options: { color: "DCD8D3" } }, { text: "Existing (modules / yr)" }], {
    x: 5.35, y: 5.52, w: 4.3, h: 0.28, margin: 0, align: "center", fontSize: 11, color: INK, isTextBox: true, objectName: "Network legend",
  });

  takeaway(s, "With 3,000 modules of capacity against 1,700 planned, FTAI can absorb share gains.");
  source(s, "FTAI Q1/Q2'26 earnings supplements; GMF and EgyptAir reports; GPS estimates (E)");
  s.addNotes("Network output 757 modules in 2025, 1,200 guided for 2026 (Montreal 450, Miami 475, Europe 275) and 1,700 targeted for 2027 including GMF and EgyptAir. " +
    "Network capacity raised from 2,000 to 3,000 modules in 2026. Montreal capacity up to 900 (377 output in 2025). Jakarta 300–450 and Cairo 150–180 are GPS estimates; partners are ~7–18% of 2027 output.");
}

// 1b (5/5): share gains and the volume math
{
  const s = pres.addSlide({ masterName: "GPS Content Subtitle", sectionTitle: "Thesis 1b" });
  s.addText("Thesis 1b: Share Gains (5/5)", { placeholder: "title" });
  s.addText("Share gains plus the SCI floor take FTAI to ~1,700 modules in FY27, in line with its target.", { placeholder: "subtitle" });

  // Volume math tiles (FY27E)
  const tiles = [["2,386", "CFM56 shop visits"], ["× 3", "modules each"], ["× 16.8%", "FTAI share"], ["+ 482", "SCI modules"], ["= 1,687", "FY27E modules"]];
  const tw = 1.72, tg = 0.17;
  tiles.forEach(([big, lab], i) => {
    const x = 0.35 + i * (tw + tg), last = i === tiles.length - 1;
    s.addText([{ text: big, options: { fontSize: 20, bold: true, breakLine: true } }, { text: lab, options: { fontSize: 11 } }], {
      x, y: 1.75, w: tw, h: 0.95, fill: { color: last ? NAVY : PLAT_LT }, color: last ? C.background1 : C.text2,
      align: "center", valign: "middle", margin: 2, isTextBox: true, objectName: `Volume tile ${i + 1}`,
    });
  });

  sectionHeader(s, "FTAI Share of CFM56 Module Work", 0.35, 2.85, 4.6, "Share header");
  const sy = ["2024", "2025", "2026E", "2027E", "2028E", "2029E", "2030E"];
  s.addChart(pres.charts.BAR, [
    { name: "Reported", labels: sy, values: [0.04, 0.08, null, null, null, null, null] },
    { name: "GPS model", labels: sy, values: [null, null, 0.124, 0.168, 0.19, 0.195, 0.20] },
  ], chartFrame({
    x: 0.35, y: 3.4, w: 4.6, h: 2.45, barDir: "col", barGrouping: "clustered", barOverlapPct: 100, barGapWidthPct: 35,
    chartColors: [NAVY, "B5AEA9"], valAxisMinVal: 0, valAxisMaxVal: 0.25, catAxisLabelFontSize: 10,
    dataLabelFormatCode: "0%", dataLabelPosition: "outEnd", dataLabelFontSize: 11, objectName: "Share chart",
  }));

  sectionHeader(s, "FTAI Modules Produced", 5.35, 2.85, 4.3, "Modules header");
  const my = ["2025", "2026E", "2027E", "2028E", "2029E", "2030E"];
  s.addChart(pres.charts.BAR, [
    { name: "Third-party", labels: my, values: [675, 866, 1206, 1321, 1298, 1272] },
    { name: "SCI (contracted)", labels: my, values: [82, 328, 482, 660, 780, 840] },
  ], chartFrame({
    x: 5.35, y: 3.4, w: 4.3, h: 2.2, barDir: "col", barGrouping: "stacked", barGapWidthPct: 35, chartColors: [NAVY, "B5AEA9"],
    valAxisMinVal: 0, valAxisMaxVal: 2300, showValue: false, catAxisLabelFontSize: 10, objectName: "Modules chart",
  }));
  s.addText([{ text: "■ ", options: { color: NAVY } }, { text: "Third-party   " }, { text: "■ ", options: { color: "B5AEA9" } }, { text: "SCI floor" }], {
    x: 5.35, y: 5.6, w: 4.3, h: 0.25, margin: 0, align: "center", fontSize: 11, color: INK, isTextBox: true, objectName: "Modules legend",
  });

  takeaway(s, "Even if share stalls, SCI's contracted fleet keeps adding volume: a floor under the thesis.");
  source(s, "GPS model (RPM tab); 2024–25 share per GPS analysis; FTAI 2027 target of 1,700 modules (Q2'26 supplement)");
  s.addNotes("Volume math (FY27E, GPS model): 2,386 CFM56 shop visits × 3 modules = 7,159 modules of demand × 16.8% FTAI share = 1,206 third-party modules, " +
    "plus 482 SCI modules (450 aircraft × 2 engines × 20% shop-visit rate × 3 modules, approx.) = 1,687, vs. FTAI's 1,700 target. " +
    "Share path 12.4% FY26E → 20% by FY30E. 2025 split approximates SCI at 82 modules and the remainder third-party.");
}

// ---------- Thesis 1b: The LEAP Option (2 slides) ----------
// LEAP (1/2): TATT "APU Licenses" timeline architecture
{
  const s = pres.addSlide({ masterName: "GPS Content Subtitle", sectionTitle: "Thesis 1b" });
  s.addText("Thesis 1b: The LEAP Option (1/2)", { placeholder: "title" });
  s.addText("LEAP engines need more maintenance, and OEM contracts start rolling off after 2030.", { placeholder: "subtitle" });

  // Timeline arrow
  s.addShape(pres.shapes.RIGHT_ARROW, { x: 0.35, y: 1.95, w: 9.3, h: 0.5, fill: { color: NAVY }, line: { type: "none" }, objectName: "Timeline arrow" });
  const stops = [
    ["Today", "~50% of LEAPs on OEM deals", "vs. ~15% of CFM56s"],
    ["2030", "~2,000 LEAP visits a year", "OEM coverage peaks near 70%"],
    ["2030+", "Contracts roll off", "Work opens to independents"],
  ];
  stops.forEach(([when, head, sub], i) => {
    const x = 0.75 + i * 3.1;
    s.addText(when, {
      x, y: 1.78, w: 2.3, h: 0.84, fill: { color: "FFFFFF" }, line: { color: NAVY, width: 2 }, align: "center", valign: "middle",
      fontSize: 22, bold: true, color: C.text2, margin: 0, isTextBox: true, objectName: `Stop ${i + 1}`,
    });
    s.addText([{ text: head, options: { bold: true, fontSize: 14, color: C.text2, breakLine: true } }, { text: sub, options: { fontSize: 12, color: INK } }], {
      x: x - 0.25, y: 2.72, w: 2.8, h: 0.7, align: "center", valign: "top", margin: 0, isTextBox: true, objectName: `Stop ${i + 1} detail`,
    });
  });

  // Three cards: why LEAP matters to FTAI
  const cards = [
    ["2.5x", "sooner", "More shop visits", "First LEAP visits at ~4,000 cycles vs. the 10,000+ originally planned."],
    ["$2–4.5M", "per visit", "Costlier visits", "LEAP overhauls cost far more than the same work on a CFM56."],
    ["Same", "tooling", "FTAI can pivot fast", "A CFM56/LEAP test cell is coming to Rome, and CFM56 tools and techs carry over."],
  ];
  cards.forEach(([big, unit, head, body], i) => {
    const x = 0.35 + i * 3.17;
    s.addShape(pres.shapes.RECTANGLE, { x, y: 3.6, w: 2.96, h: 2.25, fill: { color: PLAT_XLT }, line: { type: "none" }, objectName: `Card ${i + 1}` });
    s.addText([{ text: big, options: { fontSize: big.length > 5 ? 14 : 20, bold: true, breakLine: true } }, { text: unit, options: { fontSize: 10 } }], {
      shape: pres.shapes.OVAL, x: x + 0.1, y: 3.72, w: 1.25, h: 1.25, fill: { color: i === 2 ? NAVY : "FFFFFF" },
      line: { color: NAVY, width: 2 }, color: i === 2 ? C.background1 : C.text2, align: "center", valign: "middle", margin: 0,
      objectName: `Card ${i + 1} stat`,
    });
    s.addText(head, { x: x + 1.42, y: 3.85, w: 1.5, h: 0.95, margin: 0, align: "left", valign: "middle", fontSize: 15, bold: true, color: C.text2, isTextBox: true, objectName: `Card ${i + 1} head` });
    s.addText(body, { x: x + 0.15, y: 5.0, w: 2.66, h: 0.8, margin: 0, align: "left", valign: "top", fontSize: 12, color: INK, isTextBox: true, objectName: `Card ${i + 1} body` });
  });

  takeaway(s, "As OEM contracts roll off, LEAP becomes FTAI's next CFM56, with costlier, more frequent visits.");
  source(s, "Safran via Aviation Week; Visual Approach; The Air Current; Safe Fly Aviation; FTAI Q2'26 call; GPS expert call");
  s.addNotes("LTSA coverage: Safran estimates ~50% of ~5,500 in-service LEAPs are on long-term agreements vs. ~15% of CFM56s, peaking near 70% in 2030 before shifting back to time-and-materials (Aviation Week). " +
    "LEAP overhauls ~2,000 a year by 2030, roughly matching CFM56 (Aviation Week). First LEAP shop visits clustering at 2,000–6,000 cycles with ~4,000 as a planning base, vs. 10,000+ originally expected (Visual Approach). " +
    "LEAP-1A/1B shop visit $2.0–4.5M+ before LLPs (Safe Fly, unsourced benchmark); The Air Current: the overhaul far eclipses the cost of the same work on a CFM56. " +
    "FTAI: CFM56/LEAP test cell planned at Rome as its entry into next-generation engine maintenance (Q2'26 call coverage). No public LEAP repair licence found; confirm before presenting. " +
    "Former MRO executive: the machines and capital equipment for LEAP are 'very near that for CFM'.");
}

// LEAP (2/2): TATT "APU Summary" architecture — your return vs. LEAP share
{
  const s = pres.addSlide({ masterName: "GPS Content Subtitle", sectionTitle: "Thesis 1b" });
  s.addText("Thesis 1b: The LEAP Option (2/2)", { placeholder: "title" });
  s.addText("LEAP isn't in our target. Matching FTAI's CFM56 share takes your return past 100%.", { placeholder: "subtitle" });

  // Quote banner with attribution set below, TATT style
  s.addText("“It will happen. The reason why it will happen is because they have set their CFM line up to have a measurable amount of shared services in that line.”", {
    x: 0.9, y: 1.78, w: 8.2, h: 0.95, fill: { color: PLAT_XLT }, align: "left", valign: "middle", fontSize: 16, bold: true, color: INK,
    margin: [14, 14, 4, 4], isTextBox: true, objectName: "LEAP quote",
  });
  s.addText("— Former executive, engine MRO shop", {
    x: 4.6, y: 2.78, w: 4.5, h: 0.3, margin: 0, align: "right", fontSize: 14, bold: true, italic: true, color: INK,
    isTextBox: true, objectName: "LEAP quote attribution",
  });

  // Your return vs. LEAP share: platinum bars, 20% (FTAI's CFM56 share) in navy
  const shares = ["0% (base)", "5%", "10%", "15%", "20% (CFM56)", "25%"];
  s.addChart(pres.charts.BAR, [
    { name: "Your return", labels: shares, values: [0.66, 0.74, 0.83, 0.92, null, 1.09] },
    { name: "Matches CFM56 share", labels: shares, values: [null, null, null, null, 1.01, null] },
  ], chartFrame({
    x: 1.05, y: 3.2, w: 8.4, h: 2.35, barDir: "col", barGrouping: "clustered", barOverlapPct: 100, barGapWidthPct: 55,
    chartColors: ["B5AEA9", NAVY], valAxisMinVal: 0, valAxisMaxVal: 1.25, dataLabelFormatCode: "0%", dataLabelPosition: "outEnd",
    dataLabelFontSize: 14, catAxisLabelColor: NAVY, catAxisLabelFontSize: 13, objectName: "LEAP return chart",
  }));
  s.addText("Your return", {
    x: 0.0, y: 4.05, w: 1.5, h: 0.35, margin: 0, align: "center", valign: "middle", fontSize: 12, bold: true, color: INK, rotate: 270,
    isTextBox: true, objectName: "Y label",
  });
  s.addText("FTAI share of off-contract LEAP shop visits", {
    x: 1.05, y: 5.58, w: 8.4, h: 0.28, margin: 0, align: "center", fontSize: 12, bold: true, color: INK, isTextBox: true, objectName: "X label",
  });

  takeaway(s, "Every 5 pts of off-contract LEAP share adds ~9 pts to your return on top of our base case.");
  source(s, "GPS analysis: 2,000 LEAP visits/yr, 50% off contract, 3 modules/visit, FY27E EBITDA/module, 16x, discounted 4 yrs at 9.5%");
  s.addNotes("Return = (base-case SOTP $276.65 + LEAP value per share) / $167.03 − 1. LEAP value: 2,000 LEAP shop visits a year (Aviation Week, ~2030) × 50% off OEM contracts " +
    "(coverage falling back from the ~70% 2030 peak) × FTAI share × 3 modules per visit × $0.913M EBITDA per module (FY27E CFM56 level; LEAP visits cost more, so conservative) × 16x Aerospace multiple, " +
    "discounted four years at the 9.5% WACC. Each point of share ≈ $2.93/share. 20% share (FTAI's FY28E+ CFM56 share) ≈ $548M EBITDA and +$59/share → 101% return.");
}

// ---------- Thesis 2: Power (4 slides) ----------
pres.addSection({ title: "Thesis 2" });

// T2 (1/4): demand outruns the grid
{
  const s = pres.addSlide({ masterName: "GPS Content Subtitle", sectionTitle: "Thesis 2" });
  s.addText("Thesis 2: Power (1/4)", { placeholder: "title" });
  s.addText("AI spending is exploding, and our model shows the grid falling short from 2029.", { placeholder: "subtitle" });

  sectionHeader(s, "Big Four Hyperscaler Capex ($B)", 0.35, 1.7, 4.6, "Capex header");
  const cy = ["2019", "2020", "2021", "2022", "2023", "2024", "2025", "2026E"];
  s.addChart(pres.charts.BAR, [
    { name: "Reported", labels: cy, values: [69, 95, 128, 151, 147, 228, 376, null] },
    { name: "Guided", labels: cy, values: [null, null, null, null, null, null, null, 733] },
  ], chartFrame({
    x: 0.35, y: 2.3, w: 4.6, h: 3.5, barDir: "col", barGrouping: "clustered", barOverlapPct: 100, barGapWidthPct: 35,
    chartColors: ["B5AEA9", NAVY], valAxisMinVal: 0, valAxisMaxVal: 820, catAxisLabelFontSize: 10,
    dataLabelFormatCode: "#,##0", dataLabelPosition: "outEnd", dataLabelFontSize: 11, objectName: "Capex chart",
  }));

  sectionHeader(s, "U.S. Power Reserve Shortfall (GW)", 5.35, 1.7, 4.3, "Shortfall header");
  const sy = ["2026", "2027", "2028", "2029", "2030", "2031"];
  s.addChart(pres.charts.BAR, [
    { name: "Shortfall", labels: sy, values: [0, 0, 0, 8.4, 27.2, 47.2] },
  ], chartFrame({
    x: 5.35, y: 2.3, w: 4.3, h: 3.2, barDir: "col", barGapWidthPct: 35, chartColors: [NAVY],
    valAxisMinVal: 0, valAxisMaxVal: 54, dataLabelFormatCode: "0.0;;0", dataLabelPosition: "outEnd", dataLabelFontSize: 12,
    objectName: "Shortfall chart",
  }));
  s.addText("Capacity below required reserve margin, NERC regions (GPS model)", {
    x: 5.35, y: 5.5, w: 4.3, h: 0.3, margin: 0, align: "center", fontSize: 10, italic: true, color: C.accent2, isTextBox: true, objectName: "Shortfall caption",
  });

  takeaway(s, "Hyperscalers will spend ~$730B this year, but there won't be enough power to run it.");
  source(s, "Company filings and 2026 guidance (Amazon, Alphabet, Meta, Microsoft); NERC; GPS model (Power outlook, Regional model tabs)");
  s.addNotes("Big Four cash capex: $69B (2019) → $376B (2025); 2026 guidance midpoints sum to ~$733B. Reserve shortfall = required capacity (NERC demand × reserve margin) minus anticipated capacity " +
    "and contracted additions, summed across NERC regions: 8.4 GW in 2029 (PJM), 27.2 GW in 2030 (PJM, MISO), 47.2 GW in 2031. US data center energy demand rises from ~298 TWh (2026) to ~649 TWh (2030).");
}

// T2 (2/4): new supply arrives too late — the bridge
{
  const s = pres.addSlide({ masterName: "GPS Content Subtitle", sectionTitle: "Thesis 2" });
  s.addText("Thesis 2: Power (2/4)", { placeholder: "title" });
  s.addText("Most new power hyperscalers have contracted isn't fully online until 2029 or later.", { placeholder: "subtitle" });

  sectionHeader(s, "New Capacity by Online Date (GW)", 0.35, 1.7, 5.0, "COD header");
  const yrs = ["≤2026", "2027", "2028", "2029", "2030", "2031", "2032+"];
  s.addChart(pres.charts.BAR, [
    { name: "Before 2029", labels: yrs, values: [1.8, 5.7, 3.3, null, null, null, null] },
    { name: "2029 or later", labels: yrs, values: [null, null, null, 3.1, 2.2, 6.2, 3.0] },
  ], chartFrame({
    x: 0.35, y: 2.3, w: 5.0, h: 3.2, barDir: "col", barGrouping: "clustered", barOverlapPct: 100, barGapWidthPct: 35,
    chartColors: ["B5AEA9", NAVY], valAxisMinVal: 0, valAxisMaxVal: 7.5, catAxisLabelFontSize: 11,
    dataLabelFormatCode: "0.0", dataLabelPosition: "outEnd", dataLabelFontSize: 12, objectName: "COD chart",
  }));
  s.addText([{ text: "57%", options: { fontSize: 22, bold: true, breakLine: true } }, { text: "2029 or later", options: { fontSize: 10, bold: true } }], {
    shape: pres.shapes.OVAL, x: 2.95, y: 2.3, w: 1.1, h: 1.1, fill: { color: NAVY }, line: { color: NAVY },
    align: "center", valign: "middle", color: C.background1, margin: 0, objectName: "Late share callout",
  });
  s.addText("25 GW of new and restarted capacity across 45 tracked hyperscaler power deals", {
    x: 0.35, y: 5.5, w: 5.0, h: 0.3, margin: 0, align: "center", fontSize: 10, italic: true, color: C.accent2, isTextBox: true, objectName: "COD caption",
  });

  // The bridge
  sectionHeader(s, "The Bridge", 5.7, 1.7, 3.95, "Bridge header");
  const steps = [
    ["Today", "GPUs bought, data center shells built", PLAT_LT, C.text2],
    ["2026–2029", "FTAI's mobile turbines power the site", NAVY, C.background1],
    ["2029+", "Grid connections and new plants arrive", PLAT_LT, C.text2],
  ];
  steps.forEach(([when, what, fill, col], i) => {
    const y = 2.35 + i * 1.12;
    s.addText([{ text: when, options: { fontSize: 16, bold: true, breakLine: true } }, { text: what, options: { fontSize: 12 } }], {
      x: 5.7, y, w: 3.95, h: 0.88, fill: { color: fill }, color: col, align: "center", valign: "middle", margin: 6,
      isTextBox: true, objectName: `Bridge step ${i + 1}`,
    });
    if (i < 2) s.addShape(pres.shapes.DOWN_ARROW, { x: 7.47, y: y + 0.9, w: 0.4, h: 0.2, fill: { color: PLAT }, line: { type: "none" }, objectName: `Bridge arrow ${i + 1}` });
  });

  takeaway(s, "Data centers built today need power now. Transitory units like FTAI's fill the gap.");
  source(s, "GPS model (Power agreements tab: 45 hyperscaler deals, new/restart MW by full COD); company announcements");
  s.addNotes("Power agreements tab: 45 included hyperscaler deals with ~25.3 GW of new or restarted capacity. By full commercial operation date: ≤2026 1.8 GW, 2027 5.7 GW, 2028 3.3 GW, " +
    "2029 3.1 GW, 2030 2.2 GW, 2031 6.2 GW, 2032+ 3.0 GW. 57% is fully online in 2029 or later (38% by first COD). Existing-plant offtake deals (no new MW) are excluded. " +
    "TV risk: a bridge business ends when the grid catches up. Mitigants: the modeled shortfall still widens to 47 GW by 2031; turbines can remain as on-site backup/peaking capacity; " +
    "the SOTP applies 12x to Power vs. 16x for Aerospace, pricing in a shorter life. The DCF does carry Power growth to FY31, so judges may push here.");
}

// T2 (3/4): waiting is expensive, supply is scarce — pricing power
{
  const s = pres.addSlide({ masterName: "GPS Content Subtitle", sectionTitle: "Thesis 2" });
  s.addText("Thesis 2: Power (3/4)", { placeholder: "title" });
  s.addText("Power is a small slice of a data center's cost, and new turbines are sold out. FTAI has pricing power.", { placeholder: "subtitle" });

  sectionHeader(s, "Cost to Build 100 MW ($M)", 0.35, 1.7, 4.3, "Cost header");
  const bars = [["Data center facility", 1200, "B5AEA9"], ["FTAI turbines (6 units)", 150, NAVY]];
  const bx = 2.45, bscale = 1.5 / 1200;
  bars.forEach(([lab, v, col], i) => {
    const y = 2.45 + i * 0.85;
    s.addText(lab, { x: 0.35, y, w: bx - 0.45, h: 0.6, margin: 0, align: "right", valign: "middle", fontSize: 12, color: INK, isTextBox: true, objectName: `Build cost label ${i + 1}` });
    s.addShape(pres.shapes.RECTANGLE, { x: bx, y, w: v * bscale, h: 0.6, fill: { color: col }, line: { type: "none" }, objectName: `Build cost bar ${i + 1}` });
    s.addText(`$${v.toLocaleString("en-US")}M`, { x: bx + v * bscale + 0.08, y, w: 0.9, h: 0.6, margin: 0, align: "left", valign: "middle", fontSize: 13, bold: true, color: C.text2, isTextBox: true, objectName: `Build cost value ${i + 1}` });
  });
  s.addText([{ text: "~13%", options: { fontSize: 26, bold: true, color: C.text2, breakLine: true } }, { text: "of the build cost, with 50% spare units for reliability, before counting the GPUs inside.", options: { fontSize: 12, color: INK } }], {
    x: 0.35, y: 4.3, w: 4.3, h: 1.45, fill: { color: PLAT_XLT }, align: "center", valign: "middle", margin: 10, isTextBox: true, objectName: "Cost takeaway",
  });

  sectionHeader(s, "When New Turbines Can Arrive", 5.0, 1.7, 4.65, "Lead time header");
  const tl0 = 6.75, tlw = 2.85, y0 = 2026, yN = 2031, tscale = tlw / (yN - y0);
  ["2026", "2028", "2030"].forEach((yr) => {
    const x = tl0 + (Number(yr) - y0) * tscale;
    s.addShape(pres.shapes.LINE, { x, y: 2.3, w: 0, h: 2.75, line: { color: "E3E0DC", width: 0.75 }, objectName: `Year grid ${yr}` });
    s.addText(yr, { x: x - 0.3, y: 5.05, w: 0.6, h: 0.25, margin: 0, align: "center", fontSize: 10, color: C.accent2, isTextBox: true, objectName: `Year tick ${yr}` });
  });
  const lanes = [
    ["FTAI Mod-1", 2026.8, 2028.0, NAVY],
    ["New aero orders", 2028.0, 2030.9, "B5AEA9"],
    ["New large turbines", 2029.0, 2031.0, "B5AEA9"],
  ];
  lanes.forEach(([lab, a, b, col], i) => {
    const y = 2.5 + i * 0.85;
    s.addText(lab, { x: 5.0, y, w: 1.65, h: 0.55, margin: 0, align: "right", valign: "middle", fontSize: 12, bold: i === 0, color: i === 0 ? C.text2 : INK, isTextBox: true, objectName: `Lane ${i + 1} label` });
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: tl0 + (a - y0) * tscale, y: y + 0.08, w: (b - a) * tscale, h: 0.4, rectRadius: 0.08, fill: { color: col }, line: { type: "none" }, objectName: `Lane ${i + 1} bar` });
  });
  s.addText("Delivery windows; large-turbine order books full to 2029", {
    x: 5.0, y: 5.4, w: 4.65, h: 0.3, margin: 0, align: "center", fontSize: 10, italic: true, color: C.accent2, isTextBox: true, objectName: "Lead time caption",
  });

  takeaway(s, "Idle data centers cost far more than power. FTAI delivers years before the competition.");
  source(s, "GPS model ($12M/MW facility; ~$1M/MW, 25 MW units, 50% redundancy); CNBC (Jun-26); Tom's Hardware (Oct-25); FTAI calls");
  s.addNotes("Build cost: GPS model assumes ~$12M per MW of data center facility spend, so 100 MW ≈ $1.2B before GPUs; FTAI's contract implies ~$1M per MW; 100 MW of load needs ~150 MW of turbines with the model's 50% redundancy allowance, so six 25 MW Mod-1 units ≈ $150M (~13%). Hot-weather derating could add a unit. " +
    "Lead times: GE Vernova's large gas turbine order book is full until 2029 with orders out to 2031 (CNBC, Jun-26); new aeroderivative orders are being slotted for 2028–2030 (Tom's Hardware, Oct-25). " +
    "FTAI guided first Mod-1 deliveries to Q4'26, later saying it is prudent to expect deliveries in 2027.");
}

// T2 (4/4): returns by contracts signed / units delivered
{
  const s = pres.addSlide({ masterName: "GPS Content Subtitle", sectionTitle: "Thesis 2" });
  s.addText("Thesis 2: Power (4/4)", { placeholder: "title" });
  s.addText("Each new contract the size of FTAI's first adds ~20 points to your return.", { placeholder: "subtitle" });

  sectionHeader(s, "Scenario Build (FY27E)", 0.35, 1.7, 3.75, "Scenario header");
  const rows = [
    ["Signed order", "~50", "$450M", PLAT_LT, C.text2],
    ["+1 contract", "~90", "$750M", "B5AEA9", C.text2],
    ["+2 contracts", "~130", "$1,050M", NAVY, C.background1],
  ];
  s.addText("Units", { x: 1.85, y: 2.22, w: 1.0, h: 0.25, margin: 0, align: "center", fontSize: 11, italic: true, color: C.accent2, isTextBox: true, objectName: "Units col" });
  s.addText("EBITDA", { x: 2.95, y: 2.22, w: 1.15, h: 0.25, margin: 0, align: "center", fontSize: 11, italic: true, color: C.accent2, isTextBox: true, objectName: "EBITDA col" });
  rows.forEach(([name, units, ebitda, fill, col], i) => {
    const y = 2.52 + i * 0.95;
    s.addText(name, { x: 0.35, y, w: 1.45, h: 0.78, fill: { color: fill }, color: col, align: "center", valign: "middle", fontSize: 14, bold: true, margin: 2, isTextBox: true, objectName: `Scenario ${i + 1} name` });
    s.addText(units, { x: 1.85, y, w: 1.0, h: 0.78, align: "center", valign: "middle", fontSize: 14, bold: true, color: C.text2, margin: 0, isTextBox: true, objectName: `Scenario ${i + 1} units` });
    s.addText(ebitda, { x: 2.95, y, w: 1.15, h: 0.78, align: "center", valign: "middle", fontSize: 16, bold: true, color: C.text2, margin: 0, isTextBox: true, objectName: `Scenario ${i + 1} EBITDA` });
  });
  s.addText("Each new ~$1B order ≈ 40 more units and ~$300M of EBITDA", {
    x: 0.35, y: 5.4, w: 3.75, h: 0.4, margin: 0, align: "center", fontSize: 11, italic: true, color: C.accent2, isTextBox: true, objectName: "Scenario caption",
  });

  sectionHeader(s, "Your Return", 4.45, 1.7, 5.2, "Return header");
  const sc = ["No Power", "Signed order", "+1 contract", "+2 contracts"];
  s.addChart(pres.charts.BAR, [
    { name: "Return", labels: sc, values: [0.35, 0.66, null, null] },
    { name: "Upside scenarios", labels: sc, values: [null, null, 0.86, 1.07] },
  ], chartFrame({
    x: 4.45, y: 2.3, w: 5.2, h: 3.15, barDir: "col", barGrouping: "clustered", barOverlapPct: 100, barGapWidthPct: 45,
    chartColors: ["B5AEA9", NAVY], valAxisMinVal: 0, valAxisMaxVal: 1.25, catAxisLabelFontSize: 11, catAxisLabelColor: NAVY,
    dataLabelFormatCode: "0%", dataLabelPosition: "outEnd", dataLabelFontSize: 14, objectName: "Contract return chart",
  }));
  s.addText("Base case = signed order only; returns on the FY27E SOTP vs. $167 today", {
    x: 4.45, y: 5.45, w: 5.2, h: 0.3, margin: 0, align: "center", fontSize: 10, italic: true, color: C.accent2, isTextBox: true, objectName: "Return caption",
  });

  takeaway(s, "Our base case needs no new contracts. Every one FTAI signs is upside the market isn't paying for.");
  source(s, "FTAI earnings calls ($450–750M FY27 guide; 'materially fewer than 100 units'); GPS estimates; GPS model (SOTP, Power at 12x)");
  s.addNotes("Scenarios on FTAI's FY27 Power guide: the signed $1.465B J&F order (est. 40–60 units, ~1.0–1.5 GW) underpins the $450M low end; reaching $750M needs ~$1B of new orders " +
    "(follow-ons under the hyperscaler master agreement or a second customer). A second ~$1B contract is extrapolated at the same ~$300M step to ~$1,050M. Units ≈ $1B / ($1M/MW × 25 MW) ≈ 40 per contract. " +
    "Returns: SOTP ex-Power $224.75 + Power EBITDA × 12 / 104.0M shares, vs. $167.03: no Power 35%, signed order 66% (base case), +1 contract 86%, +2 contracts 107%.");
}

// ---------- Valuation: What You Need to Believe (TATT architecture) ----------
pres.addSection({ title: "Valuation" });
{
  const s = pres.addSlide({ masterName: "GPS Content", sectionTitle: "Valuation" });
  s.addText("Valuation: What You Need to Believe", { placeholder: "title" });

  const beliefs = [
    ["Margins: ~30% is the floor, and PMA parts, OEM-linked pricing and returning light work rebuild them."],
    ["Share: FTAI reaches 20% of CFM56 work by FY30, at half the ~4 pts a year it has already been growing."],
    ["Power: FTAI delivers the order it has already signed."],
  ];
  beliefs.forEach(([t], i) => {
    const y = 1.2 + i * 0.78;
    s.addText(String(i + 1), {
      shape: pres.shapes.OVAL, x: 1.15, y: y + 0.08, w: 0.5, h: 0.5, fill: { color: NAVY }, line: { color: NAVY },
      align: "center", valign: "middle", fontSize: 18, bold: true, color: C.background1, margin: 0, objectName: `Belief ${i + 1} number`,
    });
    s.addText(t, {
      x: 1.85, y, w: 7.2, h: 0.66, margin: 0, align: "left", valign: "middle", fontSize: 16, bold: true, color: C.text2,
      isTextBox: true, objectName: `Belief ${i + 1}`,
    });
  });

  s.addText("Or… just pick one:", {
    x: 0.35, y: 3.62, w: 9.3, h: 0.42, margin: 0, align: "center", fontSize: 20, bold: true, color: INK, isTextBox: true, objectName: "Pick one",
  });

  const th = ["Margins + share only", "Power only"];
  s.addChart(pres.charts.BAR, [
    { name: "Return", labels: th, values: [0.33, 0.36] },
  ], chartFrame({
    x: 2.55, y: 4.05, w: 4.9, h: 2.25, barDir: "col", barGapWidthPct: 110, chartColors: [NAVY],
    valAxisMinVal: 0, valAxisMaxVal: 0.45, dataLabelFormatCode: "0%", dataLabelPosition: "outEnd", dataLabelFontSize: 15,
    catAxisLabelFontSize: 13, objectName: "Pick one chart",
  }));
  s.addText("Your return if only one comes true", {
    x: 2.55, y: 6.3, w: 4.9, h: 0.28, margin: 0, align: "center", fontSize: 11, italic: true, color: C.accent2, isTextBox: true, objectName: "Pick one caption",
  });
  s.addText("Each bar holds the other side at our bear case", {
    x: 0.35, y: 4.65, w: 2.0, h: 1.05, line: { color: INK, width: 1, dashType: "dash" }, align: "center", valign: "middle",
    fontSize: 12, bold: true, color: C.text2, margin: 4, isTextBox: true, objectName: "Left assumption box",
  });
  s.addText([{ text: "All three:", options: { breakLine: true } }, { text: "+66%", options: { fontSize: 20 } }], {
    x: 7.65, y: 4.65, w: 2.0, h: 1.05, line: { color: INK, width: 1, dashType: "dash" }, align: "center", valign: "middle",
    fontSize: 13, bold: true, color: C.text2, margin: 4, isTextBox: true, objectName: "Right assumption box",
  });

  source(s, "GPS model: SOTP (FY27E EBITDA, base multiples), aviation theses vs. Power switched on separately; share history per GPS analysis");
  s.addNotes("Bars = base-case SOTP with one thesis on and the others off (bear-case margins/share rows, Power units = 0), at base multiples, vs. $167.03: " +
    "margins + share only (no Power) $222 (+33%); Power (signed order) only, with bear-case margins and share, $227 (+36%). All three = $277 (+66%). " +
    "Share path: ~4% (2024) → ~8% (2025) → ~12% (2026E), i.e. ~4 pts a year; the model reaches 20% by FY30, ~2 pts a year. " +
    "With all three off, the SOTP is $172, about today's price: the market is pricing the bear case.");
}

// ---------- Valuation: SOTP waterfall ----------
{
  const s = pres.addSlide({ masterName: "GPS Content Subtitle", sectionTitle: "Valuation" });
  s.addText("Valuation: Sum of the Parts", { placeholder: "title" });
  s.addText("At $167 the market prices our bear case. Each thesis builds from there to $277.", { placeholder: "subtitle" });

  sectionHeader(s, "From Today to Our Base Case ($ / Share)", 0.35, 1.7, 6.25, "Waterfall header");
  const wc = ["Today", "To bear case", "Margins", "Share", "Power", "Base case"];
  s.addChart(pres.charts.BAR, [
    { name: "Base", labels: wc, values: [0, 167.0, 171.9, 188.9, 221.6, 0] },
    { name: "Today", labels: wc, values: [167.0, 0, 0, 0, 0, 0] },
    { name: "Theses", labels: wc, values: [0, 4.8, 17.0, 32.7, 55.1, 0] },
    { name: "Base case", labels: wc, values: [0, 0, 0, 0, 0, 276.6] },
  ], chartFrame({
    x: 0.35, y: 2.3, w: 6.25, h: 3.25, barDir: "col", barGrouping: "stacked", barGapWidthPct: 30,
    chartColors: ["FFFFFF", PLAT, NAVY, NAVY], valAxisMinVal: 0, valAxisMaxVal: 300, catAxisLabelFontSize: 11,
    showValue: false, objectName: "Thesis waterfall",
  }));
  // Value labels above each bar (plot: $0 at y≈5.0", ~0.00878"/$; bar centers ~1" apart from x≈0.97")
  [["$167", 0.97, 167.0], ["+$5", 1.97, 171.9], ["+$17", 2.97, 188.9], ["+$33", 3.97, 221.6], ["+$55", 4.97, 276.7], ["$277", 5.97, 276.6]].forEach(([t, cx, top], i) => {
    s.addText(t, {
      x: cx - 0.45, y: 5.0 - top * 0.00878 - 0.3, w: 0.9, h: 0.26, margin: 0, align: "center", valign: "bottom", fontSize: 13, bold: true,
      color: i === 0 ? INK : C.text2, isTextBox: true, objectName: `Waterfall label ${i + 1}`,
    });
  });
  s.addText("FY27E SOTP; each thesis switched from our bear case to base (Shapley average)", {
    x: 0.35, y: 5.55, w: 6.25, h: 0.28, margin: 0, align: "center", fontSize: 10, italic: true, color: C.accent2, isTextBox: true, objectName: "Waterfall caption",
  });

  sectionHeader(s, "What It Means", 6.9, 1.7, 2.75, "Means header");
  [["+66%", "upside to our $277 base case"], ["$50", "from the aviation theses: margins and share"], ["$55", "from Power, on just the signed order"]].forEach(([big, lab], i) => {
    s.addText([{ text: big, options: { fontSize: 28, bold: true, color: C.text2, breakLine: true } }, { text: lab, options: { fontSize: 12, color: INK } }], {
      x: 6.9, y: 2.3 + i * 1.1, w: 2.75, h: 1.0, align: "center", valign: "middle", margin: 0, isTextBox: true, objectName: `Means stat ${i + 1}`,
    });
  });

  takeaway(s, "Get the aviation theses right and you make 33%. Power on just the signed order takes it to 66%.");
  source(s, "GPS model (SOTP: Aerospace 16x, Power 12x, Leasing + SCI 9x FY27E EBITDA); thesis attribution re-runs; price $167.03 (10/2/26)");
  s.addNotes("Waterfall: today $167.03; bear case (bear margins and share, no Power) SOTP $171.86 (+$4.83); Shapley contributions on the SOTP: margins +$17.04, share +$32.66, Power +$55.08 = $276.65 (+66%). " +
    "Base-case SOTP build: Aerospace $1,541M × 16x = $237; Power $450M × 12x = $52; Leasing + SCI $455M × 9x = $39; corporate −$28; net debt and preferred −$24.");
}

// ---------- Catalysts (TATT timeline, centered arrow) ----------
pres.addSection({ title: "Catalysts" });
{
  const s = pres.addSlide({ masterName: "GPS Content Subtitle", sectionTitle: "Catalysts" });
  s.addText("Catalysts", { placeholder: "title" });
  s.addText("Three catalysts over the next 12–15 months, one for each thesis.", { placeholder: "subtitle" });

  // Center arrow running down the slide
  s.addShape(pres.shapes.DOWN_ARROW, { x: 4.72, y: 1.7, w: 0.56, h: 4.2, fill: { color: NAVY }, line: { type: "none" }, objectName: "Timeline arrow" });

  const rows = [
    ["Q3 & Q4 '26 prints", "Two quarters of stable margins",
      "Aerospace margins hold at ~30% or better, plus early PMA usage commentary on the Q3 call (late Oct.)"],
    ["1H '27", "New facilities ramp up",
      "Jakarta, Cairo and Lisbon come online, putting FTAI on track for its 1,700-module target"],
    ["2H '27", "Power units deliver, or a new contract",
      "Mod-1 deliveries on schedule, or a follow-on order that pushes FY27 Power EBITDA toward $750M"],
  ];
  rows.forEach(([when, head, watch], i) => {
    const y = 1.85 + i * 1.33;
    s.addShape(pres.shapes.RECTANGLE, { x: 0.35, y, w: 9.3, h: 1.08, fill: { color: PLAT_XLT }, line: { type: "none" }, objectName: `Catalyst ${i + 1} band` });
    s.addText(head, {
      fontSize: 15, bold: true, color: C.text2, x: 0.5, y, w: 3.5, h: 1.08, margin: 0, align: "left", valign: "middle", isTextBox: true, objectName: `Catalyst ${i + 1} head`,
    });
    s.addText(when, {
      x: 4.15, y: y + 0.19, w: 1.7, h: 0.7, fill: { color: "FFFFFF" }, line: { color: NAVY, width: 2 }, align: "center", valign: "middle",
      fontSize: 15, bold: true, color: C.text2, margin: 0, isTextBox: true, objectName: `Catalyst ${i + 1} date`,
    });
    s.addText(watch, {
      x: 6.0, y, w: 3.5, h: 1.08, margin: 0, align: "left", valign: "middle", fontSize: 12, color: INK, isTextBox: true, objectName: `Catalyst ${i + 1} watch`,
    });
  });

  takeaway(s, "Each catalyst tests one thesis directly, and all three land by the end of 2027.");
  source(s, "FTAI earnings calls and Q2'26 supplement (1,700-module 2027 target; FY27 Power guide $450–750M); GPS analysis");
  s.addNotes("1) Q3'26 (late Oct. 2026) and Q4'26 (~Feb. 2027) prints: Aerospace Adj. EBITDA margin holding at ~30% confirms the floor; watch PMA usage and parts 4/5 approval commentary. " +
    "2) Capacity (1H'27) and 3) Power (2H'27), reordered. Power: management moved first Mod-1 deliveries from Q4'26 to 'prudent to expect deliveries in 2027'; delivery cadence or a follow-on order (Jereh must disclose large contracts) moves Power toward the top of the $450–750M FY27 guide. " +
    "3) Capacity: partner sites in Jakarta (GMF) and Cairo (EgyptAir) plus Lisbon ramp in 2027; network capacity 3,000 modules vs. a 1,700-module 2027 target.");
}

(async () => {
  await pres.writeFile({ fileName: OUT });
  await applyTheme(OUT, THEME);
  console.log("Wrote", OUT);
})();
