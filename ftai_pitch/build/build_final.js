const G = require("./g");
(async () => {
  const pres = G.makePres();
  const order = ["v3_cover", "v3_op", "v3_bo", "v3_io", "v3_th", "v3_t1", "v3_t2", "v3_t3", "v3_val", "v3_cr"];
  for (const m of order) await require("./" + m)(pres);
  await pres.writeFile({ fileName: process.argv[2] });
  console.log("ok", pres.slides.length);
})().catch((e) => { console.error(e); process.exit(1); });
