import os
import sys
import subprocess
import urllib.parse
import time
from PIL import Image
from batch_generate_menu import MENU_ITEMS_PROMPTS

def generate_image(item_key, item_data):
    output_path = os.path.join(os.path.dirname(__file__), "..", item_data["output"])
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    prompt = item_data["prompt"]
    encoded_prompt = urllib.parse.quote(prompt)
    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=800&height=800&model=flux&nologo=true"
    
    temp_path = output_path.replace(".webp", "_temp.jpg")
    
    print(f"Generating {item_key}...")
    for attempt in range(3):
        try:
            result = subprocess.run(
                ["curl", "-s", "-L", "-o", temp_path, url],
                check=True,
                capture_output=True
            )
            
            if os.path.exists(temp_path):
                if os.path.getsize(temp_path) < 5000:
                    print(f"Attempt {attempt+1} failed {item_key}: image too small, retrying...")
                    time.sleep(2)
                    continue
                    
                with Image.open(temp_path) as img:
                    width, height = img.size
                    crop_height = int(height * 0.94)
                    cropped_img = img.crop((0, 0, width, crop_height))
                    final_img = cropped_img.resize((width, height), Image.Resampling.LANCZOS)
                    final_img.save(output_path, "WEBP", quality=90)
                
                os.remove(temp_path)
                print(f"Successfully generated and cropped: {output_path}")
                return True
        except Exception as e:
            print(f"Error processing {item_key}: {e}")
            time.sleep(2)
    print(f"Failed to generate {item_key} after 3 attempts.")
    return False

def main():
    print(f"Starting sequential generation of {len(MENU_ITEMS_PROMPTS)} items...")
    for key, data in MENU_ITEMS_PROMPTS.items():
        generate_image(key, data)
        time.sleep(2)

if __name__ == "__main__":
    main()
