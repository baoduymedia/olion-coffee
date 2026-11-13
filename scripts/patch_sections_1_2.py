import os

def patch_builder():
    with open('scripts/build_cuoi_ky_final.py', 'r', encoding='utf-8') as f:
        text = f.read()

    # 1. New CSS additions
    new_css_additions = '''
    /* ========================================================
       SECTION 1: OVERVIEW & POSITIONING MATRIX (ENHANCED)
       ======================================================== */
    .overview-cards-row.cols-4 {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
      margin: 24px 0 32px;
    }
    @media (max-width: 1024px) {
      .overview-cards-row.cols-4 {
        grid-template-columns: repeat(2, 1fr);
      }
    }
    @media (max-width: 640px) {
      .overview-cards-row.cols-4 {
        grid-template-columns: 1fr;
      }
    }
    .overview-card-item {
      background: linear-gradient(145deg, rgba(28, 20, 15, 0.92) 0%, rgba(18, 13, 9, 0.98) 100%);
      border: 1.5px solid rgba(240, 167, 101, 0.28);
      border-radius: var(--radius-md);
      padding: 20px 22px;
      position: relative;
      overflow: hidden;
      transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
      box-shadow: 0 8px 24px rgba(0,0,0,0.55);
      display: flex;
      flex-direction: column;
    }
    .overview-card-item:hover {
      transform: translateY(-5px);
      border-color: var(--accent-gold);
      box-shadow: 0 14px 32px rgba(240, 167, 101, 0.25);
    }
    .overview-card-item::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 3px;
      background: linear-gradient(90deg, transparent, var(--accent-gold), transparent);
      opacity: 0.8;
    }
    .overview-card-label {
      font-size: 12px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.12em;
      color: var(--accent-gold);
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 8px;
    }
    .overview-card-value {
      font-size: 16.5px;
      font-weight: 700;
      color: var(--crema);
      line-height: 1.35;
      margin-bottom: 6px;
    }
    .overview-card-sub {
      font-size: 12.5px;
      color: var(--text-muted);
      line-height: 1.45;
    }

    /* Positioning Matrix 4 Blocks */
    .positioning-matrix-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 20px;
      margin: 28px 0;
    }
    @media (max-width: 768px) {
      .positioning-matrix-grid {
        grid-template-columns: 1fr;
        gap: 16px;
      }
    }
    .pos-matrix-card {
      background: linear-gradient(145deg, rgba(22, 17, 12, 0.95) 0%, rgba(14, 10, 7, 0.98) 100%);
      border: 1.5px solid rgba(240, 167, 101, 0.22);
      border-radius: var(--radius-md);
      padding: 22px 24px;
      box-shadow: var(--shadow-wood);
      transition: all 0.3s ease;
      display: flex;
      flex-direction: column;
    }
    .pos-matrix-card:hover {
      transform: translateY(-3px);
      border-color: var(--accent-gold);
      box-shadow: 0 12px 30px rgba(0,0,0,0.7), 0 0 15px rgba(240, 167, 101, 0.15);
    }
    .pos-matrix-card.matcha-accent {
      border-color: rgba(46, 204, 113, 0.3);
    }
    .pos-matrix-card.matcha-accent:hover {
      border-color: var(--matcha-green);
      box-shadow: 0 12px 30px rgba(0,0,0,0.7), 0 0 15px rgba(46, 204, 113, 0.2);
    }
    .pos-matrix-header {
      display: flex;
      align-items: center;
      gap: 14px;
      margin-bottom: 16px;
      padding-bottom: 12px;
      border-bottom: 1px dashed rgba(255,255,255,0.1);
    }
    .pos-matrix-icon-box {
      width: 42px;
      height: 42px;
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }
    .pos-matrix-icon-box.gold {
      background: rgba(240, 167, 101, 0.15);
      border: 1px solid rgba(240, 167, 101, 0.4);
      color: var(--accent-gold);
    }
    .pos-matrix-icon-box.red {
      background: rgba(239, 68, 68, 0.15);
      border: 1px solid rgba(239, 68, 68, 0.4);
      color: #f87171;
    }
    .pos-matrix-icon-box.matcha {
      background: rgba(46, 204, 113, 0.15);
      border: 1px solid rgba(46, 204, 113, 0.4);
      color: var(--matcha-bright);
    }
    .pos-matrix-icon-box.emerald {
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid rgba(16, 185, 129, 0.4);
      color: #34d399;
    }
    .pos-matrix-badge {
      font-size: 11px;
      font-weight: 800;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      margin-bottom: 3px;
    }
    .pos-matrix-title {
      font-size: 17px;
      font-weight: 700;
      color: var(--crema);
      margin: 0;
      line-height: 1.3;
    }
    .pos-matrix-list {
      list-style: none;
      padding: 0;
      margin: 0;
      font-size: 13.5px;
      line-height: 1.6;
      color: var(--text-muted);
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .pos-matrix-list li {
      position: relative;
      padding-left: 20px;
    }
    .pos-matrix-list li strong {
      color: var(--crema);
    }
    .pos-matrix-list li::before {
      content: '✓';
      position: absolute;
      left: 0;
      top: 0;
      color: var(--accent-gold);
      font-weight: bold;
    }
    .pos-matrix-card.matcha-accent .pos-matrix-list li::before {
      color: var(--matcha-green);
    }

    /* Positioning Statement Callout Box */
    .pos-stmt-banner {
      background: radial-gradient(circle at 10% 20%, rgba(46, 204, 113, 0.08) 0%, transparent 45%),
                  radial-gradient(circle at 90% 80%, rgba(240, 167, 101, 0.09) 0%, transparent 50%),
                  linear-gradient(145deg, #1A130E 0%, #0E0A07 100%);
      border: 1.5px solid var(--border-brass);
      border-radius: var(--radius-md);
      padding: 26px 30px;
      margin: 28px 0;
      box-shadow: 0 12px 36px rgba(0,0,0,0.7);
      position: relative;
    }
    .pos-stmt-badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-size: 12px;
      font-weight: 800;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: var(--matcha-bright);
      background: rgba(46, 204, 113, 0.12);
      border: 1px solid rgba(46, 204, 113, 0.35);
      padding: 5px 12px;
      border-radius: var(--radius-full);
      margin-bottom: 14px;
    }
    .pos-stmt-lead {
      font-size: 15px;
      line-height: 1.7;
      color: var(--crema);
      margin-bottom: 18px;
    }
    .pos-stmt-tagline {
      border-top: 1px solid rgba(240, 167, 101, 0.2);
      padding-top: 14px;
      display: flex;
      flex-direction: column;
      gap: 4px;
    }
    .tagline-quote {
      font-family: var(--font-serif);
      font-size: 20px;
      font-weight: 700;
      font-style: italic;
      color: var(--accent-gold-light);
    }
    .tagline-sub {
      font-size: 13px;
      color: var(--text-muted);
    }

    /* PERSONA DOSSIER STYLING OVERRIDES & ENHANCEMENTS */
    .persona-container {
      background: radial-gradient(circle at 20% 20%, rgba(46, 204, 113, 0.05) 0%, transparent 40%),
                  radial-gradient(circle at 80% 80%, rgba(240, 167, 101, 0.08) 0%, transparent 45%),
                  linear-gradient(145deg, #1C140F 0%, #0F0A07 100%);
      border: 2px solid var(--border-brass);
      border-radius: var(--radius-lg);
      padding: 32px;
      margin-top: 25px;
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.8), inset 0 1px 0 rgba(255, 255, 255, 0.08);
      position: relative;
      overflow: hidden;
    }
    @media (max-width: 768px) {
      .persona-container {
        padding: 20px 16px;
      }
    }
    .persona-photo-wrapper {
      position: relative;
      width: 100%;
      aspect-ratio: 4 / 5;
      max-height: 480px;
      overflow: hidden;
      background: #000;
    }
    .persona-photo-img, .persona-main-img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center 30%;
      display: block;
      transition: transform 0.7s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .persona-photo-col:hover .persona-photo-img,
    .persona-photo-col:hover .persona-main-img {
      transform: scale(1.05);
    }
    .persona-traits-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 14px;
    }
    @media (max-width: 768px) {
      .persona-traits-grid {
        grid-template-columns: 1fr;
      }
    }
    .persona-trait-card {
      background: rgba(22, 16, 12, 0.9);
      border: 1.2px solid rgba(240, 167, 101, 0.2);
      border-radius: var(--radius-sm);
      padding: 14px 16px;
      display: flex;
      align-items: flex-start;
      gap: 12px;
      transition: all 0.25s ease;
    }
    .persona-trait-card:hover {
      border-color: var(--accent-gold);
      transform: translateY(-2px);
      box-shadow: 0 6px 16px rgba(0,0,0,0.5);
    }
    .persona-trait-card.full-width {
      grid-column: 1 / -1;
    }
    .trait-icon-box {
      width: 38px;
      height: 38px;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }
    .trait-icon-box.green {
      background: rgba(34, 197, 94, 0.15);
      border: 1px solid rgba(34, 197, 94, 0.4);
      color: #4ade80;
    }
    .trait-icon-box.gold {
      background: rgba(240, 167, 101, 0.15);
      border: 1px solid rgba(240, 167, 101, 0.4);
      color: var(--accent-gold);
    }
    .trait-icon-box.red {
      background: rgba(239, 68, 68, 0.15);
      border: 1px solid rgba(239, 68, 68, 0.4);
      color: #f87171;
    }
    .trait-icon-box.orange {
      background: rgba(251, 146, 60, 0.15);
      border: 1px solid rgba(251, 146, 60, 0.4);
      color: #fb923c;
    }
    .trait-icon-box.emerald {
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid rgba(16, 185, 129, 0.4);
      color: #34d399;
    }
    .trait-content {
      flex: 1;
    }
    .trait-header-title {
      font-size: 11.5px;
      font-weight: 800;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      margin-bottom: 4px;
    }
    .trait-body-text {
      font-size: 13px;
      color: var(--warm-gray);
      line-height: 1.45;
    }
'''

    pos_extra_start = text.find('extra_css = """')
    pos_extra_end = text.find('"""', pos_extra_start + 15)
    extra_css_content = text[pos_extra_start + 15 : pos_extra_end]

    if '.overview-cards-row.cols-4' not in extra_css_content:
        new_extra_css = extra_css_content + '\n' + new_css_additions
        text = text[:pos_extra_start + 15] + new_extra_css + text[pos_extra_end:]

    # 2. Section 1 and Section 2 HTML
    new_sec_1_and_2 = '''  <!-- ========================================================
       MỤC 1: TỔNG QUAN DỰ ÁN & ĐỊNH VỊ THƯƠNG HIỆU
       ======================================================== -->
  <section class="report-section" id="muc-1">
    <div class="shell">
      <div class="section-chapter-tag">1. TỔNG QUAN DỰ ÁN &amp; ĐỊNH VỊ THƯƠNG HIỆU</div>
      <h2 class="section-main-heading">1. Tổng Quan Dự Án &amp; Định Vị Thương Hiệu</h2>
      <p style="color:var(--text-muted);margin-bottom:28px;font-size:15px;line-height:1.6;">
        Nghiên cứu thị trường và chiến lược định vị thương hiệu <strong style="color:var(--crema);">Olion Coffee</strong> — điểm đến cà phê máy lạnh lý tưởng dành riêng cho sinh viên Đại học Văn Lang (Cơ sở 3 Gò Vấp) học tập, giải tỏa áp lực và nạp lại năng lượng.
      </p>

      <!-- 4 Trụ Cột Cơ Bản (Visual Glassmorphism Pillar Cards) -->
      <div class="overview-cards-row cols-4">
        <div class="overview-card-item">
          <div class="overview-card-label">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="var(--accent-gold)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 8h1a4 4 0 1 1 0 8h-1"/><path d="M3 8h14v9a4 4 0 0 1-4 4H7a4 4 0 0 1-4-4Z"/><line x1="6" y1="2" x2="6" y2="4"/><line x1="10" y1="2" x2="10" y2="4"/><line x1="14" y1="2" x2="14" y2="4"/></svg>
            <span>Sản Phẩm</span>
          </div>
          <div class="overview-card-value">Cà Phê &bull; Trà &bull; Sữa Chua &bull; Matcha</div>
          <div class="overview-card-sub">Menu tinh tuyển: Cà phê pha máy, Trà trái cây tươi, Yogurt mát lạnh, Matcha Series &amp; Cacao đậm vị.</div>
        </div>

        <div class="overview-card-item">
          <div class="overview-card-label">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="var(--matcha-green)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
            <span>Dịch Vụ</span>
          </div>
          <div class="overview-card-value">Máy Lạnh &bull; Wifi Mạnh &bull; Ổ Cắm Điện</div>
          <div class="overview-card-sub">Không gian mát mẻ, yên tĩnh tối ưu cho học nhóm, cắm máy chạy deadline cả ngày dài.</div>
        </div>

        <div class="overview-card-item">
          <div class="overview-card-label">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="var(--accent-gold-light)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/></svg>
            <span>Mô Hình</span>
          </div>
          <div class="overview-card-value">Thoải Mái &bull; Ngon &bull; Giá Sinh Viên</div>
          <div class="overview-card-sub">Mức giá sinh viên dễ chịu chỉ từ 35.000đ - 45.000đ, phong cách phục vụ chu đáo, gần gũi như bạn bè.</div>
        </div>

        <div class="overview-card-item">
          <div class="overview-card-label">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="var(--matcha-bright)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>
            <span>Vị Trí Đắc Địa</span>
          </div>
          <div class="overview-card-value">80/64a Dương Quảng Hàm</div>
          <div class="overview-card-sub">Nằm ngay sát cổng ĐH Văn Lang CS3 (An Nhơn, Gò Vấp), chỉ mất 1-2 phút đi bộ từ giảng đường.</div>
        </div>
      </div>

      <!-- Khung Định Vị Chiến Lược 4 Khối (Positioning Matrix Grid) -->
      <h3 style="font-family:var(--font-serif);font-size:24px;color:#fff;margin:32px 0 16px;display:flex;align-items:center;gap:10px;">
        <span style="color:var(--accent-gold);">❖</span> Ma Trận Định Vị &amp; Giá Trị Cốt Lõi Cho Sinh Viên VLU
      </h3>

      <div class="positioning-matrix-grid">
        <!-- Khối 1: Sinh viên mục tiêu -->
        <div class="pos-matrix-card">
          <div class="pos-matrix-header">
            <div class="pos-matrix-icon-box gold">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
            </div>
            <div>
              <div class="pos-matrix-badge" style="color:var(--accent-gold);">ĐỐI TƯỢNG TRỌNG TÂM</div>
              <h4 class="pos-matrix-title">Sinh Viên Mục Tiêu (Target Audience)</h4>
            </div>
          </div>
          <ul class="pos-matrix-list">
            <li><strong>Chân dung trọng tâm:</strong> Sinh viên ĐH Văn Lang (VLU Cơ sở 3 Gò Vấp) &amp; các trường lân cận có nhu cầu mua nước, học bài.</li>
            <li><strong>Hành vi tìm kiếm quán:</strong> Lướt xem review trên TikTok/Instagram, đi ngang thấy quán ngay cạnh trường, bạn bè rỉ tai giới thiệu.</li>
            <li><strong>Tiêu chí ưu tiên hàng đầu:</strong> Quán nằm sát trường, máy lạnh mát rượi, chỗ ngồi êm để chạy deadline &amp; trò chuyện ngắn giữa ca.</li>
          </ul>
        </div>

        <!-- Khối 2: Vấn đề sinh viên -->
        <div class="pos-matrix-card">
          <div class="pos-matrix-header">
            <div class="pos-matrix-icon-box red">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
            </div>
            <div>
              <div class="pos-matrix-badge" style="color:#f87171;">VẤN ĐỀ CẦN GIẢI QUYẾT</div>
              <h4 class="pos-matrix-title">Vấn Đề &amp; Nỗi Đau Của Sinh Viên</h4>
            </div>
          </div>
          <ul class="pos-matrix-list">
            <li><strong>Không thích menu đại trà:</strong> Các quán quanh trường đa phần pha chế công nghiệp ngọt gắt, thiếu sự sáng tạo, uống nhanh ngán.</li>
            <li><strong>Né tránh không gian xô bồ:</strong> Quán quá ồn ào không thể tập trung, thiếu chỗ ngồi và ổ cắm điện vào giờ cao điểm giữa các ca học.</li>
            <li><strong>Áp lực thời gian:</strong> Quán phục vụ quá lâu làm trễ giờ điểm danh vào lớp hoặc không kịp nghỉ ngơi sau tiết học căng thẳng.</li>
          </ul>
        </div>

        <!-- Khối 3: Lợi ích khác biệt USP -->
        <div class="pos-matrix-card matcha-accent">
          <div class="pos-matrix-header">
            <div class="pos-matrix-icon-box matcha">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
            </div>
            <div>
              <div class="pos-matrix-badge" style="color:var(--matcha-bright);">LỢI ÍCH KHÁC BIỆT (USP)</div>
              <h4 class="pos-matrix-title">Giá Trị Độc Bản Tại Olion Coffee</h4>
            </div>
          </div>
          <ul class="pos-matrix-list">
            <li><strong>Đồ uống chất lượng &amp; đặc trưng:</strong> Công thức pha chế thanh dịu độc quyền (Bộ Tứ Matcha Series, Trà trái cây tươi, Cacao nguyên chất).</li>
            <li><strong>Không gian máy lạnh êm ái:</strong> Luôn duy trì máy lạnh mát rượi, âm nhạc chill nhẹ nhàng, wifi mạnh giúp tăng hiệu suất học tập.</li>
            <li><strong>Phục vụ nhanh &amp; Vị trí sát cổng trường:</strong> Mua mang đi trong 2 phút, nhân viên nhiệt tình, mức giá sinh viên dễ chịu (35k - 45k).</li>
          </ul>
        </div>

        <!-- Khối 4: Lý do để tin RTB -->
        <div class="pos-matrix-card matcha-accent">
          <div class="pos-matrix-header">
            <div class="pos-matrix-icon-box emerald">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
            </div>
            <div>
              <div class="pos-matrix-badge" style="color:#34d399;">BẢO CHỨNG NIỀM TIN (RTB)</div>
              <h4 class="pos-matrix-title">Lý Do Sinh Viên Lựa Chọn &amp; Gắn Bó</h4>
            </div>
          </div>
          <ul class="pos-matrix-list">
            <li><strong>Khảo sát thực tế người dùng:</strong> Sinh viên trải nghiệm trực tiếp đều đánh giá cao sự mát mẻ, yên tĩnh và hương vị đồ uống chuẩn gu.</li>
            <li><strong>Chất lượng con người:</strong> Đội ngũ nhân viên am hiểu công thức, pha chế tỉ mỉ, thái độ chu đáo và gần gũi như những người bạn.</li>
            <li><strong>Uy tín truyền miệng:</strong> Được đông đảo sinh viên VLU giới thiệu cho nhau, kiểm chứng chất lượng qua trải nghiệm thực tế mỗi ngày.</li>
          </ul>
        </div>
      </div>

      <!-- Tuyên Ngôn Định Vị Trọng Tâm (Executive Positioning Statement Callout Box) -->
      <div class="pos-stmt-banner">
        <div class="pos-stmt-badge">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="var(--matcha-green)" stroke="var(--matcha-green)"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
          <span>TUYÊN NGÔN ĐỊNH VỊ TRỌNG TÂM DÀNH CHO SINH VIÊN ĐH VĂN LANG</span>
        </div>
        <p class="pos-stmt-lead">
          “Đối với sinh viên đang học tại trường ĐH VLU, các bạn thường mệt mỏi vì áp lực bài vở và thời tiết ngột ngạt. Vậy nên các bạn cần một chỗ nghỉ ngơi mát mẻ để vừa chạy deadline vừa trò chuyện thoải mái mà không lo về giá. <strong style="color:var(--accent-gold-light);">Olion Coffee</strong> là quán cafe không gian máy lạnh, cung cấp không gian để học nhóm, nghỉ ngơi, giải toả áp lực nằm ngay sát trường, mang lại khoảng thời gian nghỉ ngơi mát mẻ, nạp đầy năng lượng và sẵn sàng bắt đầu lại.”
        </p>
        <div class="pos-stmt-tagline">
          <div class="tagline-quote">“Take your time. Find your moment. Begin again.”</div>
          <div class="tagline-sub">(Hãy cứ thong thả. Tìm lấy khoảnh khắc của riêng mình. Và bắt đầu lại.)</div>
        </div>
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
      <p style="color:var(--text-muted);margin-bottom:24px;font-size:15px;line-height:1.6;">
        Hình mẫu đại diện chuẩn xác cho nhóm khách hàng sinh viên năm 3 Đại học Văn Lang có nhu cầu học tập, thư giãn và tiêu dùng đồ uống chất lượng tại Olion Coffee.
      </p>

      <div class="persona-container">
        <!-- Top Ribbon Header -->
        <div class="persona-top-ribbon">
          <div class="persona-dossier-tag">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="3" rx="2"/><path d="M7 7h.01"/><path d="M17 7h.01"/><path d="M7 17h10"/></svg>
            <span>HỒ SƠ KHÁCH HÀNG MỤC TIÊU &bull; GEN Z ĐH VĂN LANG</span>
          </div>
          <div class="live-status-pill">
            <span class="pulsing-green-dot"></span>
            <span>ĐỐI TƯỢNG GEN Z THỰC TẾ TẠI QUÁN</span>
          </div>
        </div>

        <div class="persona-layout-grid">
          <!-- Cột Trái: Chân Dung VIP Frame -->
          <div class="persona-photo-col" onclick="openLightbox('assets/cuoi-ky/persona-doan-minh-trang.webp?v=20261113c', 'Persona: Đoàn Minh Trang (Sinh viên năm 3 ĐH Văn Lang)', 'Đoàn Minh Trang học bài &amp; thưởng thức ly Matcha Dâu tại không gian quán Olion Coffee')">
            <div class="persona-photo-wrapper">
              <div class="persona-photo-live-badge">
                <svg width="13" height="13" viewBox="0 0 24 24" fill="var(--accent-gold)" stroke="var(--accent-gold)" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                <span>KHÁCH MỤC TIÊU VLU</span>
              </div>
              <div class="persona-photo-zoom-btn" title="Phóng to ảnh nét cao">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/><line x1="11" y1="8" x2="11" y2="14"/><line x1="8" y1="11" x2="14" y2="11"/></svg>
              </div>
              <img src="assets/cuoi-ky/persona-doan-minh-trang.webp?v=20261113c" alt="Đoàn Minh Trang - Sinh viên năm 3 thưởng thức Matcha Dâu tại quán Olion Coffee" class="persona-photo-img" />
            </div>
            <div class="persona-photo-plate">
              <div class="persona-photo-name">
                <span>Đoàn Minh Trang</span>
                <span style="font-size:13px;color:var(--accent-gold);font-weight:700;">21 tuổi</span>
              </div>
              <div class="persona-photo-role">
                Sinh viên năm 3 ĐH Văn Lang (CS3 Gò Vấp) &bull; Khách quen chạy deadline &amp; thưởng thức Matcha Dâu tại Olion Coffee
              </div>
              <div class="persona-zoom-callout">
                <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/><line x1="11" y1="8" x2="11" y2="14"/><line x1="8" y1="11" x2="14" y2="11"/></svg>
                <span>Bấm trực tiếp vào ảnh để phóng to nét cao</span>
              </div>
            </div>
          </div>

          <!-- Cột Phải: Bảng Chi Tiết Thuộc Tính & Insight Chuyên Sâu -->
          <div class="persona-details-col">
            <div class="persona-name-banner">
              <h3 class="persona-hero-name">Đoàn Minh Trang</h3>
              <div class="persona-quick-chips">
                <span class="persona-chip highlight">
                  <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg>
                  <span>Sinh viên năm 3 (21 tuổi)</span>
                </span>
                <span class="persona-chip">
                  <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="var(--matcha-green)" stroke-width="2"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>
                  <span>ĐH Văn Lang CS3 (Gò Vấp)</span>
                </span>
                <span class="persona-chip">
                  <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="var(--accent-gold)" stroke-width="2"><rect width="18" height="12" x="3" y="4" rx="2"/><line x1="2" y1="20" x2="22" y2="20"/></svg>
                  <span>Thói quen: Laptop, Sổ tay &amp; Deadline</span>
                </span>
                <span class="persona-chip highlight">
                  <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#f87171" stroke-width="2"><path d="M17 8h1a4 4 0 1 1 0 8h-1"/><path d="M3 8h14v9a4 4 0 0 1-4 4H7a4 4 0 0 1-4-4Z"/></svg>
                  <span>Món gu: Matcha Dâu Olion</span>
                </span>
              </div>
            </div>

            <!-- Executive Signature Quote Card -->
            <div class="persona-quote-card">
              <div class="persona-quote-mark">&ldquo;</div>
              <div class="persona-quote-text">
                &ldquo;Giá có thể cao một chút nhưng phải ngon, có chỗ ngồi thoải mái để nghỉ ngơi, làm bài, nói chuyện với bạn khi rảnh.&rdquo;
              </div>
              <div class="persona-quote-source">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><path d="M3 21c3 0 7-1 7-8V5c0-1.25-.75-2-2-2H4c-1.25 0-2 .75-2 2v6c0 1.25.75 2 2 2h4c-.5 2.5-2 4-5 4v4zm14 0c3 0 7-1 7-8V5c0-1.25-.75-2-2-2h-4c-1.25 0-2 .75-2 2v6c0 1.25.75 2 2 2h4c-.5 2.5-2 4-5 4v4z"/></svg>
                <span>Khảo sát thực tế tiếng nói khách hàng sinh viên Văn Lang &bull; Báo cáo cuối kỳ</span>
              </div>
            </div>

            <!-- 5 Thuộc Tính Chuẩn Xác Từ Báo Cáo Cuối Kỳ -->
            <div class="persona-traits-grid">
              <!-- 1. Hành vi số -->
              <div class="persona-trait-card">
                <div class="trait-icon-box green">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="14" height="20" x="5" y="2" rx="2" ry="2"/><path d="M12 18h.01"/></svg>
                </div>
                <div class="trait-content">
                  <div class="trait-header-title" style="color:#4ade80;">HÀNH VI SỐ</div>
                  <div class="trait-body-text">
                    Lướt TikTok xem review đồ uống hot trend, tìm quán thông qua giới thiệu của bạn bè và đánh giá mạng xã hội.
                  </div>
                </div>
              </div>

              <!-- 2. Mục tiêu -->
              <div class="persona-trait-card">
                <div class="trait-icon-box gold">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>
                </div>
                <div class="trait-content">
                  <div class="trait-header-title" style="color:var(--accent-gold);">MỤC TIÊU</div>
                  <div class="trait-body-text">
                    Mua mang đi nhanh gọn trước giờ học, có không gian mát mẻ để trò chuyện với bạn bè giữa ca và cắm máy chạy deadline.
                  </div>
                </div>
              </div>

              <!-- 3. Nỗi đau -->
              <div class="persona-trait-card">
                <div class="trait-icon-box red">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
                </div>
                <div class="trait-content">
                  <div class="trait-header-title" style="color:#f87171;">NỖI ĐAU (PAIN POINT)</div>
                  <div class="trait-body-text">
                    Menu các quán xá quanh trường đại trà, pha chế ngọt gắt công nghiệp, chưa có sự đột phá hay thức uống sáng tạo.
                  </div>
                </div>
              </div>

              <!-- 4. Rào cản -->
              <div class="persona-trait-card">
                <div class="trait-icon-box orange">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
                </div>
                <div class="trait-content">
                  <div class="trait-header-title" style="color:#fb923c;">RÀO CẢN</div>
                  <div class="trait-body-text">
                    Sợ nước uống không hợp khẩu vị mà giá lại đắt; ngại những quán ồn ào không thể tập trung làm bài học nhóm.
                  </div>
                </div>
              </div>

              <!-- 5. Tin vào -->
              <div class="persona-trait-card full-width">
                <div class="trait-icon-box emerald">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/></svg>
                </div>
                <div class="trait-content">
                  <div class="trait-header-title" style="color:#34d399;">TIN VÀO (BELIEF &amp; TRUST)</div>
                  <div class="trait-body-text">
                    Lời giới thiệu chân thật từ bạn bè thân thiết và trải nghiệm thực tế người thật việc thật tại không gian quán Olion Coffee.
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>'''

    s1_pos = text.find('<!-- ========================================================\n       MỤC 1: TỔNG QUAN DỰ ÁN')
    s3_pos = text.find('<!-- ========================================================\n       MỤC 3: KPI DỰ ÁN')

    if s1_pos == -1 or s3_pos == -1:
        print("ERROR finding section 1 or 3 markers!", s1_pos, s3_pos)
        return

    text = text[:s1_pos] + new_sec_1_and_2 + '\n\n' + text[s3_pos:]

    with open('scripts/build_cuoi_ky_final.py', 'w', encoding='utf-8') as f:
        f.write(text)

    print("SUCCESS: scripts/build_cuoi_ky_final.py updated successfully!")

if __name__ == '__main__':
    patch_builder()
