with open('/Users/thanhduy/Documents/olion-coffee/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Reviews avatar icons
text = text.replace('<div class="review-avatar">🐻</div>', '<div class="review-avatar"><i data-lucide="user" style="width:20px;height:20px;"></i></div>')
text = text.replace('<div class="review-avatar">🌿</div>', '<div class="review-avatar"><i data-lucide="user-check" style="width:20px;height:20px;"></i></div>')
text = text.replace('<div class="review-avatar">☕</div>', '<div class="review-avatar"><i data-lucide="smile" style="width:20px;height:20px;"></i></div>')
text = text.replace("const avatarIcons = ['☕', '🌿', '🐻', '✨', '🌸', '💫'];", "const avatarIcons = ['user', 'user-check', 'smile', 'award', 'heart'];")

# 2. Minigame wheels and celebrations
text = text.replace('<span>🎡</span>', '<i data-lucide="disc" style="width:16px;height:16px;"></i>')
text = text.replace('<div style="font-size: 32px; margin-bottom: 4px;">🎉</div>', '<div style="margin-bottom: 8px; color: var(--accent-gold);"><i data-lucide="gift" style="width:36px;height:36px;"></i></div>')
text = text.replace('<div style="font-size: 40px; margin-bottom: 10px;">🎉</div>', '<div style="margin-bottom: 12px; color: var(--accent-gold);"><i data-lucide="check-circle" style="width:44px;height:44px;"></i></div>')

# 3. News modal and addresses
text = text.replace('<span class="news-date" id="newsModalDate">📅 19/09/2026</span>', '<span class="news-date" id="newsModalDate"><i data-lucide="calendar" style="width:12px;height:12px;margin-right:4px;"></i>19/09/2026</span>')
text = text.replace('OLION’S FIRST WEEK 🤎', 'OLION’S FIRST WEEK')
text = text.replace('<div style="font-weight: 700; font-size: 16px; margin-bottom: 12px;">📸 Album Kỷ Niệm Tuần Đầu Tiên (Trọn bộ 5 ảnh)</div>',
                    '<div style="font-weight: 700; font-size: 16px; margin-bottom: 12px; display:flex; align-items:center; gap:8px;"><i data-lucide="camera" style="width:18px;height:18px;color:var(--accent-gold);"></i> Album Kỷ Niệm Tuần Đầu Tiên (Trọn bộ 5 ảnh)</div>')
text = text.replace('<strong>📍 Địa chỉ quán:</strong>', '<strong><i data-lucide="map-pin" style="width:14px;height:14px;margin-right:4px;vertical-align:middle;"></i>Địa chỉ quán:</strong>')
text = text.replace('<strong>⏰ Giờ mở cửa:</strong>', '<strong><i data-lucide="clock" style="width:14px;height:14px;margin-right:4px;vertical-align:middle;"></i>Giờ mở cửa:</strong>')

# 4. Preview remove image button
text = text.replace('style="position: absolute; top: -6px; right: -6px; width: 22px; height: 22px; border-radius: 50%; background: #E74C3C; color: #fff; border: 2px solid #141D16; cursor: pointer; display: flex; align-items: center; justify-content: center; font-size: 12px;">✕</button>',
                    'style="position: absolute; top: -6px; right: -6px; width: 22px; height: 22px; border-radius: 50%; background: #E74C3C; color: #fff; border: 2px solid #141D16; cursor: pointer; display: flex; align-items: center; justify-content: center; font-size: 12px;"><i data-lucide="x" style="width:12px;height:12px;"></i></button>')

# 5. Rating stars in reviews description
text = text.replace('4.9/5.0★', '4.9/5.0')

# 6. Welcome modal weather icon default
text = text.replace('<span id="welcomeWeatherIcon">🌤️</span>', '<span id="welcomeWeatherIcon"><i data-lucide="sun-medium" style="width:18px;height:18px;"></i></span>')

# 7. Quote box weather icons in JS
text = text.replace("icon: '🌅'", "icon: 'sunrise'")
text = text.replace("icon: '☀️'", "icon: 'sun'")
text = text.replace("icon: '🌤️'", "icon: 'sun-medium'")
text = text.replace("icon: '🌆'", "icon: 'sunset'")
text = text.replace("icon: '🌙'", "icon: 'moon'")
text = text.replace("icon: '✨'", "icon: 'sparkles'")

# 8. Welcome weather update in JS
text = text.replace("let icon = isDay ? '☀️' : '🌙';", "let icon = isDay ? 'sun' : 'moon';")
text = text.replace("icon = isDay ? '☀️' : '✨';", "icon = isDay ? 'sun' : 'sparkles';")
text = text.replace("icon = '🌤️';", "icon = 'cloud-sun';")
text = text.replace("icon = '🌧️';", "icon = 'cloud-rain';")
text = text.replace("icon = '⛈️';", "icon = 'cloud-lightning';")

# 9. Greeting welcome returning
text = text.replace("name ? `Chào mừng ${name} trở lại! 👋` : `Chào mừng bạn ghé chơi! ✨`", "name ? `Chào mừng ${name} trở lại!` : `Chào mừng bạn ghé chơi!`")

# 10. Rating stars display in review card generator
text = text.replace("const stars = '★'.repeat(Math.min(5, Math.max(1, fb.rating || 5)));",
                    "const starCount = Math.min(5, Math.max(1, fb.rating || 5)); const stars = `<span style='color:var(--accent-gold);letter-spacing:2px;'>${'★'.repeat(starCount)}</span>`;")

with open('/Users/thanhduy/Documents/olion-coffee/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Second pass emoji cleanup completed!')
