const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox'] });
  const page = await browser.newPage();
  
  await page.goto('https://www.olioncoffee.app/?v=' + Date.now(), { waitUntil: 'networkidle2' });
  await new Promise(r => setTimeout(r, 2000));
  
  const matchas = await page.evaluate(() => {
    return Array.from(document.querySelectorAll('.menu-card-name'))
      .map(el => el.textContent.trim())
      .filter(name => name.includes('MATCHA'));
  });
  
  console.log(matchas);
  await browser.close();
})();
