import re

with open('index.html', 'r') as f:
    c = f.read()

modal = """  <!-- ======== 18. APP DOWNLOAD MODAL ======== -->
  <div class="modal-overlay" id="downloadAppModal" onclick="if(event.target === this) this.classList.remove('open')">
    <div class="modal-content" style="max-width: 480px; padding: 32px 24px; text-align: center; border-radius: 20px;">
      <button type="button" class="modal-close-btn" onclick="document.getElementById('downloadAppModal').classList.remove('open')">✕</button>
      <img src="assets/logo-white.webp" alt="Olion Logo" style="width: 140px; margin-bottom: 24px;" />
      <h3 style="font-family: var(--font-heading); color: var(--accent-gold); font-size: 1.6rem; margin-bottom: 12px;">Cài Đặt Ứng Dụng</h3>
      <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.6; margin-bottom: 28px;">
        Trải nghiệm mượt mà hơn, tích điểm nhanh chóng và nhận thông báo ưu đãi độc quyền.
      </p>

      <div style="display: flex; flex-direction: column; gap: 16px;">
        <!-- iOS Button -->
        <button class="btn btn-primary" onclick="showInstallGuide('ios')" style="background: #2D2D2D; color: #FFF; border: 1px solid #444; justify-content: center;">
          <i data-lucide="apple" style="width:20px;height:20px;margin-right:8px;"></i> Tải App cho iOS (iPhone/iPad)
        </button>

        <!-- Android Button -->
        <button class="btn btn-primary" onclick="handleAndroidInstall()" style="background: #1A73E8; color: #FFF; border: none; justify-content: center;">
          <i data-lucide="smartphone" style="width:20px;height:20px;margin-right:8px;"></i> Tải App cho Android
        </button>
      </div>

      <!-- Guides Area -->
      <div id="installGuideArea" style="display: none; margin-top: 24px; padding: 16px; background: rgba(255,255,255,0.05); border-radius: 12px; text-align: left;">
        <h4 id="guideTitle" style="color: var(--accent-gold); font-size: 1rem; margin-bottom: 12px; font-weight: 600;">Hướng dẫn</h4>
        <div id="guideContent" style="color: var(--text-body); font-size: 0.9rem; line-height: 1.6;"></div>
      </div>
    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/@vimeo/player@2.23.0/dist/player.min.js"></script>"""

c = c.replace('  <script src="https://cdn.jsdelivr.net/npm/@vimeo/player@2.23.0/dist/player.min.js"></script>', modal)

new_js = """      const handleInstall = () => {
        document.getElementById('downloadAppModal').classList.add('open');
      };

      window.showInstallGuide = function(platform) {
        const guideArea = document.getElementById('installGuideArea');
        const guideTitle = document.getElementById('guideTitle');
        const guideContent = document.getElementById('guideContent');
        guideArea.style.display = 'block';

        if (platform === 'ios') {
          guideTitle.innerHTML = '<i data-lucide="apple" style="width:16px;height:16px;margin-bottom:-2px;"></i> Hướng dẫn iOS (Safari)';
          guideContent.innerHTML = `
            <ol style="margin-left: 20px; margin-top: 0; padding-top: 0;">
              <li style="margin-bottom: 8px;">Mở trang web này bằng trình duyệt <strong>Safari</strong>.</li>
              <li style="margin-bottom: 8px;">Nhấn vào biểu tượng <strong>Chia sẻ (Share) <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="margin-bottom:-2px;"><path d="M4 12v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8"></path><polyline points="16 6 12 2 8 6"></polyline><line x1="12" y1="2" x2="12" y2="15"></line></svg></strong> ở thanh menu dưới cùng.</li>
              <li>Kéo xuống và chọn <strong>"Thêm vào MH chính" (Add to Home Screen) <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="margin-bottom:-2px;"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><line x1="12" y1="8" x2="12" y2="16"></line><line x1="8" y1="12" x2="16" y2="12"></line></svg></strong>.</li>
            </ol>
          `;
        }
        if (window.lucide) window.lucide.createIcons();
      };

      window.handleAndroidInstall = async function() {
        if (typeof deferredPrompt !== 'undefined' && deferredPrompt !== null) {
          deferredPrompt.prompt();
          await deferredPrompt.userChoice;
          deferredPrompt = null;
          document.getElementById('downloadAppModal').classList.remove('open');
        } else {
          const guideArea = document.getElementById('installGuideArea');
          const guideTitle = document.getElementById('guideTitle');
          const guideContent = document.getElementById('guideContent');
          guideArea.style.display = 'block';
          
          guideTitle.innerHTML = '<i data-lucide="smartphone" style="width:16px;height:16px;margin-bottom:-2px;"></i> Hướng dẫn Android (Chrome)';
          guideContent.innerHTML = `
            <ol style="margin-left: 20px; margin-top: 0; padding-top: 0;">
              <li style="margin-bottom: 8px;">Nhấn vào biểu tượng <strong>Menu 3 chấm [ ⋮ ]</strong> ở góc phải trên cùng trình duyệt.</li>
              <li>Chọn <strong>"Thêm vào màn hình chính" (Add to Home screen)</strong> hoặc <strong>"Cài đặt ứng dụng"</strong>.</li>
            </ol>
          `;
          if (window.lucide) window.lucide.createIcons();
        }
      };"""

c = re.sub(r'const handleInstall = async \(\) => \{.*?\};', new_js, c, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(c)

