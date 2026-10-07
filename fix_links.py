import re

with open('index.html', 'r') as f:
    c = f.read()

# Replace all old short links
c = c.replace('https://maps.app.goo.gl/vfqfzV82xyswVRTm6', 'https://maps.app.goo.gl/ZHHq6Rw4GDNJ2nkf9')

with open('index.html', 'w') as f:
    f.write(c)

with open('manifest.json', 'r') as f:
    m = f.read()
m = m.replace('https://maps.app.goo.gl/vfqfzV82xyswVRTm6', 'https://maps.app.goo.gl/ZHHq6Rw4GDNJ2nkf9')
with open('manifest.json', 'w') as f:
    f.write(m)
