import re

with open('index.html', 'r') as f:
    c = f.read()

share_js = """
      // H. Web Share API
      window.shareApp = async () => {
        if (navigator.share) {
          try {
            await navigator.share({
              title: 'Olion Coffee',
              text: 'Góc nhỏ bình yên giữa lòng Sài Gòn. Khám phá menu cà phê thủ công tinh tế ngay!',
              url: window.location.href,
            });
          } catch (err) {
            console.log('User cancelled share or error:', err);
          }
        } else {
          navigator.clipboard.writeText(window.location.href);
          showOlionToast('Đã sao chép link website!', '🔗');
        }
      };
"""

c = c.replace('if (drawerInstallBtn) drawerInstallBtn.addEventListener(\'click\', handleInstall);', 'if (drawerInstallBtn) drawerInstallBtn.addEventListener(\'click\', handleInstall);\n' + share_js)

with open('index.html', 'w') as f:
    f.write(c)
