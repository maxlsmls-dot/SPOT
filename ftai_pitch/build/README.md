# FTAI long pitch deck build

`node build.js ../FTAI_Long_Pitch.pptx` (needs `pptxgenjs`, `react`, `react-dom`, `react-icons`, `sharp`).

Note: pptxgenjs writes one `<a:pPr>` per text run, which breaks bullets on mixed-format paragraphs.
Patch `node_modules/pptxgenjs/dist/pptxgen.cjs.js` so the paragraph-properties line in the line loop only runs when `idx === 0`.

Model figures live in `data.js` and inline in the slide modules; all come from `FTAI_Model_vFinal.xlsx` (base case, with Bull/Bear from the DCF!C3 case toggle).
