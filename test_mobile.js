const puppeteer = require('puppeteer-core');
const path = require('path');
const fs = require('fs');

const CHROME_PATH = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const OUT_DIR = '/Users/thanhduy/.gemini/antigravity/brain/1f8b9f5c-6d23-4a96-aeca-464b2f6f43a0';

async function main() {
  const browser = await puppeteer.launch({
    executablePath: CHROME_PATH,
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-gpu']
  });

  const page = await browser.newPage();
  
  // Mobile Viewport: 393 x 852, device scale factor 2 (like iPhone 15 Pro)
  await page.setViewport({
    width: 393,
    height: 852,
    deviceScaleFactor: 2,
    isMobile: true,
    hasTouch: true
  });

  const fileUrl = 'file://' + path.resolve(__dirname, 'index.html');
  console.log('Navigating to:', fileUrl);
  await page.goto(fileUrl, { waitUntil: 'load' });

  // Wait and ensure preloader is hidden
  await page.evaluate(() => {
    const p = document.getElementById('preloader');
    if (p) {
      p.style.display = 'none';
      p.classList.add('hidden');
    }
  });
  await new Promise(r => setTimeout(r, 1000));

  // Screenshot 1: Hero
  await page.screenshot({ path: path.join(OUT_DIR, 'shot_01_hero.png') });
  console.log('Saved shot_01_hero.png');

  // Scroll to About section
  await page.evaluate(() => {
    document.querySelector('#about')?.scrollIntoView();
  });
  await new Promise(r => setTimeout(r, 600));
  await page.screenshot({ path: path.join(OUT_DIR, 'shot_02_about.png') });
  console.log('Saved shot_02_about.png');

  // Scroll to Menu section
  await page.evaluate(() => {
    document.querySelector('#menu')?.scrollIntoView();
  });
  await new Promise(r => setTimeout(r, 600));
  await page.screenshot({ path: path.join(OUT_DIR, 'shot_03_menu.png') });
  console.log('Saved shot_03_menu.png');

  // Scroll to Atmosphere section
  await page.evaluate(() => {
    document.querySelector('#atmosphere')?.scrollIntoView();
  });
  await new Promise(r => setTimeout(r, 600));
  await page.screenshot({ path: path.join(OUT_DIR, 'shot_04_atmosphere.png') });
  console.log('Saved shot_04_atmosphere.png');

  // Scroll to Reviews section
  await page.evaluate(() => {
    document.querySelector('#reviews')?.scrollIntoView();
  });
  await new Promise(r => setTimeout(r, 600));
  await page.screenshot({ path: path.join(OUT_DIR, 'shot_05_reviews.png') });
  console.log('Saved shot_05_reviews.png');

  // Scroll to Contact & Footer section
  await page.evaluate(() => {
    document.querySelector('#contact')?.scrollIntoView();
  });
  await new Promise(r => setTimeout(r, 600));
  await page.screenshot({ path: path.join(OUT_DIR, 'shot_06_contact.png') });
  console.log('Saved shot_06_contact.png');

  // Test Mobile Drawer
  await page.evaluate(() => {
    window.scrollTo(0, 0);
    const toggle = document.querySelector('.mobile-toggle');
    if (toggle) toggle.click();
  });
  await new Promise(r => setTimeout(r, 500));
  await page.screenshot({ path: path.join(OUT_DIR, 'shot_07_drawer.png') });
  console.log('Saved shot_07_drawer.png');

  // Full page screenshot
  await page.evaluate(() => {
    const drawer = document.querySelector('.mobile-drawer');
    if (drawer && drawer.classList.contains('active')) {
      document.querySelector('.mobile-toggle')?.click();
    }
  });
  await new Promise(r => setTimeout(r, 500));
  await page.screenshot({ path: path.join(OUT_DIR, 'shot_00_fullpage.png'), fullPage: true });
  console.log('Saved shot_00_fullpage.png');

  await browser.close();
  console.log('Done capturing screenshots!');
}

main().catch(err => {
  console.error('Error in main:', err);
  process.exit(1);
});
