import re

with open('index.html', 'r') as f:
    c = f.read()

# Make the header button visible by default instead of display: none
c = c.replace('style="display: none; padding: 8px 16px; min-height: 38px; font-size: 12.5px; border-radius: 20px;"', 
              'style="display: inline-flex; padding: 8px 16px; min-height: 38px; font-size: 12.5px; border-radius: 20px;"')

# Make the drawer button visible by default
c = c.replace('style="display: none !important; color: var(--accent-gold); font-weight: 700;"', 
              'style="display: flex; color: var(--accent-gold); font-weight: 700;"')


old_js = """      // G. PWA Install Prompt (Header & Drawer)
      let deferredPrompt;
      const headerInstallBtn = document.getElementById('headerInstallBtn');
      const drawerInstallBtn = document.getElementById('drawerInstallBtn');

      window.addEventListener('beforeinstallprompt', (e) => {
        e.preventDefault();
        deferredPrompt = e;
        if (headerInstallBtn) headerInstallBtn.style.setProperty('display', 'inline-flex', 'important');
        if (drawerInstallBtn) drawerInstallBtn.style.setProperty('display', 'flex', 'important');
      });

      const handleInstall = async () => {
        if (deferredPrompt !== null) {
          deferredPrompt.prompt();
          await deferredPrompt.userChoice;
          deferredPrompt = null;
          if (headerInstallBtn) headerInstallBtn.style.setProperty('display', 'none', 'important');
          if (drawerInstallBtn) drawerInstallBtn.style.setProperty('display', 'none', 'important');
        }
      };"""

new_js = """      // G. PWA Install Prompt (Header & Drawer)
      let deferredPrompt = null;
      const headerInstallBtn = document.getElementById('headerInstallBtn');
      const drawerInstallBtn = document.getElementById('drawerInstallBtn');

      window.addEventListener('beforeinstallprompt', (e) => {
        e.preventDefault();
        deferredPrompt = e;
      });

      const handleInstall = async () => {
        if (deferredPrompt !== null) {
          deferredPrompt.prompt();
          await deferredPrompt.userChoice;
          deferredPrompt = null;
        } else {
          // Fallback if beforeinstallprompt didn't fire (e.g., iOS Safari or already installed)
          showOlionToast('Để cài đặt App, hãy nhấn vào biểu tượng Tải Xuống/Chia sẻ trên thanh địa chỉ của trình duyệt nhé!', 'info');
        }
      };"""

c = c.replace(old_js, new_js)

with open('index.html', 'w') as f:
    f.write(c)
