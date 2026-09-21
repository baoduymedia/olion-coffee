import re

with open('index.html', 'r') as f:
    c = f.read()

# 1. Revert CSS Variables
new_root = """    :root {
      --font-heading: 'Cormorant Garamond', 'Playfair Display', Didot, Garamond, serif;
      --font-body: 'Poppins', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      
      --bg-darkest: #0A0F0B;
      --bg-dark: #0E1510;
      --bg-card: #141D16;
      --bg-card-hover: #1A261D;
      
      --accent-gold: #E59A55;
      --accent-gold-light: #F3B378;
      --accent-gold-glow: rgba(229, 154, 85, 0.25);
      --accent-rust: #D86326;
      --accent-green: #1D5A38;
      --accent-green-bright: #2ECC71;
      
      --text-white: #FFFFFF;
      --text-cream: #F5EFE6;
      --text-body: #D4CDC3;
      --text-muted: #8F968E;
      
      --border-subtle: rgba(255, 255, 255, 0.08);
      --border-gold: rgba(229, 154, 85, 0.25);
      --border-green: rgba(46, 204, 113, 0.2);"""

c = re.sub(r'    :root \{.*?--border-green: rgba\(124, 130, 104, 0\.2\);', new_root, c, flags=re.DOTALL)

# 2. Revert Hero Overlay
c = re.sub(r'rgba\(246,\s*241,\s*231,\s*([0-9.]+)\)', r'rgba(10, 15, 11, \1)', c)
# Fix theme-color
c = c.replace('content="#F6F1E7"', 'content="#0A0F0B"')

# 3. Restore shadows (approximate or exact)
c = c.replace('rgba(0, 0, 0, 0.15)', 'rgba(0, 0, 0, 0.65)')
c = c.replace('rgba(0, 0, 0, 0.2)', 'rgba(0, 0, 0, 0.8)')
c = c.replace('rgba(0, 0, 0, 0.1)', 'rgba(0, 0, 0, 0.5)')
c = c.replace('rgba(0, 0, 0, 0.08)', 'rgba(0, 0, 0, 0.4)')
c = c.replace('rgba(0, 0, 0, 0.12)', 'rgba(0, 0, 0, 0.6)')
c = c.replace('rgba(0,0,0,0.1)', 'rgba(0,0,0,0.5)')
c = c.replace('rgba(0,0,0,0.08)', 'rgba(0,0,0,0.4)')

# 4. Wheel colors back to dark
c = c.replace("color: '#F9F6F0'", "color: '#141D16'")

# 5. Fix form input background in index.html and admin.html
# Wait, form input was var(--bg-dark), which is back to dark now. 
# But in admin.html I manually changed rgba(0,0,0,0.25) to rgba(255,255,255,0.6)

with open('index.html', 'w') as f:
    f.write(c)

# ADMIN.HTML REVERT
with open('admin.html', 'r') as f:
    admin_c = f.read()

admin_root = """    :root {
      --bg-dark: #190D07;
      --bg-sidebar: #22120A;
      --bg-card: #2C1810;
      --bg-hover: #382015;
      --accent: #E59A55;
      --accent-hover: #F2AC6D;
      --gold: #C59B63;
      --text: #F6F1E7;
      --text-muted: #B8A58B;
      --border: rgba(184, 165, 139, 0.18);
      --success: #2ECC71;
      --danger: #E74C3C;
      --purple: #9B59B6;"""

admin_c = re.sub(r'    :root \{.*?--purple: #B8A58B;', admin_root, admin_c, flags=re.DOTALL)
admin_c = admin_c.replace('background: rgba(255, 255, 255, 0.6);', 'background: rgba(0, 0, 0, 0.25);')
admin_c = admin_c.replace('background: rgba(255,255,255,0.8);', 'background: rgba(0, 0, 0, 0.2);')

with open('admin.html', 'w') as f:
    f.write(admin_c)

