import re

with open('index.html', 'r') as f:
    c = f.read()

# 1. Add install button to header-actions
old_feedback_btn = '<button type="button" class="btn btn-ghost header-feedback-btn"'
new_install_btn = '<button type="button" class="btn btn-primary" id="headerInstallBtn" style="display: none; padding: 8px 16px; min-height: 38px; font-size: 12.5px; border-radius: 20px;" aria-label="Cài đặt App"><i data-lucide="download" style="width:16px;height:16px;margin-right:6px;"></i><span data-i18n="nav_install">Tải App</span></button>\n        '
c = c.replace(old_feedback_btn, new_install_btn + old_feedback_btn)

# 2. Add install button to drawer-nav
old_drawer_contact = '<a href="#contact" class="drawer-link"><span data-i18n="drawer_contact">Thông tin liên hệ</span> <span>→</span></a>'
new_drawer_install = '<a href="javascript:void(0)" id="drawerInstallBtn" class="drawer-link" style="display: none !important; color: var(--accent-gold); font-weight: 700;"><i data-lucide="download" style="width:16px;height:16px;margin-right:6px;"></i><span data-i18n="nav_install">Cài Đặt App Olion</span> <span>→</span></a>'
c = c.replace(old_drawer_contact, old_drawer_contact + '\n      ' + new_drawer_install)


# 3. Rewrite JS logic
old_js = """      // G. PWA Install Prompt
      let deferredPrompt;
      const installBanner = document.getElementById('pwa-install-banner');
      const installBtn = document.getElementById('pwa-install-btn');
      const closeInstallBtn = document.getElementById('pwa-close-btn');

      window.addEventListener('beforeinstallprompt', (e) => {
        e.preventDefault();
        deferredPrompt = e;
        if (installBanner) {
          installBanner.classList.remove('opacity-0', 'pointer-events-none', 'translate-y-10');
          installBanner.classList.add('opacity-100', 'translate-y-0');
        }
      });

      if (installBtn) {
        installBtn.addEventListener('click', async () => {
          if (deferredPrompt !== null) {
            deferredPrompt.prompt();
            await deferredPrompt.userChoice;
            deferredPrompt = null;
            if (installBanner) {
              installBanner.style.display = 'none';
            }
          }
        });
      }

      if (closeInstallBtn) {
        closeInstallBtn.addEventListener('click', () => {
          if (installBanner) installBanner.style.display = 'none';
        });
      }"""

new_js = """      // G. PWA Install Prompt (Header & Drawer)
      let deferredPrompt;
      const headerInstallBtn = document.getElementById('headerInstallBtn');
      const drawerInstallBtn = document.getElementById('drawerInstallBtn');

      window.addEventListener('beforeinstallprompt', (e) => {
        e.preventDefault();
        deferredPrompt = e;
        if (headerInstallBtn) headerInstallBtn.style.display = 'inline-flex';
        if (drawerInstallBtn) drawerInstallBtn.style.setProperty('display', 'flex', 'important');
      });

      const handleInstall = async () => {
        if (deferredPrompt !== null) {
          deferredPrompt.prompt();
          await deferredPrompt.userChoice;
          deferredPrompt = null;
          if (headerInstallBtn) headerInstallBtn.style.display = 'none';
          if (drawerInstallBtn) drawerInstallBtn.style.setProperty('display', 'none', 'important');
        }
      };

      if (headerInstallBtn) headerInstallBtn.addEventListener('click', handleInstall);
      if (drawerInstallBtn) drawerInstallBtn.addEventListener('click', handleInstall);"""

c = c.replace(old_js, new_js)

# 4. Remove old #pwa-install-banner completely
c = re.sub(r'<div id="pwa-install-banner">.*?</div>', '', c, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(c)
