with open('index.html', 'r') as f:
    c = f.read()

modal = """
  <!-- ======== 18. APP DOWNLOAD MODAL ======== -->
  <div class="modal-overlay" id="downloadAppModal" onclick="if(event.target === this) this.classList.remove('open')">
    <div class="modal-content" style="max-width: 480px; padding: 32px 24px; text-align: center; border-radius: 20px;">
      <button type="button" class="modal-close-btn" onclick="document.getElementById('downloadAppModal').classList.remove('open')">✕</button>
      <img src="assets/logo-white.webp" alt="Olion Logo" style="width: 140px; margin-bottom: 24px;" loading="lazy" />
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
"""

c = c.replace('</body>', modal + '\n</body>')

with open('index.html', 'w') as f:
    f.write(c)
