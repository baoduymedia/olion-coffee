import re

with open('index.html', 'r') as f:
    c = f.read()

# Replace og:image URLs
c = c.replace('https://baoduymedia.github.io/olion-coffee/assets/space-4.webp', 'https://olion-coffee.vercel.app/assets/logo.png?v=2')

# Replace type
c = c.replace('<meta property="og:image:type" content="image/webp" />', '<meta property="og:image:type" content="image/png" />')

# Replace alt
c = c.replace('<meta property="og:image:alt" content="Không gian sang trọng ấm cúng tại Olion Coffee Dương Quảng Hàm" />', '<meta property="og:image:alt" content="Olion Coffee Logo" />')

# Replace dimensions
c = c.replace('<meta property="og:image:width" content="1200" />', '<meta property="og:image:width" content="512" />')
c = c.replace('<meta property="og:image:height" content="630" />', '<meta property="og:image:height" content="512" />')

with open('index.html', 'w') as f:
    f.write(c)

