const puppeteer = require('puppeteer');
const wait = ms => new Promise(r => setTimeout(r, ms));

(async () => {
  const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox'] });
  const page = await browser.newPage();
  
  console.log('Opening admin page...');
  await page.goto('https://olion-coffee.vercel.app/admin.html', { waitUntil: 'networkidle2' });
  
  console.log('Logging in...');
  await page.type('#adminUsername', 'admin');
  await page.type('#adminPassword', 'admin');
  await page.click('#loginForm button[type="submit"]');
  
  await wait(2000);
  
  console.log('Switching to Minigame tab...');
  await page.evaluate(() => {
    switchTab('minigame');
  });
  
  await wait(1000);
  
  console.log('Toggling switch...');
  await page.evaluate(() => {
    const toggle = document.getElementById('minigameEnableToggle');
    if (toggle.checked) toggle.click(); // ensure it's OFF
    const btn = document.getElementById('saveMinigameSettingsBtn');
    if (btn) btn.click();
  });
  
  await wait(3000);
  
  console.log('Opening homepage...');
  const page2 = await browser.newPage();
  await page2.goto('https://olion-coffee.vercel.app/', { waitUntil: 'networkidle2' });
  
  console.log('Checking visibility of Minigame...');
  const wheelVisible = await page2.evaluate(() => {
    const el = document.getElementById('wheelFloatBtn');
    if (!el) return false;
    const style = window.getComputedStyle(el);
    return style.display !== 'none' && style.visibility !== 'hidden';
  });
  console.log('=> Wheel visible on homepage:', wheelVisible);
  
  console.log('Checking visibility of Announcement...');
  const bannerVisible = await page2.evaluate(() => {
    const el = document.getElementById('announcementBanner');
    if (!el) return false;
    const style = window.getComputedStyle(el);
    return style.display !== 'none' && style.visibility !== 'hidden';
  });
  console.log('=> Announcement banner visible:', bannerVisible);
  
  await browser.close();
})();
