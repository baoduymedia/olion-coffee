import re

# 1. index.html
with open('index.html', 'r') as f:
    text = f.read()
text = text.replace('href="admin.html"', 'href="admin"')
text = text.replace("window.location.href = 'admin.html'", "window.location.href = 'admin'")
with open('index.html', 'w') as f:
    f.write(text)

# 2. news.html
with open('news.html', 'r') as f:
    text = f.read()
text = text.replace('href="admin.html"', 'href="admin"')
with open('news.html', 'w') as f:
    f.write(text)

# 3. admin.html
with open('admin.html', 'r') as f:
    text = f.read()
text = text.replace('href="index.html"', 'href="/"')
with open('admin.html', 'w') as f:
    f.write(text)

# 4. manifest.json
with open('manifest.json', 'r') as f:
    text = f.read()
text = text.replace('"./index.html"', '"/"')
text = text.replace('"/index.html#menu"', '"/#menu"')
with open('manifest.json', 'w') as f:
    f.write(text)

# 5. sitemap.xml
with open('sitemap.xml', 'r') as f:
    text = f.read()
text = text.replace('<loc>https://www.olioncoffee.app/admin.html</loc>', '<loc>https://www.olioncoffee.app/news</loc>')
with open('sitemap.xml', 'w') as f:
    f.write(text)

# 6. service-worker.js (only match cache arrays, we can cache `/` instead of `./index.html`)
with open('service-worker.js', 'r') as f:
    text = f.read()
text = text.replace("'./index.html',", "'/',")
text = text.replace("caches.match('./index.html')", "caches.match('/')")
with open('service-worker.js', 'w') as f:
    f.write(text)
