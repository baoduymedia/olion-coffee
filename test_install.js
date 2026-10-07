const puppeteer = require('puppeteer');
(async () => {
  const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox'] });
  const page = await browser.newPage();
  
  page.on('console', msg => console.log('PAGE LOG:', msg.text()));
  page.on('pageerror', err => console.log('PAGE ERROR:', err.message));
  
  await page.goto('https://olion-coffee.vercel.app/?v=' + Date.now(), { waitUntil: 'networkidle2' });
  
  // Wait for preloader to hide
  await new Promise(r => setTimeout(r, 2000));
  
  console.log("Evaluating handleInstall...");
  try {
    await page.evaluate(() => {
      // Find the mobile dock install button if any, or trigger handleInstall directly
      const modal = document.getElementById('downloadAppModal');
      console.log('Modal exists:', !!modal);
      if (typeof handleInstall !== 'undefined') {
         handleInstall();
      } else {
         console.log('handleInstall is not globally defined, simulating click on floating install btn');
         const floatBtn = document.getElementById('floatingInstallBtn');
         if (floatBtn) floatBtn.click();
         else console.log('floatingInstallBtn not found');
      }
      
      const drawerBtn = document.getElementById('drawerInstallBtn');
      if (drawerBtn) drawerBtn.click();
    });
  } catch (err) {
    console.log("Evaluate error:", err.message);
  }
  
  await browser.close();
})();
