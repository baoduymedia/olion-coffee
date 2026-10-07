import re

with open('index.html', 'r') as f:
    c = f.read()

# 1. JSON-LD Schema
schema = """
  <!-- ======== 6. GOOGLE E-E-A-T / SEO SCHEMA ======== -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "CafeOrCoffeeShop",
    "name": "Olion Coffee",
    "image": "https://baoduymedia.github.io/olion-coffee/assets/space-4.webp",
    "@id": "https://baoduymedia.github.io/olion-coffee/",
    "url": "https://baoduymedia.github.io/olion-coffee/",
    "telephone": "+84783657587",
    "menu": "https://baoduymedia.github.io/olion-coffee/#menu",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "80/64a Dương Quảng Hàm",
      "addressLocality": "Gò Vấp",
      "addressRegion": "TP.HCM",
      "postalCode": "700000",
      "addressCountry": "VN"
    },
    "geo": {
      "@type": "GeoCoordinates",
      "latitude": 10.8231,
      "longitude": 106.6297
    },
    "openingHoursSpecification": {
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
      "opens": "07:00",
      "closes": "23:00"
    },
    "sameAs": [
      "https://www.facebook.com/profile.php?id=61594159312837",
      "https://www.tiktok.com/@olion.coffee",
      "https://www.instagram.com/olion.coffee/"
    ]
  }
  </script>
</head>"""
c = c.replace('</head>', schema)

# 2. Expertise Block in About Us
expertise = """            </div>
            
            <div class="expertise-block" style="margin-top: 32px; padding: 24px; background: rgba(211, 108, 45, 0.05); border-left: 4px solid var(--accent-gold); border-radius: 0 8px 8px 0;">
              <h3 style="font-family: var(--font-heading); color: var(--accent-gold); font-size: 1.5rem; margin-bottom: 12px; display: flex; align-items: center; gap: 8px;">
                <i data-lucide="award" style="width:24px;height:24px;"></i> Triết Lý Pha Chế
              </h3>
              <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.6; margin-bottom: 16px;">
                Chúng tôi đề cao tính <strong>chuyên môn (Expertise)</strong> trong từng giọt cà phê. 100% hạt cà phê tại Olion được tuyển chọn từ các nông trại canh tác theo tiêu chuẩn <em>nông sản sạch (Clean Agriculture)</em> tại Cầu Đất và Đắk Nông, rang mộc (không tẩm ướp) để giữ trọn vẹn hương vị nguyên bản (Specialty Coffee). Đội ngũ Barista được đào tạo chuyên sâu về kỹ thuật chiết xuất chuẩn SCA.
              </p>
              <div style="display: flex; gap: 16px; align-items: flex-start;">
                <div style="width: 54px; height: 54px; border-radius: 50%; overflow: hidden; border: 2px solid var(--border-light); flex-shrink: 0;">
                  <img src="assets/news/news-1-barista.webp" alt="Founder Olion" style="width:100%; height:100%; object-fit:cover;" loading="lazy" />
                </div>
                <div>
                  <p style="font-style: italic; color: #fff; font-size: 0.95rem; line-height: 1.5; margin-bottom: 8px;">
                    "Một ly cà phê ngon không chỉ nằm ở hạt chất lượng, mà còn ở trải nghiệm và sự tâm huyết của người pha. Ở Olion, chúng tôi làm điều đó mỗi ngày."
                  </p>
                  <p style="color: var(--accent-gold); font-weight: 600; font-size: 0.85rem; letter-spacing: 1px;">— FOUNDER & HEAD BARISTA</p>
                </div>
              </div>
            </div>
          </div>"""
c = c.replace('            </div>\n          </div>', expertise, 1)

# 3. Footer Privacy Policy Link
footer_bottom = """      <div class="footer-bottom">
        <p data-i18n="footer_rights">© 2024 Olion Coffee. All rights reserved. | <a href="#" onclick="event.preventDefault(); document.getElementById('privacyModal').classList.add('open')" style="color: var(--text-muted); text-decoration: underline;">Chính sách bảo mật dữ liệu</a></p>
        <p data-i18n="footer_credit">Thiết kế & Vận hành bởi Olion Creative Studio</p>
      </div>"""
c = re.sub(r'<div class="footer-bottom">.*?</div>', footer_bottom, c, flags=re.DOTALL)

# 4. Privacy Modal
privacy_modal = """  <!-- ======== 17. PRIVACY POLICY MODAL ======== -->
  <div class="modal-overlay" id="privacyModal" onclick="if(event.target === this) this.classList.remove('open')">
    <div class="modal-content" style="max-width: 500px; text-align: left;">
      <button type="button" class="modal-close-btn" onclick="document.getElementById('privacyModal').classList.remove('open')">✕</button>
      <h3 style="font-family: var(--font-heading); color: var(--accent-gold); font-size: 1.5rem; margin-bottom: 16px;">Chính sách bảo mật dữ liệu</h3>
      <p style="color: var(--text-body); font-size: 0.95rem; line-height: 1.6; margin-bottom: 12px;">Tại Olion Coffee, chúng tôi trân trọng sự tin tưởng của bạn. Dữ liệu số điện thoại và tên của bạn khi tham gia Minigame, Góp ý hoặc chương trình Tích điểm được chúng tôi cam kết:</p>
      <ul style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.6; padding-left: 20px; margin-bottom: 16px;">
        <li style="margin-bottom: 8px;"><strong>Bảo mật tuyệt đối:</strong> Chỉ lưu trữ trên máy chủ an toàn (Supabase Cloud), không chia sẻ hoặc bán cho bất kỳ bên thứ 3 nào.</li>
        <li style="margin-bottom: 8px;"><strong>Mục đích sử dụng:</strong> Chỉ dùng để đối chiếu tích điểm, trả thưởng Minigame và gửi các mã ưu đãi nội bộ (SMS/Zalo) nếu bạn đồng ý.</li>
        <li><strong>Xóa dữ liệu:</strong> Bất cứ lúc nào bạn muốn, chỉ cần gọi hotline, chúng tôi sẽ xóa toàn bộ lịch sử điểm và số điện thoại của bạn khỏi hệ thống.</li>
      </ul>
      <button type="button" class="btn btn-primary" style="width: 100%; justify-content: center;" onclick="document.getElementById('privacyModal').classList.remove('open')">Đã hiểu</button>
    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/@vimeo/player@2.23.0/dist/player.min.js"></script>"""
c = c.replace('  <script src="https://cdn.jsdelivr.net/npm/@vimeo/player@2.23.0/dist/player.min.js"></script>', privacy_modal)

with open('index.html', 'w') as f:
    f.write(c)

