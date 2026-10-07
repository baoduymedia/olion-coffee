import re

with open('index.html', 'r') as f:
    c = f.read()

disclaimer = """          <div style="font-size: 10px; color: var(--text-muted); margin-top: 10px; text-align: center;">
            Bảo vệ bởi reCAPTCHA. <a href="https://policies.google.com/privacy" style="color:var(--accent-gold);text-decoration:none;">Bảo mật</a> & <a href="https://policies.google.com/terms" style="color:var(--accent-gold);text-decoration:none;">Điều khoản</a> áp dụng.
          </div>"""

# 1. Add under Minigame wheel (after submit button)
c = c.replace('<button type="submit" id="wheelSubmitBtn" class="btn btn-primary" style="width: 100%; border-radius: 50px;">Gửi Lấy Mã</button>', '<button type="submit" id="wheelSubmitBtn" class="btn btn-primary" style="width: 100%; border-radius: 50px;">Gửi Lấy Mã</button>\n' + disclaimer)

# 2. Add under Feedback form (after submit button)
c = c.replace('<button type="submit" id="fbSubmitBtn" class="btn btn-primary" style="width: 100%;">Gửi Góp Ý</button>', '<button type="submit" id="fbSubmitBtn" class="btn btn-primary" style="width: 100%;">Gửi Góp Ý</button>\n' + disclaimer)

with open('index.html', 'w') as f:
    f.write(c)
