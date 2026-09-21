import re

with open('admin.html', 'r') as f:
    c = f.read()

new_root = """    :root {
      /* Bảng màu Brand Guideline cho Admin (Dark/Light hybrid) */
      --bg-dark: #F6F1E7;
      --bg-sidebar: #EBE5D8;
      --bg-card: #FFFFFF;
      --bg-hover: #FDFBFC;
      --accent: #B8A58B;
      --accent-hover: #CBAF8D;
      --gold: #B8A58B;
      --text: #2C211B;
      --text-muted: #7C8268;
      --border: rgba(44, 33, 27, 0.1);
      --success: #7C8268;
      --danger: #D32F2F;
      --purple: #B8A58B;"""

c = re.sub(r'    :root \{.*?--purple: #9B59B6;', new_root, c, flags=re.DOTALL)

with open('admin.html', 'w') as f:
    f.write(c)
