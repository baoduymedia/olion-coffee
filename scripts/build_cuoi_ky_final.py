import re
import os

def run():
    with open('scripts/clean_source_build.py', 'r', encoding='utf-8') as f:
        src = f.read()

    with open('campaign-report.html', 'r', encoding='utf-8') as f:
        src_html = f.read()

    style_start = src_html.find('<style>')
    style_end = src_html.find('</style>')
    base_css = src_html[style_start+7:style_end]

    start_extra = src.find('extra_css = """')
    end_extra = src.find('"""', start_extra + 16)
    extra_css = src[start_extra+15:end_extra]
    extra_css = extra_css.replace('-webkit-line-clamp: 2;', '-webkit-line-clamp: unset;')
    extra_css = extra_css.replace('display: -webkit-box;', 'display: block;')

    # Canva Palette CSS with Overflow-Proof PC Layout
    canva_palette_css = """
    /* ========================================================
       CANVA BRAND COLOR PALETTE & OVERFLOW-PROOF PC DESIGN
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
      --bg-glass: rgba(255, 255, 255, 0.96) !important;
      
      --crema: #2C211B !important;
      --crema-muted: #4A3B32 !important;
      --text-main: #2C211B !important;
      --text-white: #2C211B !important;
      --text-muted: #5C4D44 !important;
      --text-dim: #78685E !important;
      
      --accent-gold: #7C5A32 !important;
      --accent-gold-light: #5C4328 !important;
      --accent-gold-glow: rgba(184, 165, 139, 0.35) !important;
      --border-brass: rgba(184, 165, 139, 0.45) !important;
      --border-subtle: rgba(44, 33, 27, 0.12) !important;
      
      --matcha: #7C8268 !important;
      --matcha-green: #2E7D32 !important;
      --matcha-bright: #8F957B !important;
      --matcha-dark: #464C37 !important;
      --matcha-glow: rgba(124, 130, 104, 0.3) !important;
      --border-matcha: rgba(124, 130, 104, 0.4) !important;
      
      --accent-rust: #D32F2F !important;
      --accent-red: #D32F2F !important;
      
      --shadow-wood: 0 10px 30px rgba(44, 33, 27, 0.08), 0 2px 8px rgba(184, 165, 139, 0.15) !important;
      --shadow-matcha: 0 10px 30px rgba(124, 130, 104, 0.12), 0 2px 8px rgba(124, 130, 104, 0.2) !important;
    }

    /* ZERO HORIZONTAL SCROLL GUARANTEE */
    html, body {
      background-color: #F6F1E7 !important;
      color: #2C211B !important;
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
      overflow-x: hidden !important;
      max-width: 100vw !important;
      width: 100% !important;
      margin: 0 !important;
      padding: 0 !important;
      box-sizing: border-box !important;
    }

    *, *::before, *::after {
      box-sizing: border-box !important;
    }

    /* Keyframes */
    @keyframes pulseBeacon {
      0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(124, 130, 104, 0.7); }
      70% { transform: scale(1.15); box-shadow: 0 0 0 8px rgba(124, 130, 104, 0); }
      100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(124, 130, 104, 0); }
    }

    /* Reading Progress Bar */
    .scroll-progress-line {
      background: linear-gradient(90deg, #B8A58B, #7C8268, #D32F2F) !important;
      height: 4px !important;
      box-shadow: 0 0 10px rgba(124, 130, 104, 0.5) !important;
    }

    /* Standard Shell Container */
    .shell {
      max-width: 1240px !important;
      margin: 0 auto !important;
      padding: 0 24px !important;
      width: 100% !important;
    }
    @media (max-width: 768px) {
      .shell {
        padding: 0 16px !important;
      }
    }

    /* ========================================================
       PC HEADER & NON-OVERFLOWING NAVIGATION BAR
       ======================================================== */
    .cafe-header {
      position: fixed !important;
      top: 0 !important;
      left: 0 !important;
      right: 0 !important;
      width: 100% !important;
      z-index: 1000 !important;
      background: rgba(246, 241, 231, 0.96) !important;
      backdrop-filter: blur(16px) !important;
      -webkit-backdrop-filter: blur(16px) !important;
      border-bottom: 1.5px solid rgba(184, 165, 139, 0.4) !important;
      box-shadow: 0 4px 20px rgba(44, 33, 27, 0.05) !important;
    }
    .header-inner {
      max-width: 1380px !important;
      height: 64px !important;
      display: flex !important;
      align-items: center !important;
      justify-content: space-between !important;
      gap: 10px !important;
      padding: 0 20px !important;
    }
    .header-brand {
      display: flex !important;
      align-items: center !important;
      gap: 10px !important;
      flex-shrink: 0 !important;
    }
    .header-brand img {
      height: 32px !important;
      width: auto !important;
      display: block !important;
    }
    .header-brand-divider {
      width: 1px !important;
      height: 24px !important;
      background: rgba(184, 165, 139, 0.45) !important;
    }
    .badge-hub-title {
      color: #2C211B !important;
      font-weight: 800 !important;
      font-size: 13px !important;
      letter-spacing: 0.04em !important;
    }
    .badge-hub-sub {
      color: #7C8268 !important;
      font-weight: 600 !important;
      font-size: 11px !important;
      white-space: nowrap !important;
    }

    /* Compact 8-Pill Navigation for PC */
    .header-menu-nav {
      display: flex !important;
      align-items: center !important;
      gap: 4px !important;
      flex-shrink: 1 !important;
      min-width: 0 !important;
    }
    .menu-link {
      background: #FFFFFF !important;
      border: 1px solid rgba(184, 165, 139, 0.45) !important;
      color: #2C211B !important;
      font-size: 11.5px !important;
      font-weight: 700 !important;
      padding: 5px 8px !important;
      border-radius: 16px !important;
      text-decoration: none !important;
      white-space: nowrap !important;
      box-shadow: 0 1px 3px rgba(44, 33, 27, 0.04) !important;
      transition: all 0.2s ease !important;
    }
    .menu-link:hover {
      background: #FAF7F2 !important;
      border-color: #B8A58B !important;
      color: #2C211B !important;
      transform: translateY(-1px) !important;
    }
    .menu-link.active {
      background: #2C211B !important;
      border-color: #2C211B !important;
      color: #FFFFFF !important;
      box-shadow: 0 3px 10px rgba(44, 33, 27, 0.2) !important;
    }

    .header-actions {
      display: flex !important;
      align-items: center !important;
      gap: 6px !important;
      flex-shrink: 0 !important;
    }
    .action-btn-icon {
      background: #FFFFFF !important;
      border: 1px solid rgba(184, 165, 139, 0.4) !important;
      color: #2C211B !important;
      border-radius: 50% !important;
      width: 34px !important;
      height: 34px !important;
      display: inline-flex !important;
      align-items: center !important;
      justify-content: center !important;
      cursor: pointer !important;
      transition: all 0.2s ease !important;
    }
    .action-btn-icon:hover {
      background: #FAF7F2 !important;
      color: #7C8268 !important;
    }
    .btn-home-link {
      background: #7C8268 !important;
      color: #FFFFFF !important;
      border: 1px solid #7C8268 !important;
      border-radius: 16px !important;
      padding: 5px 11px !important;
      font-weight: 700 !important;
      font-size: 12px !important;
      text-decoration: none !important;
      display: inline-flex !important;
      align-items: center !important;
      gap: 5px !important;
      white-space: nowrap !important;
      transition: all 0.2s ease !important;
    }
    .btn-home-link:hover {
      background: #464C37 !important;
      color: #FFFFFF !important;
    }

    @media (max-width: 1240px) {
      .badge-hub-sub { display: none !important; }
      .menu-link { font-size: 11px !important; padding: 4px 6px !important; }
      .btn-home-link span { display: none !important; }
    }
    @media (max-width: 1040px) {
      .header-menu-nav { display: none !important; }
      .btn-home-link { display: none !important; }
      .mobile-menu-btn { display: flex !important; }
    }

    /* Mobile Drawer */
    .mobile-nav-drawer {
      background: #F6F1E7 !important;
      border-left: 2px solid rgba(184, 165, 139, 0.4) !important;
      box-shadow: -10px 0 35px rgba(44, 33, 27, 0.15) !important;
    }
    .mobile-nav-link {
      color: #2C211B !important;
      border-bottom: 1px solid rgba(184, 165, 139, 0.25) !important;
      font-weight: 600 !important;
    }
    .mobile-nav-link:hover, .mobile-nav-link.active {
      background: rgba(184, 165, 139, 0.18) !important;
      color: #7C8268 !important;
      font-weight: 700 !important;
    }

    /* Global Headings & Text Colors */
    h1, h2, h3, h4, h5, h6,
    .section-main-heading,
    .hero-title,
    .hero-title-main,
    .overview-card-value,
    .hero-stat-num,
    .pos-matrix-title,
    .persona-hero-name,
    .persona-photo-name,
    .social-card-title,
    .round-card-num,
    .stat-chip,
    .feed-brand-name,
    .chart-evidence-title,
    .proposal-poster-title,
    .org-leader-name,
    .org-mini-name {
      color: #2C211B !important;
    }

    p, li, .hero-lead, .overview-card-desc, .pos-matrix-list li, .persona-bio-row,
    .persona-quote-text, .trait-desc, .social-card-desc, .chart-evidence-desc,
    .report-table td, .wrap-content-table td {
      color: #4A3B32 !important;
    }

    .section-chapter-tag {
      background: rgba(184, 165, 139, 0.18) !important;
      color: #2C211B !important;
      border: 1.5px solid rgba(184, 165, 139, 0.45) !important;
      font-weight: 800 !important;
      letter-spacing: 0.08em !important;
      border-radius: 20px !important;
      padding: 5px 14px !important;
      display: inline-flex !important;
    }
    .section-chapter-tag.matcha {
      background: rgba(124, 130, 104, 0.16) !important;
      color: #3E4330 !important;
      border-color: rgba(124, 130, 104, 0.5) !important;
    }

    .report-section {
      border-top: 1.5px solid rgba(184, 165, 139, 0.35) !important;
      padding: 50px 0 !important;
      background: #F6F1E7 !important;
      color: #2C211B !important;
    }

    /* Hero Section */
    .hero-section {
      background: linear-gradient(180deg, #FAF6F0 0%, #F6F1E7 100%) !important;
      border-bottom: 2px solid rgba(184, 165, 139, 0.4) !important;
      padding: 45px 0 25px !important;
      color: #2C211B !important;
    }
    .hero-eyebrow {
      background: rgba(184, 165, 139, 0.22) !important;
      border: 1px solid rgba(184, 165, 139, 0.5) !important;
      color: #2C211B !important;
      font-weight: 800 !important;
      border-radius: 20px !important;
      padding: 6px 16px !important;
      display: inline-flex !important;
      align-items: center !important;
      gap: 8px !important;
      margin-bottom: 18px !important;
    }
    .hero-title-main {
      font-family: 'Cormorant Garamond', Georgia, serif !important;
      font-weight: 700 !important;
      font-size: clamp(28px, 4vw, 42px) !important;
      color: #2C211B !important;
      display: block !important;
      line-height: 1.2 !important;
    }
    .hero-title-sub {
      font-family: 'Cormorant Garamond', Georgia, serif !important;
      font-size: clamp(22px, 3.2vw, 32px) !important;
      display: block !important;
      margin-top: 6px !important;
    }
    .hero-title-sub .text-matcha { color: #7C8268 !important; font-weight: 700 !important; }
    .hero-title-sub .text-gold { color: #B8A58B !important; font-weight: 600 !important; }
    .hero-lead {
      color: #4A3B32 !important;
      font-size: 15.5px !important;
      line-height: 1.7 !important;
      max-width: 900px !important;
      margin-top: 14px !important;
    }

    /* Slogan Callout Card */
    .hero-slogan-card {
      background: #FFFFFF !important;
      border: 2px solid rgba(184, 165, 139, 0.5) !important;
      border-radius: 18px !important;
      padding: 22px 28px !important;
      margin: 24px 0 !important;
      box-shadow: 0 10px 30px rgba(44, 33, 27, 0.07) !important;
    }
    .hero-slogan-badge {
      background: rgba(124, 130, 104, 0.15) !important;
      color: #3E4330 !important;
      border: 1px solid rgba(124, 130, 104, 0.4) !important;
      border-radius: 20px !important;
      padding: 5px 12px !important;
      font-size: 11.5px !important;
      font-weight: 800 !important;
      text-transform: uppercase !important;
      display: inline-flex !important;
      align-items: center !important;
      gap: 6px !important;
      margin-bottom: 10px !important;
    }
    .hero-slogan-quote {
      font-family: 'Cormorant Garamond', Georgia, serif !important;
      font-size: 22px !important;
      font-weight: 700 !important;
      font-style: italic !important;
      color: #2C211B !important;
      line-height: 1.4 !important;
    }
    .hero-slogan-vi {
      color: #7C8268 !important;
      font-size: 14px !important;
      font-weight: 600 !important;
      margin-top: 6px !important;
    }

    /* Hero Banner Image Box */
    .hero-banner-image-box {
      background: #FFFFFF !important;
      border: 2px solid rgba(184, 165, 139, 0.45) !important;
      border-radius: 20px !important;
      overflow: hidden !important;
      box-shadow: 0 12px 32px rgba(44, 33, 27, 0.08) !important;
      margin-bottom: 24px !important;
    }
    .hero-banner-caption {
      background: #FAF7F2 !important;
      border-top: 1.5px solid rgba(184, 165, 139, 0.35) !important;
      padding: 12px 18px !important;
      color: #2C211B !important;
      font-size: 13px !important;
      display: flex !important;
      flex-wrap: wrap !important;
      justify-content: space-between !important;
      align-items: center !important;
      gap: 8px !important;
    }

    /* Hero 4 Stat Metric Cards Strip */
    .hero-stat-strip {
      display: grid !important;
      grid-template-columns: repeat(4, 1fr) !important;
      gap: 16px !important;
      margin: 24px 0 16px !important;
    }
    @media (max-width: 900px) {
      .hero-stat-strip {
        grid-template-columns: repeat(2, 1fr) !important;
        gap: 12px !important;
      }
    }
    .hero-stat-item {
      background: #FFFFFF !important;
      border: 2px solid rgba(184, 165, 139, 0.45) !important;
      border-radius: 18px !important;
      padding: 20px 16px !important;
      text-align: center !important;
      box-shadow: 0 8px 24px rgba(44, 33, 27, 0.06) !important;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
      display: flex !important;
      flex-direction: column !important;
      align-items: center !important;
      justify-content: center !important;
    }
    .hero-stat-item:hover {
      transform: translateY(-5px) !important;
      border-color: #B8A58B !important;
      box-shadow: 0 16px 36px rgba(44, 33, 27, 0.12) !important;
    }
    .hero-stat-icon {
      background: rgba(184, 165, 139, 0.18) !important;
      color: #2C211B !important;
      width: 42px !important;
      height: 42px !important;
      border-radius: 12px !important;
      display: inline-flex !important;
      align-items: center !important;
      justify-content: center !important;
      margin-bottom: 8px !important;
    }
    .hero-stat-item.matcha-card .hero-stat-icon {
      background: rgba(124, 130, 104, 0.18) !important;
      color: #7C8268 !important;
    }
    .hero-stat-num {
      font-size: 26px !important;
      font-weight: 800 !important;
      color: #2C211B !important;
      margin-bottom: 4px !important;
    }
    .hero-stat-lbl {
      font-size: 13px !important;
      font-weight: 700 !important;
      color: #7C8268 !important;
      text-transform: uppercase !important;
      letter-spacing: 0.05em !important;
    }
    .hero-stat-sub {
      font-size: 11.5px !important;
      color: #8C7B70 !important;
      margin-top: 4px !important;
    }

    /* Section 1: Overview 4 Pillars */
    .overview-cards-row {
      display: grid !important;
      grid-template-columns: repeat(4, 1fr) !important;
      gap: 16px !important;
      margin: 24px 0 !important;
    }
    @media (max-width: 900px) {
      .overview-cards-row {
        grid-template-columns: repeat(2, 1fr) !important;
      }
    }
    @media (max-width: 540px) {
      .overview-cards-row {
        grid-template-columns: 1fr !important;
      }
    }
    .overview-card-item {
      background: #FFFFFF !important;
      border: 1.5px solid rgba(184, 165, 139, 0.45) !important;
      border-radius: 18px !important;
      padding: 22px 20px !important;
      box-shadow: 0 8px 24px rgba(44, 33, 27, 0.06) !important;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
    }
    .overview-card-item:hover {
      transform: translateY(-5px) !important;
      border-color: #B8A58B !important;
      box-shadow: 0 16px 36px rgba(44, 33, 27, 0.1) !important;
    }
    .overview-card-label {
      color: #7C8268 !important;
      font-size: 12px !important;
      font-weight: 800 !important;
      text-transform: uppercase !important;
      letter-spacing: 0.08em !important;
      display: flex !important;
      align-items: center !important;
      gap: 6px !important;
    }
    .overview-card-value {
      color: #2C211B !important;
      font-size: 17.5px !important;
      font-weight: 800 !important;
      margin: 8px 0 6px !important;
    }
    .overview-card-desc {
      color: #4A3B32 !important;
      font-size: 13.5px !important;
      line-height: 1.6 !important;
    }

    /* Positioning Matrix */
    .pos-matrix-grid {
      display: grid !important;
      grid-template-columns: repeat(2, 1fr) !important;
      gap: 18px !important;
      margin: 24px 0 !important;
    }
    @media (max-width: 768px) {
      .pos-matrix-grid {
        grid-template-columns: 1fr !important;
      }
    }
    .pos-matrix-card {
      background: #FFFFFF !important;
      border: 1.5px solid rgba(184, 165, 139, 0.45) !important;
      border-radius: 18px !important;
      padding: 22px 24px !important;
      box-shadow: 0 8px 24px rgba(44, 33, 27, 0.06) !important;
      transition: all 0.3s ease !important;
    }
    .pos-matrix-card:hover {
      transform: translateY(-4px) !important;
      border-color: #B8A58B !important;
      box-shadow: 0 16px 36px rgba(44, 33, 27, 0.1) !important;
    }
    .pos-matrix-header {
      display: flex !important;
      align-items: center !important;
      gap: 12px !important;
      margin-bottom: 14px !important;
    }
    .pos-matrix-title {
      font-family: 'Cormorant Garamond', Georgia, serif !important;
      font-size: 19px !important;
      font-weight: 700 !important;
      color: #2C211B !important;
      margin: 0 !important;
    }
    .pos-matrix-list {
      list-style: none !important;
      padding: 0 !important;
      margin: 0 !important;
      display: flex !important;
      flex-direction: column !important;
      gap: 10px !important;
    }
    .pos-matrix-list li {
      color: #4A3B32 !important;
      font-size: 13.5px !important;
      line-height: 1.6 !important;
      position: relative !important;
      padding-left: 20px !important;
    }
    .pos-matrix-list li strong {
      color: #2C211B !important;
      font-weight: 700 !important;
    }
    .pos-matrix-list li::before {
      content: '✓' !important;
      position: absolute !important;
      left: 0 !important;
      top: 0 !important;
      color: #7C8268 !important;
      font-weight: bold !important;
    }

    /* Positioning Statement Banner */
    .pos-stmt-banner {
      background: #FFFFFF !important;
      border: 2px solid rgba(184, 165, 139, 0.5) !important;
      border-radius: 18px !important;
      padding: 26px 30px !important;
      margin: 28px 0 !important;
      box-shadow: 0 10px 30px rgba(44, 33, 27, 0.07) !important;
    }
    .pos-stmt-badge {
      background: rgba(124, 130, 104, 0.15) !important;
      color: #3E4330 !important;
      border: 1px solid rgba(124, 130, 104, 0.4) !important;
      border-radius: 20px !important;
      padding: 5px 14px !important;
      font-size: 12px !important;
      font-weight: 800 !important;
      text-transform: uppercase !important;
      display: inline-flex !important;
      align-items: center !important;
      gap: 6px !important;
    }
    .pos-stmt-lead {
      color: #4A3B32 !important;
      font-size: 15.5px !important;
      line-height: 1.7 !important;
      margin-top: 12px !important;
    }
    .tagline-quote {
      color: #2C211B !important;
      font-family: 'Cormorant Garamond', Georgia, serif !important;
      font-size: 21px !important;
      font-weight: 700 !important;
      font-style: italic !important;
    }
    .tagline-sub {
      color: #7C8268 !important;
      font-size: 13.5px !important;
      font-weight: 600 !important;
      margin-top: 4px !important;
    }

    /* Persona Dossier */
    .persona-container {
      background: #FFFFFF !important;
      border: 2px solid rgba(184, 165, 139, 0.5) !important;
      border-radius: 22px !important;
      padding: 28px !important;
      margin-top: 28px !important;
      box-shadow: 0 16px 45px rgba(44, 33, 27, 0.08) !important;
      width: 100% !important;
      max-width: 100% !important;
      box-sizing: border-box !important;
    }
    .persona-top-ribbon {
      display: flex !important;
      justify-content: space-between !important;
      align-items: center !important;
      flex-wrap: wrap !important;
      gap: 12px !important;
      margin-bottom: 24px !important;
      padding-bottom: 16px !important;
      border-bottom: 1.5px solid rgba(184, 165, 139, 0.3) !important;
    }
    .persona-dossier-tag {
      background: rgba(184, 165, 139, 0.18) !important;
      color: #2C211B !important;
      border: 1px solid rgba(184, 165, 139, 0.45) !important;
      border-radius: 20px !important;
      padding: 6px 14px !important;
      font-size: 12px !important;
      font-weight: 700 !important;
      display: inline-flex !important;
      align-items: center !important;
      gap: 6px !important;
    }
    .live-status-pill {
      background: rgba(124, 130, 104, 0.15) !important;
      color: #3E4330 !important;
      border: 1px solid rgba(124, 130, 104, 0.45) !important;
      border-radius: 20px !important;
      padding: 5px 12px !important;
      font-size: 11.5px !important;
      font-weight: 700 !important;
      display: inline-flex !important;
      align-items: center !important;
      gap: 6px !important;
    }
    .pulsing-green-dot {
      background: #7C8268 !important;
      width: 8px !important;
      height: 8px !important;
      border-radius: 50% !important;
      animation: pulseBeacon 1.8s infinite !important;
    }

    .persona-layout-grid {
      display: grid !important;
      grid-template-columns: 360px 1fr !important;
      gap: 28px !important;
      align-items: start !important;
    }
    @media (max-width: 900px) {
      .persona-layout-grid {
        grid-template-columns: 1fr !important;
        gap: 22px !important;
      }
    }

    .persona-photo-col {
      background: #FFFFFF !important;
      border: 2px solid rgba(184, 165, 139, 0.45) !important;
      border-radius: 18px !important;
      overflow: hidden !important;
      box-shadow: 0 12px 32px rgba(44, 33, 27, 0.08) !important;
      cursor: zoom-in !important;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
    }
    .persona-photo-col:hover {
      transform: translateY(-4px) !important;
      border-color: #B8A58B !important;
      box-shadow: 0 18px 40px rgba(44, 33, 27, 0.12) !important;
    }
    .persona-photo-wrapper {
      position: relative !important;
      width: 100% !important;
      aspect-ratio: 3 / 4 !important;
      max-height: 500px !important;
      overflow: hidden !important;
      background: #FAF6F0 !important;
    }
    .persona-photo-img {
      width: 100% !important;
      height: 100% !important;
      object-fit: cover !important;
      object-position: center 38% !important;
      display: block !important;
      transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1) !important;
    }
    .persona-photo-col:hover .persona-photo-img {
      transform: scale(1.03) !important;
    }
    .persona-photo-plate {
      padding: 16px 18px !important;
      background: #FAF7F2 !important;
      border-top: 1.5px solid rgba(184, 165, 139, 0.3) !important;
    }
    .persona-photo-name {
      display: flex !important;
      justify-content: space-between !important;
      align-items: center !important;
      font-family: 'Cormorant Garamond', Georgia, serif !important;
      font-size: 20px !important;
      font-weight: 700 !important;
      color: #2C211B !important;
      margin-bottom: 4px !important;
    }
    .persona-photo-role {
      font-size: 13px !important;
      color: #7C8268 !important;
      font-weight: 600 !important;
      line-height: 1.45 !important;
    }

    .persona-hero-name {
      color: #2C211B !important;
      -webkit-text-fill-color: #2C211B !important;
      background: none !important;
      font-family: 'Cormorant Garamond', Georgia, serif !important;
      font-size: 32px !important;
      font-weight: 700 !important;
      margin: 0 0 10px 0 !important;
    }
    .persona-chip {
      display: inline-flex !important;
      align-items: center !important;
      gap: 6px !important;
      padding: 6px 12px !important;
      border-radius: 20px !important;
      font-size: 12.5px !important;
      font-weight: 600 !important;
      background: #FAF7F2 !important;
      border: 1px solid rgba(184, 165, 139, 0.4) !important;
      color: #2C211B !important;
    }
    .persona-chip.highlight {
      background: rgba(124, 130, 104, 0.15) !important;
      border-color: rgba(124, 130, 104, 0.4) !important;
      color: #3E4330 !important;
      font-weight: 700 !important;
    }
    .persona-quote-card {
      background: #FFFFFF !important;
      border: 1.5px solid rgba(184, 165, 139, 0.4) !important;
      border-left: 5px solid #7C8268 !important;
      border-radius: 14px !important;
      padding: 18px 22px !important;
      box-shadow: 0 6px 18px rgba(44, 33, 27, 0.05) !important;
      margin: 16px 0 !important;
    }
    .persona-quote-text {
      color: #2C211B !important;
      font-family: 'Cormorant Garamond', Georgia, serif !important;
      font-size: 19px !important;
      font-weight: 700 !important;
      font-style: italic !important;
      line-height: 1.55 !important;
    }
    .persona-quote-source {
      color: #7C8268 !important;
      font-size: 12.5px !important;
      font-weight: 700 !important;
      margin-top: 8px !important;
      display: flex !important;
      align-items: center !important;
      gap: 6px !important;
    }
    .persona-traits-grid {
      display: grid !important;
      grid-template-columns: repeat(2, 1fr) !important;
      gap: 14px !important;
    }
    @media (max-width: 640px) {
      .persona-traits-grid {
        grid-template-columns: 1fr !important;
      }
    }
    .persona-trait-card, .persona-trait-card.full-width {
      background: #FFFFFF !important;
      border: 1.5px solid rgba(184, 165, 139, 0.4) !important;
      border-radius: 14px !important;
      padding: 16px 18px !important;
      box-shadow: 0 6px 18px rgba(44, 33, 27, 0.04) !important;
      display: flex !important;
      align-items: flex-start !important;
      gap: 14px !important;
      transition: all 0.3s ease !important;
    }
    .persona-trait-card:hover, .persona-trait-card.full-width:hover {
      transform: translateY(-3px) !important;
      border-color: #B8A58B !important;
      box-shadow: 0 12px 28px rgba(44, 33, 27, 0.09) !important;
      background: #FFFFFF !important;
    }
    .trait-icon-box {
      width: 40px !important;
      height: 40px !important;
      min-width: 40px !important;
      border-radius: 10px !important;
      display: flex !important;
      align-items: center !important;
      justify-content: center !important;
    }
    .trait-icon-box.green {
      background: rgba(124, 130, 104, 0.15) !important;
      color: #464C37 !important;
      border: 1px solid rgba(124, 130, 104, 0.35) !important;
    }
    .trait-icon-box.gold {
      background: rgba(184, 165, 139, 0.2) !important;
      color: #2C211B !important;
      border: 1px solid rgba(184, 165, 139, 0.4) !important;
    }
    .trait-icon-box.red {
      background: rgba(211, 47, 47, 0.12) !important;
      color: #D32F2F !important;
      border: 1px solid rgba(211, 47, 47, 0.3) !important;
    }
    .trait-header-title {
      font-size: 13.5px !important;
      font-weight: 800 !important;
      text-transform: uppercase !important;
      letter-spacing: 0.05em !important;
      margin-bottom: 4px !important;
      color: #2C211B !important;
    }
    .trait-body-text {
      font-size: 13.5px !important;
      color: #4A3B32 !important;
      line-height: 1.6 !important;
    }

    /* Section 2: Channel QR Cards */
    .channel-qr-grid {
      display: grid !important;
      grid-template-columns: repeat(4, 1fr) !important;
      gap: 20px !important;
      margin: 28px 0 36px !important;
    }
    @media (max-width: 960px) {
      .channel-qr-grid {
        grid-template-columns: repeat(2, 1fr) !important;
        gap: 16px !important;
      }
    }
    @media (max-width: 480px) {
      .channel-qr-grid {
        grid-template-columns: 1fr !important;
        gap: 14px !important;
      }
    }
    .channel-qr-card {
      background: #FFFFFF !important;
      border: 2px solid rgba(184, 165, 139, 0.45) !important;
      border-radius: 20px !important;
      padding: 24px 20px 22px !important;
      display: flex !important;
      flex-direction: column !important;
      align-items: center !important;
      text-align: center !important;
      box-shadow: 0 8px 24px rgba(44, 33, 27, 0.06) !important;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
    }
    .channel-qr-card:hover { transform: translateY(-6px) !important; }
    .channel-qr-card:nth-child(1):hover {
      border-color: #1877F2 !important;
      box-shadow: 0 18px 40px rgba(24, 119, 242, 0.2), 0 0 0 2px rgba(24, 119, 242, 0.4) !important;
    }
    .channel-qr-card:nth-child(2):hover {
      border-color: #2C211B !important;
      box-shadow: 0 18px 40px rgba(44, 33, 27, 0.25), 0 0 0 2px rgba(44, 33, 27, 0.5) !important;
    }
    .channel-qr-card:nth-child(3):hover {
      border-color: #C13584 !important;
      box-shadow: 0 18px 40px rgba(193, 53, 132, 0.2), 0 0 0 2px rgba(193, 53, 132, 0.4) !important;
    }
    .channel-qr-card:nth-child(4):hover {
      border-color: #7C8268 !important;
      box-shadow: 0 18px 40px rgba(124, 130, 104, 0.25), 0 0 0 2px rgba(124, 130, 104, 0.5) !important;
    }

    .channel-qr-badge {
      display: inline-flex !important;
      align-items: center !important;
      gap: 6px !important;
      font-size: 11px !important;
      font-weight: 800 !important;
      text-transform: uppercase !important;
      letter-spacing: 0.08em !important;
      padding: 5px 12px !important;
      border-radius: 20px !important;
      margin-bottom: 14px !important;
    }
    .channel-qr-badge.fb { background: rgba(24, 119, 242, 0.12) !important; color: #1877F2 !important; border: 1px solid rgba(24, 119, 242, 0.3) !important; }
    .channel-qr-badge.tiktok { background: rgba(44, 33, 27, 0.12) !important; color: #2C211B !important; border: 1px solid rgba(44, 33, 27, 0.25) !important; }
    .channel-qr-badge.ig { background: rgba(225, 48, 108, 0.12) !important; color: #C13584 !important; border: 1px solid rgba(225, 48, 108, 0.3) !important; }
    .channel-qr-badge.web { background: rgba(124, 130, 104, 0.15) !important; color: #464C37 !important; border: 1px solid rgba(124, 130, 104, 0.35) !important; }

    .channel-qr-img-box {
      width: 156px !important;
      height: 156px !important;
      background: #FFFFFF !important;
      border: 1.5px solid rgba(184, 165, 139, 0.4) !important;
      border-radius: 14px !important;
      padding: 8px !important;
      margin-bottom: 14px !important;
      cursor: zoom-in !important;
      transition: all 0.25s ease !important;
      box-shadow: 0 4px 14px rgba(44, 33, 27, 0.06) !important;
    }
    .channel-qr-img-box:hover { transform: scale(1.04) !important; }
    .channel-qr-img { width: 100% !important; height: 100% !important; object-fit: contain !important; display: block !important; }
    .channel-qr-name { font-family: 'Cormorant Garamond', Georgia, serif !important; font-size: 19px !important; font-weight: 700 !important; color: #2C211B !important; margin-bottom: 4px !important; }
    .channel-qr-handle { font-size: 12.5px !important; color: #7C8268 !important; font-weight: 600 !important; margin-bottom: 16px !important; }
    .channel-qr-btn {
      display: inline-flex !important;
      align-items: center !important;
      justify-content: center !important;
      gap: 6px !important;
      width: 100% !important;
      padding: 10px 16px !important;
      border-radius: 12px !important;
      font-size: 13px !important;
      font-weight: 700 !important;
      color: #FFFFFF !important;
      text-decoration: none !important;
      transition: all 0.25s ease !important;
      box-shadow: 0 4px 12px rgba(44, 33, 27, 0.15) !important;
    }
    
    .channel-qr-btn.tt, .channel-qr-btn.tiktok { background: #111111 !important; color: #FFFFFF !important; }
    .channel-qr-btn.fb { background: #1877F2 !important; color: #FFFFFF !important; }
    .channel-qr-btn.ig { background: linear-gradient(45deg, #F58529, #DD2A7B, #8134AF) !important; color: #FFFFFF !important; }
    .channel-qr-btn.web { background: #5A6B47 !important; color: #FFFFFF !important; }

    .channel-qr-btn.tiktok { background: #2C211B !important; }
    .channel-qr-btn.ig { background: linear-gradient(45deg, #F58529, #DD2A7B, #8134AF) !important; }
    .channel-qr-btn.web { background: #7C8268 !important; }
    .channel-qr-btn:hover { transform: translateY(-2px) !important; filter: brightness(1.1) !important; color: #FFFFFF !important; }

    /* ========================================================
       CHỐNG KHUẤT CHỮ TRÊN PC & MOBILE - BẢNG ĐA CỘT VUỐT MƯỢT
       ======================================================== */
    .table-scroll-hint {
      display: none;
    }
    @media (max-width: 768px) {
      .table-scroll-hint.mobile-only {
        display: inline-flex !important;
        align-items: center !important;
        gap: 6px !important;
        background: rgba(124, 130, 104, 0.15) !important;
        border: 1px solid rgba(124, 130, 104, 0.4) !important;
        color: #3E4330 !important;
        padding: 6px 12px !important;
        border-radius: 20px !important;
        font-size: 11.5px !important;
        font-weight: 700 !important;
        margin-bottom: 10px !important;
      }
    }

    .report-table-card, .table-container {
      background: #FFFFFF !important;
      border: 1.5px solid rgba(184, 165, 139, 0.45) !important;
      border-radius: 18px !important;
      overflow-x: auto !important; /* Cho phép cuộn ngang mượt mà trên mobile, không bao giờ bị cắt chữ */
      overflow-y: hidden !important;
      -webkit-overflow-scrolling: touch !important;
      box-shadow: 0 8px 24px rgba(44, 33, 27, 0.05) !important;
      width: 100% !important;
      margin: 20px 0 !important;
    }
    .table-scroll-wrap {
      overflow-x: auto !important;
      -webkit-overflow-scrolling: touch !important;
      width: 100% !important;
    }
    table.pdf-table, table.report-table {
      width: 100% !important;
      min-width: 660px !important; /* Đảm bảo đủ chiều rộng hiển thị 5 cột số liệu rõ ràng */
      border-collapse: collapse !important;
      background: #FFFFFF !important;
    }
    table.wrap-content-table {
      width: 100% !important;
      min-width: 0 !important;
      table-layout: auto !important;
      border-collapse: collapse !important;
      background: #FFFFFF !important;
    }
    @media (min-width: 992px) {
      table.wrap-content-table {
        table-layout: fixed !important;
        width: 100% !important;
      }
      table.wrap-content-table th {
        white-space: normal !important;
      }
      table.wrap-content-table th:nth-child(1),
      table.wrap-content-table td:nth-child(1) {
        width: 16% !important;
      }
      table.wrap-content-table th:nth-child(2),
      table.wrap-content-table td:nth-child(2) {
        width: 28% !important;
      }
      table.wrap-content-table th:nth-child(3),
      table.wrap-content-table td:nth-child(3) {
        width: 28% !important;
      }
      table.wrap-content-table th:nth-child(4),
      table.wrap-content-table td:nth-child(4) {
        width: 28% !important;
      }
      #muc-4 .table-container,
      #muc-6 .table-container {
        overflow-x: visible !important;
      }
    }
    table.pdf-table th, table.report-table th {
      background: #2C211B !important; /* Nền Espresso đậm tương phản cao */
      color: #F6F1E7 !important; /* Chữ kem sáng rõ nét, không bao giờ chìm */
      font-size: 12.5px !important;
      font-weight: 800 !important;
      text-transform: uppercase !important;
      letter-spacing: 0.05em !important;
      padding: 13px 16px !important;
      border-bottom: 2px solid #B8A58B !important;
      white-space: nowrap !important;
    }
    table.wrap-content-table th {
      background: #2C211B !important;
      color: #F6F1E7 !important;
      font-size: 13px !important;
      font-weight: 800 !important;
      text-transform: uppercase !important;
      letter-spacing: 0.05em !important;
      padding: 13px 16px !important;
      border-bottom: 2px solid #B8A58B !important;
      white-space: normal !important;
    }
    table.pdf-table td, table.report-table td, table.wrap-content-table td {
      color: #4A3B32 !important;
      font-size: 13.5px !important;
      padding: 13px 16px !important;
      border-bottom: 1px solid rgba(184, 165, 139, 0.25) !important;
      line-height: 1.55 !important;
      white-space: normal !important;
      word-wrap: break-word !important;
    }
    table.pdf-table tr:nth-child(even) td,
    table.report-table tr:nth-child(even) td,
    table.wrap-content-table tr:nth-child(even) td {
      background: #FAF7F2 !important;
    }
    table.pdf-table tr:hover td,
    table.report-table tr:hover td,
    table.wrap-content-table tr:hover td {
      background: rgba(184, 165, 139, 0.12) !important;
    }
    table.pdf-table td.avg-cell {
      background: rgba(184, 165, 139, 0.15) !important;
      color: #2C211B !important;
      font-weight: 800 !important;
    }
    table.pdf-table td.highlight-cell {
      color: #2E7D32 !important;
      font-weight: 800 !important;
    }
    .badge-kpi-pass {
      background: #7C8268 !important;
      color: #FFFFFF !important;
      font-weight: 700 !important;
      border-radius: 20px !important;
      padding: 3px 10px !important;
      font-size: 11.5px !important;
      display: inline-flex !important;
      align-items: center !important;
      gap: 4px !important;
    }

    /* ========================================================
       MỤC 2: METRIC STRIP & CHỨNG TỪ BIỂU ĐỒ SÁNG RÕ NÉT
       ======================================================== */
    .round-metric-strip {
      display: grid !important;
      grid-template-columns: repeat(4, 1fr) !important;
      gap: 16px !important;
      margin: 24px 0 !important;
    }
    @media (max-width: 900px) {
      .round-metric-strip {
        grid-template-columns: repeat(2, 1fr) !important;
      }
    }
    @media (max-width: 540px) {
      .round-metric-strip {
        grid-template-columns: 1fr !important;
      }
    }
    .metric-strip-card {
      background: #FFFFFF !important;
      border: 1.5px solid rgba(184, 165, 139, 0.45) !important;
      border-radius: 16px !important;
      padding: 18px 20px !important;
      box-shadow: 0 6px 20px rgba(44, 33, 27, 0.05) !important;
      transition: all 0.25s ease !important;
    }
    .metric-strip-card:hover {
      transform: translateY(-3px) !important;
      border-color: #B8A58B !important;
      box-shadow: 0 12px 28px rgba(44, 33, 27, 0.1) !important;
    }
    .metric-strip-card.highlight {
      border-color: #7C8268 !important;
      background: #FAF7F2 !important;
    }
    .metric-strip-lbl {
      color: #7C8268 !important;
      font-size: 11.5px !important;
      font-weight: 800 !important;
      letter-spacing: 0.06em !important;
      text-transform: uppercase !important;
      display: flex !important;
      align-items: center !important;
      gap: 6px !important;
    }
    .metric-strip-val {
      color: #2C211B !important;
      font-size: 24px !important;
      font-weight: 800 !important;
      margin: 6px 0 !important;
    }
    .metric-strip-val.text-matcha {
      color: #2E7D32 !important;
    }
    .metric-strip-sub {
      color: #5C4D44 !important;
      font-size: 12.5px !important;
      font-weight: 600 !important;
    }
    .metric-strip-sub.text-matcha {
      color: #2E7D32 !important;
    }

    .proof-showcase-box {
      background: #FAF7F2 !important;
      border: 1.5px solid rgba(184, 165, 139, 0.45) !important;
      border-radius: 18px !important;
      padding: 24px 26px !important;
      margin: 26px 0 !important;
      box-shadow: 0 8px 24px rgba(44, 33, 27, 0.05) !important;
    }
    .proof-showcase-box.matcha-theme {
      border-color: rgba(124, 130, 104, 0.45) !important;
    }
    .proof-showcase-header {
      border-bottom: 1.5px solid rgba(184, 165, 139, 0.35) !important;
      padding-bottom: 16px !important;
      margin-bottom: 22px !important;
    }
    .proof-header-badge {
      background: rgba(184, 165, 139, 0.2) !important;
      color: #2C211B !important;
      border: 1px solid rgba(184, 165, 139, 0.45) !important;
      padding: 4px 10px !important;
      border-radius: 20px !important;
      font-size: 11.5px !important;
      font-weight: 800 !important;
    }
    .proof-header-badge.matcha {
      background: rgba(124, 130, 104, 0.18) !important;
      color: #3E4330 !important;
      border-color: rgba(124, 130, 104, 0.45) !important;
    }
    .proof-header-title {
      color: #2C211B !important;
      font-family: 'Cormorant Garamond', Georgia, serif !important;
      font-size: 22px !important;
      font-weight: 700 !important;
      margin-top: 4px !important;
    }
    .proof-header-hint {
      color: #7C8268 !important;
      font-size: 13px !important;
      font-weight: 600 !important;
    }

    .chart-evidence-card {
      background: #FFFFFF !important;
      border: 1.5px solid rgba(184, 165, 139, 0.45) !important;
      border-radius: 16px !important;
      overflow: hidden !important;
      box-shadow: 0 8px 24px rgba(44, 33, 27, 0.06) !important;
      cursor: zoom-in !important;
      transition: all 0.3s ease !important;
      width: 100% !important;
    }
    .chart-evidence-card:hover {
      transform: translateY(-4px) !important;
      border-color: #B8A58B !important;
      box-shadow: 0 16px 36px rgba(44, 33, 27, 0.12) !important;
    }
    .chart-evidence-media {
      background: #FAF7F2 !important;
      border-bottom: 1.5px solid rgba(184, 165, 139, 0.3) !important;
      display: flex !important;
      align-items: center !important;
      justify-content: center !important;
      padding: 16px !important;
      min-height: 240px !important;
    }
    .chart-evidence-img {
      max-height: 520px !important;
      object-fit: contain !important;
      width: 100% !important;
      height: auto !important;
      border-radius: 6px !important;
    }
    .proof-card-zoom-badge {
      background: #2C211B !important;
      color: #F6F1E7 !important;
      font-size: 12px !important;
      font-weight: 700 !important;
      border-radius: 20px !important;
      padding: 5px 12px !important;
      box-shadow: 0 4px 12px rgba(44, 33, 27, 0.2) !important;
    }
    .chart-evidence-info {
      padding: 18px 22px !important;
      background: #FFFFFF !important;
    }
    .chart-evidence-title {
      color: #2C211B !important;
      font-family: 'Cormorant Garamond', Georgia, serif !important;
      font-size: 20px !important;
      font-weight: 700 !important;
      margin-bottom: 8px !important;
    }
    .chart-evidence-note {
      color: #4A3B32 !important;
      font-size: 13.5px !important;
      line-height: 1.6 !important;
    }

    /* ========================================================
       MỤC 3: THẺ BÀI ĐĂNG SOCIAL MEDIA SÁNG TRẮNG SANG TRỌNG
       ======================================================== */
    .social-post-card, .social-post-card.featured-horizontal {
      background: #FFFFFF !important;
      border: 1.5px solid rgba(184, 165, 139, 0.45) !important;
      border-radius: 18px !important;
      overflow: hidden !important;
      box-shadow: 0 8px 24px rgba(44, 33, 27, 0.06) !important;
      cursor: zoom-in !important;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
      display: flex !important;
      flex-direction: column !important;
    }
    .social-post-card.featured-horizontal {
      display: grid !important;
      grid-template-columns: 1.35fr 1fr !important;
      margin-bottom: 24px !important;
    }
    @media (max-width: 900px) {
      .social-post-card.featured-horizontal {
        grid-template-columns: 1fr !important;
      }
    }
    .social-post-card:hover, .social-post-card.featured-horizontal:hover {
      transform: translateY(-5px) !important;
      border-color: #B8A58B !important;
      box-shadow: 0 16px 36px rgba(44, 33, 27, 0.12) !important;
    }
    .social-post-media {
      background: #FAF7F2 !important;
      border-bottom: 1.5px solid rgba(184, 165, 139, 0.3) !important;
    }
    .social-post-card.featured-horizontal .social-post-media {
      border-bottom: none !important;
      border-right: 1.5px solid rgba(184, 165, 139, 0.3) !important;
    }
    @media (max-width: 900px) {
      .social-post-card.featured-horizontal .social-post-media {
        border-right: none !important;
        border-bottom: 1.5px solid rgba(184, 165, 139, 0.3) !important;
      }
    }
    .social-card-body {
      padding: 20px 22px !important;
      background: #FFFFFF !important;
    }
    .social-card-title {
      color: #2C211B !important;
      font-family: 'Cormorant Garamond', Georgia, serif !important;
      font-size: 20px !important;
      font-weight: 700 !important;
      margin: 6px 0 8px !important;
      line-height: 1.3 !important;
    }
    .social-card-desc {
      color: #4A3B32 !important;
      font-size: 13.5px !important;
      line-height: 1.6 !important;
      margin-bottom: 14px !important;
    }
    .stat-chip {
      background: #FAF7F2 !important;
      border: 1px solid rgba(184, 165, 139, 0.45) !important;
      color: #2C211B !important;
      font-size: 12px !important;
      font-weight: 700 !important;
      padding: 4px 10px !important;
      border-radius: 6px !important;
      display: inline-flex !important;
      align-items: center !important;
      gap: 5px !important;
    }
    .stat-chip.matcha {
      background: rgba(124, 130, 104, 0.15) !important;
      border-color: rgba(124, 130, 104, 0.45) !important;
      color: #3E4330 !important;
    }
    .stat-chip.highlight {
      background: #7C8268 !important;
      border-color: #7C8268 !important;
      color: #FFFFFF !important;
    }

    /* ========================================================
       MỤC 6: CHIẾN LƯỢC 4 KÊNH & MỤC TIÊU SỐ LIỆU TƯƠNG PHẢN CAO
       ======================================================== */
    .sec8-strategy-grid {
      display: grid !important;
      grid-template-columns: repeat(2, 1fr) !important;
      gap: 20px !important;
      margin: 20px 0 32px !important;
    }
    @media (max-width: 800px) {
      .sec8-strategy-grid {
        grid-template-columns: 1fr !important;
      }
    }
    .sec8-channel-card {
      background: #FFFFFF !important;
      border: 1.5px solid rgba(184, 165, 139, 0.45) !important;
      border-radius: 18px !important;
      padding: 22px 24px !important;
      box-shadow: 0 8px 24px rgba(44, 33, 27, 0.05) !important;
      transition: all 0.3s ease !important;
      display: flex !important;
      flex-direction: column !important;
    }
    .sec8-channel-card:hover {
      transform: translateY(-4px) !important;
      border-color: #B8A58B !important;
      box-shadow: 0 16px 36px rgba(44, 33, 27, 0.12) !important;
    }
    .sec8-card-header {
      border-bottom: 1.5px dashed rgba(184, 165, 139, 0.35) !important;
      padding-bottom: 12px !important;
      margin-bottom: 14px !important;
    }
    .sec8-card-name {
      color: #2C211B !important;
      font-family: 'Cormorant Garamond', Georgia, serif !important;
      font-size: 21px !important;
      font-weight: 700 !important;
    }
    .sec8-card-badge {
      font-size: 11px !important;
      font-weight: 800 !important;
      text-transform: uppercase !important;
      letter-spacing: 0.06em !important;
      padding: 3px 10px !important;
      border-radius: 999px !important;
    }
    .sec8-card-badge.gold {
      background: rgba(184, 165, 139, 0.2) !important;
      color: #2C211B !important;
      border: 1px solid rgba(184, 165, 139, 0.45) !important;
    }
    .sec8-card-badge.matcha {
      background: rgba(124, 130, 104, 0.18) !important;
      color: #3E4330 !important;
      border: 1px solid rgba(124, 130, 104, 0.45) !important;
    }
    .sec8-kpi-pill {
      background: #FAF7F2 !important;
      border: 1px solid rgba(184, 165, 139, 0.45) !important;
      color: #2C211B !important;
      font-size: 13px !important;
      font-weight: 600 !important;
      padding: 7px 14px !important;
      border-radius: 10px !important;
      margin-bottom: 12px !important;
    }
    .sec8-card-desc {
      color: #4A3B32 !important;
      font-size: 13.5px !important;
      line-height: 1.6 !important;
    }
    .sec8-card-desc strong {
      color: #2C211B !important;
      font-weight: 700 !important;
    }

    .sec8-targets-grid {
      display: grid !important;
      grid-template-columns: repeat(4, 1fr) !important;
      gap: 16px !important;
      margin: 20px 0 28px !important;
    }
    @media (max-width: 900px) {
      .sec8-targets-grid {
        grid-template-columns: repeat(2, 1fr) !important;
      }
    }
    @media (max-width: 480px) {
      .sec8-targets-grid {
        grid-template-columns: 1fr !important;
      }
    }
    .sec8-target-item {
      background: #FFFFFF !important;
      border: 1.5px solid rgba(184, 165, 139, 0.45) !important;
      border-radius: 16px !important;
      padding: 22px 18px !important;
      text-align: center !important;
      box-shadow: 0 6px 20px rgba(44, 33, 27, 0.05) !important;
      transition: all 0.3s ease !important;
    }
    .sec8-target-item:hover {
      transform: translateY(-4px) !important;
      border-color: #B8A58B !important;
      box-shadow: 0 14px 32px rgba(44, 33, 27, 0.12) !important;
    }
    .sec8-target-num {
      font-family: 'Cormorant Garamond', Georgia, serif !important;
      font-size: 36px !important;
      font-weight: 800 !important;
      color: #2C211B !important;
      margin-bottom: 4px !important;
      line-height: 1.1 !important;
    }
    .sec8-target-num.text-matcha {
      color: #2E7D32 !important;
    }
    .sec8-target-num.text-gold {
      color: #B8A58B !important;
    }
    .sec8-target-lbl {
      color: #7C8268 !important;
      font-size: 12px !important;
      font-weight: 800 !important;
      text-transform: uppercase !important;
      letter-spacing: 0.06em !important;
      margin-top: 4px !important;
    }
    .sec8-target-cadence {
      color: #5C4D44 !important;
      font-size: 12px !important;
      margin-top: 4px !important;
    }

    .pos-stmt-banner {
      background: #FFFFFF !important;
      border: 2px solid rgba(184, 165, 139, 0.45) !important;
      border-radius: 18px !important;
      padding: 26px 30px !important;
      box-shadow: 0 8px 24px rgba(44, 33, 27, 0.06) !important;
      margin: 28px 0 !important;
    }
    .pos-stmt-badge {
      background: rgba(124, 130, 104, 0.15) !important;
      border: 1px solid rgba(124, 130, 104, 0.4) !important;
      color: #3E4330 !important;
      font-size: 11.5px !important;
      font-weight: 800 !important;
      padding: 4px 12px !important;
      border-radius: 20px !important;
      margin-bottom: 12px !important;
    }
    .pos-stmt-lead {
      color: #4A3B32 !important;
      font-size: 15px !important;
      line-height: 1.7 !important;
    }
    .pos-stmt-tagline {
      border-top: 1px solid rgba(184, 165, 139, 0.3) !important;
      padding-top: 14px !important;
    }
    .tagline-quote {
      color: #2C211B !important;
      font-family: 'Cormorant Garamond', Georgia, serif !important;
      font-size: 22px !important;
      font-weight: 700 !important;
      font-style: italic !important;
    }
    .tagline-sub {
      color: #7C8268 !important;
      font-size: 13px !important;
      font-weight: 600 !important;
    }

    
    /* Hộp nhận xét tự động & Đánh giá thực tế */
    .auto-note-box {
      background: #FAF7F2 !important;
      border: 1.5px solid rgba(124, 130, 104, 0.45) !important;
      border-radius: 16px !important;
      padding: 18px 22px !important;
      margin: 20px 0 !important;
      color: #2C211B !important;
      font-size: 14px !important;
      line-height: 1.65 !important;
      box-shadow: 0 4px 16px rgba(44, 33, 27, 0.04) !important;
    }
    .auto-note-box strong {
      color: #2C211B !important;
      font-weight: 700 !important;
    }

    /* Subheadings trên toàn trang chuẩn màu Espresso & Serif sang trọng */
    .report-section h3,
    .section-subheading {
      color: #2C211B !important;
      font-family: 'Cormorant Garamond', Georgia, serif !important;
      font-weight: 700 !important;
    }

    /* Reflection box ở Mục 4 */
    div[style*="background:rgba(240,167,101,0.08)"],
    div[style*="background: rgba(240,167,101,0.08)"] {
      background: #FAF7F2 !important;
      border-left: 4px solid #B8A58B !important;
      border-top: 1px solid rgba(184, 165, 139, 0.35) !important;
      border-right: 1px solid rgba(184, 165, 139, 0.35) !important;
      border-bottom: 1px solid rgba(184, 165, 139, 0.35) !important;
      border-radius: 14px !important;
      padding: 18px 22px !important;
      color: #2C211B !important;
      box-shadow: 0 4px 16px rgba(44, 33, 27, 0.04) !important;
      margin: 18px 0 !important;
    }
    div[style*="background:rgba(240,167,101,0.08)"] strong,
    div[style*="background: rgba(240,167,101,0.08)"] strong {
      color: #2C211B !important;
      font-weight: 700 !important;
    }
    div[style*="background:rgba(240,167,101,0.08)"] p,
    div[style*="background: rgba(240,167,101,0.08)"] p,
    div[style*="background:rgba(240,167,101,0.08)"] div,
    div[style*="background: rgba(240,167,101,0.08)"] div {
      color: #4A3B32 !important;
      line-height: 1.65 !important;
    }

    /* Chi tiết thẻ bài đăng Mục 3 */
    .social-card-body {
      background: #FFFFFF !important;
      padding: 18px 20px !important;
    }
    .social-card-title {
      color: #2C211B !important;
      font-family: 'Cormorant Garamond', Georgia, serif !important;
      font-size: 19px !important;
      font-weight: 700 !important;
      margin-bottom: 6px !important;
    }
    .social-card-desc {
      color: #4A3B32 !important;
      font-size: 13px !important;
      line-height: 1.6 !important;
    }
    .social-post-card .badge,
    .social-post-card span[style*="border-radius:999px"],
    .social-post-card span[style*="border-radius: 999px"],
    .social-post-card span[style*="border-radius:20px"],
    .social-post-card span[style*="border-radius: 20px"] {
      background: #FAF7F2 !important;
      color: #4A3B32 !important;
      border: 1px solid rgba(184, 165, 139, 0.45) !important;
    }

    @media (max-width: 768px) {
      table.pdf-table, table.report-table, table.wrap-content-table {
        min-width: 500px !important;
      }
      table.pdf-table th, table.report-table th, table.wrap-content-table th {
        font-size: 11px !important;
        padding: 10px 8px !important;
        letter-spacing: 0.02em !important;
      }
      table.pdf-table td, table.report-table td, table.wrap-content-table td {
        font-size: 11.5px !important;
        padding: 9px 8px !important;
        line-height: 1.4 !important;
      }
      table.pdf-table td:first-child, table.report-table td:first-child {
        font-size: 11.5px !important;
        font-weight: 700 !important;
      }
    }

    
    /* Modern Channel QR Cards & Buttons */
    .live-pulse-dot {
      width: 8px !important;
      height: 8px !important;
      background: #2E7D32 !important;
      border-radius: 50% !important;
      display: inline-block !important;
      box-shadow: 0 0 0 0 rgba(46, 125, 50, 0.7) !important;
      animation: pulseBeacon 1.8s infinite !important;
    }

    .channel-qr-scan-tag {
      position: absolute !important;
      bottom: 6px !important;
      left: 50% !important;
      transform: translateX(-50%) !important;
      background: rgba(44, 33, 27, 0.88) !important;
      color: #F6F1E7 !important;
      font-size: 10.5px !important;
      font-weight: 700 !important;
      padding: 3px 8px !important;
      border-radius: 12px !important;
      white-space: nowrap !important;
      display: flex !important;
      align-items: center !important;
      gap: 4px !important;
      backdrop-filter: blur(4px) !important;
      transition: all 0.2s ease !important;
      pointer-events: none !important;
    }
    .channel-qr-img-box:hover .channel-qr-scan-tag {
      background: #2C211B !important;
      color: #FFFFFF !important;
      transform: translateX(-50%) scale(1.05) !important;
    }
    .channel-qr-img-box {
      position: relative !important;
    }

    .channel-qr-btn-group {
      display: flex !important;
      gap: 8px !important;
      width: 100% !important;
      margin-top: auto !important;
    }
    .channel-qr-btn-group .channel-qr-btn {
      flex: 1 !important;
      padding: 9px 10px !important;
      font-size: 12px !important;
    }
    .channel-qr-copy-btn {
      background: #FAF7F2 !important;
      border: 1.5px solid rgba(184, 165, 139, 0.45) !important;
      color: #4A3B32 !important;
      padding: 9px 10px !important;
      border-radius: 12px !important;
      font-size: 11.5px !important;
      font-weight: 700 !important;
      display: inline-flex !important;
      align-items: center !important;
      justify-content: center !important;
      gap: 4px !important;
      cursor: pointer !important;
      transition: all 0.2s ease !important;
      white-space: nowrap !important;
    }
    .channel-qr-copy-btn:hover {
      background: #2C211B !important;
      color: #F6F1E7 !important;
      border-color: #2C211B !important;
      transform: translateY(-2px) !important;
    }

    .channel-quick-pill {
      display: inline-flex !important;
      align-items: center !important;
      gap: 7px !important;
      padding: 8px 18px !important;
      border-radius: 30px !important;
      font-size: 13px !important;
      font-weight: 700 !important;
      text-decoration: none !important;
      background: #FFFFFF !important;
      border: 1.5px solid rgba(184, 165, 139, 0.45) !important;
      color: #2C211B !important;
      box-shadow: 0 4px 14px rgba(44, 33, 27, 0.05) !important;
      transition: all 0.25s ease !important;
    }
    .channel-quick-pill:hover {
      transform: translateY(-2px) !important;
      box-shadow: 0 8px 20px rgba(44, 33, 27, 0.1) !important;
    }
    .channel-quick-pill.fb:hover { border-color: #1877F2 !important; color: #1877F2 !important; }
    .channel-quick-pill.tiktok:hover { border-color: #000000 !important; color: #000000 !important; }
    .channel-quick-pill.ig:hover { border-color: #E1306C !important; color: #E1306C !important; }
    .channel-quick-pill.web:hover { border-color: #7C8268 !important; color: #7C8268 !important; }

    /* Toast Notification */
    .toast-notification {
      position: fixed !important;
      bottom: 28px !important;
      right: 28px !important;
      background: #2C211B !important;
      color: #F6F1E7 !important;
      padding: 12px 20px !important;
      border-radius: 30px !important;
      display: flex !important;
      align-items: center !important;
      gap: 10px !important;
      font-size: 13.5px !important;
      font-weight: 700 !important;
      box-shadow: 0 12px 32px rgba(44, 33, 27, 0.35) !important;
      border: 1.5px solid #B8A58B !important;
      z-index: 999999 !important;
      opacity: 0 !important;
      transform: translateY(20px) !important;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
      pointer-events: none !important;
    }
    .toast-notification.show {
      opacity: 1 !important;
      transform: translateY(0) !important;
      pointer-events: auto !important;
    }

    /* Section 7: Proposal Poster Luxury Frame */
    .proposal-poster-card {
      background: #FFFFFF !important;
      border: 2px solid rgba(184, 165, 139, 0.5) !important;
      border-radius: 22px !important;
      overflow: hidden !important;
      box-shadow: 0 18px 45px rgba(44, 33, 27, 0.09) !important;
      margin-bottom: 34px !important;
    }
    .proposal-poster-media {
      position: relative !important;
      background: #FAF7F2 !important;
      cursor: zoom-in !important;
      border-bottom: 1.5px solid rgba(184, 165, 139, 0.35) !important;
      padding: 20px !important;
      display: flex !important;
      justify-content: center !important;
      align-items: center !important;
    }
    .proposal-poster-img {
      width: 100% !important;
      max-width: 1040px !important;
      height: auto !important;
      display: block !important;
      border-radius: 14px !important;
      box-shadow: 0 10px 30px rgba(44, 33, 27, 0.12) !important;
      transition: transform 0.4s ease !important;
    }
    .proposal-poster-card:hover .proposal-poster-img {
      transform: scale(1.01) !important;
    }
    .proposal-poster-banner {
      padding: 22px 28px !important;
      background: #FAF6F0 !important;
      display: flex !important;
      flex-wrap: wrap !important;
      align-items: center !important;
      justify-content: space-between !important;
      gap: 16px !important;
    }
    .proposal-poster-title {
      font-family: 'Cormorant Garamond', Georgia, serif !important;
      font-size: 22px !important;
      font-weight: 700 !important;
      color: #2C211B !important;
    }
    .proposal-poster-sub {
      font-size: 14px !important;
      color: #7C8268 !important;
      font-weight: 700 !important;
    }

    /* Section 8: Final Team Members (Bảng Gia Phả) - ZERO TEXT CLAMPING */
    .org-tree-container {
      background: #FFFFFF !important;
      border: 2px solid rgba(184, 165, 139, 0.5) !important;
      border-radius: 22px !important;
      padding: 34px 24px !important;
      box-shadow: 0 16px 45px rgba(44, 33, 27, 0.08) !important;
      margin: 28px 0 !important;
      width: 100% !important;
    }
    .org-leader-card {
      background: #FFFFFF !important;
      border: 2.5px solid #B8A58B !important;
      border-radius: 18px !important;
      padding: 22px 28px !important;
      box-shadow: 0 14px 36px rgba(44, 33, 27, 0.09) !important;
      max-width: 520px !important;
      margin: 0 auto !important;
      text-align: center !important;
      position: relative !important;
      transition: all 0.3s ease !important;
      display: flex !important;
      align-items: center !important;
      gap: 18px !important;
    }
    @media (max-width: 600px) {
      .org-leader-card {
        flex-direction: column !important;
        text-align: center !important;
        padding: 20px 16px !important;
      }
    }
    .org-leader-card:hover {
      transform: translateY(-4px) !important;
      box-shadow: 0 20px 45px rgba(44, 33, 27, 0.14) !important;
    }
    .org-avatar-box {
      position: relative !important;
      width: 76px !important;
      height: 76px !important;
      flex-shrink: 0 !important;
    }
    .org-avatar-img {
      width: 76px !important;
      height: 76px !important;
      border-radius: 50% !important;
      object-fit: cover !important;
      border: 2.5px solid #B8A58B !important;
    }
    .org-crown-badge {
      position: absolute !important;
      top: -8px !important;
      right: -4px !important;
      background: #B8A58B !important;
      color: #2C211B !important;
      font-size: 16px !important;
      border-radius: 50% !important;
      width: 26px !important;
      height: 26px !important;
      display: flex !important;
      align-items: center !important;
      justify-content: center !important;
      box-shadow: 0 2px 8px rgba(0,0,0,0.15) !important;
    }
    .org-leader-info {
      text-align: left !important;
      flex-grow: 1 !important;
    }
    @media (max-width: 600px) {
      .org-leader-info {
        text-align: center !important;
      }
    }
    .org-leader-name {
      font-family: 'Cormorant Garamond', Georgia, serif !important;
      font-size: 24px !important;
      font-weight: 700 !important;
      color: #2C211B !important;
      margin-bottom: 2px !important;
    }
    .org-leader-role {
      font-size: 13.5px !important;
      color: #7C8268 !important;
      font-weight: 700 !important;
      margin-bottom: 6px !important;
    }
    .org-leader-desc {
      font-size: 12.5px !important;
      color: #5C4D44 !important;
      line-height: 1.5 !important;
      overflow: visible !important;
    }

    .org-tree-stem {
      width: 2px !important;
      height: 36px !important;
      background: #B8A58B !important;
      margin: 0 auto !important;
    }
    .org-tree-horiz-bar {
      height: 2px !important;
      background: #B8A58B !important;
      width: 80% !important;
      margin: 0 auto 30px !important;
      position: relative !important;
    }

    /* 4 Branches Grid on PC */
    .org-branches-grid {
      display: grid !important;
      grid-template-columns: repeat(4, 1fr) !important;
      gap: 16px !important;
    }
    @media (max-width: 1140px) {
      .org-branches-grid {
        grid-template-columns: repeat(2, 1fr) !important;
        gap: 16px !important;
      }
    }
    @media (max-width: 600px) {
      .org-branches-grid {
        grid-template-columns: 1fr !important;
      }
    }

    .org-branch-column {
      background: #FAF7F2 !important;
      border: 1.5px solid rgba(184, 165, 139, 0.4) !important;
      border-radius: 16px !important;
      padding: 16px 14px !important;
      display: flex !important;
      flex-direction: column !important;
      gap: 12px !important;
    }
    .org-branch-header {
      background: #FFFFFF !important;
      border: 1px solid rgba(184, 165, 139, 0.35) !important;
      padding: 10px 12px !important;
      border-radius: 12px !important;
      text-align: center !important;
      box-shadow: 0 2px 8px rgba(44, 33, 27, 0.03) !important;
    }
    .org-branch-title {
      font-family: 'Cormorant Garamond', Georgia, serif !important;
      font-size: 18px !important;
      font-weight: 700 !important;
      color: #2C211B !important;
    }
    .org-branch-badge {
      font-size: 11px !important;
      font-weight: 700 !important;
      color: #7C8268 !important;
      text-transform: uppercase !important;
      margin-top: 2px !important;
    }

    .org-member-mini-card {
      background: #FFFFFF !important;
      border: 1.2px solid rgba(184, 165, 139, 0.35) !important;
      border-radius: 12px !important;
      padding: 12px 14px !important;
      display: flex !important;
      align-items: flex-start !important;
      gap: 12px !important;
      cursor: pointer !important;
      transition: all 0.25s ease !important;
      box-shadow: 0 2px 8px rgba(44, 33, 27, 0.03) !important;
    }
    .org-member-mini-card:hover {
      transform: translateY(-2px) !important;
      border-color: #B8A58B !important;
      box-shadow: 0 8px 20px rgba(44, 33, 27, 0.08) !important;
    }
    .org-mini-avatar-box {
      width: 44px !important;
      height: 44px !important;
      flex-shrink: 0 !important;
    }
    .org-mini-avatar {
      width: 44px !important;
      height: 44px !important;
      border-radius: 50% !important;
      object-fit: cover !important;
      border: 1.5px solid #B8A58B !important;
    }
    .org-mini-info {
      flex-grow: 1 !important;
      min-width: 0 !important;
    }
    .org-mini-name {
      font-family: 'Cormorant Garamond', Georgia, serif !important;
      font-size: 17px !important;
      font-weight: 700 !important;
      color: #2C211B !important;
      line-height: 1.2 !important;
    }
    .org-mini-role {
      font-size: 11.5px !important;
      color: #7C8268 !important;
      font-weight: 700 !important;
      margin: 2px 0 4px !important;
    }
    /* NO TEXT CLAMP - NEVER TRUNCATE */
    .org-mini-desc {
      font-size: 12px !important;
      color: #5C4D44 !important;
      line-height: 1.45 !important;
      display: block !important;
      -webkit-line-clamp: unset !important;
      -webkit-box-orient: unset !important;
      overflow: visible !important;
      white-space: normal !important;
      word-wrap: break-word !important;
    }

    /* Buttons */
    .cafe-btn-primary {
      background: #2C211B !important;
      color: #F6F1E7 !important;
      border: 1.5px solid #2C211B !important;
      font-weight: 700 !important;
      box-shadow: 0 4px 14px rgba(44, 33, 27, 0.15) !important;
      transition: all 0.25s ease !important;
    }
    .cafe-btn-primary:hover {
      background: #7C8268 !important;
      border-color: #7C8268 !important;
      color: #FFFFFF !important;
      transform: translateY(-2px) !important;
      box-shadow: 0 8px 22px rgba(124, 130, 104, 0.3) !important;
    }

    /* Footer */
    footer.custom-cafe-footer {
      background: #FAF6F0 !important;
      border-top: 1.5px solid rgba(184, 165, 139, 0.4) !important;
      padding: 48px 0 36px !important;
      margin-top: 50px !important;
      color: #5C4D44 !important;
      font-size: 14px !important;
    }
    
    /* ========================================================
       ADDITIONAL PC OVERFLOW CONSTRAINTS & HIGH CONTRAST TYPOGRAPHY
       ======================================================== */
    .shell {
      max-width: 1180px !important;
      width: 100% !important;
      margin-left: auto !important;
      margin-right: auto !important;
      padding-left: 24px !important;
      padding-right: 24px !important;
      box-sizing: border-box !important;
    }

    .hero-banner-image-box {
      max-width: 960px !important;
      width: 100% !important;
      margin-left: auto !important;
      margin-right: auto !important;
      margin-top: 20px !important;
      margin-bottom: 28px !important;
      border-radius: 18px !important;
      border: 2px solid rgba(184, 165, 139, 0.45) !important;
      background: #FFFFFF !important;
      box-shadow: 0 10px 30px rgba(44, 33, 27, 0.08) !important;
      overflow: hidden !important;
      box-sizing: border-box !important;
    }
    .hero-banner-image {
      width: 100% !important;
      height: auto !important;
      display: block !important;
    }
    .hero-banner-caption {
      background: #FAF7F2 !important;
      border-top: 1.5px solid rgba(184, 165, 139, 0.35) !important;
      padding: 12px 18px !important;
      font-size: 13.5px !important;
      color: #2C211B !important;
      display: flex !important;
      justify-content: space-between !important;
      align-items: center !important;
    }
    .hero-banner-caption strong,
    .hero-banner-caption span {
      color: #2C211B !important;
    }

    .persona-container {
      width: 100% !important;
      max-width: 100% !important;
      box-sizing: border-box !important;
    }

    .channel-qr-grid {
      display: grid !important;
      grid-template-columns: repeat(4, 1fr) !important;
      gap: 20px !important;
      width: 100% !important;
      max-width: 100% !important;
      box-sizing: border-box !important;
      margin-top: 20px !important;
    }
    @media (max-width: 992px) {
      .channel-qr-grid {
        grid-template-columns: repeat(2, 1fr) !important;
      }
    }
    @media (max-width: 540px) {
      .channel-qr-grid {
        grid-template-columns: 1fr !important;
      }
    }

    /* Universal Anti-White / High Contrast Overrides */
    .auto-note-box {
      background: #FAF7F2 !important;
      border: 1.5px solid rgba(124, 130, 104, 0.45) !important;
      border-radius: 16px !important;
      padding: 18px 22px !important;
      margin: 20px 0 !important;
      color: #2C211B !important;
      font-size: 14px !important;
      line-height: 1.65 !important;
      box-shadow: 0 4px 16px rgba(44, 33, 27, 0.04) !important;
    }
    .auto-note-box strong,
    .auto-note-box b,
    .auto-note-box span {
      color: #2C211B !important;
    }

    .text-gold {
      color: #7C5A32 !important;
      text-shadow: none !important;
    }
    .text-matcha {
      color: #2E7D32 !important;
      text-shadow: none !important;
    }
    .hero-title .text-gold {
      color: #7C5A32 !important;
    }
    .hero-title .text-matcha {
      color: #2E7D32 !important;
    }

    /* Family Tree Avatar Enlargements */
    .org-avatar-box {
      width: 120px !important;
      height: 120px !important;
      flex-shrink: 0 !important;
      position: relative !important;
    }
    .org-avatar-img {
      width: 120px !important;
      height: 120px !important;
      border-radius: 50% !important;
      object-fit: cover !important;
      border: 3.5px solid #B8A58B !important;
      box-shadow: 0 8px 24px rgba(44, 33, 27, 0.18) !important;
      display: block !important;
    }
    .org-crown-badge {
      position: absolute !important;
      top: -12px !important;
      right: -8px !important;
      width: 36px !important;
      height: 36px !important;
      font-size: 20px !important;
      background: #B8A58B !important;
      color: #2C211B !important;
      border-radius: 50% !important;
      display: flex !important;
      align-items: center !important;
      justify-content: center !important;
      box-shadow: 0 4px 12px rgba(0,0,0,0.25) !important;
    }
    .org-crown-badge {
      position: absolute !important;
      top: -10px !important;
      right: -6px !important;
      width: 32px !important;
      height: 32px !important;
      font-size: 18px !important;
      background: #B8A58B !important;
      color: #2C211B !important;
      border-radius: 50% !important;
      display: flex !important;
      align-items: center !important;
      justify-content: center !important;
      box-shadow: 0 3px 10px rgba(0,0,0,0.2) !important;
    }
    .org-leader-card {
      background: #FFFFFF !important;
      border: 2.5px solid #B8A58B !important;
      border-radius: 20px !important;
      padding: 24px 32px !important;
      box-shadow: 0 16px 40px rgba(44, 33, 27, 0.09) !important;
      max-width: 580px !important;
      margin: 0 auto !important;
      text-align: left !important;
      position: relative !important;
      transition: all 0.3s ease !important;
      display: flex !important;
      align-items: center !important;
      gap: 22px !important;
      cursor: pointer !important;
    }
    .org-leader-name {
      font-family: 'Cormorant Garamond', Georgia, serif !important;
      font-size: 26px !important;
      font-weight: 700 !important;
      color: #2C211B !important;
      margin-bottom: 3px !important;
    }
    .org-leader-role {
      font-size: 14px !important;
      color: #5C4328 !important;
      font-weight: 700 !important;
      margin-bottom: 6px !important;
      text-transform: uppercase !important;
      letter-spacing: 0.05em !important;
    }
    .org-leader-desc {
      font-size: 13.5px !important;
      color: #4A3B32 !important;
      line-height: 1.5 !important;
    }

    .org-tree-stem {
      width: 3px !important;
      height: 36px !important;
      background: #B8A58B !important;
      margin: 0 auto !important;
    }
    .org-tree-branches-bar {
      height: 3px !important;
      background: #B8A58B !important;
      width: 84% !important;
      margin: 0 auto 30px !important;
      position: relative !important;
    }
    .org-tree-branches-bar::before,
    .org-tree-branches-bar::after {
      content: '' !important;
      position: absolute !important;
      top: 0 !important;
      width: 3px !important;
      height: 18px !important;
      background: #B8A58B !important;
    }
    .org-tree-branches-bar::before { left: 0 !important; }
    .org-tree-branches-bar::after { right: 0 !important; }

    .org-mini-avatar-box {
      width: 96px !important;
      height: 96px !important;
      flex-shrink: 0 !important;
    }
    .org-mini-avatar {
      width: 96px !important;
      height: 96px !important;
      border-radius: 50% !important;
      object-fit: cover !important;
      border: 3px solid #B8A58B !important;
      box-shadow: 0 6px 16px rgba(44, 33, 27, 0.14) !important;
      display: block !important;
    }
    @media (max-width: 600px) {
      .org-avatar-box, .org-avatar-img {
        width: 104px !important;
        height: 104px !important;
      }
      .org-mini-avatar-box, .org-mini-avatar {
        width: 84px !important;
        height: 84px !important;
      }
    }
    .org-member-mini-card {
      background: #FAF7F2 !important;
      border: 1.5px solid rgba(184, 165, 139, 0.45) !important;
      border-radius: 18px !important;
      padding: 16px 16px !important;
      display: flex !important;
      align-items: center !important;
      gap: 18px !important;
      margin-bottom: 14px !important;
      transition: all 0.25s ease !important;
      cursor: pointer !important;
      box-shadow: 0 4px 14px rgba(44, 33, 27, 0.04) !important;
    }
    .org-member-mini-card:hover {
      transform: translateY(-3px) !important;
      box-shadow: 0 10px 24px rgba(44, 33, 27, 0.1) !important;
      border-color: #7C8268 !important;
      background: #FFFFFF !important;
    }
    .org-mini-name {
      font-family: 'Cormorant Garamond', Georgia, serif !important;
      font-size: 19px !important;
      font-weight: 700 !important;
      color: #2C211B !important;
      line-height: 1.25 !important;
      margin-bottom: 2px !important;
    }
    .org-mini-role {
      font-size: 11px !important;
      color: #5C4328 !important;
      font-weight: 700 !important;
      text-transform: uppercase !important;
      letter-spacing: 0.05em !important;
      margin-bottom: 4px !important;
    }
    .org-mini-desc {
      font-size: 12px !important;
      color: #4A3B32 !important;
      line-height: 1.4 !important;
    }
"""

    full_css = base_css + "\n" + extra_css + "\n" + canva_palette_css

    # Helper: Extract sections from clean_source_build.py
    def get_sec(sid):
        p = rf'(<section class="report-section" id="{sid}">[\s\S]*?</section>)'
        m = re.search(p, src)
        return m.group(1) if m else ""

    def extract_inner_shell(section_html):
        s = re.sub(r'^\s*<section[^>]*>\s*<div class="shell"[^>]*>', '', section_html.strip(), flags=re.IGNORECASE)
        s = re.sub(r'</div>\s*</section>\s*$', '', s.strip(), flags=re.IGNORECASE)
        return s.strip()

    sec1_raw = get_sec('muc-1')
    sec2_raw = get_sec('muc-2')
    sec3_raw = get_sec('muc-3')
    sec4_raw = get_sec('muc-4')
    sec5_raw = get_sec('muc-5')
    sec6_raw = get_sec('muc-6')
    sec7_raw = get_sec('muc-7')
    sec8_raw = get_sec('muc-8')
    sec9_raw = get_sec('muc-9')

    # Head & Hero part (up to muc-1)
    m1 = re.search(r'<section class="report-section" id="muc-1">', src)
    html_start = src.find('html = """') + 10
    head_hero = src[html_start:m1.start()]
    head_hero = head_hero.replace('ĐH Văn Lang &bull; K28', 'ĐH Văn Lang &bull; K30')
    head_hero = head_hero.replace('ĐH Văn Lang • K28', 'ĐH Văn Lang • K30')
    head_hero = head_hero.replace('K28', 'K30')

    new_header_nav = """<nav class="header-menu-nav" aria-label="Menu điều hướng báo cáo cuối kỳ">
          <a href="#muc-1" class="menu-link active">1. Tổng Quan</a>
          <a href="#muc-2" class="menu-link">2. Kết Quả KPI</a>
          <a href="#muc-3" class="menu-link">3. Sản Phẩm Demo</a>
          <a href="#muc-4" class="menu-link">4. Phân Tích</a>
          <a href="#muc-5" class="menu-link">5. Pháp Lý</a>
          <a href="#muc-6" class="menu-link">6. Sáng Tạo &amp; Thành Viên</a>
          <a href="#muc-7" class="menu-link">7. Tổng Kết Số Liệu</a>
        </nav>"""

    drawer_html = """
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
        <a href="#muc-6" class="mobile-nav-link" onclick="toggleDrawer()"><span>6. Sáng tạo nội dung &amp; Bảng gia phả thành viên</span> <i data-lucide="chevron-right" style="width:14px;height:14px;"></i></a>
        <a href="#muc-7" class="mobile-nav-link" onclick="toggleDrawer()"><span>7. Tổng kết ảnh số liệu (Proposal Poster)</span> <i data-lucide="chevron-right" style="width:14px;height:14px;"></i></a>
      </div>
    </div>
    """


    head_hero = re.sub(r'<nav class="header-menu-nav"[^>]*>[\s\S]*?</nav>', new_header_nav.strip(), head_hero)
    head_hero = re.sub(r'<nav class="cafe-nav-menu"[^>]*>[\s\S]*?</nav>', new_header_nav.strip(), head_hero)
    head_hero = re.sub(r'<div class="mobile-nav-drawer" id="mobileDrawer">[\s\S]*?</div>(?=\s*<!--|\s*<section class="hero-section")', drawer_html.strip(), head_hero)

    # ========================================================
    # 1. SECTION 1: Tổng Quan Dự Án & Persona Đoàn Minh Trang
    # ========================================================
    s1_inner = extract_inner_shell(sec1_raw)
    s2_inner = extract_inner_shell(sec2_raw)

    s2_inner = re.sub(r'<div class="section-chapter-tag[^"]*">2\.[^<]+</div>',
                      '<div class="section-chapter-tag matcha" style="margin-bottom:12px;"><i data-lucide="sparkles" style="width:12px;height:12px;display:inline-block;vertical-align:middle;margin-right:4px;"></i>CHÂN DUNG KHÁCH HÀNG MỤC TIÊU (PERSONA)</div>',
                      s2_inner)
    s2_inner = s2_inner.replace('<h2 class="section-main-heading">2. Chân Dung Khách Hàng Mục Tiêu: Đoàn Minh Trang</h2>',
                                '<h3 class="section-main-heading" style="font-size:28px;margin-bottom:14px;color:#2C211B;">Chân Dung Khách Hàng Mục Tiêu: Đoàn Minh Trang</h3>')

    sec1_final = f"""
  <!-- ========================================================
       MỤC 1: TỔNG QUAN DỰ ÁN & CHÂN DUNG KHÁCH HÀNG (PERSONA)
       ======================================================== -->
  <section class="report-section" id="muc-1">
    <div class="shell">
      {s1_inner}
      <div class="section-divider" style="margin: 48px 0 36px; border-top: 1.5px dashed rgba(184, 165, 139, 0.4);"></div>
      {s2_inner}
    </div>
  </section>
"""

    # ========================================================
    # 2. SECTION 2: Kết Quả So Với KPI, 4 Kênh QR & Biểu Đồ 6 Tuần
    # ========================================================
    s3_inner = extract_inner_shell(sec3_raw)
    s4_inner = extract_inner_shell(sec4_raw)

    s3_inner = s3_inner.replace('<div class="section-chapter-tag">3. KPI DỰ ÁN &amp; KẾT QUẢ ĐẠT ĐƯỢC</div>',
                                '<div class="section-chapter-tag">2. KẾT QUẢ SO VỚI KPI &amp; TĂNG TRƯỞNG</div>')
    s3_inner = s3_inner.replace('<h2 class="section-main-heading">3. Mục Tiêu KPI Kế Hoạch &amp; Kết Quả Thực Tế Từng Kênh</h2>',
                                '<h2 class="section-main-heading">2. Kết Quả So Với KPI Kế Hoạch &amp; Tăng Trưởng Thực Tế</h2>')

    dark_eval_box = """<div style="background:rgba(20,15,10,0.85);border:1px solid rgba(240,167,101,0.3);border-radius:var(--radius-sm);padding:14px 20px;margin-bottom:28px;display:flex;align-items:center;gap:12px;">
        <i data-lucide="check-circle" style="width:20px;height:20px;color:var(--matcha-green);flex-shrink:0;"></i>
        <div style="font-size:13.5px;color:var(--crema);line-height:1.5;">
          <strong>Tiêu chuẩn đánh giá thực tế:</strong> Không chỉ dừng lại ở việc đếm lượt thích (like), nhóm tập trung đo lường <strong>tương tác sâu</strong> (bình luận, chia sẻ) và <strong>chuyển đổi thực tế</strong> (lượt nhấp vào Landing Page để xem menu).
        </div>
      </div>"""
    light_eval_box = """<div style="background:#FAF7F2;border:1.5px solid rgba(184,165,139,0.5);border-radius:14px;padding:16px 22px;margin-bottom:28px;display:flex;align-items:center;gap:14px;box-shadow:0 4px 16px rgba(44,33,27,0.04);">
        <i data-lucide="check-circle" style="width:22px;height:22px;color:#7C8268;flex-shrink:0;"></i>
        <div style="font-size:14px;color:#2C211B;line-height:1.6;">
          <strong style="color:#2C211B;">Tiêu chuẩn đánh giá thực tế:</strong> Không chỉ dừng lại ở việc đếm lượt thích (like), nhóm tập trung đo lường <strong style="color:#2C211B;">tương tác sâu</strong> (bình luận, chia sẻ) và <strong style="color:#2C211B;">chuyển đổi thực tế</strong> (lượt nhấp vào Landing Page để xem menu).
        </div>
      </div>"""
    s3_inner = s3_inner.replace(dark_eval_box, light_eval_box)
    s3_inner = re.sub(r'<div style="background:rgba\(20,15,10,0\.85\);border:1px solid rgba\(240,167,101,0\.3\);[\s\S]*?</div>\s*</div>', light_eval_box, s3_inner)

    # 4 Channel Cards & QR Codes
    channel_qr_html = """
      <!-- CỔNG KẾT NỐI 4 NỀN TẢNG SỐ & 4 MÃ QR CODE CHÍNH THỨC -->
      <div style="margin-top: 36px; margin-bottom: 12px;">
        <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;margin-bottom:16px;">
          <div>
            <span style="font-size:12px;font-weight:700;color:var(--matcha-green);text-transform:uppercase;letter-spacing:0.08em;display:flex;align-items:center;gap:6px;">
              <i data-lucide="qr-code" style="width:14px;height:14px;"></i> Hệ Thống Đa Nền Tảng Số Chính Thức
            </span>
            <h3 style="font-family:var(--font-serif);font-size:25px;font-weight:700;color:var(--crema);margin:4px 0 0 0;">
              Truy Cập Trực Tiếp &amp; Quét Mã QR 4 Kênh Truyền Thông
            </h3>
          </div>
          <div style="display:flex;align-items:center;gap:8px;font-size:13px;color:var(--text-muted);">
            <i data-lucide="scan" style="width:15px;height:15px;color:var(--matcha-green);"></i>
            <span>Quét bằng camera điện thoại hoặc bấm nút để mở kênh</span>
          </div>
        </div>

        <div class="channel-qr-grid">
          <!-- 1. FACEBOOK -->
          <div class="channel-qr-card fb">
            <div class="channel-qr-badge fb">
              <i data-lucide="facebook" style="width:13px;height:13px;"></i>
              <span>Facebook Fanpage</span>
            </div>
            <div class="channel-qr-img-box" onclick="openLightbox('assets/cuoi-ky/qr-facebook.png', 'Mã QR Facebook Fanpage Olion Coffee', 'Quét để truy cập trang Facebook chính thức của Olion Coffee')">
              <img src="assets/cuoi-ky/qr-facebook.png" alt="QR Facebook Olion Coffee" class="channel-qr-img" />
              <div class="channel-qr-scan-hint"><i data-lucide="maximize-2" style="width:13px;height:13px;"></i> Phóng to</div>
            </div>
            <div class="channel-qr-name">Facebook Fanpage</div>
            <div class="channel-qr-desc">
              Cổng thông tin &amp; kết nối chính thức, tương tác đạt <strong>665 lượt</strong> (110,8% KPI).
            </div>
            <a href="https://www.facebook.com/share/19kbsppy1a/?mibextid=wwXIfr" target="_blank" rel="noopener noreferrer" class="channel-qr-btn fb">
              <span>Mở Trang Facebook</span> <i data-lucide="arrow-up-right" style="width:14px;height:14px;"></i>
            </a>
          </div>

          <!-- 2. TIKTOK -->
          <div class="channel-qr-card tt">
            <div class="channel-qr-badge tt">
              <i data-lucide="video" style="width:13px;height:13px;"></i>
              <span>TikTok Channel 🏆</span>
            </div>
            <div class="channel-qr-img-box" onclick="openLightbox('assets/cuoi-ky/qr-tiktok.png', 'Mã QR TikTok Olion Coffee', 'Quét để theo dõi kênh TikTok triệu view của Olion Coffee')">
              <img src="assets/cuoi-ky/qr-tiktok.png" alt="QR TikTok Olion Coffee" class="channel-qr-img" />
              <div class="channel-qr-scan-hint"><i data-lucide="maximize-2" style="width:13px;height:13px;"></i> Phóng to</div>
            </div>
            <div class="channel-qr-name">TikTok Channel</div>
            <div class="channel-qr-desc">
              Kênh viral tiếp cận sinh viên VLU, đạt <strong>14.617 views</strong> và bứt phá 282 followers.
            </div>
            <a href="https://www.tiktok.com/@olion.coffee?_r=1&_d=e1mfaaj8dihc4d&sec_uid=MS4wLjABAAAAmR8D8Qd7n74zY2aF9kH76T0c5c4A3QGZ087B-P30C95Gg&share_author_id=7445747444356498439" target="_blank" rel="noopener noreferrer" class="channel-qr-btn tt">
              <span>Mở Kênh TikTok</span> <i data-lucide="arrow-up-right" style="width:14px;height:14px;"></i>
            </a>
          </div>

          <!-- 3. INSTAGRAM -->
          <div class="channel-qr-card ig">
            <div class="channel-qr-badge ig">
              <i data-lucide="instagram" style="width:13px;height:13px;"></i>
              <span>Instagram Art</span>
            </div>
            <div class="channel-qr-img-box" onclick="openLightbox('assets/cuoi-ky/qr-instagram.png', 'Mã QR Instagram Olion Coffee', 'Quét để xem thư viện ảnh thẩm mỹ cao trên Instagram Olion Coffee')">
              <img src="assets/cuoi-ky/qr-instagram.png" alt="QR Instagram Olion Coffee" class="channel-qr-img" />
              <div class="channel-qr-scan-hint"><i data-lucide="maximize-2" style="width:13px;height:13px;"></i> Phóng to</div>
            </div>
            <div class="channel-qr-name">Instagram Profile</div>
            <div class="channel-qr-desc">
              Không gian nghệ thuật thẩm mỹ cao, thu hút <strong>1.186 tương tác</strong> &amp; 142 followers.
            </div>
            <a href="https://www.instagram.com/olion.coffee" target="_blank" rel="noopener noreferrer" class="channel-qr-btn ig">
              <span>Mở Trang Instagram</span> <i data-lucide="arrow-up-right" style="width:14px;height:14px;"></i>
            </a>
          </div>

          <!-- 4. LANDING PAGE -->
          <div class="channel-qr-card web">
            <div class="channel-qr-badge web">
              <i data-lucide="globe" style="width:13px;height:13px;"></i>
              <span>Landing Page</span>
            </div>
            <div class="channel-qr-img-box" onclick="openLightbox('assets/cuoi-ky/qr-landingpage.png', 'Mã QR Landing Page Olion Coffee', 'Quét để trải nghiệm trang đích giới thiệu không gian & menu Olion')">
              <img src="assets/cuoi-ky/qr-landingpage.png" alt="QR Landing Page Olion Coffee" class="channel-qr-img" />
              <div class="channel-qr-scan-hint"><i data-lucide="maximize-2" style="width:13px;height:13px;"></i> Phóng to</div>
            </div>
            <div class="channel-qr-name">Landing Page Web</div>
            <div class="channel-qr-desc">
              Trang đích tích hợp menu điện tử, bùng nổ <strong>280 visits</strong> ở tuần 4 (tổng 381 visits).
            </div>
            <a href="https://www.olioncoffee.app" target="_blank" rel="noopener noreferrer" class="channel-qr-btn web">
              <span>Mở Trang Web</span> <i data-lucide="arrow-up-right" style="width:14px;height:14px;"></i>
            </a>
          </div>
        </div>
      </div>
    """

    s4_inner = re.sub(r'<div class="section-chapter-tag[^"]*">4\.[^<]+</div>',
                      '<div class="section-chapter-tag matcha" style="margin-bottom:12px;"><i data-lucide="trending-up" style="width:12px;height:12px;display:inline-block;vertical-align:middle;margin-right:4px;"></i>TĂNG TRƯỞNG QUA 6 TUẦN</div>',
                      s4_inner)
    s4_inner = s4_inner.replace('<h2 class="section-main-heading">4. Theo Dõi &amp; Đánh Giá Tăng Trưởng Qua 6 Tuần</h2>',
                                '<h3 class="section-main-heading" style="font-size:26px;color:#2C211B;margin-bottom:12px;">Theo Dõi &amp; Đánh Giá Tăng Trưởng Qua 6 Tuần</h3>')
    s4_inner = s4_inner.replace('<div class="table-container">',
                                """<div class="table-swipe-hint" style="display:none;margin-bottom:8px;font-size:12.5px;color:#7C8268;align-items:center;gap:6px;"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="13 17 18 12 13 7"></polyline><polyline points="6 17 11 12 6 7"></polyline></svg> <span>Vuốt ngang bảng để xem chi tiết 4 kênh theo từng tuần</span></div>
      <div class="table-container">""", 1)

    sec2_final = f"""
  <!-- ========================================================
       MỤC 2: KẾT QUẢ SO VỚI KPI, 4 KÊNH QR & BIỂU ĐỒ 6 TUẦN
       ======================================================== -->
  <section class="report-section" id="muc-2">
    <div class="shell">
      {s3_inner}
      {channel_qr_html}
      <div class="section-divider" style="margin: 48px 0 36px; border-top: 1.5px dashed rgba(184, 165, 139, 0.4);"></div>
      {s4_inner}
    </div>
  </section>
"""

    # ========================================================
    # 3. SECTION 3: Sản Phẩm Truyền Thông Nổi Bật & Demo Thực Tế
    # ========================================================
    s5_inner = extract_inner_shell(sec5_raw)
    s5_inner = re.sub(r'<div class="section-chapter-tag[^"]*">5\.[^<]+</div>', '<div class="section-chapter-tag matcha">3. SẢN PHẨM TRUYỀN THÔNG NỔI BẬT &amp; DEMO</div>', s5_inner)
    s5_inner = s5_inner.replace('<h2 class="section-main-heading">5. Sản Phẩm Truyền Thông Nổi Bật &amp; Minh Chứng Thực Tế</h2>',
                                '<h2 class="section-main-heading">3. Sản Phẩm Truyền Thông Nổi Bật &amp; Minh Chứng Thực Tế</h2>')
    s5_inner = s5_inner.replace('background:#000;', 'background:#FAF7F2;')

    sec3_final = f"""
  <!-- ========================================================
       MỤC 3: SẢN PHẨM TRUYỀN THÔNG NỔI BẬT & DEMO THỰC TẾ
       ======================================================== -->
  <section class="report-section" id="muc-3">
    <div class="shell">
      {s5_inner}
    </div>
  </section>
"""

    # ========================================================
    # 4. SECTION 4: Phân Tích Tổng Quan 4 Kênh & Điều Chỉnh
    # ========================================================
    s6_inner = extract_inner_shell(sec6_raw)
    s6_inner = re.sub(r'<div class="section-chapter-tag[^"]*">6\.[^<]+</div>', '<div class="section-chapter-tag matcha">4. PHÂN TÍCH TỔNG QUAN &amp; ĐIỀU CHỈNH CHIẾN LƯỢC</div>', s6_inner)
    s6_inner = s6_inner.replace('<h2 class="section-main-heading">6. Đánh Giá Tổng Quan 4 Kênh &amp; Bài Học Chiến Lược</h2>',
                                '<h2 class="section-main-heading">4. Phân Tích Tổng Quan 4 Kênh &amp; Điều Chỉnh Chiến Lược</h2>')
    light_eval_box_sec6 = """<div style="background:#FAF7F2;border:1.5px solid rgba(184,165,139,0.5);border-radius:14px;padding:16px 22px;margin-bottom:28px;display:flex;align-items:center;gap:14px;box-shadow:0 4px 16px rgba(44,33,27,0.04);">
        <i data-lucide="lightbulb" style="width:22px;height:22px;color:#7C8268;flex-shrink:0;"></i>
        <div style="font-size:14px;color:#2C211B;line-height:1.6;">
          <strong style="color:#2C211B;">Đúc kết giá trị cốt lõi:</strong> Kênh mạng xã hội phát huy tối đa vai trò tạo nhận diện (Awareness) và tương tác cảm xúc, trong khi Landing Page đóng vai trò neo giữ thông tin và điểm chạm ra quyết định (Action).
        </div>
      </div>"""
    s6_inner = re.sub(r'<div style="background:rgba\(20,15,10,0\.85\);border:1px solid rgba\(240,167,101,0\.3\);padding:14px 20px;[\s\S]*?</div>\s*</div>', light_eval_box_sec6, s6_inner)

    sec4_final = f"""
  <!-- ========================================================
       MỤC 4: PHÂN TÍCH TỔNG QUAN 4 KÊNH & ĐIỀU CHỈNH CHIẾN LƯỢC
       ======================================================== -->
  <section class="report-section" id="muc-4">
    <div class="shell">
      {s6_inner}
    </div>
  </section>
"""

    # ========================================================
    # 5. SECTION 5: Tuân Thủ Pháp Lý (12 Tiêu Chí)
    # ========================================================
    s7_inner = extract_inner_shell(sec7_raw)
    s7_inner = re.sub(r'<div class="section-chapter-tag[^"]*">7\.[^<]+</div>', '<div class="section-chapter-tag matcha">5. TUÂN THỦ PHÁP LÝ (12 TIÊU CHÍ)</div>', s7_inner)
    s7_inner = s7_inner.replace('<h2 class="section-main-heading">7. Tuân Thủ Pháp Lý &amp; Đạo Đức Truyền Thông</h2>',
                                '<h2 class="section-main-heading">5. Tuân Thủ Pháp Lý (12 Tiêu Chí) &amp; Đạo Đức Truyền Thông</h2>')

    sec5_final = f"""
  <!-- ========================================================
       MỤC 5: TUÂN THỦ PHÁP LÝ (12 TIÊU CHÍ) & ĐẠO ĐỨC TRUYỀN THÔNG
       ======================================================== -->
  <section class="report-section" id="muc-5">
    <div class="shell">
      {s7_inner}
    </div>
  </section>
"""

    # ========================================================
    # 6. SECTION 6: Sáng Tạo Nội Dung, Khởi Nghiệp & Bảng Gia Phả
    # ========================================================
    s8_inner = extract_inner_shell(sec8_raw)
    s8_inner = re.sub(r'<div class="section-chapter-tag[^"]*">8\.[^<]+</div>', '<div class="section-chapter-tag matcha">6. SÁNG TẠO NỘI DUNG, ĐỊNH HƯỚNG KHỞI NGHIỆP &amp; PHÂN VAI THÀNH VIÊN</div>', s8_inner)
    s8_inner = s8_inner.replace('<h2 class="section-main-heading">8. Định Hướng Duy Trì Kênh &amp; Mục Tiêu Phát Triển 3 Tháng Tới</h2>',
                                '<h2 class="section-main-heading">6. Sáng Tạo Nội Dung, Định Hướng Khởi Nghiệp &amp; Phân Vai Thành Viên</h2>')

    sec6_eval_pattern = r'<div style="background:rgba\(20,15,10,0\.85\);border:1px solid rgba\(240,167,101,0\.3\);border-radius:var\(--radius-sm\);padding:14px 20px;margin-bottom:28px;display:flex;align-items:center;gap:12px;">[\s\S]*?</div>\s*</div>'
    light_eval_box_sec8 = """<div style="background:#FAF7F2;border:1.5px solid rgba(184,165,139,0.5);border-radius:14px;padding:16px 22px;margin-bottom:28px;display:flex;align-items:center;gap:14px;box-shadow:0 4px 16px rgba(44,33,27,0.04);">
        <i data-lucide="compass" style="width:22px;height:22px;color:#7C8268;flex-shrink:0;"></i>
        <div style="font-size:14px;color:#2C211B;line-height:1.6;">
          <strong style="color:#2C211B;">Tầm nhìn khởi nghiệp bền vững:</strong> Chuyển hóa dự án học phần thành mô hình kinh doanh thực chiến, tận dụng tài sản số đã xây dựng để tiếp tục nuôi dưỡng tệp khách hàng trung thành tại cơ sở Gò Vấp.
        </div>
      </div>"""
    s8_inner = re.sub(sec6_eval_pattern, light_eval_box_sec8, s8_inner)

    # Process Team Members (s9_inner) into the Family Tree part of Section 6
    s9_inner = extract_inner_shell(sec9_raw)
    s9_inner = re.sub(r'<div class="section-chapter-tag[^"]*">9\.[^<]+</div>', '', s9_inner)
    s9_inner = re.sub(r'<h2 class="section-main-heading">9\.[^<]+</h2>', '', s9_inner)
    s9_inner = re.sub(r'<p style="color:var\(--text-muted\);margin-bottom:30px;font-size:15px;">[\s\S]*?</p>', '', s9_inner)

    dark_team_box = """<div style="background:rgba(20,15,10,0.85);border:1px solid rgba(240,167,101,0.3);border-radius:var(--radius-md);padding:18px 24px;margin-top:28px;text-align:center;box-shadow:var(--shadow-wood);">
          <div style="font-family:var(--font-serif);font-size:18px;color:var(--accent-gold);margin-bottom:6px;">
            🤝 Tinh Thần Đồng Đội &amp; Hợp Tác Nhóm 7 (Gỗ Xà Cừ)
          </div>
          <p style="font-size:13.5px;color:var(--crema);margin:0;line-height:1.6;max-width:860px;display:inline-block;">
            11 thành viên đã cùng nhau làm việc gắn kết như một gia đình, chủ động hỗ trợ lẫn nhau giữa các ban từ khâu ý tưởng, quay chụp, sản xuất video, đăng bài đến phân tích số liệu để hoàn thành xuất sắc chiến dịch truyền thông Olion Coffee.
          </p>
        </div>"""
    light_team_box = """<div style="background:#FAF7F2;border:1.5px solid rgba(184,165,139,0.5);border-radius:18px;padding:22px 28px;margin-top:28px;text-align:center;box-shadow:0 8px 24px rgba(44,33,27,0.04);">
          <div style="font-family:var(--font-serif);font-size:20px;font-weight:700;color:#2C211B;margin-bottom:8px;">
            🤝 Tinh Thần Đồng Đội &amp; Hợp Tác Gia Đình Gỗ Xà Cừ
          </div>
          <p style="font-size:14px;color:#5C4D44;margin:0;line-height:1.65;max-width:860px;display:inline-block;">
            11 thành viên đã cùng nhau làm việc gắn kết như một gia đình, chủ động hỗ trợ lẫn nhau giữa 4 ban từ khâu khảo sát insight, quay chụp sản phẩm, dựng clip viral, xuất bản đa kênh đến phân tích số liệu hàng tuần để hoàn thành xuất sắc chiến dịch truyền thông Olion Coffee.
          </p>
        </div>"""
    s9_inner = s9_inner.replace(dark_team_box, light_team_box)

    family_tree_header = """
      <div class="section-chapter-tag matcha" style="margin-bottom:12px;">
        <i data-lucide="users" style="width:12px;height:12px;display:inline-block;vertical-align:middle;margin-right:4px;"></i>
        BẢNG GIA PHẢ THÀNH VIÊN NHÓM 7 (GỖ XÀ CỪ)
      </div>
      <h3 class="section-main-heading" style="font-size:26px;color:#2C211B;margin-bottom:8px;">
        Phân Vai Chuyên Môn &amp; Đóng Góp 11 Thành Viên
      </h3>
      <p style="color:#5C4D44;margin-bottom:28px;font-size:15px;line-height:1.6;">
        Đội ngũ 11 thành viên được tổ chức theo sơ đồ gia phả gồm Trưởng Nhóm điều phối chung và 4 ban chuyên môn, gắn kết chặt chẽ như một gia đình trong suốt 6 tuần thực hiện chiến dịch.
      </p>
    """

    sec6_final = f"""
  <!-- ========================================================
       MỤC 6: SÁNG TẠO NỘI DUNG, ĐỊNH HƯỚNG KHỞI NGHIỆP & BẢNG GIA PHẢ THÀNH VIÊN
       ======================================================== -->
  <section class="report-section" id="muc-6">
    <div class="shell">
      {s8_inner}
      <div class="section-divider" style="margin: 48px 0 36px; border-top: 1.5px dashed rgba(184, 165, 139, 0.4);"></div>
      {family_tree_header}
      {s9_inner}
    </div>
  </section>
"""

    # ========================================================
    # 7. SECTION 7: Proposal Poster + 3 Bảng Số Liệu 6 Tuần (Phần Cuối)
    # ========================================================
    sec7_final = """
  <!-- ========================================================
       MỤC 7: TỔNG KẾT ẢNH SỐ LIỆU & PROPOSAL DỰ ÁN 6 TUẦN
       ======================================================== -->
  <section class="report-section" id="muc-7">
    <div class="shell">
      <div class="section-chapter-tag matcha">7. TỔNG KẾT ẢNH SỐ LIỆU &amp; PROPOSAL DỰ ÁN 6 TUẦN</div>
      <h2 class="section-main-heading">7. Tổng Kết Ảnh Số Liệu &amp; Proposal Dự Án 6 Tuần</h2>
      <p style="color:var(--text-muted);margin-bottom:28px;font-size:15px;line-height:1.6;">
        Bảng tổng kết Proposal Dự án Truyền thông số học kỳ 261 (GV: Jon Lâm), tổng hợp toàn bộ các chỉ số đo lường thực tế định kỳ 6 tuần trên 4 nền tảng số (Instagram, Facebook, TikTok và Landing Page), kèm mã QR tra cứu trực tiếp.
      </p>

      <!-- Proposal Poster Luxury Card with High Resolution Image -->
      <div class="proposal-poster-card">
        <div class="proposal-poster-banner">
          <div>
            <div class="proposal-poster-title">Bảng Tổng Hợp Proposal Chiến Dịch Truyền Thông Số</div>
            <div class="proposal-poster-sub">Học kỳ 261 &bull; GV: Jon Lâm &bull; Nhóm 7 — Gỗ Xà Cừ (Olion Coffee)</div>
          </div>
          <div class="poster-action-btns">
            <button type="button" class="cafe-btn-primary" onclick="openLightbox('assets/cuoi-ky/proposal-du-an-truyen-thong-so.jpg?v=proposal2026', 'Bảng Tổng Hợp Proposal Dự Án Truyền Thông Số (Học kỳ 261 • GV: Jon Lâm)')" style="padding:8px 16px;border-radius:9999px;font-size:13px;display:inline-flex;align-items:center;gap:6px;cursor:pointer;">
              <i data-lucide="maximize-2" style="width:14px;height:14px;"></i> Phóng To Toàn Màn Hình
            </button>
            <a href="assets/cuoi-ky/proposal-du-an-truyen-thong-so.jpg?v=proposal2026" download="Proposal-Olion-Coffee-Nhom-7.jpg" class="header-icon-btn" style="padding:8px 14px;border-radius:9999px;font-size:13px;text-decoration:none;display:inline-flex;align-items:center;gap:6px;background:#FAF7F2;border:1px solid rgba(184,165,139,0.4);color:#2C211B;">
              <i data-lucide="download" style="width:14px;height:14px;"></i> Tải Ảnh Gốc Nét Cao
            </a>
          </div>
        </div>

        <div class="proposal-poster-media" onclick="openLightbox('assets/cuoi-ky/proposal-du-an-truyen-thong-so.jpg?v=proposal2026', 'Bảng Tổng Hợp Proposal Dự Án Truyền Thông Số (Học kỳ 261 • GV: Jon Lâm)')">
          <img src="assets/cuoi-ky/proposal-du-an-truyen-thong-so.jpg?v=proposal2026" alt="Proposal Dự Án Truyền Thông Số Olion Coffee - Nhóm 7 Gỗ Xà Cừ" class="proposal-poster-img" loading="lazy" />
        </div>
      </div>

      <!-- Quick Access Channel Pills in Section 7 -->
      <div style="display:flex;align-items:center;justify-content:center;gap:12px;flex-wrap:wrap;margin:24px 0 32px;">
        <a href="https://www.facebook.com/share/19kbsppy1a/?mibextid=wwXIfr" target="_blank" rel="noopener noreferrer" class="channel-quick-pill fb">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="currentColor"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
          <span>Facebook Fanpage ↗</span>
        </a>
        <a href="https://www.tiktok.com/@olion.coffee?_r=1&_t=ZS-99wZ7guuZeC" target="_blank" rel="noopener noreferrer" class="channel-quick-pill tiktok">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="currentColor"><path d="M12.525.02c1.31-.02 2.61-.01 3.91-.02.08 1.53.63 3.09 1.75 4.17 1.12 1.11 2.7 1.62 4.24 1.79v4.03c-1.44-.05-2.89-.35-4.2-.97-.57-.26-1.1-.59-1.62-.93-.01 2.92.01 5.84-.02 8.75-.08 1.4-.54 2.79-1.35 3.94-1.31 1.92-3.58 3.17-5.91 3.21-1.43.08-2.86-.31-4.08-1.03-2.02-1.19-3.44-3.37-3.65-5.71-.02-.5-.03-1-.01-1.49.18-1.9 1.12-3.72 2.58-4.96 1.66-1.44 3.98-2.13 6.15-1.72.02 1.48-.04 2.96-.04 4.44-.99-.32-2.15-.23-3.02.37-.63.41-1.11 1.04-1.36 1.75-.21.51-.24 1.07-.14 1.61.24 1.64 1.82 3.02 3.5 2.87 1.12-.01 2.19-.66 2.77-1.61.19-.33.4-.67.41-1.06.1-1.79.06-3.57.07-5.36.01-4.03-.01-8.05.02-12.07z"/></svg>
          <span>TikTok Channel ↗</span>
        </a>
        <a href="https://www.instagram.com/olion.coffee?stkn=dWlxejYzeHEzNTY1" target="_blank" rel="noopener noreferrer" class="channel-quick-pill ig">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg>
          <span>Instagram Profile ↗</span>
        </a>
        <a href="https://www.olioncoffee.app/" target="_blank" rel="noopener noreferrer" class="channel-quick-pill web">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
          <span>Landing Page Web ↗</span>
        </a>
      </div>

      <!-- 3 Tables trích xuất số liệu 6 tuần chi tiết từ poster -->
      <div style="margin-top:32px;">
        <h3 style="font-family:var(--font-serif);font-size:24px;font-weight:700;color:var(--crema);margin-bottom:16px;">
          Bảng Thống Kê Số Liệu Chi Tiết 6 Tuần Từng Nền Tảng (Trích Xuất Từ Poster)
        </h3>
        
        <div class="report-two-cols" style="display:grid;grid-template-columns:repeat(auto-fit, minmax(320px, 1fr));gap:20px;margin-bottom:24px;">
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
      </div>
    </div>
  </section>
"""

    m9_end = src.find("</section>", src.find('id="muc-9"')) + 10
    raw_tail = src[m9_end:]

    py_marker = raw_tail.find('html = html.replace("__CSS__", full_css)')
    if py_marker != -1:
        html_end = raw_tail.rfind('</html>', 0, py_marker)
        if html_end != -1:
            raw_tail = raw_tail[:html_end + 7]

    raw_tail = raw_tail.replace('background:#070503;', 'background:#FAF6F0;color:#5C4D44;')
    raw_tail = raw_tail.replace('currentSectionId = "muc-7";', 'currentSectionId = "muc-7";')

    raw_tail = raw_tail.replace("color: '#FAF5EE',", "color: '#2C211B',")
    raw_tail = raw_tail.replace("color: 'rgba(255, 255, 255, 0.06)'", "color: 'rgba(184, 165, 139, 0.22)'")
    raw_tail = raw_tail.replace("color: '#A8A096',", "color: '#2C211B',")
    raw_tail = raw_tail.replace("backgroundColor: 'rgba(17, 13, 9, 0.95)',", "backgroundColor: '#2C211B',")
    raw_tail = raw_tail.replace("titleColor: '#F0A765',", "titleColor: '#F6F1E7',")
    raw_tail = raw_tail.replace("bodyColor: '#FAF5EE',", "bodyColor: '#F6F1E7',")

    toast_html_and_js = """
  <!-- Toast Notification System -->
  <div id="toastNotification" class="toast-notification">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#7C8268" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
    <span id="toastMessage">Đã sao chép liên kết thành công!</span>
  </div>

  <script>
    function copyChannelLink(url, channelName) {
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(url).then(function() {
          showToast('Đã sao chép link ' + channelName + '!');
        }).catch(function() {
          fallbackCopy(url, channelName);
        });
      } else {
        fallbackCopy(url, channelName);
      }
    }
    function fallbackCopy(url, channelName) {
      const el = document.createElement('textarea');
      el.value = url;
      el.style.position = 'fixed';
      el.style.opacity = '0';
      document.body.appendChild(el);
      el.select();
      document.execCommand('copy');
      document.body.removeChild(el);
      showToast('Đã sao chép link ' + channelName + '!');
    }
    function showToast(msg) {
      const toast = document.getElementById('toastNotification');
      const toastMsg = document.getElementById('toastMessage');
      if (toast && toastMsg) {
        toastMsg.textContent = msg;
        toast.classList.add('show');
        clearTimeout(window._toastTimer);
        window._toastTimer = setTimeout(function() {
          toast.classList.remove('show');
        }, 2600);
      }
    }
  </script>
"""
    raw_tail = raw_tail.replace("</html>", toast_html_and_js + "\\n</html>")


    # Assemble Document
    final_doc = "\n\n".join([
        head_hero.strip(),
        sec1_final.strip(),
        sec2_final.strip(),
        sec3_final.strip(),
        sec4_final.strip(),
        sec5_final.strip(),
        sec6_final.strip(),
        sec7_final.strip(),
        raw_tail.strip()
    ])

    final_doc = final_doc.replace('__CSS__', full_css)

    with open('cuoi-ky.html', 'w', encoding='utf-8') as f:
        f.write(final_doc)
    with open('bao-cao-cuoi-ky.html', 'w', encoding='utf-8') as f:
        f.write(final_doc)

    print("REBUILD SUCCESS: Generated cuoi-ky.html & bao-cao-cuoi-ky.html with 8 sections, team members at the very end!")

if __name__ == '__main__':
    run()
