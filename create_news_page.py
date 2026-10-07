import re
import os

with open('index.html', 'r') as f:
    html = f.read()

# We need to extract the Header, Footer, and the basic head block.
# Let's extract head
head_match = re.search(r'(<!DOCTYPE html>.*?</head>)', html, re.DOTALL)
head = head_match.group(1)

# Modify title in head
head = head.replace('<title>Olion Coffee', '<title>Tin Tức & Sự Kiện | Olion Coffee')
head = head.replace('Elegance in Every Sip', 'Cập nhật sự kiện, ưu đãi và câu chuyện từ Olion')

# Extract Header
header_match = re.search(r'(<header.*?</header>)', html, re.DOTALL)
header = header_match.group(1)

# Modify header active state if needed (remove active from Home, add to News if we have one, but we don't have a news link in the top nav yet).

# Extract Footer
footer_match = re.search(r'(<footer.*?</footer>)', html, re.DOTALL)
footer = footer_match.group(1)

# Extract News Modal
news_modal_match = re.search(r'(<div class="modal-overlay" id="newsModal".*?</div>\s*</div>\s*</div>)', html, re.DOTALL)
news_modal = news_modal_match.group(1) if news_modal_match else ""

# Extract the News JS config
news_js_match = re.search(r'(const newsDatabase = {.*?};\s*function openNewsModal[^\}]+})', html, re.DOTALL)
# Wait, it's safer to just load the same script or include it manually. Let's just grab the whole script block that contains newsDatabase.
# Actually I can just write it from scratch for news.html

news_html_content = f"""{head}
<body style="background: var(--bg-dark); color: var(--text-white); padding-top: 80px;">
{header}

<main>
  <section class="shell" style="padding: 60px 0;">
    <div class="section-header" style="text-align: center; margin-bottom: 50px;">
      <h1 style="font-family: var(--font-heading); color: var(--accent-gold); font-size: clamp(2.5rem, 5vw, 3.5rem); margin-bottom: 16px;">TIN TỨC & SỰ KIỆN</h1>
      <p style="color: var(--text-muted); max-width: 600px; margin: 0 auto;">Cập nhật những hoạt động, chương trình khuyến mãi và câu chuyện mới nhất tại Olion Coffee.</p>
    </div>

    <!-- The actual news grid -->
    <div class="news-main-grid" id="newsGridPage">
      <!-- We will inject the existing news cards here using JS or hardcode them based on index.html -->
    </div>
  </section>

  <!-- Social Media Sync Section -->
  <section style="background: rgba(20,29,22,0.5); border-top: 1px solid rgba(229,154,85,0.1); padding: 80px 0;">
    <div class="shell">
      <div class="section-header" style="text-align: center; margin-bottom: 40px;">
        <h2 style="font-family: var(--font-heading); color: var(--accent-gold); font-size: 2rem;">HOẠT ĐỘNG TRÊN MẠNG XÃ HỘI</h2>
        <p style="color: var(--text-muted);">Theo dõi Olion Coffee để không bỏ lỡ bất kỳ ưu đãi nào.</p>
      </div>
      
      <div style="display: flex; flex-wrap: wrap; gap: 30px; justify-content: center;">
        <!-- Facebook Feed Plugin -->
        <div style="flex: 1; min-width: 300px; max-width: 500px; background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
          <div id="fb-root"></div>
          <script async defer crossorigin="anonymous" src="https://connect.facebook.net/vi_VN/sdk.js#xfbml=1&version=v18.0"></script>
          <div class="fb-page" data-href="https://www.facebook.com/profile.php?id=61594159312837" data-tabs="timeline" data-width="500" data-height="600" data-small-header="false" data-adapt-container-width="true" data-hide-cover="false" data-show-facepile="true">
            <blockquote cite="https://www.facebook.com/profile.php?id=61594159312837" class="fb-xfbml-parse-ignore"><a href="https://www.facebook.com/profile.php?id=61594159312837">Olion Coffee</a></blockquote>
          </div>
        </div>
      </div>
    </div>
  </section>
</main>

{footer}

{news_modal}

<script>
  // Copy of newsDatabase for the news page
  const newsDatabase = {{
    'news-first-week': {{
      title: 'OLION’S FIRST WEEK — NHẬT KÝ TUẦN ĐẦU TIÊN',
      date: '19/09/2026',
      category: 'Sự kiện đặc biệt',
      images: [
        'assets/news/news-1-flowers.webp',
        'assets/news/news-1-drinks.webp',
        'assets/news/news-1-serving.webp',
        'assets/news/news-1-recap.webp',
        'assets/news/news-1-barista.webp'
      ],
      contentHtml: `
        <p>Tuần đầu tiên mở cửa đã khép lại với biết bao cung bậc cảm xúc! Olion Coffee vô cùng trân trọng và biết ơn những lẵng hoa tươi thắm, những lời chúc mừng chân thành từ quý đối tác, bạn bè và đặc biệt là sự ủng hộ nhiệt tình của hàng trăm lượt khách hàng đã ghé thăm quán mỗi ngày.</p>
        <p>Mỗi ly cà phê trao đi là một lời cảm ơn sâu sắc. Chúng tôi cam kết sẽ tiếp tục hoàn thiện không gian và chất lượng đồ uống để mang đến những trải nghiệm tuyệt vời nhất cho bạn.</p>
      `
    }},
    'news-signature-drinks': {{
      title: 'Khám Phá Bộ Đôi Matcha Latte & Cà Phê Muối Chuẩn Vị',
      date: '18/09/2026',
      category: 'Thực Đơn Signature',
      images: [
        'assets/news/news-1-drinks.webp',
        'assets/space-1.webp'
      ],
      contentHtml: `
        <p>Tại Olion Coffee, mỗi ly thức uống đều được pha chế bằng cả sự nâng niu và tỉ mỉ.</p>
        <div class="news-quote-box">
          "Lớp bọt kem muối béo mặn sánh mịn hòa cùng cốt cà phê đậm đà tạo nên hương vị bùng nổ ngay từ ngụm đầu tiên."
        </div>
        <p>Bên cạnh đó, dòng Matcha Latte sử dụng 100% bột trà xanh nhập khẩu từ Shizuoka Nhật Bản, mang hương thơm thanh nhã và vị đắng dịu êm ái.</p>
      `
    }},
    'news-space-story': {{
      title: 'Góc Yên Bình Giữa Lòng Gò Vấp Cho Những Buổi Chiều Làm Việc',
      date: '15/09/2026',
      category: 'Không Gian Quán',
      images: [
        'assets/news/news-1-space.webp',
        'assets/space-4.webp'
      ],
      contentHtml: `
        <p>Bước qua cánh cửa Olion, bạn sẽ cảm nhận ngay một không gian tách biệt khỏi nhịp sống vội vã ngoài phố thị.</p>
        <p>Tông màu gỗ ấm cúng, hệ thống đèn lồng giấy dịu mắt cùng những chậu cây xanh mướt tạo nên một chốn dừng chân hoàn hảo để đọc sách, làm việc hay trò chuyện cùng bạn bè.</p>
      `
    }},
    'news-opening-promo': {{
      title: 'Grand Opening Recap — Tuần Lễ Khai Trương Rực Rỡ Ưu Đãi',
      date: '12/09/2026',
      category: 'Chương Trình Khuyến Mãi',
      images: [
        'assets/news/news-1-recap.webp'
      ],
      contentHtml: `
        <p>Nhìn lại những khoảnh khắc tuyệt vời trong tuần lễ Grand Opening! Khách hàng không chỉ được thưởng thức menu giảm giá 20% mà còn nhận được hàng trăm phần quà thú vị từ Vòng Quay May Mắn.</p>
        <p>Đừng quên Olion Coffee vẫn đang áp dụng chương trình Tích điểm Loyalty: 10 ly tặng 1 ly hoàn toàn miễn phí nhé!</p>
      `
    }}
  }};

  function openNewsModal(id) {{
    const data = newsDatabase[id];
    if (!data) return;
    
    document.getElementById('newsModalTitle').textContent = data.title;
    document.getElementById('newsModalDate').textContent = data.date;
    document.getElementById('newsModalCategory').textContent = data.category;
    document.getElementById('newsModalBody').innerHTML = data.contentHtml;
    
    const sliderWrap = document.getElementById('newsModalSlider');
    sliderWrap.innerHTML = '';
    
    if (data.images && data.images.length > 0) {{
      sliderWrap.style.display = 'block';
      
      const track = document.createElement('div');
      track.className = 'news-slider-track';
      
      data.images.forEach(src => {{
        const slide = document.createElement('div');
        slide.className = 'news-slide';
        slide.innerHTML = `<img src="${{src}}" alt="Ảnh tin tức Olion" loading="lazy" />`;
        track.appendChild(slide);
      }});
      
      sliderWrap.appendChild(track);
      
      if (data.images.length > 1) {{
        const btnPrev = document.createElement('button');
        btnPrev.className = 'news-slider-btn prev';
        btnPrev.innerHTML = '❮';
        btnPrev.onclick = () => {{ track.scrollBy({{ left: -track.offsetWidth, behavior: 'smooth' }}); }};
        
        const btnNext = document.createElement('button');
        btnNext.className = 'news-slider-btn next';
        btnNext.innerHTML = '❯';
        btnNext.onclick = () => {{ track.scrollBy({{ left: track.offsetWidth, behavior: 'smooth' }}); }};
        
        sliderWrap.appendChild(btnPrev);
        sliderWrap.appendChild(btnNext);
      }}
    }} else {{
      sliderWrap.style.display = 'none';
    }}
    
    document.getElementById('newsModal').classList.add('open');
    document.body.style.overflow = 'hidden';
  }}
  
  function closeNewsModal() {{
    document.getElementById('newsModal').classList.remove('open');
    document.body.style.overflow = 'auto';
  }}
</script>

<!-- Add Lucide icons -->
<script src="https://unpkg.com/lucide@latest"></script>
<script>
  lucide.createIcons();
</script>
</body>
</html>
"""

with open('news.html', 'w') as f:
    f.write(news_html_content)

