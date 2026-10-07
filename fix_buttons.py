import re

with open('index.html', 'r') as f:
    c = f.read()

# Make dock visible on mobile and adjust scale
old_css = """    @media (max-width: 767px) {
      .floating-social-dock { display: none; }
    }"""
new_css = """    @media (max-width: 767px) {
      .floating-social-dock {
        bottom: 85px;
        right: 12px;
        transform: scale(0.9);
        transform-origin: bottom right;
      }
    }"""
c = c.replace(old_css, new_css)

# Replace the HTML dock
old_html = """  <aside class="floating-social-dock" aria-label="Liên hệ nhanh">
    <a href="tel:0783657587" class="float-icon-btn" title="Gọi Hotline: 0783 657 587" aria-label="Gọi hotline">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M6.62 10.79a15.05 15.05 0 006.59 6.59l2.2-2.2a1 1 0 011.02-.24 11.4 11.4 0 003.57.57 1 1 0 011 1v3.5a1 1 0 01-1 1A17 17 0 013 4a1 1 0 011-1h3.5a1 1 0 011 1 11.4 11.4 0 00.57 3.57 1 1 0 01-.24 1.02l-2.21 2.2z"/></svg>
    </a>
    <a href="https://zalo.me/0783657587" target="_blank" rel="noopener noreferrer" class="float-icon-btn" title="Chat Zalo" aria-label="Chat Zalo">
      <img src="assets/zalo-logo.webp" alt="Zalo" width="22" height="22" loading="lazy" decoding="async" />
    </a>
    <a href="https://maps.app.goo.gl/ZHHq6Rw4GDNJ2nkf9" target="_blank" rel="noopener noreferrer" class="float-icon-btn" title="Chỉ đường Google Maps" aria-label="Google Maps">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7z" fill="#EA4335"/><circle cx="12" cy="9" r="2.8" fill="#FFFFFF"/></svg>
    </a>
  </aside>"""

new_html = """  <aside class="floating-social-dock" aria-label="Liên hệ nhanh">
    <a href="tel:0783657587" class="float-icon-btn" style="background: #007AFF; border:none;" title="Gọi Hotline: 0783 657 587" aria-label="Gọi hotline">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M6.62 10.79a15.05 15.05 0 006.59 6.59l2.2-2.2a1 1 0 011.02-.24 11.4 11.4 0 003.57.57 1 1 0 011 1v3.5a1 1 0 01-1 1A17 17 0 013 4a1 1 0 011-1h3.5a1 1 0 011 1 11.4 11.4 0 00.57 3.57 1 1 0 01-.24 1.02l-2.21 2.2z"/></svg>
    </a>
    <a href="https://zalo.me/0783657587" target="_blank" rel="noopener noreferrer" class="float-icon-btn" style="background: #0068FF; border:none;" title="Chat Zalo" aria-label="Chat Zalo">
      <img src="assets/zalo-logo.webp" alt="Zalo" width="22" height="22" loading="lazy" decoding="async" />
    </a>
    <a href="https://www.facebook.com/profile.php?id=61594159312837" target="_blank" rel="noopener noreferrer" class="float-icon-btn" style="background: #1877F2; border:none;" title="Facebook" aria-label="Facebook">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.469h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.469h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
    </a>
    <a href="https://www.tiktok.com/@olion.coffee" target="_blank" rel="noopener noreferrer" class="float-icon-btn" style="background: #000000; border:none;" title="Tiktok" aria-label="Tiktok">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12.525.02c1.31-.02 2.61-.01 3.91-.02.08 1.53.63 3.09 1.75 4.17 1.12 1.11 2.7 1.62 4.24 1.79v4.03c-1.44-.05-2.89-.35-4.2-.97-.57-.26-1.1-.59-1.62-.93-.01 2.92.01 5.84-.02 8.75-.08 1.4-.54 2.79-1.35 3.94-1.31 1.92-3.58 3.17-5.91 3.21-1.43.08-2.86-.31-4.08-1.03-2.02-1.12-3.44-3.1-3.66-5.39-.17-1.89.28-3.8 1.25-5.39 1.43-2.3 4.12-3.64 6.78-3.32v4.05c-1.66-.27-3.33.22-4.38 1.5-.6.7-.93 1.6-.96 2.53-.02 1.07.3 2.12.91 2.99.9 1.22 2.45 1.83 3.94 1.5 1.53-.33 2.65-1.55 2.87-3.08.1-1.39.05-2.79.05-4.18V.02z"/></svg>
    </a>
  </aside>"""
c = c.replace(old_html, new_html)

with open('index.html', 'w') as f:
    f.write(c)

