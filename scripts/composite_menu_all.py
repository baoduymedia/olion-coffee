import os
import glob
from PIL import Image, ImageFilter, ImageEnhance

def main():
    assets_dir = 'assets/menu'
    
    # Create the background
    try:
        bg_source = Image.open('assets/space-1.webp').convert('RGB')
        bg_source = bg_source.resize((800, 800), Image.LANCZOS)
        bg_source = bg_source.filter(ImageFilter.GaussianBlur(radius=12))
        # Darken it for contrast
        bg_source = bg_source.point(lambda p: p * 0.5)
    except:
        bg_source = Image.new('RGB', (800, 800), (20, 15, 10))

    skip_list = ['bac_xiu', 'ca_phe_muoi', 'matcha_latte']
    
    success = 0
    pngs = glob.glob(os.path.join(assets_dir, '*.png'))
    for png_path in pngs:
        basename = os.path.basename(png_path)
        item = basename.replace('.png', '')
        
        if item in skip_list:
            continue
            
        webp_path = os.path.join(assets_dir, f"{item}.webp")
        
        try:
            fg = Image.open(png_path).convert('RGBA')
            
            target_h = 650
            aspect = fg.width / fg.height
            target_w = int(target_h * aspect)
            fg = fg.resize((target_w, target_h), Image.LANCZOS)
            
            # Slightly enhance contrast of foreground
            enhancer = ImageEnhance.Contrast(fg)
            fg = enhancer.enhance(1.05)
            
            comp = bg_source.copy()
            
            # Add a soft drop shadow effect
            shadow = Image.new('RGBA', fg.size, (0, 0, 0, 0))
            shadow_mask = fg.getchannel('A').point(lambda p: p * 0.4)
            shadow.paste((0, 0, 0), (0, 0), shadow_mask)
            shadow = shadow.filter(ImageFilter.GaussianBlur(radius=10))
            
            offset_x = (800 - target_w) // 2
            offset_y = 800 - target_h - 20
            
            # Paste shadow slightly lower
            comp.paste(shadow, (offset_x, offset_y + 15), shadow)
            # Paste drink
            comp.paste(fg, (offset_x, offset_y), fg)
            
            comp.save(webp_path, 'WEBP', quality=88)
            success += 1
        except Exception as e:
            print(f"Error on {item}: {e}")
            
    print(f"✅ Composited {success} items to standard studio format!")

if __name__ == '__main__':
    main()
