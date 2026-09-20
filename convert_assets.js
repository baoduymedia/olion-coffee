const fs = require('fs');
const path = require('path');

/**
 * Script tự động quét và chuyển đổi toàn bộ ảnh JPG, JPEG, PNG sang WebP (Quality 80%)
 * Thư mục quét mặc định: ./assets/
 */

const TARGET_DIR = path.resolve(__dirname, 'assets');
const QUALITY = 80; // Chất lượng nén tối ưu (0-100)

// Kiểm tra và load thư viện sharp
let sharp;
try {
  sharp = require('sharp');
} catch (err) {
  console.error('\n❌ Chưa cài đặt thư viện sharp. Hãy chạy lệnh: npm install sharp\n');
  process.exit(1);
}

// Hàm quét đệ quy thư mục
async function scanAndConvert(dir) {
  if (!fs.existsSync(dir)) {
    console.error(`❌ Thư mục không tồn tại: ${dir}`);
    return;
  }

  const entries = fs.readdirSync(dir, { withFileTypes: true });

  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);

    if (entry.isDirectory()) {
      // Đệ quy vào thư mục con (ví dụ: ./assets/menu/)
      await scanAndConvert(fullPath);
    } else if (entry.isFile()) {
      const ext = path.extname(entry.name).toLowerCase();

      if (['.jpg', '.jpeg', '.png'].includes(ext)) {
        const outPath = fullPath.replace(/\.(jpg|jpeg|png)$/i, '.webp');

        try {
          const originalSize = fs.statSync(fullPath).size;

          // Chuyển đổi sang WebP với Sharp
          await sharp(fullPath)
            .webp({
              quality: QUALITY,
              effort: 6, // Mức độ nén tối đa (0-6)
              lossless: false
            })
            .toFile(outPath);

          const newSize = fs.statSync(outPath).size;
          const savedPct = (((originalSize - newSize) / originalSize) * 100).toFixed(1);

          console.log(`✅ [Chuyển đổi thành công] ${path.relative(TARGET_DIR, fullPath)} -> ${path.basename(outPath)}`);
          console.log(`   Dung lượng: ${(originalSize / 1024).toFixed(1)} KB ➔ ${(newSize / 1024).toFixed(1)} KB (Tiết kiệm: ${savedPct}%)\n`);
        } catch (error) {
          console.error(`❌ Lỗi khi xử lý file ${entry.name}:`, error.message);
        }
      }
    }
  }
}

async function main() {
  console.log('🚀 Bắt đầu quét và tối ưu hóa ảnh sang định dạng WebP...\n');
  console.log(`📁 Thư mục mục tiêu: ${TARGET_DIR}`);
  console.log(`🎯 Chất lượng nén: ${QUALITY}%\n`);

  const startTime = Date.now();
  await scanAndConvert(TARGET_DIR);
  const elapsed = ((Date.now() - startTime) / 1000).toFixed(2);

  console.log(`\n🎉 Hoàn thành xuất sắc toàn bộ ảnh trong ${elapsed} giây!`);
}

main();
