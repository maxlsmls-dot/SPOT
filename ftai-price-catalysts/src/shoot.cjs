// Screenshot every build/*.html to images/*.png (full page, 2x).
// Run: NODE_PATH=$(npm root -g) node src/shoot.cjs
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const root = path.resolve(__dirname, '..');
const build = path.join(root, 'build'), out = path.join(root, 'images');
(async () => {
  fs.mkdirSync(out, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1600, height: 900 }, deviceScaleFactor: 2 });
  for (const f of fs.readdirSync(build).filter(f => f.endsWith('.html')).sort()) {
    await page.goto('file://' + path.join(build, f));
    await page.screenshot({ path: path.join(out, f.replace('.html', '.png')), fullPage: true });
    console.log(f);
  }
  await browser.close();
})();
