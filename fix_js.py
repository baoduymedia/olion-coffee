import re

with open('index.html', 'r') as f:
    c = f.read()

# Remove the CSS block for pwa-install-banner
c = re.sub(r'/\* PWA INSTALL BANNER \*/.*?#pwa-close-btn:hover {\n    color: var\(--text-white\);\n  }', '', c, flags=re.DOTALL)

# Replace the JS block safely
c = re.sub(r'// G\. PWA Install Prompt.*?// H\. SCROLL REVEAL ANIMATION', 
"""// G. PWA Install Prompt
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
      };

      if (headerInstallBtn) headerInstallBtn.addEventListener('click', handleInstall);
      if (drawerInstallBtn) drawerInstallBtn.addEventListener('click', handleInstall);

      // H. SCROLL REVEAL ANIMATION""", c, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(c)
