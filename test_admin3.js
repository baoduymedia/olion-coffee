const puppeteer = require('puppeteer');
const wait = ms => new Promise(r => setTimeout(r, ms));

(async () => {
  const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox'] });
  
  const page2 = await browser.newPage();
  page2.on('console', msg => console.log('PAGE LOG:', msg.text()));
  
  await page2.goto('https://olion-coffee.vercel.app/', { waitUntil: 'networkidle2' });
  
  await wait(2000);
  
  const styles = await page2.evaluate(() => {
    const el = document.getElementById('wheelFloatBtn');
    return {
      cssText: el.style.cssText,
      computed: window.getComputedStyle(el).display,
    };
  });
  console.log('Styles:', styles);
  
  await browser.close();
})();
