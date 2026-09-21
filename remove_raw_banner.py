import re

with open('index.html', 'r') as f:
    c = f.read()

# The raw banner looks like this:
raw_html = """  <div class="pwa-text-col">
    <span class="pwa-title">Tải App Olion Coffee</span>
    <span class="pwa-desc">Trải nghiệm mượt mà & Offline</span>
  </div>
  <button id="pwa-install-btn">Cài đặt</button>
  <button id="pwa-close-btn">
    <i data-lucide="x" style="width: 16px; height: 16px;"></i>
  </button>
</div>"""

c = c.replace(raw_html, "")

with open('index.html', 'w') as f:
    f.write(c)
