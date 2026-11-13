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
  </section>

  <!-- ========================================================
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
      <h3 style="font-family:var(--font-serif);font-size:24px;color:#2C211B;margin:32px 0 16px;display:flex;align-items:center;gap:10px;">
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
          <div class="persona-photo-col" onclick="openLightbox('assets/cuoi-ky/persona-doan-minh-trang.webp?v=20261113_final', 'Persona: Đoàn Minh Trang (Sinh viên năm 3 ĐH Văn Lang)', 'Đoàn Minh Trang học bài &amp; thưởng thức ly Matcha Dâu tại không gian quán Olion Coffee')">
            <div class="persona-photo-wrapper">
              <div class="persona-photo-live-badge">
                <svg width="13" height="13" viewBox="0 0 24 24" fill="var(--accent-gold)" stroke="var(--accent-gold)" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                <span>KHÁCH MỤC TIÊU VLU</span>
              </div>
              <div class="persona-photo-zoom-btn" title="Phóng to ảnh nét cao">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/><line x1="11" y1="8" x2="11" y2="14"/><line x1="8" y1="11" x2="14" y2="11"/></svg>
              </div>
              <img src="assets/cuoi-ky/persona-doan-minh-trang.webp?v=20261113_final" alt="Đoàn Minh Trang - Sinh viên năm 3 thưởng thức Matcha Dâu tại quán Olion Coffee" class="persona-photo-img" />
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

      <!-- Bộ 2 Ảnh Minh Chứng Biểu Đồ từ Báo Cáo Gốc (Đã tách thành 2 hàng riêng, hiển thị 100% không bị crop) -->
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

      <!-- Bảng So Sánh 4 Kênh (Tự động xuống hàng, hiển thị trọn vẹn 100% khi kéo xuống) -->
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

      <!-- 1. DẢI THẺ CHIẾN LƯỢC ĐỊNH HƯỚNG 4 KÊNH (LUXURY CARDS GRID) -->
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
