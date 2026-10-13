# FTAI long pitch deck build

`node build_final.js ../FTAI_Long_Pitch.pptx` (needs `pptxgenjs`). 13 slides: cover + 12 content slides in the GPS (CarGurus) house style.

Note: pptxgenjs writes one `<a:pPr>` per text run, which breaks bullets on mixed-format paragraphs.
Patch `node_modules/pptxgenjs/dist/pptxgen.cjs.js` so the paragraph-properties line in the line loop only runs when `idx === 0`.

Figures come from `FTAI_Model_vFinal.xlsx` (Bear/Base/Bull via DCF!C3; valuation bridge via switching each thesis's Assumptions bear rows to base) and the CFM56 Outsourcing Flip Tracker.
