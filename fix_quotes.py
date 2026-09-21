import re

with open('admin.html', 'r') as f:
    c = f.read()

# Fix toggleApproveFeedback
c = re.sub(r'onclick="toggleApproveFeedback\(\$\{fb\.id\},', r'onclick="toggleApproveFeedback(\'${fb.id}\',', c)
# Fix handleDeleteFeedback
c = re.sub(r'onclick="handleDeleteFeedback\(\$\{fb\.id\}\)"', r'onclick="handleDeleteFeedback(\'${fb.id}\')" ', c)
# Fix handleDeleteMenuItem
c = re.sub(r'onclick="handleDeleteMenuItem\(\$\{item\.id\}\)"', r'onclick="handleDeleteMenuItem(\'${item.id}\')"', c)
# Fix handleDeleteCustomer
c = re.sub(r'onclick="handleDeleteCustomer\(\$\{c\.id\}\)"', r'onclick="handleDeleteCustomer(\'${c.id}\')"', c)
# Fix edit
c = re.sub(r'onclick="openEditMenuItem\(\$\{item\.id\}\)"', r'onclick="openEditMenuItem(\'${item.id}\')"', c)
c = re.sub(r'onclick="openLoyaltyAction\(\$\{c\.id\},', r'onclick="openLoyaltyAction(\'${c.id}\',', c)


with open('admin.html', 'w') as f:
    f.write(c)
