import re

with open('admin.html', 'r') as f:
    c = f.read()
c = re.sub(r'p => p\.id === id', r'p => String(p.id) === String(id)', c)
with open('admin.html', 'w') as f:
    f.write(c)

with open('supabaseClient.js', 'r') as f:
    s = f.read()
s = re.sub(r'm\.id === id', r'String(m.id) === String(id)', s)
s = re.sub(r'f\.id === id', r'String(f.id) === String(id)', s)
s = re.sub(r'c\.id === cust\.id', r'String(c.id) === String(cust.id)', s)
with open('supabaseClient.js', 'w') as f:
    f.write(s)
