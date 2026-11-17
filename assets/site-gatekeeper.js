/**
 * OLION COFFEE - SITE GATEKEEPER & ACCESS CONTROL SHIELD (KILL-SWITCH)
 * Giám sát và điều khiển trạng thái bật/tắt toàn bộ website olioncoffee.app
 * Khi Website TẮT: Khách hàng vào bất kỳ đường link nào đều bị chặn và hiển thị màn hình bảo trì sang trọng.
 * Khi Website BẬT: Hệ thống tự động mở lại ngay lập tức mà không cần người dùng thao tác.
 */

(function () {
  'use strict';

  // 1. Tuyệt đối không chặn trang Quản trị Admin
  const path = window.location.pathname.toLowerCase();
  if (path.includes('admin') || path.endsWith('/admin.html')) {
    return;
  }

  // 2. Cấu hình mặc định Supabase & Hotline Olion Coffee
  const SUPABASE_URL = "https://xwbrbesgnwcngzohprxt.supabase.co";
  const SUPABASE_KEY = "sb_publishable_vWuV07_xPU0wNftK0lpnFQ_oA9XHPLS";
  const DEFAULT_TITLE = "Olion Coffee Tạm Đóng Cửa Để Nâng Cấp Dịch Vụ";
  const DEFAULT_MSG = "Hệ thống website đang tạm ngưng phục vụ để bảo trì & nâng cấp trải nghiệm tốt nhất cho quý khách. Rất mong quý khách thông cảm và hẹn sớm gặp lại!";
  const DEFAULT_TIME = "Dự kiến mở lại: Sớm nhất";
  const DEFAULT_HOTLINE = "0783 657 587";
  const DEFAULT_ZALO = "https://zalo.me/0783657587";
  const DEFAULT_ADDRESS = "80/64a Dương Quảng Hàm, P. An Nhơn, Gò Vấp, TP.HCM";

  // 3. Admin Bypass Check (Chế độ xem trước dành riêng cho Quản Trị Viên)
  const urlParams = new URLSearchParams(window.location.search);
  const isAdminBypass = urlParams.get('admin_bypass') === '1' || sessionStorage.getItem('olion_admin_bypass') === 'true';
  if (isAdminBypass) {
    sessionStorage.setItem('olion_admin_bypass', 'true');
    console.log('🛡️ [Gatekeeper] Admin Bypass Active: Bạn đang duyệt web ở chế độ xem trước của Quản Trị Viên.');
    // Thêm banner cảnh báo nhỏ trên cùng
    window.addEventListener('DOMContentLoaded', () => {
      const banner = document.createElement('div');
      banner.id = 'olionAdminPreviewBanner';
      banner.innerHTML = `
        <div style="position:fixed;top:0;left:0;right:0;z-index:9999999;background:linear-gradient(90deg,#991b1b,#b91c1c);color:#fff;padding:8px 16px;font-size:12.5px;font-family:sans-serif;display:flex;justify-content:space-between;align-items:center;box-shadow:0 2px 10px rgba(0,0,0,0.5);">
          <span>⚠️ <strong>CHẾ ĐỘ XEM TRƯỚC (QUẢN TRỊ VIÊN):</strong> Website hiện đang TẮT đối với khách hàng công cộng.</span>
          <a href="admin.html" style="background:#fff;color:#991b1b;padding:4px 10px;border-radius:4px;text-decoration:none;font-weight:700;font-size:11.5px;">Vào Admin Bật Web ↗</a>
        </div>
      `;
      document.body.prepend(banner);
      document.body.style.paddingTop = '38px';
    });
    return;
  }

  // 4. CSS Chặn & Màn Hình Bảo Trì Sang Trọng (Luxury Coffee Theme)
  const INJECTED_CSS = `
    html.olion-site-offline body > *:not(#olionMaintenanceOverlay) {
      display: none !important;
    }
    html.olion-site-offline {
      overflow: hidden !important;
      height: 100% !important;
    }
    #olionMaintenanceOverlay {
      position: fixed !important;
      inset: 0 !important;
      width: 100vw !important;
      height: 100vh !important;
      z-index: 2147483647 !important;
      background: radial-gradient(circle at 50% 15%, #2c160c 0%, #160a04 55%, #080301 100%) !important;
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
      max-width: 560px;
      width: 100%;
      background: rgba(30, 16, 9, 0.85);
      border: 1px solid rgba(229, 154, 85, 0.35);
      border-radius: 20px;
      padding: 36px 28px;
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.85), 0 0 45px rgba(229, 154, 85, 0.15);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      box-sizing: border-box;
      position: relative;
    }
    .olion-maint-logo {
      width: 110px;
      height: auto;
      margin-bottom: 20px;
      filter: drop-shadow(0 4px 12px rgba(229, 154, 85, 0.3));
    }
    .olion-maint-badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: rgba(231, 76, 60, 0.15);
      border: 1px solid rgba(231, 76, 60, 0.45);
      color: #ff7675;
      padding: 6px 14px;
      border-radius: 999px;
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      margin-bottom: 18px;
    }
    .olion-pulse-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #e74c3c;
      box-shadow: 0 0 10px #e74c3c;
      animation: olionPulse 1.8s infinite;
    }
    @keyframes olionPulse {
      0% { transform: scale(0.9); opacity: 0.8; }
      50% { transform: scale(1.3); opacity: 1; }
      100% { transform: scale(0.9); opacity: 0.8; }
    }
    .olion-maint-title {
      font-family: "Cormorant Garamond", Georgia, "Times New Roman", serif;
      font-size: 26px;
      line-height: 1.3;
      color: #ffffff;
      margin: 0 0 14px 0;
      font-weight: 700;
      text-shadow: 0 2px 8px rgba(0,0,0,0.6);
    }
    .olion-maint-desc {
      font-size: 14.5px;
      line-height: 1.6;
      color: #d1c2b4;
      margin: 0 0 22px 0;
    }
    .olion-maint-box {
      background: rgba(0, 0, 0, 0.35);
      border: 1px dashed rgba(229, 154, 85, 0.3);
      border-radius: 12px;
      padding: 14px 18px;
      margin-bottom: 22px;
      font-size: 13.5px;
      color: #e59a55;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }
    .olion-maint-actions {
      display: flex;
      gap: 12px;
      justify-content: center;
      flex-wrap: wrap;
      margin-bottom: 20px;
    }
    .olion-maint-btn-primary {
      background: linear-gradient(135deg, #e59a55, #c5823f);
      color: #120904;
      text-decoration: none;
      font-weight: 700;
      font-size: 14px;
      padding: 11px 20px;
      border-radius: 10px;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 4px 15px rgba(229, 154, 85, 0.3);
      transition: transform 0.2s, filter 0.2s;
    }
    .olion-maint-btn-primary:hover {
      transform: translateY(-2px);
      filter: brightness(1.08);
    }
    .olion-maint-btn-secondary {
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(229, 154, 85, 0.35);
      color: #f5efe6;
      text-decoration: none;
      font-weight: 600;
      font-size: 14px;
      padding: 11px 18px;
      border-radius: 10px;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: background 0.2s;
    }
    .olion-maint-btn-secondary:hover {
      background: rgba(229, 154, 85, 0.15);
    }
    .olion-maint-auto-reopen {
      font-size: 12px;
      color: #a38f7d;
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }
    .olion-spinner {
      width: 14px;
      height: 14px;
      border: 2px solid rgba(229, 154, 85, 0.25);
      border-top-color: #e59a55;
      border-radius: 50%;
      animation: olionSpin 1s linear infinite;
    }
    @keyframes olionSpin {
      to { transform: rotate(360deg); }
    }
    .olion-admin-link {
      margin-top: 18px;
      font-size: 11.5px;
      color: rgba(255, 255, 255, 0.3);
      text-decoration: none;
      transition: color 0.2s;
    }
    .olion-admin-link:hover {
      color: #e59a55;
    }
  `;

  // Thêm style vào head ngay lập tức
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

  // Khởi tạo thông tin bảo trì từ cache
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
        window.addEventListener('DOMContentLoaded', () => document.body.appendChild(overlay));
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
      }, 400);
    }
  }

  // Nếu ngay từ đầu cache báo offline, render luôn
  if (initialOffline) {
    if (document.body) {
      showMaintenanceOverlay(cachedInfo);
    } else {
      window.addEventListener('DOMContentLoaded', () => showMaintenanceOverlay(cachedInfo));
    }
  }

  // 8. Trích xuất trạng thái Website từ Supabase Cloud Record
  function parseCloudStatus(data) {
    if (!data) return { isOnline: true };

    let isOnline = true;
    let title = DEFAULT_TITLE;
    let message = DEFAULT_MSG;
    let expected_time = DEFAULT_TIME;
    let hotline = DEFAULT_HOTLINE;

    // A. Kiểm tra cột riêng `is_site_online` (nếu đã chạy migration)
    if (typeof data.is_site_online === 'boolean') {
      isOnline = data.is_site_online;
    } else if (typeof data.is_site_online === 'string') {
      isOnline = data.is_site_online === 'true';
    }

    // B. Kiểm tra fallback trong `notification_text` dạng <!--SITE_STATUS:{...}-->
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

    return {
      isOnline,
      title,
      message,
      expected_time,
      hotline
    };
  }

  // 9. Đồng bộ trạng thái Cloud siêu nhanh qua REST API
  let isChecking = false;
  let pollInterval = null;

  async function checkSiteStatusFromCloud() {
    if (isChecking) return;
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

            // Bật kiểm tra liên tục mỗi 3.5 giây để tự động mở lại ngay khi Admin BẬT web
            if (!pollInterval) {
              pollInterval = setInterval(checkSiteStatusFromCloud, 3500);
            }
          } else {
            // WEBSITE ĐANG BẬT BÌNH THƯỜNG
            const wasOffline = localStorage.getItem('olion_site_online') === 'false';
            localStorage.setItem('olion_site_online', 'true');
            hideMaintenanceOverlay();

            if (pollInterval) {
              clearInterval(pollInterval);
              pollInterval = null;
            }

            // Nếu vừa chuyển từ Offline sang Online, tải lại tài nguyên nếu cần
            if (wasOffline) {
              console.log('🎉 [Gatekeeper] Olion Coffee đã mở cửa trở lại!');
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

  // Kiểm tra định kỳ nhẹ nhàng mỗi 25 giây khi đang online
  setInterval(() => {
    if (!pollInterval) {
      checkSiteStatusFromCloud();
    }
  }, 25000);

  // Lắng nghe thay đổi từ tab khác (qua Storage Event)
  window.addEventListener('storage', (e) => {
    if (e.key === 'olion_site_online') {
      if (e.newValue === 'false') {
        showMaintenanceOverlay();
      } else {
        hideMaintenanceOverlay();
      }
    }
  });

  // Export API phục vụ test hoặc admin preview
  window.OlionGatekeeper = {
    checkStatus: checkSiteStatusFromCloud,
    showMaintenance: () => showMaintenanceOverlay(),
    hideMaintenance: hideMaintenanceOverlay,
    isOffline: () => localStorage.getItem('olion_site_online') === 'false'
  };

})();
