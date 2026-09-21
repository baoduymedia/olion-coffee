import re

with open('index.html', 'r') as f:
    c = f.read()

# Extract floating install button
match = re.search(r'  <!-- Floating Install Button -->.*?  </button>\n', c, flags=re.DOTALL)
if match:
    btn_html = match.group(0)
    c = c.replace(btn_html, '')
    
    # Inject it right after <div class="olion-toast"...>...</div>
    c = re.sub(r'(  <div class="olion-toast".*?</div>\n)', r'\1\n' + btn_html, c, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(c)
