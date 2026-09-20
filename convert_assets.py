import os
import sys
import time

"""
Script Python tự động quét và chuyển đổi toàn bộ ảnh JPG, JPEG, PNG sang WebP (Quality 80%)
Yêu cầu thư viện: Pillow
Cài đặt: pip install Pillow
"""

try:
    from PIL import Image
except ImportError:
    print("\n❌ Chưa cài đặt thư viện Pillow. Hãy chạy lệnh: pip install Pillow\n")
    sys.exit(1)

# Thư mục mục tiêu: ./assets/
TARGET_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
QUALITY = 80  # Chất lượng nén WebP (0-100)

def convert_images(target_folder):
    if not os.path.exists(target_folder):
        print(f"❌ Thư mục không tồn tại: {target_folder}")
        return

    valid_extensions = ('.jpg', '.jpeg', '.png')
    count = 0
    total_orig_size = 0
    total_new_size = 0

    print("🚀 Bắt đầu quét và tối ưu hóa ảnh sang định dạng WebP...\n")
    print(f"📁 Thư mục: {target_folder}")
    print(f"🎯 Chất lượng nén: {QUALITY}%\n")
    start_time = time.time()

    # Quét đệ quy toàn bộ thư mục và thư mục con (ví dụ: assets/menu/)
    for root, _, files in os.walk(target_folder):
        for file in files:
            file_lower = file.lower()
            if file_lower.endswith(valid_extensions):
                input_path = os.path.join(root, file)
                # Đổi đuôi thành .webp
                base_name = os.path.splitext(file)[0]
                output_path = os.path.join(root, f"{base_name}.webp")

                try:
                    orig_size = os.path.getsize(input_path)
                    
                    with Image.open(input_path) as img:
                        # Bảo toàn kênh alpha (trong suốt) cho file PNG
                        if img.mode in ("RGBA", "LA") or (img.mode == "P" and "transparency" in img.info):
                            img = img.convert("RGBA")
                        else:
                            img = img.convert("RGB")
                        
                        # Lưu dưới định dạng WebP với nén tối ưu
                        img.save(output_path, "WEBP", quality=QUALITY, method=6)

                    new_size = os.path.getsize(output_path)
                    saved_pct = ((orig_size - new_size) / orig_size) * 100

                    total_orig_size += orig_size
                    total_new_size += new_size
                    count += 1

                    rel_input = os.path.relpath(input_path, target_folder)
                    print(f"✅ [Chuyển đổi] {rel_input} -> {base_name}.webp")
                    print(f"   Dung lượng: {orig_size / 1024:.1f} KB ➔ {new_size / 1024:.1f} KB (Tiết kiệm: {saved_pct:.1f}%)\n")
                except Exception as e:
                    print(f"❌ Lỗi khi xử lý {file}: {e}")

    elapsed = time.time() - start_time
    total_saved_pct = ((total_orig_size - total_new_size) / total_orig_size * 100) if total_orig_size > 0 else 0
    print(f"🎉 Đã chuyển đổi thành công {count} ảnh trong {elapsed:.2f} giây!")
    print(f"📊 Tổng dung lượng gốc: {total_orig_size / (1024*1024):.2f} MB")
    print(f"📊 Tổng dung lượng WebP: {total_new_size / (1024*1024):.2f} MB")
    print(f"💰 Tiết kiệm tổng cộng: {total_saved_pct:.1f}% dung lượng!")

if __name__ == "__main__":
    convert_images(TARGET_DIR)
