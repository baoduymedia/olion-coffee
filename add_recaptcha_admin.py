import re

with open('admin.html', 'r') as f:
    c = f.read()

recaptcha_script = """  <!-- Google reCAPTCHA v3 (For Admin Verification) -->
  <script src="https://www.google.com/recaptcha/api.js?render=6LcrCcYtAAAAAImurcyCcHkt-SY3N2qbFRcHdiMK" async defer></script>
</head>"""

c = c.replace('</head>', recaptcha_script)

with open('admin.html', 'w') as f:
    f.write(c)

