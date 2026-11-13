import re
import os

def build_cuoi_ky_7parts():
    # 1. Read base css from campaign-report.html
    with open('campaign-report.html', 'r', encoding='utf-8') as f:
        src_html = f.read()

    style_start = src_html.find('<style>')
    style_end = src_html.find('</style>')
    base_css = src_html[style_start+7:style_end]

    # 2. Read previous script to extract raw sections & components
    with open('scripts/build_cuoi_ky_final.py', 'r', encoding='utf-8') as f:
        src_script = f.read()

    start_extra = src_script.find('extra_css = """')
    end_extra = src_script.find('"""', start_extra + 16)
    extra_css = src_script[start_extra+15:end_extra]

    def get_section(sid):
        pattern = rf'(<section class="report-section" id="{sid}">[\s\S]*?</section>)'
        m = re.search(pattern, src_script)
        return m.group(1) if m else ""

    sec1_raw = get_section('muc-1')
    sec2_raw = get_section('muc-2')
    sec3_raw = get_section('muc-3')
    sec4_raw = get_section('muc-4')
    sec5_raw = get_section('muc-5')
    sec6_raw = get_section('muc-6')
    sec7_raw = get_section('muc-7')
    sec8_raw = get_section('muc-8')
    sec9_raw = get_section('muc-9')

    # ========================================================
    # NEW COMPREHENSIVE CSS OVERRIDE: CANVA BRAND COLOR PALETTE
    # Warm Ivory (#F6F1E7), Espresso Brown (#2C211B),
    # Warm Taupe (#B8A58B), Muted Sage (#7C8268), Scarlet Red (#D32F2F)
    # ========================================================
    canva_palette_css = """
    /* ========================================================
       CANVA BRAND COLOR PALETTE — OLION COFFEE
       Warm Ivory: #F6F1E7 (Nền chủ đạo)
       Espresso Brown: #2C211B (Chữ, menu, bao bì)
       Warm Taupe: #B8A58B (Logo, đường nét, điểm nhấn)
       Muted Sage: #7C8268 (Điểm nhấn thiên nhiên)
       Scarlet Red: #D32F2F (Màu nhấn, xuất hiện ít)
       ======================================================== */
    :root {
      --bg-darkest: #F6F1E7 !important;
      --bg-espresso: #F6F1E7 !important;
      --bg-wood: #FAF6F0 !important;
      --bg-card: #FFFFFF !important;
      --bg-card-alt: #FDFBF8 !important;
      --bg-card-subtle: #F9F6F0 !important;
      --bg-glass: rgba(255, 255, 255, 0.94) !important;
      
      --crema: #2C211B !important;
      --crema-muted: #5C4D44 !important;
      --text-main: #2C211B !important;
      --text-white: #2C211B !important;
      --text-muted: #66554B !important;
      --text-dim: #8B7C72 !important;
      
      --accent-gold: #B8A58B !important;
      --accent-gold-light: #DDD4C7 !important;
      --accent-gold-glow: rgba(184, 165, 139, 0.25) !important;
      --border-brass: rgba(184, 165, 139, 0.4) !important;
      --border-subtle: rgba(44, 33, 27, 0.12) !important;
      
      --matcha: #7C8268 !important;
      --matcha-green: #7C8268 !important;
      --matcha-bright: #8F957B !important;
      --matcha-dark: #585D48 !important;
      --matcha-glow: rgba(124, 130, 104, 0.25) !important;
      --border-matcha: rgba(124, 130, 104, 0.35) !important;
      
      --accent-rust: #D32F2F !important;
      --accent-red: #D32F2F !important;
      
      --shadow-wood: 0 10px 30px rgba(44, 33, 27, 0.07), 0 2px 8px rgba(184, 165, 139, 0.12) !important;
      --shadow-matcha: 0 10px 30px rgba(124, 130, 104, 0.1), 0 2px 8px rgba(124, 130, 104, 0.15) !important;
    }

    body {
      background-color: #F6F1E7 !important;
      color: #2C211B !important;
    }

    /* Fixed Cafe Header */
    .cafe-header {
      background: rgba(246, 241, 231, 0.94) !important;
      border-bottom: 1.5px solid rgba(184, 165, 139, 0.35) !important;
      box-shadow: 0 4px 20px rgba(44, 33, 27, 0.05) !important;
    }
    .header-brand-divider {
      background: rgba(184, 165, 139, 0.45) !important;
    }
    .badge-hub-title {
      color: #2C211B !important;
    }
    .badge-hub-sub {
      color: #7C8268 !important;
    }
    .cafe-nav-link {
      color: #2C211B !important;
    }
    .cafe-nav-link:hover, .cafe-nav-link.active {
      color: #7C8268 !important;
    }
    .cafe-nav-link.active::after {
      background: #7C8268 !important;
    }
    .header-icon-btn {
      background: rgba(184, 165, 139, 0.15) !important;
      border-color: rgba(184, 165, 139, 0.35) !important;
      color: #2C211B !important;
    }
    .header-icon-btn:hover {
      background: #B8A58B !important;
      color: #FFFFFF !important;
    }
    .header-icon-btn.home-btn {
      background: #7C8268 !important;
      border-color: #7C8268 !important;
      color: #FFFFFF !important;
    }

    /* Mobile Drawer */
    .mobile-nav-drawer {
      background: #F6F1E7 !important;
      border-left: 1.5px solid rgba(184, 165, 139, 0.35) !important;
    }
    .mobile-nav-link {
      color: #2C211B !important;
      border-bottom: 1px solid rgba(184, 165, 139, 0.2) !important;
    }
    .mobile-nav-link:hover, .mobile-nav-link.active {
      color: #7C8268 !important;
      background: rgba(124, 130, 104, 0.1) !important;
    }

    /* Hero Section */
    .hero-report-section {
      background: #F6F1E7 !important;
    }
    .hero-report-title {
      color: #2C211B !important;
    }
    .hero-report-subtitle {
      color: #7C8268 !important;
    }
    .hero-lead-text {
      color: #5C4D44 !important;
    }
    .hero-stat-item {
      background: #FFFFFF !important;
      border: 1.5px solid rgba(184, 165, 139, 0.35) !important;
      box-shadow: 0 8px 24px rgba(44, 33, 27, 0.05) !important;
    }
    .hero-stat-item.matcha-card {
      border-color: rgba(124, 130, 104, 0.45) !important;
      background: #FAF9F5 !important;
    }
    .hero-stat-num.text-gold {
      color: #B8A58B !important;
    }
    .hero-stat-num.text-matcha {
      color: #7C8268 !important;
    }
    .hero-stat-lbl {
      color: #2C211B !important;
    }
    .hero-stat-sub {
      color: #84766C !important;
    }
    .hero-banner-card {
      border: 1.5px solid rgba(184, 165, 139, 0.4) !important;
      box-shadow: 0 12px 32px rgba(44, 33, 27, 0.08) !important;
    }
    .hero-banner-caption {
      background: rgba(246, 241, 231, 0.95) !important;
      color: #2C211B !important;
      border-top: 1px solid rgba(184, 165, 139, 0.3) !important;
    }

    /* Sections & Headings */
    .section-chapter-tag {
      background: rgba(124, 130, 104, 0.12) !important;
      color: #585D48 !important;
      border: 1px solid rgba(124, 130, 104, 0.35) !important;
    }
    .section-chapter-tag.matcha {
      background: rgba(124, 130, 104, 0.15) !important;
      color: #585D48 !important;
      border-color: rgba(124, 130, 104, 0.4) !important;
    }
    .section-main-heading {
      color: #2C211B !important;
    }
    .report-section {
      border-top: 1.5px solid rgba(184, 165, 139, 0.3) !important;
    }

    /* Cards & Surfaces */
    .overview-card-item,
    .proof-card,
    .strategy-card,
    .kpi-card,
    .org-node-box,
    .channel-qr-card,
    .legal-card,
    .proposal-poster-card {
      background: #FFFFFF !important;
      border: 1.5px solid rgba(184, 165, 139, 0.35) !important;
      box-shadow: 0 6px 20px rgba(44, 33, 27, 0.05) !important;
      color: #2C211B !important;
    }
    .overview-card-item:hover,
    .proof-card:hover,
    .channel-qr-card:hover,
    .strategy-card:hover {
      border-color: #B8A58B !important;
      box-shadow: 0 12px 32px rgba(44, 33, 27, 0.1) !important;
    }

    /* Persona Card */
    .persona-card {
      background: #FFFFFF !important;
      border: 1.5px solid rgba(184, 165, 139, 0.4) !important;
      box-shadow: 0 12px 36px rgba(44, 33, 27, 0.06) !important;
    }
    .persona-info-panel {
      background: #FFFFFF !important;
    }
    .persona-name {
      color: #2C211B !important;
    }
    .persona-role {
      color: #7C8268 !important;
    }
    .persona-quote-box {
      background: #FAF7F2 !important;
      border-left: 3px solid #7C8268 !important;
      color: #2C211B !important;
    }

    /* Tables */
    .report-table-card {
      background: #FFFFFF !important;
      border: 1.5px solid rgba(184, 165, 139, 0.35) !important;
      box-shadow: 0 8px 24px rgba(44, 33, 27, 0.05) !important;
    }
    .report-table thead th {
      background: #EFE9DE !important;
      color: #2C211B !important;
      border-bottom: 2px solid #B8A58B !important;
      font-weight: 700 !important;
    }
    .report-table tbody tr {
      background: #FFFFFF !important;
      border-bottom: 1px solid rgba(184, 165, 139, 0.2) !important;
    }
    .report-table tbody tr:nth-child(even) {
      background: #FAF7F2 !important;
    }
    .report-table tbody tr:hover {
      background: rgba(184, 165, 139, 0.1) !important;
    }
    .report-table td {
      color: #2C211B !important;
    }
    .table-row-highlight {
      background: rgba(124, 130, 104, 0.12) !important;
    }
    .badge-kpi-pass {
      background: rgba(124, 130, 104, 0.18) !important;
      color: #4A503B !important;
      border: 1px solid #7C8268 !important;
    }
    .badge-kpi-red {
      background: rgba(211, 47, 47, 0.12) !important;
      color: #D32F2F !important;
      border: 1px solid rgba(211, 47, 47, 0.35) !important;
    }

    /* Org Tree Box (Gia Phả) */
    .org-node-box {
      background: #FFFFFF !important;
      border: 1.5px solid rgba(184, 165, 139, 0.35) !important;
    }
    .org-node-leader {
      background: #FAF7F2 !important;
      border-color: #B8A58B !important;
    }
    .org-node-name {
      color: #2C211B !important;
    }
    .org-node-role {
      color: #7C8268 !important;
    }
    .org-dept-header {
      background: #EFE9DE !important;
      color: #2C211B !important;
      border-bottom: 1px solid rgba(184, 165, 139, 0.35) !important;
    }
    .org-member-chip {
      background: #FFFFFF !important;
      border: 1px solid rgba(184, 165, 139, 0.3) !important;
      color: #2C211B !important;
    }
    .org-member-chip:hover {
      border-color: #7C8268 !important;
      background: #FAF9F5 !important;
    }

    /* Buttons */
    .cafe-btn-primary {
      background: #2C211B !important;
      color: #F6F1E7 !important;
      border: 1.5px solid #2C211B !important;
    }
    .cafe-btn-primary:hover {
      background: #7C8268 !important;
      border-color: #7C8268 !important;
      color: #FFFFFF !important;
    }

    /* ========================================================
       CHANNEL QR & DIRECT LINKS GRID (SECTION 2)
       ======================================================== */
    .channel-qr-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 20px;
      margin: 28px 0 36px;
    }
    @media (min-width: 640px) {
      .channel-qr-grid {
        grid-template-columns: repeat(2, 1fr);
      }
    }
    @media (min-width: 1024px) {
      .channel-qr-grid {
        grid-template-columns: repeat(4, 1fr);
      }
    }
    .channel-qr-card {
      background: #FFFFFF;
      border: 1.5px solid rgba(184, 165, 139, 0.4);
      border-radius: 16px;
      padding: 22px 18px 20px;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      transition: all 0.25s ease;
      position: relative;
      box-shadow: 0 6px 18px rgba(44, 33, 27, 0.05);
    }
    .channel-qr-card:hover {
      transform: translateY(-4px);
      border-color: #B8A58B;
      box-shadow: 0 14px 30px rgba(44, 33, 27, 0.1);
    }
    .channel-qr-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      padding: 4px 10px;
      border-radius: 20px;
      margin-bottom: 14px;
    }
    .channel-qr-badge.fb {
      background: rgba(24, 119, 242, 0.12);
      color: #1877F2;
      border: 1px solid rgba(24, 119, 242, 0.25);
    }
    .channel-qr-badge.tiktok {
      background: rgba(44, 33, 27, 0.1);
      color: #2C211B;
      border: 1px solid rgba(44, 33, 27, 0.2);
    }
    .channel-qr-badge.ig {
      background: rgba(225, 48, 108, 0.12);
      color: #C13584;
      border: 1px solid rgba(225, 48, 108, 0.25);
    }
    .channel-qr-badge.web {
      background: rgba(124, 130, 104, 0.14);
      color: #585D48;
      border: 1px solid rgba(124, 130, 104, 0.3);
    }

    .channel-qr-img-box {
      width: 154px;
      height: 154px;
      background: #FFFFFF;
      border: 1.5px solid rgba(184, 165, 139, 0.35);
      border-radius: 12px;
      padding: 8px;
      margin-bottom: 14px;
      cursor: zoom-in;
      position: relative;
      transition: all 0.2s ease;
      box-shadow: 0 4px 12px rgba(44, 33, 27, 0.04);
    }
    .channel-qr-img-box:hover {
      border-color: #B8A58B;
      transform: scale(1.03);
      box-shadow: 0 8px 20px rgba(44, 33, 27, 0.08);
    }
    .channel-qr-img {
      width: 100%;
      height: 100%;
      object-fit: contain;
      display: block;
    }
    .channel-qr-title {
      font-family: var(--font-serif);
      font-size: 19px;
      font-weight: 700;
      color: #2C211B;
      margin-bottom: 4px;
    }
    .channel-qr-desc {
      font-size: 12.5px;
      line-height: 1.45;
      color: #66554B;
      margin-bottom: 16px;
      flex-grow: 1;
    }
    .channel-qr-btn {
      width: 100%;
      padding: 9px 14px;
      border-radius: 9999px;
      font-size: 12.5px;
      font-weight: 600;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      text-decoration: none;
      transition: all 0.2s ease;
      color: #FFFFFF !important;
    }
    .channel-qr-btn.fb {
      background: #1877F2;
    }
    .channel-qr-btn.tiktok {
      background: #2C211B;
    }
    .channel-qr-btn.ig {
      background: linear-gradient(135deg, #833AB4, #FD1D1D, #FCAF45);
    }
    .channel-qr-btn.web {
      background: #7C8268;
    }
    .channel-qr-btn:hover {
      opacity: 0.9;
      transform: translateY(-1px);
    }

    /* ========================================================
       SECTION 7: TỔNG KẾT ẢNH SỐ LIỆU (PROPOSAL POSTER)
       ======================================================== */
    .proposal-poster-card {
      background: #FFFFFF;
      border: 1.5px solid rgba(184, 165, 139, 0.45);
      border-radius: 20px;
      overflow: hidden;
      box-shadow: 0 14px 36px rgba(44, 33, 27, 0.08);
      margin-bottom: 32px;
    }
    .proposal-poster-media {
      position: relative;
      background: #FAF7F2;
      cursor: zoom-in;
      border-bottom: 1.5px solid rgba(184, 165, 139, 0.3);
      padding: 16px;
      display: flex;
      justify-content: center;
      align-items: center;
    }
    .proposal-poster-img {
      width: 100%;
      max-width: 1000px;
      height: auto;
      display: block;
      border-radius: 12px;
      box-shadow: 0 8px 24px rgba(44, 33, 27, 0.1);
    }
    .proposal-poster-banner {
      padding: 20px 24px;
      background: #F9F6F0;
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 14px;
    }
    .proposal-poster-title {
      font-family: var(--font-serif);
      font-size: 21px;
      font-weight: 700;
      color: #2C211B;
    }
    .proposal-poster-sub {
      font-size: 13.5px;
      color: #7C8268;
      font-weight: 600;
    }

    /* Footer */
    .report-footer {
      background: #FAF6F0 !important;
      border-top: 1.5px solid rgba(184, 165, 139, 0.35) !important;
      color: #5C4D44 !important;
    }
    .footer-brand-tagline {
      color: #7C8268 !important;
    }
    """

    full_css = base_css + "\n" + extra_css + "\n" + canva_palette_css

    # Assemble Section 1: Combine muc-1 and muc-2 (Persona)
    # Strip </section> from sec1_raw
    sec1_clean = sec1_raw.rstrip()
    if sec1_clean.endswith('</section>'):
        sec1_clean = sec1_clean[:-10]
    
    # Strip outer section and shell from sec2_raw
    sec2_body = sec2_raw
    sec2_body = re.sub(r'<section class="report-section" id="muc-2">\s*<div class="shell">', '', sec2_body)
    sec2_body = re.sub(r'</div>\s*</section>$', '', sec2_body.strip())
    # Adjust headings in sec2_body
    sec2_body = sec2_body.replace('<div class="section-chapter-tag">2. CHÂN DUNG KHÁCH HÀNG (PERSONA)</div>', 
                                  '<div class="section-chapter-tag matcha" style="margin-bottom:12px;">1.2. CHÂN DUNG KHÁCH HÀNG MỤC TIÊU (PERSONA)</div>')
    sec2_body = sec2_body.replace('<h2 class="section-main-heading">2. Chân Dung Khách Hàng Mục Tiêu: Đoàn Minh Trang</h2>',
                                  '<h3 class="section-main-heading" style="font-size:28px;margin-bottom:14px;">Chân Dung Khách Hàng Mục Tiêu: Đoàn Minh Trang</h3>')

    sec1_combined = f"""{sec1_clean}
      <!-- Divider between 1.1 and 1.2 -->
      <div class="section-divider" style="margin: 48px 0 36px; border-top: 1.5px dashed rgba(184, 165, 139, 0.4);"></div>
      {sec2_body}
    </div>
  </section>"""

    # Assemble Section 2: Combine muc-3 and muc-4 (Growth Charts) + 4 QR Codes
    # Strip </section> from sec3_raw
    sec3_clean = sec3_raw.rstrip()
    if sec3_clean.endswith('</section>'):
        sec3_clean = sec3_clean[:-10]

    # Adjust sec3 headers
    sec3_clean = sec3_clean.replace('id="muc-3"', 'id="muc-2"')
    sec3_clean = sec3_clean.replace('<div class="section-chapter-tag">3. KPI DỰ ÁN &amp; KẾT QUẢ ĐẠT ĐƯỢC</div>',
                                    '<div class="section-chapter-tag">2. KẾT QUẢ SO VỚI KPI &amp; TĂNG TRƯỞNG</div>')
    sec3_clean = sec3_clean.replace('<h2 class="section-main-heading">3. Mục Tiêu KPI Kế Hoạch &amp; Kết Quả Thực Tế Từng Kênh</h2>',
                                    '<h2 class="section-main-heading">2. Kết Quả So Với KPI Kế Hoạch &amp; Tăng Trưởng Thực Tế</h2>')

    # Channel QR codes HTML block
    channel_qr_html = """
      <!-- ========================================================
           CỔNG KẾT NỐI 4 NỀN TẢNG SỐ & 4 MÃ QR CODE
           ======================================================== -->
      <div style="margin-top: 28px; margin-bottom: 8px;">
        <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px;margin-bottom:14px;">
          <div>
            <span style="font-size:12px;font-weight:700;color:var(--matcha-green);text-transform:uppercase;letter-spacing:0.08em;display:flex;align-items:center;gap:6px;">
              <i data-lucide="qr-code" style="width:14px;height:14px;"></i> Hệ Thống Đa Nền Tảng Số
            </span>
            <h3 style="font-family:var(--font-serif);font-size:24px;font-weight:700;color:var(--crema);margin:4px 0 0 0;">
              Truy Cập Trực Tiếp &amp; Quét Mã QR 4 Kênh Truyền Thông
            </h3>
          </div>
          <span style="font-size:13px;color:var(--text-muted);">
            <i data-lucide="info" style="width:14px;height:14px;display:inline-block;vertical-align:middle;margin-right:4px;"></i>
            Quét bằng camera điện thoại hoặc bấm nút để mở kênh
          </span>
        </div>
      </div>

      <div class="channel-qr-grid">
        <!-- Facebook Fanpage -->
        <div class="channel-qr-card">
          <div class="channel-qr-badge fb">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
            Facebook Fanpage
          </div>
          <div class="channel-qr-img-box" onclick="openLightbox('assets/cuoi-ky/qr-facebook.png', 'Mã QR Kênh Facebook Fanpage Olion Coffee (Quét để truy cập)')" title="Nhấp để phóng to QR">
            <img src="assets/cuoi-ky/qr-facebook.png" alt="QR Code Facebook Fanpage Olion Coffee" class="channel-qr-img" />
          </div>
          <div class="channel-qr-title">Facebook Fanpage</div>
          <div class="channel-qr-desc">
            Cổng thông tin &amp; kết nối chính thức, tương tác đạt <strong>665 lượt (110,8% KPI)</strong>.
          </div>
          <a href="https://www.facebook.com/profile.php?id=61594159312837" target="_blank" rel="noopener noreferrer" class="channel-qr-btn fb">
            <span>Mở Trang Facebook</span> <i data-lucide="external-link" style="width:13px;height:13px;"></i>
          </a>
        </div>

        <!-- TikTok Channel -->
        <div class="channel-qr-card">
          <div class="channel-qr-badge tiktok">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><path d="M12.525.02c1.31-.02 2.61-.01 3.91-.02.08 1.53.63 3.09 1.75 4.17 1.12 1.11 2.7 1.62 4.24 1.79v4.03c-1.44-.05-2.89-.35-4.2-.97-.57-.26-1.1-.59-1.62-.93-.01 2.92.01 5.84-.02 8.75-.08 1.4-.54 2.79-1.35 3.94-1.31 1.92-3.58 3.17-5.91 3.21-1.43.08-2.86-.31-4.08-1.03-2.02-1.19-3.44-3.37-3.65-5.71-.02-.5-.03-1-.01-1.49.18-1.9 1.12-3.72 2.58-4.96 1.66-1.44 3.98-2.13 6.15-1.72.02 1.48-.04 2.96-.04 4.44-.99-.32-2.15-.23-3.02.37-.63.41-1.11 1.04-1.36 1.75-.21.51-.24 1.07-.14 1.61.24 1.64 1.82 3.02 3.5 2.87 1.12-.01 2.19-.66 2.77-1.61.19-.33.4-.67.41-1.06.1-1.79.06-3.57.07-5.36.01-4.03-.01-8.05.02-12.07z"/></svg>
            TikTok Channel 🏆
          </div>
          <div class="channel-qr-img-box" onclick="openLightbox('assets/cuoi-ky/qr-tiktok.png', 'Mã QR Kênh TikTok @olion.coffee (Quét để truy cập)')" title="Nhấp để phóng to QR">
            <img src="assets/cuoi-ky/qr-tiktok.png" alt="QR Code TikTok Olion Coffee" class="channel-qr-img" />
          </div>
          <div class="channel-qr-title">TikTok Channel</div>
          <div class="channel-qr-desc">
            Kênh viral tiếp cận sinh viên VLU, đạt <strong>14.617 views</strong> và bứt phá <strong>282 followers</strong>.
          </div>
          <a href="https://www.tiktok.com/@olion.coffee" target="_blank" rel="noopener noreferrer" class="channel-qr-btn tiktok">
            <span>Mở Kênh TikTok</span> <i data-lucide="external-link" style="width:13px;height:13px;"></i>
          </a>
        </div>

        <!-- Instagram Profile -->
        <div class="channel-qr-card">
          <div class="channel-qr-badge ig">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg>
            Instagram Art
          </div>
          <div class="channel-qr-img-box" onclick="openLightbox('assets/cuoi-ky/qr-instagram.png', 'Mã QR Kênh Instagram @olion.coffee (Quét để truy cập)')" title="Nhấp để phóng to QR">
            <img src="assets/cuoi-ky/qr-instagram.png" alt="QR Code Instagram Olion Coffee" class="channel-qr-img" />
          </div>
          <div class="channel-qr-title">Instagram Profile</div>
          <div class="channel-qr-desc">
            Không gian nghệ thuật thẩm mỹ cao, thu hút <strong>1.186 tương tác</strong> &amp; <strong>142 followers</strong>.
          </div>
          <a href="https://www.instagram.com/olion.coffee/" target="_blank" rel="noopener noreferrer" class="channel-qr-btn ig">
            <span>Mở Trang Instagram</span> <i data-lucide="external-link" style="width:13px;height:13px;"></i>
          </a>
        </div>

        <!-- Landing Page Web -->
        <div class="channel-qr-card">
          <div class="channel-qr-badge web">
            <i data-lucide="globe" style="width:12px;height:12px;"></i>
            Landing Page
          </div>
          <div class="channel-qr-img-box" onclick="openLightbox('assets/cuoi-ky/qr-landingpage.png', 'Mã QR Website Landing Page Olion Coffee (Quét để truy cập)')" title="Nhấp để phóng to QR">
            <img src="assets/cuoi-ky/qr-landingpage.png" alt="QR Code Landing Page Olion Coffee" class="channel-qr-img" />
          </div>
          <div class="channel-qr-title">Landing Page Web</div>
          <div class="channel-qr-desc">
            Trang đích tích hợp menu điện tử, bùng nổ <strong>280 visits ở tuần 4</strong> (tổng 381 visits).
          </div>
          <a href="https://www.olioncoffee.app/" target="_blank" rel="noopener noreferrer" class="channel-qr-btn web">
            <span>Mở Trang Web</span> <i data-lucide="external-link" style="width:13px;height:13px;"></i>
          </a>
        </div>
      </div>
    """

    # Inject channel_qr_html right before the KPI table
    table_marker = '<div class="report-table-card" style="margin-top:28px;">'
    if table_marker in sec3_clean:
        sec3_clean = sec3_clean.replace(table_marker, channel_qr_html + '\n' + table_marker)
    else:
        sec3_clean += channel_qr_html

    # Strip outer section and shell from sec4_raw (growth charts)
    sec4_body = sec4_raw
    sec4_body = re.sub(r'<section class="report-section" id="muc-4">\s*<div class="shell">', '', sec4_body)
    sec4_body = re.sub(r'</div>\s*</section>$', '', sec4_body.strip())
    sec4_body = sec4_body.replace('<div class="section-chapter-tag">4. TĂNG TRƯỞNG QUA 6 TUẦN</div>',
                                  '<div class="section-chapter-tag matcha" style="margin-bottom:12px;">2.2. THEO DÕI TĂNG TRƯỞNG QUA 6 TUẦN</div>')
    sec4_body = sec4_body.replace('<h2 class="section-main-heading">4. Theo Dõi &amp; Đánh Giá Tăng Trưởng Qua 6 Tuần</h2>',
                                  '<h3 class="section-main-heading" style="font-size:28px;margin-bottom:14px;">Biểu Đồ Theo Dõi &amp; Đánh Giá Tăng Trưởng Qua 6 Tuần</h3>')

    sec2_combined = f"""{sec3_clean}
      <!-- Divider between 2.1 and 2.2 -->
      <div class="section-divider" style="margin: 48px 0 36px; border-top: 1.5px dashed rgba(184, 165, 139, 0.4);"></div>
      {sec4_body}
    </div>
  </section>"""

    # Assemble Section 3: Sản phẩm truyền thông nổi bật và demo (was muc-5)
    sec3_combined = sec5_raw
    sec3_combined = sec3_combined.replace('id="muc-5"', 'id="muc-3"')
    sec3_combined = sec3_combined.replace('<div class="section-chapter-tag">5. SẢN PHẨM TRUYỀN THÔNG TIÊU BIỂU</div>',
                                          '<div class="section-chapter-tag">3. SẢN PHẨM TRUYỀN THÔNG &amp; DEMO</div>')
    sec3_combined = sec3_combined.replace('<h2 class="section-main-heading">5. Sản Phẩm Truyền Thông Nổi Bật &amp; Minh Chứng Thực Tế</h2>',
                                          '<h2 class="section-main-heading">3. Sản Phẩm Truyền Thông Nổi Bật &amp; Minh Chứng Thực Tế</h2>')

    # Assemble Section 4: Phân tích và điều chỉnh (was muc-6 + kế hoạch đẩy số)
    sec4_combined = sec6_raw
    sec4_combined = sec4_combined.replace('id="muc-6"', 'id="muc-4"')
    sec4_combined = sec4_combined.replace('<div class="section-chapter-tag">6. ĐÁNH GIÁ &amp; BÀI HỌC KINH NGHIỆM</div>',
                                          '<div class="section-chapter-tag">4. PHÂN TÍCH &amp; ĐIỀU CHỈNH CHIẾN LƯỢC</div>')
    sec4_combined = sec4_combined.replace('<h2 class="section-main-heading">6. Đánh Giá Tổng Quan 4 Kênh &amp; Bài Học Chiến Lược</h2>',
                                          '<h2 class="section-main-heading">4. Phân Tích Tổng Quan 4 Kênh &amp; Điều Chỉnh Chiến Lược</h2>')

    # Assemble Section 5: Tuân thủ pháp lý (was muc-7)
    sec5_combined = sec7_raw
    sec5_combined = sec5_combined.replace('id="muc-7"', 'id="muc-5"')
    sec5_combined = sec5_combined.replace('<div class="section-chapter-tag">7. TUÂN THỦ PHÁP LÝ &amp; ĐẠO ĐỨC</div>',
                                          '<div class="section-chapter-tag">5. TUÂN THỦ PHÁP LÝ &amp; ĐẠO ĐỨC</div>')
    sec5_combined = sec5_combined.replace('<h2 class="section-main-heading">7. Danh Mục 12 Tiêu Chí Tuân Thủ Pháp Lý &amp; Quảng Cáo</h2>',
                                          '<h2 class="section-main-heading">5. Danh Mục 12 Tiêu Chí Tuân Thủ Pháp Lý &amp; Chuẩn Mực Quảng Cáo</h2>')

    # Assemble Section 6: Sáng tạo và định hướng khởi nghiệp (was muc-8 + muc-9 Gia Phả)
    sec8_clean = sec8_raw.rstrip()
    if sec8_clean.endswith('</section>'):
        sec8_clean = sec8_clean[:-10]
    sec8_clean = sec8_clean.replace('id="muc-8"', 'id="muc-6"')
    sec8_clean = sec8_clean.replace('<div class="section-chapter-tag">8. KẾ HOẠCH PHÁT TRIỂN 3 THÁNG</div>',
                                    '<div class="section-chapter-tag">6. SÁNG TẠO &amp; ĐỊNH HƯỚNG KHỞI NGHIỆP</div>')
    sec8_clean = sec8_clean.replace('<h2 class="section-main-heading">8. Định Hướng Duy Trì Kênh &amp; Mục Tiêu Phát Triển 3 Tháng Tới</h2>',
                                    '<h2 class="section-main-heading">6. Sáng Tạo Nội Dung &amp; Định Hướng Khởi Nghiệp Thực Tế</h2>')

    # Strip outer section and shell from sec9_raw (Gia phả)
    sec9_body = sec9_raw
    sec9_body = re.sub(r'<section class="report-section" id="muc-9">\s*<div class="shell">', '', sec9_body)
    sec9_body = re.sub(r'</div>\s*</section>$', '', sec9_body.strip())
    sec9_body = sec9_body.replace('<div class="section-chapter-tag">9. ĐỘI NGŨ THỰC HIỆN DỰ ÁN</div>',
                                  '<div class="section-chapter-tag matcha" style="margin-bottom:12px;">6.4. ĐỘI NGŨ THỰC HIỆN DỰ ÁN (BẢNG GIA PHẢ)</div>')
    sec9_body = sec9_body.replace('<h2 class="section-main-heading">9. Phân Vai &amp; Đóng Góp Của Các Thành Viên Nhóm 7 (Gỗ Xà Cừ)</h2>',
                                  '<h3 class="section-main-heading" style="font-size:28px;margin-bottom:14px;">Cơ Cấu Tổ Chức &amp; Phân Vai Thành Viên Nhóm 7 (Gỗ Xà Cừ)</h3>')

    sec6_combined = f"""{sec8_clean}
      <!-- Divider between 6.1-6.3 and 6.4 (Gia Phả) -->
      <div class="section-divider" style="margin: 48px 0 36px; border-top: 1.5px dashed rgba(184, 165, 139, 0.4);"></div>
      {sec9_body}
    </div>
  </section>"""

    # Assemble Section 7: BRAND NEW SECTION FOR THE USER'S COMPLETED POSTER
    sec7_combined = """
  <!-- ========================================================
       MỤC 7: TỔNG KẾT ẢNH SỐ LIỆU (PROPOSAL DỰ ÁN TRUYỀN THÔNG SỐ)
       ======================================================== -->
  <section class="report-section" id="muc-7">
    <div class="shell">
      <div class="section-chapter-tag">7. TỔNG KẾT ẢNH SỐ LIỆU</div>
      <h2 class="section-main-heading">7. Tổng Kết Ảnh Số Liệu &amp; Proposal Dự Án 6 Tuần</h2>
      <p style="color:var(--text-muted);margin-bottom:28px;font-size:15px;line-height:1.6;">
        Bảng tổng kết Proposal Dự án Truyền thông số học kỳ 261 (GV: Jon Lâm), tổng hợp toàn bộ các chỉ số đo lường thực tế định kỳ 6 tuần trên 4 nền tảng số (Instagram, Facebook, TikTok và Landing Page), kèm mã QR tra cứu trực tiếp.
      </p>

      <!-- Proposal Poster Luxury Card -->
      <div class="proposal-poster-card">
        <div class="proposal-poster-banner">
          <div>
            <div class="proposal-poster-title">Bảng Tổng Hợp Proposal Chiến Dịch Truyền Thông Số</div>
            <div class="proposal-poster-sub">Học kỳ 261 &bull; GV: Jon Lâm &bull; Nhóm 7 — Gỗ Xà Cừ (Olion Coffee)</div>
          </div>
          <div class="poster-action-btns">
            <button type="button" class="cafe-btn-primary" onclick="openLightbox('assets/cuoi-ky/proposal-du-an-truyen-thong-so.jpg', 'Bảng Tổng Hợp Proposal Dự Án Truyền Thông Số (Học kỳ 261 • GV: Jon Lâm)')" style="padding:8px 16px;border-radius:9999px;font-size:13px;display:inline-flex;align-items:center;gap:6px;cursor:pointer;">
              <i data-lucide="maximize-2" style="width:14px;height:14px;"></i> Phóng To Toàn Màn Hình
            </button>
            <a href="assets/cuoi-ky/proposal-du-an-truyen-thong-so.jpg" download="Proposal-Olion-Coffee-Nhom-7.jpg" class="header-icon-btn" style="padding:8px 14px;border-radius:9999px;font-size:13px;text-decoration:none;display:inline-flex;align-items:center;gap:6px;">
              <i data-lucide="download" style="width:14px;height:14px;"></i> Tải Ảnh Gốc
            </a>
          </div>
        </div>

        <div class="proposal-poster-media" onclick="openLightbox('assets/cuoi-ky/proposal-du-an-truyen-thong-so.jpg', 'Bảng Tổng Hợp Proposal Dự Án Truyền Thông Số (Học kỳ 261 • GV: Jon Lâm)')">
          <img src="assets/cuoi-ky/proposal-du-an-truyen-thong-so.jpg" alt="Proposal Dự Án Truyền Thông Số Olion Coffee - Nhóm 7 Gỗ Xà Cừ" class="proposal-poster-img" loading="lazy" />
        </div>
      </div>

      <!-- 3 Tables trích xuất số liệu 6 tuần chi tiết từ poster -->
      <div style="margin-top:32px;">
        <h3 style="font-family:var(--font-serif);font-size:24px;font-weight:700;color:var(--crema);margin-bottom:16px;">
          Bảng Thống Kê Số Liệu Chi Tiết 6 Tuần Từng Nền Tảng (Trích Xuất Từ Poster)
        </h3>
        
        <div class="report-two-cols" style="margin-bottom:24px;">
          <!-- Instagram Table -->
          <div class="report-table-card" style="margin-top:0;">
            <div style="padding:14px 18px;background:#FAF7F2;border-bottom:1px solid rgba(184,165,139,0.3);display:flex;align-items:center;justify-content:space-between;">
              <strong style="color:var(--crema);font-size:15px;display:flex;align-items:center;gap:8px;">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#C13584" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg>
                Kênh Instagram
              </strong>
              <span class="badge-kpi-pass" style="font-size:11px;padding:3px 8px;">Tổng 142 Followers</span>
            </div>
            <div class="table-scroll-wrap">
              <table class="report-table" style="font-size:13px;">
                <thead>
                  <tr>
                    <th>Tuần</th>
                    <th style="text-align:center;">Số bài</th>
                    <th style="text-align:right;">Lượt xem</th>
                    <th style="text-align:right;">Tương tác</th>
                    <th style="text-align:right;">Followers</th>
                  </tr>
                </thead>
                <tbody>
                  <tr><td>Tuần 1</td><td style="text-align:center;">5</td><td style="text-align:right;">4.300</td><td style="text-align:right;">291</td><td style="text-align:right;font-weight:600;">58</td></tr>
                  <tr><td>Tuần 2</td><td style="text-align:center;">5</td><td style="text-align:right;">2.000</td><td style="text-align:right;">73</td><td style="text-align:right;font-weight:600;">64</td></tr>
                  <tr><td>Tuần 3</td><td style="text-align:center;">6</td><td style="text-align:right;">1.500</td><td style="text-align:right;">115</td><td style="text-align:right;font-weight:600;">79</td></tr>
                  <tr><td>Tuần 4</td><td style="text-align:center;">5</td><td style="text-align:right;">2.100</td><td style="text-align:right;">513</td><td style="text-align:right;font-weight:600;">119</td></tr>
                  <tr><td>Tuần 5</td><td style="text-align:center;">5</td><td style="text-align:right;">1.100</td><td style="text-align:right;">85</td><td style="text-align:right;font-weight:600;">122</td></tr>
                  <tr class="table-row-highlight"><td>Tuần 6</td><td style="text-align:center;font-weight:700;">4</td><td style="text-align:right;font-weight:700;">1.200</td><td style="text-align:right;font-weight:700;">107</td><td style="text-align:right;font-weight:700;color:var(--matcha-green);">142</td></tr>
                </tbody>
              </table>
            </div>
          </div>

          <!-- Facebook Table -->
          <div class="report-table-card" style="margin-top:0;">
            <div style="padding:14px 18px;background:#FAF7F2;border-bottom:1px solid rgba(184,165,139,0.3);display:flex;align-items:center;justify-content:space-between;">
              <strong style="color:var(--crema);font-size:15px;display:flex;align-items:center;gap:8px;">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="#1877F2"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
                Kênh Facebook Fanpage
              </strong>
              <span class="badge-kpi-pass" style="font-size:11px;padding:3px 8px;">Tổng 100 Followers</span>
            </div>
            <div class="table-scroll-wrap">
              <table class="report-table" style="font-size:13px;">
                <thead>
                  <tr>
                    <th>Tuần</th>
                    <th style="text-align:center;">Số bài</th>
                    <th style="text-align:right;">Lượt xem</th>
                    <th style="text-align:right;">Tương tác</th>
                    <th style="text-align:right;">Followers</th>
                  </tr>
                </thead>
                <tbody>
                  <tr><td>Tuần 1</td><td style="text-align:center;">5</td><td style="text-align:right;">2.300</td><td style="text-align:right;">157</td><td style="text-align:right;font-weight:600;">50</td></tr>
                  <tr><td>Tuần 2</td><td style="text-align:center;">5</td><td style="text-align:right;">1.900</td><td style="text-align:right;">112</td><td style="text-align:right;font-weight:600;">56</td></tr>
                  <tr><td>Tuần 3</td><td style="text-align:center;">6</td><td style="text-align:right;">1.600</td><td style="text-align:right;">92</td><td style="text-align:right;font-weight:600;">66</td></tr>
                  <tr><td>Tuần 4</td><td style="text-align:center;">5</td><td style="text-align:right;">1.300</td><td style="text-align:right;">138</td><td style="text-align:right;font-weight:600;">79</td></tr>
                  <tr><td>Tuần 5</td><td style="text-align:center;">5</td><td style="text-align:right;">1.700</td><td style="text-align:right;">65</td><td style="text-align:right;font-weight:600;">92</td></tr>
                  <tr class="table-row-highlight"><td>Tuần 6</td><td style="text-align:center;font-weight:700;">4</td><td style="text-align:right;font-weight:700;">852</td><td style="text-align:right;font-weight:700;">91</td><td style="text-align:right;font-weight:700;color:var(--matcha-green);">100</td></tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <!-- TikTok Full Width Table -->
        <div class="report-table-card" style="margin-top:0;margin-bottom:28px;">
          <div style="padding:14px 18px;background:#FAF7F2;border-bottom:1px solid rgba(184,165,139,0.3);display:flex;align-items:center;justify-content:space-between;">
            <strong style="color:var(--crema);font-size:15px;display:flex;align-items:center;gap:8px;">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="#2C211B"><path d="M12.525.02c1.31-.02 2.61-.01 3.91-.02.08 1.53.63 3.09 1.75 4.17 1.12 1.11 2.7 1.62 4.24 1.79v4.03c-1.44-.05-2.89-.35-4.2-.97-.57-.26-1.1-.59-1.62-.93-.01 2.92.01 5.84-.02 8.75-.08 1.4-.54 2.79-1.35 3.94-1.31 1.92-3.58 3.17-5.91 3.21-1.43.08-2.86-.31-4.08-1.03-2.02-1.19-3.44-3.37-3.65-5.71-.02-.5-.03-1-.01-1.49.18-1.9 1.12-3.72 2.58-4.96 1.66-1.44 3.98-2.13 6.15-1.72.02 1.48-.04 2.96-.04 4.44-.99-.32-2.15-.23-3.02.37-.63.41-1.11 1.04-1.36 1.75-.21.51-.24 1.07-.14 1.61.24 1.64 1.82 3.02 3.5 2.87 1.12-.01 2.19-.66 2.77-1.61.19-.33.4-.67.41-1.06.1-1.79.06-3.57.07-5.36.01-4.03-.01-8.05.02-12.07z"/></svg>
              Kênh TikTok (Kênh Mũi Nhọn Tăng Trưởng)
            </strong>
            <span class="badge-kpi-pass" style="font-size:11px;padding:3px 8px;">Bứt Phá 282 Followers</span>
          </div>
          <div class="table-scroll-wrap">
            <table class="report-table" style="font-size:13px;">
              <thead>
                <tr>
                  <th>Tuần Triển Khai</th>
                  <th style="text-align:center;">Số bài đăng</th>
                  <th style="text-align:right;">Lượt xem (Views)</th>
                  <th style="text-align:right;">Lượt tương tác</th>
                  <th style="text-align:right;">Tổng Followers</th>
                  <th>Ghi chú chiến lược</th>
                </tr>
              </thead>
              <tbody>
                <tr><td>Tuần 1</td><td style="text-align:center;">5</td><td style="text-align:right;">1.800</td><td style="text-align:right;">184</td><td style="text-align:right;font-weight:600;">60</td><td style="color:var(--text-muted);">Khởi động kênh, giới thiệu vị trí quán</td></tr>
                <tr><td>Tuần 2</td><td style="text-align:center;">5</td><td style="text-align:right;">4.400</td><td style="text-align:right;">218</td><td style="text-align:right;font-weight:600;">73</td><td style="color:var(--text-muted);">Video không gian quán thu hút sinh viên VLU</td></tr>
                <tr><td>Tuần 3</td><td style="text-align:center;">5</td><td style="text-align:right;">3.100</td><td style="text-align:right;">240</td><td style="text-align:right;font-weight:600;">137</td><td style="color:var(--text-muted);">Tập trung menu thức uống Matcha &amp; Cacao</td></tr>
                <tr class="table-row-highlight"><td>Tuần 4</td><td style="text-align:center;font-weight:700;">5</td><td style="text-align:right;font-weight:700;">4.400</td><td style="text-align:right;font-weight:700;">362</td><td style="text-align:right;font-weight:700;color:var(--matcha-green);">275</td><td style="color:var(--crema);font-weight:600;">Bùng nổ tương tác &amp; tăng trưởng follower vượt bậc</td></tr>
                <tr><td>Tuần 5</td><td style="text-align:center;">5</td><td style="text-align:right;">4.500</td><td style="text-align:right;">378</td><td style="text-align:right;font-weight:600;">261</td><td style="color:var(--text-muted);">Duy trì nhịp đăng đều đặn</td></tr>
                <tr class="table-row-highlight"><td>Tuần 6</td><td style="text-align:center;font-weight:700;">6</td><td style="text-align:right;font-weight:700;color:var(--matcha-green);">5.300</td><td style="text-align:right;font-weight:700;color:var(--matcha-green);">616</td><td style="text-align:right;font-weight:700;color:var(--matcha-green);">282</td><td style="color:var(--crema);font-weight:600;">Đạt đỉnh lượt xem &amp; tương tác toàn chiến dịch</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- Total Campaign Highlights Box -->
      <div style="background:#FAF7F2;border:1.5px solid rgba(184,165,139,0.4);border-radius:16px;padding:24px 28px;margin-bottom:32px;">
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:12px;">
          <i data-lucide="award" style="width:24px;height:24px;color:var(--matcha-green);"></i>
          <h3 style="font-family:var(--font-serif);font-size:22px;font-weight:700;color:var(--crema);margin:0;">
            Tổng Kết Thành Tựu Chiến Dịch Truyền Thông Số Olion Coffee
          </h3>
        </div>
        <p style="font-size:14.5px;line-height:1.65;color:var(--text-muted);margin-bottom:16px;">
          Sau 6 tuần triển khai thực tế trên cả 4 nền tảng số, Nhóm 7 — Gỗ Xà Cừ đã đạt được những chỉ số ấn tượng:
        </p>
        <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(200px, 1fr));gap:16px;margin-bottom:20px;">
          <div style="background:#FFFFFF;border:1px solid rgba(184,165,139,0.3);border-radius:12px;padding:14px 16px;">
            <div style="font-size:12px;color:var(--text-muted);text-transform:uppercase;font-weight:600;">Tổng Reach (Tiếp Cận)</div>
            <div style="font-size:24px;font-weight:800;color:var(--matcha-green);margin-top:4px;">15.656+</div>
            <div style="font-size:11.5px;color:var(--text-muted);">Vượt mục tiêu nhận diện</div>
          </div>
          <div style="background:#FFFFFF;border:1px solid rgba(184,165,139,0.3);border-radius:12px;padding:14px 16px;">
            <div style="font-size:12px;color:var(--text-muted);text-transform:uppercase;font-weight:600;">Tổng Lượt Xem Video</div>
            <div style="font-size:24px;font-weight:800;color:var(--crema);margin-top:4px;">22.500+</div>
            <div style="font-size:11.5px;color:var(--text-muted);">TikTok &amp; Instagram Reels</div>
          </div>
          <div style="background:#FFFFFF;border:1px solid rgba(184,165,139,0.3);border-radius:12px;padding:14px 16px;">
            <div style="font-size:12px;color:var(--text-muted);text-transform:uppercase;font-weight:600;">Tỷ Lệ Đạt KPI Tương Tác</div>
            <div style="font-size:24px;font-weight:800;color:var(--matcha-green);margin-top:4px;">110,8%</div>
            <div style="font-size:11.5px;color:var(--text-muted);">Vượt KPI Facebook đề ra</div>
          </div>
          <div style="background:#FFFFFF;border:1px solid rgba(184,165,139,0.3);border-radius:12px;padding:14px 16px;">
            <div style="font-size:12px;color:var(--text-muted);text-transform:uppercase;font-weight:600;">Lượt Truy Cập Landing Page</div>
            <div style="font-size:24px;font-weight:800;color:var(--crema);margin-top:4px;">381 Visits</div>
            <div style="font-size:11.5px;color:var(--text-muted);">Đỉnh điểm 280 visits (Tuần 4)</div>
          </div>
        </div>
        <p style="font-size:14px;line-height:1.6;color:var(--crema);margin:0;font-style:italic;">
          &ldquo;Dự án truyền thông số cho quán cà phê Olion không chỉ là bài tập thực hành trên giảng đường mà đã trở thành cầu nối thương hiệu vững chắc giữa quán và cộng đồng sinh viên Đại học Văn Lang. Nhóm 7 xin trân trọng cảm ơn Thầy Jon Lâm đã tận tình định hướng và hướng dẫn nhóm trong suốt học kỳ 261 vừa qua!&rdquo;
        </p>
      </div>
    </div>
  </section>
"""

    # Assemble the full HTML document
    # Header navigation menu with EXACT 7 ITEMS:
    nav_menu_html = """
        <nav class="cafe-nav-menu">
          <a href="#muc-1" class="cafe-nav-link active">1. Tổng Quan</a>
          <a href="#muc-2" class="cafe-nav-link">2. Kết Quả KPI</a>
          <a href="#muc-3" class="cafe-nav-link">3. Sản Phẩm Demo</a>
          <a href="#muc-4" class="cafe-nav-link">4. Phân Tích</a>
          <a href="#muc-5" class="cafe-nav-link">5. Pháp Lý</a>
          <a href="#muc-6" class="cafe-nav-link">6. Sáng Tạo &amp; Khởi Nghiệp</a>
          <a href="#muc-7" class="cafe-nav-link">7. Tổng Kết Số Liệu</a>
        </nav>
    """

    mobile_drawer_html = """
    <div class="mobile-nav-drawer" id="mobileDrawer">
      <div class="mobile-drawer-header">
        <span style="font-weight:700;font-family:var(--font-serif);color:var(--crema);font-size:18px;">MỤC LỤC BÁO CÁO</span>
        <button type="button" class="lightbox-close-btn" onclick="toggleDrawer()" style="position:static;">
          <i data-lucide="x" style="width:18px;height:18px;"></i>
        </button>
      </div>
      <div class="mobile-nav-links">
        <a href="#muc-1" class="mobile-nav-link active" onclick="toggleDrawer()"><span>1. Tổng quan dự án &amp; Persona</span> <i data-lucide="chevron-right" style="width:14px;height:14px;"></i></a>
        <a href="#muc-2" class="mobile-nav-link" onclick="toggleDrawer()"><span>2. Kết quả so với KPI &amp; 4 Mã QR</span> <i data-lucide="chevron-right" style="width:14px;height:14px;"></i></a>
        <a href="#muc-3" class="mobile-nav-link" onclick="toggleDrawer()"><span>3. Sản phẩm truyền thông nổi bật &amp; Demo</span> <i data-lucide="chevron-right" style="width:14px;height:14px;"></i></a>
        <a href="#muc-4" class="mobile-nav-link" onclick="toggleDrawer()"><span>4. Phân tích tổng quan &amp; Điều chỉnh</span> <i data-lucide="chevron-right" style="width:14px;height:14px;"></i></a>
        <a href="#muc-5" class="mobile-nav-link" onclick="toggleDrawer()"><span>5. Tuân thủ pháp lý (12 tiêu chí)</span> <i data-lucide="chevron-right" style="width:14px;height:14px;"></i></a>
        <a href="#muc-6" class="mobile-nav-link" onclick="toggleDrawer()"><span>6. Sáng tạo &amp; Khởi nghiệp (Gia phả)</span> <i data-lucide="chevron-right" style="width:14px;height:14px;"></i></a>
        <a href="#muc-7" class="mobile-nav-link" onclick="toggleDrawer()"><span>7. Tổng kết ảnh số liệu (Proposal Poster)</span> <i data-lucide="chevron-right" style="width:14px;height:14px;"></i></a>
      </div>
    </div>
    """

    # Extract HTML head and hero up to muc-1
    head_hero_part = src_script[src_script.find('html = """') + 10 : src_script.find('<section class="report-section" id="muc-1">')]

    # Replace navigation in head_hero_part
    old_nav_pattern = r'<nav class="cafe-nav-menu">[\s\S]*?</nav>'
    head_hero_part = re.sub(old_nav_pattern, nav_menu_html.strip(), head_hero_part)

    old_drawer_pattern = r'<div class="mobile-nav-drawer" id="mobileDrawer">[\s\S]*?</div>\s*</div>'
    head_hero_part = re.sub(old_drawer_pattern, mobile_drawer_html.strip(), head_hero_part)

    # Extract footer and script tail after muc-9
    tail_part = src_script[src_script.find('</section>\n\n  <!-- ========================================================\n       FOOTER') :]
    tail_part = tail_part[:tail_part.find('html = html.replace("__CSS__", full_css)')]

    # Combine all parts
    assembled_html = head_hero_part + "\n" + \
                     sec1_combined + "\n\n" + \
                     sec2_combined + "\n\n" + \
                     sec3_combined + "\n\n" + \
                     sec4_combined + "\n\n" + \
                     sec5_combined + "\n\n" + \
                     sec6_combined + "\n\n" + \
                     sec7_combined + "\n\n" + \
                     tail_part

    # Replace CSS placeholder
    assembled_html = assembled_html.replace('__CSS__', full_css)

    # Clean any dangling references
    assembled_html = assembled_html.replace('<!-- Slogan Ribbon Banner -->', '<!-- Slogan Ribbon Banner -->')

    # Save to cuoi-ky.html and bao-cao-cuoi-ky.html
    with open('cuoi-ky.html', 'w', encoding='utf-8') as f:
        f.write(assembled_html)

    with open('bao-cao-cuoi-ky.html', 'w', encoding='utf-8') as f:
        f.write(assembled_html)

    print("Successfully built cuoi-ky.html and bao-cao-cuoi-ky.html with 7 sections & Canva Palette!")

if __name__ == '__main__':
    build_cuoi_ky_7parts()
