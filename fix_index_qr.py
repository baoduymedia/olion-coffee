import re

with open('index.html', 'r') as f:
    c = f.read()

# 1. Add qrcode.js CDN to head
c = c.replace('<!-- Include Supabase SDK -->', '<!-- Include Supabase SDK & QRCode -->\n  <script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>')

# 2. Modify wheelResultArea to include QR div
old_result_area = """              <div class="prize-code-box">
                Mã: <strong id="wheelPromoCode">OLION15</strong>
              </div>
              <button type="button" class="btn btn-primary" onclick="closeWheelModal()" style="width: 100%; justify-content: center; margin-top: 15px;">Tuyệt vời!</button>"""

new_result_area = """              <div class="prize-code-box">
                Mã: <strong id="wheelPromoCode">OLION15</strong>
              </div>
              
              <div id="qrCodeContainer" style="margin: 20px auto 10px; display: flex; justify-content: center; background: #fff; padding: 10px; border-radius: 8px; width: fit-content;"></div>
              <p style="font-size: 12.5px; color: var(--text-muted); text-align: center; margin-bottom: 20px;">Đưa mã QR này cho nhân viên khi thanh toán</p>
              
              <button type="button" class="btn btn-primary" onclick="closeWheelModal()" style="width: 100%; justify-content: center;">Đóng</button>"""
c = c.replace(old_result_area, new_result_area)

# 3. Modify spin success logic
old_spin_logic = """              // Lưu lên Supabase Cloud Database (kèm Device ID)
              if (typeof recordLuckySpinToCloud === 'function') {
                recordLuckySpinToCloud({
                  customer_name: name || 'Khách quay minigame',
                  customer_phone: phone,
                  prize_name: prize.text,
                  promo_code: prize.code
                });
              }"""
new_spin_logic = """              // Lưu lên Supabase Cloud Database (kèm Device ID)
              if (typeof recordLuckySpinToCloud === 'function') {
                const insertedData = await recordLuckySpinToCloud({
                  customer_name: name || 'Khách quay minigame',
                  customer_phone: phone,
                  prize_name: prize.text,
                  promo_code: prize.code
                });
                
                // Generate QR Code
                const qrContainer = document.getElementById('qrCodeContainer');
                qrContainer.innerHTML = '';
                if (insertedData && insertedData.id) {
                  new QRCode(qrContainer, {
                    text: 'olion-voucher:' + insertedData.id,
                    width: 150,
                    height: 150,
                    colorDark : "#190D07",
                    colorLight : "#ffffff",
                    correctLevel : QRCode.CorrectLevel.H
                  });
                }
              }"""
c = c.replace(old_spin_logic, new_spin_logic)

with open('index.html', 'w') as f:
    f.write(c)
