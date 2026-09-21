import subprocess
import urllib.parse
from PIL import Image
import os

output_path = "assets/menu/ca_phe_muoi.webp"
prompt = (
    "Professional commercial beverage photography of Vietnamese Salted Coffee (Cà Phê Muối). "
    "Served in a clear fluted glass cup, showing distinct layers: a thick layer of creamy white condensed milk at the bottom, "
    "rich dark espresso coffee in the middle, and topped with a thick, velvety layer of white salted cream foam. "
    "Set on a luxury dark walnut cafe table with a few roasted coffee beans scattered nearby. "
    "Moody ambient cafe lighting, warm golden rim light, shallow depth of field, 8k resolution, photorealistic."
)

encoded_prompt = urllib.parse.quote(prompt)
url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=800&height=800&model=flux&nologo=true"
temp_path = "assets/menu/ca_phe_muoi_temp.jpg"

print("Generating Cà Phê Muối...")
subprocess.run(["curl", "-s", "-L", "-o", temp_path, url], check=True)

if os.path.exists(temp_path) and os.path.getsize(temp_path) > 5000:
    with Image.open(temp_path) as img:
        width, height = img.size
        crop_height = int(height * 0.94)
        cropped_img = img.crop((0, 0, width, crop_height))
        final_img = cropped_img.resize((width, height), Image.Resampling.LANCZOS)
        final_img.save(output_path, "WEBP", quality=90)
    os.remove(temp_path)
    print(f"Successfully generated: {output_path}")
else:
    print("Failed to generate Cà Phê Muối.")
