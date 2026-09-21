import re

with open('index.html', 'r') as f:
    c = f.read()

# 1. Fix hero overlay to fade to Ivory instead of Black
# rgba(10, 15, 11, x) -> rgba(246, 241, 231, x)
c = re.sub(r'rgba\(10,\s*15,\s*11,\s*([0-9.]+)\)', r'rgba(246, 241, 231, \1)', c)

# 2. Replace #0A0F0B with var(--bg-darkest) where appropriate
# theme-color
c = c.replace('content="#0A0F0B"', 'content="#F6F1E7"')
# Hero overlay bottom fade
c = c.replace('#0A0F0B 100%', 'var(--bg-darkest) 100%')
# Button text color: was #0A0F0B (dark text on gold), now let's make it Espresso Brown (var(--text-white)) 
# Wait, Espresso Brown is --text-white. 
c = c.replace('color: #0A0F0B;', 'color: var(--text-white);')
# Wheel code bg
c = c.replace('background: #0A0F0B;', 'background: var(--bg-card);')

# 3. Replace #0E1510 with var(--bg-dark)
c = c.replace('#0E1510', 'var(--bg-dark)')

# 4. Replace #141D16 with var(--bg-card)
c = c.replace('#141D16', 'var(--bg-card)')

# 5. Wheel colors
c = c.replace("color: '#141D16'", "color: '#F9F6F0'")

with open('index.html', 'w') as f:
    f.write(c)
