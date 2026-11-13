import re

with open('scripts/build_cuoi_ky_final.py', 'r', encoding='utf-8') as f:
    text = f.read()

vivid_effects_css = """
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
      --bg-glass: rgba(255, 255, 255, 0.95) !important;
      
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
      font-family: 'Plus Jakarta Sans', -apple-system, sans-serif !important;
    }

    /* ========================================================
       KEYFRAME ANIMATIONS FOR DYNAMIC & VIVID EFFECTS
       ======================================================== */
    @keyframes goldShimmer {
      0% { background-position: -200% 0; }
      100% { background-position: 200% 0; }
    }

    @keyframes pulseBeacon {
      0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(124, 130, 104, 0.7); }
      70% { transform: scale(1.15); box-shadow: 0 0 0 8px rgba(124, 130, 104, 0); }
      100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(124, 130, 104, 0); }
    }

    @keyframes floatCard {
      0%, 100% { transform: translateY(0); }
      50% { transform: translateY(-4px); }
    }

    @keyframes gentleGlow {
      0%, 100% { opacity: 0.8; }
      50% { opacity: 1; }
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
    .cafe-nav-link {
      color: #2C211B !important;
      font-weight: 600 !important;
      padding: 6px 14px !important;
      border-radius: 20px !important;
      transition: all 0.25s ease !important;
    }
    .cafe-nav-link:hover {
      color: #7C8268 !important;
      background: rgba(124, 130, 104, 0.08) !important;
    }
    .cafe-nav-link.active {
      color: #FFFFFF !important;
      background: #7C8268 !important;
      box-shadow: 0 4px 12px rgba(124, 130, 104, 0.3) !important;
    }
    .cafe-nav-link.active::after {
      display: none !important;
    }
    .header-icon-btn {
      background: rgba(184, 165, 139, 0.15) !important;
      border-color: rgba(184, 165, 139, 0.4) !important;
      color: #2C211B !important;
      transition: all 0.25s ease !important;
    }
    .header-icon-btn:hover {
      background: #B8A58B !important;
      color: #FFFFFF !important;
      transform: translateY(-2px) !important;
      box-shadow: 0 6px 16px rgba(184, 165, 139, 0.35) !important;
    }
    .header-icon-btn.home-btn {
      background: #7C8268 !important;
      border-color: #7C8268 !important;
      color: #FFFFFF !important;
    }
    .header-icon-btn.home-btn:hover {
      background: #464C37 !important;
    }

    /* Mobile Drawer */
    .mobile-nav-drawer {
      background: #F6F1E7 !important;
      border-left: 1.5px solid rgba(184, 165, 139, 0.4) !important;
      box-shadow: -8px 0 30px rgba(44, 33, 27, 0.1) !important;
    }
    .mobile-nav-link {
      color: #2C211B !important;
      border-bottom: 1px solid rgba(184, 165, 139, 0.25) !important;
      font-weight: 600 !important;
    }
    .mobile-nav-link:hover, .mobile-nav-link.active {
      color: #7C8268 !important;
      background: rgba(124, 130, 104, 0.12) !important;
    }

    /* ========================================================
       HERO SECTION: VIVID AURA & ANIMATED GLOW
       ======================================================== */
    .hero-report-section {
      background: radial-gradient(ellipse at 50% -10%, rgba(184, 165, 139, 0.28) 0%, rgba(246, 241, 231, 0.85) 60%, #F6F1E7 100%) !important;
      position: relative !important;
      overflow: hidden !important;
    }
    .hero-badge-tag {
      background: rgba(124, 130, 104, 0.14) !important;
      color: #464C37 !important;
      border: 1.5px solid rgba(124, 130, 104, 0.4) !important;
      box-shadow: 0 2px 8px rgba(124, 130, 104, 0.15) !important;
    }
    .hero-report-title, .hero-title, .hero-title-main {
      color: #2C211B !important;
      font-family: 'Cormorant Garamond', Georgia, serif !important;
      letter-spacing: -0.02em !important;
      text-shadow: 0 1px 2px rgba(44, 33, 27, 0.05) !important;
    }
    .hero-report-subtitle {
      color: #7C8268 !important;
      font-family: 'Cormorant Garamond', Georgia, serif !important;
      font-weight: 700 !important;
      letter-spacing: -0.01em !important;
    }
    .hero-lead-text {
      color: #4A3B32 !important;
      font-size: 16px !important;
      line-height: 1.7 !important;
    }

    /* Slogan Ribbon with Golden Light Shimmer */
    .hero-slogan-ribbon {
      background: linear-gradient(90deg, rgba(184, 165, 139, 0.15) 0%, rgba(184, 165, 139, 0.35) 50%, rgba(184, 165, 139, 0.15) 100%) !important;
      background-size: 200% 100% !important;
      animation: goldShimmer 5s infinite ease-in-out !important;
      border: 1.5px solid rgba(184, 165, 139, 0.5) !important;
      box-shadow: 0 6px 20px rgba(44, 33, 27, 0.06) !important;
      border-radius: 14px !important;
    }
    .hero-slogan-tag {
      color: #7C8268 !important;
      font-weight: 800 !important;
    }
    .hero-slogan-quote {
      color: #2C211B !important;
      font-family: 'Cormorant Garamond', Georgia, serif !important;
      font-weight: 700 !important;
      font-size: 19px !important;
    }
    .hero-slogan-trans {
      color: #5C4D44 !important;
      font-style: italic !important;
    }

    /* Hero Banner Card */
    .hero-banner-card {
      border: 2px solid rgba(184, 165, 139, 0.45) !important;
      border-radius: 20px !important;
      box-shadow: 0 16px 40px rgba(44, 33, 27, 0.08), 0 2px 8px rgba(184, 165, 139, 0.15) !important;
      transition: all 0.35s ease !important;
    }
    .hero-banner-card:hover {
      transform: translateY(-4px) !important;
      border-color: #B8A58B !important;
      box-shadow: 0 24px 50px rgba(44, 33, 27, 0.12), 0 0 0 2px rgba(184, 165, 139, 0.5) !important;
    }
    .hero-banner-image {
      transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1) !important;
    }
    .hero-banner-card:hover .hero-banner-image {
      transform: scale(1.03) !important;
    }
    .hero-banner-caption {
      background: rgba(246, 241, 231, 0.98) !important;
      color: #2C211B !important;
      border-top: 1.5px solid rgba(184, 165, 139, 0.35) !important;
    }
    .hero-banner-caption strong {
      color: #2C211B !important;
    }

    /* 4 Hero Metric Cards with Floating Hover Effect */
    .hero-stat-item {
      background: #FFFFFF !important;
      border: 1.5px solid rgba(184, 165, 139, 0.4) !important;
      border-radius: 18px !important;
      box-shadow: 0 8px 24px rgba(44, 33, 27, 0.05) !important;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
      position: relative !important;
      overflow: hidden !important;
    }
    .hero-stat-item:hover {
      transform: translateY(-6px) !important;
      border-color: #B8A58B !important;
      box-shadow: 0 16px 36px rgba(44, 33, 27, 0.1), 0 0 0 1.5px rgba(184, 165, 139, 0.5) !important;
    }
    .hero-stat-item.matcha-card {
      border-color: rgba(124, 130, 104, 0.45) !important;
      background: linear-gradient(145deg, #FFFFFF, #FAF9F5) !important;
    }
    .hero-stat-item.matcha-card:hover {
      border-color: #7C8268 !important;
      box-shadow: 0 16px 36px rgba(124, 130, 104, 0.15), 0 0 0 1.5px rgba(124, 130, 104, 0.5) !important;
    }
    .hero-stat-num.text-gold {
      color: #B8A58B !important;
      font-weight: 800 !important;
    }
    .hero-stat-num.text-matcha {
      color: #7C8268 !important;
      font-weight: 800 !important;
    }
    .hero-stat-lbl {
      color: #2C211B !important;
      font-weight: 700 !important;
    }
    .hero-stat-sub {
      color: #6E5D53 !important;
    }

    /* ========================================================
       GLOBAL HEADINGS & TEXT CONTRAST (ABSOLUTELY NO WHITE TEXT ON LIGHT BACKGROUND)
       ======================================================== */
    h1, h2, h3, h4, h5, h6,
    .section-main-heading,
    .overview-card-value,
    .overview-card-title,
    .persona-quote-text,
    .persona-photo-name,
    .drink-title,
    .action-card h4,
    .feed-brand-name,
    .vong2-stat-val,
    .gov-card-title,
    .gov-metric-target,
    .playbook-text strong,
    .round-card-num,
    .round-card-title,
    .round-hero-stat-box .val,
    .sim-limit-title,
    .stepper-title,
    .metric-strip-val,
    .kpi-summary-card .metric-counts strong,
    .matrix-change-title,
    .matrix-val,
    .exact-matrix-table td.col-vong,
    .exact-matrix-table td.col-thaydoi,
    .exact-matrix-table td.col-num,
    .exact-matrix-table td.col-ketluan strong,
    .org-leader-name,
    .org-node-name,
    .channel-qr-title,
    .proposal-poster-title {
      color: #2C211B !important;
    }

    p, li, td, span, div {
      color: inherit;
    }
    p, li {
      color: #4A3B32;
    }
    strong, b {
      color: #2C211B;
      font-weight: 700;
    }

    /* Section Headings */
    .section-chapter-tag {
      background: rgba(124, 130, 104, 0.12) !important;
      color: #464C37 !important;
      border: 1.5px solid rgba(124, 130, 104, 0.4) !important;
      font-weight: 700 !important;
      letter-spacing: 0.08em !important;
      border-radius: 20px !important;
      padding: 5px 14px !important;
    }
    .section-chapter-tag.matcha {
      background: rgba(124, 130, 104, 0.16) !important;
      color: #3E4330 !important;
      border-color: rgba(124, 130, 104, 0.5) !important;
    }
    .section-main-heading {
      color: #2C211B !important;
      font-family: 'Cormorant Garamond', Georgia, serif !important;
      font-weight: 700 !important;
      letter-spacing: -0.015em !important;
    }
    .report-section {
      border-top: 1.5px solid rgba(184, 165, 139, 0.35) !important;
    }

    /* ========================================================
       CARDS & SURFACES: VIVID ELEVATION & BORDER GLOW
       ======================================================== */
    .overview-card-item,
    .proof-card,
    .strategy-card,
    .kpi-card,
    .org-node-box,
    .channel-qr-card,
    .legal-card,
    .proposal-poster-card,
    .report-table-card {
      background: #FFFFFF !important;
      border: 1.5px solid rgba(184, 165, 139, 0.4) !important;
      border-radius: 18px !important;
      box-shadow: 0 8px 24px rgba(44, 33, 27, 0.06), 0 1px 3px rgba(44, 33, 27, 0.04) !important;
      color: #2C211B !important;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
    }
    .overview-card-item:hover,
    .proof-card:hover,
    .channel-qr-card:hover,
    .strategy-card:hover {
      transform: translateY(-5px) !important;
      border-color: #B8A58B !important;
      box-shadow: 0 16px 38px rgba(44, 33, 27, 0.1), 0 0 0 1.5px rgba(184, 165, 139, 0.5) !important;
    }

    /* Overview Pillar Cards in Sec 1 */
    .overview-card-label {
      color: #7C8268 !important;
      font-weight: 700 !important;
    }
    .overview-card-value {
      color: #2C211B !important;
      font-weight: 800 !important;
      font-size: 18px !important;
    }
    .overview-card-desc {
      color: #5C4D44 !important;
      line-height: 1.55 !important;
    }

    /* Persona Card Redesign */
    .persona-container {
      background: linear-gradient(145deg, #FFFFFF 0%, #FAF7F2 100%) !important;
      border: 2px solid rgba(184, 165, 139, 0.5) !important;
      border-radius: 22px !important;
      box-shadow: 0 16px 40px rgba(44, 33, 27, 0.08), 0 2px 6px rgba(184, 165, 139, 0.15) !important;
    }
    .persona-dossier-tag {
      background: rgba(184, 165, 139, 0.18) !important;
      color: #2C211B !important;
      border: 1px solid rgba(184, 165, 139, 0.45) !important;
    }
    .live-status-pill {
      background: rgba(124, 130, 104, 0.15) !important;
      color: #3E4330 !important;
      border: 1px solid rgba(124, 130, 104, 0.45) !important;
    }
    .pulsing-green-dot {
      background: #7C8268 !important;
      animation: pulseBeacon 1.8s infinite !important;
    }
    .persona-photo-col {
      border: 2px solid rgba(184, 165, 139, 0.5) !important;
      border-radius: 16px !important;
      overflow: hidden !important;
      box-shadow: 0 10px 28px rgba(44, 33, 27, 0.1) !important;
    }
    .persona-photo-plate {
      background: #FAF7F2 !important;
      border-top: 1.5px solid rgba(184, 165, 139, 0.35) !important;
    }
    .persona-photo-name {
      color: #2C211B !important;
      font-weight: 800 !important;
    }
    .persona-photo-role {
      color: #7C8268 !important;
      font-weight: 600 !important;
    }
    .persona-quote-box {
      background: #FFFFFF !important;
      border-left: 4px solid #7C8268 !important;
      border: 1px solid rgba(184, 165, 139, 0.35);
      border-left: 4px solid #7C8268 !important;
      border-radius: 12px !important;
      padding: 16px 20px !important;
      box-shadow: 0 4px 14px rgba(44, 33, 27, 0.04) !important;
    }
    .persona-quote-text {
      color: #2C211B !important;
      font-family: 'Cormorant Garamond', Georgia, serif !important;
      font-weight: 700 !important;
      font-size: 19px !important;
      line-height: 1.5 !important;
    }
    .persona-bio-row {
      border-bottom: 1px solid rgba(184, 165, 139, 0.2) !important;
      color: #4A3B32 !important;
    }
    .persona-bio-label {
      color: #7C8268 !important;
      font-weight: 700 !important;
    }
    .persona-bio-val {
      color: #2C211B !important;
    }

    /* ========================================================
       CHANNEL QR & DIRECT LINKS GRID (VIVID PLATFORM GLOW)
       ======================================================== */
    .channel-qr-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 22px;
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
      background: #FFFFFF !important;
      border: 2px solid rgba(184, 165, 139, 0.45) !important;
      border-radius: 20px !important;
      padding: 24px 20px 22px !important;
      display: flex !important;
      flex-direction: column !important;
      align-items: center !important;
      text-align: center !important;
      position: relative !important;
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
      border-color: #B8A58B !important;
      box-shadow: 0 8px 24px rgba(44, 33, 27, 0.12) !important;
    }
    .channel-qr-img {
      width: 100% !important;
      height: 100% !important;
      object-fit: contain !important;
      display: block !important;
    }
    .channel-qr-title {
      font-family: 'Cormorant Garamond', Georgia, serif !important;
      font-size: 20px !important;
      font-weight: 700 !important;
      color: #2C211B !important;
      margin-bottom: 4px !important;
    }
    .channel-qr-desc {
      font-size: 13px !important;
      line-height: 1.5 !important;
      color: #5C4D44 !important;
      margin-bottom: 16px !important;
      flex-grow: 1 !important;
    }
    .channel-qr-btn {
      width: 100% !important;
      padding: 10px 16px !important;
      border-radius: 9999px !important;
      font-size: 13px !important;
      font-weight: 700 !important;
      display: inline-flex !important;
      align-items: center !important;
      justify-content: center !important;
      gap: 7px !important;
      text-decoration: none !important;
      transition: all 0.25s ease !important;
      box-shadow: 0 4px 12px rgba(44, 33, 27, 0.08) !important;
    }
    .channel-qr-btn.fb {
      background: #1877F2 !important;
      color: #FFFFFF !important;
    }
    .channel-qr-btn.tiktok {
      background: #2C211B !important;
      color: #FFFFFF !important;
    }
    .channel-qr-btn.ig {
      background: linear-gradient(135deg, #833AB4, #FD1D1D, #FCAF45) !important;
      color: #FFFFFF !important;
    }
    .channel-qr-btn.web {
      background: #7C8268 !important;
      color: #FFFFFF !important;
    }
    .channel-qr-btn:hover {
      transform: translateY(-2px) !important;
      box-shadow: 0 8px 20px rgba(44, 33, 27, 0.15) !important;
      opacity: 0.95 !important;
    }

    /* ========================================================
       TABLES: HIGH CONTRAST & CLEAR READABILITY
       ======================================================== */
    .report-table thead th {
      background: #EFE8DD !important;
      color: #2C211B !important;
      border-bottom: 2px solid #B8A58B !important;
      font-weight: 800 !important;
      font-size: 13.5px !important;
      letter-spacing: 0.02em !important;
    }
    .report-table tbody tr {
      background: #FFFFFF !important;
      border-bottom: 1px solid rgba(184, 165, 139, 0.25) !important;
    }
    .report-table tbody tr:nth-child(even) {
      background: #FAF7F2 !important;
    }
    .report-table tbody tr:hover {
      background: rgba(184, 165, 139, 0.12) !important;
    }
    .report-table td {
      color: #2C211B !important;
      font-size: 13.5px !important;
    }
    .table-row-highlight {
      background: rgba(124, 130, 104, 0.12) !important;
    }
    .badge-kpi-pass {
      background: rgba(124, 130, 104, 0.18) !important;
      color: #3E4330 !important;
      border: 1px solid #7C8268 !important;
      font-weight: 700 !important;
      border-radius: 12px !important;
    }
    .badge-kpi-red {
      background: rgba(211, 47, 47, 0.12) !important;
      color: #B71C1C !important;
      border: 1px solid rgba(211, 47, 47, 0.35) !important;
      font-weight: 700 !important;
      border-radius: 12px !important;
    }

    /* ========================================================
       SECTION 6: ORG TREE (BẢNG GIA PHẢ) LUXURY POLISH
       ======================================================== */
    .org-node-box {
      background: #FFFFFF !important;
      border: 1.5px solid rgba(184, 165, 139, 0.45) !important;
      box-shadow: 0 6px 18px rgba(44, 33, 27, 0.05) !important;
    }
    .org-node-leader {
      background: linear-gradient(135deg, #FFFFFF, #FAF7F2) !important;
      border: 2px solid #B8A58B !important;
      box-shadow: 0 12px 30px rgba(184, 165, 139, 0.25) !important;
    }
    .org-node-name {
      color: #2C211B !important;
      font-weight: 800 !important;
    }
    .org-node-role {
      color: #7C8268 !important;
      font-weight: 700 !important;
    }
    .org-dept-header {
      background: #EFE8DD !important;
      color: #2C211B !important;
      border-bottom: 1.5px solid rgba(184, 165, 139, 0.4) !important;
      font-weight: 800 !important;
    }
    .org-member-chip {
      background: #FFFFFF !important;
      border: 1.5px solid rgba(184, 165, 139, 0.35) !important;
      color: #2C211B !important;
      box-shadow: 0 3px 10px rgba(44, 33, 27, 0.04) !important;
      transition: all 0.25s ease !important;
    }
    .org-member-chip:hover {
      border-color: #7C8268 !important;
      transform: translateY(-2px) !important;
      box-shadow: 0 8px 20px rgba(124, 130, 104, 0.15) !important;
      background: #FAF9F5 !important;
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

# Replace the canva_palette_css in build_cuoi_ky_final.py
start = text.find('canva_palette_css = """')
end = text.find('"""', start + 25)

new_text = text[:start] + 'canva_palette_css = """' + vivid_effects_css + '"""' + text[end+3:]

with open('scripts/build_cuoi_ky_final.py', 'w', encoding='utf-8') as f:
    f.write(new_text)

print('Updated scripts/build_cuoi_ky_final.py with vivid effects and contrast fixes!')
