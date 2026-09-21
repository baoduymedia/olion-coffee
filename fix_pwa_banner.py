import re

with open('index.html', 'r') as f:
    c = f.read()

pwa_css = """
  /* PWA INSTALL BANNER */
  #pwa-install-banner {
    position: fixed;
    bottom: 24px;
    left: 50%;
    transform: translate(-50%, 40px);
    background: var(--bg-card);
    border: 1px solid var(--border-gold);
    border-radius: 50px;
    padding: 10px 16px;
    display: flex;
    align-items: center;
    gap: 12px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    z-index: 9999;
    opacity: 0;
    pointer-events: none;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    white-space: nowrap;
  }
  
  #pwa-install-banner.show {
    opacity: 1;
    pointer-events: auto;
    transform: translate(-50%, 0);
  }

  .pwa-icon-box {
    width: 32px;
    height: 32px;
    border-radius: 50%;
    background: var(--accent-gold-glow);
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--accent-gold);
  }

  .pwa-text-col {
    display: flex;
    flex-direction: column;
  }

  .pwa-title {
    font-family: var(--font-heading);
    font-size: 15px;
    font-weight: 700;
    color: var(--text-white);
    line-height: 1.2;
  }

  .pwa-desc {
    font-size: 11px;
    color: var(--text-muted);
  }

  #pwa-install-btn {
    margin-left: 8px;
    background: var(--accent-gold);
    color: #FFFFFF;
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 600;
    transition: background 0.3s ease;
  }
  
  #pwa-install-btn:hover {
    background: var(--accent-gold-light);
  }

  #pwa-close-btn {
    color: var(--text-muted);
    padding: 4px;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  #pwa-close-btn:hover {
    color: var(--text-white);
  }
</style>
"""

c = c.replace('</style>', pwa_css, 1)

old_banner = """<div id="pwa-install-banner" class="fixed bottom-4 left-1/2 transform -translate-x-1/2 bg-surface border border-primary/20 rounded-full px-6 py-3 flex items-center gap-3 shadow-2xl z-[9999] opacity-0 pointer-events-none transition-all duration-500 translate-y-10">
  <div class="w-8 h-8 rounded-full bg-primary/10 flex items-center justify-center">
    <i data-lucide="download" class="w-4 h-4 text-primary"></i>
  </div>
  <div class="flex flex-col">
    <span class="text-sm font-heading font-medium text-text">Tải App Olion Coffee</span>
    <span class="text-xs text-text/60">Trải nghiệm nhanh & mượt mà hơn</span>
  </div>
  <button id="pwa-install-btn" class="ml-2 bg-primary text-surface px-4 py-1.5 rounded-full text-xs font-medium hover:bg-primary/90 transition-colors">Cài đặt</button>
  <button id="pwa-close-btn" class="text-text/40 hover:text-text p-1">
    <i data-lucide="x" class="w-4 h-4"></i>
  </button>
</div>"""

new_banner = """<div id="pwa-install-banner">
  <div class="pwa-icon-box">
    <i data-lucide="download" style="width: 16px; height: 16px;"></i>
  </div>
  <div class="pwa-text-col">
    <span class="pwa-title">Tải App Olion Coffee</span>
    <span class="pwa-desc">Trải nghiệm mượt mà & Offline</span>
  </div>
  <button id="pwa-install-btn">Cài đặt</button>
  <button id="pwa-close-btn">
    <i data-lucide="x" style="width: 16px; height: 16px;"></i>
  </button>
</div>"""

c = c.replace(old_banner, new_banner)

with open('index.html', 'w') as f:
    f.write(c)
