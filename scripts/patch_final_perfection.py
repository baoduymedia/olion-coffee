import re
import os

with open('scripts/build_cuoi_ky_final.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update the Canva Palette CSS with comprehensive styling and dynamic effects
vivid_canva_css = """
    /* ========================================================
       CANVA BRAND COLOR PALETTE & VIVID DYNAMIC EFFECTS (OLION COFFEE)
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
      
      --accent-gold: #B8A58B !important;
      --accent-gold-light: #DDD4C7 !important;
      --accent-gold-glow: rgba(184, 165, 139, 0.35) !important;
      --border-brass: rgba(184, 165, 139, 0.45) !important;
      --border-subtle: rgba(44, 33, 27, 0.12) !important;
      
      --matcha: #7C8268 !important;
      --matcha-green: #7C8268 !important;
      --matcha-bright: #8F957B !important;
      --matcha-dark: #464C37 !important;
      --matcha-glow: rgba(124, 130, 104, 0.3) !important;
      --border-matcha: rgba(124, 130, 104, 0.4) !important;
      
      --accent-rust: #D32F2F !important;
      --accent-red: #D32F2F !important;
      
      --shadow-wood: 0 10px 30px rgba(44, 33, 27, 0.08), 0 2px 8px rgba(184, 165, 139, 0.15) !important;
      --shadow-matcha: 0 10px 30px rgba(124, 130, 104, 0.12), 0 2px 8px rgba(124, 130, 104, 0.2) !important;
    }

    body {
      background-color: #F6F1E7 !important;
      color: #2C211B !important;
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
    }

    /* Keyframes */
    @keyframes pulseBeacon {
      0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(124, 130, 104, 0.7); }
      70% { transform: scale(1.15); box-shadow: 0 0 0 8px rgba(124, 130, 104, 0); }
      100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(124, 130, 104, 0); }
    }
    @keyframes goldShimmer {
      0% { background-position: -200% 0; }
      100% { background-position: 200% 0; }
    }

    /* Reading Progress Bar with Gradient */
    .scroll-progress-line {
      background: linear-gradient(90deg, #B8A58B, #7C8268, #D32F2F) !important;
      height: 4px !important;
      box-shadow: 0 0 10px rgba(124, 130, 104, 0.5) !important;
    }

    /* Fixed Cafe Header */
    .cafe-header {
      background: rgba(246, 241, 231, 0.96) !important;
      backdrop-filter: blur(16px) !important;
      -webkit-backdrop-filter: blur(16px) !important;
      border-bottom: 1.5px solid rgba(184, 165, 139, 0.4) !important;
      box-shadow: 0 4px 20px rgba(44, 33, 27, 0.06) !important;
    }
    .header-brand-divider {
      background: rgba(184, 165, 139, 0.5) !important;
    }
    .badge-hub-title {
      color: #2C211B !important;
      font-weight: 800 !important;
    }
    .badge-hub-sub {
      color: #7C8268 !important;
      font-weight: 600 !important;
    }

    /* Header Nav Links */
    .header-menu-nav {
      display: flex !important;
      align-items: center !important;
      gap: 6px !important;
    }
    .menu-link {
      color: #5C4D44 !important;
      font-size: 13.5px !important;
      font-weight: 600 !important;
      padding: 6px 12px !important;
      border-radius: 20px !important;
      transition: all 0.2s ease !important;
      text-decoration: none !important;
    }
    .menu-link:hover, .menu-link.active {
      color: #2C211B !important;
      background: rgba(184, 165, 139, 0.22) !important;
      font-weight: 700 !important;
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

    /* Headings & Text Colors */
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
    .org-member-mini-name {
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
    }

    /* ========================================================
       HERO BANNER & 4 STAT METRICS CARDS
       ======================================================== */
    .hero-section {
      padding: 45px 0 25px !important;
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
      font-size: clamp(28px, 4.5vw, 44px) !important;
      color: #2C211B !important;
      display: block !important;
      line-height: 1.2 !important;
    }
    .hero-title-sub {
      font-family: 'Cormorant Garamond', Georgia, serif !important;
      font-size: clamp(22px, 3.5vw, 34px) !important;
      display: block !important;
      margin-top: 6px !important;
    }
    .hero-title-sub .text-matcha {
      color: #7C8268 !important;
      font-weight: 700 !important;
    }
    .hero-title-sub .text-gold {
      color: #B8A58B !important;
      font-weight: 600 !important;
    }
    .hero-lead {
      color: #4A3B32 !important;
      font-size: 16px !important;
      line-height: 1.7 !important;
      max-width: 860px !important;
      margin-top: 14px !important;
    }

    /* Slogan Callout Card */
    .hero-slogan-card {
      background: #FFFFFF !important;
      border: 2px solid rgba(184, 165, 139, 0.5) !important;
      border-radius: 18px !important;
      padding: 22px 28px !important;
      margin: 26px 0 !important;
      box-shadow: 0 10px 30px rgba(44, 33, 27, 0.07) !important;
      position: relative !important;
      overflow: hidden !important;
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
      font-size: 13.5px !important;
      display: flex !important;
      flex-wrap: wrap !important;
      justify-content: space-between !important;
      align-items: center !important;
      gap: 8px !important;
    }

    /* Hero 4 Stat Metric Cards Strip (Responsive 2x2 mobile, 4-col desktop) */
    .hero-stat-strip {
      display: grid !important;
      grid-template-columns: repeat(4, 1fr) !important;
      gap: 16px !important;
      margin: 26px 0 16px !important;
    }
    @media (max-width: 900px) {
      .hero-stat-strip {
        grid-template-columns: repeat(2, 1fr) !important;
        gap: 12px !important;
      }
    }
    @media (max-width: 480px) {
      .hero-stat-strip {
        grid-template-columns: repeat(2, 1fr) !important;
        gap: 10px !important;
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

    /* ========================================================
       SECTION 1: OVERVIEW 4 PILLARS & POSITIONING MATRIX
       ======================================================== */
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

    /* Positioning Matrix 4 Blocks */
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

    /* ========================================================
       PERSONA: ĐOÀN MINH TRANG (PRECISE 3:4 PROPORTION & LAYOUT)
       ======================================================== */
    .persona-container {
      background: #FFFFFF !important;
      border: 2px solid rgba(184, 165, 139, 0.5) !important;
      border-radius: 22px !important;
      padding: 28px !important;
      margin-top: 28px !important;
      box-shadow: 0 16px 45px rgba(44, 33, 27, 0.08) !important;
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

    /* Grid Layout: Desktop 360px left, right details. Mobile: single column full-width */
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
    .persona-photo-live-badge {
      position: absolute !important;
      top: 12px !important;
      left: 12px !important;
      background: rgba(44, 33, 27, 0.88) !important;
      color: #FFFFFF !important;
      font-size: 11px !important;
      font-weight: 700 !important;
      padding: 5px 10px !important;
      border-radius: 20px !important;
      display: inline-flex !important;
      align-items: center !important;
      gap: 5px !important;
      backdrop-filter: blur(8px) !important;
      border: 1px solid rgba(184, 165, 139, 0.4) !important;
      z-index: 2 !important;
    }
    .persona-photo-zoom-btn {
      position: absolute !important;
      top: 12px !important;
      right: 12px !important;
      background: rgba(44, 33, 27, 0.8) !important;
      color: #FFFFFF !important;
      width: 32px !important;
      height: 32px !important;
      border-radius: 50% !important;
      display: inline-flex !important;
      align-items: center !important;
      justify-content: center !important;
      backdrop-filter: blur(8px) !important;
      z-index: 2 !important;
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
    .persona-zoom-callout {
      margin-top: 8px !important;
      font-size: 11.5px !important;
      color: #8C7B70 !important;
      display: flex !important;
      align-items: center !important;
      gap: 5px !important;
      font-weight: 600 !important;
    }

    /* Details Column */
    .persona-details-col {
      display: flex !important;
      flex-direction: column !important;
      gap: 16px !important;
    }
    .persona-hero-name {
      font-family: 'Cormorant Garamond', Georgia, serif !important;
      font-size: 26px !important;
      font-weight: 700 !important;
      color: #2C211B !important;
      margin: 0 0 8px !important;
    }
    .persona-quick-chips {
      display: flex !important;
      flex-wrap: wrap !important;
      gap: 8px !important;
      margin-bottom: 6px !important;
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
      border-left: 4px solid #7C8268 !important;
      border-radius: 14px !important;
      padding: 18px 22px !important;
      box-shadow: 0 4px 14px rgba(44, 33, 27, 0.04) !important;
    }
    .persona-quote-text {
      font-family: 'Cormorant Garamond', Georgia, serif !important;
      font-size: 19px !important;
      font-weight: 700 !important;
      font-style: italic !important;
      color: #2C211B !important;
      line-height: 1.5 !important;
    }
    .persona-quote-author {
      font-size: 13px !important;
      color: #7C8268 !important;
      font-weight: 700 !important;
      margin-top: 6px !important;
    }
    .persona-traits-grid {
      display: grid !important;
      grid-template-columns: repeat(2, 1fr) !important;
      gap: 12px !important;
    }
    @media (max-width: 640px) {
      .persona-traits-grid {
        grid-template-columns: 1fr !important;
      }
    }
    .persona-trait-card {
      background: #FFFFFF !important;
      border: 1.5px solid rgba(184, 165, 139, 0.35) !important;
      border-radius: 12px !important;
      padding: 14px 16px !important;
      box-shadow: 0 4px 12px rgba(44, 33, 27, 0.03) !important;
      display: flex !important;
      align-items: flex-start !important;
      gap: 12px !important;
      transition: all 0.25s ease !important;
    }
    .persona-trait-card:hover {
      transform: translateY(-2px) !important;
      border-color: #B8A58B !important;
      box-shadow: 0 8px 20px rgba(44, 33, 27, 0.08) !important;
    }
    .trait-title {
      font-size: 14px !important;
      font-weight: 700 !important;
      color: #2C211B !important;
      margin-bottom: 4px !important;
    }
    .trait-desc {
      font-size: 13px !important;
      color: #4A3B32 !important;
      line-height: 1.5 !important;
    }

    /* ========================================================
       SECTION 2: 4 CHANNEL QR CARDS & KPI SUMMARY
       ======================================================== */
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
    .channel-qr-card:hover {
      transform: translateY(-6px) !important;
    }
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
    .channel-qr-badge.fb {
      background: rgba(24, 119, 242, 0.12) !important;
      color: #1877F2 !important;
      border: 1px solid rgba(24, 119, 242, 0.3) !important;
    }
    .channel-qr-badge.tiktok {
      background: rgba(44, 33, 27, 0.12) !important;
      color: #2C211B !important;
      border: 1px solid rgba(44, 33, 27, 0.25) !important;
    }
    .channel-qr-badge.ig {
      background: rgba(225, 48, 108, 0.12) !important;
      color: #C13584 !important;
      border: 1px solid rgba(225, 48, 108, 0.3) !important;
    }
    .channel-qr-badge.web {
      background: rgba(124, 130, 104, 0.15) !important;
      color: #464C37 !important;
      border: 1px solid rgba(124, 130, 104, 0.35) !important;
    }

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
    .channel-qr-img-box:hover {
      transform: scale(1.04) !important;
    }
    .channel-qr-img {
      width: 100% !important;
      height: 100% !important;
      object-fit: contain !important;
      display: block !important;
    }
    .channel-qr-name {
      font-family: 'Cormorant Garamond', Georgia, serif !important;
      font-size: 19px !important;
      font-weight: 700 !important;
      color: #2C211B !important;
      margin-bottom: 4px !important;
    }
    .channel-qr-handle {
      font-size: 12.5px !important;
      color: #7C8268 !important;
      font-weight: 600 !important;
      margin-bottom: 16px !important;
    }
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
    .channel-qr-btn.fb { background: #1877F2 !important; }
    .channel-qr-btn.tiktok { background: #2C211B !important; }
    .channel-qr-btn.ig { background: linear-gradient(45deg, #F58529, #DD2A7B, #8134AF) !important; }
    .channel-qr-btn.web { background: #7C8268 !important; }
    .channel-qr-btn:hover {
      transform: translateY(-2px) !important;
      filter: brightness(1.1) !important;
      color: #FFFFFF !important;
    }

    /* ========================================================
       SECTION 3: SOCIAL MEDIA POSTS & WEB DEMO
       ======================================================== */
    .social-post-card {
      background: #FFFFFF !important;
      border: 1.5px solid rgba(184, 165, 139, 0.45) !important;
      border-radius: 18px !important;
      overflow: hidden !important;
      box-shadow: 0 10px 28px rgba(44, 33, 27, 0.07) !important;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
    }
    .social-post-card:hover {
      transform: translateY(-5px) !important;
      border-color: #B8A58B !important;
      box-shadow: 0 18px 40px rgba(44, 33, 27, 0.12) !important;
    }
    .social-post-media {
      background: #FAF7F2 !important;
    }
    .social-card-body {
      background: #FFFFFF !important;
      padding: 18px !important;
    }
    .social-card-title {
      font-family: 'Cormorant Garamond', Georgia, serif !important;
      font-size: 18px !important;
      font-weight: 700 !important;
      color: #2C211B !important;
      margin-bottom: 6px !important;
    }
    .social-card-desc {
      font-size: 13.5px !important;
      color: #4A3B32 !important;
      line-height: 1.55 !important;
    }
    .stat-chip {
      background: #FAF7F2 !important;
      border: 1px solid rgba(184, 165, 139, 0.35) !important;
      color: #2C211B !important;
      font-weight: 600 !important;
      font-size: 12px !important;
      padding: 4px 10px !important;
      border-radius: 16px !important;
    }
    .social-post-card.featured-horizontal {
      background: #FFFFFF !important;
      border: 2px solid rgba(184, 165, 139, 0.5) !important;
      border-radius: 20px !important;
    }

    /* Web Demo Frame */
    .web-demo-card {
      background: #FFFFFF !important;
      border: 2px solid rgba(184, 165, 139, 0.5) !important;
      border-radius: 20px !important;
      overflow: hidden !important;
      box-shadow: 0 12px 36px rgba(44, 33, 27, 0.08) !important;
    }

    /* ========================================================
       SECTION 4: 4-CHANNEL EVALUATION TABLE & BOTTLENECK CARDS
       ======================================================== */
    .report-table-card, .table-container {
      background: #FFFFFF !important;
      border: 2px solid rgba(184, 165, 139, 0.45) !important;
      border-radius: 18px !important;
      overflow: hidden !important;
      box-shadow: 0 10px 30px rgba(44, 33, 27, 0.06) !important;
    }
    .table-scroll-wrap {
      overflow-x: auto !important;
      -webkit-overflow-scrolling: touch !important;
    }
    table.report-table, table.wrap-content-table {
      width: 100% !important;
      border-collapse: collapse !important;
      background: #FFFFFF !important;
    }
    table.report-table th, table.wrap-content-table th {
      background: #FAF7F2 !important;
      color: #2C211B !important;
      font-size: 13px !important;
      font-weight: 800 !important;
      text-transform: uppercase !important;
      letter-spacing: 0.05em !important;
      padding: 14px 16px !important;
      border-bottom: 2px solid rgba(184, 165, 139, 0.4) !important;
    }
    table.report-table td, table.wrap-content-table td {
      color: #4A3B32 !important;
      font-size: 13.5px !important;
      padding: 14px 16px !important;
      border-bottom: 1px solid rgba(184, 165, 139, 0.25) !important;
      line-height: 1.55 !important;
    }
    table.wrap-content-table td {
      white-space: normal !important;
      word-wrap: break-word !important;
    }
    table.report-table tr:hover td, table.wrap-content-table tr:hover td {
      background: #FAF9F5 !important;
    }
    table.report-table tr.table-row-highlight td {
      background: rgba(124, 130, 104, 0.08) !important;
      font-weight: 600 !important;
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
    .badge-overachieve {
      background: #D32F2F !important;
      color: #FFFFFF !important;
      font-weight: 700 !important;
      border-radius: 20px !important;
      padding: 3px 10px !important;
      font-size: 11.5px !important;
    }

    /* ========================================================
       SECTION 6: ORG TREE (BẢNG GIA PHẢ) LUXURY DESIGN
       ======================================================== */
    .org-family-tree-wrap {
      background: #FFFFFF !important;
      border: 2px solid rgba(184, 165, 139, 0.5) !important;
      border-radius: 22px !important;
      padding: 32px 24px !important;
      box-shadow: 0 16px 45px rgba(44, 33, 27, 0.08) !important;
      margin: 28px 0 !important;
    }
    .org-leader-card {
      background: #FFFFFF !important;
      border: 2.5px solid #B8A58B !important;
      border-radius: 18px !important;
      padding: 22px 28px !important;
      box-shadow: 0 14px 36px rgba(44, 33, 27, 0.09) !important;
      max-width: 480px !important;
      margin: 0 auto !important;
      text-align: center !important;
      position: relative !important;
      transition: all 0.3s ease !important;
    }
    .org-leader-card:hover {
      transform: translateY(-4px) !important;
      box-shadow: 0 20px 45px rgba(44, 33, 27, 0.14) !important;
    }
    .org-crown-badge {
      background: #B8A58B !important;
      color: #2C211B !important;
      font-weight: 800 !important;
      padding: 4px 14px !important;
      border-radius: 20px !important;
      font-size: 11.5px !important;
      display: inline-flex !important;
      align-items: center !important;
      gap: 6px !important;
      margin-bottom: 10px !important;
    }
    .org-leader-name {
      font-family: 'Cormorant Garamond', Georgia, serif !important;
      font-size: 24px !important;
      font-weight: 700 !important;
      color: #2C211B !important;
      margin-bottom: 4px !important;
    }
    .org-leader-role {
      font-size: 13.5px !important;
      color: #7C8268 !important;
      font-weight: 700 !important;
    }
    .org-tree-stem {
      background: #B8A58B !important;
    }
    .org-branch-column {
      background: #FFFFFF !important;
      border: 1.5px solid rgba(184, 165, 139, 0.4) !important;
      border-radius: 16px !important;
      padding: 18px !important;
      box-shadow: 0 8px 24px rgba(44, 33, 27, 0.06) !important;
    }
    .org-branch-header {
      background: #FAF7F2 !important;
      border-bottom: 1.5px solid rgba(184, 165, 139, 0.3) !important;
      padding: 10px 14px !important;
      border-radius: 10px !important;
      font-family: 'Cormorant Garamond', Georgia, serif !important;
      font-size: 17px !important;
      font-weight: 700 !important;
      color: #2C211B !important;
      margin-bottom: 14px !important;
    }
    .org-member-mini-card {
      background: #FAF7F2 !important;
      border: 1.2px solid rgba(184, 165, 139, 0.35) !important;
      border-radius: 12px !important;
      padding: 12px 14px !important;
      margin-bottom: 10px !important;
      transition: all 0.25s ease !important;
    }
    .org-member-mini-card:hover {
      transform: translateY(-2px) !important;
      border-color: #B8A58B !important;
      box-shadow: 0 6px 18px rgba(44, 33, 27, 0.08) !important;
      background: #FFFFFF !important;
    }
    .org-member-mini-name {
      font-family: 'Cormorant Garamond', Georgia, serif !important;
      font-size: 16.5px !important;
      font-weight: 700 !important;
      color: #2C211B !important;
    }
    .org-member-mini-role {
      font-size: 12px !important;
      color: #7C8268 !important;
      font-weight: 600 !important;
    }

    /* ========================================================
       SECTION 7: PROPOSAL POSTER LUXURY FRAME
       ======================================================== */
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
      max-width: 1020px !important;
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
"""

# Replace canva_palette_css in scripts/build_cuoi_ky_final.py
start_marker = 'canva_palette_css = """'
end_marker = 'full_css = base_css'
s_idx = content.find(start_marker)
e_idx = content.find(end_marker)

if s_idx != -1 and e_idx != -1:
    content = content[:s_idx] + f'canva_palette_css = """{vivid_canva_css}\n    """\n\n    ' + content[e_idx:]
    print("Replaced canva_palette_css successfully!")
else:
    print(f"Could not find markers: s_idx={s_idx}, e_idx={e_idx}")

# Also fix the desktop header navigation replacement
header_nav_target = r'<nav class="header-menu-nav"[^>]*>[\s\S]*?</nav>'
new_header_nav = """<nav class="header-menu-nav" aria-label="Menu điều hướng báo cáo cuối kỳ">
          <a href="#muc-1" class="menu-link active">1. Tổng Quan</a>
          <a href="#muc-2" class="menu-link">2. Kết Quả KPI</a>
          <a href="#muc-3" class="menu-link">3. Sản Phẩm Demo</a>
          <a href="#muc-4" class="menu-link">4. Phân Tích</a>
          <a href="#muc-5" class="menu-link">5. Pháp Lý</a>
          <a href="#muc-6" class="menu-link">6. Sáng Tạo &amp; Khởi Nghiệp</a>
          <a href="#muc-7" class="menu-link">7. Tổng Kết Số Liệu</a>
        </nav>"""

content = re.sub(r'head_hero = re\.sub\(r\'<nav class="cafe-nav-menu">[\s\S]*?</nav>\', nav_html\.strip\(\), head_hero\)',
                 f'head_hero = re.sub(r\'<nav class="header-menu-nav"[^>]*>[\\s\\S]*?</nav>\', \'\'\'{new_header_nav}\'\'\', head_hero)',
                 content)

with open('scripts/build_cuoi_ky_final.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated scripts/build_cuoi_ky_final.py successfully!")
