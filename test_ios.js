const puppeteer = require('puppeteer');
(async () => {
  const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox'] });
  const page = await browser.newPage();
  
  page.on('console', msg => console.log('PAGE LOG:', msg.text()));
  page.on('pageerror', err => console.log('PAGE ERROR:', err.message));
  
  await page.goto('https://olion-coffee.vercel.app/?v=' + Date.now(), { waitUntil: 'networkidle2' });
  
  // Wait for preloader to hide
  await new Promise(r => setTimeout(r, 2000));
  
  console.log("Testing iOS button...");
  await page.evaluate(() => {
    window.showInstallGuide('ios');
  });
  
  await new Promise(r => setTimeout(r, 1000));
  
  const text = await page.evaluate(() => {
    return document.getElementById('guideContent').innerText;
  });
  console.log("Guide text:", text.substring(0, 50));
  
  await browser.close();
})();
