/**
 * OLION COFFEE - SITE GATEKEEPER & ACCESS CONTROL SHIELD (KILL-SWITCH)
 * Giám sát và điều khiển trạng thái bật/tắt toàn bộ website olioncoffee.app
 * Khi Website TẮT: Khách hàng vào bất kỳ đường link nào đều bị chặn và hiển thị màn hình bảo trì sang trọng.
 * Khi Website BẬT: Hệ thống tự động mở lại ngay lập tức mà không cần người dùng thao tác.
 */

(function () {
  'use strict';

  // 1. Tuyệt đối không chặn trang Quản trị Admin
  const currentPath = (window.location.pathname || '').toLowerCase();
  if (currentPath.includes('admin') || currentPath.endsWith('admin.html')) {
    return;
  }

  // 2. Cấu hình Supabase & Thông tin mặc định
  const SUPABASE_URL = "https://xwbrbesgnwcngzohprxt.supabase.co";
  const SUPABASE_KEY = "sb_publishable_vWuV07_xPU0wNftK0lpnFQ_oA9XHPLS";
  const DEFAULT_TITLE = "Olion Coffee Tạm Đóng Cửa Để Nâng Cấp Dịch Vụ";
  const DEFAULT_MSG = "Hệ thống website đang tạm ngưng phục vụ để bảo trì & nâng cấp trải nghiệm tốt nhất cho quý khách. Rất mong quý khách thông cảm và hẹn sớm gặp lại!";
  const DEFAULT_TIME = "Dự kiến mở lại: Sớm nhất";
  const DEFAULT_HOTLINE = "0783 657 587";
  const DEFAULT_ZALO = "https://zalo.me/0783657587";
  const DEFAULT_ADDRESS = "80/64a Dương Quảng Hàm, P. An Nhơn, Gò Vấp, TP.HCM";

  // 3. Admin Bypass Check (Chỉ bypass khi có tham số tường minh ?admin_bypass=1 trên URL)
  const urlParams = new URLSearchParams(window.location.search);
  const isAdminBypass = urlParams.get('admin_bypass') === '1';
  if (isAdminBypass) {
    console.log('🛡️ [Gatekeeper] Admin Bypass Active: Đang xem trước bằng link Quản Trị Viên.');
    window.addEventListener('DOMContentLoaded', () => {
      const banner = document.createElement('div');
      banner.id = 'olionAdminPreviewBanner';
      banner.innerHTML = `
        <div style="position:fixed;top:0;left:0;right:0;z-index:2147483647;background:linear-gradient(90deg,#991b1b,#7f1d1d);color:#fff;padding:8px 16px;font-size:12.5px;font-family:sans-serif;display:flex;justify-content:space-between;align-items:center;box-shadow:0 2px 10px rgba(0,0,0,0.5);">
          <span>⚠️ <strong>CHẾ ĐỘ XEM TRƯỚC (ADMIN BYPASS):</strong> Khách hàng bình thường hiện đang thấy màn hình bảo trì.</span>
          <div style="display:flex;gap:8px;">
            <a href="admin.html" style="background:#fff;color:#991b1b;padding:4px 10px;border-radius:4px;text-decoration:none;font-weight:700;font-size:11.5px;">Vào Admin Bật Web ↗</a>
            <a href="${window.location.pathname}" style="background:rgba(255,255,255,0.2);color:#fff;padding:4px 10px;border-radius:4px;text-decoration:none;font-size:11.5px;">Xem Như Khách Thường</a>
          </div>
        </div>
      `;
      document.body.prepend(banner);
      document.body.style.paddingTop = '38px';
    });
    return;
  }

  // 4. CSS Chặn & Giao Diện Bảo Trì Luxury Coffee
  const INJECTED_CSS = `
    html.olion-site-offline body > *:not(#olionMaintenanceOverlay) {
      display: none !important;
    }
    html.olion-site-offline, html.olion-site-offline body {
      overflow: hidden !important;
      height: 100% !important;
      background: #0d0603 !important;
    }
    #olionMaintenanceOverlay {
      position: fixed !important;
      top: 0 !important;
      left: 0 !important;
      right: 0 !important;
      bottom: 0 !important;
      width: 100vw !important;
      height: 100vh !important;
      z-index: 2147483647 !important;
      background: radial-gradient(circle at 50% 20%, #2b150b 0%, #140904 55%, #080301 100%) !important;
      color: #f5efe6 !important;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif !important;
      display: flex !important;
      flex-direction: column !important;
      align-items: center !important;
      justify-content: center !important;
      padding: 24px 16px !important;
      box-sizing: border-box !important;
      overflow-y: auto !important;
      text-align: center !important;
      opacity: 1 !important;
      transition: opacity 0.4s ease, visibility 0.4s ease !important;
    }
    #olionMaintenanceOverlay.closing {
      opacity: 0 !important;
      pointer-events: none !important;
    }
    .olion-maint-card {
      max-width: 540px;
      width: 100%;
      background: rgba(28, 14, 8, 0.92);
      border: 1.5px solid rgba(229, 154, 85, 0.4);
      border-radius: 24px;
      padding: 38px 28px;
      box-shadow: 0 30px 70px rgba(0, 0, 0, 0.9), 0 0 50px rgba(229, 154, 85, 0.18);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      box-sizing: border-box;
      position: relative;
    }
    .olion-maint-logo {
      width: 120px;
      height: auto;
      margin-bottom: 20px;
      filter: drop-shadow(0 4px 15px rgba(229, 154, 85, 0.35));
    }
    .olion-maint-badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: rgba(231, 76, 60, 0.16);
      border: 1px solid rgba(231, 76, 60, 0.5);
      color: #ff7675;
      padding: 6px 16px;
      border-radius: 999px;
      font-size: 12px;
      font-weight: 800;
      letter-spacing: 0.8px;
      text-transform: uppercase;
      margin-bottom: 20px;
    }
    .olion-pulse-dot {
      width: 9px;
      height: 9px;
      border-radius: 50%;
      background: #e74c3c;
      box-shadow: 0 0 10px #e74c3c;
      animation: olionPulseAnim 1.6s infinite;
    }
    @keyframes olionPulseAnim {
      0% { transform: scale(0.9); opacity: 0.8; }
      50% { transform: scale(1.35); opacity: 1; }
      100% { transform: scale(0.9); opacity: 0.8; }
    }
    .olion-maint-title {
      font-family: Georgia, "Cormorant Garamond", "Times New Roman", serif;
      font-size: 26px;
      line-height: 1.35;
      color: #ffffff;
      margin: 0 0 14px 0;
      font-weight: 700;
      text-shadow: 0 2px 10px rgba(0,0,0,0.7);
    }
    .olion-maint-desc {
      font-size: 14.5px;
      line-height: 1.65;
      color: #d8c8ba;
      margin: 0 0 22px 0;
    }
    .olion-maint-box {
      background: rgba(0, 0, 0, 0.4);
      border: 1px dashed rgba(229, 154, 85, 0.35);
      border-radius: 14px;
      padding: 15px 18px;
      margin-bottom: 22px;
      font-size: 13.5px;
      color: #e59a55;
      display: flex;
      flex-direction: column;
      gap: 7px;
    }
    .olion-maint-actions {
      display: flex;
      gap: 12px;
      justify-content: center;
      flex-wrap: wrap;
      margin-bottom: 22px;
    }
    .olion-maint-btn-primary {
      background: linear-gradient(135deg, #e59a55, #c5823f);
      color: #120904;
      text-decoration: none;
      font-weight: 800;
      font-size: 14px;
      padding: 12px 22px;
      border-radius: 12px;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 5px 20px rgba(229, 154, 85, 0.35);
      transition: transform 0.2s, filter 0.2s;
    }
    .olion-maint-btn-primary:hover {
      transform: translateY(-2px);
      filter: brightness(1.1);
    }
    .olion-maint-btn-secondary {
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(229, 154, 85, 0.4);
      color: #f5efe6;
      text-decoration: none;
      font-weight: 600;
      font-size: 14px;
      padding: 12px 20px;
      border-radius: 12px;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: background 0.2s;
    }
    .olion-maint-btn-secondary:hover {
      background: rgba(229, 154, 85, 0.18);
    }
    .olion-maint-auto-reopen {
      font-size: 12px;
      color: #a38f7d;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
    }
    .olion-spinner {
      width: 14px;
      height: 14px;
      border: 2px solid rgba(229, 154, 85, 0.25);
      border-top-color: #e59a55;
      border-radius: 50%;
      animation: olionSpinAnim 1s linear infinite;
    }
    @keyframes olionSpinAnim {
      to { transform: rotate(360deg); }
    }
    .olion-admin-link {
      margin-top: 20px;
      font-size: 11.5px;
      color: rgba(255, 255, 255, 0.25);
      text-decoration: none;
      transition: color 0.2s;
      display: inline-block;
    }
    .olion-admin-link:hover {
      color: #e59a55;
    }
  `;

  function injectGatekeeperCSS() {
    if (document.getElementById('olionGatekeeperStyles')) return;
    const style = document.createElement('style');
    style.id = 'olionGatekeeperStyles';
    style.textContent = INJECTED_CSS;
    (document.head || document.documentElement).appendChild(style);
  }
  injectGatekeeperCSS();

  // 5. Kiểm tra nhanh từ Cache LocalStorage (Zero-Flicker Pre-render)
  let initialOffline = localStorage.getItem('olion_site_online') === 'false';
  if (initialOffline) {
    document.documentElement.classList.add('olion-site-offline');
  }

  let cachedInfo = null;
  try {
    cachedInfo = JSON.parse(localStorage.getItem('olion_maintenance_info') || 'null');
  } catch (e) {}

  // 6. Hàm render màn hình bảo trì
  function showMaintenanceOverlay(info) {
    document.documentElement.classList.add('olion-site-offline');
    let overlay = document.getElementById('olionMaintenanceOverlay');
    if (!overlay) {
      overlay = document.createElement('div');
      overlay.id = 'olionMaintenanceOverlay';
      overlay.setAttribute('role', 'dialog');
      overlay.setAttribute('aria-modal', 'true');
      overlay.setAttribute('aria-label', 'Thông báo tạm ngưng phục vụ');
      if (document.body) {
        document.body.appendChild(overlay);
      } else {
        window.addEventListener('DOMContentLoaded', () => {
          if (!document.getElementById('olionMaintenanceOverlay')) {
            document.body.appendChild(overlay);
          }
        });
      }
    }

    const title = (info && info.title) || (cachedInfo && cachedInfo.title) || DEFAULT_TITLE;
    const msg = (info && info.message) || (cachedInfo && cachedInfo.message) || DEFAULT_MSG;
    const time = (info && info.expected_time) || (cachedInfo && cachedInfo.expected_time) || DEFAULT_TIME;
    const hotline = (info && info.hotline) || (cachedInfo && cachedInfo.hotline) || DEFAULT_HOTLINE;
    const cleanPhone = hotline.replace(/[^0-9]/g, '') || "0783657587";

    overlay.innerHTML = `
      <div class="olion-maint-card">
        <img src="assets/logo-white.webp" onerror="this.src='assets/logo-white.png'" alt="Olion Coffee" class="olion-maint-logo" />
        <div>
          <span class="olion-maint-badge">
            <span class="olion-pulse-dot"></span>
            Hệ Thống Đang Tạm Ngưng Phục Vụ
          </span>
        </div>
        <h1 class="olion-maint-title">${title}</h1>
        <p class="olion-maint-desc">${msg}</p>

        <div class="olion-maint-box">
          <div style="font-weight: 700; color: #fff;">⏰ ${time}</div>
          <div style="font-size: 12.5px; color: #b8a58b;">📍 ${DEFAULT_ADDRESS}</div>
        </div>

        <div class="olion-maint-actions">
          <a href="tel:${cleanPhone}" class="olion-maint-btn-primary">
            <span>📞</span>
            <span>Gọi Hotline: ${hotline}</span>
          </a>
          <a href="${DEFAULT_ZALO}" target="_blank" rel="noopener noreferrer" class="olion-maint-btn-secondary">
            <span>💬</span>
            <span>Nhắn Tin Zalo</span>
          </a>
        </div>

        <div class="olion-maint-auto-reopen">
          <span class="olion-spinner"></span>
          <span>Hệ thống sẽ tự động mở lại ngay khi quán hoàn tất nâng cấp...</span>
        </div>

        <div>
          <a href="admin.html" class="olion-admin-link">🔒 Dành cho Quản trị viên (Đăng nhập)</a>
        </div>
      </div>
    `;
  }

  // 7. Hàm gỡ bỏ màn hình bảo trì (khi Web được Bật lại)
  function hideMaintenanceOverlay() {
    document.documentElement.classList.remove('olion-site-offline');
    const overlay = document.getElementById('olionMaintenanceOverlay');
    if (overlay) {
      overlay.classList.add('closing');
      setTimeout(() => {
        if (overlay && overlay.parentNode) {
          overlay.parentNode.removeChild(overlay);
        }
      }, 350);
    }
  }

  // Nếu ngay từ đầu cache báo offline, kích hoạt ngay
  if (initialOffline) {
    if (document.body) {
      showMaintenanceOverlay(cachedInfo);
    } else {
      window.addEventListener('DOMContentLoaded', () => showMaintenanceOverlay(cachedInfo));
    }
  }

  // 8. Trích xuất trạng thái Website từ Cloud Record
  function parseCloudStatus(data) {
    if (!data) return { isOnline: true };

    let isOnline = true;
    let title = DEFAULT_TITLE;
    let message = DEFAULT_MSG;
    let expected_time = DEFAULT_TIME;
    let hotline = DEFAULT_HOTLINE;

    // A. Kiểm tra cột riêng is_site_online
    if (typeof data.is_site_online === 'boolean') {
      isOnline = data.is_site_online;
    } else if (typeof data.is_site_online === 'string') {
      isOnline = data.is_site_online === 'true';
    }

    // B. Kiểm tra fallback tag <!--SITE_STATUS:{...}--> trong notification_text
    if (data.notification_text && typeof data.notification_text === 'string') {
      const match = data.notification_text.match(/<!--SITE_STATUS:(\{[\s\S]*?\})-->/);
      if (match && match[1]) {
        try {
          const parsed = JSON.parse(match[1]);
          if (parsed && typeof parsed.online === 'boolean') {
            isOnline = parsed.online;
          }
          if (parsed.title) title = parsed.title;
          if (parsed.message) message = parsed.message;
          if (parsed.expected_time) expected_time = parsed.expected_time;
          if (parsed.hotline) hotline = parsed.hotline;
        } catch (e) {}
      }
    }

    if (data.maintenance_title) title = data.maintenance_title;
    if (data.maintenance_message) message = data.maintenance_message;
    if (data.maintenance_expected_time) expected_time = data.maintenance_expected_time;
    if (data.maintenance_hotline) hotline = data.maintenance_hotline;

    return { isOnline, title, message, expected_time, hotline };
  }

  // 9. Đồng bộ Cloud qua REST API
  let isChecking = false;
  let pollInterval = null;

  async function checkSiteStatusFromCloud() {
    if (isChecking) return;
    if (typeof fetch === 'undefined') return;
    isChecking = true;

    try {
      const endpoint = `${SUPABASE_URL}/rest/v1/site_settings?id=eq.1&select=*`;
      const res = await fetch(endpoint, {
        method: 'GET',
        headers: {
          'apikey': SUPABASE_KEY,
          'Authorization': `Bearer ${SUPABASE_KEY}`
        },
        cache: 'no-cache'
      });

      if (res.ok) {
        const rows = await res.json();
        if (Array.isArray(rows) && rows.length > 0) {
          const status = parseCloudStatus(rows[0]);

          if (!status.isOnline) {
            // WEBSITE ĐANG TẮT
            localStorage.setItem('olion_site_online', 'false');
            localStorage.setItem('olion_maintenance_info', JSON.stringify(status));
            showMaintenanceOverlay(status);

            // Bật kiểm tra liên tục mỗi 3 giây để tự mở lại khi Admin bật
            if (!pollInterval) {
              pollInterval = setInterval(checkSiteStatusFromCloud, 3000);
            }
          } else {
            // WEBSITE ĐANG BẬT BÌNH THƯỜNG
            localStorage.setItem('olion_site_online', 'true');
            hideMaintenanceOverlay();

            if (pollInterval) {
              clearInterval(pollInterval);
              pollInterval = null;
            }
          }
        }
      }
    } catch (err) {
      console.warn('⚠️ [Gatekeeper] Lỗi kiểm tra trạng thái Cloud:', err);
    } finally {
      isChecking = false;
    }
  }

  // Kích hoạt kiểm tra ngay khi load
  checkSiteStatusFromCloud();

  // Kiểm tra định kỳ mỗi 20 giây khi đang Online
  setInterval(() => {
    if (!pollInterval) {
      checkSiteStatusFromCloud();
    }
  }, 20000);

  // 10. Tức thời liên tab (BroadcastChannel & Storage Event)
  try {
    if (typeof BroadcastChannel !== 'undefined') {
      const bc = new BroadcastChannel('olion_site_status_channel');
      bc.onmessage = (e) => {
        if (e.data && typeof e.data.is_online === 'boolean') {
          if (!e.data.is_online) {
            localStorage.setItem('olion_site_online', 'false');
            showMaintenanceOverlay(e.data);
            if (!pollInterval) pollInterval = setInterval(checkSiteStatusFromCloud, 3000);
          } else {
            localStorage.setItem('olion_site_online', 'true');
            hideMaintenanceOverlay();
            if (pollInterval) { clearInterval(pollInterval); pollInterval = null; }
          }
        }
      };
    }
  } catch (e) {}

  window.addEventListener('storage', (e) => {
    if (e.key === 'olion_site_online') {
      if (e.newValue === 'false') {
        showMaintenanceOverlay();
      } else {
        hideMaintenanceOverlay();
      }
    }
  });

  // Export API
  window.OlionGatekeeper = {
    checkStatus: checkSiteStatusFromCloud,
    showMaintenance: (info) => showMaintenanceOverlay(info),
    hideMaintenance: hideMaintenanceOverlay,
    isOffline: () => localStorage.getItem('olion_site_online') === 'false'
  };

})();
