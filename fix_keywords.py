import re

with open('index.html', 'r') as f:
    c = f.read()

# Update keywords meta tag
old_kw = '<meta name="keywords" content="olion coffee, quán cà phê đẹp ở dương quảng hàm, cafe không gian sang trọng tphcm, quán cà phê gò vấp, cà phê muối gò vấp, bạc xỉu kem trứng sài gòn, matcha latte tphcm, quán cafe yên tĩnh làm việc gò vấp, cà phê dương quảng hàm, menu olion coffee" />'
new_kw = '<meta name="keywords" content="olion coffee, quán cafe gò vấp, quán cà phê đẹp gò vấp, cafe dương quảng hàm, cà phê muối gò vấp, cafe check in gò vấp, quán cafe làm việc gò vấp, cafe không gian đẹp, quán nước dương quảng hàm, bạc xỉu gò vấp, matcha latte gò vấp, quán cafe chạy deadline gò vấp, quán cafe yên tĩnh gò vấp, specialty coffee tphcm, cafe sang trọng, trà trái cây gò vấp, olion cafe, olion coffee dương quảng hàm" />'

c = c.replace(old_kw, new_kw)

# Add keywords to JSON-LD
# We find "servesCuisine" and append "keywords"
old_json = '"servesCuisine": ["Vietnamese Specialty Coffee", "Fine Espresso", "Japanese Matcha", "Fresh Fruit Tea", "Craft Cacao"],'
new_json = '"servesCuisine": ["Vietnamese Specialty Coffee", "Fine Espresso", "Japanese Matcha", "Fresh Fruit Tea", "Craft Cacao"],\n        "keywords": "olion coffee, cafe gò vấp, cà phê muối gò vấp, cafe dương quảng hàm, quán cafe đẹp, cafe làm việc, matcha latte gò vấp, quán nước gò vấp",'

c = c.replace(old_json, new_json)

with open('index.html', 'w') as f:
    f.write(c)

