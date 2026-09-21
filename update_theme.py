import re

with open('index.html', 'r') as f:
    c = f.read()

new_root = """    :root {
      --font-heading: 'Cormorant Garamond', 'Playfair Display', Didot, Garamond, serif;
      --font-body: 'Poppins', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      
      /* Brand Guideline Tone of Voice */
      --bg-darkest: #F6F1E7; /* Warm Ivory (Nền chủ đạo) */
      --bg-dark: #FFFFFF;    /* Surface / White */
      --bg-card: #F9F6F0;    /* Slightly offset for cards */
      --bg-card-hover: #FFFFFF;
      
      --accent-gold: #B8A58B;       /* Warm Taupe */
      --accent-gold-light: #CBAF8D;
      --accent-gold-glow: rgba(184, 165, 139, 0.25);
      --accent-rust: #D32F2F;       /* Scarlet Red */
      --accent-green: #7C8268;      /* Muted Sage */
      --accent-green-bright: #9CA385;
      
      --text-white: #2C211B;  /* Espresso Brown (Chữ, menu, bao bì) */
      --text-cream: #3A2B23;
      --text-body: #514238;
      --text-muted: #84766C;
      
      --border-subtle: rgba(44, 33, 27, 0.1);
      --border-gold: rgba(184, 165, 139, 0.3);
      --border-green: rgba(124, 130, 104, 0.2);"""

c = re.sub(r'    :root \{.*?--border-green: rgba\(46, 204, 113, 0\.2\);', new_root, c, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(c)
