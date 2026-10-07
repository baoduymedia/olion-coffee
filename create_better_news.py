import re

with open('news.html', 'r') as f:
    html = f.read()

# Extract header and footer and head
head_match = re.search(r'(<!DOCTYPE html>.*?</head>)', html, re.DOTALL)
head = head_match.group(1) if head_match else ""

header_match = re.search(r'(<header.*?</header>)', html, re.DOTALL)
header = header_match.group(1) if header_match else ""

footer_match = re.search(r'(<footer.*?</footer>)', html, re.DOTALL)
footer = footer_match.group(1) if footer_match else ""

news_modal_match = re.search(r'(<div class="modal-overlay" id="newsModal".*?</div>\s*</div>\s*</div>)', html, re.DOTALL)
news_modal = news_modal_match.group(1) if news_modal_match else ""

# Replace the modal share buttons (we need to inject share buttons into the modal!)
if news_modal:
    share_html = """
      <div style="margin-top: 24px; padding-top: 20px; border-top: 1px solid rgba(255,255,255,0.1); display: flex; justify-content: space-between; align-items: center;">
        <span style="color: var(--text-muted); font-size: 14px;">Chia sẻ bài viết này:</span>
        <div style="display: flex; gap: 12px;">
          <button onclick="shareToFB()" style="background: #1877F2; border: none; width: 36px; height: 36px; border-radius: 50%; color: white; cursor: pointer; display: flex; align-items: center; justify-content: center;"><i data-lucide="facebook" style="width: 18px; height: 18px;"></i></button>
          <button onclick="copyLink()" style="background: #E59A55; border: none; width: 36px; height: 36px; border-radius: 50%; color: white; cursor: pointer; display: flex; align-items: center; justify-content: center;"><i data-lucide="link" style="width: 18px; height: 18px;"></i></button>
        </div>
      </div>
"""
    # Insert share html before the end of modal-content
    news_modal = news_modal.replace('</div>\n  </div>\n</div>', f'{share_html}    </div>\n  </div>\n</div>')

news_html_content = f"""{head}
<body style="background: var(--bg-dark); color: var(--text-white); padding-top: 80px; font-family: var(--font-body);">
{header}

<style>
  /* Tabs */
  .news-tabs {{
    display: flex; justify-content: center; gap: 20px; margin-bottom: 40px; flex-wrap: wrap;
  }}
  .news-tab-btn {{
    padding: 12px 24px; border-radius: 50px; border: 1px solid var(--border-gold); background: transparent; color: var(--text-muted); font-family: var(--font-heading); font-size: 1.1rem; cursor: pointer; transition: all 0.3s ease;
  }}
  .news-tab-btn.active {{
    background: linear-gradient(135deg, var(--accent-gold), var(--accent-rust)); color: white; border-color: transparent;
  }}
  .news-tab-btn:hover:not(.active) {{
    background: rgba(229,154,85,0.1); color: var(--accent-gold);
  }}
  
  /* Article Cards */
  .article-grid {{
    display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px;
  }}
  .article-card {{
    background: #111A14; border: 1px solid rgba(229,154,85,0.2); border-radius: 16px; overflow: hidden; transition: transform 0.3s; cursor: pointer; display: flex; flex-direction: column;
  }}
  .article-card:hover {{ transform: translateY(-5px); border-color: var(--accent-gold); box-shadow: 0 10px 30px rgba(0,0,0,0.5); }}
  .article-img-wrap {{ height: 220px; overflow: hidden; position: relative; }}
  .article-img {{ width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s; }}
  .article-card:hover .article-img {{ transform: scale(1.05); }}
  .article-content {{ padding: 24px; display: flex; flex-direction: column; flex: 1; }}
  .article-meta {{ font-size: 12px; color: var(--text-muted); display: flex; justify-content: space-between; margin-bottom: 12px; }}
  .article-title {{ font-family: var(--font-heading); font-size: 1.3rem; color: var(--text-white); margin-bottom: 12px; line-height: 1.4; }}
  .article-desc {{ color: var(--text-muted); font-size: 0.95rem; line-height: 1.6; margin-bottom: 20px; flex: 1; }}
  .article-readmore {{ color: var(--accent-gold); font-weight: 600; display: inline-flex; align-items: center; gap: 8px; font-size: 14px; }}
  
  /* Social Grid */
  .social-grid {{
    display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 30px; align-items: start;
  }}
  .social-box {{
    background: white; border-radius: 16px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.5);
  }}
  .ig-box {{
    background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%);
    padding: 3px; border-radius: 16px;
  }}
  .ig-inner {{
    background: #111A14; border-radius: 13px; padding: 40px 20px; text-align: center; height: 100%;
  }}
</style>

<main>
  <section style="padding: 60px 0 20px;">
    <div class="shell" style="text-align: center;">
      <h1 style="font-family: var(--font-heading); color: var(--accent-gold); font-size: clamp(2.5rem, 5vw, 3.5rem); margin-bottom: 16px;">TIN TỨC & SỰ KIỆN</h1>
      <p style="color: var(--text-muted); max-width: 600px; margin: 0 auto 40px;">Theo dõi những thông tin mới nhất, câu chuyện thú vị và các hoạt động mạng xã hội của Olion Coffee.</p>
      
      <div class="news-tabs">
        <button class="news-tab-btn active" onclick="switchTab('articles')">Bài Viết Từ Olion</button>
        <button class="news-tab-btn" onclick="switchTab('social')">Mạng Xã Hội</button>
      </div>
    </div>
  </section>

  <!-- TAB 1: WEBSITE ARTICLES -->
  <section id="tab-articles" class="shell" style="padding-bottom: 80px; display: block;">
    <div class="article-grid" id="articleGrid">
      <!-- Injected by JS -->
    </div>
  </section>

  <!-- TAB 2: SOCIAL MEDIA -->
  <section id="tab-social" class="shell" style="padding-bottom: 80px; display: none;">
    <div class="social-grid">
      
      <!-- Facebook -->
      <div class="social-box" style="min-height: 500px; display: flex; flex-direction: column;">
        <div style="background: #1877F2; color: white; padding: 16px; font-weight: bold; display: flex; align-items: center; gap: 10px;">
          <i data-lucide="facebook"></i> Fanpage Facebook
        </div>
        <div style="flex: 1; padding: 10px; background: white; display: flex; justify-content: center;">
          <div id="fb-root"></div>
          <script async defer crossorigin="anonymous" src="https://connect.facebook.net/vi_VN/sdk.js#xfbml=1&version=v18.0"></script>
          <div class="fb-page" data-href="https://www.facebook.com/profile.php?id=61594159312837" data-tabs="timeline" data-width="340" data-height="500" data-small-header="false" data-adapt-container-width="true" data-hide-cover="false" data-show-facepile="true">
            <blockquote cite="https://www.facebook.com/profile.php?id=61594159312837" class="fb-xfbml-parse-ignore"><a href="https://www.facebook.com/profile.php?id=61594159312837">Olion Coffee</a></blockquote>
          </div>
        </div>
      </div>

      <!-- TikTok -->
      <div class="social-box" style="background: #000; min-height: 500px; display: flex; flex-direction: column;">
        <div style="background: #111; color: white; padding: 16px; font-weight: bold; display: flex; align-items: center; gap: 10px; border-bottom: 1px solid #333;">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12.525.02c1.31-.02 2.61-.01 3.91-.02.08 1.53.63 3.09 1.75 4.17 1.12 1.11 2.7 1.62 4.24 1.79v4.03c-1.44-.05-2.89-.35-4.2-.97-.57-.26-1.1-.59-1.62-.93-.01 2.92.01 5.84-.02 8.75-.08 1.4-.54 2.79-1.35 3.94-1.31 1.92-3.58 3.17-5.91 3.21-1.43.08-2.86-.31-4.08-1.03-2.02-1.12-3.44-3.1-3.66-5.39-.17-1.89.28-3.8 1.25-5.39 1.43-2.3 4.12-3.64 6.78-3.32v4.05c-1.66-.27-3.33.22-4.38 1.5-.6.7-.93 1.6-.96 2.53-.02 1.07.3 2.12.91 2.99.9 1.22 2.45 1.83 3.94 1.5 1.53-.33 2.65-1.55 2.87-3.08.1-1.39.05-2.79.05-4.18V.02z"/></svg>
          Kênh TikTok
        </div>
        <div style="flex: 1; display: flex; justify-content: center; align-items: center; overflow: hidden; background: white;">
          <blockquote class="tiktok-embed" cite="https://www.tiktok.com/@olion.coffee" data-unique-id="olion.coffee" data-embed-type="creator" style="max-width: 340px; min-width: 288px; margin: 0;" > <section> <a target="_blank" href="https://www.tiktok.com/@olion.coffee?refer=creator_embed">@olion.coffee</a> </section> </blockquote> <script async src="https://www.tiktok.com/embed.js"></script>
        </div>
      </div>

      <!-- Instagram -->
      <div class="ig-box">
        <div class="ig-inner" style="display: flex; flex-direction: column; justify-content: center; align-items: center;">
          <i data-lucide="instagram" style="width: 48px; height: 48px; color: white; margin-bottom: 20px;"></i>
          <h3 style="color: white; font-family: var(--font-heading); font-size: 1.8rem; margin-bottom: 10px;">@olion.coffee</h3>
          <p style="color: var(--text-muted); margin-bottom: 30px;">Khám phá những khoảnh khắc đẹp nhất và check-in không gian cực chill tại Olion Coffee trên Instagram.</p>
          <a href="https://www.instagram.com/olion.coffee/" target="_blank" class="btn btn-primary" style="border-radius: 50px; background: white; color: black; font-weight: bold; padding: 12px 32px; display: inline-flex; align-items: center; gap: 8px;">
            Theo dõi ngay <i data-lucide="arrow-right" style="width: 16px; height: 16px;"></i>
          </a>
        </div>
      </div>

    </div>
  </section>
</main>

{footer}

{news_modal}

<script>
  function switchTab(tabId) {{
    document.querySelectorAll('.news-tab-btn').forEach(btn => btn.classList.remove('active'));
    document.getElementById('tab-articles').style.display = 'none';
    document.getElementById('tab-social').style.display = 'none';
    
    if(tabId === 'articles') {{
      document.querySelectorAll('.news-tab-btn')[0].classList.add('active');
      document.getElementById('tab-articles').style.display = 'block';
    }} else {{
      document.querySelectorAll('.news-tab-btn')[1].classList.add('active');
      document.getElementById('tab-social').style.display = 'block';
    }}
  }}

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
      desc: 'Tuần đầu tiên mở cửa đã khép lại với biết bao cung bậc cảm xúc! Olion Coffee vô cùng trân trọng và biết ơn...',
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
      desc: 'Tại Olion Coffee, mỗi ly thức uống đều được pha chế bằng cả sự nâng niu và tỉ mỉ. Lớp bọt kem muối béo mặn...',
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
      desc: 'Bước qua cánh cửa Olion, bạn sẽ cảm nhận ngay một không gian tách biệt khỏi nhịp sống vội vã ngoài phố thị...',
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
      desc: 'Nhìn lại những khoảnh khắc tuyệt vời trong tuần lễ Grand Opening! Khách hàng không chỉ được thưởng thức menu giảm giá 20%...',
      contentHtml: `
        <p>Nhìn lại những khoảnh khắc tuyệt vời trong tuần lễ Grand Opening! Khách hàng không chỉ được thưởng thức menu giảm giá 20% mà còn nhận được hàng trăm phần quà thú vị từ Vòng Quay May Mắn.</p>
        <p>Đừng quên Olion Coffee vẫn đang áp dụng chương trình Tích điểm Loyalty: 10 ly tặng 1 ly hoàn toàn miễn phí nhé!</p>
      `
    }}
  }};

  // Render Articles
  const grid = document.getElementById('articleGrid');
  for (const [id, data] of Object.entries(newsDatabase)) {{
    const img = data.images && data.images.length > 0 ? data.images[0] : 'assets/logo-white.webp';
    grid.innerHTML += `
      <article class="article-card" onclick="openNewsModal('${{id}}')">
        <div class="article-img-wrap">
          <img src="${{img}}" class="article-img" loading="lazy" />
        </div>
        <div class="article-content">
          <div class="article-meta">
            <span><i data-lucide="calendar" style="width:12px;height:12px;margin-right:4px;vertical-align:-2px;"></i>${{data.date}}</span>
            <span style="color:var(--accent-gold);">${{data.category}}</span>
          </div>
          <h3 class="article-title">${{data.title}}</h3>
          <p class="article-desc">${{data.desc}}</p>
          <div class="article-readmore">Đọc tiếp <i data-lucide="arrow-right" style="width:16px;height:16px;"></i></div>
        </div>
      </article>
    `;
  }}

  let currentModalId = '';

  function openNewsModal(id) {{
    currentModalId = id;
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

  function shareToFB() {{
    const url = encodeURIComponent(window.location.origin + window.location.pathname + "?article=" + currentModalId);
    window.open(`https://www.facebook.com/sharer/sharer.php?u=${{url}}`, '_blank', 'width=600,height=400');
  }}

  function copyLink() {{
    const url = window.location.origin + window.location.pathname + "?article=" + currentModalId;
    navigator.clipboard.writeText(url).then(() => {{
      alert("Đã sao chép đường link bài viết!");
    }});
  }}

  // Auto open article if URL has ?article=...
  window.addEventListener('DOMContentLoaded', () => {{
    const urlParams = new URLSearchParams(window.location.search);
    const articleId = urlParams.get('article');
    if(articleId && newsDatabase[articleId]) {{
      openNewsModal(articleId);
    }}
  }});
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

