import re

with open('admin.html', 'r') as f:
    c = f.read()

# openEditMenuModal
c = re.sub(r'onclick="openEditMenuModal\(\$\{item\.id\}\)"', r'onclick="openEditMenuModal(\'${item.id}\')"', c)

# openPointHistoryModal
c = re.sub(r'onclick="openPointHistoryModal\(\$\{c\.id\},', r'onclick="openPointHistoryModal(\'${c.id}\',', c)

# togglePromo
c = re.sub(r'onclick="togglePromo\(\$\{p\.id\}\)"', r'onclick="togglePromo(\'${p.id}\')"', c)

# deletePromo
c = re.sub(r'onclick="deletePromo\(\$\{p\.id\}\)"', r'onclick="deletePromo(\'${p.id}\')"', c)

with open('admin.html', 'w') as f:
    f.write(c)
