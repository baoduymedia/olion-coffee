/**
 * TEST SUITE: WEBSITE STATUS & MAINTENANCE (KILL-SWITCH) - ENHANCED
 * Kiểm thử tính năng Bật/Tắt Website trên toàn bộ hệ thống Olion Coffee
 */

const fs = require('fs');
const path = require('path');
const { JSDOM } = require('jsdom');

async function runTests() {
  console.log('🧪 BẮT ĐẦU KIỂM THỬ TÍNH NĂNG TẮT/BẬT WEBSITE (KILL-SWITCH)...\n');

  let passed = 0;
  let failed = 0;

  function assert(condition, message) {
    if (condition) {
      console.log(`  ✅ PASS: ${message}`);
      passed++;
    } else {
      console.error(`  ❌ FAIL: ${message}`);
      failed++;
    }
  }

  // TEST 1: Kiểm tra chèn script gatekeeper vào các file HTML public
  console.log('--- TEST 1: Kiểm tra sự hiện diện của Site Gatekeeper trên các trang public ---');
  const publicPages = [
    'index.html',
    'news.html',
    'booking.html',
    'table-qr.html',
    'cuoi-ky.html',
    'bao-cao-cuoi-ky.html',
    'campaign-report.html',
    'report.html',
    'ws2010.html'
  ];

  publicPages.forEach(file => {
    const filePath = path.join(__dirname, file);
    if (fs.existsSync(filePath)) {
      const content = fs.readFileSync(filePath, 'utf-8');
      assert(
        content.includes('assets/site-gatekeeper.js'),
        `${file} đã được bảo vệ bởi assets/site-gatekeeper.js`
      );
    }
  });

  // TEST 2: Kiểm tra trang Admin (admin.html)
  console.log('\n--- TEST 2: Kiểm tra cấu trúc Admin (admin.html) ---');
  const adminHtml = fs.readFileSync(path.join(__dirname, 'admin.html'), 'utf-8');
  assert(
    !adminHtml.includes('<script src="assets/site-gatekeeper.js"></script>'),
    'admin.html không bị Gatekeeper chặn'
  );
  assert(
    adminHtml.includes('id="heroSiteStatusCard"'),
    'admin.html có HERO CONTROL CARD to rõ ràng ngay đầu Tab Tổng Quan (Overview)'
  );
  assert(
    adminHtml.includes('id="heroToggleActionBtn"'),
    'Hero Card có nút bấm to 1 chạm [TẮT WEBSITE NGAY] / [BẬT WEBSITE NGAY]'
  );
  assert(
    adminHtml.includes('id="siteStatusPill"'),
    'admin.html có Quick Toggle trạng thái Website trên Desktop Topbar'
  );
  assert(
    adminHtml.includes('id="mSiteStatusToggle"'),
    'admin.html có Quick Toggle trạng thái Website trên Mobile Topbar'
  );
  assert(
    adminHtml.includes('id="siteOfflineAdminBanner"'),
    'admin.html có Banner cảnh báo khẩn cấp khi Website Đang Tắt'
  );
  assert(
    adminHtml.includes('id="siteOnlineToggleInput"'),
    'admin.html có Switch iOS Toggle lớn trong Tab Cài Đặt (Customizer)'
  );
  assert(
    adminHtml.includes('id="siteStatusConfirmModal"'),
    'admin.html có Modal xác nhận an toàn trước khi tắt website'
  );

  // TEST 3: Giả lập Client khi Website Đang BẬT (Online = true)
  console.log('\n--- TEST 3: Giả lập Client khi Website Đang BẬT (Online = true) ---');
  {
    const indexHtml = fs.readFileSync(path.join(__dirname, 'index.html'), 'utf-8');
    const dom = new JSDOM(indexHtml, {
      url: 'https://www.olioncoffee.app/',
      runScripts: 'outside-only'
    });
    const { window } = dom;
    window.localStorage.setItem('olion_site_online', 'true');

    const gatekeeperCode = fs.readFileSync(path.join(__dirname, 'assets/site-gatekeeper.js'), 'utf-8');
    window.eval(gatekeeperCode);

    assert(
      !window.document.documentElement.classList.contains('olion-site-offline'),
      'Thẻ <html> không có class olion-site-offline khi web Online'
    );
    assert(
      !window.document.getElementById('olionMaintenanceOverlay'),
      'Màn hình bảo trì #olionMaintenanceOverlay không hiển thị khi web Online'
    );
  }

  // TEST 4: Giả lập Client khi Website ĐÃ TẮT (Offline = false)
  console.log('\n--- TEST 4: Giả lập Client khi Website ĐÃ TẮT (Offline = false) ---');
  {
    const bookingHtml = fs.readFileSync(path.join(__dirname, 'booking.html'), 'utf-8');
    const dom = new JSDOM(bookingHtml, {
      url: 'https://www.olioncoffee.app/booking',
      runScripts: 'outside-only'
    });
    const { window } = dom;
    window.localStorage.setItem('olion_site_online', 'false');
    window.localStorage.setItem('olion_maintenance_info', JSON.stringify({
      title: 'Quán Đang Nâng Cấp Hệ Thống',
      message: 'Xin quý khách quay lại sau!',
      expected_time: '18:00 chiều nay',
      hotline: '0783 657 587'
    }));

    const gatekeeperCode = fs.readFileSync(path.join(__dirname, 'assets/site-gatekeeper.js'), 'utf-8');
    window.eval(gatekeeperCode);

    assert(
      window.document.documentElement.classList.contains('olion-site-offline'),
      'Thẻ <html> lập tức nhận class olion-site-offline để chặn toàn bộ trang'
    );
    const overlay = window.document.getElementById('olionMaintenanceOverlay');
    assert(
      Boolean(overlay),
      'Màn hình bảo trì #olionMaintenanceOverlay lập tức được kích hoạt che kín màn hình'
    );
    if (overlay) {
      assert(
        overlay.innerHTML.includes('Quán Đang Nâng Cấp Hệ Thống'),
        'Màn hình bảo trì hiển thị đúng tiêu đề tùy biến từ Admin'
      );
      assert(
        overlay.innerHTML.includes('Xin quý khách quay lại sau!'),
        'Màn hình bảo trì hiển thị đúng lời nhắn gửi khách hàng'
      );
      assert(
        overlay.innerHTML.includes('0783 657 587'),
        'Màn hình bảo trì hiển thị số Hotline để khách liên hệ khẩn cấp'
      );
      assert(
        overlay.innerHTML.includes('admin.html'),
        'Có lối dẫn an toàn về trang Admin cho quản trị viên'
      );
    }
  }

  // TEST 5: Kiểm tra Modal Confirm hoạt động đúng (thêm class .open)
  console.log('\n--- TEST 5: Kiểm tra Modal Xác Nhận & Logic Mở/Đóng trong Admin ---');
  {
    const dom = new JSDOM(adminHtml, {
      url: 'https://www.olioncoffee.app/admin.html',
      runScripts: 'outside-only'
    });
    const { window } = dom;

    // Load supabaseClient.js code first
    const supabaseClientCode = fs.readFileSync(path.join(__dirname, 'supabaseClient.js'), 'utf-8');
    window.eval(supabaseClientCode);

    // Mock global showToast & Chart
    window.showToast = () => {};
    window.Chart = function() { return { destroy: () => {}, update: () => {} }; };

    // Eval admin scripts safely
    const scripts = adminHtml.match(/<script(?:\s+[^>]*)?>([\s\S]*?)<\/script>/gi) || [];
    scripts.forEach(s => {
      const code = s.replace(/<\/?script(?:\s+[^>]*)?>/gi, "");
      if (code.includes("openSiteConfirmModal")) {
        try { window.eval(code); } catch(e) {}
      }
    });

    const modal = window.document.getElementById('siteStatusConfirmModal');
    assert(Boolean(modal), 'Tìm thấy #siteStatusConfirmModal trong DOM');

    // Gọi hàm mở modal
    window.openSiteConfirmModal(false);
    assert(
      modal.classList.contains('open') || modal.style.display === 'flex',
      'Modal được hiển thị (display: flex / class open) khi gọi openSiteConfirmModal(false)'
    );

    // Gọi hàm đóng modal
    window.closeSiteConfirmModal();
    assert(
      !modal.classList.contains('open'),
      'Modal được gỡ bỏ class open khi gọi closeSiteConfirmModal()'
    );
  }

  // TEST 6: Kiểm tra các hàm API trong supabaseClient.js
  console.log('\n--- TEST 6: Kiểm tra các hàm API trong supabaseClient.js ---');
  const supabaseCode = fs.readFileSync(path.join(__dirname, 'supabaseClient.js'), 'utf-8');
  assert(
    supabaseCode.includes('fetchSiteStatusFromCloud'),
    'supabaseClient.js có hàm fetchSiteStatusFromCloud()'
  );
  assert(
    supabaseCode.includes('updateSiteStatusToCloud'),
    'supabaseClient.js có hàm updateSiteStatusToCloud()'
  );
  assert(
    supabaseCode.includes('window.fetchSiteStatusFromCloud'),
    'fetchSiteStatusFromCloud được export lên window'
  );
  assert(
    supabaseCode.includes('window.updateSiteStatusToCloud'),
    'updateSiteStatusToCloud được export lên window'
  );

  console.log(`\n========================================`);
  console.log(`TỔNG KẾT KIỂM THỬ: ${passed} PASS, ${failed} FAIL`);
  console.log(`========================================\n`);

  process.exit(failed > 0 ? 1 : 0);
}

runTests().catch(err => {
  console.error('Test crashed:', err);
  process.exit(1);
});
