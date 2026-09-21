from PIL import Image
import os

toppings = [
    "tran_chau_trang", "tran_chau_o_long", "thach_suong_sao",
    "thach_que_hoa", "thach_vai_hoa_hong", "thach_ca_phe"
]

out_dir = "assets/menu"

for t in toppings:
    png_path = f"{out_dir}/{t}.png"
    webp_path = f"{out_dir}/{t}.webp"
    
    if os.path.exists(png_path):
        print(f"Restoring {t}...")
        img = Image.open(png_path)
        img.save(webp_path, "WEBP", quality=95)
        print(f"Saved {webp_path}")

print("Done restoring toppings.")
