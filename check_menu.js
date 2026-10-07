const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox'] });
  const page = await browser.newPage();
  
  await page.goto('https://www.olioncoffee.app/?v=' + Date.now(), { waitUntil: 'networkidle2' });
  
  await new Promise(r => setTimeout(r, 3000)); // wait for supabase fetch
  
  const menuItems = await page.evaluate(() => {
    const items = [];
    document.querySelectorAll('.menu-card').forEach(el => {
      const name = el.querySelector('.menu-card-name')?.textContent.trim() || 'N/A';
      const price = el.querySelector('.menu-card-price')?.textContent.trim() || 'N/A';
      if(name !== 'N/A') items.push(`${name}: ${price}`);
    });
    return items;
  });
  
  console.log(`Found ${menuItems.length} items`);
  menuItems.slice(0, 5).forEach(item => console.log(item)); // print first 5
  // check toppings specifically
  const toppings = menuItems.filter(i => i.includes('TRÂN CHÂU') || i.includes('THẠCH'));
  console.log("Toppings:");
  toppings.forEach(t => console.log(t));
  
  await browser.close();
})();
