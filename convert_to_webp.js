const puppeteer = require('puppeteer-core');
const fs = require('fs');
const path = require('path');

const CHROME_PATH = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';

async function convertToWebp() {
  const browser = await puppeteer.launch({
    executablePath: CHROME_PATH,
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  const page = await browser.newPage();

  async function processDir(dir) {
    const files = fs.readdirSync(dir);
    for (const file of files) {
      const fullPath = path.join(dir, file);
      const stat = fs.statSync(fullPath);
      if (stat.isDirectory()) {
        await processDir(fullPath);
      } else if (file.endsWith('.jpg') || file.endsWith('.png')) {
        const webpPath = fullPath.replace(/\.(png|jpg)$/, '.webp');
        if (!fs.existsSync(webpPath)) {
          const fileData = fs.readFileSync(fullPath).toString('base64');
          const ext = file.endsWith('.png') ? 'png' : 'jpeg';
          const mime = `image/${ext}`;
          
          const webpBase64 = await page.evaluate(async (dataUrl) => {
            return new Promise((resolve) => {
              const img = new Image();
              img.onload = () => {
                const canvas = document.createElement('canvas');
                canvas.width = img.naturalWidth;
                canvas.height = img.naturalHeight;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(img, 0, 0);
                const outUrl = canvas.toDataURL('image/webp', 0.85);
                resolve(outUrl.split(',')[1]);
              };
              img.src = dataUrl;
            });
          }, `data:${mime};base64,${fileData}`);

          fs.writeFileSync(webpPath, Buffer.from(webpBase64, 'base64'));
          console.log(`Converted: ${file} -> ${path.basename(webpPath)}`);
        }
      }
    }
  }

  await processDir(path.resolve(__dirname, 'assets'));
  await browser.close();
  console.log('Finished WebP conversion for all assets!');
}

convertToWebp().catch(console.error);
