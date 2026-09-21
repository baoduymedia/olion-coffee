import re

with open('admin.html', 'r') as f:
    c = f.read()

# 1. Add nav-item for Scanner
nav_scanner = """        <div class="nav-item" data-tab="scanner">
          <span class="nav-icon">📸</span>
          <span class="nav-text">Quét mã E-Voucher</span>
        </div>"""
c = c.replace('<div class="nav-item" data-tab="minigame">', nav_scanner + '\n        <div class="nav-item" data-tab="minigame">')

# 2. Add tab content for Scanner
content_scanner = """
        <!-- ==================== TAB: QUÉT E-VOUCHER ==================== -->
        <section class="tab-content" id="tab-scanner">
          <div class="card" style="max-width: 600px; margin: 0 auto; text-align: center;">
            <div class="card-header" style="justify-content: center; margin-bottom: 20px;">
              <h3 class="card-title">📸 Quét Mã E-Voucher QR</h3>
            </div>
            
            <div id="qr-reader" style="width: 100%; border-radius: 12px; overflow: hidden; border: 2px solid var(--border); margin-bottom: 20px; background: #000;"></div>
            
            <div id="qr-result" style="display: none; background: rgba(46, 204, 113, 0.1); border: 1px solid rgba(46, 204, 113, 0.3); padding: 20px; border-radius: 12px; margin-top: 20px;">
              <h4 style="color: var(--success); font-size: 18px; margin-bottom: 10px;">✅ Hợp Lệ!</h4>
              <p id="qr-prize-name" style="font-size: 20px; font-weight: bold; color: var(--text); margin-bottom: 5px;"></p>
              <p id="qr-customer" style="color: var(--text-muted); font-size: 14px; margin-bottom: 15px;"></p>
              <button id="btnMarkUsed" class="btn-primary" style="width: 100%; justify-content: center; padding: 12px;">Đánh dấu Đã Sử Dụng</button>
            </div>
            
            <div id="qr-error" style="display: none; background: rgba(231, 76, 60, 0.1); border: 1px solid rgba(231, 76, 60, 0.3); padding: 15px; border-radius: 12px; margin-top: 20px;">
              <p style="color: var(--danger); font-weight: 500; margin: 0;" id="qr-error-msg">Mã không hợp lệ hoặc đã được sử dụng.</p>
            </div>
          </div>
        </section>
"""
c = c.replace('<section class="tab-content" id="tab-minigame">', content_scanner + '\n        <section class="tab-content" id="tab-minigame">')

# 3. Add title translation for scanner
c = c.replace("minigame: '🎡 Cấu hình Vòng Quay May Mắn',", "scanner: '📸 Quét Mã E-Voucher QR',\n      minigame: '🎡 Cấu hình Vòng Quay May Mắn',")

# 4. Attach JS logic properly
js_logic = """
    // ==========================================
    // QR SCANNER LOGIC
    // ==========================================
    let html5QrcodeScanner = null;
    let currentScannedId = null;

    function onScanSuccess(decodedText, decodedResult) {
      if (decodedText.startsWith('olion-voucher:')) {
        const id = decodedText.split(':')[1];
        if (id !== currentScannedId) {
          currentScannedId = id;
          html5QrcodeScanner.pause(true); // Pause scanning
          processVoucher(id);
        }
      } else {
        showToast('Mã QR không thuộc hệ thống Olion Coffee!');
      }
    }

    async function processVoucher(id) {
      document.getElementById('qr-result').style.display = 'none';
      document.getElementById('qr-error').style.display = 'none';
      
      const res = await getSpinDetails(id);
      if (res.error || !res.data) {
        document.getElementById('qr-error').style.display = 'block';
        document.getElementById('qr-error-msg').textContent = 'Không tìm thấy thông tin Voucher này trên máy chủ!';
        setTimeout(() => { html5QrcodeScanner.resume(); currentScannedId = null; }, 3000);
        return;
      }
      
      const v = res.data;
      if (v.status === 'used') {
        document.getElementById('qr-error').style.display = 'block';
        document.getElementById('qr-error-msg').textContent = 'Voucher này đã được sử dụng vào lúc: ' + new Date(v.updated_at || v.created_at).toLocaleString('vi-VN');
        setTimeout(() => { html5QrcodeScanner.resume(); currentScannedId = null; }, 3000);
        return;
      }
      
      // Show success
      document.getElementById('qr-result').style.display = 'block';
      document.getElementById('qr-prize-name').textContent = `🎁 ${v.prize_name} (Mã: ${v.promo_code})`;
      document.getElementById('qr-customer').textContent = `👤 Khách: ${v.customer_name} - 📞 ${v.customer_phone}`;
      
      document.getElementById('btnMarkUsed').onclick = async () => {
        document.getElementById('btnMarkUsed').textContent = 'Đang xử lý...';
        await markSpinAsUsed(id);
        document.getElementById('btnMarkUsed').textContent = 'Đánh dấu Đã Sử Dụng';
        document.getElementById('qr-result').style.display = 'none';
        showToast('✅ Đã thu hồi E-Voucher thành công!');
        html5QrcodeScanner.resume();
        currentScannedId = null;
      };
    }

    // Bind scanner to tab switch
    const oldSwitchTab = switchTab;
    switchTab = function(tabKey) {
      oldSwitchTab(tabKey);
      if (tabKey === 'scanner') {
        if (!html5QrcodeScanner) {
          html5QrcodeScanner = new Html5QrcodeScanner("qr-reader", { fps: 10, qrbox: {width: 250, height: 250} }, false);
          html5QrcodeScanner.render(onScanSuccess);
        }
      }
    };
"""
c = c.replace('// ---- TAB SWITCHING ----', js_logic + '\n    // ---- TAB SWITCHING ----')

# 5. Remove the old junk from my previous failed attempt
# I'll just clean up the `c.replace('// Dashboard setup', scanner_js + '\n    // Dashboard setup')` which might have actually inserted something?
# Wait! Let's check if `let html5QrcodeScanner = null;` exists in admin.html right now!
