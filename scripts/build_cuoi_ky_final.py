import re

def build_cuoi_ky_report():
    # Read the full CSS style block from campaign-report.html
    with open('campaign-report.html', 'r', encoding='utf-8') as f:
        src_html = f.read()

    style_start = src_html.find('<style>')
    style_end = src_html.find('</style>')
    base_css = src_html[style_start+7:style_end]

    # Additional CSS for Team Members and Custom Visuals
    extra_css = """
    /* ========================================================
       SECTION 9: THÀNH VIÊN NHÓM 7 (GỖ XÀ CỪ)
       ======================================================== */
    .team-showcase-container {
      margin-top: 30px;
    }
    .team-dept-block {
      margin-bottom: 40px;
    }
    .team-dept-title {
      font-family: var(--font-serif);
      font-size: 24px;
      font-weight: 700;
      color: var(--accent-gold);
      margin-bottom: 20px;
      display: flex;
      align-items: center;
      gap: 12px;
      padding-bottom: 10px;
      border-bottom: 1.5px solid rgba(240, 167, 101, 0.25);
    }
    .team-dept-title.matcha {
      color: var(--matcha-green);
      border-bottom-color: rgba(46, 204, 113, 0.25);
    }
    .team-members-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 24px;
    }
    @media (min-width: 640px) {
      .team-members-grid.cols-2 {
        grid-template-columns: repeat(2, 1fr);
      }
      .team-members-grid.cols-3 {
        grid-template-columns: repeat(3, 1fr);
      }
    }
    @media (min-width: 1024px) {
      .team-members-grid.cols-1 {
        grid-template-columns: 1fr;
        max-width: 520px;
        margin: 0 auto;
      }
      .team-members-grid.cols-2 {
        grid-template-columns: repeat(2, 1fr);
      }
      .team-members-grid.cols-3 {
        grid-template-columns: repeat(3, 1fr);
      }
    }
    .member-card {
      background: linear-gradient(145deg, #18120D 0%, #100C08 100%);
      border: 1.5px solid var(--border-brass);
      border-radius: var(--radius-md);
      overflow: hidden;
      box-shadow: var(--shadow-wood);
      transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
      display: flex;
      flex-direction: column;
      position: relative;
    }
    .member-card:hover {
      transform: translateY(-8px);
      border-color: var(--accent-gold);
      box-shadow: 0 20px 42px rgba(0,0,0,0.85), 0 0 20px rgba(240, 167, 101, 0.25);
    }
    .member-card.leader {
      border-color: var(--accent-gold);
      box-shadow: 0 16px 40px rgba(0,0,0,0.8), 0 0 22px rgba(240, 167, 101, 0.3);
    }
    .member-card.leader:hover {
      border-color: var(--accent-gold-light);
      box-shadow: 0 22px 50px rgba(0,0,0,0.9), 0 0 28px rgba(240, 167, 101, 0.4);
    }
    .member-photo-frame {
      width: 100%;
      aspect-ratio: 4 / 5;
      overflow: hidden;
      position: relative;
      background: #080604;
      cursor: pointer;
    }
    .member-photo-img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: top center;
      display: block;
      transition: transform 0.45s ease;
    }
    .member-card:hover .member-photo-img {
      transform: scale(1.06);
    }
    .member-role-badge {
      position: absolute;
      top: 14px;
      left: 14px;
      background: rgba(13, 10, 7, 0.88);
      backdrop-filter: blur(8px);
      border: 1px solid var(--accent-gold);
      color: var(--accent-gold-light);
      font-size: 11.5px;
      font-weight: 800;
      letter-spacing: 0.8px;
      text-transform: uppercase;
      padding: 5px 12px;
      border-radius: 999px;
      z-index: 2;
      display: inline-flex;
      align-items: center;
      gap: 5px;
    }
    .member-role-badge.leader-badge {
      border-color: var(--accent-gold);
      background: linear-gradient(135deg, rgba(240,167,101,0.25) 0%, rgba(13,10,7,0.9) 100%);
      color: #FFF;
    }
    .member-role-badge.matcha-badge {
      border-color: var(--matcha-green);
      color: var(--matcha-bright);
    }
    .member-zoom-badge {
      position: absolute;
      bottom: 12px;
      right: 12px;
      background: rgba(0, 0, 0, 0.8);
      backdrop-filter: blur(5px);
      border: 1px solid rgba(255, 255, 255, 0.25);
      color: #fff;
      font-size: 11.5px;
      font-weight: 600;
      padding: 5px 10px;
      border-radius: 5px;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      pointer-events: none;
    }
    .member-info-content {
      padding: 20px 22px 24px;
      flex: 1;
      display: flex;
      flex-direction: column;
    }
    .member-name {
      font-family: var(--font-serif);
      font-size: 22px;
      font-weight: 700;
      color: var(--crema);
      margin-bottom: 4px;
      line-height: 1.3;
    }
    .member-dept {
      font-size: 12px;
      font-weight: 800;
      color: var(--accent-gold);
      text-transform: uppercase;
      letter-spacing: 0.8px;
      margin-bottom: 12px;
    }
    .member-dept.matcha {
      color: var(--matcha-bright);
    }
    .member-desc {
      font-size: 14px;
      color: var(--text-muted);
      line-height: 1.6;
    }

    /* Proof Cards for Social Content & Evidence */
    .social-showcase-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 24px;
      margin-bottom: 35px;
    }
    @media (min-width: 768px) {
      .social-showcase-grid {
        grid-template-columns: repeat(3, 1fr);
      }
    }
    .social-post-card {
      background: linear-gradient(145deg, #18120D 0%, #100C08 100%);
      border: 1.5px solid var(--border-brass);
      border-radius: var(--radius-md);
      overflow: hidden;
      box-shadow: var(--shadow-wood);
      transition: all 0.35s ease;
      display: flex;
      flex-direction: column;
      cursor: pointer;
    }
    .social-post-card:hover {
      transform: translateY(-6px);
      border-color: var(--accent-gold);
      box-shadow: 0 18px 40px rgba(0,0,0,0.85), 0 0 18px var(--accent-gold-glow);
    }
    .social-post-card.matcha:hover {
      border-color: var(--matcha-green);
      box-shadow: 0 18px 40px rgba(0,0,0,0.85), 0 0 18px var(--matcha-glow);
    }
    .social-post-media {
      width: 100%;
      aspect-ratio: 9 / 14;
      overflow: hidden;
      position: relative;
      background: #000;
    }
    .social-post-media.landscape {
      aspect-ratio: 16 / 10;
    }
    .social-post-img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: top center;
      display: block;
      transition: transform 0.4s ease;
    }
    .social-post-card:hover .social-post-img {
      transform: scale(1.05);
    }
    .social-card-body {
      padding: 18px 20px 22px;
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .social-card-title {
      font-size: 16px;
      font-weight: 700;
      color: var(--crema);
      margin-bottom: 8px;
      line-height: 1.4;
    }
    .social-card-desc {
      font-size: 13px;
      color: var(--text-muted);
      line-height: 1.5;
      margin-bottom: 12px;
    }
    .social-stat-chips {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-bottom: 12px;
    }
    .stat-chip {
      background: rgba(240, 167, 101, 0.12);
      border: 1px solid rgba(240, 167, 101, 0.25);
      color: var(--accent-gold-light);
      font-size: 11.5px;
      font-weight: 600;
      padding: 3px 8px;
      border-radius: 4px;
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }
    .stat-chip.matcha {
      background: rgba(46, 204, 113, 0.12);
      border-color: rgba(46, 204, 113, 0.3);
      color: var(--matcha-bright);
    }
    .stat-chip.highlight {
      background: rgba(46, 204, 113, 0.2);
      border-color: var(--matcha-green);
      color: #FFF;
      font-weight: 700;
    }

    /* 6-Week Evidence Showcase */
    .chart-evidence-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 24px;
      margin: 28px 0;
    }
    @media (min-width: 860px) {
      .chart-evidence-grid {
        grid-template-columns: 1.15fr 1fr;
      }
    }
    .chart-evidence-card {
      background: rgba(22, 17, 12, 0.9);
      border: 1.5px solid var(--border-brass);
      border-radius: var(--radius-md);
      overflow: hidden;
      box-shadow: var(--shadow-wood);
      cursor: pointer;
      transition: all 0.35s ease;
    }
    .chart-evidence-card:hover {
      transform: translateY(-5px);
      border-color: var(--accent-gold);
      box-shadow: 0 16px 36px rgba(0,0,0,0.8), 0 0 18px var(--accent-gold-glow);
    }
    .chart-evidence-media {
      position: relative;
      background: #000;
      overflow: hidden;
      aspect-ratio: 16 / 9;
    }
    .chart-evidence-img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.4s ease;
    }
    .chart-evidence-card:hover .chart-evidence-img {
      transform: scale(1.04);
    }
    .chart-evidence-info {
      padding: 16px 18px;
    }
    .chart-evidence-title {
      font-size: 15.5px;
      font-weight: 700;
      color: var(--crema);
      margin-bottom: 6px;
    }
    .chart-evidence-note {
      font-size: 13px;
      color: var(--text-muted);
      line-height: 1.45;
    }
    """

    full_css = base_css + "\n" + extra_css

    # Assemble HTML document
    html = """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover" />
  
  <title>Báo Cáo Cuối Kỳ: Chiến Dịch Truyền Thông Số | Nhóm 7 — Gỗ Xà Cừ • Olion Coffee</title>
  <meta name="title" content="Báo Cáo Cuối Kỳ: Chiến Dịch Truyền Thông Số | Nhóm 7 — Gỗ Xà Cừ • Olion Coffee" />
  <meta name="description" content="Báo cáo tổng kết học phần Truyền thông số (IMC) cho quán cà phê Olion Coffee: Tổng quan dự án, Persona, KPI đa kênh 6 tuần, Top content, Tuân thủ pháp lý và Kế hoạch 3 tháng." />
  <meta name="author" content="Nhóm 7 - Gỗ Xà Cừ (ĐH Văn Lang)" />
  <meta name="robots" content="noindex, nofollow, noarchive" />

  <!-- Open Graph -->
  <meta property="og:type" content="article" />
  <meta property="og:url" content="https://www.olioncoffee.app/cuoi-ky" />
  <meta property="og:title" content="Báo Cáo Cuối Kỳ: Chiến Dịch Truyền Thông Số | Olion Coffee" />
  <meta property="og:description" content="Báo cáo cuối kỳ Nhóm 7 — Gỗ Xà Cừ: Đánh giá hiệu quả 6 tuần truyền thông số cho quán cà phê Olion Coffee." />
  <meta property="og:image" content="https://www.olioncoffee.app/assets/cuoi-ky/chart-followers-6tuan.webp" />
  <link rel="canonical" href="https://www.olioncoffee.app/cuoi-ky" />
  <link rel="icon" href="assets/logo-transparent.webp" type="image/webp" />

  <!-- Google Fonts: Cormorant Garamond, Plus Jakarta Sans, Playfair Display -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,400;1,600;1,700&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;1,600&display=swap" rel="stylesheet" />

  <!-- Lucide Icons & Chart.js -->
  <script src="https://unpkg.com/lucide@latest"></script>
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

  <style>
__CSS__
  </style>
</head>
<body>

  <!-- Reading Progress Bar -->
  <div class="scroll-progress-line" id="progressBar"></div>

  <!-- Trailing Matcha Leaf Cursor Following Mouse -->
  <svg id="matchaLeafTrail" viewBox="0 0 28 28">
    <path d="M14 2 C14 2 24 7 22 19 C20.5 25 15.5 26 14 26 C12.5 26 7.5 25 6 19 C4 7 14 2 14 2 Z" fill="#2ECC71" stroke="#0F3B20" stroke-width="1.5"/>
    <path d="M14 4 Q14 16 14 24" stroke="#0F3B20" stroke-width="1.5" stroke-linecap="round"/>
    <circle cx="14" cy="3" r="1.5" fill="#FFF"/>
  </svg>

  <!-- Ambient Steam Canvas -->
  <canvas id="cafeCanvas"></canvas>

  <div class="toast-box" id="toast">
    <i data-lucide="check-circle" style="width:16px;height:16px;color:var(--matcha-green);"></i>
    <span id="toastMsg">Đã sao chép link báo cáo!</span>
  </div>

  <!-- Photo Lightbox Modal -->
  <div class="photo-lightbox" id="photoLightbox" onclick="closeLightbox()">
    <div class="photo-lightbox-inner" onclick="event.stopPropagation()">
      <button type="button" class="lightbox-close-btn" onclick="closeLightbox()" aria-label="Đóng ảnh">
        <i data-lucide="x" style="width:18px;height:18px;"></i>
      </button>
      <img src="" alt="Olion Coffee Report" id="lightboxImg" class="lightbox-img" />
      <div class="lightbox-foot">
        <span id="lightboxCaption">Báo Cáo Cuối Kỳ</span>
        <span style="font-size:14px;color:var(--text-muted);">Nhóm 7 — Gỗ Xà Cừ • Olion Coffee</span>
      </div>
    </div>
  </div>

  <!-- ========================================================
       TOP HEADER & ĐIỀU HƯỚNG CỐ ĐỊNH (CHUẨN CAMPAIGN REPORT)
       ======================================================== -->
  <header class="cafe-header">
    <div class="shell header-inner">
      <div class="header-brand">
        <a href="/" title="Trang chủ Olion Coffee">
          <img src="assets/logo-white.webp" alt="Olion Coffee" onerror="this.src='assets/logo-transparent.webp'" />
        </a>
        <div class="header-brand-divider"></div>
        <div class="header-badge-hub">
          <span class="badge-hub-title">BÁO CÁO CUỐI KỲ</span>
          <span class="badge-hub-sub">Nhóm 7: Gỗ Xà Cừ (ĐH Văn Lang)</span>
        </div>
      </div>

      <!-- Navigation Menu Strictly Follows 9 Sections -->
      <nav class="header-menu-nav" aria-label="Menu điều hướng báo cáo cuối kỳ">
        <a href="#muc-1" class="menu-link active" title="1. Tổng quan &amp; Định vị">1. Tổng Quan</a>
        <a href="#muc-2" class="menu-link" title="2. Persona Đoàn Minh Trang">2. Persona</a>
        <a href="#muc-3" class="menu-link" title="3. KPI kế hoạch vs thực tế">3. KPI Dự Án</a>
        <a href="#muc-4" class="menu-link" title="4. Tăng trưởng 6 tuần">4. Tăng Trưởng</a>
        <a href="#muc-5" class="menu-link" title="5. Sản phẩm nổi bật">5. Top Content</a>
        <a href="#muc-6" class="menu-link" title="6. Đánh giá &amp; Bài học">6. Đánh Giá</a>
        <a href="#muc-7" class="menu-link" title="7. Tuân thủ pháp lý">7. Pháp Lý</a>
        <a href="#muc-8" class="menu-link" title="8. Kế hoạch 3 tháng">8. Kế Hoạch</a>
        <a href="#muc-9" class="menu-link" title="9. Thành viên Nhóm 7">9. Thành Viên</a>
      </nav>

      <div class="header-actions">
        <button type="button" class="action-btn-icon" onclick="copyLink()" title="Sao chép liên kết">
          <i data-lucide="share-2" style="width:15px;height:15px;"></i>
        </button>
        <button type="button" class="action-btn-icon" onclick="window.print()" title="In báo cáo">
          <i data-lucide="printer" style="width:15px;height:15px;"></i>
        </button>
        <a href="/" class="btn-home-link desktop-only">
          <i data-lucide="home" style="width:14px;height:14px;"></i>
          <span>Trang Chủ Olion</span>
        </a>
        <button type="button" class="mobile-menu-btn" onclick="toggleDrawer()" aria-label="Menu">
          <i data-lucide="menu" style="width:18px;height:18px;"></i>
        </button>
      </div>
    </div>
  </header>

  <!-- Mobile Menu Drawer -->
  <div class="mobile-nav-drawer" id="mobileDrawer">
    <a href="#muc-1" class="mobile-nav-link" onclick="toggleDrawer()"><span>1. Tổng quan &amp; Định vị thương hiệu</span><i data-lucide="chevron-right" style="width:14px;height:14px;"></i></a>
    <a href="#muc-2" class="mobile-nav-link" onclick="toggleDrawer()"><span>2. Chân dung khách hàng (Persona)</span><i data-lucide="chevron-right" style="width:14px;height:14px;"></i></a>
    <a href="#muc-3" class="mobile-nav-link" onclick="toggleDrawer()"><span>3. KPI kế hoạch vs thực tế</span><i data-lucide="chevron-right" style="width:14px;height:14px;"></i></a>
    <a href="#muc-4" class="mobile-nav-link" onclick="toggleDrawer()"><span>4. Tăng trưởng số liệu qua 6 tuần</span><i data-lucide="chevron-right" style="width:14px;height:14px;"></i></a>
    <a href="#muc-5" class="mobile-nav-link" onclick="toggleDrawer()"><span>5. Sản phẩm truyền thông nổi bật &amp; demo</span><i data-lucide="chevron-right" style="width:14px;height:14px;"></i></a>
    <a href="#muc-6" class="mobile-nav-link" onclick="toggleDrawer()"><span>6. Đánh giá tổng quan &amp; Bài học</span><i data-lucide="chevron-right" style="width:14px;height:14px;"></i></a>
    <a href="#muc-7" class="mobile-nav-link" onclick="toggleDrawer()"><span>7. Tuân thủ pháp lý (12 tiêu chí)</span><i data-lucide="chevron-right" style="width:14px;height:14px;"></i></a>
    <a href="#muc-8" class="mobile-nav-link" onclick="toggleDrawer()"><span>8. Kế hoạch tiếp tục &amp; Mục tiêu 3 tháng</span><i data-lucide="chevron-right" style="width:14px;height:14px;"></i></a>
    <a href="#muc-9" class="mobile-nav-link" onclick="toggleDrawer()"><span>9. Phân vai thành viên Nhóm 7 (Gỗ Xà Cừ)</span><i data-lucide="chevron-right" style="width:14px;height:14px;"></i></a>
  </div>

  <!-- ========================================================
       HERO BANNER CHÍNH THỨC
       ======================================================== -->
  <section class="hero-section">
    <div class="shell">
      <div class="hero-eyebrow">
        <span class="dot"></span>
        <span>BÁO CÁO TỔNG KẾT HỌC PHẦN TRUYỀN THÔNG SỐ (IMC) &bull; ĐẠI HỌC VĂN LANG</span>
      </div>

      <h1 class="hero-title">
        Báo Cáo Cuối Kỳ: Chiến Dịch Truyền Thông Số<br />
        <span class="text-matcha">Olion Coffee — Quán Cà Phê Máy Lạnh Cho Sinh Viên</span>
      </h1>

      <p class="hero-lead">
        Chiến dịch truyền thông số đa kênh (Facebook, Instagram, TikTok &amp; Landing Page) triển khai thực tế qua 6 tuần bởi <strong>Nhóm 7 — Gỗ Xà Cừ</strong>. Mục tiêu xây dựng nhận diện thương hiệu, kết nối sinh viên ĐH Văn Lang và tối ưu chuyển đổi khách hàng.
      </p>

      <!-- Slogan Callout Box -->
      <div style="background:rgba(24,19,14,0.85);border:1.5px solid var(--border-brass);border-radius:var(--radius-md);padding:18px 24px;margin-bottom:28px;display:inline-block;box-shadow:var(--shadow-wood);">
        <span style="font-size:12px;font-weight:800;color:var(--accent-gold);text-transform:uppercase;letter-spacing:1px;display:block;margin-bottom:4px;">✨ Thông Điệp Cốt Lõi Thương Hiệu (Core Message)</span>
        <span style="font-family:var(--font-serif);font-size:20px;font-style:italic;color:var(--crema);">“Take your time. Find your moment. Begin again.”</span>
        <span style="display:block;font-size:13px;color:var(--text-muted);margin-top:4px;">(Hãy cứ thong thả. Tìm lấy khoảnh khắc của riêng mình. Và bắt đầu lại.)</span>
      </div>

      <!-- Hero Stat Strip -->
      <div class="hero-stat-strip">
        <div class="hero-stat-item">
          <div class="hero-stat-num text-gold">6 Tuần</div>
          <div class="hero-stat-lbl">Thời Gian Triển Khai</div>
        </div>
        <div class="hero-stat-item">
          <div class="hero-stat-num text-matcha">4 Kênh</div>
          <div class="hero-stat-lbl">FB, IG, TikTok, Landing Page</div>
        </div>
        <div class="hero-stat-item">
          <div class="hero-stat-num text-gold">15.656+</div>
          <div class="hero-stat-lbl">Tổng Lượt Tiếp Cận (Reach)</div>
        </div>
        <div class="hero-stat-item">
          <div class="hero-stat-num text-matcha">11</div>
          <div class="hero-stat-lbl">Thành Viên Nhóm 7 (Gỗ Xà Cừ)</div>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================================
       MỤC 1: TỔNG QUAN DỰ ÁN & ĐỊNH VỊ
       ======================================================== -->
  <section class="report-section" id="muc-1">
    <div class="shell">
      <div class="section-chapter-tag">1. TỔNG QUAN DỰ ÁN &amp; ĐỊNH VỊ</div>
      <h2 class="section-main-heading">1. Tổng Quan Dự Án &amp; Định Vị Thương Hiệu</h2>
      <p style="color:var(--text-muted);margin-bottom:24px;font-size:15px;">
        Nghiên cứu thị trường và định vị thương hiệu Olion Coffee — quán cà phê máy lạnh lý tưởng dành riêng cho sinh viên Đại học Văn Lang.
      </p>

      <div class="report-two-cols">
        <!-- Cột trái: Mô hình & Định vị -->
        <div class="report-card">
          <div class="card-tag gold">MÔ HÌNH &amp; SẢN PHẨM</div>
          <h3 class="card-title">Mô Hình Cà Phê Sinh Viên Tiện Ích</h3>
          <ul class="clean-list">
            <li><strong>Sản phẩm chủ đạo:</strong> Cà phê pha máy, Trà trái cây tươi, Sữa chua (Yogurt), Matcha Series cao cấp, Cacao đậm vị.</li>
            <li><strong>Dịch vụ cung cấp:</strong> Quán cà phê máy lạnh mát mẻ, yên tĩnh, trang bị ổ cắm điện, wifi tốc độ cao phục vụ học nhóm, làm bài, chạy deadline.</li>
            <li><strong>Mô hình kinh doanh:</strong> Thoải mái, ngon, giá vừa túi tiền sinh viên (35.000đ - 45.000đ).</li>
            <li><strong>Địa điểm đắc địa:</strong> 80/64a Dương Quảng Hàm, An Nhơn, TP.HCM — nằm ngay sát cổng trường ĐH Văn Lang cơ sở 3 (Gò Vấp).</li>
          </ul>
        </div>

        <!-- Cột phải: Vấn đề & Khác biệt -->
        <div class="report-card">
          <div class="card-tag matcha">VẤN ĐỀ &amp; GIẢI PHÁP</div>
          <h3 class="card-title">Lợi Ích Khác Biệt &amp; Lý Do Để Tin</h3>
          <ul class="clean-list">
            <li><strong>Vấn đề sinh viên gặp phải:</strong> Quanh trường menu đại trà, vị ngọt gắt công nghiệp; quán xá ồn ào, thiếu chỗ ngồi giờ cao điểm giữa ca.</li>
            <li><strong>Lợi ích khác biệt tại Olion:</strong> Đồ uống chất lượng đặc trưng, công thức riêng; không gian máy lạnh mát mẻ, phục vụ nhanh, giá sinh viên.</li>
            <li><strong>Lý do để tin (Reason to Believe):</strong> Đã khảo sát thực tế sinh viên VLU; nhân viên am hiểu chuyên sâu, nhiệt tình, thân thiện như bạn bè.</li>
            <li><strong>Uy tín thương hiệu:</strong> Được bạn bè truyền miệng giới thiệu, kiểm chứng chất lượng qua trải nghiệm thực tế.</li>
          </ul>
        </div>
      </div>

      <!-- Trích dẫn bối cảnh sinh viên VLU -->
      <div class="reason-box" style="margin-top:24px;border-left-color:var(--matcha-green);">
        <h4 style="color:var(--matcha-green);font-size:16px;margin-bottom:8px;">
          <i data-lucide="sparkles" style="width:16px;height:16px;"></i> Định Vị Trọng Tâm Dành Cho Sinh Viên ĐH Văn Lang:
        </h4>
        <p style="font-size:14.5px;line-height:1.65;color:var(--crema);">
          Đối với sinh viên đang học tại trường ĐH VLU, các bạn thường mệt mỏi vì áp lực bài vở và thời tiết ngột ngạt. Vậy nên các bạn cần một chỗ nghỉ ngơi mát mẻ để vừa chạy deadline vừa trò chuyện thoải mái mà không lo về giá. <strong>Olion Coffee</strong> là quán cafe không gian máy lạnh, cung cấp không gian để học nhóm, nghỉ ngơi, giải toả áp lực nằm ngay sát trường, mang lại khoảng thời gian nghỉ ngơi mát mẻ, nạp đầy năng lượng và sẵn sàng bắt đầu lại.
        </p>
      </div>
    </div>
  </section>

  <!-- ========================================================
       MỤC 2: CHÂN DUNG KHÁCH HÀNG (PERSONA)
       ======================================================== -->
  <section class="report-section" id="muc-2">
    <div class="shell">
      <div class="section-chapter-tag matcha">2. CHÂN DUNG KHÁCH HÀNG (PERSONA)</div>
      <h2 class="section-main-heading">2. Chân Dung Khách Hàng Mục Tiêu: Đoàn Minh Trang</h2>
      <p style="color:var(--text-muted);margin-bottom:24px;font-size:15px;">
        Đại diện cho nhóm khách hàng sinh viên năm 3 Đại học Văn Lang có nhu cầu học tập, thư giãn và tiêu dùng đồ uống chất lượng.
      </p>

      <div class="persona-layout-grid">
        <!-- Cột Trái: Chân Dung Khung Ảnh VIP -->
        <div class="persona-photo-col" onclick="openLightbox('assets/cuoi-ky/persona-doan-minh-trang.webp?v=20261113', 'Persona: Đoàn Minh Trang (Sinh viên năm 3 ĐH Văn Lang)', 'Khách quen tại Olion Coffee — Thưởng thức đồ uống và chạy deadline')">
          <div class="persona-photo-wrapper">
            <div class="persona-photo-live-badge">
              <i data-lucide="star" style="width:12px;height:12px;color:var(--accent-gold);fill:var(--accent-gold);"></i> KHÁCH MỤC TIÊU VLU
            </div>
            <div class="persona-photo-zoom-btn" title="Phóng to ảnh">
              <i data-lucide="zoom-in" style="width:14px;height:14px;"></i>
            </div>
            <img src="assets/cuoi-ky/persona-doan-minh-trang.webp?v=20261113" alt="Persona Đoàn Minh Trang" class="persona-main-img" />
          </div>
          <div class="persona-photo-caption">
            <strong>Đoàn Minh Trang</strong> &bull; Sinh viên năm 3 ĐH Văn Lang
          </div>
        </div>

        <!-- Cột Phải: Bảng Chi Tiết Hành Vi & Nhu Cầu -->
        <div class="persona-details-col">
          <div class="persona-row-item">
            <div class="row-icon-box"><i data-lucide="smartphone" style="width:18px;height:18px;color:var(--accent-gold);"></i></div>
            <div class="row-text-content">
              <div class="row-label">Hành vi số</div>
              <div class="row-value">Lướt TikTok xem review đồ uống hot trend, tìm quán thông qua giới thiệu của bạn bè và đánh giá mạng xã hội.</div>
            </div>
          </div>

          <div class="persona-row-item">
            <div class="row-icon-box"><i data-lucide="target" style="width:18px;height:18px;color:var(--matcha-green);"></i></div>
            <div class="row-text-content">
              <div class="row-label">Mục tiêu</div>
              <div class="row-value">Mua đi nhanh gọn trước giờ học, có không gian mát mẻ để trò chuyện với bạn bè giữa ca và thỉnh thoảng cắm máy chạy deadline.</div>
            </div>
          </div>

          <div class="persona-row-item">
            <div class="row-icon-box"><i data-lucide="alert-circle" style="width:18px;height:18px;color:#E74C3C;"></i></div>
            <div class="row-text-content">
              <div class="row-label">Nỗi đau (Pain point)</div>
              <div class="row-value">Menu các quán quanh trường đại trà, pha chế ngọt gắt công nghiệp, chưa có sự đột phá hay thức uống sáng tạo.</div>
            </div>
          </div>

          <div class="persona-row-item">
            <div class="row-icon-box"><i data-lucide="shield-alert" style="width:18px;height:18px;color:var(--accent-gold);"></i></div>
            <div class="row-text-content">
              <div class="row-label">Rào cản</div>
              <div class="row-value">Sợ nước uống không hợp khẩu vị mà giá lại đắt; ngại những quán ồn ào không thể tập trung làm bài.</div>
            </div>
          </div>

          <div class="persona-row-item">
            <div class="row-icon-box"><i data-lucide="heart" style="width:18px;height:18px;color:var(--matcha-green);"></i></div>
            <div class="row-text-content">
              <div class="row-label">Tin vào</div>
              <div class="row-value">Lời giới thiệu chân thật từ bạn bè thân thiết và trải nghiệm thực tế người thật việc thật.</div>
            </div>
          </div>

          <!-- Quote Persona -->
          <div class="persona-quote-callout">
            <i data-lucide="quote" style="width:20px;height:20px;color:var(--accent-gold);margin-bottom:6px;"></i>
            <p>“Giá có thể cao một chút nhưng phải ngon, có chỗ ngồi thoải mái để nghỉ ngơi, làm bài, nói chuyện với bạn khi rảnh.”</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================================
       MỤC 3: KPI DỰ ÁN & KẾT QUẢ ĐẠT ĐƯỢC
       ======================================================== -->
  <section class="report-section" id="muc-3">
    <div class="shell">
      <div class="section-chapter-tag">3. KPI DỰ ÁN &amp; KẾT QUẢ ĐẠT ĐƯỢC</div>
      <h2 class="section-main-heading">3. Mục Tiêu KPI Kế Hoạch &amp; Kết Quả Thực Tế Từng Kênh</h2>
      <p style="color:var(--text-muted);margin-bottom:24px;font-size:15px;">
        Sau 6 tuần thực hiện truyền thông số cho quán cà phê Olion, nhóm tổng hợp các chỉ số đạt được so với kế hoạch ban đầu trên 4 nền tảng.
      </p>

      <!-- Metric Strip 4 Kênh -->
      <div class="round-metric-strip">
        <div class="metric-strip-card">
          <div class="metric-strip-lbl"><i data-lucide="facebook" style="width:14px;height:14px;color:var(--accent-gold);"></i> FACEBOOK FANPAGE</div>
          <div class="metric-strip-val text-gold">665 Tương Tác</div>
          <div class="metric-strip-sub text-matcha">✓ Vượt KPI 110,8% (KPI 600)</div>
        </div>

        <div class="metric-strip-card highlight">
          <div class="metric-strip-lbl"><i data-lucide="video" style="width:14px;height:14px;color:var(--matcha-green);"></i> TIKTOK CHANNEL 🏆</div>
          <div class="metric-strip-val text-matcha">14.617 Người Xem</div>
          <div class="metric-strip-sub text-matcha">Like 115,1% &bull; Share 110,6%</div>
        </div>

        <div class="metric-strip-card">
          <div class="metric-strip-lbl"><i data-lucide="instagram" style="width:14px;height:14px;color:#E1306C;"></i> INSTAGRAM</div>
          <div class="metric-strip-val">1.186 Tương Tác</div>
          <div class="metric-strip-sub">3.301 người xem (66% KPI)</div>
        </div>

        <div class="metric-strip-card">
          <div class="metric-strip-lbl"><i data-lucide="globe" style="width:14px;height:14px;color:var(--accent-gold-light);"></i> LANDING PAGE</div>
          <div class="metric-strip-val text-gold">381 Visits</div>
          <div class="metric-strip-sub">Đạt 76,2% chỉ tiêu 500</div>
        </div>
      </div>

      <!-- Bảng KPI Kế Hoạch vs Thực Tế -->
      <div class="table-container">
        <table class="pdf-table">
          <thead>
            <tr>
              <th>Kênh truyền thông</th>
              <th>Chỉ số đo lường</th>
              <th>KPI Kế hoạch</th>
              <th>Thực tế đạt</th>
              <th>Tỷ lệ hoàn thành</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td rowspan="4" style="font-weight:700;color:var(--crema);"><i data-lucide="facebook" style="width:14px;height:14px;display:inline;vertical-align:middle;margin-right:4px;"></i> Facebook Fanpage</td>
              <td>Tổng người theo dõi (Followers)</td>
              <td>1.000</td>
              <td>100</td>
              <td>10,0%</td>
            </tr>
            <tr>
              <td>Người xem (Reach)</td>
              <td>1.000</td>
              <td>853</td>
              <td>85,3%</td>
            </tr>
            <tr>
              <td>Lượt tương tác (Engagement)</td>
              <td>600</td>
              <td class="avg-cell highlight-cell">665</td>
              <td class="avg-cell highlight-cell" style="color:var(--matcha-green);font-weight:800;">110,8% (Vượt KPI) ✓</td>
            </tr>
            <tr>
              <td>Truy cập Landing Page từ Facebook</td>
              <td>100</td>
              <td>35</td>
              <td>35,0%</td>
            </tr>

            <tr style="border-top:2px solid var(--border-brass);">
              <td rowspan="4" style="font-weight:700;color:var(--crema);"><i data-lucide="instagram" style="width:14px;height:14px;display:inline;vertical-align:middle;margin-right:4px;"></i> Instagram</td>
              <td>Tổng người theo dõi (Followers)</td>
              <td>1.000</td>
              <td>142</td>
              <td>14,2%</td>
            </tr>
            <tr>
              <td>Người xem (Reach)</td>
              <td>5.000</td>
              <td>3.301</td>
              <td>66,0%</td>
            </tr>
            <tr>
              <td>Lượt tương tác (Engagement)</td>
              <td>2.000</td>
              <td>1.186</td>
              <td>59,3%</td>
            </tr>
            <tr>
              <td>Truy cập Landing Page từ Instagram</td>
              <td>100</td>
              <td>3</td>
              <td>3,0%</td>
            </tr>

            <tr style="border-top:2px solid var(--border-brass);">
              <td rowspan="6" style="font-weight:700;color:var(--matcha-green);"><i data-lucide="video" style="width:14px;height:14px;display:inline;vertical-align:middle;margin-right:4px;"></i> TikTok 🏆</td>
              <td>Tổng người theo dõi (Followers)</td>
              <td>1.000</td>
              <td>280</td>
              <td>28,0%</td>
            </tr>
            <tr>
              <td>Tổng số người xem (Video Views)</td>
              <td>15.000</td>
              <td>14.617</td>
              <td>97,4%</td>
            </tr>
            <tr>
              <td>Lượt thích (Likes)</td>
              <td>1.000</td>
              <td class="avg-cell highlight-cell">1.151</td>
              <td class="avg-cell highlight-cell" style="color:var(--matcha-green);font-weight:800;">115,1% (Vượt KPI) ✓</td>
            </tr>
            <tr>
              <td>Lượt bình luận (Comments)</td>
              <td>400</td>
              <td>289</td>
              <td>72,3%</td>
            </tr>
            <tr>
              <td>Lượt chia sẻ (Shares)</td>
              <td>500</td>
              <td class="avg-cell highlight-cell">553</td>
              <td class="avg-cell highlight-cell" style="color:var(--matcha-green);font-weight:800;">110,6% (Vượt KPI) ✓</td>
            </tr>
            <tr>
              <td>Truy cập Landing Page từ TikTok</td>
              <td>100</td>
              <td>0</td>
              <td>0,0%</td>
            </tr>

            <tr style="border-top:2px solid var(--border-brass);">
              <td style="font-weight:700;color:var(--crema);"><i data-lucide="globe" style="width:14px;height:14px;display:inline;vertical-align:middle;margin-right:4px;"></i> Landing Page</td>
              <td>Lượt truy cập (Visits - Cloudflare Analytics)</td>
              <td>500</td>
              <td class="avg-cell">381</td>
              <td class="avg-cell" style="font-weight:700;color:var(--accent-gold);">76,2%</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Hộp Nhận Xét Tự Động -->
      <div class="auto-note-box">
        <strong>Đánh giá thực tế từ nhóm thực hiện:</strong><br />
        ✓ <strong>TikTok là kênh bùng nổ mạnh nhất:</strong> Tổng người xem đạt 14.617/15.000 (97,4%), lượt thích (1.151) và lượt chia sẻ (553) đều vượt kế hoạch.<br />
        ✓ <strong>Facebook tương tác chất lượng:</strong> Lượt tương tác đạt 665 vượt mục tiêu 600 (110,8%).<br />
        ℹ <strong>Bài học về điều hướng:</strong> Hoạt động truyền thông thu hút tương tác tốt trên mạng xã hội, nhưng tỷ lệ click link kéo về Landing Page còn hạn chế do người dùng quen tiêu thụ nội dung tại chỗ.
      </div>
    </div>
  </section>

  <!-- ========================================================
       MỤC 4: TĂNG TRƯỞNG SỐ LIỆU QUA 6 TUẦN
       ======================================================== -->
  <section class="report-section" id="muc-4">
    <div class="shell">
      <div class="section-chapter-tag matcha">4. TĂNG TRƯỞNG QUA 6 TUẦN</div>
      <h2 class="section-main-heading">4. Theo Dõi &amp; Đánh Giá Tăng Trưởng Qua 6 Tuần</h2>
      <p style="color:var(--text-muted);margin-bottom:24px;font-size:15px;">
        Dữ liệu theo dõi định kỳ hàng tuần cho thấy lộ trình phát triển rõ rệt của từng nền tảng, đặc biệt là sự bứt phá của TikTok và Landing Page ở tuần 4.
      </p>

      <!-- Bộ 2 Ảnh Minh Chứng Biểu Đồ từ Báo Cáo Gốc (Evidence Screenshots) -->
      <div class="proof-showcase-box matcha-theme">
        <div class="proof-showcase-header matcha-theme">
          <div class="proof-header-left">
            <span class="proof-header-badge matcha"><i data-lucide="image" style="width:13px;height:13px;"></i> ẢNH MINH CHỨNG TÀI LIỆU</span>
            <h3 class="proof-header-title">Biểu Đồ Theo Dõi Tăng Trưởng Trích Xuất Từ Báo Cáo</h3>
          </div>
          <div class="proof-header-hint"><i data-lucide="zoom-in" style="width:13px;height:13px;"></i> Nhấp ảnh để phóng to chi tiết</div>
        </div>

        <div class="chart-evidence-grid">
          <!-- Ảnh Minh Chứng 1: Biểu đồ người theo dõi -->
          <div class="chart-evidence-card" onclick="openLightbox('assets/cuoi-ky/chart-followers-6tuan.webp', 'Biểu đồ biến động người theo dõi trên Facebook, Instagram và TikTok qua các tuần', 'Trích từ tài liệu Báo cáo cuối kỳ Nhóm 7 — Gỗ Xà Cừ')">
            <div class="chart-evidence-media">
              <img src="assets/cuoi-ky/chart-followers-6tuan.webp" alt="Biểu đồ biến động người theo dõi 6 tuần" class="chart-evidence-img" />
              <div class="proof-card-zoom-badge"><i data-lucide="zoom-in" style="width:11px;height:11px;"></i> Phóng to</div>
            </div>
            <div class="chart-evidence-info">
              <div class="chart-evidence-title">📈 Biểu đồ biến động Follower qua 6 tuần</div>
              <div class="chart-evidence-note">Facebook tăng từ 50 lên 100 followers; Instagram tăng từ 55 lên 142 followers; TikTok bứt phá mạnh nhất đạt 275 followers ở tuần 4.</div>
            </div>
          </div>

          <!-- Ảnh Minh Chứng 2: Biểu đồ Landing page visits -->
          <div class="chart-evidence-card" onclick="openLightbox('assets/cuoi-ky/chart-landing-page-visits-6tuan.webp', 'Lượt truy cập Landing Page theo từng tuần (Cloudflare Analytics)', 'Trích từ tài liệu Báo cáo cuối kỳ Nhóm 7 — Gỗ Xà Cừ')">
            <div class="chart-evidence-media">
              <img src="assets/cuoi-ky/chart-landing-page-visits-6tuan.webp" alt="Biểu đồ lượt truy cập Landing Page qua 6 tuần" class="chart-evidence-img" />
              <div class="proof-card-zoom-badge"><i data-lucide="zoom-in" style="width:11px;height:11px;"></i> Phóng to</div>
            </div>
            <div class="chart-evidence-info">
              <div class="chart-evidence-title">📊 Lượt truy cập Landing Page theo tuần</div>
              <div class="chart-evidence-note">Tuần 1-2 chưa có traffic; Tuần 3 đạt 30 visits; Tuần 4 bùng nổ 280 visits (sau khi gắn link FB); Tuần 5 duy trì 51 visits. Tổng 381 visits.</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Biểu Đồ Tương Tác Động Chart.js -->
      <div style="background:rgba(22,17,12,0.92);border:1.5px solid var(--border-brass);border-radius:var(--radius-md);padding:26px;margin:28px 0;box-shadow:var(--shadow-wood);">
        <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:18px;flex-wrap:wrap;gap:10px;">
          <h4 style="font-family:var(--font-serif);font-size:20px;color:var(--crema);margin:0;">
            <i data-lucide="activity" style="width:18px;height:18px;color:var(--matcha-green);display:inline;vertical-align:middle;margin-right:6px;"></i>
            Mô Hình Hóa Dữ Liệu Tăng Trưởng 6 Tuần (Interactive Chart)
          </h4>
          <span style="font-size:12px;color:var(--text-muted);">Di chuột vào từng điểm mốc để xem chi tiết</span>
        </div>
        <div style="height:360px;position:relative;">
          <canvas id="growthInteractiveChart"></canvas>
        </div>
      </div>

      <!-- Bảng Tổng Hợp Follower & Visits Theo Tuần -->
      <h3 style="font-family:var(--font-serif);font-size:20px;color:var(--accent-gold);margin:24px 0 12px;">Bảng số liệu người theo dõi &amp; lượt truy cập theo tuần:</h3>
      <div class="table-container">
        <table class="pdf-table">
          <thead>
            <tr>
              <th>Giai đoạn</th>
              <th>Facebook followers</th>
              <th>Instagram followers</th>
              <th>TikTok followers</th>
              <th>Landing Page Visits</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Tuần 1</td>
              <td>50</td>
              <td>55</td>
              <td>60</td>
              <td>0</td>
            </tr>
            <tr>
              <td>Tuần 2</td>
              <td>56</td>
              <td>64</td>
              <td>73</td>
              <td>0</td>
            </tr>
            <tr>
              <td>Tuần 3</td>
              <td>66</td>
              <td>79</td>
              <td>137</td>
              <td>20</td>
            </tr>
            <tr style="background:rgba(46,204,113,0.08);">
              <td style="color:var(--matcha-bright);font-weight:700;">Tuần 4 (Bứt phá) 🚀</td>
              <td style="color:var(--matcha-bright);font-weight:700;">79</td>
              <td style="color:var(--matcha-bright);font-weight:700;">119</td>
              <td style="color:var(--matcha-bright);font-weight:700;">275</td>
              <td style="color:var(--matcha-bright);font-weight:800;font-size:15px;">280 (Cao nhất)</td>
            </tr>
            <tr>
              <td>Tuần 5</td>
              <td>82</td>
              <td>122</td>
              <td>261</td>
              <td>81</td>
            </tr>
            <tr>
              <td style="font-weight:700;color:var(--accent-gold);">Tuần 6 (Chốt chiến dịch)</td>
              <td class="avg-cell highlight-cell">100</td>
              <td class="avg-cell highlight-cell">142</td>
              <td class="avg-cell highlight-cell">282</td>
              <td class="avg-cell">10</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>

  <!-- ========================================================
       MỤC 5: SẢN PHẨM TRUYỀN THÔNG NỔI BẬT & DEMO
       ======================================================== -->
  <section class="report-section" id="muc-5">
    <div class="shell">
      <div class="section-chapter-tag">5. SẢN PHẨM TRUYỀN THÔNG NỔI BẬT</div>
      <h2 class="section-main-heading">5. Sản Phẩm Truyền Thông Nổi Bật &amp; Minh Chứng Thực Tế</h2>
      <p style="color:var(--text-muted);margin-bottom:28px;font-size:15px;">
        Tổng hợp 9 sản phẩm truyền thông tiêu biểu nhất trên Facebook, Instagram và TikTok cùng số liệu tương tác thực tế và hình ảnh minh chứng.
      </p>

      <!-- 1. KÊNH FACEBOOK -->
      <div style="margin-bottom:45px;">
        <h3 style="font-family:var(--font-serif);font-size:24px;color:var(--accent-gold);margin-bottom:16px;display:flex;align-items:center;gap:10px;">
          <i data-lucide="facebook" style="width:22px;height:22px;"></i> Kênh Facebook Fanpage — Trọng Tâm Nhận Diện &amp; Hương Vị
        </h3>
        <div class="social-showcase-grid">
          <!-- FB 1 -->
          <div class="social-post-card" onclick="openLightbox('assets/cuoi-ky/fb-post-1-matcha-que-hoa-cacao-bac-ha.webp', 'Facebook: Matcha Quế Hoa &amp; Cacao Bạc Hà', 'Bài đăng giới thiệu hương vị sản phẩm (gắn nhãn AI) — 57 tương tác')">
            <div class="social-post-media landscape">
              <img src="assets/cuoi-ky/fb-post-1-matcha-que-hoa-cacao-bac-ha.webp" alt="Matcha Quế Hoa và Cacao Bạc Hà" class="social-post-img" />
              <div class="proof-card-zoom-badge"><i data-lucide="zoom-in" style="width:11px;height:11px;"></i> Phóng to</div>
            </div>
            <div class="social-card-body">
              <div>
                <div class="social-card-title">Sản phẩm 1: Matcha Quế Hoa &amp; Cacao Bạc Hà</div>
                <div class="social-card-desc">Bài đăng giới thiệu 2 thức uống bằng hình ảnh sản phẩm và thông tin hương vị đặc trưng để giữ năng lượng cho ngày dài (có gắn nhãn AI).</div>
                <div class="social-stat-chips">
                  <span class="stat-chip"><i data-lucide="thumbs-up" style="width:11px;height:11px;"></i> 35 thích</span>
                  <span class="stat-chip"><i data-lucide="message-circle" style="width:11px;height:11px;"></i> 21 bình luận</span>
                  <span class="stat-chip"><i data-lucide="share-2" style="width:11px;height:11px;"></i> 1 share</span>
                  <span class="stat-chip highlight">Tổng: 57 tương tác</span>
                </div>
              </div>
            </div>
          </div>

          <!-- FB 2 -->
          <div class="social-post-card" onclick="openLightbox('assets/cuoi-ky/fb-post-2-luc-tra-nhan-tra-xoai-chanh-day.webp', 'Facebook: Lục Trà Nhãn &amp; Trà Xoài Chanh Dây', 'Bài đăng dạng câu hỏi lựa chọn với hình ảnh nhân viên cầm ly thực tế — 31 tương tác')">
            <div class="social-post-media">
              <img src="assets/cuoi-ky/fb-post-2-luc-tra-nhan-tra-xoai-chanh-day.webp" alt="Lục Trà Nhãn và Trà Xoài Chanh Dây" class="social-post-img" />
              <div class="proof-card-zoom-badge"><i data-lucide="zoom-in" style="width:11px;height:11px;"></i> Phóng to</div>
            </div>
            <div class="social-card-body">
              <div>
                <div class="social-card-title">Sản phẩm 2: Lục Trà Nhãn &amp; Trà Xoài Chanh Dây</div>
                <div class="social-card-desc">Bài đăng đặt câu hỏi tương tác giữa 2 món nước giải nhiệt, kết hợp nhân viên trực tiếp cầm sản phẩm thực tế tại quầy.</div>
                <div class="social-stat-chips">
                  <span class="stat-chip"><i data-lucide="thumbs-up" style="width:11px;height:11px;"></i> 17 thích</span>
                  <span class="stat-chip"><i data-lucide="message-circle" style="width:11px;height:11px;"></i> 13 bình luận</span>
                  <span class="stat-chip"><i data-lucide="share-2" style="width:11px;height:11px;"></i> 1 share</span>
                  <span class="stat-chip highlight">Tổng: 31 tương tác</span>
                </div>
              </div>
            </div>
          </div>

          <!-- FB 3 -->
          <div class="social-post-card" onclick="openLightbox('assets/cuoi-ky/fb-post-3-must-try-drinks.webp', 'Facebook: Must Try Drinks (Cà Phê hay Trà)', 'Bài đăng tổng hợp Cacao Kem Muối, Trà Vải Hoa Hồng — 39 tương tác')">
            <div class="social-post-media">
              <img src="assets/cuoi-ky/fb-post-3-must-try-drinks.webp" alt="Must Try Drinks Olion Coffee" class="social-post-img" />
              <div class="proof-card-zoom-badge"><i data-lucide="zoom-in" style="width:11px;height:11px;"></i> Phóng to</div>
            </div>
            <div class="social-card-body">
              <div>
                <div class="social-card-title">Sản phẩm 3: Bộ Sưu Tập Must-Try Drinks</div>
                <div class="social-card-desc">Bài đăng giới thiệu đồng loạt các thức uống bán chạy nhất menu như Cacao Kem Muối, Trà Vải Hoa Hồng... tạo sự đa dạng lựa chọn.</div>
                <div class="social-stat-chips">
                  <span class="stat-chip"><i data-lucide="thumbs-up" style="width:11px;height:11px;"></i> 20 thích</span>
                  <span class="stat-chip"><i data-lucide="message-circle" style="width:11px;height:11px;"></i> 17 bình luận</span>
                  <span class="stat-chip"><i data-lucide="share-2" style="width:11px;height:11px;"></i> 2 share</span>
                  <span class="stat-chip highlight">Tổng: 39 tương tác</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- 2. KÊNH INSTAGRAM -->
      <div style="margin-bottom:45px;">
        <h3 style="font-family:var(--font-serif);font-size:24px;color:#E1306C;margin-bottom:16px;display:flex;align-items:center;gap:10px;">
          <i data-lucide="instagram" style="width:22px;height:22px;"></i> Kênh Instagram — Thẩm Mỹ, Cảm Xúc &amp; Reels Sáng Tạo
        </h3>
        <div class="social-showcase-grid">
          <!-- IG 1 -->
          <div class="social-post-card" onclick="openLightbox('assets/cuoi-ky/ig-reel-1-i-think-you-need-a-coffee.webp', 'Instagram Reel: I think you need a coffee', 'Reel không gian quán kết hợp thông điệp chữ bàn tay — 130 tương tác, 64 shares')">
            <div class="social-post-media">
              <img src="assets/cuoi-ky/ig-reel-1-i-think-you-need-a-coffee.webp" alt="Reel I think you need a coffee" class="social-post-img" />
              <div class="proof-card-zoom-badge"><i data-lucide="zoom-in" style="width:11px;height:11px;"></i> Phóng to</div>
            </div>
            <div class="social-card-body">
              <div>
                <div class="social-card-title">Sản phẩm 1: Reel “I think you need a coffee”</div>
                <div class="social-card-desc">Video kết hợp không gian quán với chữ viết tay kích thích sự tò mò. Đạt lượng tương tác cao nhất Instagram với 64 lượt gửi trực tiếp.</div>
                <div class="social-stat-chips">
                  <span class="stat-chip"><i data-lucide="heart" style="width:11px;height:11px;"></i> 63 thích</span>
                  <span class="stat-chip"><i data-lucide="send" style="width:11px;height:11px;"></i> 64 gửi</span>
                  <span class="stat-chip"><i data-lucide="repeat" style="width:11px;height:11px;"></i> 1 repost</span>
                  <span class="stat-chip highlight">Tổng: 130 tương tác</span>
                </div>
              </div>
            </div>
          </div>

          <!-- IG 2 -->
          <div class="social-post-card" onclick="openLightbox('assets/cuoi-ky/ig-post-2-yogurt-viet-quat.webp', 'Instagram: Yogurt Việt Quất', 'Hình ảnh sản phẩm tươi mát kèm mô tả hương vị — 157 tương tác, 131 shares')">
            <div class="social-post-media">
              <img src="assets/cuoi-ky/ig-post-2-yogurt-viet-quat.webp" alt="Yogurt Việt Quất" class="social-post-img" />
              <div class="proof-card-zoom-badge"><i data-lucide="zoom-in" style="width:11px;height:11px;"></i> Phóng to</div>
            </div>
            <div class="social-card-body">
              <div>
                <div class="social-card-title">Sản phẩm 2: Yogurt Việt Quất Mát Lạnh</div>
                <div class="social-card-desc">Bài đăng hình ảnh sản phẩm sắc nét, hương vị chua nhẹ thanh ngọt, ghi nhận tới 131 lượt chia sẻ qua tin nhắn bạn bè.</div>
                <div class="social-stat-chips">
                  <span class="stat-chip"><i data-lucide="heart" style="width:11px;height:11px;"></i> 20 thích</span>
                  <span class="stat-chip"><i data-lucide="message-circle" style="width:11px;height:11px;"></i> 5 bình luận</span>
                  <span class="stat-chip"><i data-lucide="send" style="width:11px;height:11px;"></i> 131 chia sẻ</span>
                  <span class="stat-chip highlight">Tổng: 157 tương tác</span>
                </div>
              </div>
            </div>
          </div>

          <!-- IG 3 -->
          <div class="social-post-card" onclick="openLightbox('assets/cuoi-ky/ig-post-3-olion-first-week.webp', 'Instagram: OLION FIRST WEEK', 'Grand Opening Recap &amp; hoạt động tuần đầu tiên — 50 tương tác')">
            <div class="social-post-media">
              <img src="assets/cuoi-ky/ig-post-3-olion-first-week.webp" alt="OLION FIRST WEEK" class="social-post-img" />
              <div class="proof-card-zoom-badge"><i data-lucide="zoom-in" style="width:11px;height:11px;"></i> Phóng to</div>
            </div>
            <div class="social-card-body">
              <div>
                <div class="social-card-title">Sản phẩm 3: Recap Tuần Khai Trương (First Week)</div>
                <div class="social-card-desc">Tổng hợp hình ảnh kỷ niệm tuần đầu mở bán, chương trình Buy 2 Get 1 cùng khoảnh khắc vui tươi của nhân viên và khách hàng.</div>
                <div class="social-stat-chips">
                  <span class="stat-chip"><i data-lucide="heart" style="width:11px;height:11px;"></i> 44 thích</span>
                  <span class="stat-chip"><i data-lucide="repeat" style="width:11px;height:11px;"></i> 3 repost</span>
                  <span class="stat-chip"><i data-lucide="send" style="width:11px;height:11px;"></i> 3 gửi</span>
                  <span class="stat-chip highlight">Tổng: 50 tương tác</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- 3. KÊNH TIKTOK -->
      <div>
        <h3 style="font-family:var(--font-serif);font-size:24px;color:var(--matcha-green);margin-bottom:16px;display:flex;align-items:center;gap:10px;">
          <i data-lucide="video" style="width:22px;height:22px;"></i> Kênh TikTok — Video Hài Hước, Bắt Trend &amp; Viral Mạnh Mẽ 🏆
        </h3>
        <div class="social-showcase-grid">
          <!-- TikTok 1 -->
          <div class="social-post-card matcha" onclick="openLightbox('assets/cuoi-ky/tiktok-video-1-pov-quen-ca-lam.webp', 'TikTok: POV Bạn quên mất mình đang trong ca làm', 'Video viral nhất chiến dịch: 3.049 views, 157 likes, 194 tương tác')">
            <div class="social-post-media">
              <img src="assets/cuoi-ky/tiktok-video-1-pov-quen-ca-lam.webp" alt="POV Quên ca làm TikTok" class="social-post-img" />
              <div class="proof-card-zoom-badge"><i data-lucide="zoom-in" style="width:11px;height:11px;"></i> Phóng to</div>
            </div>
            <div class="social-card-body">
              <div>
                <div class="social-card-title">Sản phẩm 1: POV Bạn quên mất mình đang trong ca làm 🏆</div>
                <div class="social-card-desc">Khai thác tình huống lướt điện thoại hài hước của nhân viên. Video đạt lượt xem cao nhất toàn chiến dịch (3.049 views) nhờ bắt kịp xu hướng.</div>
                <div class="social-stat-chips">
                  <span class="stat-chip matcha"><i data-lucide="eye" style="width:11px;height:11px;"></i> 3.049 views</span>
                  <span class="stat-chip matcha"><i data-lucide="heart" style="width:11px;height:11px;"></i> 157 thích</span>
                  <span class="stat-chip matcha"><i data-lucide="bookmark" style="width:11px;height:11px;"></i> 16 lưu</span>
                  <span class="stat-chip highlight">Tổng: 194 tương tác</span>
                </div>
              </div>
            </div>
          </div>

          <!-- TikTok 2 -->
          <div class="social-post-card matcha" onclick="openLightbox('assets/cuoi-ky/tiktok-video-2-why-teamwork-is-important.webp', 'TikTok: Why teamwork is important', 'Video phối hợp phục vụ giữa nhân viên — 1.343 views, 57 tương tác')">
            <div class="social-post-media">
              <img src="assets/cuoi-ky/tiktok-video-2-why-teamwork-is-important.webp" alt="Why teamwork is important" class="social-post-img" />
              <div class="proof-card-zoom-badge"><i data-lucide="zoom-in" style="width:11px;height:11px;"></i> Phóng to</div>
            </div>
            <div class="social-card-body">
              <div>
                <div class="social-card-title">Sản phẩm 2: Why teamwork is important</div>
                <div class="social-card-desc">Thể hiện sự ăn ý và phối hợp nhịp nhàng giữa các bạn nhân viên quầy bar và chạy bàn trong không gian ấm cúng của quán.</div>
                <div class="social-stat-chips">
                  <span class="stat-chip matcha"><i data-lucide="eye" style="width:11px;height:11px;"></i> 1.343 views</span>
                  <span class="stat-chip matcha"><i data-lucide="heart" style="width:11px;height:11px;"></i> 45 thích</span>
                  <span class="stat-chip matcha"><i data-lucide="share-2" style="width:11px;height:11px;"></i> 5 share</span>
                  <span class="stat-chip highlight">Tổng: 57 tương tác</span>
                </div>
              </div>
            </div>
          </div>

          <!-- TikTok 3 -->
          <div class="social-post-card matcha" onclick="openLightbox('assets/cuoi-ky/tiktok-video-3-ngu-8-tieng-trong-2-tieng.webp', 'TikTok: Cách để ngủ 8 tiếng trong 2 tiếng mà vẫn khỏe', 'Tiêu đề gây tò mò cho sinh viên chạy deadline — 1.142 views, 59 tương tác')">
            <div class="social-post-media">
              <img src="assets/cuoi-ky/tiktok-video-3-ngu-8-tieng-trong-2-tieng.webp" alt="Cách để ngủ 8 tiếng trong 2 tiếng" class="social-post-img" />
              <div class="proof-card-zoom-badge"><i data-lucide="zoom-in" style="width:11px;height:11px;"></i> Phóng to</div>
            </div>
            <div class="social-card-body">
              <div>
                <div class="social-card-title">Sản phẩm 3: Cách ngủ 8 tiếng trong 2 tiếng mà vẫn khỏe</div>
                <div class="social-card-desc">Đánh trúng tâm lý sinh viên thức khuya làm đồ án, tiêu đề gây sốc hài hước dẫn về giải pháp uống cà phê nạp năng lượng tại Olion.</div>
                <div class="social-stat-chips">
                  <span class="stat-chip matcha"><i data-lucide="eye" style="width:11px;height:11px;"></i> 1.142 views</span>
                  <span class="stat-chip matcha"><i data-lucide="heart" style="width:11px;height:11px;"></i> 49 thích</span>
                  <span class="stat-chip matcha"><i data-lucide="message-circle" style="width:11px;height:11px;"></i> 5 comment</span>
                  <span class="stat-chip highlight">Tổng: 59 tương tác</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================================
       MỤC 6: ĐÁNH GIÁ TỔNG QUAN & BÀI HỌC KINH NGHIỆM
       ======================================================== -->
  <section class="report-section" id="muc-6">
    <div class="shell">
      <div class="section-chapter-tag matcha">6. ĐÁNH GIÁ &amp; BÀI HỌC KINH NGHIỆM</div>
      <h2 class="section-main-heading">6. Đánh Giá Tổng Quan 4 Kênh &amp; Bài Học Chiến Lược</h2>
      <p style="color:var(--text-muted);margin-bottom:24px;font-size:15px;">
        Đúc kết những thành tựu đạt được, nhận diện điểm nghẽn và rút ra bài học thực chiến quan trọng trong quản trị truyền thông số.
      </p>

      <!-- Bảng So Sánh 4 Kênh -->
      <div class="table-container">
        <table class="pdf-table">
          <thead>
            <tr>
              <th>Kênh truyền thông</th>
              <th>Vai trò chiến lược</th>
              <th>Kết quả nổi bật</th>
              <th>Hạn chế chính cần khắc phục</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td style="font-weight:700;color:var(--crema);">Facebook Fanpage</td>
              <td>Duy trì hình ảnh thương hiệu, cổng thông tin chính thức &amp; kết nối cộng đồng</td>
              <td>Follower tăng từ 50 lên 100; tương tác vượt KPI đạt 110,8% (665 tương tác)</td>
              <td>Khả năng lan truyền tự nhiên thấp, lượt xem có xu hướng giảm dần qua các tuần</td>
            </tr>
            <tr>
              <td style="font-weight:700;color:var(--crema);">Instagram</td>
              <td>Xây dựng thẩm mỹ thương hiệu cao cấp, thu hút giới trẻ thích check-in &amp; Reels</td>
              <td>Follower tăng từ 58 lên 142; tuần 4 bùng nổ đạt 513 tương tác nhờ Reels viral</td>
              <td>Hiệu quả tương tác chưa đồng đều, chênh lệch lớn giữa các tuần</td>
            </tr>
            <tr style="background:rgba(46,204,113,0.06);">
              <td style="font-weight:700;color:var(--matcha-green);">TikTok 🏆</td>
              <td>Mở rộng phễu tiếp cận, lan truyền nội dung viral và thu hút tệp khách hàng mới</td>
              <td style="color:var(--matcha-bright);font-weight:600;">Lượt xem bài đăng tăng từ 1.800 lên 5.300/tuần; Tuần 4 thu được 138 follower ròng; Tuần 6 đạt 219 shares</td>
              <td>Tỷ lệ chuyển đổi người xem video thành follower theo dõi lâu dài chưa thực sự ổn định</td>
            </tr>
            <tr>
              <td style="font-weight:700;color:var(--crema);">Landing Page</td>
              <td>Điểm đến tập trung thông tin, menu, địa chỉ và đo lường chuyển đổi cuối</td>
              <td>Tuần 4 đạt đỉnh 280 lượt truy cập (sau khi chủ động gắn link dưới bài đăng FB)</td>
              <td>Lượng truy cập sụt giảm ở tuần 5 và 6 khi tần suất gắn link giảm bớt</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Hai Khối Bài Học Lớn Nhất -->
      <div class="report-two-cols" style="margin-top:24px;">
        <div class="reason-box">
          <h4 style="color:var(--accent-gold);font-size:16px;margin-bottom:8px;">
            <i data-lucide="lightbulb" style="width:16px;height:16px;"></i> Bài Học Lớn Nhất (Key Takeaway):
          </h4>
          <p style="font-size:14px;line-height:1.6;color:var(--crema);">
            <strong>Không áp dụng một cách truyền thông giống nhau cho tất cả nền tảng:</strong> Nội dung giới thiệu sản phẩm chỉn chu có thể phù hợp với Facebook và Instagram để duy trì nhận diện thương hiệu, nhưng chưa chắc tạo được sức hút trên TikTok. Đối với TikTok, nội dung bắt buộc phải mang tính giải trí, gần gũi, bắt trend và đặc biệt là phải có <strong>yếu tố Hook giữ chân người xem ngay trong 3 giây đầu tiên</strong>.
          </p>
        </div>

        <div class="reason-box" style="border-left-color:var(--matcha-green);">
          <h4 style="color:var(--matcha-green);font-size:16px;margin-bottom:8px;">
            <i data-lucide="trending-up" style="width:16px;height:16px;"></i> Đổi Mới Sáng Tạo Dựa Trên Dữ Liệu Thực Tế:
          </h4>
          <p style="font-size:14px;line-height:1.6;color:var(--crema);">
            Sau khi nhận thấy hiệu quả tuần đầu chưa cao, nhóm đã chủ động phân tích chỉ số và thay đổi kịch bản video TikTok: chú trọng Hook mở đầu tạo tò mò, biến nội dung khô khan thành video hài hước ca làm. Đồng thời, nhận thấy tuần 1-2 Landing Page không có lượt truy cập, nhóm đã thay đổi cách thức bằng việc gắn link trực tiếp dưới bài đăng Facebook, lập tức tạo ra <strong>280 visits trong tuần 4</strong>.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================================
       MỤC 7: TUÂN THỦ PHÁP LÝ (12 TIÊU CHÍ)
       ======================================================== -->
  <section class="report-section" id="muc-7">
    <div class="shell">
      <div class="section-chapter-tag">7. TUÂN THỦ PHÁP LÝ &amp; ĐẠO ĐỨC</div>
      <h2 class="section-main-heading">7. Danh Mục 12 Tiêu Chí Tuân Thủ Pháp Lý &amp; Quảng Cáo</h2>
      <p style="color:var(--text-muted);margin-bottom:24px;font-size:15px;">
        Dự án Olion Coffee cam kết tuân thủ nghiêm ngặt chuẩn mực đạo đức truyền thông số và chính sách quảng cáo hiện hành.
      </p>

      <div class="table-container">
        <table class="pdf-table">
          <thead>
            <tr>
              <th style="width:70px;text-align:center;">STT</th>
              <th>Nội dung tiêu chí tuân thủ pháp lý (Dự án Olion Coffee)</th>
              <th style="width:160px;text-align:center;">Trạng thái thẩm định</th>
            </tr>
          </thead>
          <tbody>
            <tr><td style="text-align:center;">01</td><td>Gắn nhãn rõ ràng <code>#quangcao</code> / <code>#taitro</code> ngay đầu bài viết truyền thông</td><td style="text-align:center;color:var(--matcha-bright);font-weight:700;">☑ Đã đạt</td></tr>
            <tr><td style="text-align:center;">02</td><td>Người review, trải nghiệm thực tế đã trực tiếp uống và sử dụng sản phẩm thật tại quán</td><td style="text-align:center;color:var(--matcha-bright);font-weight:700;">☑ Đã đạt</td></tr>
            <tr><td style="text-align:center;">03</td><td>Tuyệt đối không dùng từ ngữ mang tính cam kết quá đà, tuyệt đối hóa khi thiếu căn cứ y khoa/khoa học</td><td style="text-align:center;color:var(--matcha-bright);font-weight:700;">☑ Đã đạt</td></tr>
            <tr><td style="text-align:center;">04</td><td>Tất cả phản hồi (Feedback) và số liệu lượng khách hàng ghi nhận là số liệu thật 100%</td><td style="text-align:center;color:var(--matcha-bright);font-weight:700;">☑ Đã đạt</td></tr>
            <tr><td style="text-align:center;">05</td><td>Ghi rõ đầy đủ thông tin người bán, hotline liên hệ (0783 657 587) và chính sách đổi trả thức uống</td><td style="text-align:center;color:var(--matcha-bright);font-weight:700;">☑ Đã đạt</td></tr>
            <tr><td style="text-align:center;">06</td><td>Chính sách Affiliate / Tiếp thị liên kết: nêu rõ ràng định hướng và tỷ lệ hoa hồng</td><td style="text-align:center;color:var(--matcha-bright);font-weight:700;">☑ Đã đạt</td></tr>
            <tr><td style="text-align:center;">07</td><td>Hoạt động Livestream bán hàng: công khai thông tin chính xác, minh bạch giấy phép kinh doanh</td><td style="text-align:center;color:var(--matcha-bright);font-weight:700;">☑ Đã đạt</td></tr>
            <tr><td style="text-align:center;">08</td><td>Biểu mẫu thu thập dữ liệu (Form): ô chấp thuận điều khoản để trống, tuyệt đối không tích sẵn</td><td style="text-align:center;color:var(--matcha-bright);font-weight:700;">☑ Đã đạt</td></tr>
            <tr><td style="text-align:center;">09</td><td>Bảng tính dữ liệu đơn hàng và khách hàng được phân quyền nội bộ, bảo mật tuyệt đối</td><td style="text-align:center;color:var(--matcha-bright);font-weight:700;">☑ Đã đạt</td></tr>
            <tr><td style="text-align:center;">10</td><td>Tất cả nhãn mác, hình ảnh sản phẩm, âm nhạc và font chữ thiết kế đều có bản quyền giấy phép hợp lệ</td><td style="text-align:center;color:var(--matcha-bright);font-weight:700;">☑ Đã đạt</td></tr>
            <tr><td style="text-align:center;">11</td><td>Các hình ảnh sản phẩm hoặc người thật có ứng dụng công nghệ AI đều được gắn nhãn công khai rõ ràng</td><td style="text-align:center;color:var(--matcha-bright);font-weight:700;">☑ Đã đạt</td></tr>
            <tr><td style="text-align:center;">12</td><td>Tuyệt đối không mua follower, like ảo hay cày view ảo — 100% người theo dõi là người dùng tự nhiên</td><td style="text-align:center;color:var(--matcha-bright);font-weight:700;">☑ Đã đạt</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>

  <!-- ========================================================
       MỤC 8: KẾ HOẠCH PHÁT TRIỂN 3 THÁNG TỚI
       ======================================================== -->
  <section class="report-section" id="muc-8">
    <div class="shell">
      <div class="section-chapter-tag matcha">8. KẾ HOẠCH PHÁT TRIỂN 3 THÁNG</div>
      <h2 class="section-main-heading">8. Định Hướng Duy Trì Kênh &amp; Mục Tiêu Phát Triển 3 Tháng Tới</h2>
      <p style="color:var(--text-muted);margin-bottom:24px;font-size:15px;">
        Kế hoạch hành động chi tiết sau khi kết thúc môn học nhằm tiếp tục mở rộng quy mô thương hiệu Olion Coffee trong thực tế.
      </p>

      <div class="report-two-cols">
        <!-- Cột trái: Định hướng 4 kênh -->
        <div class="report-card">
          <div class="card-tag gold">CHIẾN LƯỢC KÊNH</div>
          <h3 class="card-title">Định Hướng Duy Trì Các Kênh</h3>
          <ul class="clean-list">
            <li><strong>TikTok (Kênh mũi nhọn):</strong> Tiếp tục ưu tiên số 1 vì hiệu quả view và tương tác vượt trội. Duy trì video vui nhộn, bắt trend lồng ghép sản phẩm tự nhiên, tối ưu hóa Hook 3 giây đầu.</li>
            <li><strong>Facebook Fanpage:</strong> Kênh thông tin chính thống cập nhật món mới, chương trình ưu đãi, không gian quán và duy trì gắn link Landing Page.</li>
            <li><strong>Instagram:</strong> Nâng cao tính thẩm mỹ hình ảnh, duy trì định dạng Stories và Reels ngắn tương tác với giới trẻ.</li>
            <li><strong>Landing Page:</strong> Cập nhật liên tục menu điện tử, đặt bàn học nhóm, định vị bản đồ và khuyến mãi theo mùa.</li>
          </ul>
        </div>

        <!-- Cột phải: Bảng mục tiêu 3 tháng -->
        <div class="report-card">
          <div class="card-tag matcha">MỤC TIÊU 3 THÁNG TỚI</div>
          <h3 class="card-title">Chỉ Tiêu Định Lượng &amp; Định Tính</h3>
          <ul class="clean-list">
            <li><strong>TikTok:</strong> Duy trì 5 video/tuần, hướng tới mốc <strong>500 followers</strong>.</li>
            <li><strong>Facebook:</strong> Duy trì 5 bài đăng/tuần, mục tiêu đạt <strong>150 followers</strong>.</li>
            <li><strong>Instagram:</strong> Duy trì 5 bài đăng/tuần + 5-6 stories/tuần, hướng đến <strong>200 followers</strong>.</li>
            <li><strong>Landing Page:</strong> Thu hút tối thiểu <strong>500 visits</strong> trong 3 tháng.</li>
            <li><strong>Tiêu chuẩn đánh giá thực tế:</strong> Không chỉ đếm like, tập trung đo lường số tin nhắn hỏi món, lượng khách sinh viên đến quán trực tiếp từ mạng xã hội.</li>
          </ul>
        </div>
      </div>

      <!-- Kết luận khởi nghiệp -->
      <div class="reason-box" style="margin-top:24px;">
        <h4 style="color:var(--accent-gold);font-size:16px;margin-bottom:8px;">
          <i data-lucide="compass" style="width:16px;height:16px;"></i> Định Hướng Khởi Nghiệp Thực Tế (Startup Vision):
        </h4>
        <p style="font-size:14px;line-height:1.6;color:var(--crema);">
          Nhóm nhận thấy dự án không chỉ dừng lại ở phạm vi một bài tập học phần mà còn có tiềm năng tiếp tục phát triển thành hoạt động truyền thông thực tế cho thương hiệu. Trong thời gian tới, nhóm định hướng tiếp tục phát huy thế mạnh của TikTok trong việc tạo độ nhận diện và thu hút khách hàng mới, kết hợp Facebook và Instagram để duy trì hình ảnh thương hiệu, đồng thời sử dụng Landing Page làm điểm đến tập trung thông tin. Đây sẽ là nền tảng để nhóm từng bước hoàn thiện hoạt động truyền thông, xây dựng tệp khách hàng tiềm năng và tạo tiền đề cho sự phát triển lâu dài của dự án.
        </p>
      </div>
    </div>
  </section>

  <!-- ========================================================
       MỤC 9: THÀNH VIÊN NHÓM 7 (GỖ XÀ CỪ)
       ĐƯA TOÀN BỘ 11 HÌNH ẢNH THÀNH VIÊN XUỐNG ĐÂY CHUẨN XÁC
       ======================================================== -->
  <section class="report-section" id="muc-9">
    <div class="shell">
      <div class="section-chapter-tag">9. THÀNH VIÊN NHÓM 7 — GỖ XÀ CỪ</div>
      <h2 class="section-main-heading">9. Phân Vai &amp; Đóng Góp Của Các Thành Viên Nhóm 7</h2>
      <p style="color:var(--text-muted);margin-bottom:30px;font-size:15px;">
        Đội ngũ 11 thành viên trực tiếp tham gia xây dựng kế hoạch, sáng tạo nội dung, sản xuất hình ảnh/video, vận hành kênh và đo lường hiệu quả chiến dịch Olion Coffee.
      </p>

      <div class="team-showcase-container">

        <!-- 1. TRƯỞNG NHÓM -->
        <div class="team-dept-block">
          <div class="team-dept-title">
            <i data-lucide="crown" style="width:22px;height:22px;"></i> TRƯỞNG NHÓM &bull; ĐIỀU PHỐI CHUNG
          </div>
          <div class="team-members-grid cols-1">
            <div class="member-card leader" onclick="openLightbox('assets/cuoi-ky/member-quang-hung-truong-nhom.webp', 'Quang Hưng — Trưởng Nhóm 7 (Gỗ Xà Cừ)', 'Điều phối hoạt động chung, xây dựng kế hoạch, phân công nhiệm vụ, theo dõi tiến độ và tổng hợp kết quả')">
              <div class="member-photo-frame">
                <span class="member-role-badge leader-badge"><i data-lucide="crown" style="width:12px;height:12px;"></i> Trưởng Nhóm</span>
                <div class="member-zoom-badge"><i data-lucide="zoom-in" style="width:11px;height:11px;"></i> Phóng to ảnh</div>
                <img src="assets/cuoi-ky/member-quang-hung-truong-nhom.webp" alt="Quang Hưng - Trưởng Nhóm" class="member-photo-img" />
              </div>
              <div class="member-info-content">
                <div class="member-name">Quang Hưng</div>
                <div class="member-dept">Trưởng Nhóm &bull; Quản Trị Dự Án</div>
                <div class="member-desc">
                  Chịu trách nhiệm điều phối hoạt động chung, xây dựng kế hoạch tổng thể, phân công nhiệm vụ cho từng ban, theo dõi sát sao tiến độ triển khai hàng tuần và tổng hợp báo cáo đánh giá kết quả.
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- 2. PHỤ TRÁCH NỘI DUNG -->
        <div class="team-dept-block">
          <div class="team-dept-title matcha">
            <i data-lucide="pen-tool" style="width:22px;height:22px;"></i> BAN NỘI DUNG &bull; KỊCH BẢN &amp; XU HƯỚNG
          </div>
          <div class="team-members-grid cols-2">
            <!-- Uyên Thuỳ -->
            <div class="member-card" onclick="openLightbox('assets/cuoi-ky/member-uyen-thuy-noi-dung.webp', 'Uyên Thuỳ — Phụ Trách Nội Dung', 'Nghiên cứu ý tưởng, xây dựng kịch bản, viết nội dung bài đăng và đề xuất xu hướng')">
              <div class="member-photo-frame">
                <span class="member-role-badge matcha-badge"><i data-lucide="edit-3" style="width:12px;height:12px;"></i> Content Creator</span>
                <div class="member-zoom-badge"><i data-lucide="zoom-in" style="width:11px;height:11px;"></i> Phóng to ảnh</div>
                <img src="assets/cuoi-ky/member-uyen-thuy-noi-dung.webp" alt="Uyên Thuỳ - Ban Nội Dung" class="member-photo-img" />
              </div>
              <div class="member-info-content">
                <div class="member-name">Uyên Thuỳ</div>
                <div class="member-dept matcha">Phụ Trách Nội Dung</div>
                <div class="member-desc">
                  Nghiên cứu insight sinh viên ĐH Văn Lang, sáng tạo ý tưởng bài viết, xây dựng kịch bản chi tiết cho các bài đăng mạng xã hội và đề xuất các xu hướng viral phù hợp với quán.
                </div>
              </div>
            </div>

            <!-- Thuý Hiền -->
            <div class="member-card" onclick="openLightbox('assets/cuoi-ky/member-thuy-hien-noi-dung.webp', 'Thuý Hiền — Phụ Trách Nội Dung', 'Nghiên cứu ý tưởng, biên soạn nội dung bài đăng và kiểm duyệt thông điệp thương hiệu')">
              <div class="member-photo-frame">
                <span class="member-role-badge matcha-badge"><i data-lucide="edit-3" style="width:12px;height:12px;"></i> Content Writer</span>
                <div class="member-zoom-badge"><i data-lucide="zoom-in" style="width:11px;height:11px;"></i> Phóng to ảnh</div>
                <img src="assets/cuoi-ky/member-thuy-hien-noi-dung.webp" alt="Thuý Hiền - Ban Nội Dung" class="member-photo-img" />
              </div>
              <div class="member-info-content">
                <div class="member-name">Thuý Hiền</div>
                <div class="member-dept matcha">Phụ Trách Nội Dung</div>
                <div class="member-desc">
                  Phối hợp xây dựng kịch bản video TikTok, chắp bút nội dung bài đăng Facebook và Instagram, trau chuốt câu từ (caption) và đảm bảo thông điệp thương hiệu truyền tải nhất quán.
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- 3. PHỤ TRÁCH HÌNH ẢNH VÀ THIẾT KẾ -->
        <div class="team-dept-block">
          <div class="team-dept-title">
            <i data-lucide="camera" style="width:22px;height:22px;"></i> BAN HÌNH ẢNH &amp; THIẾT KẾ &bull; VISUAL &amp; VIDEO
          </div>
          <div class="team-members-grid cols-3">
            <!-- Duy Khánh -->
            <div class="member-card" onclick="openLightbox('assets/cuoi-ky/member-duy-khanh-thiet-ke.webp', 'Duy Khánh — Phụ Trách Hình Ảnh &amp; Thiết Kế', 'Chụp ảnh sản phẩm, quay dựng video TikTok, chỉnh sửa visual trực quan')">
              <div class="member-photo-frame">
                <span class="member-role-badge"><i data-lucide="video" style="width:12px;height:12px;"></i> Media &amp; Video</span>
                <div class="member-zoom-badge"><i data-lucide="zoom-in" style="width:11px;height:11px;"></i> Phóng to ảnh</div>
                <img src="assets/cuoi-ky/member-duy-khanh-thiet-ke.webp" alt="Duy Khánh - Ban Thiết Kế" class="member-photo-img" />
              </div>
              <div class="member-info-content">
                <div class="member-name">Duy Khánh</div>
                <div class="member-dept">Hình Ảnh &amp; Thiết Kế</div>
                <div class="member-desc">
                  Trực tiếp quay chụp hình ảnh thức uống tại quán, sản xuất và dựng các video ngắn TikTok vui nhộn, chỉnh sửa nội dung trực quan bắt mắt.
                </div>
              </div>
            </div>

            <!-- Thiên Ý -->
            <div class="member-card" onclick="openLightbox('assets/cuoi-ky/member-thien-y-thiet-ke.webp', 'Thiên Ý — Phụ Trách Hình Ảnh &amp; Thiết Kế', 'Thiết kế đồ họa, căn chỉnh màu sắc và đảm bảo tính nhất quán nhận diện Olion')">
              <div class="member-photo-frame">
                <span class="member-role-badge"><i data-lucide="palette" style="width:12px;height:12px;"></i> Graphic Designer</span>
                <div class="member-zoom-badge"><i data-lucide="zoom-in" style="width:11px;height:11px;"></i> Phóng to ảnh</div>
                <img src="assets/cuoi-ky/member-thien-y-thiet-ke.webp" alt="Thiên Ý - Ban Thiết Kế" class="member-photo-img" />
              </div>
              <div class="member-info-content">
                <div class="member-name">Thiên Ý</div>
                <div class="member-dept">Hình Ảnh &amp; Thiết Kế</div>
                <div class="member-desc">
                  Thiết kế banner, poster đồ uống, bố cục hình ảnh bài đăng, đảm bảo tính thẩm mỹ đồng bộ và chuẩn nhận diện thương hiệu Olion Coffee.
                </div>
              </div>
            </div>

            <!-- Gia Quyền -->
            <div class="member-card" onclick="openLightbox('assets/cuoi-ky/member-gia-quyen-thiet-ke.webp', 'Gia Quyền — Phụ Trách Hình Ảnh &amp; Thiết Kế', 'Hậu kỳ video, tối ưu hiệu ứng đồ họa và âm thanh cho các nền tảng mạng xã hội')">
              <div class="member-photo-frame">
                <span class="member-role-badge"><i data-lucide="film" style="width:12px;height:12px;"></i> Video Editor</span>
                <div class="member-zoom-badge"><i data-lucide="zoom-in" style="width:11px;height:11px;"></i> Phóng to ảnh</div>
                <img src="assets/cuoi-ky/member-gia-quyen-thiet-ke.webp" alt="Gia Quyền - Ban Thiết Kế" class="member-photo-img" />
              </div>
              <div class="member-info-content">
                <div class="member-name">Gia Quyền</div>
                <div class="member-dept">Hình Ảnh &amp; Thiết Kế</div>
                <div class="member-desc">
                  Hậu kỳ video, chèn âm thanh bắt trend, chỉnh hiệu ứng chuyển cảnh và hỗ trợ sản xuất visual phục vụ các chiến dịch truyền thông đa kênh.
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- 4. PHỤ TRÁCH VẬN HÀNH KÊNH -->
        <div class="team-dept-block">
          <div class="team-dept-title matcha">
            <i data-lucide="share-2" style="width:22px;height:22px;"></i> BAN VẬN HÀNH KÊNH &bull; ĐIỀU HƯỚNG &amp; TƯƠNG TÁC
          </div>
          <div class="team-members-grid cols-2">
            <!-- Thành Duy -->
            <div class="member-card" onclick="openLightbox('assets/cuoi-ky/member-thanh-duy-van-hanh.webp', 'Thành Duy — Phụ Trách Vận Hành Kênh', 'Quản lý lịch đăng bài, tối ưu hóa phân phối và điều hướng traffic về Landing Page')">
              <div class="member-photo-frame">
                <span class="member-role-badge matcha-badge"><i data-lucide="sliders" style="width:12px;height:12px;"></i> Channel Operations</span>
                <div class="member-zoom-badge"><i data-lucide="zoom-in" style="width:11px;height:11px;"></i> Phóng to ảnh</div>
                <img src="assets/cuoi-ky/member-thanh-duy-van-hanh.webp" alt="Thành Duy - Ban Vận Hành" class="member-photo-img" />
              </div>
              <div class="member-info-content">
                <div class="member-name">Thành Duy</div>
                <div class="member-dept matcha">Phụ Trách Vận Hành Kênh</div>
                <div class="member-desc">
                  Quản lý lịch trình đăng tải trên Facebook, Instagram và TikTok; trực tiếp triển khai chiến thuật gắn link điều hướng người dùng về Landing Page.
                </div>
              </div>
            </div>

            <!-- Như Ý -->
            <div class="member-card" onclick="openLightbox('assets/cuoi-ky/member-nhu-y-van-hanh.webp', 'Như Ý — Phụ Trách Vận Hành Kênh', 'Điều phối thời gian đăng bài, chăm sóc tương tác bình luận và phản hồi khách hàng')">
              <div class="member-photo-frame">
                <span class="member-role-badge matcha-badge"><i data-lucide="message-square" style="width:12px;height:12px;"></i> Community Mod</span>
                <div class="member-zoom-badge"><i data-lucide="zoom-in" style="width:11px;height:11px;"></i> Phóng to ảnh</div>
                <img src="assets/cuoi-ky/member-nhu-y-van-hanh.webp" alt="Như Ý - Ban Vận Hành" class="member-photo-img" />
              </div>
              <div class="member-info-content">
                <div class="member-name">Như Ý</div>
                <div class="member-dept matcha">Phụ Trách Vận Hành Kênh</div>
                <div class="member-desc">
                  Theo dõi phản hồi của người dùng, trả lời bình luận, tin nhắn tư vấn và duy trì sự tương tác ấm áp, gần gũi như bạn bè của thương hiệu.
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- 5. PHỤ TRÁCH ĐO LƯỜNG VÀ BÁO CÁO -->
        <div class="team-dept-block">
          <div class="team-dept-title">
            <i data-lucide="bar-chart-2" style="width:22px;height:22px;"></i> BAN ĐO LƯỜNG &amp; BÁO CÁO &bull; DATA &amp; ANALYTICS
          </div>
          <div class="team-members-grid cols-3">
            <!-- Anh Thư -->
            <div class="member-card" onclick="openLightbox('assets/cuoi-ky/member-anh-thu-do-luong.webp', 'Anh Thư — Phụ Trách Đo Lường &amp; Báo Cáo', 'Theo dõi chỉ số lượt xem, tương tác, follower và lượt truy cập Landing Page hàng tuần')">
              <div class="member-photo-frame">
                <span class="member-role-badge"><i data-lucide="trending-up" style="width:12px;height:12px;"></i> Data Analyst</span>
                <div class="member-zoom-badge"><i data-lucide="zoom-in" style="width:11px;height:11px;"></i> Phóng to ảnh</div>
                <img src="assets/cuoi-ky/member-anh-thu-do-luong.webp" alt="Anh Thư - Ban Đo Lường" class="member-photo-img" />
              </div>
              <div class="member-info-content">
                <div class="member-name">Anh Thư</div>
                <div class="member-dept">Đo Lường &amp; Báo Cáo</div>
                <div class="member-desc">
                  Thu thập và theo dõi các chỉ số reach, tương tác, follower và traffic Landing Page hàng ngày qua các công cụ đo lường chuyên sâu.
                </div>
              </div>
            </div>

            <!-- Phương Linh -->
            <div class="member-card" onclick="openLightbox('assets/cuoi-ky/member-phuong-linh-do-luong.webp', 'Phương Linh — Phụ Trách Đo Lường &amp; Báo Cáo', 'Tổng hợp dữ liệu, phân tích hiệu suất các bài đăng và đánh giá tỷ lệ chuyển đổi')">
              <div class="member-photo-frame">
                <span class="member-role-badge"><i data-lucide="file-text" style="width:12px;height:12px;"></i> Reporting Lead</span>
                <div class="member-zoom-badge"><i data-lucide="zoom-in" style="width:11px;height:11px;"></i> Phóng to ảnh</div>
                <img src="assets/cuoi-ky/member-phuong-linh-do-luong.webp" alt="Phương Linh - Ban Đo Lường" class="member-photo-img" />
              </div>
              <div class="member-info-content">
                <div class="member-name">Phương Linh</div>
                <div class="member-dept">Đo Lường &amp; Báo Cáo</div>
                <div class="member-desc">
                  Tổng hợp bảng số liệu báo cáo 6 tuần, trực quan hóa biểu đồ tăng trưởng và đánh giá mức độ hoàn thành so với chỉ tiêu KPI kế hoạch.
                </div>
              </div>
            </div>

            <!-- Thanh Ngân -->
            <div class="member-card" onclick="openLightbox('assets/cuoi-ky/member-thanh-ngan-do-luong.webp', 'Thanh Ngân — Phụ Trách Đo Lường &amp; Báo Cáo', 'Đánh giá hiệu quả truyền thông, rút ra bài học kinh nghiệm và đề xuất giải pháp tối ưu')">
              <div class="member-photo-frame">
                <span class="member-role-badge"><i data-lucide="pie-chart" style="width:12px;height:12px;"></i> Insight &amp; Audit</span>
                <div class="member-zoom-badge"><i data-lucide="zoom-in" style="width:11px;height:11px;"></i> Phóng to ảnh</div>
                <img src="assets/cuoi-ky/member-thanh-ngan-do-luong.webp" alt="Thanh Ngân - Ban Đo Lường" class="member-photo-img" />
              </div>
              <div class="member-info-content">
                <div class="member-name">Thanh Ngân</div>
                <div class="member-dept">Đo Lường &amp; Báo Cáo</div>
                <div class="member-desc">
                  Phân tích nguyên nhân tăng giảm số liệu, đối chiếu hành vi người dùng giữa các kênh và đề xuất giải pháp điều chỉnh chiến lược kịp thời.
                </div>
              </div>
            </div>
          </div>
        </div>

      </div>

      <!-- Khối ghi nhận tinh thần làm việc nhóm -->
      <div class="auto-note-box" style="margin-top:28px;">
        <strong>Tinh Thần Đồng Đội &amp; Hợp Tác Nhóm 7 (Gỗ Xà Cừ):</strong><br />
        Các thành viên không chỉ hoàn thành xuất sắc nhiệm vụ được phân công mà còn chủ động hỗ trợ lẫn nhau trong quá trình sáng tạo kịch bản, quay dựng video và giải quyết các vấn đề phát sinh. Qua 6 tuần thực chiến, nhóm đã tích lũy kỹ năng làm việc nhóm chuyên nghiệp, quản trị tiến độ bài bản và sẵn sàng cho các dự án lớn trong tương lai!
      </div>
    </div>
  </section>

  <!-- ========================================================
       CHÂN TRANG (FOOTER)
       ======================================================== -->
  <footer style="background:#070503;border-top:1.5px solid var(--border-brass);padding:45px 0 35px;margin-top:50px;color:var(--text-muted);font-size:13.5px;">
    <div class="shell" style="display:flex;flex-direction:column;align-items:center;text-align:center;gap:18px;">
      <a href="/" title="Olion Coffee">
        <img src="assets/logo-white.webp" alt="Olion Coffee" style="height:44px;width:auto;" onerror="this.src='assets/logo-transparent.webp'" />
      </a>
      <div style="font-family:var(--font-serif);font-size:18px;color:var(--crema);">
        Olion Coffee &bull; Elegance in Every Sip
      </div>
      <p style="max-width:680px;line-height:1.6;margin:0;">
        Báo cáo tổng kết cuối kỳ môn học Truyền thông số (IMC) &bull; Khoa Quan hệ Công chúng &amp; Truyền thông &bull; Trường Đại học Văn Lang (VLU).<br />
        Thực hiện bởi: <strong>Nhóm 7 — Gỗ Xà Cừ</strong> &bull; Đơn vị thực tế: Quán cà phê <strong>Olion Coffee</strong> (80/64a Dương Quảng Hàm, An Nhơn, TP.HCM).
      </p>
      <div style="display:flex;gap:18px;align-items:center;margin-top:8px;flex-wrap:wrap;justify-content:center;">
        <a href="/" style="color:var(--accent-gold);text-decoration:none;font-weight:600;"><i data-lucide="home" style="width:13px;height:13px;display:inline;vertical-align:middle;"></i> Trang Chủ Olion</a>
        <span style="opacity:0.3;">&bull;</span>
        <a href="https://www.olioncoffee.app/campaign-report" style="color:var(--matcha-green);text-decoration:none;font-weight:600;"><i data-lucide="file-text" style="width:13px;height:13px;display:inline;vertical-align:middle;"></i> Báo Cáo Chiến Dịch Giữa Kỳ</a>
        <span style="opacity:0.3;">&bull;</span>
        <span style="color:var(--text-dim);">&copy; 2026 Olion Coffee &amp; Nhóm 7 Gỗ Xà Cừ. All rights reserved.</span>
      </div>
    </div>
  </footer>

  <!-- ========================================================
       SCRIPTS: CON CHUỘT LÁ TRÀ, CHARTS & TƯƠNG TÁC
       ======================================================== -->
  <script>
    // Lucide Icons Init
    if (window.lucide && typeof window.lucide.createIcons === 'function') {
      window.lucide.createIcons();
    }

    // Lightbox Modal
    function openLightbox(src, title, desc) {
      const box = document.getElementById('photoLightbox');
      const img = document.getElementById('lightboxImg');
      const cap = document.getElementById('lightboxCaption');
      if (box && img && cap) {
        img.src = src;
        cap.innerHTML = '<strong>' + title + '</strong>' + (desc ? '<br><small style="color:#A8A096;font-size:12.5px;font-weight:normal;">' + desc + '</small>' : '');
        box.classList.add('open');
        if (window.lucide) window.lucide.createIcons();
      }
    }

    function closeLightbox() {
      const box = document.getElementById('photoLightbox');
      if (box) box.classList.remove('open');
    }

    // Copy Link function
    function copyLink() {
      if (navigator.clipboard) {
        navigator.clipboard.writeText(window.location.href).then(() => {
          showToast('Đã sao chép liên kết báo cáo cuối kỳ!');
        });
      } else {
        showToast('Link: ' + window.location.href);
      }
    }

    function showToast(msg) {
      const toast = document.getElementById('toast');
      const msgEl = document.getElementById('toastMsg');
      if (toast && msgEl) {
        msgEl.innerText = msg;
        toast.classList.add('show');
        setTimeout(() => toast.classList.remove('show'), 3000);
      }
    }

    function toggleDrawer() {
      const d = document.getElementById('mobileDrawer');
      if (d) d.classList.toggle('open');
    }

    // Trailing Matcha Leaf Cursor Following Mouse
    (function initLeafCursor() {
      const trail = document.getElementById('matchaLeafTrail');
      if (!trail) return;
      let mouseX = window.innerWidth / 2;
      let mouseY = window.innerHeight / 2;
      let trailX = mouseX;
      let trailY = mouseY;

      window.addEventListener('mousemove', (e) => {
        mouseX = e.clientX;
        mouseY = e.clientY;
      });

      function animate() {
        const dx = mouseX - trailX;
        const dy = mouseY - trailY;
        trailX += dx * 0.18;
        trailY += dy * 0.18;
        trail.style.left = trailX + 'px';
        trail.style.top = trailY + 'px';
        trail.style.transform = `translate(-50%, -50%) rotate(${dx * 0.6}deg)`;
        requestAnimationFrame(animate);
      }
      animate();
    })();

    // Scroll Progress Bar
    window.addEventListener('scroll', () => {
      const top = document.documentElement.scrollTop || document.body.scrollTop;
      const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      const progress = (top / height) * 100;
      const bar = document.getElementById('progressBar');
      if (bar) bar.style.width = progress + '%';
    });

    // Background Canvas Steam
    (function initSteam() {
      const canvas = document.getElementById('cafeCanvas');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      let w, h;
      function resize() {
        w = canvas.width = window.innerWidth;
        h = canvas.height = window.innerHeight;
      }
      resize();
      window.addEventListener('resize', resize);

      const particles = [];
      const particleCount = 38;
      for (let i = 0; i < particleCount; i++) {
        particles.push({
          x: Math.random() * w,
          y: Math.random() * h,
          r: Math.random() * 2.2 + 0.8,
          dx: (Math.random() - 0.5) * 0.4,
          dy: -Math.random() * 0.6 - 0.2,
          alpha: Math.random() * 0.45 + 0.1,
          color: Math.random() > 0.45 ? 'rgba(240, 167, 101, ' : 'rgba(46, 204, 113, '
        });
      }

      function loop() {
        ctx.clearRect(0, 0, w, h);
        for (let i = 0; i < particleCount; i++) {
          const p = particles[i];
          ctx.beginPath();
          ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
          ctx.fillStyle = p.color + p.alpha + ')';
          ctx.fill();

          p.x += p.dx;
          p.y += p.dy;
          if (p.y < -10) {
            p.y = h + 10;
            p.x = Math.random() * w;
          }
          if (p.x < -10) p.x = w + 10;
          if (p.x > w + 10) p.x = -10;
        }
        requestAnimationFrame(loop);
      }
      loop();
    })();

    // Interactive Growth Chart (Chart.js)
    document.addEventListener('DOMContentLoaded', () => {
      const ctx = document.getElementById('growthInteractiveChart');
      if (ctx && window.Chart) {
        new Chart(ctx, {
          type: 'line',
          data: {
            labels: ['Tuần 1', 'Tuần 2', 'Tuần 3', 'Tuần 4', 'Tuần 5', 'Tuần 6'],
            datasets: [
              {
                label: 'TikTok Followers',
                data: [60, 73, 137, 275, 261, 282],
                borderColor: '#2ECC71',
                backgroundColor: 'rgba(46, 204, 113, 0.1)',
                borderWidth: 3,
                tension: 0.35,
                fill: true,
                pointBackgroundColor: '#2ECC71',
                pointRadius: 6,
                pointHoverRadius: 8
              },
              {
                label: 'Instagram Followers',
                data: [55, 64, 79, 119, 122, 142],
                borderColor: '#E1306C',
                backgroundColor: 'transparent',
                borderWidth: 2.5,
                tension: 0.35,
                pointBackgroundColor: '#E1306C',
                pointRadius: 5,
                pointHoverRadius: 7
              },
              {
                label: 'Facebook Followers',
                data: [50, 56, 66, 79, 82, 100],
                borderColor: '#4267B2',
                backgroundColor: 'transparent',
                borderWidth: 2.5,
                tension: 0.35,
                pointBackgroundColor: '#4267B2',
                pointRadius: 5,
                pointHoverRadius: 7
              },
              {
                label: 'Landing Page Visits',
                data: [0, 0, 20, 280, 81, 20],
                borderColor: '#F0A765',
                backgroundColor: 'rgba(240, 167, 101, 0.08)',
                borderWidth: 2.5,
                borderDash: [6, 4],
                tension: 0.35,
                fill: true,
                pointBackgroundColor: '#F0A765',
                pointRadius: 5,
                pointHoverRadius: 7
              }
            ]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            interaction: {
              mode: 'index',
              intersect: false
            },
            plugins: {
              legend: {
                position: 'top',
                labels: {
                  color: '#FAF5EE',
                  usePointStyle: true,
                  padding: 18,
                  font: {
                    family: "'Plus Jakarta Sans', sans-serif",
                    size: 12.5,
                    weight: 600
                  }
                }
              },
              tooltip: {
                backgroundColor: 'rgba(17, 13, 9, 0.95)',
                titleColor: '#F0A765',
                bodyColor: '#FAF5EE',
                borderColor: 'rgba(240, 167, 101, 0.4)',
                borderWidth: 1.2,
                padding: 12,
                boxPadding: 6,
                usePointStyle: true,
                callbacks: {
                  label: function(context) {
                    let label = context.dataset.label || '';
                    if (label) label += ': ';
                    if (context.parsed.y !== null) {
                      label += context.parsed.y + (label.includes('Visits') ? ' lượt' : ' followers');
                    }
                    return label;
                  }
                }
              }
            },
            scales: {
              x: {
                grid: {
                  color: 'rgba(255, 255, 255, 0.06)'
                },
                ticks: {
                  color: '#A8A096',
                  font: {
                    family: "'Plus Jakarta Sans', sans-serif",
                    size: 12
                  }
                }
              },
              y: {
                beginAtZero: true,
                grid: {
                  color: 'rgba(255, 255, 255, 0.06)'
                },
                ticks: {
                  color: '#A8A096',
                  font: {
                    family: "'Plus Jakarta Sans', sans-serif",
                    size: 12
                  }
                }
              }
            }
          }
        });
      }
    });

    // Active Navigation ScrollSpy (Đồng bộ 100% với campaign-report.html)
    (function initScrollSpy() {
      const sections = document.querySelectorAll(".report-section");
      const menuLinks = document.querySelectorAll(".menu-link");
      const mobileLinks = document.querySelectorAll(".mobile-nav-link");

      function setActiveLink(id) {
        menuLinks.forEach(link => {
          const href = link.getAttribute("href");
          if (href === "#" + id) {
            link.classList.add("active");
          } else {
            link.classList.remove("active");
          }
        });

        mobileLinks.forEach(link => {
          const href = link.getAttribute("href");
          if (href === "#" + id) {
            link.classList.add("active");
          } else {
            link.classList.remove("active");
          }
        });
      }

      document.querySelectorAll(".menu-link, .mobile-nav-link").forEach(link => {
        link.addEventListener("click", function(e) {
          const href = this.getAttribute("href");
          if (href && href.startsWith("#")) {
            const targetId = href.substring(1);
            setActiveLink(targetId);
          }
        });
      });

      function onScroll() {
        const scrollPos = window.scrollY + 140;
        let currentSectionId = null;

        sections.forEach(section => {
          const top = section.offsetTop;
          const height = section.offsetHeight;
          if (scrollPos >= top && scrollPos < top + height) {
            currentSectionId = section.getAttribute("id");
          }
        });

        if (!currentSectionId && window.scrollY < 200) {
          currentSectionId = "muc-1";
        } else if (!currentSectionId && (window.innerHeight + window.scrollY) >= document.body.offsetHeight - 80) {
          currentSectionId = "muc-9";
        }

        if (currentSectionId) {
          setActiveLink(currentSectionId);
        }
      }

      let isThrottled = false;
      window.addEventListener("scroll", () => {
        if (!isThrottled) {
          window.requestAnimationFrame(() => {
            onScroll();
            isThrottled = false;
          });
          isThrottled = true;
        }
      }, { passive: true });

      function checkInitialHash() {
        if (window.location.hash) {
          const hashId = window.location.hash.substring(1);
          const target = document.getElementById(hashId);
          if (target) {
            setActiveLink(hashId);
            return;
          }
        }
        onScroll();
      }

      if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", checkInitialHash);
      } else {
        checkInitialHash();
      }
      window.addEventListener("hashchange", checkInitialHash);
    })();

  </script>
</body>
</html>
"""

    html = html.replace("__CSS__", full_css)
    with open('cuoi-ky.html', 'w', encoding='utf-8') as f:
        f.write(html)
    with open('bao-cao-cuoi-ky.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("cuoi-ky.html and bao-cao-cuoi-ky.html generated successfully!")

if __name__ == '__main__':
    build_cuoi_ky_report()
