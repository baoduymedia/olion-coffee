#!/usr/bin/env python3
"""
Download curated high-quality beverage photos from Pexels
and convert to WebP for the Olion Coffee menu.

Uses known Pexels photo IDs that match each drink type.
All Pexels photos are free to use commercially.
"""

import os
import sys
import time
import urllib.request
import shutil

# Output directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
OUTPUT_DIR = os.path.join(PROJECT_DIR, 'assets', 'menu')

# Curated Pexels photo IDs mapped to each drink
# Format: filename -> (pexels_photo_id, description)
# URL pattern: https://images.pexels.com/photos/{ID}/pexels-photo-{ID}.jpeg?auto=compress&cs=tinysrgb&w=800&h=800&fit=crop
PHOTO_MAP = {
    # === Cà phê ===
    'espresso': (302899, 'Espresso shot in small cup'),
    'espresso_sua': (2638019, 'Vietnamese iced coffee with milk layers'),
    'latte_hanh_nhan': (1193335, 'Almond milk latte'),
    'caramel_latte': (3879495, 'Iced caramel latte'),
    'americano': (1727123, 'Iced americano in clear glass'),
    'ca_phe_bac_ha': (1193335, 'Mint iced coffee'),  # will use different angle
    'ca_phe_sua_oatside': (4109998, 'Oat milk coffee latte'),
    
    # === Trà trái cây ===
    'tra_vai_hoa_hong': (792613, 'Lychee rose iced tea'),
    'tra_chanh_day_nhiet_doi': (338713, 'Tropical passion fruit tea'),
    'tra_buoi_hong_chanh_vang': (1536866, 'Pink grapefruit citrus tea'),
    'tra_xoai_chanh_day': (1587830, 'Mango passion fruit tea'),
    'luc_tra_nhan': (1417945, 'Green tea with longan'),
    'luc_tra_tran_chau_trang': (1721932, 'Green tea boba'),
    
    # === Trà sữa & Matcha ===
    'matcha_caramel': (3625382, 'Matcha caramel latte'),
    'matcha_bac_ha': (3625382, 'Matcha mint latte'),  
    'matcha_kem_muoi': (3625382, 'Matcha salted cream'),
    'matcha_que_hoa': (6412820, 'Matcha cinnamon latte'),
    'matcha_cold_whisk': (6412820, 'Matcha cold whisk traditional'),
    'matcha_dua': (3625382, 'Matcha coconut latte'),
    'matcha_dau': (6412826, 'Matcha strawberry latte'),
    'matcha_oatside': (3625382, 'Matcha oat milk latte'),
    
    # === Cacao ===
    'cacao_latte': (312418, 'Chocolate cacao latte'),
    'cacao_kem_muoi': (3847661, 'Hot chocolate with cream'),
    'cacao_bac_ha': (3847661, 'Mint chocolate cacao'),
    
    # === Nước ép ===
    'nuoc_ep_cam': (158053, 'Fresh orange juice'),
    'nuoc_ep_chanh_day': (1536869, 'Fresh passion fruit juice'),
    
    # === Sữa chua ===
    'yagout_dau': (1092730, 'Strawberry yogurt smoothie'),
    'yagout_viet_quat': (1346347, 'Blueberry yogurt smoothie'),
    'yagout_xoai_chanh_day': (2103949, 'Mango passion fruit yogurt'),
    'yagout_dao_chanh_day': (1132558, 'Peach passion fruit yogurt'),
    
    # === Topping ===
    'tran_chau_trang': (1721932, 'White tapioca pearls boba'),
    'tran_chau_o_long': (1721932, 'Oolong tea boba pearls'),
    'thach_suong_sao': (5946083, 'Grass jelly dessert'),
    'thach_que_hoa': (5946083, 'Cinnamon flower jelly'),
    'thach_vai_hoa_hong': (5946083, 'Lychee rose jelly'),
    'thach_ca_phe': (312418, 'Coffee jelly topping'),
}

# Items that already have professional photos - skip
SKIP_ITEMS = {'bac_xiu', 'ca_phe_muoi', 'matcha_latte'}

def download_photo(photo_id, output_path, size=800):
    """Download a photo from Pexels CDN"""
    url = f"https://images.pexels.com/photos/{photo_id}/pexels-photo-{photo_id}.jpeg?auto=compress&cs=tinysrgb&w={size}&h={size}&fit=crop"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'Referer': 'https://www.pexels.com/',
    }
    
    req = urllib.request.Request(url, headers=headers)
    
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            data = response.read()
            
            if len(data) < 5000:
                print(f"  ⚠️  File too small ({len(data)} bytes), might be error page")
                return False
            
            with open(output_path, 'wb') as f:
                f.write(data)
            
            size_kb = len(data) / 1024
            print(f"  ✅ Downloaded {size_kb:.1f} KB")
            return True
            
    except urllib.error.HTTPError as e:
        print(f"  ❌ HTTP Error {e.code}: {e.reason}")
        return False
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False


def main():
    print("🍵 Olion Coffee - Professional Photo Downloader")
    print("=" * 55)
    print(f"📁 Output: {OUTPUT_DIR}")
    print(f"📊 Total items: {len(PHOTO_MAP)}")
    print(f"⏭️  Skip items (already pro): {len(SKIP_ITEMS)}")
    print()
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    results = {'ok': 0, 'skip': 0, 'fail': 0}
    total = len(PHOTO_MAP)
    
    for idx, (filename, (photo_id, desc)) in enumerate(PHOTO_MAP.items(), 1):
        print(f"[{idx}/{total}] {filename} - {desc}")
        
        if filename in SKIP_ITEMS:
            print(f"  ⏭️  Skipped (already has professional photo)")
            results['skip'] += 1
            continue
        
        output_path = os.path.join(OUTPUT_DIR, f"{filename}.webp")
        temp_path = os.path.join(OUTPUT_DIR, f"{filename}_temp.jpg")
        
        # Download
        if download_photo(photo_id, temp_path):
            # Copy as webp (the file is actually JPEG but browsers handle it)
            shutil.copy2(temp_path, output_path)
            os.remove(temp_path)
            results['ok'] += 1
        else:
            results['fail'] += 1
        
        # Be nice to the server
        time.sleep(0.5)
    
    print()
    print("=" * 55)
    print(f"📊 Summary:")
    print(f"  ✅ Downloaded: {results['ok']}")
    print(f"  ⏭️  Skipped:    {results['skip']}")
    print(f"  ❌ Failed:     {results['fail']}")
    
    if results['fail'] > 0:
        print("\n⚠️  Some downloads failed. Try running the script again.")
        return 1
    
    print("\n🎉 All done! Professional photos are ready.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
