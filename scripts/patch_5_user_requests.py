import re

def apply_5_requests():
    with open('scripts/build_cuoi_ky_final.py', 'r', encoding='utf-8') as f:
        content = f.read()

    # =========================================================================
    # 1. NEW CSS FOR ALL 5 REQUESTS
    # =========================================================================
    custom_css = """
    /* ========================================================
       CẢI TIẾN THEO 5 YÊU CẦU NGƯỜI DÙNG (USER FEEDBACK PATCH)
       ======================================================== */

    /* 1. SECTION 4: TÁCH 2 BIỂU ĐỒ 6 TUẦN ĐỂ KHÔNG BỊ CROP */
    .chart-evidence-grid {
      display: flex !important;
      flex-direction: column !important;
      gap: 30px !important;
      margin: 24px 0 !important;
    }
    .chart-evidence-card {
      background: linear-gradient(145deg, rgba(28, 20, 15, 0.94) 0%, rgba(16, 11, 8, 0.98) 100%) !important;
      border: 1.5px solid var(--border-brass) !important;
      border-radius: var(--radius-md) !important;
      overflow: hidden !important;
      box-shadow: var(--shadow-wood) !important;
      cursor: pointer !important;
      transition: all 0.35s ease !important;
      width: 100% !important;
    }
    .chart-evidence-card:hover {
      transform: translateY(-4px) !important;
      border-color: var(--accent-gold) !important;
      box-shadow: 0 16px 36px rgba(0,0,0,0.85), 0 0 18px var(--accent-gold-glow) !important;
    }
    .chart-evidence-media {
      position: relative !important;
      background: #FFFFFF !important;
      overflow: hidden !important;
      width: 100% !important;
      aspect-ratio: auto !important;
      display: flex !important;
      align-items: center !important;
      justify-content: center !important;
      padding: 14px 18px !important;
      min-height: 220px !important;
    }
    .chart-evidence-img {
      width: 100% !important;
      height: auto !important;
      max-height: 540px !important;
      object-fit: contain !important;
      display: block !important;
      border-radius: 4px !important;
    }

    /* 2. SECTION 5: BÀI ĐĂNG NGANG FACEBOOK LÊN 1 HÀNG RIÊNG */
    .social-post-card.featured-horizontal {
      display: grid !important;
      grid-template-columns: 1.35fr 1fr !important;
      margin-bottom: 24px !important;
      background: linear-gradient(145deg, #18120D 0%, #100C08 100%) !important;
      border: 1.5px solid var(--border-brass) !important;
      border-radius: var(--radius-md) !important;
      overflow: hidden !important;
      box-shadow: var(--shadow-wood) !important;
      cursor: pointer !important;
      transition: all 0.35s ease !important;
    }
    .social-post-card.featured-horizontal:hover {
      transform: translateY(-4px) !important;
      border-color: var(--accent-gold) !important;
      box-shadow: 0 16px 36px rgba(0,0,0,0.85), 0 0 20px var(--accent-gold-glow) !important;
    }
    @media (max-width: 860px) {
      .social-post-card.featured-horizontal {
        grid-template-columns: 1fr !important;
      }
    }
    .social-showcase-grid.cols-2 {
      display: grid !important;
      grid-template-columns: repeat(2, 1fr) !important;
      gap: 20px !important;
    }
    @media (max-width: 768px) {
      .social-showcase-grid.cols-2 {
        grid-template-columns: 1fr !important;
      }
    }

    /* 3. SECTION 6: BẢNG SO SÁNH CHO CHỮ XUỐNG HÀNG TỰ NHIÊN (WRAP TEXT) */
    .wrap-content-table {
      width: 100% !important;
      border-collapse: collapse !important;
      text-align: left !important;
      font-size: 14.5px !important;
      white-space: normal !important;
      table-layout: auto !important;
    }
    .wrap-content-table th,
    .wrap-content-table td {
      white-space: normal !important;
      word-break: normal !important;
      overflow-wrap: break-word !important;
      line-height: 1.6 !important;
      padding: 14px 16px !important;
      vertical-align: top !important;
    }
    .wrap-content-table th {
      background: rgba(240, 167, 101, 0.16) !important;
      color: var(--accent-gold-light) !important;
      font-weight: 800 !important;
      text-transform: uppercase !important;
      font-size: 13px !important;
      letter-spacing: 0.08em !important;
      position: sticky;
      top: 0;
    }
    .wrap-content-table td {
      border-bottom: 1px solid rgba(255, 255, 255, 0.08) !important;
    }
    .wrap-content-table th:nth-child(1),
    .wrap-content-table td:nth-child(1) {
      width: 18% !important;
      min-width: 130px !important;
      font-weight: 700 !important;
    }
    .wrap-content-table th:nth-child(2),
    .wrap-content-table td:nth-child(2) {
      width: 28% !important;
      min-width: 170px !important;
    }
    .wrap-content-table th:nth-child(3),
    .wrap-content-table td:nth-child(3) {
      width: 30% !important;
      min-width: 190px !important;
    }
    .wrap-content-table th:nth-child(4),
    .wrap-content-table td:nth-child(4) {
      width: 24% !important;
      min-width: 160px !important;
    }

    /* 4. SECTION 8: THIẾT KẾ LẠI MỤC TIÊU 3 THÁNG HIỆN ĐẠI & ĐẸP MẮT */
    .sec8-strategy-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 20px;
      margin: 24px 0 32px;
    }
    @media (max-width: 768px) {
      .sec8-strategy-grid {
        grid-template-columns: 1fr;
        gap: 16px;
      }
    }
    .sec8-channel-card {
      background: linear-gradient(145deg, rgba(26, 19, 14, 0.95) 0%, rgba(16, 11, 8, 0.98) 100%);
      border: 1.5px solid var(--border-brass);
      border-radius: var(--radius-md);
      padding: 22px 24px;
      box-shadow: var(--shadow-wood);
      transition: all 0.3s ease;
      position: relative;
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }
    .sec8-channel-card:hover {
      transform: translateY(-4px);
      border-color: var(--accent-gold);
      box-shadow: 0 14px 32px rgba(240, 167, 101, 0.22);
    }
    .sec8-channel-card.matcha-accent {
      border-color: rgba(46, 204, 113, 0.35);
    }
    .sec8-channel-card.matcha-accent:hover {
      border-color: var(--matcha-green);
      box-shadow: 0 14px 32px rgba(46, 204, 113, 0.22);
    }
    .sec8-card-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 14px;
      padding-bottom: 12px;
      border-bottom: 1px dashed rgba(255, 255, 255, 0.1);
    }
    .sec8-card-brand {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .sec8-card-icon {
      width: 36px;
      height: 36px;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }
    .sec8-card-icon.gold {
      background: rgba(240, 167, 101, 0.15);
      border: 1px solid rgba(240, 167, 101, 0.4);
      color: var(--accent-gold);
    }
    .sec8-card-icon.matcha {
      background: rgba(46, 204, 113, 0.15);
      border: 1px solid rgba(46, 204, 113, 0.4);
      color: var(--matcha-green);
    }
    .sec8-card-icon.ig {
      background: rgba(225, 48, 108, 0.15);
      border: 1px solid rgba(225, 48, 108, 0.4);
      color: #E1306C;
    }
    .sec8-card-name {
      font-size: 17px;
      font-weight: 700;
      color: var(--crema);
    }
    .sec8-card-badge {
      font-size: 11px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      padding: 3px 10px;
      border-radius: 999px;
      white-space: nowrap;
    }
    .sec8-card-badge.gold {
      background: rgba(240, 167, 101, 0.15);
      color: var(--accent-gold-light);
      border: 1px solid rgba(240, 167, 101, 0.35);
    }
    .sec8-card-badge.matcha {
      background: rgba(46, 204, 113, 0.15);
      color: var(--matcha-green);
      border: 1px solid rgba(46, 204, 113, 0.35);
    }
    .sec8-kpi-pill {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(0, 0, 0, 0.45);
      border: 1px solid rgba(255, 255, 255, 0.12);
      padding: 6px 12px;
      border-radius: 8px;
      font-size: 13px;
      color: var(--accent-gold);
      margin-bottom: 12px;
    }
    .sec8-card-desc {
      font-size: 13.5px;
      color: var(--text-muted);
      line-height: 1.55;
    }
    .sec8-card-desc strong {
      color: var(--crema);
    }

    /* 3-Month KPI Target Showcase */
    .sec8-targets-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
      margin: 24px 0 28px;
    }
    @media (max-width: 900px) {
      .sec8-targets-grid {
        grid-template-columns: repeat(2, 1fr);
      }
    }
    @media (max-width: 480px) {
      .sec8-targets-grid {
        grid-template-columns: repeat(2, 1fr);
        gap: 10px;
      }
    }
    .sec8-target-item {
      background: linear-gradient(145deg, rgba(28, 20, 15, 0.94) 0%, rgba(16, 11, 8, 0.98) 100%);
      border: 1.5px solid rgba(240, 167, 101, 0.28);
      border-radius: var(--radius-md);
      padding: 18px 16px;
      text-align: center;
      box-shadow: 0 8px 24px rgba(0,0,0,0.55);
      transition: all 0.3s ease;
      position: relative;
      overflow: hidden;
    }
    .sec8-target-item::before {
      content: '';
      position: absolute;
      top: 0; left: 0; right: 0;
      height: 2.5px;
      background: linear-gradient(90deg, transparent, var(--accent-gold), transparent);
    }
    .sec8-target-item.matcha::before {
      background: linear-gradient(90deg, transparent, var(--matcha-green), transparent);
    }
    .sec8-target-item:hover {
      transform: translateY(-3px);
      border-color: var(--accent-gold);
      box-shadow: 0 12px 28px rgba(240, 167, 101, 0.2);
    }
    .sec8-target-num {
      font-family: var(--font-serif);
      font-size: clamp(24px, 3.4vw, 36px);
      font-weight: 800;
      line-height: 1.15;
      margin-bottom: 4px;
    }
    .sec8-target-lbl {
      font-size: 12px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--text-muted);
    }
    .sec8-target-cadence {
      font-size: 11.5px;
      color: var(--warm-gray);
      margin-top: 4px;
    }

    /* 5. SECTION 9: BẢNG GIA PHẢ NHÓM 7 (ORG HIERARCHY TREE) */
    .org-tree-container {
      margin-top: 28px;
      position: relative;
    }
    /* Node Trưởng Nhóm Đỉnh Cây */
    .org-tree-root {
      display: flex;
      flex-direction: column;
      align-items: center;
      position: relative;
      margin-bottom: 36px;
    }
    .org-leader-card {
      background: radial-gradient(circle at 50% 20%, rgba(240, 167, 101, 0.18) 0%, rgba(20, 14, 10, 0.98) 80%);
      border: 2px solid var(--accent-gold);
      border-radius: var(--radius-lg);
      padding: 20px 28px;
      max-width: 520px;
      width: 100%;
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.85), 0 0 24px rgba(240, 167, 101, 0.28);
      display: flex;
      align-items: center;
      gap: 20px;
      cursor: pointer;
      transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
      position: relative;
    }
    .org-leader-card:hover {
      transform: translateY(-5px);
      border-color: var(--accent-gold-light);
      box-shadow: 0 22px 50px rgba(0, 0, 0, 0.9), 0 0 32px rgba(240, 167, 101, 0.4);
    }
    .org-avatar-box {
      position: relative;
      flex-shrink: 0;
    }
    .org-avatar-img {
      width: 88px;
      height: 88px;
      border-radius: 50%;
      object-fit: cover;
      object-position: top center;
      display: block;
      border: 2.5px solid var(--accent-gold);
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.7);
      transition: transform 0.3s ease;
    }
    .org-leader-card:hover .org-avatar-img {
      transform: scale(1.06);
    }
    .org-crown-badge {
      position: absolute;
      top: -8px;
      right: -6px;
      background: var(--accent-gold);
      color: #000;
      width: 26px;
      height: 26px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 2px 8px rgba(0,0,0,0.6);
      font-size: 13px;
    }
    .org-leader-info {
      flex: 1;
    }
    .org-leader-name {
      font-family: var(--font-serif);
      font-size: 22px;
      font-weight: 700;
      color: #FFFFFF;
      margin-bottom: 3px;
    }
    .org-leader-role {
      font-size: 13px;
      font-weight: 800;
      color: var(--accent-gold);
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 6px;
    }
    .org-leader-desc {
      font-size: 12.5px;
      color: var(--warm-gray);
      line-height: 1.45;
    }

    /* Thân Dây Cây Gia Phả (Tree Connectors) */
    .org-tree-stem {
      width: 2px;
      height: 36px;
      background: linear-gradient(180deg, var(--accent-gold), rgba(240, 167, 101, 0.6));
      margin: 0 auto;
    }
    .org-tree-branches-bar {
      height: 2px;
      background: linear-gradient(90deg, transparent, rgba(46, 204, 113, 0.8) 15%, var(--accent-gold) 50%, rgba(46, 204, 113, 0.8) 85%, transparent);
      width: 88%;
      margin: 0 auto 30px;
      position: relative;
    }
    .org-tree-branches-bar::before,
    .org-tree-branches-bar::after {
      content: '';
      position: absolute;
      top: -4px;
      width: 10px;
      height: 10px;
      border-radius: 50%;
      background: var(--accent-gold);
      box-shadow: 0 0 8px var(--accent-gold);
    }
    .org-tree-branches-bar::before { left: 14%; }
    .org-tree-branches-bar::after { right: 14%; }

    /* Lưới 4 Chi Nhánh Ban Chuyên Môn (4 Departments) */
    .org-branches-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 20px;
      position: relative;
    }
    @media (max-width: 1100px) {
      .org-branches-grid {
        grid-template-columns: repeat(2, 1fr);
        gap: 24px;
      }
      .org-tree-branches-bar { display: none; }
    }
    @media (max-width: 640px) {
      .org-branches-grid {
        grid-template-columns: 1fr;
        gap: 20px;
      }
    }
    .org-branch-column {
      background: linear-gradient(145deg, rgba(22, 16, 12, 0.95) 0%, rgba(14, 10, 7, 0.98) 100%);
      border: 1.5px solid var(--border-brass);
      border-radius: var(--radius-md);
      padding: 18px 16px;
      box-shadow: var(--shadow-wood);
      display: flex;
      flex-direction: column;
      position: relative;
    }
    .org-branch-column.matcha-theme {
      border-color: rgba(46, 204, 113, 0.35);
    }
    .org-branch-header {
      display: flex;
      align-items: center;
      gap: 8px;
      padding-bottom: 12px;
      margin-bottom: 16px;
      border-bottom: 1px dashed rgba(255, 255, 255, 0.12);
    }
    .org-branch-header.matcha-theme {
      border-bottom-color: rgba(46, 204, 113, 0.25);
    }
    .org-branch-icon {
      width: 28px;
      height: 28px;
      border-radius: 6px;
      display: flex;
      align-items: center;
      justify-content: center;
      background: rgba(240, 167, 101, 0.15);
      border: 1px solid rgba(240, 167, 101, 0.35);
      color: var(--accent-gold);
      flex-shrink: 0;
    }
    .org-branch-column.matcha-theme .org-branch-icon {
      background: rgba(46, 204, 113, 0.15);
      border-color: rgba(46, 204, 113, 0.35);
      color: var(--matcha-green);
    }
    .org-branch-title {
      font-size: 13.5px;
      font-weight: 800;
      color: var(--accent-gold);
      text-transform: uppercase;
      letter-spacing: 0.08em;
    }
    .org-branch-column.matcha-theme .org-branch-title {
      color: var(--matcha-green);
    }

    /* Danh Sách Thẻ Thành Viên Gọn Gàng Trong Từng Ban */
    .org-members-list {
      display: flex;
      flex-direction: column;
      gap: 14px;
    }
    .org-member-mini-card {
      background: rgba(10, 8, 6, 0.75);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: var(--radius-sm);
      padding: 12px 14px;
      display: flex;
      align-items: center;
      gap: 14px;
      cursor: pointer;
      transition: all 0.25s ease;
      position: relative;
    }
    .org-member-mini-card:hover {
      transform: translateY(-3px);
      border-color: var(--accent-gold);
      background: rgba(24, 18, 13, 0.95);
      box-shadow: 0 8px 20px rgba(0, 0, 0, 0.6);
    }
    .org-branch-column.matcha-theme .org-member-mini-card:hover {
      border-color: var(--matcha-green);
      box-shadow: 0 8px 20px rgba(46, 204, 113, 0.15);
    }
    .org-mini-avatar-box {
      position: relative;
      flex-shrink: 0;
    }
    .org-mini-avatar {
      width: 64px;
      height: 64px;
      border-radius: 50%;
      object-fit: cover;
      object-position: top center;
      display: block;
      border: 1.5px solid var(--accent-gold);
      box-shadow: 0 3px 10px rgba(0,0,0,0.6);
      transition: transform 0.3s ease;
    }
    .org-branch-column.matcha-theme .org-mini-avatar {
      border-color: var(--matcha-green);
    }
    .org-member-mini-card:hover .org-mini-avatar {
      transform: scale(1.08);
    }
    .org-mini-info {
      flex: 1;
      min-width: 0;
    }
    .org-mini-name {
      font-size: 15px;
      font-weight: 700;
      color: var(--crema);
      margin-bottom: 2px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .org-mini-role {
      font-size: 11px;
      font-weight: 800;
      color: var(--accent-gold);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 4px;
    }
    .org-branch-column.matcha-theme .org-mini-role {
      color: var(--matcha-green);
    }
    .org-mini-desc {
      font-size: 11.5px;
      color: var(--text-muted);
      line-height: 1.4;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }
    """

    # Add custom_css to extra_css
    idx_extra = content.find('full_css = base_css + "\\n" + extra_css')
    if idx_extra != -1:
        idx_quote = content.rfind('"""', 0, idx_extra)
        content = content[:idx_quote] + "\n" + custom_css + content[idx_quote:]
        print("1. Custom CSS added to extra_css.")

    # =========================================================================
    # 2. UPDATE SECTION 4 (TÁCH 2 BIỂU ĐỒ RA 2 HÀNG ĐỂ KHÔNG BỊ CROP)
    # =========================================================================
    sec4_old = """      <!-- Bộ 2 Ảnh Minh Chứng Biểu Đồ từ Báo Cáo Gốc (Evidence Screenshots) -->
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
      </div>"""

    sec4_new = """      <!-- Bộ 2 Ảnh Minh Chứng Biểu Đồ từ Báo Cáo Gốc (Đã tách thành 2 hàng riêng, hiển thị 100% không bị crop) -->
      <div class="proof-showcase-box matcha-theme">
        <div class="proof-showcase-header matcha-theme">
          <div class="proof-header-left">
            <span class="proof-header-badge matcha"><i data-lucide="image" style="width:13px;height:13px;"></i> ẢNH MINH CHỨNG TÀI LIỆU GỐC</span>
            <h3 class="proof-header-title">Biểu Đồ Theo Dõi Tăng Trưởng Trích Xuất Từ Báo Cáo (Nguyên Bản 6 Tuần)</h3>
          </div>
          <div class="proof-header-hint"><i data-lucide="zoom-in" style="width:13px;height:13px;"></i> Nhấp ảnh để phóng to chi tiết</div>
        </div>

        <div class="chart-evidence-grid">
          <!-- Ảnh Minh Chứng 1: Biểu đồ người theo dõi (Hàng 1 riêng biệt) -->
          <div class="chart-evidence-card" onclick="openLightbox('assets/cuoi-ky/chart-followers-6tuan.webp', 'Biểu đồ biến động người theo dõi trên Facebook, Instagram và TikTok qua 6 tuần', 'Trích nguyên văn từ tài liệu Báo cáo cuối kỳ Nhóm 7 — Gỗ Xà Cừ')">
            <div class="chart-evidence-media">
              <img src="assets/cuoi-ky/chart-followers-6tuan.webp" alt="Biểu đồ biến động người theo dõi 6 tuần" class="chart-evidence-img" />
              <div class="proof-card-zoom-badge"><i data-lucide="zoom-in" style="width:11px;height:11px;"></i> Phóng to chi tiết</div>
            </div>
            <div class="chart-evidence-info">
              <div class="chart-evidence-title">📈 Biểu đồ 1: Biến động Người theo dõi (Follower) trên 3 Kênh qua 6 tuần</div>
              <div class="chart-evidence-note">Facebook tăng trưởng đều đặn từ 50 lên 100 followers; Instagram tăng từ 55 lên 142 followers; TikTok bứt phá mạnh mẽ nhất đạt 275 followers ở tuần 4 và chạm mốc 282 followers ở tuần 6.</div>
            </div>
          </div>

          <!-- Ảnh Minh Chứng 2: Biểu đồ Landing page visits (Hàng 2 riêng biệt) -->
          <div class="chart-evidence-card" onclick="openLightbox('assets/cuoi-ky/chart-landing-page-visits-6tuan.webp', 'Lượt truy cập Landing Page theo từng tuần (Cloudflare Analytics)', 'Trích nguyên văn từ tài liệu Báo cáo cuối kỳ Nhóm 7 — Gỗ Xà Cừ')">
            <div class="chart-evidence-media">
              <img src="assets/cuoi-ky/chart-landing-page-visits-6tuan.webp" alt="Biểu đồ lượt truy cập Landing Page qua 6 tuần" class="chart-evidence-img" />
              <div class="proof-card-zoom-badge"><i data-lucide="zoom-in" style="width:11px;height:11px;"></i> Phóng to chi tiết</div>
            </div>
            <div class="chart-evidence-info">
              <div class="chart-evidence-title">📊 Biểu đồ 2: Lượt truy cập Landing Page (Visits) theo từng tuần</div>
              <div class="chart-evidence-note">Tuần 1–2 chưa triển khai gắn link; Tuần 3 bắt đầu ghi nhận 30 visits; Tuần 4 bùng nổ kỷ lục 280 visits (sau khi chủ động gắn link dưới bài đăng FB); Tuần 5 duy trì 51 visits và Tuần 6 đạt 10 visits. Tổng chiến dịch đạt 381 visits.</div>
            </div>
          </div>
        </div>
      </div>"""

    if sec4_old in content:
        content = content.replace(sec4_old, sec4_new)
        print("2. Section 4 updated (Separated charts, 100% uncropped).")
    else:
        print("WARNING: Section 4 old snippet not found directly, checking...")

    # =========================================================================
    # 3. UPDATE SECTION 5 (CHO ẢNH NGANG FACEBOOK LÊN 1 HÀNG RIÊNG)
    # =========================================================================
    sec5_old = """      <!-- 1. KÊNH FACEBOOK -->
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
      </div>"""

    sec5_new = """      <!-- 1. KÊNH FACEBOOK -->
      <div style="margin-bottom:45px;">
        <h3 style="font-family:var(--font-serif);font-size:24px;color:var(--accent-gold);margin-bottom:16px;display:flex;align-items:center;gap:10px;">
          <i data-lucide="facebook" style="width:22px;height:22px;"></i> Kênh Facebook Fanpage — Trọng Tâm Nhận Diện &amp; Hương Vị
        </h3>

        <!-- HÀNG 1 RIÊNG BIỆT: Bài đăng định dạng ngang (Sản phẩm 1) -->
        <div class="social-post-card featured-horizontal" onclick="openLightbox('assets/cuoi-ky/fb-post-1-matcha-que-hoa-cacao-bac-ha.webp', 'Facebook: Matcha Quế Hoa &amp; Cacao Bạc Hà', 'Bài đăng giới thiệu hương vị sản phẩm (gắn nhãn AI) — 57 tương tác')">
          <div class="social-post-media landscape" style="min-height:260px;background:#000;">
            <img src="assets/cuoi-ky/fb-post-1-matcha-que-hoa-cacao-bac-ha.webp" alt="Matcha Quế Hoa và Cacao Bạc Hà" class="social-post-img" style="object-fit:contain;width:100%;height:100%;" />
            <div class="proof-card-zoom-badge"><i data-lucide="zoom-in" style="width:11px;height:11px;"></i> Phóng to ảnh ngang</div>
          </div>
          <div class="social-card-body" style="display:flex;flex-direction:column;justify-content:center;">
            <div>
              <div style="display:inline-block;background:rgba(240,167,101,0.15);border:1px solid rgba(240,167,101,0.35);color:var(--accent-gold-light);font-size:11px;font-weight:800;padding:3px 10px;border-radius:999px;text-transform:uppercase;margin-bottom:8px;">★ Định dạng bài đăng ngang</div>
              <div class="social-card-title" style="font-size:18px;">Sản phẩm 1: Matcha Quế Hoa &amp; Cacao Bạc Hà</div>
              <div class="social-card-desc" style="font-size:14px;line-height:1.6;margin:8px 0 14px;">Bài đăng giới thiệu 2 thức uống bằng hình ảnh sản phẩm định dạng ngang và thông tin hương vị đặc trưng để giữ năng lượng cho ngày dài (có gắn nhãn AI minh bạch). Thu hút lượng tương tác cao nhất Fanpage.</div>
              <div class="social-stat-chips">
                <span class="stat-chip"><i data-lucide="thumbs-up" style="width:11px;height:11px;"></i> 35 thích</span>
                <span class="stat-chip"><i data-lucide="message-circle" style="width:11px;height:11px;"></i> 21 bình luận</span>
                <span class="stat-chip"><i data-lucide="share-2" style="width:11px;height:11px;"></i> 1 share</span>
                <span class="stat-chip highlight">Tổng: 57 tương tác</span>
              </div>
            </div>
          </div>
        </div>

        <!-- HÀNG 2: 2 Bài đăng định dạng dọc xếp thành lưới 2 cột cân xứng -->
        <div class="social-showcase-grid cols-2">
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
      </div>"""

    if sec5_old in content:
        content = content.replace(sec5_old, sec5_new)
        print("3. Section 5 updated (Horizontal post on its own row).")
    else:
        print("WARNING: Section 5 old snippet not found directly, checking...")

    # =========================================================================
    # 4. UPDATE SECTION 6 (CHO CHỮ XUỐNG HÀNG ĐỂ KÉO XUỐNG HIỆN HẾT)
    # =========================================================================
    sec6_table_old = """      <!-- Bảng So Sánh 4 Kênh -->
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
      </div>"""

    sec6_table_new = """      <!-- Bảng So Sánh 4 Kênh (Tự động xuống hàng, hiển thị trọn vẹn 100% khi kéo xuống) -->
      <div class="table-container" style="overflow-x:visible;">
        <table class="wrap-content-table">
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
              <td style="font-weight:700;color:var(--crema);"><i data-lucide="facebook" style="width:14px;height:14px;display:inline;vertical-align:middle;margin-right:4px;color:var(--accent-gold);"></i> Facebook Fanpage</td>
              <td>Duy trì hình ảnh thương hiệu, cổng thông tin chính thức &amp; kết nối cộng đồng sinh viên.</td>
              <td>Follower tăng từ <strong>50 lên 100</strong>; tổng tương tác vượt KPI đạt <strong>110,8% (665 tương tác)</strong>.</td>
              <td>Khả năng lan truyền tự nhiên thấp, lượt xem bài đăng có xu hướng giảm dần qua các tuần sau khi kết thúc đợt đẩy tin ban đầu.</td>
            </tr>
            <tr>
              <td style="font-weight:700;color:var(--crema);"><i data-lucide="instagram" style="width:14px;height:14px;display:inline;vertical-align:middle;margin-right:4px;color:#E1306C;"></i> Instagram</td>
              <td>Xây dựng thẩm mỹ thương hiệu cao cấp, thu hút giới trẻ thích check-in &amp; Reels không gian quán.</td>
              <td>Follower tăng từ <strong>58 lên 142</strong>; Tuần 4 bùng nổ đạt <strong>513 tương tác</strong> nhờ Reels viral chữ viết tay.</td>
              <td>Hiệu quả tương tác chưa thực sự đồng đều giữa các bài đăng tĩnh và video ngắn; chênh lệch lớn giữa các tuần.</td>
            </tr>
            <tr style="background:rgba(46,204,113,0.08);">
              <td style="font-weight:700;color:var(--matcha-green);"><i data-lucide="video" style="width:14px;height:14px;display:inline;vertical-align:middle;margin-right:4px;color:var(--matcha-green);"></i> TikTok 🏆 (Mũi nhọn)</td>
              <td>Mở rộng phễu tiếp cận, lan truyền nội dung viral và thu hút tệp khách hàng sinh viên mới.</td>
              <td style="color:var(--matcha-bright);font-weight:600;">Lượt xem bài đăng tăng từ <strong>1.800 lên 5.300/tuần</strong>; Tuần 4 thu về <strong>138 follower ròng</strong>; Tuần 6 đạt đỉnh <strong>219 shares</strong>.</td>
              <td>Tỷ lệ chuyển đổi người xem video thành follower theo dõi lâu dài chưa ổn định; cần duy trì liên tục tần suất đăng bài bắt trend.</td>
            </tr>
            <tr>
              <td style="font-weight:700;color:var(--crema);"><i data-lucide="globe" style="width:14px;height:14px;display:inline;vertical-align:middle;margin-right:4px;color:var(--accent-gold);"></i> Landing Page</td>
              <td>Điểm đến tập trung thông tin, menu điện tử, định vị bản đồ và đo lường chuyển đổi cuối cùng.</td>
              <td>Tuần 4 đạt đỉnh <strong>280 lượt truy cập</strong> (ngay sau khi chủ động gắn link điều hướng dưới bài đăng FB).</td>
              <td>Lượng truy cập phụ thuộc trực tiếp vào tần suất gắn link trên mạng xã hội; giảm mạnh ở tuần 5-6 khi giảm tần suất kêu gọi hành động.</td>
            </tr>
          </tbody>
        </table>
      </div>"""

    if sec6_table_old in content:
        content = content.replace(sec6_table_old, sec6_table_new)
        print("4. Section 6 table updated (Text wraps down cleanly, no cutting off).")
    else:
        print("WARNING: Section 6 table snippet not found directly, checking...")

    # =========================================================================
    # 5. UPDATE SECTION 8 (THIẾT KẾ LẠI ĐẸP MẮT CHO KẾ HOẠCH 3 THÁNG)
    # =========================================================================
    sec8_old = """      <div class="report-two-cols">
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
      </div>"""

    sec8_new = """      <!-- 1. DẢI THẺ CHIẾN LƯỢC ĐỊNH HƯỚNG 4 KÊNH (LUXURY CARDS GRID) -->
      <h3 style="font-family:var(--font-serif);font-size:22px;color:var(--accent-gold);margin:10px 0 16px;display:flex;align-items:center;gap:10px;">
        <i data-lucide="target" style="width:20px;height:20px;"></i> Định Hướng Vận Hành Chiến Lược 4 Kênh
      </h3>
      <div class="sec8-strategy-grid">
        <!-- Card 1: TikTok -->
        <div class="sec8-channel-card matcha-accent">
          <div class="sec8-card-header">
            <div class="sec8-card-brand">
              <div class="sec8-card-icon matcha"><i data-lucide="video" style="width:20px;height:20px;"></i></div>
              <div class="sec8-card-name">TikTok Channel</div>
            </div>
            <span class="sec8-card-badge matcha">Mũi nhọn số 1</span>
          </div>
          <div class="sec8-kpi-pill">
            <i data-lucide="zap" style="width:14px;height:14px;color:var(--matcha-green);"></i>
            <span>Tần suất: <strong>5 video/tuần</strong> &bull; Mục tiêu: <strong>500 followers</strong></span>
          </div>
          <div class="sec8-card-desc">
            Tiếp tục ưu tiên số 1 nhờ hiệu quả tạo view và tương tác vượt trội. Tập trung sản xuất video tình huống vui nhộn, bắt trend sinh viên, lồng ghép sản phẩm tự nhiên và <strong>tối ưu hóa Hook 3 giây đầu</strong> để giữ chân người xem.
          </div>
        </div>

        <!-- Card 2: Facebook Fanpage -->
        <div class="sec8-channel-card">
          <div class="sec8-card-header">
            <div class="sec8-card-brand">
              <div class="sec8-card-icon gold"><i data-lucide="facebook" style="width:20px;height:20px;"></i></div>
              <div class="sec8-card-name">Facebook Fanpage</div>
            </div>
            <span class="sec8-card-badge gold">Cổng thông tin</span>
          </div>
          <div class="sec8-kpi-pill">
            <i data-lucide="zap" style="width:14px;height:14px;color:var(--accent-gold);"></i>
            <span>Tần suất: <strong>5 bài đăng/tuần</strong> &bull; Mục tiêu: <strong>150 followers</strong></span>
          </div>
          <div class="sec8-card-desc">
            Kênh thông tin chính thống cập nhật liên tục món mới, chương trình ưu đãi, hình ảnh không gian quán mát lạnh và <strong>duy trì gắn link Landing Page</strong> dưới bình luận để điều hướng người dùng xem chi tiết.
          </div>
        </div>

        <!-- Card 3: Instagram -->
        <div class="sec8-channel-card">
          <div class="sec8-card-header">
            <div class="sec8-card-brand">
              <div class="sec8-card-icon ig"><i data-lucide="instagram" style="width:20px;height:20px;"></i></div>
              <div class="sec8-card-name">Instagram Profile</div>
            </div>
            <span class="sec8-card-badge gold">Visual Thẩm Mỹ</span>
          </div>
          <div class="sec8-kpi-pill">
            <i data-lucide="zap" style="width:14px;height:14px;color:#E1306C;"></i>
            <span>Tần suất: <strong>5 bài + 5-6 stories/tuần</strong> &bull; Mục tiêu: <strong>200 followers</strong></span>
          </div>
          <div class="sec8-card-desc">
            Nâng cao tính thẩm mỹ hình ảnh đồ uống nghệ thuật, duy trì định dạng Stories tương tác hàng ngày và Reels ngắn chạm cảm xúc, thu hút tệp bạn trẻ thích không gian check-in fine dining.
          </div>
        </div>

        <!-- Card 4: Landing Page -->
        <div class="sec8-channel-card matcha-accent">
          <div class="sec8-card-header">
            <div class="sec8-card-brand">
              <div class="sec8-card-icon matcha"><i data-lucide="globe" style="width:20px;height:20px;"></i></div>
              <div class="sec8-card-name">Landing Page Olion</div>
            </div>
            <span class="sec8-card-badge matcha">Phễu chuyển đổi</span>
          </div>
          <div class="sec8-kpi-pill">
            <i data-lucide="zap" style="width:14px;height:14px;color:var(--matcha-green);"></i>
            <span>Tần suất: <strong>Cập nhật realtime</strong> &bull; Mục tiêu: <strong>500 visits</strong></span>
          </div>
          <div class="sec8-card-desc">
            Điểm đến trung tâm cập nhật menu điện tử, thông tin đặt bàn học nhóm, định vị bản đồ cơ sở Gò Vấp và các chương trình khuyến mãi theo mùa; gắn liền với hệ thống đo lường chuyển đổi.
          </div>
        </div>
      </div>

      <!-- 2. THƯỚC ĐO CHỈ TIÊU KPI 3 THÁNG TỚI (METRIC TARGET BOXES) -->
      <h3 style="font-family:var(--font-serif);font-size:22px;color:var(--accent-gold);margin:20px 0 16px;display:flex;align-items:center;gap:10px;">
        <i data-lucide="award" style="width:20px;height:20px;"></i> Chỉ Tiêu Định Lượng &amp; Tiêu Chuẩn Thực Tế 3 Tháng
      </h3>
      <div class="sec8-targets-grid">
        <div class="sec8-target-item matcha">
          <div class="sec8-target-num text-matcha">500</div>
          <div class="sec8-target-lbl">Followers TikTok</div>
          <div class="sec8-target-cadence">Duy trì 5 video/tuần</div>
        </div>
        <div class="sec8-target-item">
          <div class="sec8-target-num text-gold">150</div>
          <div class="sec8-target-lbl">Followers Facebook</div>
          <div class="sec8-target-cadence">Duy trì 5 bài đăng/tuần</div>
        </div>
        <div class="sec8-target-item">
          <div class="sec8-target-num text-gold">200</div>
          <div class="sec8-target-lbl">Followers Instagram</div>
          <div class="sec8-target-cadence">5 bài + 5-6 stories/tuần</div>
        </div>
        <div class="sec8-target-item matcha">
          <div class="sec8-target-num text-matcha">500+</div>
          <div class="sec8-target-lbl">Visits Landing Page</div>
          <div class="sec8-target-cadence">Lượng truy cập 3 tháng</div>
        </div>
      </div>

      <!-- Tiêu chuẩn đánh giá thực tế -->
      <div style="background:rgba(20,15,10,0.85);border:1px solid rgba(240,167,101,0.3);border-radius:var(--radius-sm);padding:14px 20px;margin-bottom:28px;display:flex;align-items:center;gap:12px;">
        <i data-lucide="check-circle" style="width:20px;height:20px;color:var(--matcha-green);flex-shrink:0;"></i>
        <div style="font-size:13.5px;color:var(--crema);line-height:1.5;">
          <strong>Tiêu chuẩn đánh giá thực tế:</strong> Không chỉ dừng lại ở việc đếm lượt thích (like), nhóm tập trung đo lường số tin nhắn hỏi thông tin đồ uống, tỷ lệ người dùng tương tác và lượng khách sinh viên thực tế đến trải nghiệm quán tại Cơ sở 3 Gò Vấp.
        </div>
      </div>

      <!-- 3. BANNER KHỞI NGHIỆP THỰC TẾ (STARTUP VISION CALLOUT) -->
      <div class="pos-stmt-banner" style="margin-top:20px;">
        <div class="pos-stmt-badge">
          <i data-lucide="compass" style="width:14px;height:14px;"></i>
          <span>Định Hướng Khởi Nghiệp Thực Tế (Startup Vision)</span>
        </div>
        <div class="pos-stmt-content" style="font-size:15px;line-height:1.75;">
          Nhóm nhận thấy dự án <strong>Olion Coffee</strong> không chỉ dừng lại ở phạm vi một bài tập học phần mà còn có tiềm năng tiếp tục phát triển thành hoạt động truyền thông thương mại thực tế. Trong thời gian tới, nhóm định hướng tiếp tục phát huy thế mạnh của TikTok trong việc tạo độ nhận diện và thu hút khách hàng mới, kết hợp Facebook và Instagram để duy trì hình ảnh thương hiệu, đồng thời sử dụng Landing Page làm điểm đến tập trung thông tin. Đây sẽ là nền tảng để nhóm từng bước hoàn thiện hoạt động truyền thông, xây dựng tệp khách hàng tiềm năng và tạo tiền đề vững chắc cho sự phát triển dài hạn của dự án.
        </div>
      </div>"""

    if sec8_old in content:
        content = content.replace(sec8_old, sec8_new)
        print("5. Section 8 updated (Modern card-based layout, KPI boxes, luxury banner).")
    else:
        print("WARNING: Section 8 old snippet not found directly, checking...")

    # =========================================================================
    # 6. UPDATE SECTION 9: BẢNG GIA PHẢ NHÓM 7 (ORG HIERARCHY TREE)
    # =========================================================================
    sec9_pattern = re.compile(r'<div class="team-showcase-container">.*?</section>', re.DOTALL)
    
    sec9_tree_html = """<div class="team-showcase-container">
        <div class="org-tree-container">

          <!-- 1. ĐỈNH CÂY GIA PHẢ: TRƯỞNG NHÓM (QUANG HÙNG) -->
          <div class="org-tree-root">
            <div class="org-leader-card" onclick="openLightbox('assets/cuoi-ky/member-quang-hung-truong-nhom.webp', 'Quang Hưng — Trưởng Nhóm 7 (Gỗ Xà Cừ)', 'Điều phối hoạt động chung, xây dựng kế hoạch, phân công nhiệm vụ, theo dõi tiến độ và tổng hợp kết quả')">
              <div class="org-avatar-box">
                <img src="assets/cuoi-ky/member-quang-hung-truong-nhom.webp" alt="Quang Hưng - Trưởng Nhóm" class="org-avatar-img" />
                <div class="org-crown-badge" title="Trưởng Nhóm 7">👑</div>
              </div>
              <div class="org-leader-info">
                <div class="org-leader-name">Quang Hưng</div>
                <div class="org-leader-role">Trưởng Nhóm &bull; Quản Trị &amp; Điều Phối Chung</div>
                <div class="org-leader-desc">
                  Chịu trách nhiệm điều phối hoạt động chung, phân công nhiệm vụ 4 ban, theo dõi sát tiến độ 6 tuần và tổng hợp báo cáo.
                </div>
              </div>
            </div>

            <!-- Thân dây nối cây gia phả -->
            <div class="org-tree-stem"></div>
            <div class="org-tree-branches-bar"></div>
          </div>

          <!-- 2. BỐN NHÁNH BAN CHUYÊN MÔN CỦA GIA ĐÌNH GỖ XÀ CỪ -->
          <div class="org-branches-grid">

            <!-- NHÁNH 1: BAN NỘI DUNG (2 THÀNH VIÊN) -->
            <div class="org-branch-column matcha-theme">
              <div class="org-branch-header matcha-theme">
                <div class="org-branch-icon"><i data-lucide="pen-tool" style="width:16px;height:16px;"></i></div>
                <div class="org-branch-title">Ban Nội Dung (2)</div>
              </div>
              <div class="org-members-list">
                <!-- Uyên Thuỳ -->
                <div class="org-member-mini-card" onclick="openLightbox('assets/cuoi-ky/member-uyen-thuy-noi-dung.webp', 'Uyên Thuỳ — Ban Nội Dung', 'Nghiên cứu ý tưởng, xây dựng kịch bản, viết nội dung bài đăng và đề xuất xu hướng')">
                  <div class="org-mini-avatar-box">
                    <img src="assets/cuoi-ky/member-uyen-thuy-noi-dung.webp" alt="Uyên Thuỳ" class="org-mini-avatar" />
                  </div>
                  <div class="org-mini-info">
                    <div class="org-mini-name">Uyên Thuỳ</div>
                    <div class="org-mini-role">Content Creator</div>
                    <div class="org-mini-desc">Nghiên cứu insight sinh viên VLU, sáng tạo ý tưởng và kịch bản viral.</div>
                  </div>
                </div>

                <!-- Thuý Hiền -->
                <div class="org-member-mini-card" onclick="openLightbox('assets/cuoi-ky/member-thuy-hien-noi-dung.webp', 'Thuý Hiền — Ban Nội Dung', 'Nghiên cứu ý tưởng, biên soạn nội dung bài đăng và kiểm duyệt thông điệp thương hiệu')">
                  <div class="org-mini-avatar-box">
                    <img src="assets/cuoi-ky/member-thuy-hien-noi-dung.webp" alt="Thuý Hiền" class="org-mini-avatar" />
                  </div>
                  <div class="org-mini-info">
                    <div class="org-mini-name">Thuý Hiền</div>
                    <div class="org-mini-role">Content Writer</div>
                    <div class="org-mini-desc">Chắp bút nội dung Facebook/Instagram, trau chuốt caption thương hiệu.</div>
                  </div>
                </div>
              </div>
            </div>

            <!-- NHÁNH 2: BAN THIẾT KẾ (3 THÀNH VIÊN) -->
            <div class="org-branch-column">
              <div class="org-branch-header">
                <div class="org-branch-icon"><i data-lucide="palette" style="width:16px;height:16px;"></i></div>
                <div class="org-branch-title">Ban Thiết Kế (3)</div>
              </div>
              <div class="org-members-list">
                <!-- Thiên Ý -->
                <div class="org-member-mini-card" onclick="openLightbox('assets/cuoi-ky/member-thien-y-thiet-ke.webp', 'Thiên Ý — Ban Thiết Kế', 'Thiết kế đồ họa, căn chỉnh màu sắc và đảm bảo tính nhất quán nhận diện Olion')">
                  <div class="org-mini-avatar-box">
                    <img src="assets/cuoi-ky/member-thien-y-thiet-ke.webp" alt="Thiên Ý" class="org-mini-avatar" />
                  </div>
                  <div class="org-mini-info">
                    <div class="org-mini-name">Thiên Ý</div>
                    <div class="org-mini-role">Graphic Designer</div>
                    <div class="org-mini-desc">Thiết kế banner, poster đồ uống chuẩn nhận diện Olion Coffee.</div>
                  </div>
                </div>

                <!-- Gia Quyền -->
                <div class="org-member-mini-card" onclick="openLightbox('assets/cuoi-ky/member-gia-quyen-thiet-ke.webp', 'Gia Quyền — Ban Thiết Kế', 'Hậu kỳ video, tối ưu hiệu ứng đồ họa và âm thanh cho các nền tảng mạng xã hội')">
                  <div class="org-mini-avatar-box">
                    <img src="assets/cuoi-ky/member-gia-quyen-thiet-ke.webp" alt="Gia Quyền" class="org-mini-avatar" />
                  </div>
                  <div class="org-mini-info">
                    <div class="org-mini-name">Gia Quyền</div>
                    <div class="org-mini-role">Video Editor</div>
                    <div class="org-mini-desc">Hậu kỳ video TikTok, hiệu ứng chuyển cảnh và âm thanh bắt trend.</div>
                  </div>
                </div>

                <!-- Duy Khánh -->
                <div class="org-member-mini-card" onclick="openLightbox('assets/cuoi-ky/member-duy-khanh-thiet-ke.webp', 'Duy Khánh — Ban Thiết Kế', 'Chụp ảnh sản phẩm, quay dựng video TikTok, chỉnh sửa visual trực quan')">
                  <div class="org-mini-avatar-box">
                    <img src="assets/cuoi-ky/member-duy-khanh-thiet-ke.webp" alt="Duy Khánh" class="org-mini-avatar" />
                  </div>
                  <div class="org-mini-info">
                    <div class="org-mini-name">Duy Khánh</div>
                    <div class="org-mini-role">Media &amp; Visual</div>
                    <div class="org-mini-desc">Quay chụp đồ uống tại quán, dựng clip ngắn sinh động bắt mắt.</div>
                  </div>
                </div>
              </div>
            </div>

            <!-- NHÁNH 3: BAN VẬN HÀNH (2 THÀNH VIÊN) -->
            <div class="org-branch-column matcha-theme">
              <div class="org-branch-header matcha-theme">
                <div class="org-branch-icon"><i data-lucide="sliders" style="width:16px;height:16px;"></i></div>
                <div class="org-branch-title">Ban Vận Hành (2)</div>
              </div>
              <div class="org-members-list">
                <!-- Thành Duy -->
                <div class="org-member-mini-card" onclick="openLightbox('assets/cuoi-ky/member-thanh-duy-van-hanh.webp', 'Thành Duy — Ban Vận Hành', 'Quản lý lịch đăng bài, tối ưu hóa phân phối và điều hướng traffic về Landing Page')">
                  <div class="org-mini-avatar-box">
                    <img src="assets/cuoi-ky/member-thanh-duy-van-hanh.webp" alt="Thành Duy" class="org-mini-avatar" />
                  </div>
                  <div class="org-mini-info">
                    <div class="org-mini-name">Thành Duy</div>
                    <div class="org-mini-role">Channel Operations</div>
                    <div class="org-mini-desc">Quản lý lịch đăng FB/IG/TikTok, gắn link điều hướng Landing Page.</div>
                  </div>
                </div>

                <!-- Như Ý -->
                <div class="org-member-mini-card" onclick="openLightbox('assets/cuoi-ky/member-nhu-y-van-hanh.webp', 'Như Ý — Ban Vận Hành', 'Điều phối thời gian đăng bài, chăm sóc tương tác bình luận và phản hồi khách hàng')">
                  <div class="org-mini-avatar-box">
                    <img src="assets/cuoi-ky/member-nhu-y-van-hanh.webp" alt="Như Ý" class="org-mini-avatar" />
                  </div>
                  <div class="org-mini-info">
                    <div class="org-mini-name">Như Ý</div>
                    <div class="org-mini-role">Community Mod</div>
                    <div class="org-mini-desc">Chăm sóc bình luận, phản hồi tin nhắn tư vấn ấm áp, thân thiện.</div>
                  </div>
                </div>
              </div>
            </div>

            <!-- NHÁNH 4: BAN ĐO LƯỜNG & BÁO CÁO (3 THÀNH VIÊN) -->
            <div class="org-branch-column">
              <div class="org-branch-header">
                <div class="org-branch-icon"><i data-lucide="bar-chart-2" style="width:16px;height:16px;"></i></div>
                <div class="org-branch-title">Ban Đo Lường (3)</div>
              </div>
              <div class="org-members-list">
                <!-- Anh Thư -->
                <div class="org-member-mini-card" onclick="openLightbox('assets/cuoi-ky/member-anh-thu-do-luong.webp', 'Anh Thư — Ban Đo Lường', 'Thu thập chỉ số reach, tương tác, follower và traffic Landing Page hàng ngày')">
                  <div class="org-mini-avatar-box">
                    <img src="assets/cuoi-ky/member-anh-thu-do-luong.webp" alt="Anh Thư" class="org-mini-avatar" />
                  </div>
                  <div class="org-mini-info">
                    <div class="org-mini-name">Anh Thư</div>
                    <div class="org-mini-role">Data Analyst</div>
                    <div class="org-mini-desc">Theo dõi reach, tương tác, follower và traffic web hàng ngày.</div>
                  </div>
                </div>

                <!-- Phương Linh -->
                <div class="org-member-mini-card" onclick="openLightbox('assets/cuoi-ky/member-phuong-linh-do-luong.webp', 'Phương Linh — Ban Đo Lường', 'Tổng hợp số liệu báo cáo 6 tuần, trực quan hóa biểu đồ và so sánh chỉ tiêu KPI')">
                  <div class="org-mini-avatar-box">
                    <img src="assets/cuoi-ky/member-phuong-linh-do-luong.webp" alt="Phương Linh" class="org-mini-avatar" />
                  </div>
                  <div class="org-mini-info">
                    <div class="org-mini-name">Phương Linh</div>
                    <div class="org-mini-role">Reporting Lead</div>
                    <div class="org-mini-desc">Tổng hợp bảng số liệu 6 tuần, vẽ biểu đồ và đối soát KPI dự án.</div>
                  </div>
                </div>

                <!-- Thanh Ngân -->
                <div class="org-member-mini-card" onclick="openLightbox('assets/cuoi-ky/member-thanh-ngan-do-luong.webp', 'Thanh Ngân — Ban Đo Lường', 'Phân tích nguyên nhân tăng giảm, đối chiếu hành vi người dùng và đề xuất cải tiến')">
                  <div class="org-mini-avatar-box">
                    <img src="assets/cuoi-ky/member-thanh-ngan-do-luong.webp" alt="Thanh Ngân" class="org-mini-avatar" />
                  </div>
                  <div class="org-mini-info">
                    <div class="org-mini-name">Thanh Ngân</div>
                    <div class="org-mini-role">Insight &amp; Audit</div>
                    <div class="org-mini-desc">Phân tích nguyên nhân tăng giảm số liệu, đối chiếu hành vi các kênh.</div>
                  </div>
                </div>
              </div>
            </div>

          </div>
        </div>

        <!-- Banner kết tinh thần đồng đội -->
        <div style="background:rgba(20,15,10,0.85);border:1px solid rgba(240,167,101,0.3);border-radius:var(--radius-md);padding:18px 24px;margin-top:28px;text-align:center;box-shadow:var(--shadow-wood);">
          <div style="font-family:var(--font-serif);font-size:18px;color:var(--accent-gold);margin-bottom:6px;">
            🤝 Tinh Thần Đồng Đội &amp; Hợp Tác Nhóm 7 (Gỗ Xà Cừ)
          </div>
          <p style="font-size:13.5px;color:var(--crema);margin:0;line-height:1.6;max-width:860px;display:inline-block;">
            11 thành viên đã cùng nhau làm việc gắn kết như một gia đình, chủ động hỗ trợ lẫn nhau giữa các ban từ khâu ý tưởng, quay chụp, sản xuất video, đăng bài đến phân tích số liệu để hoàn thành xuất sắc chiến dịch truyền thông Olion Coffee.
          </p>
        </div>
      </div>
    </div>
  </section>"""

    match_sec9 = sec9_pattern.search(content)
    if match_sec9:
        content = content[:match_sec9.start()] + sec9_tree_html + content[match_sec9.end():]
        print("6. Section 9 updated (Family Tree / Org Hierarchy with small avatars).")
    else:
        print("WARNING: Section 9 regex pattern not found directly, checking fallback...")

    with open('scripts/build_cuoi_ky_final.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print("All patches saved to scripts/build_cuoi_ky_final.py successfully!")

if __name__ == '__main__':
    apply_5_requests()
