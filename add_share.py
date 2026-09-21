import re

with open('index.html', 'r') as f:
    c = f.read()

share_btn_html = """
        <button type="button" class="btn btn-ghost" onclick="shareApp()" style="padding: 8px 14px; min-height: 38px; font-size: 12.5px; border-radius: 20px;" aria-label="Chia sẻ Web">
          <i data-lucide="share-2" style="width:16px;height:16px;"></i><span class="desktop-only" style="margin-left:6px;" data-i18n="nav_share">Chia sẻ</span>
        </button>"""

c = c.replace('<button type="button" class="btn btn-ghost header-feedback-btn"', share_btn_html + '\n        <button type="button" class="btn btn-ghost header-feedback-btn"')

share_js = """
      // Web Share API
      window.shareApp = async () => {
        if (navigator.share) {
          try {
            await navigator.share({
              title: 'Olion Coffee',
              text: 'Góc nhỏ bình yên giữa lòng Gò Vấp. Khám phá menu cà phê thủ công tinh tế ngay!',
              url: window.location.href,
            });
          } catch (err) {
            console.log('User cancelled share or error:', err);
          }
        } else {
          // Fallback
          navigator.clipboard.writeText(window.location.href);
          showOlionToast('Đã sao chép link website!', 'link');
        }
      };
"""

c = c.replace('// H. SCROLL REVEAL ANIMATION', share_js + '\n      // H. SCROLL REVEAL ANIMATION')

with open('index.html', 'w') as f:
    f.write(c)
