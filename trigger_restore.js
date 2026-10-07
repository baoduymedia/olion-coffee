const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox'] });
  const page = await browser.newPage();
  
  page.on('console', msg => console.log('LOG:', msg.text()));
  
  await page.goto('https://olion-coffee.vercel.app/admin.html?v=' + Date.now(), { waitUntil: 'networkidle2' });
  
  // Login
  await page.type('#adminUsername', 'admin');
  await page.type('#adminPassword', 'admin');
  await page.click('button[type="submit"]');
  
  await new Promise(r => setTimeout(r, 2000));
  
  console.log("Triggering restoreDefaultMenu()...");
  
  await page.evaluate(async () => {
    // Override confirm
    window.originalConfirm = window.confirm;
    window.confirm = () => true;
    
    if (typeof restoreDefaultMenu === 'function') {
      await restoreDefaultMenu();
    } else {
      console.error('restoreDefaultMenu is not defined globally!');
    }
    
    window.confirm = window.originalConfirm;
  });
  
  await new Promise(r => setTimeout(r, 4000));
  console.log("Done.");
  
  await browser.close();
})();
