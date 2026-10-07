const puppeteer = require('puppeteer');
(async () => {
  const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox'] });
  const page = await browser.newPage();
  
  const mapUrl = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1959.3512!2d106.6977984!3d10.8267018!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3175294b803d0b41%3A0x58d79ca538a1312c!2sOLION%20COFFEE!5e0!3m2!1svi!2sVN!4v1700000000000!5m2!1svi!2sVN";
  console.log("Loading URL...");
  
  // Try to load it
  const response = await page.goto(mapUrl, { waitUntil: 'networkidle2' });
  console.log("Status:", response.status());
  
  await page.screenshot({ path: '/Users/thanhduy/.gemini/antigravity/brain/1f8b9f5c-6d23-4a96-aeca-464b2f6f43a0/map_screenshot2.png' });
  console.log("Screenshot taken.");
  
  await browser.close();
})();
