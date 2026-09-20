#!/usr/bin/env python3
import os
import urllib.request
import urllib.parse
import time
import shutil

# Import the prompts dictionary from the existing batch script
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from batch_generate_menu import MENU_ITEMS_PROMPTS

# Skip the ones we already successfully generated manually before
SKIP_ITEMS = {'bac_xiu', 'ca_phe_muoi', 'matcha_latte'}

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'assets', 'menu')

def download_pollinations_image(prompt, output_path):
    """
    Generate and download an image using the free pollinations.ai API
    """
    # URL encode the prompt
    encoded_prompt = urllib.parse.quote(prompt)
    
    # We add &nologo=true to remove their watermark, and specify a square size
    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=800&height=800&nologo=true"
    
    print(f"  Generating... (this may take a few seconds)")
    
    # We use a standard user-agent so we don't get blocked
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    req = urllib.request.Request(url, headers=headers)
    
    try:
        with urllib.request.urlopen(req, timeout=60) as response:
            data = response.read()
            if len(data) < 5000:
                print(f"  ❌ File too small ({len(data)} bytes), generation might have failed.")
                return False
                
            # Write out
            with open(output_path, 'wb') as f:
                f.write(data)
                
            size_kb = len(data) / 1024
            print(f"  ✅ Success: Saved {size_kb:.1f} KB")
            return True
            
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False

def main():
    print("🎨 Olion Coffee - Free AI Product Photography Generator (Pollinations)")
    print("=" * 65)
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    success = 0
    failed = 0
    skipped = 0
    
    for key, data in MENU_ITEMS_PROMPTS.items():
        print(f"\n[{success + failed + skipped + 1}/{len(MENU_ITEMS_PROMPTS)}] {data['name']}")
        
        if key in SKIP_ITEMS:
            print("  ⏭️ Skipped (already has custom professional photo)")
            skipped += 1
            continue
            
        output_webp = os.path.join(OUTPUT_DIR, f"{key}.webp")
        temp_jpg = os.path.join(OUTPUT_DIR, f"{key}_temp.jpg")
        
        # We append a style instruction to ensure consistency
        full_prompt = data['prompt'] + " high quality food photography, dramatic lighting, clean background, 8k, highly detailed, photorealistic."
        
        is_success = download_pollinations_image(full_prompt, temp_jpg)
        
        if is_success:
            # We just copy the file over to .webp extension. 
            # Modern browsers handle JPEG data inside a .webp extension just fine.
            shutil.copy2(temp_jpg, output_webp)
            os.remove(temp_jpg)
            success += 1
        else:
            failed += 1
            
        # Slight pause to avoid hitting rate limits hard
        time.sleep(2)
        
    print("\n" + "=" * 65)
    print("📊 FINAL SUMMARY")
    print(f"  ✅ Generated: {success}")
    print(f"  ⏭️ Skipped:   {skipped}")
    print(f"  ❌ Failed:    {failed}")
    
if __name__ == "__main__":
    main()
