with open('/Users/thanhduy/Documents/olion-coffee/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix iconEl assignments to render Lucide icon
old_quote_assign = """        if (iconEl) iconEl.textContent = data.icon;"""
new_quote_assign = """        if (iconEl) {
          iconEl.innerHTML = `<i data-lucide="${data.icon}" style="width:16px;height:16px;"></i>`;
          if (window.lucide) window.lucide.createIcons();
        }"""
text = text.replace(old_quote_assign, new_quote_assign)

old_welcome_assign = """        if (iconEl) iconEl.textContent = weather.icon;"""
new_welcome_assign = """        if (iconEl) {
          iconEl.innerHTML = `<i data-lucide="${weather.icon}" style="width:18px;height:18px;"></i>`;
          if (window.lucide) window.lucide.createIcons();
        }"""
text = text.replace(old_welcome_assign, new_welcome_assign)

with open('/Users/thanhduy/Documents/olion-coffee/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated dynamic weather and quote icon rendering with Lucide!')
