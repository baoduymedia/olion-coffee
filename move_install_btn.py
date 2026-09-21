import re

with open('index.html', 'r') as f:
    c = f.read()

# Remove the button from header-actions
c = re.sub(r'<button type="button" class="btn btn-primary" id="headerInstallBtn".*?</button>', '', c, flags=re.DOTALL)

# Add a floating button on bottom left
floating_btn = """
  <!-- Floating Install Button -->
  <button id="floatingInstallBtn" class="btn btn-primary" style="position: fixed; bottom: 24px; left: 24px; z-index: 1000; padding: 10px 20px; border-radius: 50px; display: inline-flex; align-items: center; gap: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
    <i data-lucide="download" style="width: 18px; height: 18px;"></i>
    <span style="font-weight: 600; font-size: 14px;">Tải App Olion</span>
  </button>
"""
c = c.replace('</body>', floating_btn + '\n</body>')

# Update JS to bind to the new button
c = c.replace("const headerInstallBtn = document.getElementById('headerInstallBtn');", "const floatingInstallBtn = document.getElementById('floatingInstallBtn');")
c = c.replace("if (headerInstallBtn)", "if (floatingInstallBtn)")
c = c.replace("headerInstallBtn.style", "floatingInstallBtn.style")
c = c.replace("headerInstallBtn.addEventListener", "floatingInstallBtn.addEventListener")

with open('index.html', 'w') as f:
    f.write(c)
