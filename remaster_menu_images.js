const puppeteer = require('puppeteer-core');
const fs = require('fs');
const path = require('path');

const CHROME_PATH = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const MENU_DIR = path.resolve(__dirname, 'assets/menu');

async function main() {
  const browser = await puppeteer.launch({
    executablePath: CHROME_PATH,
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  const page = await browser.newPage();
  await page.setViewport({ width: 800, height: 800 });

  const files = fs.readdirSync(MENU_DIR).filter(f => f.endsWith('.png'));
  console.log(`Processing ${files.length} menu drink images for clean studio presentation...`);

  for (const file of files) {
    const filePath = path.join(MENU_DIR, file);
    const dataUrl = `data:image/png;base64,${fs.readFileSync(filePath).toString('base64')}`;

    const remasteredBase64 = await page.evaluate(async (imgSrc) => {
      return new Promise((resolve) => {
        const img = new Image();
        img.onload = () => {
          const canvas = document.createElement('canvas');
          const ctx = canvas.getContext('2d');
          
          const size = 360;
          canvas.width = size;
          canvas.height = size;

          // Seamless studio radial background matching card container
          const bgGrad = ctx.createRadialGradient(size/2, size/2, 10, size/2, size/2, size * 0.7);
          bgGrad.addColorStop(0, '#FAF6EE');
          bgGrad.addColorStop(0.5, '#F4EEDF');
          bgGrad.addColorStop(1, '#EADBCA');
          ctx.fillStyle = bgGrad;
          ctx.fillRect(0, 0, size, size);

          // Subtle ground contact shadow
          ctx.save();
          const shadowGrad = ctx.createRadialGradient(size/2, size * 0.90, 4, size/2, size * 0.90, size * 0.38);
          shadowGrad.addColorStop(0, 'rgba(44, 24, 16, 0.22)');
          shadowGrad.addColorStop(0.5, 'rgba(44, 24, 16, 0.08)');
          shadowGrad.addColorStop(1, 'rgba(44, 24, 16, 0)');
          ctx.fillStyle = shadowGrad;
          ctx.beginPath();
          ctx.ellipse(size/2, size * 0.90, size * 0.38, size * 0.09, 0, 0, Math.PI * 2);
          ctx.fill();
          ctx.restore();

          // Zoom in slightly to focus purely on the drink and eliminate flyer crop frame
          const maxDim = size * 1.16;
          let drawW = maxDim;
          let drawH = (img.height / img.width) * drawW;
          if (drawH > maxDim) {
            drawH = maxDim;
            drawW = (img.width / img.height) * drawH;
          }

          const drawX = (size - drawW) / 2;
          const drawY = (size - drawH) / 2 - 8;

          ctx.save();
          ctx.imageSmoothingEnabled = true;
          ctx.imageSmoothingQuality = 'high';
          ctx.filter = 'contrast(108%) saturate(115%) brightness(101%)';
          ctx.drawImage(img, drawX, drawY, drawW, drawH);
          ctx.restore();

          resolve(canvas.toDataURL('image/png'));
        };
        img.src = imgSrc;
      });
    }, dataUrl);

    const base64Data = remasteredBase64.replace(/^data:image\/png;base64,/, '');
    fs.writeFileSync(filePath, Buffer.from(base64Data, 'base64'));
  }

  await browser.close();
  console.log('All menu drink images enhanced successfully!');
}

main().catch(console.error);
