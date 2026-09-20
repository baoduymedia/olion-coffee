import os
import glob
from PIL import Image, ImageFilter

def create_studio_bg(size=(800, 800)):
    # Create a simple dark warm gradient background for a "studio" look
    # (Or we can just use one of the good Pexels ambiance photos as a blurred background)
    bg = Image.new('RGB', size, (20, 15, 10))
    return bg

def main():
    assets_dir = 'assets/menu'
    # Use one of the space photos as a beautiful blurred background!
    try:
        bg_source = Image.open('assets/space-1.webp').convert('RGB')
        bg_source = bg_source.resize((800, 800), Image.LANCZOS)
        bg_source = bg_source.filter(ImageFilter.GaussianBlur(radius=15))
        # Darken it a bit to make the drink pop
        bg_source = bg_source.point(lambda p: p * 0.6)
    except:
        bg_source = create_studio_bg()

    # List of drinks to revert to original + composite (the ones AI messed up)
    # The user specifically mentioned the Matcha series looked wrong/weird.
    fix_list = [
        'matcha_caramel', 'matcha_bac_ha', 'matcha_kem_muoi', 'matcha_dau',
        'matcha_cold_whisk', 'matcha_dua', 'matcha_oatside', 'matcha_que_hoa'
    ]
    
    for item in fix_list:
        png_path = os.path.join(assets_dir, f"{item}.png")
        webp_path = os.path.join(assets_dir, f"{item}.webp")
        
        if os.path.exists(png_path):
            fg = Image.open(png_path).convert('RGBA')
            
            # The original PNGs are around 400-500px, let's scale them nicely
            # Assuming bg is 800x800
            target_h = 600
            aspect = fg.width / fg.height
            target_w = int(target_h * aspect)
            
            fg = fg.resize((target_w, target_h), Image.LANCZOS)
            
            # Create a composite
            comp = bg_source.copy()
            
            # Add a slight shadow under the cup? (Optional, let's keep it simple)
            
            # Paste the drink in the center-bottom
            offset_x = (800 - target_w) // 2
            offset_y = 800 - target_h - 40 # 40px from bottom
            
            comp.paste(fg, (offset_x, offset_y), fg)
            
            # Save over the bad webp
            comp.save(webp_path, 'WEBP', quality=90)
            print(f"✅ Composited {item} perfectly!")

if __name__ == '__main__':
    main()
