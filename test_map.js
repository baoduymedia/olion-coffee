const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox'] });
  const page = await browser.newPage();
  
  await page.setViewport({ width: 1280, height: 800 });
  
  // Go to the map iframe URL directly
  const mapUrl = "https://maps.google.com/maps?width=100%25&height=600&hl=vi&q=80/64a%20Dương%20Quảng%20Hàm,%20Gò%20Vấp+(Olion%20Coffee)&t=&z=18&ie=UTF8&iwloc=B&output=embed";
  await page.goto(mapUrl, { waitUntil: 'networkidle2' });
  
  // Take screenshot
  await page.screenshot({ path: '/Users/thanhduy/.gemini/antigravity/brain/1f8b9f5c-6d23-4a96-aeca-464b2f6f43a0/map_screenshot.png' });
  console.log("Screenshot taken.");
  
  await browser.close();
})();
