import re

with open('index.html', 'r') as f:
    c = f.read()

# 1. PWA JS
pwa_js = """
      // F. PWA / Service Worker Registration
      if ('serviceWorker' in navigator) {
        window.addEventListener('load', () => {
          navigator.serviceWorker.register('service-worker.js')
            .then((registration) => {
              console.log('ServiceWorker registration successful');
            }, (err) => {
              console.log('ServiceWorker registration failed: ', err);
            });
        });
      }

      // G. PWA Install Prompt
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
              installBanner.classList.add('opacity-0', 'pointer-events-none', 'translate-y-10');
              installBanner.classList.remove('opacity-100', 'translate-y-0');
            }
          }
        });
      }

      if (closeInstallBtn) {
        closeInstallBtn.addEventListener('click', () => {
          if (installBanner) {
            installBanner.classList.add('opacity-0', 'pointer-events-none', 'translate-y-10');
            installBanner.classList.remove('opacity-100', 'translate-y-0');
          }
        });
      }

    });
  </script>
</body>
"""
c = c.replace("    });\n  </script>\n</body>", pwa_js)

# 2. Feedback Form Fix
feedback_old = """          if (typeof submitFeedbackToCloud === 'function') {
            await submitFeedbackToCloud({
              name,
              contact,
              rating: chosenRating,
              content: message,
              imageDataUrl: imageDataUrl
            });
          }

          btnSubmitFeedback.disabled = false;
          btnSubmitFeedback.textContent = 'Gửi đánh giá ngay';

          // Reset image fields
          if (typeof removeFeedbackImage === 'function') {
            removeFeedbackImage();
          }

          document.getElementById('feedbackFormArea').style.display = 'none';
          document.getElementById('feedbackSuccess').style.display = 'block';
          showOlionToast('Cảm ơn bạn đã gửi đánh giá quý báu cho Olion Coffee!', 'check-circle');"""

feedback_new = """          let success = false;
          if (typeof submitFeedbackToCloud === 'function') {
            const res = await submitFeedbackToCloud({
              name,
              contact,
              rating: chosenRating,
              content: message,
              imageDataUrl: imageDataUrl
            });
            success = res && res.success;
          } else {
            success = true; // Fallback
          }

          btnSubmitFeedback.disabled = false;
          btnSubmitFeedback.textContent = 'Gửi đánh giá ngay';

          if (success) {
            showOlionToast('Cảm ơn bạn đã góp ý!', 'check-circle');
            if (typeof removeFeedbackImage === 'function') {
              removeFeedbackImage();
            }
            document.getElementById('feedbackFormArea').style.display = 'none';
            const feedbackSuccessArea = document.getElementById('feedbackSuccessArea');
            if (feedbackSuccessArea) feedbackSuccessArea.style.display = 'block';
          } else {
            showOlionToast('Có lỗi xảy ra, vui lòng thử lại sau!', 'alert-triangle');
          }"""

c = c.replace(feedback_old, feedback_new)

# 3. Minigame Emoji Fix
c = c.replace("showOlionToast(`Chúc mừng bạn nhận được ưu đãi ${prize.code}!`, '🎉');", "showOlionToast(`Chúc mừng bạn nhận được ưu đãi ${prize.code}!`, 'gift');")

# 4. Remove Hardcoded Menus
def replace_menu_grid(m):
    return '<div class="menu-grid">\n          </div>'
c = re.sub(r'<div class="menu-grid">.*?</div>\n        </div>\n\n        <!--', lambda m: '<div class="menu-grid">\n          </div>\n        </div>\n\n        <!--', c, flags=re.DOTALL)
# For the last one
c = re.sub(r'<div class="menu-grid">.*?</div>\n        </div>\n      </div>\n    </div>\n  </section>', '<div class="menu-grid">\n          </div>\n        </div>\n      </div>\n    </div>\n  </section>', c, flags=re.DOTALL)


# 5. Remove dummy check in syncMenuFromCloud
c = re.sub(r'\s*// Reject outdated dummy test items.*?\n\s*if\s*\(isDummyData\).*?return;\n\s*}', '', c, flags=re.DOTALL)


with open('index.html', 'w') as f:
    f.write(c)

