const puppeteer = require('puppeteer');
(async () => {
  const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox'] });
  const page = await browser.newPage();
  
  await page.evaluateOnNewDocument(() => {
    window.onerror = function(message, source, lineno, colno, error) {
      console.log('MY_ERROR_TRACE', message, source, lineno, colno);
    };
  });
  
  page.on('console', msg => console.log('PAGE LOG:', msg.text()));
  page.on('pageerror', err => console.log('PAGE ERROR:', err.message));
  
  await page.goto('file:///Users/thanhduy/Documents/olion-coffee/index.html', { waitUntil: 'networkidle2' });
  await new Promise(r => setTimeout(r, 1000));
  await browser.close();
})();
