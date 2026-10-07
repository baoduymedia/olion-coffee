import re

with open('index.html', 'r') as f:
    c = f.read()

# Fix mobile floating dock position
old_css = """    @media (max-width: 767px) {
      .floating-social-dock {
        bottom: 85px;
        right: 12px;
        transform: scale(0.9);
        transform-origin: bottom right;
      }
    }"""
new_css = """    @media (max-width: 767px) {
      .floating-social-dock {
        bottom: 145px;
        right: 12px;
        transform: scale(0.9);
        transform-origin: bottom right;
      }
    }"""
c = c.replace(old_css, new_css)

# Hide reCAPTCHA badge
# Let's inject it into a global style block
if '.grecaptcha-badge' not in c:
    c = c.replace('</style>', '  .grecaptcha-badge { visibility: hidden !important; }\n  </style>', 1)

with open('index.html', 'w') as f:
    f.write(c)

