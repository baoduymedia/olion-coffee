import re

with open('index.html', 'r') as f:
    c = f.read()

new_js = """      // G. PWA Install Prompt
      let deferredPrompt = null;
      const floatingInstallBtn = document.getElementById('floatingInstallBtn');
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
          showOlionToast('Để cài đặt App, hãy nhấn vào biểu tượng Tải Xuống/Chia sẻ trên trình duyệt nhé!', 'info');
        }
      };

      if (floatingInstallBtn) floatingInstallBtn.addEventListener('click', handleInstall);
      if (drawerInstallBtn) drawerInstallBtn.addEventListener('click', handleInstall);
"""

# Replace from // G. PWA Install Prompt to the end of the script tag
c = re.sub(r'// G\. PWA Install Prompt.*?(?=\s*}\);\s*</script>)', new_js, c, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(c)
