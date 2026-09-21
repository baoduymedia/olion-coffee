import json

with open('manifest.json', 'r') as f:
    manifest = json.load(f)

manifest['shortcuts'] = [
    {
      "name": "Khám phá Thực đơn",
      "short_name": "Thực đơn",
      "description": "Xem danh sách đồ uống",
      "url": "/index.html#menu",
      "icons": [{ "src": "assets/logo-white.png", "sizes": "192x192", "type": "image/png" }]
    },
    {
      "name": "Chỉ đường tới Quán",
      "short_name": "Chỉ đường",
      "description": "Mở Google Maps",
      "url": "https://maps.app.goo.gl/vfqfzV82xyswVRTm6",
      "icons": [{ "src": "assets/logo-transparent.png", "sizes": "192x192", "type": "image/png" }]
    },
    {
      "name": "Gọi Hotline",
      "short_name": "Hotline",
      "description": "Gọi đặt bàn / giao hàng",
      "url": "tel:0783657587",
      "icons": [{ "src": "assets/logo.png", "sizes": "192x192", "type": "image/png" }]
    }
]

with open('manifest.json', 'w') as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)

