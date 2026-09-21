import re

with open('index.html', 'r') as f:
    c = f.read()

# 1. Fix menu board image format
c = c.replace('src="assets/olion-menu-board.png"', 'src="assets/olion-menu-board.webp"')

# 2. Add scroll-margin-top to .menu-section
c = c.replace('.menu-section {\n      padding: var(--section-py) 0;', '.menu-section {\n      padding: var(--section-py) 0;\n      scroll-margin-top: 90px;')

# 3. Add @keyframes spinner
css_spinner = """
    @keyframes spinner {
      to { transform: rotate(360deg); }
    }
    .icon-spinner {
      animation: spinner 1s linear infinite;
    }
"""
c = c.replace('  </style>', css_spinner + '  </style>')

# 4. Feedback Loading State
feedback_old = """
          btnSubmitFeedback.disabled = true;
          btnSubmitFeedback.textContent = 'Đang gửi...';

          // 3. Thực thi reCAPTCHA v3 Token (nếu có cấu hình)"""
feedback_new = """
          btnSubmitFeedback.disabled = true;
          btnSubmitFeedback.innerHTML = '<i data-lucide="loader-2" class="icon-spinner" style="width:16px;height:16px;margin-right:6px;"></i> Đang gửi...';
          lucide.createIcons();

          // 3. Thực thi reCAPTCHA v3 Token (nếu có cấu hình)"""
c = c.replace(feedback_old, feedback_new)

feedback_reset_old = """
          btnSubmitFeedback.disabled = false;
          btnSubmitFeedback.textContent = 'Gửi đánh giá ngay';"""
feedback_reset_new = """
          btnSubmitFeedback.disabled = false;
          btnSubmitFeedback.textContent = 'Gửi đánh giá ngay';"""
# Already resets correctly.

# 5. Minigame Loading State
spin_old = """
            spinBtn.disabled = true;
            spinBtn.textContent = 'Đang kiểm tra...';
            const check = await canUserSpinToday(phone);
            if (!check.can_spin) {
              spinBtn.disabled = false;
              spinBtn.textContent = 'QUAY NGAY';
              showOlionToast(check.message, 'clock');
              return;
            }
            spinBtn.textContent = 'ĐANG QUAY...';
          }

          isSpinning = true;
          spinBtn.disabled = true;"""
spin_new = """
            spinBtn.disabled = true;
            spinBtn.innerHTML = '<i data-lucide="loader-2" class="icon-spinner" style="width:16px;height:16px;margin-right:6px;"></i> Đang tải...';
            lucide.createIcons();
            const check = await canUserSpinToday(phone);
            if (!check.can_spin) {
              spinBtn.disabled = false;
              spinBtn.textContent = 'QUAY NGAY';
              showOlionToast(check.message, 'clock');
              return;
            }
          }

          isSpinning = true;
          spinBtn.disabled = true;
          spinBtn.textContent = 'ĐANG QUAY...';"""
c = c.replace(spin_old, spin_new)

with open('index.html', 'w') as f:
    f.write(c)
