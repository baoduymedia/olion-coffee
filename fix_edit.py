import re

with open('admin.html', 'r') as f:
    c = f.read()

c = re.sub(r'const item = cachedMenuItems\.find\(m => m\.id === id\);', r'const item = cachedMenuItems.find(m => String(m.id) === String(id));', c)

with open('admin.html', 'w') as f:
    f.write(c)
