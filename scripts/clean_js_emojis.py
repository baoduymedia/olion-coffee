import re

with open('/Users/thanhduy/Documents/olion-coffee/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace JS toast & modal notification emojis
replacements = [
    ("showOlionToast(currentLang === 'vi' ? 'Đã đổi sang Tiếng Việt 🇻🇳' : 'Switched to English 🇬🇧', '🌐');",
     "showOlionToast(currentLang === 'vi' ? 'Đã đổi sang Tiếng Việt' : 'Switched to English', 'globe');"),
    ("showOlionToast('Vui lòng nhập đúng số điện thoại (10 số)!', '⚠️');",
     "showOlionToast('Vui lòng nhập đúng số điện thoại (10 số)!', 'alert-circle');"),
    ("showOlionToast(`Chào mừng ${name} đến với OLION COFFEE! 🎉`, '☕');",
     "showOlionToast(`Chào mừng ${name} đến với OLION COFFEE!`, 'coffee');"),
    ("tierName = 'Kim Cương 💎';", "tierName = 'Kim Cương';"),
    ("tierName = 'Hạng Vàng 👑';", "tierName = 'Hạng Vàng';"),
    ("tierName = 'Hạng Bạc ⭐';", "tierName = 'Hạng Bạc';"),
    ("tierName = 'Diamond 💎';", "tierName = 'Diamond';"),
    ("tierName = 'Gold 👑';", "tierName = 'Gold';"),
    ("tierName = 'Silver ⭐';", "tierName = 'Silver';"),
    ("🎉 ĐỦ ĐIỀU KIỆN ĐỔI LY SIGNATURE MIỄN PHÍ", "ĐỦ ĐIỀU KIỆN ĐỔI LY SIGNATURE MIỄN PHÍ"),
    ("🎉 READY FOR FREE SIGNATURE DRINK", "READY FOR FREE SIGNATURE DRINK"),
    ("showOlionToast('Vui lòng để lại vài dòng cảm nhận hoặc hình ảnh của bạn nhé!', '✍️');",
     "showOlionToast('Vui lòng để lại vài dòng cảm nhận hoặc hình ảnh của bạn nhé!', 'message-square');"),
    ("showOlionToast(check.message, '⏳');",
     "showOlionToast(check.message, 'clock');"),
    ("showOlionToast('Cảm ơn bạn đã gửi đánh giá quý báu cho Olion Coffee!', '🎉');",
     "showOlionToast('Cảm ơn bạn đã gửi đánh giá quý báu cho Olion Coffee!', 'check-circle');"),
    ("showOlionToast('Vui lòng nhập số điện thoại để nhận quà nhé!', '📱');",
     "showOlionToast('Vui lòng nhập số điện thoại để nhận quà nhé!', 'phone');"),
    ("showOlionToast('Số điện thoại không hợp lệ (tối thiểu 9-10 chữ số)!', '⚠️');",
     "showOlionToast('Số điện thoại không hợp lệ (tối thiểu 9-10 chữ số)!', 'alert-circle');"),
    ("spinBtn.textContent = 'QUAY NGAY 🎁';",
     "spinBtn.textContent = 'QUAY NGAY';"),
    ("QUAY THƯỞNG 🎁", "QUAY THƯỞNG"),
    ("showOlionToast(`Chúc mừng bạn đã nhận được ưu đãi ${prize.code}!`, '🎉');",
     "showOlionToast(`Chúc mừng bạn đã nhận được ưu đãi ${prize.code}!`, 'award');"),
    ("title: 'OLION’S FIRST WEEK 🤎'", "title: 'OLION’S FIRST WEEK'"),
    ("newsModalDate.textContent = `📅 ${article.date}`;",
     "newsModalDate.textContent = article.date;"),
    ("drawer_menu_board: '📋 Bảng Menu Tổng (Toàn Trang)'", "drawer_menu_board: 'Bảng Menu Tổng (Toàn Trang)'"),
    ("drawer_loyalty: '👑 Tra Cứu Điểm Tích Lũy'", "drawer_loyalty: 'Tra Cứu Điểm Tích Lũy'"),
    ("drawer_menu_board: '📋 Full Menu Board (Fullscreen)'", "drawer_menu_board: 'Full Menu Board (Fullscreen)'"),
    ("drawer_loyalty: '👑 Check Loyalty Points'", "drawer_loyalty: 'Check Loyalty Points'"),
    ('drawer_menu_board: "📋 Bảng Menu Tổng (Toàn Trang)"', 'drawer_menu_board: "Bảng Menu Tổng (Toàn Trang)"'),
    ('drawer_loyalty: "👑 Tra Cứu Điểm Tích Lũy"', 'drawer_loyalty: "Tra Cứu Điểm Tích Lũy"'),
    ('drawer_menu_board: "📋 Full Menu Board (Fullscreen)"', 'drawer_menu_board: "Full Menu Board (Fullscreen)"'),
    ('drawer_loyalty: "👑 Check Loyalty Points"', 'drawer_loyalty: "Check Loyalty Points"'),
]

for old, new in replacements:
    text = text.replace(old, new)

# Update showOlionToast function
old_toast = """    window.showOlionToast = function(msg, icon = '✨') {
      const toast = document.getElementById('olionToast');
      const msgEl = document.getElementById('olionToastMsg');
      const iconEl = document.getElementById('olionToastIcon');
      if (!toast || !msgEl) return;
      msgEl.textContent = msg;
      if (iconEl) iconEl.textContent = icon;"""

new_toast = """    window.showOlionToast = function(msg, icon = 'sparkles') {
      const toast = document.getElementById('olionToast');
      const msgEl = document.getElementById('olionToastMsg');
      const iconEl = document.getElementById('olionToastIcon');
      if (!toast || !msgEl) return;
      msgEl.textContent = msg;
      if (iconEl) {
        if (icon && icon.length > 2 && /^[a-z0-9-]+$/.test(icon)) {
          iconEl.innerHTML = `<i data-lucide="${icon}" style="width:18px;height:18px;"></i>`;
        } else {
          iconEl.textContent = icon;
        }
        if (window.lucide) window.lucide.createIcons();
      }"""

if old_toast in text:
    text = text.replace(old_toast, new_toast)

# Hook lucide.createIcons() into DOMContentLoaded
target_ready = "document.addEventListener('DOMContentLoaded', () => {"
if target_ready in text and "lucide.createIcons()" not in text:
    init_call = """document.addEventListener('DOMContentLoaded', () => {
      if (window.lucide) {
        window.lucide.createIcons();
      }"""
    text = text.replace(target_ready, init_call, 1)

with open('/Users/thanhduy/Documents/olion-coffee/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Cleaned JS toasts and initialized Lucide icons successfully!')
