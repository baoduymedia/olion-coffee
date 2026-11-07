import os
import re

def main():
    with open('campaign-report.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add CSS before </style>
    css_target = '  </style>'
    new_css = '''
    /* ========================================================
       PROOFS & ADS MANAGER EVIDENCE CARDS (VÒNG 0, 1, 2, 3)
       ======================================================== */
    .proof-showcase-box {
      background: linear-gradient(145deg, rgba(28, 20, 14, 0.95) 0%, rgba(18, 13, 9, 0.98) 100%);
      border: 1.5px solid var(--border-brass);
      border-radius: var(--radius-md);
      padding: 22px 24px;
      margin: 26px 0;
      box-shadow: var(--shadow-wood);
      position: relative;
    }
    .proof-showcase-box.matcha-theme {
      border-color: rgba(46, 204, 113, 0.4);
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5), 0 0 20px rgba(46, 204, 113, 0.08);
    }
    .proof-showcase-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 12px;
      margin-bottom: 20px;
      padding-bottom: 14px;
      border-bottom: 1px solid rgba(212, 175, 55, 0.2);
    }
    .proof-showcase-header.matcha-theme {
      border-bottom-color: rgba(46, 204, 113, 0.25);
    }
    .proof-header-left {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }
    .proof-header-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(212, 175, 55, 0.15);
      border: 1px solid var(--accent-gold);
      color: var(--accent-gold);
      font-size: 11.5px;
      font-weight: 800;
      letter-spacing: 0.8px;
      text-transform: uppercase;
      padding: 4px 10px;
      border-radius: 999px;
    }
    .proof-header-badge.matcha {
      background: rgba(46, 204, 113, 0.15);
      border-color: var(--matcha-green);
      color: var(--matcha-bright);
    }
    .proof-header-title {
      font-size: 17.5px;
      font-weight: 700;
      color: var(--crema);
      margin: 0;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .proof-header-hint {
      font-size: 12.5px;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      gap: 5px;
    }
    .proof-grid-3cols {
      display: grid;
      grid-template-columns: 1fr;
      gap: 20px;
    }
    @media (min-width: 860px) {
      .proof-grid-3cols {
        grid-template-columns: repeat(3, 1fr);
      }
    }
    .proof-card {
      background: rgba(14, 10, 7, 0.85);
      border: 1.2px solid rgba(212, 175, 55, 0.25);
      border-radius: var(--radius-sm);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
      cursor: pointer;
      position: relative;
    }
    .proof-card:hover {
      transform: translateY(-5px);
      border-color: var(--accent-gold);
      box-shadow: 0 14px 28px rgba(0,0,0,0.7), 0 0 15px rgba(212, 175, 55, 0.25);
    }
    .proof-card.matcha-theme:hover {
      border-color: var(--matcha-bright);
      box-shadow: 0 14px 28px rgba(0,0,0,0.7), 0 0 15px rgba(46, 204, 113, 0.3);
    }
    .proof-card-preview {
      position: relative;
      width: 100%;
      background: #000;
      overflow: hidden;
      aspect-ratio: 16 / 11;
    }
    .proof-card-img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: top center;
      display: block;
      transition: transform 0.4s ease;
    }
    .proof-card:hover .proof-card-img {
      transform: scale(1.05);
    }
    .proof-card-zoom-badge {
      position: absolute;
      bottom: 8px;
      right: 8px;
      background: rgba(0, 0, 0, 0.8);
      backdrop-filter: blur(4px);
      border: 1px solid rgba(255, 255, 255, 0.25);
      color: #fff;
      font-size: 11px;
      font-weight: 600;
      padding: 4px 8px;
      border-radius: 4px;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      pointer-events: none;
    }
    .proof-card-meta {
      padding: 14px 16px;
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .proof-card-layer-tag {
      font-size: 11px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.8px;
      color: var(--accent-gold);
      margin-bottom: 4px;
    }
    .proof-card-layer-tag.matcha {
      color: var(--matcha-bright);
    }
    .proof-card-title {
      font-size: 15px;
      font-weight: 700;
      color: var(--crema);
      margin-bottom: 8px;
      line-height: 1.35;
    }
    .proof-card-desc {
      font-size: 12.5px;
      color: var(--text-muted);
      line-height: 1.45;
      margin-bottom: 10px;
    }
    .proof-card-key-list {
      list-style: none;
      padding: 0;
      margin: 0;
      font-size: 12px;
      color: var(--warm-gray);
      border-top: 1px dashed rgba(255,255,255,0.1);
      padding-top: 8px;
    }
    .proof-card-key-list li {
      margin-bottom: 4px;
      display: flex;
      align-items: baseline;
      gap: 6px;
    }
    .proof-single-showcase-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 22px;
      align-items: center;
    }
    @media (min-width: 900px) {
      .proof-single-showcase-grid {
        grid-template-columns: 1.3fr 1fr;
      }
    }
    .proof-single-media {
      position: relative;
      border-radius: var(--radius-sm);
      overflow: hidden;
      border: 1.5px solid rgba(212, 175, 55, 0.35);
      background: #000;
      cursor: pointer;
      box-shadow: 0 12px 28px rgba(0,0,0,0.6);
      transition: all 0.35s ease;
    }
    .proof-single-media.matcha {
      border-color: rgba(46, 204, 113, 0.4);
    }
    .proof-single-media:hover {
      transform: translateY(-4px);
      border-color: var(--matcha-bright);
      box-shadow: 0 16px 36px rgba(0,0,0,0.8), 0 0 20px rgba(46, 204, 113, 0.3);
    }
    .proof-single-media img {
      width: 100%;
      height: auto;
      display: block;
      transition: transform 0.4s ease;
    }
    .proof-single-media:hover img {
      transform: scale(1.025);
    }
    .proof-param-card {
      background: rgba(14, 10, 7, 0.85);
      border: 1.2px solid rgba(212, 175, 55, 0.25);
      border-radius: var(--radius-sm);
      padding: 18px 20px;
    }
    .proof-param-card.matcha {
      border-color: rgba(46, 204, 113, 0.35);
    }
    .proof-param-row {
      display: flex;
      align-items: flex-start;
      gap: 12px;
      margin-bottom: 12px;
      padding-bottom: 12px;
      border-bottom: 1px dashed rgba(255,255,255,0.08);
    }
    .proof-param-row:last-child {
      margin-bottom: 0;
      padding-bottom: 0;
      border-bottom: none;
    }
    .proof-badge-chip {
      font-size: 11px;
      font-weight: 800;
      padding: 3px 8px;
      border-radius: 4px;
      text-transform: uppercase;
      white-space: nowrap;
    }
    .proof-badge-chip.baseline {
      background: rgba(255,255,255,0.1);
      color: var(--warm-gray);
      border: 1px solid rgba(255,255,255,0.2);
    }
    .proof-badge-chip.optimized {
      background: rgba(46, 204, 113, 0.2);
      color: var(--matcha-bright);
      border: 1px solid var(--matcha-green);
    }
''' + '\n  </style>'

    if '/* PROOFS & ADS MANAGER EVIDENCE CARDS' not in content:
        content = content.replace(css_target, new_css, 1)

    # 2. Insert into Section 3 (Vòng 0)
    v0_html = '''
      <!-- Bộ Ảnh Minh Chứng Thiết Lập Quảng Cáo Vòng 0 (3 Tầng Thiết Lập) -->
      <div class="proof-showcase-box">
        <div class="proof-showcase-header">
          <div class="proof-header-left">
            <span class="proof-header-badge"><i data-lucide="shield-check" style="width:13px;height:13px;"></i> MINH CHỨNG THỰC TẾ</span>
            <h3 class="proof-header-title">Thiết Lập 3 Tầng Trình Quản Lý Quảng Cáo (Vòng 0)</h3>
          </div>
          <div class="proof-header-hint"><i data-lucide="zoom-in" style="width:13px;height:13px;"></i> Nhấp vào ảnh để phóng to chi tiết</div>
        </div>

        <div class="proof-grid-3cols">
          <!-- Tầng 1: Chiến Dịch -->
          <div class="proof-card" onclick="openLightbox('assets/vong-0-tang-1-chien-dich.webp?v=20261107', 'Vòng 0 — Tầng 1: Thiết Lập Chiến Dịch (Mục Tiêu Tương Tác / Follow Trang)')">
            <div class="proof-card-preview">
              <img src="assets/vong-0-tang-1-chien-dich.webp?v=20261107" alt="Vòng 0 Tầng 1 Chiến Dịch" class="proof-card-img" />
              <div class="proof-card-zoom-badge"><i data-lucide="zoom-in" style="width:11px;height:11px;"></i> Phóng to</div>
            </div>
            <div class="proof-card-meta">
              <div>
                <div class="proof-card-layer-tag">TẦNG 1 &bull; CHIẾN DỊCH</div>
                <div class="proof-card-title">Mục Tiêu Tương Tác (Follow Trang)</div>
                <div class="proof-card-desc">Cấu hình mục tiêu chiến dịch để hệ thống tối ưu hóa lượt thích và theo dõi Fanpage Olion Coffee.</div>
              </div>
              <ul class="proof-card-key-list">
                <li><i data-lucide="check" style="width:12px;height:12px;color:var(--accent-gold);"></i> <strong>Tên:</strong> Chiến dịch tháng 11</li>
                <li><i data-lucide="check" style="width:12px;height:12px;color:var(--accent-gold);"></i> <strong>Mục tiêu:</strong> Tương tác (Lượt theo dõi Trang)</li>
                <li><i data-lucide="check" style="width:12px;height:12px;color:var(--accent-gold);"></i> <strong>KPI:</strong> Phục vụ mốc cơ sở 1.000 followers</li>
              </ul>
            </div>
          </div>

          <!-- Tầng 2: Nhóm Quảng Cáo -->
          <div class="proof-card" onclick="openLightbox('assets/vong-0-tang-2-nhom-quang-cao.webp?v=20261107', 'Vòng 0 — Tầng 2: Thiết Lập Nhóm Quảng Cáo (Đối Tượng Cốt Lõi: Cà Phê &amp; Sinh Viên)')">
            <div class="proof-card-preview">
              <img src="assets/vong-0-tang-2-nhom-quang-cao.webp?v=20261107" alt="Vòng 0 Tầng 2 Nhóm Quảng Cáo" class="proof-card-img" />
              <div class="proof-card-zoom-badge"><i data-lucide="zoom-in" style="width:11px;height:11px;"></i> Phóng to</div>
            </div>
            <div class="proof-card-meta">
              <div>
                <div class="proof-card-layer-tag">TẦNG 2 &bull; NHÓM QUẢNG CÁO</div>
                <div class="proof-card-title">Tệp Đối Tượng Cốt Lõi Baseline</div>
                <div class="proof-card-desc">Thiết lập phạm vi khu vực TP.HCM, độ tuổi 18-35 với sở thích cà phê và sinh viên trường đại học.</div>
              </div>
              <ul class="proof-card-key-list">
                <li><i data-lucide="check" style="width:12px;height:12px;color:var(--accent-gold);"></i> <strong>Vị trí &amp; Tuổi:</strong> TP.HCM &bull; 18 - 35 tuổi</li>
                <li><i data-lucide="check" style="width:12px;height:12px;color:var(--accent-gold);"></i> <strong>Sở thích:</strong> Cà phê, Sinh viên</li>
                <li><i data-lucide="check" style="width:12px;height:12px;color:var(--accent-gold);"></i> <strong>Quy mô ước tính:</strong> 641.250 người</li>
                <li><i data-lucide="check" style="width:12px;height:12px;color:var(--accent-gold);"></i> <strong>Ngân sách:</strong> 200k/ngày &times; 5 ngày = 1.000.000đ</li>
              </ul>
            </div>
          </div>

          <!-- Tầng 3: Quảng Cáo -->
          <div class="proof-card" onclick="openLightbox('assets/vong-0-tang-3-mau-quang-cao.webp?v=20261107', 'Vòng 0 — Tầng 3: Thiết Lập Mẫu Quảng Cáo A (Ảnh Đồ Uống + CTA Thích Trang)')">
            <div class="proof-card-preview">
              <img src="assets/vong-0-tang-3-mau-quang-cao.webp?v=20261107" alt="Vòng 0 Tầng 3 Mẫu Quảng Cáo" class="proof-card-img" />
              <div class="proof-card-zoom-badge"><i data-lucide="zoom-in" style="width:11px;height:11px;"></i> Phóng to</div>
            </div>
            <div class="proof-card-meta">
              <div>
                <div class="proof-card-layer-tag">TẦNG 3 &bull; QUẢNG CÁO</div>
                <div class="proof-card-title">Mẫu Quảng Cáo A (Mở Đầu Trực Diện)</div>
                <div class="proof-card-desc">Sử dụng hình ảnh thực tế Bộ Tứ Matcha Series, kèm nút CTA Thích Trang và landing page website.</div>
              </div>
              <ul class="proof-card-key-list">
                <li><i data-lucide="check" style="width:12px;height:12px;color:var(--accent-gold);"></i> <strong>Định dạng:</strong> Ảnh đơn (IMG_3978.JPG)</li>
                <li><i data-lucide="check" style="width:12px;height:12px;color:var(--accent-gold);"></i> <strong>Nút kêu gọi:</strong> Thích Trang (Follow)</li>
                <li><i data-lucide="check" style="width:12px;height:12px;color:var(--accent-gold);"></i> <strong>URL đích:</strong> https://www.olioncoffee.app/</li>
                <li><i data-lucide="check" style="width:12px;height:12px;color:var(--accent-gold);"></i> <strong>Kiểm duyệt:</strong> Đạt 3/3 tiêu chí cơ bản</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
'''

    target_v0 = '      <!-- Thanh Tiến Trình 4 Vòng Tối Ưu -->\n      <div class="round-metric-strip">'
    if 'Thiết Lập 3 Tầng Trình Quản Lý Quảng Cáo (Vòng 0)' not in content:
        content = content.replace(target_v0, v0_html + '\n' + target_v0, 1)

    # 3. Insert into Section 4 (Vòng 1)
    v1_html = '''
      <!-- Ảnh Minh Chứng Thiết Lập Vòng 1: Mở Rộng Đối Tượng -->
      <div class="proof-showcase-box matcha-theme">
        <div class="proof-showcase-header matcha-theme">
          <div class="proof-header-left">
            <span class="proof-header-badge matcha"><i data-lucide="users" style="width:13px;height:13px;"></i> MINH CHỨNG VÒNG 1</span>
            <h3 class="proof-header-title">Thiết Lập Nhóm Quảng Cáo: Mở Rộng Tệp Đối Tượng</h3>
          </div>
          <div class="proof-header-hint"><i data-lucide="zoom-in" style="width:13px;height:13px;"></i> Nhấp ảnh để xem chi tiết Ads Manager</div>
        </div>

        <div class="proof-single-showcase-grid">
          <!-- Ảnh lớn có phóng to -->
          <div class="proof-single-media matcha" onclick="openLightbox('assets/vong-1-thay-doi-doi-tuong.webp?v=20261107', 'Minh Chứng Vòng 1 — Tầng 2: Mở Rộng Thêm Sở Thích &quot;Nhân Viên Văn Phòng&quot; (Quy Mô 810.000 người)')">
            <img src="assets/vong-1-thay-doi-doi-tuong.webp?v=20261107" alt="Minh chứng thiết lập Vòng 1 Olion Coffee" />
            <div class="proof-card-zoom-badge"><i data-lucide="zoom-in" style="width:12px;height:12px;"></i> Phóng to ảnh gốc Ads Manager</div>
          </div>

          <!-- Thông số & Phân tích đối chiếu -->
          <div class="proof-param-card matcha">
            <div style="font-size:12px;font-weight:800;color:var(--matcha-bright);text-transform:uppercase;letter-spacing:0.8px;margin-bottom:6px;">
              TẦNG 2 &bull; NHÓM QUẢNG CÁO (TỐI ƯU HÓA)
            </div>
            <h4 style="font-size:16.5px;font-weight:700;color:var(--crema);margin-bottom:12px;">
              Bổ sung sở thích &quot;Nhân viên văn phòng&quot;
            </h4>

            <div class="proof-param-row">
              <span class="proof-badge-chip baseline">Vòng 0</span>
              <div style="font-size:13px;color:var(--warm-gray);">
                Sở thích: <code>Cà phê</code>, <code>Sinh viên</code><br />
                Quy mô ước tính: <strong>641.250 người</strong>
              </div>
            </div>

            <div class="proof-param-row">
              <span class="proof-badge-chip optimized">Vòng 1</span>
              <div style="font-size:13px;color:var(--crema);">
                Sở thích: <code>Cà phê</code>, <code>Sinh viên</code>, <strong class="text-matcha">+ Nhân viên văn phòng</strong><br />
                Quy mô ước tính: <strong class="text-matcha">810.000 người</strong> <span style="color:var(--matcha-bright);font-weight:700;">(+168.750 người / +26.3%)</span>
              </div>
            </div>

            <div class="proof-param-row">
              <span class="proof-badge-chip optimized">Hiệu Quả Thực Tế</span>
              <div style="font-size:12.5px;color:var(--text-muted);line-height:1.45;">
                ✓ <strong>Tiếp cận tăng:</strong> từ 37.279 &rarr; <strong class="text-matcha">38.254 người</strong><br />
                ✓ <strong>CPM giảm:</strong> từ 26.036đ &rarr; <strong class="text-matcha">25.526đ</strong><br />
                ✓ <strong>CPA tối ưu hơn:</strong> từ 11.183đ &rarr; <strong class="text-matcha">11.126đ</strong>
              </div>
            </div>
          </div>
        </div>
      </div>
'''

    target_v1 = '<div class="round-metric-strip">\n        <div class="metric-strip-card">\n          <div class="metric-strip-lbl"><i data-lucide="credit-card" style="width:14px;height:14px;color:var(--accent-gold);"></i> SỐ TIỀN ĐÃ CHI</div>'
    pos_m4 = content.find('id="muc-4"')
    pos_strip_m4 = content.find(target_v1, pos_m4)
    if pos_strip_m4 != -1 and 'Minh Chứng Vòng 1' not in content:
        content = content[:pos_strip_m4] + v1_html + '\n      ' + content[pos_strip_m4:]

    # 4. Insert into Section 5 (Vòng 2)
    v2_html = '''
      <!-- Ảnh Minh Chứng Thiết Lập Vòng 2: Kích Hoạt A/B Testing -->
      <div class="proof-showcase-box">
        <div class="proof-showcase-header">
          <div class="proof-header-left">
            <span class="proof-header-badge"><i data-lucide="git-pull-request" style="width:13px;height:13px;"></i> MINH CHỨNG VÒNG 2</span>
            <h3 class="proof-header-title">Thiết Lập Chiến Dịch: Bật Tính Năng Thử Nghiệm A/B Test</h3>
          </div>
          <div class="proof-header-hint"><i data-lucide="zoom-in" style="width:13px;height:13px;"></i> Nhấp ảnh để xem chi tiết Ads Manager</div>
        </div>

        <div class="proof-single-showcase-grid">
          <!-- Ảnh lớn có phóng to -->
          <div class="proof-single-media" onclick="openLightbox('assets/vong-2-tang-1-ab-test-config.webp?v=20261107', 'Minh Chứng Vòng 2 — Tầng 1: Kích Hoạt Thử Nghiệm A/B Test (Chia Đôi Ngân Sách, Chọn Bản Thắng Theo CPA)')">
            <img src="assets/vong-2-tang-1-ab-test-config.webp?v=20261107" alt="Minh chứng thiết lập Vòng 2 Olion Coffee" />
            <div class="proof-card-zoom-badge"><i data-lucide="zoom-in" style="width:12px;height:12px;"></i> Phóng to ảnh gốc Ads Manager</div>
          </div>

          <!-- Thông số & Phân tích đối chiếu -->
          <div class="proof-param-card">
            <div style="font-size:12px;font-weight:800;color:var(--accent-gold);text-transform:uppercase;letter-spacing:0.8px;margin-bottom:6px;">
              TẦNG 1 &bull; CHIẾN DỊCH (A/B TESTING)
            </div>
            <h4 style="font-size:16.5px;font-weight:700;color:var(--crema);margin-bottom:12px;">
              Cấu hình thử nghiệm phân tách A/B Testing
            </h4>

            <div class="proof-param-row">
              <span class="proof-badge-chip baseline">Nguyên tắc</span>
              <div style="font-size:13px;color:var(--warm-gray);">
                Bật A/B test &bull; Chạy 2 phiên bản (Quảng cáo A &amp; Quảng cáo B)<br />
                Ngân sách chia đôi: <strong>500.000đ / phiên bản</strong>
              </div>
            </div>

            <div class="proof-param-row">
              <span class="proof-badge-chip optimized">Tiêu chí thắng</span>
              <div style="font-size:13px;color:var(--crema);">
                <strong>Chi phí trên mỗi kết quả (CPA):</strong> bản nào có chi phí CPA thấp hơn sẽ giành chiến thắng!
              </div>
            </div>

            <div class="proof-param-row">
              <span class="proof-badge-chip optimized">Kết quả</span>
              <div style="font-size:12.5px;color:var(--text-muted);line-height:1.45;">
                🏆 <strong>Quảng cáo B thắng chung cuộc:</strong> CPA chỉ <strong class="text-matcha">10.919đ</strong> (rẻ hơn mẫu A 11.131đ), mang về 46 lượt theo dõi.
              </div>
            </div>
          </div>
        </div>
      </div>
'''

    pos_m5 = content.find('id="muc-5"')
    target_v2_split = '<!-- Trực Quan 2 Mẫu Quảng Cáo A/B Testing Đối Đầu -->'
    pos_v2_grid = content.find(target_v2_split, pos_m5)
    if pos_v2_grid != -1 and 'Minh Chứng Vòng 2' not in content:
        content = content[:pos_v2_grid] + v2_html + '\n      ' + content[pos_v2_grid:]

    # 5. Insert into Section 6 (Vòng 3)
    v3_html = '''
      <!-- Ảnh Minh Chứng Thiết Lập Vòng 3: Tăng Ngân Sách & Thời Gian Chạy -->
      <div class="proof-showcase-box matcha-theme">
        <div class="proof-showcase-header matcha-theme">
          <div class="proof-header-left">
            <span class="proof-header-badge matcha"><i data-lucide="trending-up" style="width:13px;height:13px;"></i> MINH CHỨNG VÒNG 3</span>
            <h3 class="proof-header-title">Thiết Lập Nhóm Quảng Cáo: Mở Rộng Quy Mô Ngân Sách &amp; Lịch Chạy</h3>
          </div>
          <div class="proof-header-hint"><i data-lucide="zoom-in" style="width:13px;height:13px;"></i> Nhấp ảnh để xem chi tiết Ads Manager</div>
        </div>

        <div class="proof-single-showcase-grid">
          <!-- Ảnh lớn có phóng to -->
          <div class="proof-single-media matcha" onclick="openLightbox('assets/vong-3-tang-2-ngan-sach.webp?v=20261107', 'Minh Chứng Vòng 3 — Tầng 2: Tăng Ngân Sách 250.000đ/ngày &times; 7 ngày = 1.750.000đ')">
            <img src="assets/vong-3-tang-2-ngan-sach.webp?v=20261107" alt="Minh chứng thiết lập Vòng 3 Olion Coffee" />
            <div class="proof-card-zoom-badge"><i data-lucide="zoom-in" style="width:12px;height:12px;"></i> Phóng to ảnh gốc Ads Manager</div>
          </div>

          <!-- Thông số & Phân tích đối chiếu -->
          <div class="proof-param-card matcha">
            <div style="font-size:12px;font-weight:800;color:var(--matcha-bright);text-transform:uppercase;letter-spacing:0.8px;margin-bottom:6px;">
              TẦNG 2 &bull; NHÓM QUẢNG CÁO (SCALE BUDGET)
            </div>
            <h4 style="font-size:16.5px;font-weight:700;color:var(--crema);margin-bottom:12px;">
              Tăng ngân sách lên 250k/ngày &bull; Kéo dài 7 ngày
            </h4>

            <div class="proof-param-row">
              <span class="proof-badge-chip baseline">Vòng 0, 1, 2</span>
              <div style="font-size:13px;color:var(--warm-gray);">
                Ngân sách: 200.000đ/ngày &bull; Thời gian: 5 ngày<br />
                Tổng chi tiêu: <strong>1.000.000đ</strong>
              </div>
            </div>

            <div class="proof-param-row">
              <span class="proof-badge-chip optimized">Vòng 3 (Scale)</span>
              <div style="font-size:13px;color:var(--crema);">
                Ngân sách: <strong class="text-matcha">250.000đ/ngày</strong> &bull; Thời gian: <strong class="text-matcha">7 ngày</strong><br />
                Tổng chi tiêu: <strong class="text-matcha">1.750.000đ</strong> (125.000đ/ngày/phiên bản)
              </div>
            </div>

            <div class="proof-param-row">
              <span class="proof-badge-chip optimized">Bứt phá Kỷ lục</span>
              <div style="font-size:12.5px;color:var(--text-muted);line-height:1.45;">
                🏆 <strong>Lượt theo dõi tăng vọt:</strong> đạt <strong class="text-matcha">162 lượt follow</strong> (+79% so với Vòng 2)<br />
                📉 <strong>CPA chạm đáy tối ưu:</strong> chỉ còn <strong class="text-matcha">10.833đ</strong> (mức rẻ nhất toàn chiến dịch!)
              </div>
            </div>
          </div>
        </div>
      </div>
'''

    pos_m6 = content.find('id="muc-6"')
    target_v3_table = '<h3 style="font-family:var(--font-serif);font-size:20px;color:#fff;margin:20px 0 10px;">Bảng số liệu tổng thể Vòng 3:</h3>'
    pos_v3_head = content.find(target_v3_table, pos_m6)
    if pos_v3_head != -1 and 'Minh Chứng Vòng 3' not in content:
        content = content[:pos_v3_head] + v3_html + '\n      ' + content[pos_v3_head:]

    with open('campaign-report.html', 'w', encoding='utf-8') as f:
        f.write(content)

    with open('report.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print('Updated both campaign-report.html and report.html successfully!')

if __name__ == '__main__':
    main()
