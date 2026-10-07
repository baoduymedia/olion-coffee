const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox'] });
  const page = await browser.newPage();
  await page.goto('https://olion-coffee.vercel.app/?v=' + Date.now(), { waitUntil: 'networkidle2' });
  const html = await page.content();
  console.log(html.includes('FETCH FUNC TYPE:') ? 'YES IT HAS THE LOG' : 'NO IT DOES NOT');
  await browser.close();
})();
