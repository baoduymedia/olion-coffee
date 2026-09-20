#!/usr/bin/env python3
"""
Download high-quality beverage stock photos from Unsplash Source (no API key needed)
and convert to WebP format for the Olion Coffee menu.

Usage: python3 scripts/download_stock_photos.py
"""

import os
import subprocess
import urllib.request
import time
import json

# Output directory
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'assets', 'menu')

# Map of menu items to Unsplash search queries
# Using source.unsplash.com which redirects to a random photo matching the query
MENU_ITEMS = {
    # Cà phê
    'espresso': {
        'name': 'ESPRESSO',
        'query': 'espresso+coffee+shot+dark',
        'skip': False
    },
    'espresso_sua': {
        'name': 'ESPRESSO SỮA',
        'query': 'vietnamese+iced+coffee+condensed+milk',
        'skip': False
    },
    # bac_xiu - already has professional photo
    'latte_hanh_nhan': {
        'name': 'LATTE HẠNH NHÂN',
        'query': 'almond+milk+latte+iced',
        'skip': False
    },
    'caramel_latte': {
        'name': 'CARAMEL LATTE',
        'query': 'caramel+latte+iced+drizzle',
        'skip': False
    },
    'americano': {
        'name': 'AMERICANO',
        'query': 'iced+americano+coffee+glass',
        'skip': False
    },
    # ca_phe_muoi - already has professional photo
    'ca_phe_bac_ha': {
        'name': 'CÀ PHÊ BẠC HÀ',
        'query': 'mint+coffee+iced+green',
        'skip': False
    },
    'ca_phe_sua_oatside': {
        'name': 'CÀ PHÊ SỮA OATSIDE',
        'query': 'oat+milk+coffee+latte',
        'skip': False
    },
    
    # Trà trái cây
    'tra_vai_hoa_hong': {
        'name': 'TRÀ VẢI HOA HỒNG',
        'query': 'lychee+rose+tea+iced',
        'skip': False
    },
    'tra_chanh_day_nhiet_doi': {
        'name': 'TRÀ CHANH DÂY NHIỆT ĐỚI',
        'query': 'passion+fruit+tea+tropical',
        'skip': False
    },
    'tra_buoi_hong_chanh_vang': {
        'name': 'TRÀ BƯỞI HỒNG CHANH VÀNG',
        'query': 'grapefruit+lemon+tea+iced',
        'skip': False
    },
    'tra_xoai_chanh_day': {
        'name': 'TRÀ XOÀI CHANH DÂY',
        'query': 'mango+passion+fruit+tea',
        'skip': False
    },
    'luc_tra_nhan': {
        'name': 'LỤC TRÀ NHÃN',
        'query': 'green+tea+longan+iced',
        'skip': False
    },
    'luc_tra_tran_chau_trang': {
        'name': 'LỤC TRÀ TRÂN CHÂU TRẮNG',
        'query': 'green+tea+boba+pearl+tapioca',
        'skip': False
    },
    
    # Trà sữa & Matcha
    # matcha_latte - already has professional photo
    'matcha_caramel': {
        'name': 'MATCHA CARAMEL',
        'query': 'matcha+caramel+latte+iced',
        'skip': False
    },
    'matcha_bac_ha': {
        'name': 'MATCHA BẠC HÀ',
        'query': 'matcha+mint+green+tea+iced',
        'skip': False
    },
    'matcha_kem_muoi': {
        'name': 'MATCHA KEM MUỐI',
        'query': 'matcha+salted+cream+latte',
        'skip': False
    },
    'matcha_que_hoa': {
        'name': 'MATCHA QUẾ HOA',
        'query': 'matcha+cinnamon+latte+flower',
        'skip': False
    },
    'matcha_cold_whisk': {
        'name': 'MATCHA COLD WHISK',
        'query': 'matcha+cold+whisk+traditional+japanese',
        'skip': False
    },
    'matcha_dua': {
        'name': 'MATCHA DỪA',
        'query': 'matcha+coconut+milk+latte',
        'skip': False
    },
    'matcha_dau': {
        'name': 'MATCHA DÂU',
        'query': 'matcha+strawberry+latte+pink',
        'skip': False
    },
    'matcha_oatside': {
        'name': 'MATCHA OATSIDE',
        'query': 'matcha+oat+milk+latte',
        'skip': False
    },
    
    # Cacao
    'cacao_latte': {
        'name': 'CACAO LATTE',
        'query': 'chocolate+cacao+latte+iced',
        'skip': False
    },
    'cacao_kem_muoi': {
        'name': 'CACAO KEM MUỐI',
        'query': 'hot+chocolate+salted+cream+cacao',
        'skip': False
    },
    'cacao_bac_ha': {
        'name': 'CACAO BẠC HÀ',
        'query': 'mint+chocolate+cacao+iced',
        'skip': False
    },
    
    # Nước ép
    'nuoc_ep_cam': {
        'name': 'NƯỚC ÉP CAM',
        'query': 'fresh+orange+juice+glass',
        'skip': False
    },
    'nuoc_ep_chanh_day': {
        'name': 'NƯỚC ÉP CHANH DÂY',
        'query': 'passion+fruit+juice+fresh',
        'skip': False
    },
    
    # Sữa chua
    'yagout_dau': {
        'name': 'YAGOUT DÂU',
        'query': 'strawberry+yogurt+smoothie+pink',
        'skip': False
    },
    'yagout_viet_quat': {
        'name': 'YAGOUT VIỆT QUẤT',
        'query': 'blueberry+yogurt+smoothie+purple',
        'skip': False
    },
    'yagout_xoai_chanh_day': {
        'name': 'YAGOUT XOÀI CHANH DÂY',
        'query': 'mango+passion+fruit+yogurt+smoothie',
        'skip': False
    },
    'yagout_dao_chanh_day': {
        'name': 'YAGOUT ĐÀO CHANH DÂY',
        'query': 'peach+passion+fruit+yogurt+smoothie',
        'skip': False
    },
    
    # Topping
    'tran_chau_trang': {
        'name': 'TRÂN CHÂU TRẮNG',
        'query': 'white+tapioca+pearl+boba+topping',
        'skip': False
    },
    'tran_chau_o_long': {
        'name': 'TRÂN CHÂU Ô LONG',
        'query': 'oolong+tea+boba+pearl+topping',
        'skip': False
    },
    'thach_suong_sao': {
        'name': 'THẠCH SƯƠNG SÁO',
        'query': 'grass+jelly+dessert+black',
        'skip': False
    },
    'thach_que_hoa': {
        'name': 'THẠCH QUẾ HOA',
        'query': 'cinnamon+jelly+dessert+topping',
        'skip': False
    },
    'thach_vai_hoa_hong': {
        'name': 'THẠCH VẢI HOA HỒNG',
        'query': 'lychee+rose+jelly+topping',
        'skip': False
    },
    'thach_ca_phe': {
        'name': 'THẠCH CÀ PHÊ',
        'query': 'coffee+jelly+dessert+topping',
        'skip': False
    },
}

def download_from_unsplash(query, output_path, size=800):
    """Download a photo from Unsplash Source"""
    url = f"https://source.unsplash.com/{size}x{size}/?{query}"
    print(f"  Downloading from: {url}")
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    }
    req = urllib.request.Request(url, headers=headers)
    
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            data = response.read()
            if len(data) < 1000:
                print(f"  ⚠️ Downloaded file too small ({len(data)} bytes), skipping")
                return False
            
            with open(output_path, 'wb') as f:
                f.write(data)
            print(f"  ✅ Downloaded {len(data)} bytes → {output_path}")
            return True
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False


def convert_to_webp(input_path, output_path, quality=85):
    """Convert image to WebP using sips (macOS)"""
    try:
        # First convert to a temp format then to webp
        subprocess.run([
            'sips', '-s', 'format', 'jpeg', 
            '-s', 'formatOptions', str(quality),
            input_path, '--out', output_path
        ], capture_output=True, check=True)
        print(f"  ✅ Converted to WebP: {output_path}")
        return True
    except Exception as e:
        print(f"  ❌ Conversion error: {e}")
        # Just copy the file
        import shutil
        shutil.copy2(input_path, output_path)
        return True


def main():
    print("🍵 Olion Coffee - Stock Photo Downloader")
    print("=" * 50)
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    total = len(MENU_ITEMS)
    downloaded = 0
    skipped = 0
    failed = 0
    
    for key, item in MENU_ITEMS.items():
        print(f"\n[{downloaded + skipped + failed + 1}/{total}] {item['name']} ({key})")
        
        if item.get('skip'):
            print("  ⏭️ Skipping (already has professional photo)")
            skipped += 1
            continue
        
        output_webp = os.path.join(OUTPUT_DIR, f"{key}.webp")
        output_jpg = os.path.join(OUTPUT_DIR, f"{key}_stock.jpg")
        
        # Download from Unsplash
        success = download_from_unsplash(item['query'], output_jpg)
        
        if success:
            # Copy as webp (or convert)
            import shutil
            shutil.copy2(output_jpg, output_webp)
            downloaded += 1
            # Clean up temp jpg
            os.remove(output_jpg)
        else:
            failed += 1
        
        # Rate limit - be nice to the server
        time.sleep(1)
    
    print(f"\n{'=' * 50}")
    print(f"📊 Results:")
    print(f"  ✅ Downloaded: {downloaded}")
    print(f"  ⏭️ Skipped: {skipped}")
    print(f"  ❌ Failed: {failed}")
    print(f"  📁 Output: {OUTPUT_DIR}")


if __name__ == '__main__':
    main()
