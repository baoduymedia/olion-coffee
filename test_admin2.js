const puppeteer = require('puppeteer');
const wait = ms => new Promise(r => setTimeout(r, ms));

(async () => {
  const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox'] });
  
  const page2 = await browser.newPage();
  await page2.goto('https://olion-coffee.vercel.app/', { waitUntil: 'networkidle2' });
  
  await wait(2000);
  const data = await page2.evaluate(async () => {
    return await fetchSiteSettingsFromCloud();
  });
  console.log('Site settings from Supabase:', JSON.stringify(data));
  
  const styles = await page2.evaluate(() => {
    return {
      wheel: window.getComputedStyle(document.getElementById('wheelFloatBtn')).display,
      banner: window.getComputedStyle(document.getElementById('announcementBanner')).display
    };
  });
  console.log('Computed styles:', styles);
  
  await browser.close();
})();
