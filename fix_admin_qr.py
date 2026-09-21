import re

with open('admin.html', 'r') as f:
    c = f.read()

# Add html5-qrcode
c = c.replace('<script src="https://unpkg.com/lucide@latest"></script>', '<script src="https://unpkg.com/lucide@latest"></script>\n  <script src="https://unpkg.com/html5-qrcode"></script>')

# Add Tab
c = c.replace('<button class="tab-btn active" data-tab="tab-dashboard"><i data-lucide="layout-dashboard"></i> Tổng quan</button>', '<button class="tab-btn active" data-tab="tab-dashboard"><i data-lucide="layout-dashboard"></i> Tổng quan</button>\n      <button class="tab-btn" data-tab="tab-scanner"><i data-lucide="scan-line"></i> Quét E-Voucher</button>')

# Add Tab Content
scanner_tab = """
    <!-- ========================================== -->
    <!-- TAB: SCANNER (QR E-VOUCHER)                -->
    <!-- ========================================== -->
    <div id="tab-scanner" class="tab-content" style="display: none;">
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
    </div>
"""
c = c.replace('<!-- TAB: DASHBOARD -->', scanner_tab + '\n    <!-- TAB: DASHBOARD -->')

# Add JS Logic
scanner_js = """
    // ==========================================
    // QR SCANNER LOGIC
    // ==========================================
    let html5QrcodeScanner = null;
    let currentScannedId = null;

    function onScanSuccess(decodedText, decodedResult) {
      // decodedText will be like 'olion-voucher:123' or 'olion-voucher:uuid'
      if (decodedText.startsWith('olion-voucher:')) {
        const id = decodedText.split(':')[1];
        if (id !== currentScannedId) {
          currentScannedId = id;
          html5QrcodeScanner.pause(true); // Pause scanning
          processVoucher(id);
        }
      }
    }

    async function processVoucher(id) {
      document.getElementById('qr-result').style.display = 'none';
      document.getElementById('qr-error').style.display = 'none';
      
      const res = await getSpinDetails(id);
      if (res.error || !res.data) {
        document.getElementById('qr-error').style.display = 'block';
        document.getElementById('qr-error-msg').textContent = 'Không tìm thấy thông tin Voucher này!';
        setTimeout(() => html5QrcodeScanner.resume(), 3000);
        return;
      }
      
      const v = res.data;
      if (v.status === 'used') {
        document.getElementById('qr-error').style.display = 'block';
        document.getElementById('qr-error-msg').textContent = 'Voucher này đã được sử dụng vào lúc: ' + new Date(v.updated_at || v.created_at).toLocaleString('vi-VN');
        setTimeout(() => html5QrcodeScanner.resume(), 3000);
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

    document.querySelectorAll('.tab-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        if (btn.dataset.tab === 'tab-scanner') {
          if (!html5QrcodeScanner) {
            html5QrcodeScanner = new Html5QrcodeScanner("qr-reader", { fps: 10, qrbox: {width: 250, height: 250} }, false);
            html5QrcodeScanner.render(onScanSuccess);
          }
        }
      });
    });
"""
c = c.replace('// Dashboard setup', scanner_js + '\n    // Dashboard setup')

with open('admin.html', 'w') as f:
    f.write(c)
