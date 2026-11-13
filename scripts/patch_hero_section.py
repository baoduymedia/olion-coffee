import re

def update_hero():
    with open('scripts/build_cuoi_ky_final.py', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add Hero CSS to extra_css if not present
    hero_css = """
    /* ========================================================
       HERO SECTION ENHANCEMENTS (LUXURY CAFE REPORT AESTHETIC)
       ======================================================== */
    .hero-title {
      font-family: var(--font-serif);
      font-size: clamp(26px, 4.2vw, 50px);
      font-weight: 700;
      line-height: 1.22;
      color: #FFFFFF;
      margin-bottom: 18px;
    }
    .hero-title-main {
      display: block;
      color: #FFFFFF;
      margin-bottom: 6px;
      letter-spacing: -0.01em;
    }
    .hero-title-sub {
      display: block;
      font-size: clamp(20px, 3.4vw, 36px);
      line-height: 1.3;
    }
    .hero-lead {
      font-size: clamp(15px, 1.8vw, 17.5px);
      color: var(--crema);
      max-width: 860px;
      line-height: 1.75;
      margin-bottom: 24px;
      opacity: 0.95;
    }

    /* Slogan Ribbon Callout */
    .hero-slogan-card {
      background: radial-gradient(ellipse 90% 80% at 50% 0%, rgba(240, 167, 101, 0.15) 0%, rgba(22, 16, 12, 0.94) 100%);
      border: 1.5px solid var(--border-brass);
      border-radius: var(--radius-md);
      padding: 20px 24px;
      margin: 20px 0 28px;
      box-shadow: 0 12px 30px rgba(0, 0, 0, 0.65), inset 0 1px 0 rgba(255, 255, 255, 0.1);
      position: relative;
      overflow: hidden;
    }
    .hero-slogan-card::before {
      content: '';
      position: absolute;
      top: 0;
      left: 10%;
      right: 10%;
      height: 2px;
      background: linear-gradient(90deg, transparent, var(--accent-gold), transparent);
    }
    .hero-slogan-badge {
      font-size: 11.5px;
      font-weight: 800;
      color: var(--accent-gold-light);
      text-transform: uppercase;
      letter-spacing: 0.12em;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 8px;
    }
    .hero-slogan-quote {
      font-family: var(--font-serif);
      font-size: clamp(18px, 2.5vw, 24px);
      font-style: italic;
      font-weight: 600;
      color: #FFFFFF;
      line-height: 1.4;
      text-shadow: 0 2px 12px rgba(0, 0, 0, 0.8);
    }
    .hero-slogan-vi {
      font-size: 13.5px;
      color: var(--crema);
      opacity: 0.88;
      margin-top: 6px;
      line-height: 1.5;
    }

    /* Hero Banner Image Box */
    .hero-banner-image-box {
      width: 100%;
      border-radius: var(--radius-lg);
      overflow: hidden;
      border: 2px solid var(--border-brass);
      box-shadow: var(--shadow-wood), 0 15px 40px rgba(0, 0, 0, 0.7);
      margin: 24px 0 32px;
      background: #000;
      position: relative;
      transition: all 0.3s ease;
    }
    .hero-banner-image-box:hover {
      border-color: var(--accent-gold);
      box-shadow: 0 20px 50px rgba(240, 167, 101, 0.25);
    }
    .hero-banner-image {
      width: 100%;
      height: auto;
      display: block;
      transition: transform 0.45s ease;
    }
    .hero-banner-image-box:hover .hero-banner-image {
      transform: scale(1.02);
    }
    .hero-banner-caption {
      padding: 13px 20px;
      background: rgba(18, 14, 10, 0.96);
      font-size: 14.5px;
      color: var(--accent-gold-light);
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-top: 1px solid var(--border-brass);
      gap: 12px;
      flex-wrap: wrap;
    }
    @media (max-width: 640px) {
      .hero-banner-caption {
        font-size: 12.5px;
        padding: 10px 14px;
      }
    }
    .hero-banner-caption strong {
      color: #FFFFFF;
    }
    .hero-banner-caption .caption-tag {
      font-size: 12px;
      color: var(--matcha-green);
      display: inline-flex;
      align-items: center;
      gap: 5px;
      background: rgba(46, 204, 113, 0.12);
      padding: 3px 10px;
      border-radius: var(--radius-full);
      border: 1px solid rgba(46, 204, 113, 0.3);
      white-space: nowrap;
    }

    /* Hero Stat Strip (4 Luxury Cards) */
    .hero-stat-strip {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
      margin: 28px 0 10px;
    }
    @media (max-width: 960px) {
      .hero-stat-strip {
        grid-template-columns: repeat(2, 1fr);
        gap: 12px;
      }
    }
    @media (max-width: 480px) {
      .hero-stat-strip {
        grid-template-columns: repeat(2, 1fr);
        gap: 10px;
      }
    }
    .hero-stat-item {
      background: linear-gradient(145deg, rgba(28, 20, 15, 0.94) 0%, rgba(16, 11, 8, 0.98) 100%);
      border: 1.5px solid rgba(240, 167, 101, 0.28);
      border-radius: var(--radius-md);
      padding: 18px 16px;
      text-align: center;
      position: relative;
      overflow: hidden;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.55), inset 0 1px 0 rgba(255, 255, 255, 0.06);
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
    }
    .hero-stat-item:hover {
      transform: translateY(-4px);
      border-color: var(--accent-gold);
      box-shadow: 0 14px 32px rgba(240, 167, 101, 0.24);
    }
    .hero-stat-item::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 2.5px;
      background: linear-gradient(90deg, transparent, var(--accent-gold), transparent);
    }
    .hero-stat-item.matcha-card {
      border-color: rgba(46, 204, 113, 0.28);
    }
    .hero-stat-item.matcha-card::before {
      background: linear-gradient(90deg, transparent, var(--matcha-green), transparent);
    }
    .hero-stat-item.matcha-card:hover {
      border-color: var(--matcha-green);
      box-shadow: 0 14px 32px rgba(46, 204, 113, 0.24);
    }
    .hero-stat-icon {
      width: 36px;
      height: 36px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 8px;
      background: rgba(240, 167, 101, 0.14);
      border: 1px solid rgba(240, 167, 101, 0.35);
      color: var(--accent-gold);
    }
    .hero-stat-item.matcha-card .hero-stat-icon {
      background: rgba(46, 204, 113, 0.14);
      border-color: rgba(46, 204, 113, 0.35);
      color: var(--matcha-green);
    }
    .hero-stat-num {
      font-family: var(--font-serif);
      font-size: clamp(24px, 3.2vw, 34px);
      font-weight: 800;
      line-height: 1.15;
      margin-bottom: 4px;
    }
    .hero-stat-lbl {
      font-size: 11.5px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--text-muted);
      line-height: 1.35;
    }
    .hero-stat-sub {
      font-size: 11px;
      color: var(--warm-gray);
      margin-top: 3px;
    }
    """

    if '.hero-stat-strip' not in content:
        # Insert hero_css right before full_css = base_css + "\n" + extra_css
        idx = content.find('full_css = base_css + "\\n" + extra_css')
        if idx != -1:
            # find end of extra_css before this
            idx_quote = content.rfind('"""', 0, idx)
            content = content[:idx_quote] + "\n" + hero_css + content[idx_quote:]
            print("Hero CSS inserted into extra_css.")

    # 2. Replace Hero Section HTML
    new_hero_html = """  <!-- ========================================================
       HERO BANNER CHÍNH THỨC VỚI HÌNH ẢNH CHIẾN DỊCH VÀ 4 STATS
       ======================================================== -->
  <section class="hero-section">
    <div class="shell">
      <div class="hero-eyebrow">
        <span class="dot"></span>
        <span>BÁO CÁO TỔNG KẾT HỌC PHẦN IMC &bull; ĐẠI HỌC VĂN LANG</span>
      </div>

      <h1 class="hero-title">
        <span class="hero-title-main">Báo Cáo Cuối Kỳ: Chiến Dịch Truyền Thông Số</span>
        <span class="hero-title-sub"><span class="text-matcha">Olion Coffee</span> — <span class="text-gold">Quán Cà Phê Cho Sinh Viên VLU</span></span>
      </h1>

      <p class="hero-lead">
        Chiến dịch truyền thông số đa kênh (Facebook, Instagram, TikTok &amp; Landing Page) được triển khai thực tế qua 6 tuần bởi <strong>Nhóm 7 — Gỗ Xà Cừ</strong>. Mục tiêu xây dựng nhận diện thương hiệu, kết nối sinh viên ĐH Văn Lang và tối ưu chuyển đổi khách hàng tại Cơ sở 3 Gò Vấp.
      </p>

      <!-- Slogan Callout Ribbon -->
      <div class="hero-slogan-card">
        <div class="hero-slogan-badge">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m12 3-1.9 5.8a2 2 0 0 1-1.3 1.3L3 12l5.8 1.9a2 2 0 0 1 1.3 1.3L12 21l1.9-5.8a2 2 0 0 1 1.3-1.3L21 12l-5.8-1.9a2 2 0 0 1-1.3-1.3Z"/></svg>
          <span>Thông Điệp Cốt Lõi Thương Hiệu (Core Philosophy)</span>
        </div>
        <div class="hero-slogan-quote">“Take your time. Find your moment. Begin again.”</div>
        <div class="hero-slogan-vi">Hãy cứ thong thả. Tìm lấy khoảnh khắc của riêng mình. Và bắt đầu lại.</div>
      </div>

      <!-- Hình ảnh 4 ly Matcha Series & Không gian Olion Coffee chính thức -->
      <div class="hero-banner-image-box" onclick="openLightbox('assets/matcha-series-banner.jpg', 'Bộ Tứ Matcha Series — Olion Coffee (Chiến Dịch Quảng Cáo Chính Thức)')" style="cursor: zoom-in;">
        <img src="assets/matcha-series-banner.jpg" alt="Olion Matcha Series: Matcha Bạc Hà, Matcha Dừa, Matcha Dâu, Matcha Espresso Latte" class="hero-banner-image" loading="eager" />
        <div class="hero-banner-caption">
          <span class="caption-title">🍵 <strong>Bộ Tứ Matcha Series:</strong> Matcha Bạc Hà &bull; Matcha Dừa &bull; Matcha Dâu &bull; Matcha Espresso Latte</span>
          <span class="caption-tag"><i data-lucide="zoom-in" style="width:13px;height:13px;display:inline-block;vertical-align:middle;margin-right:3px;"></i>Chiến dịch quảng cáo chính thức</span>
        </div>
      </div>

      <!-- Hero Stat Strip: 4 Luxury Glassmorphic Metric Cards -->
      <div class="hero-stat-strip">
        <div class="hero-stat-item">
          <div class="hero-stat-icon">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
          </div>
          <div class="hero-stat-num text-gold">6 Tuần</div>
          <div class="hero-stat-lbl">Thời Gian Triển Khai</div>
          <div class="hero-stat-sub">Tháng 10 &bull; Tháng 11/2026</div>
        </div>

        <div class="hero-stat-item matcha-card">
          <div class="hero-stat-icon">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>
          </div>
          <div class="hero-stat-num text-matcha">4 Kênh</div>
          <div class="hero-stat-lbl">Hệ Sinh Thái Số</div>
          <div class="hero-stat-sub">FB &bull; IG &bull; TikTok &bull; Web</div>
        </div>

        <div class="hero-stat-item">
          <div class="hero-stat-icon">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
          </div>
          <div class="hero-stat-num text-gold">15.656+</div>
          <div class="hero-stat-lbl">Lượt Tiếp Cận (Reach)</div>
          <div class="hero-stat-sub">Tổng 4 nền tảng số</div>
        </div>

        <div class="hero-stat-item matcha-card">
          <div class="hero-stat-icon">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><line x1="19" y1="8" x2="19" y2="14"/><line x1="22" y1="11" x2="16" y2="11"/></svg>
          </div>
          <div class="hero-stat-num text-matcha">11 Bạn</div>
          <div class="hero-stat-lbl">Nhóm 7 (Gỗ Xà Cừ)</div>
          <div class="hero-stat-sub">ĐH Văn Lang &bull; K28</div>
        </div>
      </div>
    </div>
  </section>"""

    # Locate the hero section in HTML string
    hero_pattern = re.compile(r'<!-- =+\s+HERO BANNER CHÍNH THỨC.*?<!-- =+\s+MỤC 1: TỔNG QUAN', re.DOTALL)
    match = hero_pattern.search(content)
    if match:
        content = content[:match.start()] + new_hero_html + "\n\n  " + content[match.end()-len('<!-- ========================================================\n       MỤC 1: TỔNG QUAN'):]
        print("Hero HTML successfully updated!")
    else:
        print("Could not match hero section regex pattern, checking fallback...")
        # fallback search
        start_tag = '<!-- ========================================================\n       HERO BANNER CHÍNH THỨC'
        end_tag = '<!-- ========================================================\n       MỤC 1: TỔNG QUAN'
        p1 = content.find(start_tag)
        p2 = content.find(end_tag, p1)
        if p1 != -1 and p2 != -1:
            content = content[:p1] + new_hero_html + "\n\n  " + content[p2:]
            print("Hero HTML updated using string indices!")
        else:
            print("Fallback also failed!")

    with open('scripts/build_cuoi_ky_final.py', 'w', encoding='utf-8') as f:
        f.write(content)

    print("build_cuoi_ky_final.py written successfully.")

if __name__ == '__main__':
    update_hero()
