import re

with open('index.html', 'r') as f:
    c = f.read()

css_fixes = """
    /* ======== UX/UI FIXES ======== */
    .install-float-btn {
      position: fixed;
      bottom: 24px;
      right: 24px;
      z-index: 990;
      padding: 10px 20px;
      border-radius: 50px;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 4px 15px rgba(0,0,0,0.5);
      transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .install-float-btn:hover {
      transform: translateY(-3px) scale(1.03);
      box-shadow: 0 8px 25px rgba(0,0,0,0.6);
    }
    
    input, textarea {
      font-size: 16px !important;
    }
    .social-btn {
      width: 44px !important;
      height: 44px !important;
    }
    .menu-tab {
      padding: 12px 24px !important;
    }
    
    @media (max-width: 767px) {
      .install-float-btn {
        bottom: 85px;
        right: 12px;
        padding: 8px 16px;
        font-size: 13px;
      }
      .hero-title {
        font-size: clamp(2.2rem, 10vw, 3rem) !important;
        line-height: 1.1;
      }
    }
"""

c = c.replace('</style>', css_fixes + '\n</style>')

with open('index.html', 'w') as f:
    f.write(c)
