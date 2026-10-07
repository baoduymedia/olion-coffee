import re

with open('index.html', 'r') as f:
    c = f.read()

c = c.replace('"closes": "21:00"', '"closes": "20:00"')
c = c.replace('08:00 — 21:00', '08:00 — 20:00')

with open('index.html', 'w') as f:
    f.write(c)

