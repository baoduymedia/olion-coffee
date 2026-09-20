const puppeteer = require('puppeteer-core');
const path = require('path');
const CHROME_PATH = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';

async function testPage() {
  const browser = await puppeteer.launch({
    executablePath: CHROME_PATH,
    headless: true,
    userDataDir: path.resolve(__dirname, '.tmp_chrome_test2'),
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-gpu']
  });

  const page = await browser.newPage();
  
  page.on('console', msg => console.log('BROWSER LOG:', msg.type(), msg.text()));
  page.on('pageerror', err => console.error('BROWSER ERROR:', err.message));

  // 1. Desktop View (1440x900)
  await page.setViewport({ width: 1440, height: 900 });
  await page.goto('file://' + path.resolve(__dirname, 'index.html'), { waitUntil: 'networkidle0' });

  const newsElem = await page.$('#news');
  if (newsElem) {
    await newsElem.scrollIntoView();
    await new Promise(r => setTimeout(r, 600));
    await page.screenshot({ path: path.resolve(__dirname, 'shot_news_desktop.png') });
    console.log('✅ Captured desktop news section screenshot!');
  }

  // Click on featured card to test modal
  await page.click('.news-featured-card');
  await new Promise(r => setTimeout(r, 600));
  await page.screenshot({ path: path.resolve(__dirname, 'shot_news_modal.png') });
  console.log('✅ Captured news modal screenshot!');

  // Close modal
  await page.click('.news-modal-box .modal-close');
  await new Promise(r => setTimeout(r, 400));

  // 2. Mobile View (390x844 - iPhone 14)
  await page.setViewport({ width: 390, height: 844, isMobile: true, hasTouch: true });
  await page.goto('file://' + path.resolve(__dirname, 'index.html'), { waitUntil: 'networkidle0' });
  const mobileNews = await page.$('#news');
  if (mobileNews) {
    await mobileNews.scrollIntoView();
    await new Promise(r => setTimeout(r, 600));
    await page.screenshot({ path: path.resolve(__dirname, 'shot_news_mobile.png') });
    console.log('✅ Captured mobile news section screenshot!');
  }

  await browser.close();
}
testPage().catch(console.error);
