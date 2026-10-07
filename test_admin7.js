const puppeteer = require('puppeteer');
const wait = ms => new Promise(r => setTimeout(r, ms));

(async () => {
  const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox'] });
  const page2 = await browser.newPage();
  await page2.goto('https://olion-coffee.vercel.app/?v=' + Date.now(), { waitUntil: 'networkidle2' });
  
  await wait(2000);
  
  const styles = await page2.evaluate(() => {
    const w = document.getElementById('wheelFloatBtn');
    const a = document.getElementById('announcementBanner');
    return {
      wheel: w ? window.getComputedStyle(w).display : 'null',
      banner: a ? window.getComputedStyle(a).display : 'null'
    };
  });
  console.log('Styles:', styles);
  await browser.close();
})();
