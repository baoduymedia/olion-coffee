import re

with open('index.html', 'r') as f:
    c = f.read()

# --- 1. Signatures ---
# HTML part
# Item 1: Matcha Quế Hoa -> Matcha Latte
c = c.replace('src="assets/menu/matcha_que_hoa.webp" alt="Matcha Quế Hoa — Đồ uống Signature thanh tao"', 'src="assets/menu/matcha_latte.webp" alt="Matcha Latte Olion — Đồ uống Signature thanh mát chuẩn Nhật"')
c = c.replace('>MATCHA QUẾ HOA</h3>', '>MATCHA LATTE</h3>')
c = c.replace('>Matcha cao cấp ướp hương hoa quế tự nhiên thanh tao quý phái, mang đến trải nghiệm hương vị Nhật Bản tinh tế.</p>', '>Matcha Nhật Bản thượng hạng thơm thanh đậm vị quyện cùng sữa tươi béo dịu, tạo nên cảm giác thư thái tươi mát trọn vẹn.</p>')

# Item 2 is kept as Cacao Bạc Hà

# Item 3: Bạc Xỉu -> Cà Phê Muối
c = c.replace('src="assets/menu/bac_xiu.webp" alt="Bạc Xỉu Olion — Đồ uống Signature ngọt ngào béo ngậy"', 'src="assets/menu/ca_phe_muoi.webp" alt="Cà Phê Muối Olion — Đồ uống Signature đậm đà béo ngậy"')
c = c.replace('>BẠC XỈU</h3>', '>CÀ PHÊ MUỐI OLION</h3>')
c = c.replace('>Cà phê sữa đặc truyền thống nhiều sữa ít cà phê, béo ngậy ngọt ngào đánh thức mọi giác quan trong từng ngụm thưởng thức.</p>', '>Cà phê Robusta rang mộc đậm đà hòa quyện cùng lớp kem muối béo mặn độc quyền của Olion, tạo nên trải nghiệm vị giác đầy lôi cuốn.</p>')

# i18n VI part
c = c.replace('sig_item_1_name: "MATCHA QUẾ HOA"', 'sig_item_1_name: "MATCHA LATTE"')
c = c.replace('sig_item_1_desc: "Matcha cao cấp ướp hương hoa quế tự nhiên thanh tao quý phái, mang đến trải nghiệm hương vị Nhật Bản tinh tế."', 'sig_item_1_desc: "Matcha Nhật Bản thượng hạng thơm thanh đậm vị quyện cùng sữa tươi béo dịu, tạo nên cảm giác thư thái tươi mát trọn vẹn."')

c = c.replace('sig_item_3_name: "BẠC XỈU"', 'sig_item_3_name: "CÀ PHÊ MUỐI OLION"')
c = c.replace('sig_item_3_desc: "Cà phê sữa đặc truyền thống nhiều sữa ít cà phê, béo ngậy ngọt ngào đánh thức mọi giác quan trong từng ngụm thưởng thức."', 'sig_item_3_desc: "Cà phê Robusta rang mộc đậm đà hòa quyện cùng lớp kem muối béo mặn độc quyền của Olion, tạo nên trải nghiệm vị giác đầy lôi cuốn."')

# i18n EN part
c = c.replace('sig_item_1_name: "OSMANTHUS MATCHA"', 'sig_item_1_name: "JAPANESE MATCHA LATTE"')
c = c.replace('sig_item_1_desc: "Premium matcha infused with the natural, elegant fragrance of osmanthus flowers, delivering a refined Japanese flavor experience."', 'sig_item_1_desc: "Premium ceremonial-grade Japanese matcha infused with silky fresh milk, delivering a crisp, refreshing, and calming indulgence."')

c = c.replace('sig_item_3_name: "BAC XIU (VIETNAMESE WHITE COFFEE)"', 'sig_item_3_name: "OLION SALTED CREAM COFFEE"')
c = c.replace('sig_item_3_desc: "Traditional Vietnamese coffee with condensed milk, sweet and creamy to awaken all senses in every sip."', 'sig_item_3_desc: "Bold artisanal Robusta coffee harmoniously blended with Olion\'s proprietary velvety salted cream, creating an irresistible flavor journey."')

# Loyalty text
c = c.replace('Đổi 1 ly Signature miễn phí (Matcha Quế Hoa, Cacao Bạc Hà, Bạc Xỉu)', 'Đổi 1 ly Signature miễn phí (Matcha Latte, Cacao Bạc Hà, Cà Phê Muối)')


# --- 2. Hours ---
# HTML layout
c = c.replace('Thứ 2 — Thứ 6', 'Thứ 2 — Thứ 7')
c = c.replace('Thứ 7 — Chủ Nhật', 'Chủ Nhật')
c = c.replace('<span style="font-weight: 700; color: var(--text-white);">08:00 — 20:00</span>\n                </div>\n                <div class="hours-row">\n                  <span style="color: var(--text-muted);" data-i18n="hours_weekend_label">Chủ Nhật</span>\n                  <span style="font-weight: 700; color: var(--text-white);">08:00 — 20:00</span>', '<span style="font-weight: 700; color: var(--text-white);">08:00 — 20:00</span>\n                </div>\n                <div class="hours-row">\n                  <span style="color: var(--text-muted);" data-i18n="hours_weekend_label">Chủ Nhật</span>\n                  <span style="font-weight: 700; color: var(--text-white);">08:00 — 17:00</span>')

c = c.replace('Giờ mở cửa:</strong> 08:00 — 20:00 (Cả tuần)', 'Giờ mở cửa:</strong> 08:00 — 20:00 (T2-T7) | 08:00 — 17:00 (CN)')

# i18n
c = c.replace('hours_weekday_label: "Monday — Friday"', 'hours_weekday_label: "Mon — Sat"')
c = c.replace('hours_weekend_label: "Saturday — Sunday"', 'hours_weekend_label: "Sunday"')

# JSON-LD
old_ld = """        "openingHoursSpecification": [
          {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": [
              "Monday",
              "Tuesday",
              "Wednesday",
              "Thursday",
              "Friday",
              "Saturday",
              "Sunday"
            ],
            "opens": "08:00",
            "closes": "20:00"
          }
        ],"""
new_ld = """        "openingHoursSpecification": [
          {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": [
              "Monday",
              "Tuesday",
              "Wednesday",
              "Thursday",
              "Friday",
              "Saturday"
            ],
            "opens": "08:00",
            "closes": "20:00"
          },
          {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Sunday"],
            "opens": "08:00",
            "closes": "17:00"
          }
        ],"""
c = c.replace(old_ld, new_ld)

with open('index.html', 'w') as f:
    f.write(c)

