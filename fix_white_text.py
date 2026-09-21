import re

with open('index.html', 'r') as f:
    c = f.read()

# Replace color: #FFFFFF; and color: #FFF; with color: var(--text-white);
c = re.sub(r'color:\s*#FFF(FFF)?\b(.*?);', r'color: var(--text-white)\2;', c, flags=re.IGNORECASE)

# Fix back badges
c = c.replace('.badge-hot { background: var(--accent-rust); color: var(--text-white); }', '.badge-hot { background: var(--accent-rust); color: #FFFFFF; }')
c = c.replace('.badge-signature { background: var(--accent-green); color: var(--text-white);', '.badge-signature { background: var(--accent-green); color: #FFFFFF;')
c = c.replace('.badge-new { background: #3498DB; color: var(--text-white); }', '.badge-new { background: #3498DB; color: #FFFFFF; }')

# Fix back .btn-primary
c = c.replace('.btn-primary {\n      background: linear-gradient(135deg, var(--accent-gold) 0%, var(--accent-rust) 100%);\n      color: var(--text-white);', 
              '.btn-primary {\n      background: linear-gradient(135deg, var(--accent-gold) 0%, var(--accent-rust) 100%);\n      color: #FFFFFF;')

# Write back
with open('index.html', 'w') as f:
    f.write(c)
