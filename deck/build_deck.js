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
  s.addText("The heavy second-visit wave peaks in 2027. Late-life, lighter work follows and lifts margins.", { placeholder: "subtitle" });

  sectionHeader(s, "CFM56 Shop Visits by Visit Number", 0.35, 1.7, 4.75, "Cohort header");
  const cy = ["2025", "2026", "2027", "2028", "2029", "2030"];
  s.addChart(pres.charts.BAR, [
    { name: "First visits", labels: cy, values: [976, 912, 845, 763, 676, 598] },
    { name: "Second visits (heaviest)", labels: cy, values: [842, 891, 914, 908, 874, 832] },
    { name: "Third+ visits (late life)", labels: cy, values: [532, 597, 641, 679, 700, 720] },
  ], chartFrame({
    x: 0.35, y: 2.3, w: 4.75, h: 3.15, barDir: "col", barGrouping: "stacked", barGapWidthPct: 40,
    chartColors: [PLAT_LT, NAVY, PLAT], valAxisMinVal: 0, valAxisMaxVal: 2700, showValue: false,
    showLegend: true, legendPos: "b", legendFontSize: 10, legendFontFace: "+mn-lt", legendColor: INK,
    objectName: "Cohort chart",
  }));
  s.addText("2nd-visit peak", {
    x: 1.87, y: 2.2, w: 1.3, h: 0.28, margin: 0, align: "center", fontSize: 11, bold: true, italic: true, color: C.text2,
    isTextBox: true, objectName: "Peak label",
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
    "second visits, typically the heaviest, peak at 914 in 2027; third-and-later visits rise 532 → 720. Late-life engines increasingly get green-time-only " +
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

(async () => {
  await pres.writeFile({ fileName: OUT });
  await applyTheme(OUT, THEME);
  console.log("Wrote", OUT);
})();
