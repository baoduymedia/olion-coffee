const puppeteer = require('puppeteer-core');
const path = require('path');
const fs = require('fs');

const CHROME_PATH = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const OUT_DIR = '/Users/thanhduy/.gemini/antigravity/brain/1f8b9f5c-6d23-4a96-aeca-464b2f6f43a0';

async function captureViewport(browser, name, width, height, isMobile = false) {
  const page = await browser.newPage();
  await page.setViewport({
    width,
    height,
    deviceScaleFactor: 2,
    isMobile,
    hasTouch: isMobile
  });

  const fileUrl = 'file://' + path.resolve(__dirname, 'index.html');
  await page.goto(fileUrl, { waitUntil: 'load' });

  // Hide preloader immediately
  await page.evaluate(() => {
    const p = document.getElementById('preloader');
    if (p) {
      p.style.display = 'none';
      p.classList.add('hidden');
    }
  });
  await new Promise(r => setTimeout(r, 600));

  // Top viewport screenshot
  await page.screenshot({ path: path.join(OUT_DIR, `shot_${name}_top.png`) });

  // Scroll down a bit to see menu
  await page.evaluate(() => {
    document.querySelector('#menu')?.scrollIntoView();
  });
  await new Promise(r => setTimeout(r, 500));
  await page.screenshot({ path: path.join(OUT_DIR, `shot_${name}_menu.png`) });

  // Full page screenshot
  await page.screenshot({ path: path.join(OUT_DIR, `shot_${name}_full.png`), fullPage: true });

  console.log(`Captured ${name} (${width}x${height})`);
  await page.close();
}

async function main() {
  const browser = await puppeteer.launch({
    executablePath: CHROME_PATH,
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-gpu']
  });

  // 1. Mobile (375x812)
  await captureViewport(browser, 'mobile_375', 375, 812, true);

  // 2. Tablet (768x1024)
  await captureViewport(browser, 'tablet_768', 768, 1024, false);

  // 3. Desktop (1440x900)
  await captureViewport(browser, 'desktop_1440', 1440, 900, false);

  await browser.close();
  console.log('All responsive captures complete!');
}

main().catch(err => {
  console.error('Error in test:', err);
  process.exit(1);
});
