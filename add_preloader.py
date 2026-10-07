import re

with open('index.html', 'r') as f:
    c = f.read()

preloader = """
  <!-- ======== PRELOADER ======== -->
  <div id="pagePreloader" style="position: fixed; inset: 0; z-index: 999999; background: var(--bg-dark); display: flex; flex-direction: column; align-items: center; justify-content: center; transition: opacity 0.5s ease; opacity: 1;">
    <img src="assets/logo-white.webp" alt="Olion Logo" style="width: 140px; margin-bottom: 24px; animation: pl-pulse 2s infinite ease-in-out;" />
    <div style="width: 36px; height: 36px; border: 3px solid rgba(211, 108, 45, 0.2); border-top-color: var(--accent-gold); border-radius: 50%; animation: pl-spin 1s linear infinite;"></div>
    <p style="margin-top: 20px; color: var(--text-muted); font-size: 14px; font-family: var(--font-body); letter-spacing: 1px;">Đang chuẩn bị không gian...</p>
  </div>
  <style>
    @keyframes pl-pulse { 0% { opacity: 0.8; transform: scale(0.98); } 50% { opacity: 1; transform: scale(1.02); } 100% { opacity: 0.8; transform: scale(0.98); } }
    @keyframes pl-spin { to { transform: rotate(360deg); } }
    body.loading { overflow: hidden; }
  </style>
  <script>
    document.body.classList.add('loading');
    function hidePreloader() {
      const p = document.getElementById('pagePreloader');
      if (p) {
        p.style.opacity = '0';
        document.body.classList.remove('loading');
        setTimeout(() => p.remove(), 500);
      }
    }
    // Chờ tối đa 5 giây hoặc ẩn ngay khi load xong
    window.addEventListener('load', hidePreloader);
    setTimeout(hidePreloader, 5000);
  </script>
"""

c = c.replace('<body>', '<body>' + preloader, 1)

with open('index.html', 'w') as f:
    f.write(c)
