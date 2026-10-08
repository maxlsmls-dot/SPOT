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

pres.defineSlideMaster({
  title: "GPS Content",
  background: { color: "FFFFFF" },
  margin: [0.4, 0.4, 0.6, 0.4],
  objects: [
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
  ],
  slideNumber: { x: 8.35, y: 6.92, w: 0.45, h: 0.3, fontSize: 11, bold: true, color: "1A1A1A", align: "right" },
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

(async () => {
  await pres.writeFile({ fileName: OUT });
  await applyTheme(OUT, THEME);
  console.log("Wrote", OUT);
})();
