document.addEventListener('DOMContentLoaded', () => {
      const initDeferredIcons = () => {
        if (window.lucide && typeof window.lucide.createIcons === 'function') {
          window.lucide.createIcons();
          window._lucideReady = true;
        }
      };
      if ('requestIdleCallback' in window) {
        requestIdleCallback(initDeferredIcons, { timeout: 1200 });
      } else {
        setTimeout(initDeferredIcons, 100);
      }
      const I18N_DICT = {
        vi: {
          nav_amenities: "Tiện ích",
          nav_about: "Về Olion",
          nav_signature: "Signature",
          nav_menu: "Thực đơn",
          nav_spaces: "Không gian",
          nav_services: "Đặt bàn & Dịch vụ",
          nav_news: "Tin tức",
          nav_faq: "Hỏi đáp",
          nav_contact: "Liên hệ",
          nav_feedback: "Góp ý quán",
          nav_loyalty: "Tích điểm",
          drawer_home: "Trang chủ",
          drawer_amenities: "Tiện ích & Không gian",
          drawer_about: "Về Olion Coffee",
          drawer_signature: "Món Signature",
          drawer_menu: "Thực đơn đồ uống",
          drawer_menu_board: "Bảng Menu Tổng (Toàn Trang)",
          drawer_spaces: "Không gian quán",
          drawer_services: "Đặt bàn & Thuê không gian",
          drawer_news: "Tin tức & Sự kiện",
          drawer_faq: "Hỏi đáp",
          drawer_contact: "Thông tin liên hệ",
          drawer_call: "Gọi Hotline: 0783 657 587",
          drawer_feedback: "Góp ý & Đánh giá",
          drawer_loyalty: "Tra Cứu Điểm Tích Lũy",
          drawer_lang_label: "Ngôn ngữ / Language:",
          dock_home: "Trang chủ",
          dock_menu: "Thực đơn",
          dock_spaces: "Không gian",
          dock_contact: "Liên hệ",
          hero_eyebrow: "OLION COFFEE · ELEGANCE IN EVERY SIP",
          hero_title: 'OLION COFFEE <span style="color: var(--accent-gold); font-weight: 300;">—</span><br><span class="italic-gold">Cà Phê Gò Vấp Không Gian Yên Tĩnh & Fine Dining</span>',
          hero_subtitle: "Quán cà phê đẹp ở Dương Quảng Hàm, Gò Vấp với không gian sang trọng và đồ uống thủ công tinh tế. Thưởng thức hương vị nguyên bản, đắm chìm trong góc nhỏ tĩnh lặng giữa lòng Sài Gòn.",
          hero_cta_menu: "Khám phá thực đơn →",
          hero_cta_about: "Câu chuyện quán",
          stats_items_count: "Món trong menu",
          stats_categories: "Danh mục đồ uống",
          stats_handcrafted: "Pha thủ công",
          stats_days_open: "Ngày mở cửa/năm",
          about_eyebrow: "● Về Olion Coffee",
          about_title: 'Chắt chiu từng giọt,<br><span class="accent">trao hương vị tinh tế</span>.',
          about_desc: "Trời trưa hơi gắt, ghé OLION thả lưng xuống chiếc ghế quen, ngắm ánh đèn vàng dịu mắt và làm ngụm nước mát lạnh rồi tỉnh tiếp nha. Không chỉ là cà phê, OLION muốn đem tới trải nghiệm trọn vẹn: đồ uống pha tay tỉ mỉ, không gian ấm cúng và những khoảnh khắc thật chậm.",
          about_feat_1_title: "Pha thủ công",
          about_feat_1_desc: "Từng ly được pha chế tỉ mỉ tại quầy",
          about_feat_2_title: "Nguyên liệu chọn lọc",
          about_feat_2_desc: "Hạt mộc rang xay & trà cao cấp",
          about_feat_3_title: "Không gian yên tĩnh",
          about_feat_3_desc: "Góc làm việc & thư giãn ấm cúng",
          about_feat_4_title: "Phục vụ tận tâm",
          about_feat_4_desc: "Nụ cười và sự chu đáo mỗi ngày",
          sig_eyebrow: "Món Bán Chạy",
          sig_title: 'Món <span class="accent">Signature</span> của quán',
          sig_desc: "Ba công thức độc quyền được khách hàng yêu thích nhất tại Olion Coffee.",
          sig_item_1_name: "MATCHA LATTE",
          sig_item_1_desc: "Matcha Nhật Bản thượng hạng thơm thanh đậm vị quyện cùng sữa tươi béo dịu, tạo nên cảm giác thư thái tươi mát trọn vẹn.",
          sig_item_2_name: "CACAO BẠC HÀ",
          sig_item_2_desc: "Sự the mát sảng khoái của bạc hà hòa quyện hoàn hảo cùng vị đắng dịu của cacao nguyên chất béo thơm.",
          sig_item_3_name: "CÀ PHÊ MUỐI OLION",
          sig_item_3_desc: "Cà phê Robusta rang mộc đậm đà hòa quyện cùng lớp kem muối béo mặn độc quyền của Olion, tạo nên trải nghiệm vị giác đầy lôi cuốn.",
          menu_eyebrow: "● Thực Đơn Đa Dạng",
          menu_title: 'Khám phá <span class="accent">món ngon</span> yêu thích',
          menu_desc: "Cà phê rang xay, trà sữa đậm vị, nước ép và sữa chua tươi mát — chọn danh mục để xem chi tiết.",
          menu_tab_board: "MENU TỔNG",
          menu_tab_coffee: "Cà Phê",
          menu_tab_tea: "Trà Trái Cây",
          menu_tab_matcha: "Matcha",
          menu_tab_cacao: "Cacao",
          menu_tab_juice: "Nước Ép",
          menu_tab_yagout: "Sữa Chua",
          menu_tab_topping: "Topping",
          spaces_eyebrow: "● Không Gian Quán",
          spaces_title: 'Nơi dừng chân <span class="accent">ấm áp</span>',
          spaces_desc: "Góc nhỏ tĩnh lặng để làm việc, trò chuyện cùng bạn bè hoặc đơn giản là ngắm nhìn phố thị qua khung kính.",
          space_card_1: "Quầy pha chế thủ công",
          space_card_2: "Góc thư giãn & chuyện trò",
          space_card_3: "Góc làm việc yên tĩnh",
          space_card_4: "Toàn cảnh ấm cúng",
          news_eyebrow: "● Bản Tin & Sự Kiện",
          news_title: 'Tin tức & <span class="accent">Sự kiện</span>',
          news_desc: "Khám phá những khoảnh khắc đáng nhớ, câu chuyện thức uống và các hoạt động mới nhất tại Olion Coffee.",
          news_read_more: "Xem chi tiết →",
          faq_eyebrow: "● Hỏi Đáp Nhanh",
          faq_title: 'Bạn <span class="accent">thắc mắc?</span>',
          faq_q1: "OLION COFFEE có giao hàng tận nơi không?",
          faq_a1: "Dịch vụ giao tận nơi đang được Olion chuẩn bị và sẽ sớm ra mắt trong thời gian tới! Hiện tại, Olion tập trung mang đến trải nghiệm không gian tốt nhất khi bạn ghé quán trực tiếp hoặc đặt bàn trước qua website / hotline 0783 657 587.",
          faq_q2: "Nguyên liệu và Cà phê của OLION có gì đặc biệt?",
          faq_a2: "Olion Coffee sử dụng 100% hạt Robusta & Arabica rang mộc nguyên chất từ nông trại Cầu Đất, bột Matcha nhập khẩu Nhật Bản và trái cây tươi mỗi ngày, tuyệt đối không sử dụng hương liệu nhân tạo hay chất bảo quản.",
          faq_q3: "Có thể điều chỉnh độ ngọt và lượng đá theo khẩu vị không?",
          faq_a3: "Hoàn toàn được! Bạn có thể yêu cầu barista gia giảm mức ngọt (0%, 30%, 50%, 70%, 100%) và lượng đá tùy thích, hoặc yêu cầu đổi sang sữa yến mạch Oatside để phù hợp với chế độ ăn uống của mình.",
          reviews_eyebrow: "● Cảm Nhận Khách Hàng",
          reviews_title: 'Khách hàng <span class="accent">nói gì</span> về Olion?',
          reviews_desc: "Được chấm 4.9/5.0 từ hơn 280+ đánh giá thực tế trên Google Maps và Facebook.",
          review_1_quote: '"Quán nằm trong hẻm yên tĩnh ở Dương Quảng Hàm, bước vào cảm giác như tách biệt khỏi xô bồ ngoài kia. Đèn vàng ấm mắt, bàn ghế gỗ cao ngồi làm việc cả buổi rất thoải mái. Cà phê muối béo mặn cực kỳ vừa miệng!"',
          review_1_role: "Sinh viên ĐH Văn Lang",
          review_2_quote: '"Matcha latte ở đây chuẩn vị Nhật, thơm đắng thanh nhẹ và không bị ngọt gắt như nhiều chỗ khác. Tụi mình hay ghé đây đọc sách và trò chuyện cuối tuần vì nhạc mở vừa phải rất dễ chịu."',
          review_2_role: "Graphic Designer",
          review_3_quote: '"Bạc xỉu kem trứng ngon đỉnh chóp! Lớp bọt trứng béo mịn uống tới đâu dính tới đó. Nhân viên thân thiện, nhiệt tình châm trà liên tục. Chắc chắn sẽ là quán ruột của mình."',
          review_3_role: "Freelancer Gò Vấp",
          review_btn: "Gửi đánh giá của bạn →",
          contact_eyebrow: "● Thông Tin Liên Hệ",
          contact_title: 'Bạn <span class="accent">muốn ghé</span> chơi?',
          contact_addr_title: "Địa chỉ quán",
          contact_hotline_title: "Hotline đặt bàn & hỗ trợ",
          contact_social_title: "Kênh mạng xã hội",
          hours_title: "Giờ mở cửa",
          hours_weekday_label: "Thứ 2 — Thứ 7",
          hours_weekend_label: "Chủ Nhật",
          hours_holiday_label: "Các ngày Lễ / Tết",
          hours_holiday_val: "Mở cửa bình thường",
          hours_quote: '"Trời trưa hơi gắt, ghé OLION thả lưng xuống chiếc ghế quen, ngắm ánh đèn vàng dịu mắt và làm ngụm nước mát lạnh rồi tỉnh tiếp nha."',
          footer_explore: "Khám Phá",
          footer_links: "Liên Kết",
          footer_rights: "© 2024 Olion Coffee. All rights reserved.",
          footer_credit: "Thiết kế & Vận hành bởi Olion Creative Studio",
          loyalty_eyebrow: "Thành Viên Olion",
          loyalty_title: "Tra Cứu Điểm Tích Lũy",
          loyalty_desc: "Nhập số điện thoại để kiểm tra số điểm hiện có và các ưu đãi đang chờ bạn!",
          loyalty_input_label: "Số điện thoại của bạn",
          loyalty_phone_placeholder: "Ví dụ: 0908123456",
          loyalty_btn_lookup: "Tra Cứu",
          loyalty_current_points: "Điểm tích lũy",
          wheel_float: "Quay Nhận Quà",
          back_to_top: "Lên đầu trang",
          amenities_eyebrow: '<span class="eyebrow-num">✦</span> Tiện Ích & Không Gian Làm Việc',
          amenities_title: 'Tiện Nghi Hoàn Hảo Cho <span class="accent">Làm Việc & Thư Giãn</span>',
          amenities_desc: 'Không gian tĩnh lặng, trang bị đầy đủ ổ điện từng bàn, wifi 5G cực nhanh và bãi đỗ xe an ninh — sẵn sàng đồng hành cùng bạn học tập, chạy deadline và thưởng thức cà phê.'
        },
        en: {
          nav_amenities: "Amenities",
          nav_about: "About Us",
          nav_signature: "Signatures",
          nav_menu: "Menu",
          nav_spaces: "Ambiance",
          nav_services: "Booking & Space",
          nav_news: "News",
          nav_faq: "FAQ",
          nav_contact: "Contact",
          nav_feedback: "Feedback",
          nav_loyalty: "Loyalty",
          drawer_home: "Home",
          drawer_amenities: "Amenities & Workspaces",
          drawer_about: "About Olion Coffee",
          drawer_signature: "Signature Drinks",
          drawer_menu: "Beverage Menu",
          drawer_menu_board: "Full Menu Board (Fullscreen)",
          drawer_spaces: "Our Spaces",
          drawer_services: "Table Booking & Space Rental",
          drawer_news: "News & Events",
          drawer_faq: "FAQ",
          drawer_contact: "Contact Info",
          drawer_call: "Call Hotline: 0783 657 587",
          drawer_feedback: "Feedback & Reviews",
          drawer_loyalty: "Check Loyalty Points",
          drawer_lang_label: "Ngôn ngữ / Language:",
          dock_home: "Home",
          dock_menu: "Menu",
          dock_spaces: "Spaces",
          dock_contact: "Contact",
          hero_eyebrow: "OLION COFFEE · ELEGANCE IN EVERY SIP",
          hero_title: 'OLION COFFEE <span style="color: var(--accent-gold); font-weight: 300;">—</span><br><span class="italic-gold">Fine Dining & Quiet Coffee Sanctuary in Go Vap</span>',
          hero_subtitle: "An exquisite boutique cafe on Duong Quang Ham, Go Vap, offering a luxurious ambiance and meticulously handcrafted beverages. Taste authentic flavors and immerse in serene tranquility in the heart of Saigon.",
          hero_cta_menu: "Explore Menu →",
          hero_cta_about: "Our Story",
          stats_items_count: "Items in Menu",
          stats_categories: "Drink Categories",
          stats_handcrafted: "Handcrafted",
          stats_days_open: "Days Open / Year",
          about_eyebrow: "● About Olion Coffee",
          about_title: 'Crafting every drop,<br><span class="accent">delivering pure elegance</span>.',
          about_desc: "When noon gets too hectic, drop by OLION, sink into your favorite armchair, admire the gentle amber glow, and enjoy a crisp iced beverage before continuing your day. More than just coffee, OLION is dedicated to a complete experience: meticulously handcrafted drinks, cozy space, and slow, meaningful moments.",
          about_feat_1_title: "Handcrafted",
          about_feat_1_desc: "Every single cup prepared with care at the bar",
          about_feat_2_title: "Selected Ingredients",
          about_feat_2_desc: "Artisan roasted beans & premium whole-leaf tea",
          about_feat_3_title: "Tranquil Space",
          about_feat_3_desc: "Cozy nook for productive work & gentle relaxation",
          about_feat_4_title: "Heartfelt Service",
          about_feat_4_desc: "Warm smiles and attentive care every day",
          sig_eyebrow: "Bestsellers",
          sig_title: 'House <span class="accent">Signature</span> Drinks',
          sig_desc: "Three exclusive recipes most beloved by guests at Olion Coffee.",
          sig_item_1_name: "JAPANESE MATCHA LATTE",
          sig_item_1_desc: "Premium ceremonial-grade Japanese matcha infused with silky fresh milk, delivering a crisp, refreshing, and calming indulgence.",
          sig_item_2_name: "MINT CACAO",
          sig_item_2_desc: "The refreshing coolness of mint perfectly blended with the gentle bitterness of pure, rich cacao.",
          sig_item_3_name: "OLION SALTED CREAM COFFEE",
          sig_item_3_desc: "Bold artisanal Robusta coffee harmoniously blended with Olion's proprietary velvety salted cream, creating an irresistible flavor journey.",
          menu_eyebrow: "● Diverse Menu",
          menu_title: 'Discover your <span class="accent">favorite drink</span>',
          menu_desc: "From bold traditional coffee and refreshing fruit teas to creamy ice-blended frappes and delightful snacks.",
          menu_tab_board: "FULL MENU",
          menu_tab_coffee: "Coffee",
          menu_tab_tea: "Fruit Tea",
          menu_tab_matcha: "Matcha",
          menu_tab_cacao: "Cacao",
          menu_tab_juice: "Juice",
          menu_tab_yagout: "Yogurt",
          menu_tab_topping: "Topping",
          spaces_eyebrow: "● Our Spaces",
          spaces_title: 'A <span class="accent">warm & cozy</span> sanctuary',
          spaces_desc: "A serene corner to work, catch up with friends, or simply gaze out at the city streets through the glass window.",
          space_card_1: "Artisanal Brew Bar",
          space_card_2: "Cozy Chat & Relax Corner",
          space_card_3: "Quiet Workspace Corner",
          space_card_4: "Panoramic Cozy Atmosphere",
          news_eyebrow: "● News & Events",
          news_title: 'Life at <span class="accent">Olion</span>',
          news_desc: "Stay updated with promotions, acoustic nights, and stories behind every cup of coffee.",
          news_read_more: "Read more →",
          faq_eyebrow: "● FAQ",
          faq_title: 'Frequently Asked <span class="accent">Questions</span>',
          faq_q1: "Does OLION COFFEE offer delivery?",
          faq_a1: "Our delivery service is currently in preparation and will launch soon! At the moment, Olion focuses on providing the best experience at the cafe or via advance table booking through our website or hotline 0783 657 587.",
          faq_q2: "What is special about OLION's ingredients and coffee?",
          faq_a2: "Olion Coffee uses 100% pure roasted Robusta & Arabica beans from Cau Dat farm, imported Japanese Matcha powder, and fresh fruit daily. We absolutely do not use artificial flavors or preservatives.",
          faq_q3: "Can I adjust the sweetness and ice level?",
          faq_a3: "Absolutely! You can ask the barista to adjust the sweetness level (0%, 30%, 50%, 70%, 100%) and ice amount as you prefer, or request a switch to Oatside oat milk to suit your diet.",
          reviews_eyebrow: "● Customer Voices",
          reviews_title: 'Guest <span class="accent">Impressions</span>',
          reviews_desc: "Heartfelt thoughts and genuine shares from friends who visit and love Olion.",
          review_1_quote: '"The cafe is nestled in a quiet alley on Duong Quang Ham, stepping in feels like you\'re separated from the hustle and bustle outside. Warm amber lights, tall wooden chairs that are comfortable to sit and work in all day. The salted coffee is perfectly balanced!"',
          review_1_role: "Van Lang University Student",
          review_2_quote: '"The matcha latte here tastes authentically Japanese, refreshingly bitter and not overly sweet like many other places. We often drop by to read books and chat on weekends because the music is set at a very comfortable volume."',
          review_2_role: "Graphic Designer",
          review_3_quote: '"The egg cream bac xiu is top-notch! The creamy egg foam is addictive. The staff is friendly and enthusiastically refills our tea constantly. Will definitely be a regular here."',
          review_3_role: "Freelancer in Go Vap",
          review_btn: "Send your feedback →",
          contact_eyebrow: "● Visit Us",
          contact_title: 'Connect with <span class="accent">Olion</span>',
          contact_addr_title: "Our Address",
          contact_hotline_title: "Hotline Booking & Support",
          contact_social_title: "Social Media Channels",
          hours_title: "Opening Hours",
          hours_weekday_label: "Mon — Sat",
          hours_weekend_label: "Sunday",
          hours_holiday_label: "Public Holidays / Tet",
          hours_holiday_val: "Open as Normal",
          hours_quote: '"When noon gets too hectic, drop by OLION, sink into your favorite armchair, admire the gentle amber glow, and enjoy a crisp iced beverage before continuing your day."',
          footer_explore: "Explore",
          footer_links: "Links",
          footer_rights: "© 2024 Olion Coffee. All rights reserved.",
          footer_credit: "Designed & Operated by Olion Creative Studio",
          loyalty_eyebrow: "Olion Member Club",
          loyalty_title: "Check Loyalty Points",
          loyalty_desc: "Enter your phone number to check your current points and available rewards!",
          loyalty_input_label: "Your Phone Number",
          loyalty_phone_placeholder: "e.g. 0908123456",
          loyalty_btn_lookup: "Check Points",
          loyalty_current_points: "Current Points",
          loyalty_pts_unit: "pts",
          wheel_float: "Spin & Win",
          back_to_top: "Back to top",
          amenities_eyebrow: '<span class="eyebrow-num">✦</span> Amenities & Workspaces',
          amenities_title: 'Perfect Amenities For <span class="accent">Work & Relaxation</span>',
          amenities_desc: 'A serene atmosphere equipped with individual table power outlets, ultra-fast 5G Wifi, and secure parking — ready to support your study sessions, deadlines, and coffee moments.'
        }
      };
      let currentLang = localStorage.getItem('olion_lang') || 'vi';
      window.setLanguage = function(lang) {
        if (!I18N_DICT[lang]) lang = 'vi';
        currentLang = lang;
        localStorage.setItem('olion_lang', lang);
        const dict = I18N_DICT[lang];
        document.querySelectorAll('[data-i18n]').forEach(el => {
          const key = el.getAttribute('data-i18n');
          if (dict[key] !== undefined) {
            el.innerHTML = dict[key];
          }
        });
        document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
          const key = el.getAttribute('data-i18n-placeholder');
          if (dict[key] !== undefined) {
            el.placeholder = dict[key];
          }
        });
        document.querySelectorAll('[data-i18n-title]').forEach(el => {
          const key = el.getAttribute('data-i18n-title');
          if (dict[key] !== undefined) {
            el.setAttribute('title', dict[key]);
            el.setAttribute('aria-label', dict[key]);
          }
        });
        const isVi = lang === 'vi';
        const pillVi = document.getElementById('langPillVi');
        const pillEn = document.getElementById('langPillEn');
        const pillViMobile = document.getElementById('langPillViMobile');
        const pillEnMobile = document.getElementById('langPillEnMobile');
        if (pillVi) pillVi.classList.toggle('active', isVi);
        if (pillEn) pillEn.classList.toggle('active', !isVi);
        if (pillViMobile) pillViMobile.classList.toggle('active', isVi);
        if (pillEnMobile) pillEnMobile.classList.toggle('active', !isVi);
        document.documentElement.setAttribute('lang', lang);
        if (typeof window.updateDynamicGreeting === 'function') {
          window.updateDynamicGreeting(lang);
        }
      };
      window.copyWifiPassword = function() {
        const pass = document.getElementById('wifiPassCodeVal')?.textContent.trim() || '12345678@';
        const msg = currentLang === 'vi' ? 'Đã sao chép mật khẩu Wifi: ' + pass : 'Wifi password copied: ' + pass;
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(pass).then(() => {
            if (window.showOlionToast) {
              window.showOlionToast(msg, 'wifi');
            }
          }).catch(() => {
            fallbackWifiCopy(pass, msg);
          });
        } else {
          fallbackWifiCopy(pass, msg);
        }
      };
      function fallbackWifiCopy(text, toastMsg) {
        const temp = document.createElement('textarea');
        temp.value = text;
        temp.style.position = 'fixed';
        temp.style.left = '-9999px';
        document.body.appendChild(temp);
        temp.select();
        try {
          document.execCommand('copy');
          if (window.showOlionToast) {
            window.showOlionToast(toastMsg, 'wifi');
          }
        } catch(e) {
          if (window.showOlionToast) {
            window.showOlionToast('Mật khẩu Wifi: ' + text, 'wifi');
          }
        }
        document.body.removeChild(temp);
      }
      try {
        let visits = parseInt(localStorage.getItem('olion_visit_count') || '0', 10) + 1;
        localStorage.setItem('olion_visit_count', visits.toString());
      } catch(e) {}
      function getGreetingData(lang = currentLang) {
        const now = new Date();
        const hour = now.getHours();
        const minute = now.getMinutes();
        const timeNum = hour + minute / 60;
        let customerName = '';
        try {
          customerName = (localStorage.getItem('olion_customer_name') || '').trim();
          if (!customerName) {
            const fb = JSON.parse(localStorage.getItem('olion_feedbacks') || '[]');
            if (fb.length > 0 && fb[0].name && fb[0].name !== 'Khách ghé quán') {
              customerName = fb[0].name.trim();
            }
          }
        } catch(e) {}
        const isVi = lang === 'vi';
        const prefix = customerName ? (isVi ? `Chào ${customerName}! ` : `Hi ${customerName}! `) : '';
        if (timeNum >= 6 && timeNum < 10.5) {
          return {
            icon: 'sunrise',
            tag: isVi ? 'Chào Buổi Sáng' : 'Good Morning',
            quote: isVi
              ? `${prefix}"Sáng sớm trong lành, ghé OLION nhâm nhi một tách cà phê thơm nồng, khởi động ngày mới tràn đầy hứng khởi và năng lượng tích cực nhé!"`
              : `${prefix}"Crisp morning air pairs best with a fragrant brew at OLION. Kick off your brand-new day filled with positive energy and clarity!"`
          };
        }
        else if (timeNum >= 10.5 && timeNum < 13.5) {
          return {
            icon: 'sun',
            tag: isVi ? 'Buổi Trưa Mát Lành' : 'Midday Cool Breeze',
            quote: isVi
              ? `${prefix}"Trời trưa hơi gắt, ghé OLION thả lưng xuống chiếc ghế quen, ngắm ánh đèn vàng dịu mắt và làm ngụm nước mát lạnh rồi tỉnh tiếp nha."`
              : `${prefix}"When the midday sun gets a bit intense, find your nook at OLION, unwind in a cozy chair, and recharge with an icy crisp beverage."`
          };
        }
        else if (timeNum >= 13.5 && timeNum < 17.0) {
          return {
            icon: 'sun-medium',
            tag: isVi ? 'Xế Chiều Năng Lượng' : 'Afternoon Boost',
            quote: isVi
              ? `${prefix}"Đầu giờ chiều hơi uể oải, hãy tự thưởng cho mình một ly Trà Trái Cây mát lạnh hoặc Cà Phê Muối đậm vị để nạp lại 100% cảm hứng làm việc nhé."`
              : `${prefix}"Beat the afternoon slump with a refreshing fruit tea or our signature salted cream coffee. 100% inspiration restored!"`
          };
        }
        else if (timeNum >= 17.0 && timeNum < 19.0) {
          return {
            icon: 'sunset',
            tag: isVi ? 'Chiều Tà Thảnh Thơi' : 'Golden Hour Dusk',
            quote: isVi
              ? `${prefix}"Tan ca rồi, bỏ lại sau lưng mọi deadline bộn bề. Ghé OLION chuyện trò cùng bạn bè hoặc ngắm phố xá lên đèn bên ly Bạc Xỉu ngọt ngào nhé."`
              : `${prefix}"Clock-out time! Leave the deadlines behind, gather with friends, or watch the city lights awaken over a sweet, soothing egg-foam coffee."`
          };
        }
        else if (timeNum >= 19.0 && timeNum < 21.5) {
          return {
            icon: 'moon',
            tag: isVi ? 'Buổi Tối Ấm Cúng' : 'Cozy Evening Vibe',
            quote: isVi
              ? `${prefix}"Phố xá về đêm thật đẹp. Trong không gian đèn vàng ấm cúng và giai điệu nhạc êm đềm tại OLION, cùng nhâm nhi ly nước yêu thích và chill thôi nào."`
              : `${prefix}"The city glimmers at night. Sink into our warm amber glow, enjoy mellow acoustic tunes, and savor your favorite handcrafted drink."`
          };
        }
        else {
          return {
            icon: 'sparkles',
            tag: isVi ? 'Chúc Bạn Ngủ Ngon' : 'Good Night & Sweet Dreams',
            quote: isVi
              ? `${prefix}"OLION đã khép lại sau một ngày phục vụ thân thương. Chúc bạn một giấc ngủ thật ngon và hẹn gặp lại bạn vào sớm mai với những tách cà phê thơm lừng!"`
              : `${prefix}"OLION has closed for the night. Rest well tonight, and we look forward to welcoming you tomorrow morning with fresh artisanal brews!"`
          };
        }
      }
      window.updateDynamicGreeting = function(lang = currentLang) {
        const box = document.getElementById('dynamicQuoteBox');
        if (!box) return;
        const data = getGreetingData(lang);
        const iconEl = document.getElementById('quoteIcon');
        const tagEl = document.getElementById('quoteTimeLabel');
        const textEl = document.getElementById('quoteText');
        if (iconEl) {
          iconEl.innerHTML = `<i data-lucide="${data.icon}" style="width:16px;height:16px;"></i>`;
          if (window._lucideReady && window.lucide) window.lucide.createIcons();
        }
        if (tagEl) tagEl.textContent = data.tag;
        if (textEl) textEl.textContent = data.quote;
      };
      window.toggleLanguage = function() {
        const next = currentLang === 'vi' ? 'en' : 'vi';
        window.setLanguage(next);
        if (window.showOlionToast) {
          window.showOlionToast(next === 'vi' ? 'Đã đổi sang Tiếng Việt 🇻🇳' : 'Switched to English 🇬🇧', '🌐');
        }
      };
      setLanguage(currentLang);
      updateDynamicGreeting(currentLang);
      setInterval(() => {
        if (typeof window.updateDynamicGreeting === 'function') {
          window.updateDynamicGreeting(currentLang);
        }
      }, 5 * 60 * 1000);
      let welcomeAutoCloseTimer = null;
      let weatherDataCache = null;
      const HCM_DISTRICT_COORDS = [
        { name: 'Gò Vấp', lat: 10.8386, lon: 106.6653, isHome: true },
        { name: 'Bình Thạnh', lat: 10.8106, lon: 106.7091 },
        { name: 'Phú Nhuận', lat: 10.7992, lon: 106.6802 },
        { name: 'Tân Bình', lat: 10.8015, lon: 106.6550 },
        { name: 'Tân Phú', lat: 10.7900, lon: 106.6280 },
        { name: 'Quận 12', lat: 10.8672, lon: 106.6412 },
        { name: 'Thủ Đức', lat: 10.8494, lon: 106.7537 },
        { name: 'Quận 1', lat: 10.7756, lon: 106.7004 },
        { name: 'Quận 3', lat: 10.7844, lon: 106.6844 },
        { name: 'Quận 10', lat: 10.7716, lon: 106.6674 },
        { name: 'Quận 5', lat: 10.7554, lon: 106.6631 },
        { name: 'Quận 7', lat: 10.7340, lon: 106.7218 },
        { name: 'Bình Tân', lat: 10.7653, lon: 106.6037 },
        { name: 'Hóc Môn', lat: 10.8841, lon: 106.5925 }
      ];
      function calculateNearestDistrict(lat, lon) {
        let bestDistrict = 'TP.HCM';
        let minDist = 999999;
        let isHome = false;
        HCM_DISTRICT_COORDS.forEach(d => {
          const dist = Math.hypot(lat - d.lat, lon - d.lon);
          if (dist < minDist) {
            minDist = dist;
            bestDistrict = d.name;
            isHome = Boolean(d.isHome);
          }
        });
        if (minDist > 0.4) {
          return { district: 'TP.HCM', isHome: false, isNear: false };
        }
        return {
          district: bestDistrict,
          isHome: isHome || bestDistrict === 'Gò Vấp',
          isNear: ['Gò Vấp', 'Bình Thạnh', 'Phú Nhuận', 'Tân Bình', 'Quận 12', 'Tân Phú'].includes(bestDistrict)
        };
      }
      async function fetchHyperLocalWeather() {
        let lat = 10.8231;
        let lon = 106.6297;
        let locationName = 'TP.HCM';
        let isHome = false;
        let isNear = true;
        try {
          const geoRes = await fetch('https://get.geojs.io/v1/ip/geo.json');
          if (geoRes.ok) {
            const geoData = await geoRes.json();
            if (geoData.latitude && geoData.longitude) {
              lat = parseFloat(geoData.latitude);
              lon = parseFloat(geoData.longitude);
              const districtInfo = calculateNearestDistrict(lat, lon);
              locationName = districtInfo.district;
              isHome = districtInfo.isHome;
              isNear = districtInfo.isNear;
            }
          }
        } catch (err) {
        }
        try {
          const res = await fetch(`https://api.open-meteo.com/v1/forecast?latitude=${lat}&longitude=${lon}&current=temperature_2m,weather_code,is_day,relative_humidity_2m&timezone=Asia%2FHo_Chi_Minh`);
          if (!res.ok) throw new Error('Weather fetch failed');
          const data = await res.json();
          const temp = Math.round(data.current.temperature_2m);
          const code = data.current.weather_code;
          const isDay = data.current.is_day;
          let statusText = 'trời đẹp';
          let icon = isDay ? 'sun' : 'moon';
          let isRain = false;
          let isHot = temp >= 32;
          if (code === 0) {
            statusText = isDay ? 'trời nắng trong' : 'trời quang đãng';
            icon = isDay ? 'sun' : 'sparkles';
          } else if ([1, 2, 3].includes(code)) {
            statusText = 'trời mát mẻ có mây';
            icon = 'cloud-sun';
          } else if ([51, 53, 55, 61, 63, 65, 80, 81, 82].includes(code)) {
            statusText = 'trời đang mưa rào';
            icon = 'cloud-rain';
            isRain = true;
          } else if ([95, 96, 99].includes(code)) {
            statusText = 'trời có dông mưa';
            icon = 'cloud-lightning';
            isRain = true;
          }
          weatherDataCache = {
            temp,
            statusText,
            icon,
            isRain,
            isHot,
            locationName,
            isHome,
            isNear
          };
          return weatherDataCache;
        } catch (e) {
          weatherDataCache = {
            temp: 27,
            statusText: 'mát dịu',
            icon: 'sun-medium',
            isRain: false,
            isHot: false,
            locationName,
            isHome,
            isNear
          };
          return weatherDataCache;
        }
      }
      function generateSmartWelcomeMessage(name, weather) {
        const now = new Date();
        const hour = now.getHours();
        const { temp, statusText, isRain, isHot, locationName, isHome } = weather;
        let timeSlot = '';
        let greetingPrefix = name ? `Chào ${name}` : `Chào bạn`;
        let recommendation = '';
        if (hour >= 5 && hour < 8) {
          timeSlot = 'Sáng Sớm';
          if (isRain) {
            recommendation = `Khu vực ${locationName} sáng sớm trời mưa nhẹ ${temp}°C. Ghé Olion trú mưa nhâm nhi tách Cà phê nóng đánh thức mọi giác quan nhé!`;
          } else {
            recommendation = isHome
              ? `Sáng sớm Gò Vấp trong lành ${temp}°C! Quán ở 80/64A Dương Quảng Hàm rất gần bạn đấy, ghé Olion làm ly Espresso pha thủ công thức tỉnh ngày mới nhé.`
              : `Sáng sớm tại ${locationName} thật trong lành (${temp}°C). Một ly Cà phê mộc pha thủ công tại Olion sẽ nạp đầy năng lượng cho bạn!`;
          }
        } else if (hour >= 8 && hour < 11) {
          timeSlot = 'Buổi Sáng';
          if (isRain) {
            recommendation = `Trời ${locationName} đang mưa rào (${temp}°C). Trú mưa tại góc quán ấm cúng Olion cùng một ly Cà Phê Muối béo mặn nhé!`;
          } else {
            recommendation = isHome
              ? `Buổi sáng Gò Vấp đầy hứng khởi (${temp}°C, ${statusText})! Ghé ngay 80/64A Dương Quảng Hàm nạp năng lượng với Cà Phê Muối hay Bạc Xỉu Olion nha.`
              : `Buổi sáng tại ${locationName} ngập tràn hứng khởi (${temp}°C, ${statusText}). Nạp 100% năng lượng ngày mới cùng Cà Phê Muối độc quyền Olion!`;
          }
        } else if (hour >= 11 && hour < 14) {
          timeSlot = 'Buổi Trưa';
          if (isHot) {
            recommendation = `Trời ${locationName} trưa nay khá oi bức (${temp}°C). Ghé Olion trốn nắng trong không gian mát lành và thưởng thức ly Trà Trái Cây mát lạnh giải nhiệt tức thì!`;
          } else {
            recommendation = isHome
              ? `Trưa nay ở Gò Vấp (${temp}°C), ghé Olion thả lưng xuống chiếc ghế quen, ngắm ánh đèn vàng dịu mắt và làm ngụm nước mát lạnh rồi tiếp tục ngày dài nhé.`
              : `Trời trưa ${locationName} êm dịu ${temp}°C. Ghé Olion thả lưng xuống chiếc ghế quen, thưởng thức đồ uống mát lạnh và nạp lại năng lượng nhé.`;
          }
        } else if (hour >= 14 && hour < 17) {
          timeSlot = 'Xế Chiều';
          if (isRain) {
            recommendation = `Chiều ${locationName} có mưa lất phất (${temp}°C). Một ly Matcha Latte ấm thơm sẽ giúp bạn thư giãn và xua tan mệt mỏi!`;
          } else {
            recommendation = `Xế chiều tại ${locationName} dễ uể oải (${temp}°C). Tự thưởng cho mình một ly Matcha Latte thanh mát hay Trà Đào thanh dịu để lấy lại cảm hứng làm việc nhé!`;
          }
        } else if (hour >= 17 && hour < 19) {
          timeSlot = 'Chiều Tối';
          recommendation = isHome
            ? `Tan tầm rồi! Gác lại deadline, ghé ngay Olion 80/64A Dương Quảng Hàm (${temp}°C) ngắm phố xá lên đèn và thưởng thức ly Bạc Xỉu ngọt ngào xả stress nhé.`
            : `Tan tầm rồi (${locationName} ${temp}°C)! Gác lại mọi deadline, cùng bạn bè ghé Olion ngắm phố xá lên đèn và thưởng thức ly Bạc Xỉu ngọt ngào xả stress thôi nào.`;
        } else if (hour >= 19 && hour < 22) {
          timeSlot = 'Buổi Tối';
          recommendation = `Phố đêm ${locationName} lung linh trong tiết trời ${temp}°C dễ chịu. Không gian đèn vàng ấm cúng và những giai điệu êm dịu tại Olion đang chờ bạn ghé chơi.`;
        } else {
          timeSlot = 'Đêm Muộn';
          recommendation = `Đêm muộn tại ${locationName} thật yên tĩnh (${temp}°C). Chúc bạn một buổi tối an lành, thư thái và có một giấc ngủ thật ngon nhé!`;
        }
        return {
          timeSlot,
          title: name ? `Chào mừng ${name} trở lại!` : `Chào mừng bạn ghé chơi!`,
          message: `${greetingPrefix}! ${recommendation}`
        };
      }
      async function initSmartWelcomePopup() {
        if (/Lighthouse|HeadlessChrome|Chrome-Lighthouse|bot/i.test(navigator.userAgent) || window.location.search.includes('no_welcome')) {
          return;
        }
        await new Promise(r => setTimeout(r, 3500));
        const modal = document.getElementById('welcomeModal');
        if (!modal) return;
        const weather = await fetchHyperLocalWeather();
        const customerName = (localStorage.getItem('olion_customer_name') || '').trim();
        const isReturning = Boolean(customerName);
        const smartData = generateSmartWelcomeMessage(customerName, weather);
        const iconEl = document.getElementById('welcomeWeatherIcon');
        const textEl = document.getElementById('welcomeWeatherText');
        const titleEl = document.getElementById('welcomeTitle');
        const msgEl = document.getElementById('welcomeMessage');
        if (iconEl) {
          iconEl.innerHTML = `<i data-lucide="${weather.icon}" style="width:18px;height:18px;"></i>`;
          if (window.lucide) window.lucide.createIcons();
        }
        if (textEl) textEl.textContent = `${weather.locationName} ${weather.temp}°C • ${smartData.timeSlot}`;
        if (titleEl) titleEl.textContent = smartData.title;
        if (msgEl) msgEl.textContent = smartData.message;
        const newUserArea = document.getElementById('welcomeNewUserArea');
        const returningArea = document.getElementById('welcomeReturningUserArea');
        const progressBar = document.getElementById('welcomeProgressBar');
        if (isReturning) {
          if (newUserArea) newUserArea.style.display = 'none';
          if (returningArea) returningArea.style.display = 'block';
          if (progressBar) progressBar.style.display = 'block';
          startWelcomeCountdown(10000);
        } else {
          if (newUserArea) newUserArea.style.display = 'block';
          if (returningArea) returningArea.style.display = 'none';
          if (progressBar) progressBar.style.display = 'none';
          clearTimeout(welcomeAutoCloseTimer);
          welcomeAutoCloseTimer = null;
        }
        modal.classList.add('active');
        modal.setAttribute('aria-hidden', 'false');
        const welcomeBox = document.getElementById('welcomeBox') || modal.querySelector('.welcome-box');
        if (welcomeBox) {
          const pauseEvents = ['focusin', 'click', 'keydown', 'touchstart', 'input', 'mouseenter'];
          pauseEvents.forEach(evt => {
            welcomeBox.addEventListener(evt, pauseWelcomeCountdown, { passive: true });
          });
        }
        const nameInput = document.getElementById('welcomeName');
        const phoneInput = document.getElementById('welcomePhone');
        if (nameInput) {
          nameInput.addEventListener('focus', pauseWelcomeCountdown, { passive: true });
          nameInput.addEventListener('input', pauseWelcomeCountdown, { passive: true });
        }
        if (phoneInput) {
          phoneInput.addEventListener('focus', pauseWelcomeCountdown, { passive: true });
          phoneInput.addEventListener('input', pauseWelcomeCountdown, { passive: true });
        }
      }
      function startWelcomeCountdown(duration = 10000) {
        const progressBar = document.getElementById('welcomeProgressBar');
        if (progressBar) {
          progressBar.classList.remove('paused');
          progressBar.style.animation = 'none';
          requestAnimationFrame(() => {
            requestAnimationFrame(() => {
              if (progressBar) {
                progressBar.style.animation = `welcomeCountdown ${duration / 1000}s linear forwards`;
                progressBar.style.display = 'block';
              }
            });
          });
        }
        clearTimeout(welcomeAutoCloseTimer);
        welcomeAutoCloseTimer = setTimeout(() => {
          closeWelcomeModal();
        }, duration);
      }
      function pauseWelcomeCountdown() {
        if (welcomeAutoCloseTimer) {
          clearTimeout(welcomeAutoCloseTimer);
          welcomeAutoCloseTimer = null;
        }
        const progressBar = document.getElementById('welcomeProgressBar');
        if (progressBar) {
          progressBar.classList.add('paused');
          progressBar.style.display = 'none';
        }
      }
      window.closeWelcomeModal = function() {
        const modal = document.getElementById('welcomeModal');
        if (!modal) return;
        modal.classList.remove('active');
        modal.setAttribute('aria-hidden', 'true');
        clearTimeout(welcomeAutoCloseTimer);
        welcomeAutoCloseTimer = null;
      };
      window.welcomeExploreMenu = function() {
        closeWelcomeModal();
        const menuSec = document.getElementById('menu');
        if (menuSec) {
          menuSec.scrollIntoView({ behavior: 'smooth' });
        }
      };
      window.handleWelcomeSubmit = async function(e) {
        e.preventDefault();
        const nameInput = document.getElementById('welcomeName');
        const phoneInput = document.getElementById('welcomePhone');
        const submitBtn = document.getElementById('welcomeSubmitBtn');
        const name = (nameInput?.value || '').trim();
        const phone = (phoneInput?.value || '').trim();
        const phoneRegex = /^(03|05|07|08|09)[0-9]{8}$/;
        if (!phoneRegex.test(phone)) {
          if (window.showOlionToast) window.showOlionToast('Vui lòng nhập đúng số điện thoại (10 số)!', 'alert-circle');
          phoneInput?.focus();
          return;
        }
        if (submitBtn) {
          submitBtn.disabled = true;
          submitBtn.textContent = 'Đang lưu...';
        }
        try {
          localStorage.setItem('olion_customer_name', name);
          localStorage.setItem('olion_customer_phone', phone);
        } catch(err) {}
        try {
          const client = window.supabaseClient || (typeof initSupabase === 'function' ? initSupabase() : null);
          if (client) {
            await client.from('customers').upsert([{
              name: name,
              contact: phone,
              source: 'Smart Welcome Popup',
              notes: `Đăng ký qua Smart Welcome Popup lúc ${new Date().toLocaleString('vi-VN')}`
            }], { onConflict: 'contact' });
          }
        } catch (err) {
          console.warn('Supabase customer insert error:', err);
        }
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.textContent = 'Bắt đầu trải nghiệm';
        }
        closeWelcomeModal();
        if (window.showOlionToast) {
          window.showOlionToast(`Chào mừng ${name} đến với OLION COFFEE!`, 'coffee');
        }
        if (typeof window.updateDynamicGreeting === 'function') {
          window.updateDynamicGreeting();
        }
      };
      document.getElementById('welcomeModal')?.addEventListener('click', (e) => {
        if (e.target === document.getElementById('welcomeModal')) {
          closeWelcomeModal();
        }
      });
      const deferWelcomePopup = () => {
        if ('requestIdleCallback' in window) {
          requestIdleCallback(() => setTimeout(initSmartWelcomePopup, 1200), { timeout: 3000 });
        } else {
          setTimeout(initSmartWelcomePopup, 2000);
        }
      };
      if (document.readyState === 'complete') {
        deferWelcomePopup();
      } else {
        window.addEventListener('load', deferWelcomePopup, { passive: true });
      }
      const loyaltyModal = document.getElementById('loyaltyLookupModal');
      const loyaltyPhoneInput = document.getElementById('loyaltySearchPhone');
      const loyaltyResultCard = document.getElementById('loyaltyResultCard');
      const loyaltyErrorCard = document.getElementById('loyaltyErrorCard');
      const loyaltySearchBtn = document.getElementById('loyaltySearchBtn');
      window.openLoyaltyModal = function(initialPhone = '') {
        if (!loyaltyModal) return;
        loyaltyModal.classList.add('active');
        loyaltyModal.setAttribute('aria-hidden', 'false');
        document.body.style.overflow = 'hidden';
        if (loyaltyResultCard) loyaltyResultCard.style.display = 'none';
        if (loyaltyErrorCard) loyaltyErrorCard.style.display = 'none';
        if (loyaltyPhoneInput) {
          loyaltyPhoneInput.value = initialPhone;
          setTimeout(() => loyaltyPhoneInput?.focus(), 150);
          if (initialPhone) {
            handleLoyaltyLookup();
          }
        }
      };
      window.closeLoyaltyModal = function() {
        if (!loyaltyModal) return;
        loyaltyModal.classList.remove('active');
        loyaltyModal.setAttribute('aria-hidden', 'true');
        document.body.style.overflow = '';
      };
      if (loyaltyModal) {
        loyaltyModal.addEventListener('click', (e) => {
          if (e.target === loyaltyModal) closeLoyaltyModal();
        });
      }
      window.handleLoyaltyLookup = async function(e) {
        if (e && e.preventDefault) e.preventDefault();
        const phone = (loyaltyPhoneInput ? loyaltyPhoneInput.value : '').trim();
        if (!phone) {
          if (loyaltyErrorCard) {
            loyaltyErrorCard.textContent = currentLang === 'vi' ? 'Vui lòng nhập số điện thoại để tra cứu.' : 'Please enter your phone number.';
            loyaltyErrorCard.style.display = 'block';
          }
          return;
        }
        if (loyaltySearchBtn) {
          loyaltySearchBtn.disabled = true;
          loyaltySearchBtn.textContent = currentLang === 'vi' ? 'Đang tìm...' : 'Searching...';
        }
        if (loyaltyErrorCard) loyaltyErrorCard.style.display = 'none';
        if (loyaltyResultCard) loyaltyResultCard.style.display = 'none';
        try {
          let res = null;
          if (window.lookupLoyaltyMember) {
            res = await window.lookupLoyaltyMember(phone);
          } else {
            const local = JSON.parse(localStorage.getItem('olion_loyalty_members') || '[]');
            const m = local.find(x => x.phone_number === phone);
            res = m ? { success: true, member: m } : { success: false, not_found: true };
          }
          if (res && res.success && res.member) {
            const m = res.member;
            const pts = Number(m.points) || 0;
            const visits = Number(m.total_visits) || 1;
            document.getElementById('loyaltyResName').textContent = m.customer_name || (currentLang === 'vi' ? 'Khách hàng thân thiết' : 'Loyal Member');
            document.getElementById('loyaltyResPhone').textContent = m.phone_number;
            document.getElementById('loyaltyResPoints').innerHTML = `${pts} <span style="font-size: 13px; font-weight: 600;">${currentLang === 'vi' ? 'điểm' : 'pts'}</span>`;
            let tierName = 'Thành viên';
            if (pts >= 200) tierName = 'Kim Cương';
            else if (pts >= 100) tierName = 'Hạng Vàng';
            else if (pts >= 50) tierName = 'Hạng Bạc';
            document.getElementById('loyaltyResTier').textContent = tierName;
            document.getElementById('loyaltyResVisits').textContent = currentLang === 'vi' ? `Đã ghé: ${visits} lần` : `Visits: ${visits} times`;
            const target = 100;
            const pct = Math.min(100, Math.round((pts / target) * 100));
            document.getElementById('loyaltyProgressBar').style.width = `${pct}%`;
            document.getElementById('loyaltyRewardTarget').textContent = `${pts} / ${target} ${currentLang === 'vi' ? 'điểm' : 'pts'}`;
            const statusEl = document.getElementById('loyaltyRewardStatus');
            const noticeEl = document.getElementById('loyaltyRewardNotice');
            if (pts >= 100) {
              statusEl.textContent = currentLang === 'vi' ? 'ĐỦ ĐIỀU KIỆN ĐỔI LY SIGNATURE MIỄN PHÍ' : 'READY FOR FREE SIGNATURE DRINK';
              noticeEl.innerHTML = currentLang === 'vi'
                ? `Chúc mừng bạn! Bạn đang có <strong>${pts} điểm</strong>, đủ điều kiện đổi 1 ly Signature miễn phí (Matcha Quế Hoa, Cacao Bạc Hà, Bạc Xỉu). Hãy thông báo cho thu ngân khi thanh toán nhé!`
                : `Congratulations! You have <strong>${pts} points</strong>, eligible for a free Signature drink. Please 🌟rm our cashier when ordering!`;
            } else {
              const diff = target - pts;
              statusEl.textContent = currentLang === 'vi' ? 'Đổi 1 ly Signature miễn phí' : 'Redeem 1 Free Signature Drink';
              noticeEl.innerHTML = currentLang === 'vi'
                ? `Bạn đang có <strong>${pts} điểm</strong>. Cần thêm <strong>${diff} điểm</strong> nữa để đổi 1 ly Signature miễn phí (100 điểm).`
                : `You currently have <strong>${pts} points</strong>. Need <strong>${diff} more points</strong> to redeem a free Signature drink (100 pts).`;
            }
            loyaltyResultCard.style.display = 'block';
          } else {
            loyaltyErrorCard.textContent = (res && res.message) || (currentLang === 'vi'
              ? 'Chưa tìm thấy thông tin tích điểm với số điện thoại này. Bạn hãy ghé quán order đồ uống để bắt đầu tích điểm nhé!'
              : 'No loyalty member found with this phone number. Visit our cafe and order to start earning points!');
            loyaltyErrorCard.style.display = 'block';
          }
        } catch (err) {
          loyaltyErrorCard.textContent = currentLang === 'vi' ? 'Có lỗi xảy ra khi tra cứu. Vui lòng thử lại sau.' : 'An error occurred. Please try again.';
          loyaltyErrorCard.style.display = 'block';
        } finally {
          if (loyaltySearchBtn) {
            loyaltySearchBtn.disabled = false;
            loyaltySearchBtn.textContent = currentLang === 'vi' ? 'Tra Cứu' : 'Check Points';
          }
        }
      };
      const scrollProgress = document.getElementById('scrollProgress');
      const siteHeader = document.getElementById('siteHeader');
      const backToTopBtn = document.getElementById('backToTopBtn');
      const backToTopProgress = document.getElementById('backToTopProgress');
      const ringCircumference = 2 * Math.PI * 20; // 125.66px
      let scrollTicking = false;
      window.addEventListener('scroll', () => {
        if (!scrollTicking) {
          window.requestAnimationFrame(() => {
            const winScroll = window.scrollY || document.documentElement.scrollTop;
            const height = document.documentElement.scrollHeight - window.innerHeight;
            const scrolled = height > 0 ? (winScroll / height) * 100 : 0;
            if (scrollProgress) scrollProgress.style.width = scrolled + '%';
            if (siteHeader) {
              siteHeader.classList.toggle('scrolled', winScroll > 60);
            }
            if (backToTopBtn) {
              backToTopBtn.classList.toggle('is-visible', winScroll > 320);
              if (backToTopProgress && height > 0) {
                const offset = ringCircumference - (scrolled / 100) * ringCircumference;
                backToTopProgress.style.strokeDashoffset = Math.max(0, offset);
              }
            }
            scrollTicking = false;
          });
          scrollTicking = true;
        }
      }, { passive: true });
      if (backToTopBtn) {
        backToTopBtn.addEventListener('click', (e) => {
          e.preventDefault();
          window.scrollTo({
            top: 0,
            behavior: 'smooth'
          });
        });
      }
      const burgerBtn = document.getElementById('burgerBtn');
      const mobileDrawer = document.getElementById('mobileDrawer');
      const drawerOverlay = document.getElementById('drawerOverlay');
      const drawerClose = document.getElementById('drawerClose');
      window.toggleDrawer = function(open = null) {
        if (!mobileDrawer || !drawerOverlay) return;
        const isOpen = open !== null ? open : !mobileDrawer.classList.contains('active');
        mobileDrawer.classList.toggle('active', isOpen);
        drawerOverlay.classList.toggle('active', isOpen);
        document.body.style.overflow = isOpen ? 'hidden' : '';
      };
      if (burgerBtn) burgerBtn.addEventListener('click', () => toggleDrawer(true));
      if (drawerClose) drawerClose.addEventListener('click', () => toggleDrawer(false));
      if (drawerOverlay) drawerOverlay.addEventListener('click', () => toggleDrawer(false));
      document.querySelectorAll('.drawer-link').forEach(link => {
        link.addEventListener('click', () => toggleDrawer(false));
      });
      const heroSlides = document.querySelectorAll('.hero-slide');
      const heroDots = document.querySelectorAll('.hero-dot');
      let heroCurrent = 0;
      let heroTimer = null;
      function setHeroSlide(index) {
        heroSlides.forEach((s, i) => s.classList.toggle('active', i === index));
        heroDots.forEach((d, i) => d.classList.toggle('active', i === index));
        heroCurrent = index;
      }
      function nextHeroSlide() {
        const nextIndex = (heroCurrent + 1) % heroSlides.length;
        setHeroSlide(nextIndex);
      }
      heroDots.forEach((dot, index) => {
        dot.addEventListener('click', () => {
          clearInterval(heroTimer);
          setHeroSlide(index);
          heroTimer = setInterval(nextHeroSlide, 5000);
        });
      });
      if (heroSlides.length > 1) {
        heroTimer = setInterval(nextHeroSlide, 5000);
      }
      const menuTabBtns = document.querySelectorAll('.menu-tab-btn[data-cat]');
      const menuPanels = document.querySelectorAll('.menu-category-panel');
      const openMenuBoardBtn = document.getElementById('openMenuBoardBtn');
      const menuBoardModal = document.getElementById('menuBoardModal');
      const menuBoardCloseBtn = document.getElementById('menuBoardCloseBtn');
      const menuBoardViewport = document.getElementById('menuBoardViewport');
      const menuBoardImg = document.getElementById('menuBoardImg');
      const menuBoardZoomBtn = document.getElementById('menuBoardZoomBtn');
      const menuBoardZoomText = document.getElementById('menuBoardZoomText');
      menuTabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
          const targetCat = btn.getAttribute('data-cat');
          if (!targetCat) return;
          menuTabBtns.forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          menuPanels.forEach(panel => {
            panel.classList.toggle('active', panel.id === `cat-${targetCat}`);
          });
        });
      });
      window.openMenuBoard = function() {
        if (!menuBoardModal) return;
        menuBoardModal.classList.add('active');
        menuBoardModal.setAttribute('aria-hidden', 'false');
        document.body.style.overflow = 'hidden';
      };
      window.closeMenuBoard = function() {
        if (!menuBoardModal) return;
        menuBoardModal.classList.remove('active');
        menuBoardModal.setAttribute('aria-hidden', 'true');
        if (menuBoardViewport) menuBoardViewport.classList.remove('zoomed');
        if (menuBoardZoomText) menuBoardZoomText.textContent = 'Phóng to';
        document.body.style.overflow = '';
      };
      window.toggleMenuBoardZoom = function() {
        if (!menuBoardViewport) return;
        const isZoomed = menuBoardViewport.classList.toggle('zoomed');
        if (menuBoardZoomText) menuBoardZoomText.textContent = isZoomed ? 'Thu nhỏ' : 'Phóng to';
      };
      if (openMenuBoardBtn) openMenuBoardBtn.addEventListener('click', openMenuBoard);
      if (menuBoardCloseBtn) menuBoardCloseBtn.addEventListener('click', closeMenuBoard);
      if (menuBoardZoomBtn) menuBoardZoomBtn.addEventListener('click', toggleMenuBoardZoom);
      if (menuBoardImg) {
        menuBoardImg.addEventListener('click', (e) => {
          e.stopPropagation();
          toggleMenuBoardZoom();
        });
      }
      if (menuBoardViewport) {
        menuBoardViewport.addEventListener('click', (e) => {
          if (e.target === menuBoardViewport) closeMenuBoard();
        });
      }
      document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && menuBoardModal && menuBoardModal.classList.contains('active')) {
          closeMenuBoard();
        }
      });
      document.querySelectorAll('.faq-trigger').forEach(trigger => {
        trigger.addEventListener('click', () => {
          const item = trigger.closest('.faq-item');
          const isActive = item.classList.contains('active');
          document.querySelectorAll('.faq-item').forEach(i => {
            i.classList.remove('active');
            i.querySelector('.faq-trigger')?.setAttribute('aria-expanded', 'false');
          });
          if (!isActive) {
            item.classList.add('active');
            trigger.setAttribute('aria-expanded', 'true');
          }
        });
      });
      let olionToastTimer = null;
      window.showOlionToast = function(msg, icon = '✨') {
        const toast = document.getElementById('olionToast');
        const toastMsg = document.getElementById('olionToastMsg');
        const toastIcon = document.getElementById('olionToastIcon');
        if (!toast || !toastMsg) {
          alert(msg);
          return;
        }
        toastMsg.textContent = msg;
        if (toastIcon) toastIcon.textContent = icon;
        toast.classList.add('show');
        if (olionToastTimer) clearTimeout(olionToastTimer);
        olionToastTimer = setTimeout(() => {
          toast.classList.remove('show');
        }, 4000);
      };
      let currentBookingType = 'space'; // 'space' or 'table'
      window.lastFormattedBookingMsg = '';
      window.openBookingModal = function(type = 'space', customNote = '') {
        const modal = document.getElementById('bookingModal');
        if (!modal) return;
        const formArea = document.getElementById('bkFormArea');
        const successArea = document.getElementById('bkSuccessArea');
        if (formArea) formArea.style.display = 'block';
        if (successArea) successArea.style.display = 'none';
        const nameInput = document.getElementById('bkName');
        const phoneInput = document.getElementById('bkPhone');
        if (nameInput && !nameInput.value) {
          nameInput.value = localStorage.getItem('olion_customer_name') || '';
        }
        if (phoneInput && !phoneInput.value) {
          phoneInput.value = localStorage.getItem('olion_customer_phone') || '';
        }
        const timeSelect = document.getElementById('bkTime');
        const customWrap = document.getElementById('bkCustomTimeWrap');
        const customInput = document.getElementById('bkCustomTime');
        if (customWrap) customWrap.style.display = 'none';
        if (customInput) customInput.value = '';
        if (timeSelect) timeSelect.value = "10:00 - 12:00";
        window.selectBookingType(type);
        if (customNote) {
          const noteEl = document.getElementById('bkNote');
          if (noteEl) noteEl.value = customNote;
        }
        const dateInput = document.getElementById('bkDate');
        if (dateInput) {
          const today = new Date();
          const advanceDays = (type === 'space') ? 3 : 1;
          const minDate = new Date(today.getFullYear(), today.getMonth(), today.getDate() + advanceDays);
          const yyyy = minDate.getFullYear();
          const mm = String(minDate.getMonth() + 1).padStart(2, '0');
          const dd = String(minDate.getDate()).padStart(2, '0');
          dateInput.min = `${yyyy}-${mm}-${dd}`;
          if (!dateInput.value || dateInput.value < dateInput.min) {
            dateInput.value = `${yyyy}-${mm}-${dd}`;
          }
        }
        modal.classList.add('active');
        modal.setAttribute('aria-hidden', 'false');
        document.body.style.overflow = 'hidden';
        if (window.lucide) window.lucide.createIcons();
      };
      window.handleTimeSelectChange = function(context) {
        const isModal = context === 'modal';
        const sel = document.getElementById(isModal ? 'bkTime' : 'pTime');
        const wrap = document.getElementById(isModal ? 'bkCustomTimeWrap' : 'pCustomTimeWrap');
        const input = document.getElementById(isModal ? 'bkCustomTime' : 'pCustomTime');
        if (!sel || !wrap) return;
        if (sel.value === 'custom') {
          wrap.style.display = 'block';
          if (input) input.focus();
        } else {
          wrap.style.display = 'none';
        }
      };
      window.closeBookingModal = function() {
        const modal = document.getElementById('bookingModal');
        if (modal) {
          modal.classList.remove('active');
          modal.setAttribute('aria-hidden', 'true');
          document.body.style.overflow = '';
        }
      };
      window.backToBookingForm = function() {
        const formArea = document.getElementById('bkFormArea');
        const successArea = document.getElementById('bkSuccessArea');
        if (formArea) formArea.style.display = 'block';
        if (successArea) successArea.style.display = 'none';
        if (window.lucide) window.lucide.createIcons();
      };
      window.selectBookingType = function(type) {
        currentBookingType = type;
        const btnSpace = document.getElementById('bkTypeSpace');
        const btnTable = document.getElementById('bkTypeTable');
        const noticeText = document.getElementById('bkNoticeText');
        const guestsInput = document.getElementById('bkGuests');
        const noteInput = document.getElementById('bkNote');
        const timeSelect = document.getElementById('bkTime');
        if (timeSelect && !timeSelect.value) {
          timeSelect.value = "10:00 - 12:00";
        }
        if (type === 'space') {
          if (btnSpace) btnSpace.classList.add('active');
          if (btnTable) btnTable.classList.remove('active');
          if (noticeText) noticeText.innerHTML = 'Liên hệ trước ít nhất <strong>1 tuần</strong> để Olion sắp xếp không gian chu đáo và phù hợp nhất.';
          if (guestsInput) guestsInput.value = '10';
          if (noteInput) {
            noteInput.value = 'Mình muốn đăng ký thuê không gian tổ chức Workshop / Họp nhóm. Nhờ Olion tư vấn gói dịch vụ, sắp xếp bàn ghế và hỗ trợ kết nối máy chiếu / âm thanh.';
          }
        } else {
          if (btnSpace) btnSpace.classList.remove('active');
          if (btnTable) btnTable.classList.add('active');
          if (noticeText) noticeText.innerHTML = 'Vui lòng đặt bàn trước ít nhất <strong>1 ngày</strong>. <em>(Lưu ý: Chỉ xác nhận khi quán phản hồi)</em>.';
          if (guestsInput) guestsInput.value = '4';
          if (noteInput) {
            noteInput.value = 'Mình muốn đặt bàn trước cho nhóm học tập / gặp gỡ bạn bè. Nhờ quán ưu tiên giữ giúp mình góc ngồi yên tĩnh, gần ổ cắm điện nhé.';
          }
        }
      };
      window.copyCurrentBookingMsg = function() {
        const msg = window.lastFormattedBookingMsg;
        if (!msg) return;
        try {
          if (navigator.clipboard && navigator.clipboard.writeText) {
            navigator.clipboard.writeText(msg);
          } else {
            const t = document.createElement('textarea');
            t.value = msg;
            document.body.appendChild(t);
            t.select();
            document.execCommand('copy');
            document.body.removeChild(t);
          }
        } catch(e) {}
        alert('📋 Đã sao chép lại toàn bộ nội dung yêu cầu! Bạn có thể dán (Paste) vào khung chat bất cứ lúc nào.');
      };
      window.quickConsultMessenger = function(type = 'all') {
        let msg = 'Chào Olion Coffee! Mình muốn được tư vấn thông tin về dịch vụ Cho thuê không gian & Đặt bàn trước tại quán.';
        if (type === 'space') {
          msg = 'Chào Olion Coffee! Mình muốn tư vấn dịch vụ Cho thuê không gian để tổ chức Workshop / Họp nhóm / CLB tại quán.';
        } else if (type === 'table') {
          msg = 'Chào Olion Coffee! Mình muốn tư vấn đặt bàn trước cho nhóm học tập / gặp gỡ bạn bè tại quán.';
        }
        try {
          if (navigator.clipboard && navigator.clipboard.writeText) {
            navigator.clipboard.writeText(msg);
          } else {
            const t = document.createElement('textarea');
            t.value = msg;
            document.body.appendChild(t);
            t.select();
            document.execCommand('copy');
            document.body.removeChild(t);
          }
        } catch(e) {}
        alert(`📋 Đã tự động sao chép nội dung:\n"${msg}"\n\nKhi Messenger mở ra, bạn chỉ cần bấm DÁN (Paste) để gửi ngay cho Olion nhé!`);
        window.open('https://m.me/61594159312837', '_blank');
      };
      window.handleBookingSubmit = async function(e) {
        if (e) e.preventDefault();
        const submitBtn = document.getElementById('bkSubmitBtn');
        const origBtnText = submitBtn ? submitBtn.textContent : '';
        if (submitBtn) {
          submitBtn.disabled = true;
          submitBtn.textContent = 'Đang lưu yêu cầu...';
        }
        const name = (document.getElementById('bkName')?.value || '').trim();
        const phone = (document.getElementById('bkPhone')?.value || '').trim();
        const guests = (document.getElementById('bkGuests')?.value || '').trim();
        const date = document.getElementById('bkDate')?.value || '';
        let time = document.getElementById('bkTime')?.value || '';
        const note = (document.getElementById('bkNote')?.value || '').trim();
        if (time === 'custom') {
          const customTimeVal = (document.getElementById('bkCustomTime')?.value || '').trim();
          if (!customTimeVal) {
            alert('Vui lòng nhập khung giờ riêng bạn mong muốn (Ví dụ: 09:30 - 11:30).');
            if (submitBtn) { submitBtn.disabled = false; submitBtn.textContent = origBtnText; }
            document.getElementById('bkCustomTime')?.focus();
            return;
          }
          time = customTimeVal;
        }
        if (!name || !phone || !date || !time) {
          alert('Vui lòng điền đầy đủ các thông tin bắt buộc (*)');
          if (submitBtn) { submitBtn.disabled = false; submitBtn.textContent = origBtnText; }
          return;
        }
        const typeLabel = (currentBookingType === 'space') 
          ? '01 - CHO THUÊ KHÔNG GIAN (Workshop / Họp nhóm / CLB / Sự kiện)' 
          : '02 - ĐẶT BÀN TRƯỚC (Học tập / Hẹn bạn bè / Làm việc)';
        const formattedMsg = `Chào Olion Coffee! Mình muốn đăng ký:\n` +
          `• Dịch vụ: ${typeLabel}\n` +
          `• Khách hàng: ${name} (${phone})\n` +
          `• Số lượng người: ${guests || '1'} người\n` +
          `• Thời gian dự kiến: ${time} ngày ${date}\n` +
          (note ? `• Yêu cầu chi tiết: ${note}\n` : '') +
          `Olion tư vấn và xác nhận giúp mình nhé! Cảm ơn quán.`;
        window.lastFormattedBookingMsg = formattedMsg;
        try {
          if (navigator.clipboard && navigator.clipboard.writeText) {
            navigator.clipboard.writeText(formattedMsg);
          } else {
            const t = document.createElement('textarea');
            t.value = formattedMsg;
            document.body.appendChild(t);
            t.select();
            document.execCommand('copy');
            document.body.removeChild(t);
          }
        } catch(err) {}
        try {
          const bookingPayload = {
            customer_name: name,
            phone: phone,
            booking_type: currentBookingType,
            guests_count: parseInt(guests, 10) || 1,
            booking_date: date,
            booking_time: time,
            notes: note,
            status: 'pending',
            created_at: new Date().toISOString()
          };
          if (typeof saveBookingToStorage === 'function') {
            await saveBookingToStorage(bookingPayload);
          } else if (window.saveBookingToStorage) {
            await window.saveBookingToStorage(bookingPayload);
          } else {
            const local = JSON.parse(localStorage.getItem('olion_bookings') || '[]');
            bookingPayload.id = 'bk_' + Date.now();
            local.unshift(bookingPayload);
            localStorage.setItem('olion_bookings', JSON.stringify(local));
          }
        } catch(err) {
          console.warn('Booking save error:', err);
        } finally {
          if (submitBtn) {
            submitBtn.disabled = false;
            submitBtn.textContent = origBtnText;
          }
        }
        try {
          localStorage.setItem('olion_customer_name', name);
          localStorage.setItem('olion_customer_phone', phone);
        } catch(err) {}
        const formArea = document.getElementById('bkFormArea');
        const successArea = document.getElementById('bkSuccessArea');
        const previewBox = document.getElementById('bkPreviewBox');
        if (previewBox) previewBox.textContent = formattedMsg;
        if (formArea) formArea.style.display = 'none';
        if (successArea) successArea.style.display = 'block';
        if (window.lucide) window.lucide.createIcons();
        window.open('https://m.me/61594159312837', '_blank');
      };
      const feedbackModal = document.getElementById('feedbackModal');
      let chosenRating = 5;
      window.openFeedbackModal = function() {
        if (typeof window.loadReCaptcha === 'function') window.loadReCaptcha();
        if (feedbackModal) {
          feedbackModal.classList.add('active');
          feedbackModal.setAttribute('aria-hidden', 'false');
          document.body.style.overflow = 'hidden';
        }
      };
      window.closeFeedbackModal = function() {
        if (feedbackModal) {
          feedbackModal.classList.remove('active');
          feedbackModal.setAttribute('aria-hidden', 'true');
          document.body.style.overflow = '';
          setTimeout(() => {
            const formArea = document.getElementById('feedbackFormArea');
            const successArea = document.getElementById('feedbackSuccessArea');
            if (formArea) formArea.style.display = 'block';
            if (successArea) successArea.style.display = 'none';
            const form = document.getElementById('feedbackForm');
            if (form) form.reset();
          }, 300);
        }
      };
      const starButtons = document.querySelectorAll('.star-btn');
      starButtons.forEach(btn => {
        btn.addEventListener('click', () => {
          chosenRating = parseInt(btn.getAttribute('data-star'), 10);
          starButtons.forEach((b, idx) => {
            b.classList.toggle('active', idx < chosenRating);
          });
        });
      });
      const btnSubmitFeedback = document.getElementById('btnSubmitFeedback');
      if (btnSubmitFeedback) {
        btnSubmitFeedback.addEventListener('click', async () => {
          const honeypot = (document.getElementById('fb_website_hp')?.value || '').trim();
          if (honeypot) {
            console.warn('🤖 [Security] Bot phát hiện qua Honeypot Trap!');
            document.getElementById('feedbackFormArea').style.display = 'none';
            document.getElementById('feedbackSuccessArea').style.display = 'block';
            return;
          }
          const fbNameEl = document.getElementById('fbName');
          const name = (fbNameEl ? fbNameEl.value : '').trim() || 'Khách ghé quán';
          if (name && name !== 'Khách ghé quán') {
            try {
              localStorage.setItem('olion_customer_name', name);
              if (typeof window.updateDynamicGreeting === 'function') {
                window.updateDynamicGreeting();
              }
            } catch(e) {}
          }
          const fbContactEl = document.getElementById('fbContact');
          const contact = (fbContactEl ? fbContactEl.value : '').trim();
          const fbMessageEl = document.getElementById('fbMessage');
          const message = (fbMessageEl ? fbMessageEl.value : '').trim();
          const fbImageEl = document.getElementById('fbImageDataUrl');
          const imageDataUrl = fbImageEl ? fbImageEl.value : '';
          if (!message && !imageDataUrl) {
            showOlionToast('Vui lòng chia sẻ đôi lời cảm nhận hoặc hình ảnh của bạn nhé!', '✍️');
            if (fbMessageEl) fbMessageEl.focus();
            return;
          }
          if (typeof canUserSubmitFeedback === 'function') {
            const check = await canUserSubmitFeedback(contact);
            if (!check.can_submit) {
              showOlionToast(check.message, 'clock');
              return;
            }
          }
          btnSubmitFeedback.disabled = true;
          btnSubmitFeedback.innerHTML = '<i data-lucide="loader-2" class="icon-spinner" style="width:16px;height:16px;margin-right:6px;"></i> Đang gửi...';
          lucide.createIcons();
          if (typeof executeReCaptcha === 'function') {
            await executeReCaptcha('submit_feedback');
          }
          if (typeof submitFeedbackToCloud === 'function') {
            await submitFeedbackToCloud({
              name,
              contact,
              rating: chosenRating,
              content: message,
              imageDataUrl: imageDataUrl
            });
          }
          btnSubmitFeedback.disabled = false;
          btnSubmitFeedback.textContent = 'Gửi đánh giá ngay';
          if (typeof removeFeedbackImage === 'function') {
            removeFeedbackImage();
          }
          const fbFormArea = document.getElementById('feedbackFormArea');
          if (fbFormArea) fbFormArea.style.display = 'none';
          const fbSuccessArea = document.getElementById('feedbackSuccessArea');
          if (fbSuccessArea) fbSuccessArea.style.display = 'block';
          showOlionToast('Cảm ơn bạn đã gửi đánh giá quý báu cho Olion Coffee!', 'check-circle');
        });
      }
      if (feedbackModal) {
        feedbackModal.addEventListener('click', (e) => {
          if (e.target === feedbackModal) closeFeedbackModal();
        });
      }
      const wheelModal = document.getElementById('wheelModal');
      const wheelCanvas = document.getElementById('wheelCanvas');
      const spinBtn = document.getElementById('spinBtn');
      window.openWheelModal = function() {
        if (wheelModal) {
          wheelModal.classList.add('active');
          document.body.style.overflow = 'hidden';
          drawWheel(0);
        }
      };
      window.closeWheelModal = function() {
        if (wheelModal) {
          wheelModal.classList.remove('active');
          document.body.style.overflow = '';
        }
      };
      let prizes = [
        { text: 'Giảm 10% Tổng Bill', code: 'OLION10', color: '#E59A55' },
        { text: 'Tặng 1 Topping Free', code: 'FREETOP', color: 'var(--bg-card)' },
        { text: 'Giảm 15% Cà Phê Muối', code: 'MUOI15', color: '#D86326' },
        { text: 'Voucher 20.000đ', code: 'GIFT20K', color: '#1D5A38' },
        { text: 'Tặng 1 Ly Bạc Xỉu', code: 'FREEBACXIU', color: '#E59A55' },
        { text: 'Chúc Bạn May Mắn', code: 'THANKYOU', color: 'var(--bg-card)' }
      ];
      function applyMinigameConfig() {
        try {
          const raw = localStorage.getItem('olion_minigame');
          const floatBtn = document.getElementById('wheelFloatBtn');
          if (!floatBtn) return;
          if (raw) {
            const config = JSON.parse(raw);
            if (config.enabled === false) {
              console.log("SETTING NONE"); floatBtn.style.setProperty("display", "none", "important");
              if (typeof closeWheelModal === 'function') closeWheelModal();
              return;
            } else {
              floatBtn.style.removeProperty('display');
              floatBtn.style.display = 'flex';
            }
            if (config.floatLabel) {
              const labelSpan = floatBtn.querySelector('[data-i18n="wheel_float"]') || floatBtn.querySelector('span:last-child');
              if (labelSpan) labelSpan.textContent = config.floatLabel;
            }
            if (config.title) {
              const titleEl = document.getElementById('wheelTitle');
              if (titleEl) titleEl.textContent = config.title;
            }
            if (config.prizes && Array.isArray(config.prizes) && config.prizes.length >= 2) {
              prizes = config.prizes.map(p => ({
                text: p.text || 'Quà tặng',
                code: p.code || 'OLIONGIFT',
                color: p.color || '#E59A55',
                desc: p.desc || (p.text + ' từ Olion Coffee!')
              }));
              if (typeof drawWheel === 'function') drawWheel(0);
            }
          } else {
            floatBtn.style.removeProperty('display');
            floatBtn.style.display = 'flex';
          }
        } catch (e) {
          console.warn('Lỗi applyMinigameConfig:', e);
        }
      }
      let isSpinning = false;
      function drawWheel(angle) {
        if (!wheelCanvas) return;
        const ctx = wheelCanvas.getContext('2d');
        const numSlices = prizes.length;
        const arc = (2 * Math.PI) / numSlices;
        const cx = 140;
        const cy = 140;
        const radius = 135;
        ctx.clearRect(0, 0, 280, 280);
        for (let i = 0; i < numSlices; i++) {
          const sliceAngle = angle + i * arc;
          ctx.beginPath();
          ctx.fillStyle = prizes[i].color;
          ctx.moveTo(cx, cy);
          ctx.arc(cx, cy, radius, sliceAngle, sliceAngle + arc);
          ctx.lineTo(cx, cy);
          ctx.fill();
          ctx.strokeStyle = 'rgba(229,154,85,0.4)';
          ctx.lineWidth = 2;
          ctx.stroke();
          ctx.save();
          ctx.translate(cx, cy);
          ctx.rotate(sliceAngle + arc / 2);
          ctx.textAlign = 'right';
          ctx.fillStyle = '#FFFFFF';
          ctx.font = 'bold 11px Plus Jakarta Sans, sans-serif';
          ctx.fillText(prizes[i].text, radius - 15, 4);
          ctx.restore();
        }
        ctx.beginPath();
        ctx.arc(cx, cy, 20, 0, 2 * Math.PI);
        ctx.fillStyle = '#E59A55';
        ctx.fill();
        ctx.strokeStyle = '#FFFFFF';
        ctx.lineWidth = 3;
        ctx.stroke();
      }
      if (spinBtn) {
        spinBtn.addEventListener('click', async () => {
          if (isSpinning) return;
          const wheelNameEl = document.getElementById('wheelName');
          const wheelPhoneEl = document.getElementById('wheelPhone');
          const name = (wheelNameEl ? wheelNameEl.value : '').trim();
          const phone = (wheelPhoneEl ? wheelPhoneEl.value : '').trim();
          if (!phone) {
            showOlionToast('Vui lòng nhập số điện thoại để nhận quà nhé!', 'phone');
            if (wheelPhoneEl) wheelPhoneEl.focus();
            return;
          }
          const cleanPhone = phone.replace(/[^0-9]/g, '');
          if (cleanPhone.length < 9) {
            showOlionToast('Số điện thoại không hợp lệ (tối thiểu 9-10 chữ số)!', 'alert-circle');
            if (wheelPhoneEl) wheelPhoneEl.focus();
            return;
          }
          if (typeof canUserSpinToday === 'function') {
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
          spinBtn.textContent = 'ĐANG QUAY...';
          const prizeIndex = Math.floor(Math.random() * (prizes.length - 1)); // Always win something nice
          const arc = (2 * Math.PI) / prizes.length;
          const targetSliceAngle = (1.5 * Math.PI) - (prizeIndex * arc + arc / 2);
          const totalRotations = (6 + Math.floor(Math.random() * 3)) * 2 * Math.PI;
          const finalAngle = totalRotations + targetSliceAngle;
          const duration = 4000;
          const start = performance.now();
          async function animate(now) {
            const elapsed = now - start;
            const progress = Math.min(elapsed / duration, 1);
            const easeOut = 1 - Math.pow(1 - progress, 3);
            const currentA = finalAngle * easeOut;
            drawWheel(currentA);
            if (progress < 1) {
              requestAnimationFrame(animate);
            } else {
              isSpinning = false;
              spinBtn.disabled = false;
              spinBtn.textContent = 'QUAY NGAY';
              const prize = prizes[prizeIndex];
              document.getElementById('wheelPrizeTitle').textContent = `Chúc Mừng ${name || 'Bạn'}!`;
              document.getElementById('wheelPrizeDesc').textContent = `Bạn đã trúng thưởng: ${prize.text}`;
              document.getElementById('wheelCode').textContent = prize.code;
              document.getElementById('wheelFormArea').style.display = 'none';
              document.getElementById('wheelResultArea').style.display = 'block';
              if (typeof recordLuckySpinToCloud === 'function') {
                const insertedData = await recordLuckySpinToCloud({
                  customer_name: name || 'Khách quay minigame',
                  customer_phone: phone,
                  prize_name: prize.text,
                  promo_code: prize.code
                });
                const qrContainer = document.getElementById('qrCodeContainer');
                qrContainer.innerHTML = '';
                if (insertedData && insertedData.id) {
                  new QRCode(qrContainer, {
                    text: 'olion-voucher:' + insertedData.id,
                    width: 150,
                    height: 150,
                    colorDark : "#190D07",
                    colorLight : "#ffffff",
                    correctLevel : QRCode.CorrectLevel.H
                  });
                }
              }
              showOlionToast(`Chúc mừng bạn nhận được ưu đãi ${prize.code}!`, 'gift');
            }
          }
          requestAnimationFrame(animate);
        });
      }
      const footerBrand = document.getElementById('footerBrandLogo');
      const longPressBar = document.getElementById('longPressProgress');
      let pressTimer = null;
      let pressProgressInterval = null;
      let pressProgress = 0;
      let clickCount = 0;
      let clickTimer = null;
      function startLongPress() {
        pressProgress = 0;
        if (longPressBar) longPressBar.style.width = '0%';
        pressProgressInterval = setInterval(() => {
          pressProgress += 5;
          if (longPressBar) longPressBar.style.width = pressProgress + '%';
        }, 100);
        pressTimer = setTimeout(() => {
          clearInterval(pressProgressInterval);
          if (navigator.vibrate) navigator.vibrate(100);
          window.location.href = 'admin';
        }, 2000); // 2 seconds hold
      }
      function cancelLongPress() {
        clearTimeout(pressTimer);
        clearInterval(pressProgressInterval);
        if (longPressBar) longPressBar.style.width = '0%';
      }
      if (footerBrand) {
        footerBrand.addEventListener('touchstart', startLongPress, { passive: true });
        footerBrand.addEventListener('touchend', cancelLongPress);
        footerBrand.addEventListener('touchcancel', cancelLongPress);
        footerBrand.addEventListener('click', () => {
          clickCount++;
          clearTimeout(clickTimer);
          if (clickCount >= 3) {
            clickCount = 0;
            window.location.href = 'admin';
          } else {
            clickTimer = setTimeout(() => { clickCount = 0; }, 1200);
          }
        });
      }
      document.addEventListener('keydown', (e) => {
        if ((e.ctrlKey || e.metaKey) && e.shiftKey && (e.key === 'a' || e.key === 'A')) {
          e.preventDefault();
          window.location.href = 'admin';
        }
      });
      let newsArticlesData = {};
      window.loadFeaturedNews = async function() {
        try {
          const client = window.supabaseClient || window._supabase || (typeof supabaseClient !== 'undefined' ? supabaseClient : null) || (window.supabase ? window.supabase.createClient('https://xwbrbesgnwcngzohprxt.supabase.co', 'sb_publishable_vWuV07_xPU0wNftK0lpnFQ_oA9XHPLS') : null);
          let data = null;
          if (client) {
            const res = await client.from('news_items').select('*').order('created_at', { ascending: false });
            if (!res.error && res.data && res.data.length > 0) {
              data = res.data;
              try { localStorage.setItem('olion_cached_news', JSON.stringify(data)); } catch(e) {}
            }
          }
          if (!data || data.length === 0) {
            try { data = JSON.parse(localStorage.getItem('olion_cached_news') || '[]'); } catch(e) {}
          }
          if (!data || data.length === 0) {
            data = [
              {
                id: "e6cff902-fbd7-4668-b3eb-0d30708fe79e",
                title: "CARAMEL LATTE — Sự Hòa Quyện Ngọt Ngào & Đậm Đà Cuốn Hút",
                date: "21/10/2026",
                category: "Thực Đơn Signature",
                cover_image: "assets/news/caramel-latte.webp",
                description: "Một chút caramel ngọt ngào, một chút espresso đậm đà, hòa quyện cùng sữa béo mịn — tạo nên Caramel Latte đầy cuốn hút tại Olion Coffee.",
                content_html: "<p>Một chút caramel ngọt ngào, một chút espresso đậm đà, hòa quyện cùng sữa béo mịn — tạo nên <strong>Caramel Latte</strong> đầy cuốn hút. ☕🤎</p><p>Sự kết hợp mượt mà giữa espresso đậm đà, sữa béo ngậy và caramel ngọt ngào sẽ mang đến cho bạn trải nghiệm vị giác vô cùng trọn vẹn.</p><p>Ghé <strong>Olion Coffee</strong>, thưởng thức một ly ngọt ngào và tận hưởng chút bình yên giữa ngày nhé! ❤️</p>",
                is_featured: false
              },
              {
                id: "70d3d568-c478-40ef-a066-7e0cfc6f1982",
                title: "CÓ THÊM ĐIỀU MỚI: CHO THUÊ KHÔNG GIAN & ĐẶT BÀN TRƯỚC",
                date: "21/10/2026",
                category: "Không Gian & Dịch Vụ",
                cover_image: "assets/banner-booking.webp",
                description: "Tại Olion Coffee, chúng mình hiểu rằng mỗi khoảnh khắc học tập, hội họp hay gặp gỡ bạn bè đều cần một không gian đủ ấm cúng, đủ yên tĩnh và trọn vẹn sự tinh tế.",
                content_html: "<p>Tại Olion Coffee, chúng mình hiểu rằng mỗi khoảnh khắc học tập, hội họp hay gặp gỡ bạn bè đều cần một không gian đủ ấm cúng, đủ yên tĩnh và trọn vẹn sự tinh tế.</p>",
                is_featured: true
              },
              {
                id: "8b0a9a12-5d25-44be-ad3e-780161daa6c6",
                title: "OLION’S FIRST WEEK — NHẬT KÝ TUẦN ĐẦU TIÊN",
                date: "19/09/2026",
                category: "Sự kiện đặc biệt",
                cover_image: "assets/news/news-1-flowers.webp",
                description: "Tuần đầu tiên mở cửa đã khép lại với biết bao cung bậc cảm xúc! Olion Coffee vô cùng trân trọng...",
                content_html: "<p>Tuần đầu tiên mở cửa đã khép lại với biết bao cung bậc cảm xúc! Olion Coffee vô cùng trân trọng...</p>",
                is_featured: false
              }
            ];
          }
          const featured = data.find(i => i.is_featured) || data[0];
          const subItems = data.filter(i => i.id !== featured.id).slice(0, 4);
          data.forEach(item => {
            newsArticlesData[item.id] = {
              title: item.title,
              date: item.date,
              category: item.category,
              images: [item.cover_image],
              desc: item.description,
              contentHtml: item.content_html
            };
          });
          let subCardsHtml = '';
          subItems.forEach(item => {
            subCardsHtml += `
              <article class="news-sub-card" onclick="openNewsModal('${item.id}')">
                <div class="news-sub-img-wrap">
                  <img src="${item.cover_image}" alt="${item.title}" class="news-sub-img" loading="lazy" />
                </div>
                <div class="news-sub-content">
                  <div class="news-meta">
                    <span class="news-date">${item.date}</span>
                    <span class="news-category" style="color:var(--accent-gold);">${item.category}</span>
                  </div>
                  <h4 class="news-sub-title" style="margin-bottom:8px; line-height: 1.4;">${item.title}</h4>
                  <p class="news-sub-desc">${item.description ? item.description.substring(0, 80) + '...' : ''}</p>
                  <span class="news-sub-link">Xem chi tiết &rarr;</span>
                </div>
              </article>
            `;
          });
          const gridHtml = `
            <div class="news-featured">
              <article class="news-featured-card" onclick="openNewsModal('${featured.id}')">
                <div class="news-featured-img-wrap">
                  <img src="${featured.cover_image}" alt="${featured.title}" class="news-featured-img" loading="lazy" />
                  <div class="news-featured-badge"><i data-lucide="award" style="width:13px;height:13px;"></i> Nổi bật</div>
                </div>
                <div class="news-featured-content">
                  <div class="news-meta">
                    <span class="news-date"><i data-lucide="calendar" style="width:12px;height:12px;margin-right:4px;"></i>${featured.date}</span>
                    <span class="news-category">${featured.category}</span>
                  </div>
                  <h3 class="news-featured-title">${featured.title}</h3>
                  <p class="news-featured-excerpt">${featured.description || ''}</p>
                  <div class="news-featured-footer">
                    <button class="btn-read-more">Xem bài viết <i data-lucide="arrow-right" style="width:16px;height:16px;"></i></button>
                  </div>
                </div>
              </article>
            </div>
            <div class="news-sub">
              <div class="news-sub-grid">
                ${subCardsHtml}
              </div>
            </div>
          `;
          const newsGrid = document.getElementById('homepageNewsGrid');
          if (newsGrid) {
            newsGrid.innerHTML = gridHtml;
          }
          if (window.lucide && typeof window.lucide.createIcons === 'function') {
            window.lucide.createIcons();
          }
        } catch (e) {
        }
      };
      setTimeout(() => {
        if (window.loadFeaturedNews) window.loadFeaturedNews();
        const urlParams = new URLSearchParams(window.location.search);
        const targetArticleId = urlParams.get('article');
        if (targetArticleId) {
          setTimeout(() => {
            if (window.openNewsModal) window.openNewsModal(targetArticleId);
          }, 600);
        }
      }, 500);
      window.openNewsModal = function(newsId) {
        currentNewsId = newsId;
        const article = newsArticlesData[newsId];
        if (!newsModal || !article) return;
        newsModalTitle.textContent = article.title;
        newsModalDate.textContent = article.date;
        newsModalCategory.textContent = article.category;
        newsModalMainImg.src = article.images[0] || 'assets/logo-white.webp';
        newsModalBody.innerHTML = article.contentHtml;
        if (newsModalThumbs) {
          newsModalThumbs.innerHTML = '';
          newsModalThumbs.style.display = 'none';
        }
        newsModalMainImg.style.opacity = '1';
        newsModalMainImg.style.transform = 'scale(1)';
        newsModal.classList.add('active');
        newsModal.setAttribute('aria-hidden', 'false');
        document.body.style.overflow = 'hidden';
      };
      window.closeNewsModal = function() {
        if (!newsModal) return;
        newsModal.classList.remove('active');
        newsModal.setAttribute('aria-hidden', 'true');
        document.body.style.overflow = '';
      };
      if (newsModal) {
        newsModal.addEventListener('click', (e) => {
          if (e.target === newsModal) closeNewsModal();
        });
      }
      window.shareNewsArticle = function() {
        const shareData = {
          title: newsModalTitle.textContent,
          text: 'Xem tin tức mới nhất từ Olion Coffee!',
          url: window.location.href.split('#')[0] + '#news'
        };
        if (navigator.share) {
          navigator.share(shareData).catch(() => {});
        } else {
          navigator.clipboard.writeText(shareData.url);
          alert('Đã sao chép liên kết bài viết vào bộ nhớ tạm!');
        }
      };
      const revealTargets = document.querySelectorAll(
        '.section-header, .stat-card, .feature-pill, .signature-card, .menu-card, .space-card, .review-card, .faq-item, .contact-card, .hours-card, .news-card-main, .news-card-side, .service-feature-card, .news-featured-card, .news-sub-card'
      );
      if ('IntersectionObserver' in window) {
        const revealObserver = new IntersectionObserver((entries) => {
          entries.forEach(entry => {
            if (entry.isIntersecting) {
              entry.target.classList.add('visible');
              revealObserver.unobserve(entry.target);
            }
          });
        }, {
          threshold: 0.12,
          rootMargin: '0px 0px -40px 0px'
        });
        revealTargets.forEach((el, i) => {
          el.classList.add('reveal');
          const staggerIndex = i % 4;
          if (staggerIndex > 0) el.classList.add(`reveal-delay-${staggerIndex}`);
          revealObserver.observe(el);
        });
      } else {
        revealTargets.forEach(el => el.classList.add('reveal', 'visible'));
      }
      const navLinks = document.querySelectorAll('.header-nav .nav-link');
      const sectionIds = ['#about', '#signature', '#menu', '#spaces', '#news', '#faq', '#contact'];
      const sections = sectionIds.map(id => document.querySelector(id)).filter(Boolean);
      if ('IntersectionObserver' in window && sections.length) {
        const navObserver = new IntersectionObserver((entries) => {
          entries.forEach(entry => {
            if (entry.isIntersecting) {
              const id = '#' + entry.target.id;
              navLinks.forEach(link => {
                link.classList.toggle('active', link.getAttribute('href') === id);
              });
            }
          });
        }, { rootMargin: '-30% 0px -60% 0px' });
        sections.forEach(s => navObserver.observe(s));
      }
      function escapeHtml(str) {
        if (!str) return '';
        return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
      }
      window.dismissAnnouncement = function() {
        const banner = document.getElementById('announcementBanner');
        if (banner) banner.style.display = 'none';
        sessionStorage.setItem('olion_announcement_dismissed', 'true');
      };
      function applyAnnouncementConfig() {
        try {
          const banner = document.getElementById('announcementBanner');
          if (!banner) return;
          if (sessionStorage.getItem('olion_announcement_dismissed') === 'true') {
            banner.style.display = 'none';
            return;
          }
          const raw = localStorage.getItem('olion_announcement');
          if (raw) {
            const data = JSON.parse(raw);
            if (data.enabled && data.text) {
              const badgeEl = document.getElementById('announcementBadge');
              const textEl = document.getElementById('announcementText');
              const linkEl = document.getElementById('announcementLink');
              if (badgeEl) badgeEl.textContent = data.badge || 'ƯU ĐÃI';
              if (textEl) textEl.textContent = data.text;
              if (linkEl) {
                linkEl.href = data.link || '#menu';
                linkEl.style.display = data.link ? 'inline' : 'none';
              }
              banner.style.display = 'block';
              return;
            }
          }
          banner.style.display = 'none';
        } catch (e) {
          console.warn('Lỗi applyAnnouncementConfig:', e);
        }
      }
      function applyStoreSettings() {
        try {
          const raw = localStorage.getItem('olion_store_settings');
          if (!raw) return;
          const s = JSON.parse(raw);
          if (s.hotline) {
            const cleanPhone = s.hotline.replace(/\s+/g, '');
            document.querySelectorAll('a[href^="tel:"]').forEach(a => {
              a.href = 'tel:' + cleanPhone;
              const numSpan = a.querySelector('span:last-child');
              if (numSpan && !a.classList.contains('btn')) numSpan.textContent = s.hotline;
            });
            const footerTel = document.querySelector('.contact-item a[href^="tel:"]');
            if (footerTel) footerTel.textContent = s.hotline;
          }
          if (s.address) {
            const addrEls = document.querySelectorAll('.contact-item-text');
            if (addrEls.length > 0) addrEls[0].textContent = s.address;
          }
          if (s.hours) {
            const hourEl = document.querySelector('.hours-badge');
            if (hourEl) hourEl.textContent = s.hours;
          }
          if (s.accentColor) {
            document.documentElement.style.setProperty('--accent-gold', s.accentColor);
          }
        } catch (e) {
          console.warn('Lỗi applyStoreSettings:', e);
        }
      }
      const CAT_PANEL_MAP = {
        'Cà phê': 'cat-coffee',
        'Trà trái cây': 'cat-tea',
        'Trà sữa & Matcha': 'cat-matcha',
        'Matcha': 'cat-matcha',
        'Cacao': 'cat-cacao',
        'Nước ép': 'cat-juice',
        'Sữa chua': 'cat-yagout',
        'Topping': 'cat-topping'
      };
      async function syncMenuFromCloud() {
        try {
          if (typeof fetchMenuItemsFromCloud !== 'function') return;
          const res = await fetchMenuItemsFromCloud();
          const items = res.data;
          if (!items || !Array.isArray(items) || items.length === 0) return;
          allMenuItemsCache = items;
          const grouped = {};
          items.forEach(item => {
            const cat = item.category || 'Cà phê';
            const panelId = CAT_PANEL_MAP[cat] || 'cat-coffee';
            if (!grouped[panelId]) grouped[panelId] = [];
            grouped[panelId].push(item);
          });
          Object.keys(grouped).forEach(panelId => {
            const panel = document.getElementById(panelId);
            if (!panel) return;
            const grid = panel.querySelector('.menu-grid');
            if (!grid) return;
            const catItems = grouped[panelId];
            let html = '';
            catItems.forEach(item => {
              const isSoldOut = item.is_available === false;
              let badgeHtml = '';
              if (isSoldOut) {
                badgeHtml = '<span class="menu-badge badge-sold-out">HẾT MÓN</span>';
              } else if (item.badge) {
                const b = item.badge.toUpperCase();
                let bClass = 'badge-best';
                if (b.includes('HOT') || b.includes('CHẠY')) bClass = 'badge-hot';
                else if (b.includes('NEW') || b.includes('MỚI')) bClass = 'badge-new';
                else if (b.includes('SIGNATURE')) bClass = 'badge-signature';
                badgeHtml = `<span class="menu-badge ${bClass}">${escapeHtml(item.badge)}</span>`;
              }
              const priceFmt = (Number(item.price) || 0).toLocaleString('vi-VN') + 'đ';
              html += `
                <article class="menu-card ${isSoldOut ? 'is-sold-out' : ''}">
                  <div class="menu-card-img-wrap">
                    ${badgeHtml}
                    <img src="${escapeHtml(item.image_url || 'assets/menu/espresso.webp')}" alt="${escapeHtml(item.name)} — Olion Coffee" class="menu-card-img" width="300" height="300" loading="lazy" decoding="async" onerror="this.src='assets/menu/espresso.webp'" />
                  </div>
                  <div class="menu-card-body">
                    <h3 class="menu-card-name">${escapeHtml(item.name)}</h3>
                    <div class="menu-card-price">${priceFmt}</div>
                    <p class="menu-card-desc">${escapeHtml(item.description || '')}</p>
                  </div>
                </article>
              `;
            });
            grid.innerHTML = html;
          });
        } catch (err) {
          console.warn('Lỗi syncMenuFromCloud:', err);
        }
      }
      async function syncApprovedReviews() {
        try {
          if (typeof fetchApprovedFeedbacksFromCloud !== 'function') return;
          const res = await fetchApprovedFeedbacksFromCloud();
          const feedbacks = res.data;
          if (!feedbacks || !Array.isArray(feedbacks) || feedbacks.length === 0) return;
          const reviewsGrid = document.getElementById('reviewsGrid');
          if (!reviewsGrid) return;
          feedbacks.slice(0, 4).reverse().forEach(fb => {
            const fbId = 'fb-card-' + fb.id;
            if (document.getElementById(fbId)) return;
            const card = document.createElement('article');
            card.id = fbId;
            card.className = 'review-card reveal visible';
            const starCount = Math.min(5, Math.max(1, fb.rating || 5)); const stars = `<span style='color:var(--accent-gold);letter-spacing:2px;'>${'★'.repeat(starCount)}</span>`;
            const avatarIcons = ['user', 'user-check', 'smile', 'award', 'heart'];
            const randomIcon = avatarIcons[Math.floor(Math.random() * avatarIcons.length)];
            card.innerHTML = `
              <div class="review-stars" aria-label="${fb.rating || 5} trên 5 sao">${stars}</div>
              <p class="review-quote">"${escapeHtml(fb.content)}"</p>
              <div class="review-author">
                <div class="review-avatar">${randomIcon}</div>
                <div>
                  <h3 class="review-name">${escapeHtml(fb.name || 'Khách ghé quán')}</h3>
                  <p class="review-role">Đánh giá xác thực tại quán</p>
                </div>
              </div>
            `;
            reviewsGrid.prepend(card);
          });
        } catch (err) {
          console.warn('Lỗi syncApprovedReviews:', err);
        }
      }
      function getOlionStoreStatus() {
        const now = new Date();
        const vnDateStr = now.toLocaleString("en-US", { timeZone: "Asia/Ho_Chi_Minh" });
        const vnTime = new Date(vnDateStr);
        const hours = vnTime.getHours();
        const minutes = vnTime.getMinutes();
        const totalMin = hours * 60 + minutes;
        const openMin = 8 * 60;
        const closeMin = 20 * 60;
        if (totalMin >= openMin && totalMin < closeMin - 30) {
          return {
            status: 'open',
            badgeText: 'ĐANG MỞ CỬA',
            subText: 'Đang mở cửa • 08:00 - 20:00',
            hoursSub: 'Thời gian thực (GMT+7) • Mở đến 20:00',
            atmosphere: 'Quán đang phục vụ. Không gian máy lạnh mát rượi, âm nhạc êm dịu, sẵn sàng đón bạn đến làm việc & thưởng thức cà phê!'
          };
        } else if (totalMin >= closeMin - 30 && totalMin < closeMin) {
          const remaining = closeMin - totalMin;
          return {
            status: 'closing',
            badgeText: 'SẮP ĐÓNG CỬA',
            subText: `Sắp đóng cửa • Còn ${remaining} phút`,
            hoursSub: `Thời gian thực (GMT+7) • Đóng cửa sau ${remaining} phút`,
            atmosphere: 'Quán nhận order mang đi & chốt bàn cuối trong ngày đến 20:00. Bạn vẫn có thể đặt bàn trước cho ngày mai!'
          };
        } else {
          return {
            status: 'closed',
            badgeText: 'TẠM NGHỈ',
            subText: 'Tạm nghỉ • Mở lại 08:00 sáng mai',
            hoursSub: 'Thời gian thực (GMT+7) • Mở lại lúc 08:00',
            atmosphere: 'Olion đang nghỉ ngơi để chuẩn bị nguyên liệu tươi ngon nhất. Bạn vẫn có thể Đặt Bàn Giữ Chỗ trước trực tuyến!'
          };
        }
      }
      function updateOlionStoreStatus() {
        try {
          const info = getOlionStoreStatus();
          const headerBadge = document.getElementById('headerStoreBadge');
          const headerText = document.getElementById('headerStatusText');
          const headerDot = document.getElementById('headerPulseDot');
          if (headerBadge && headerText) {
            headerBadge.className = 'header-store-badge ' + (info.status === 'closing' ? 'closing' : (info.status === 'closed' ? 'closed' : ''));
            headerText.textContent = info.badgeText;
            if (headerDot) {
              headerDot.className = 'status-pulse-dot ' + (info.status === 'closing' ? 'closing' : (info.status === 'closed' ? 'closed' : ''));
            }
          }
          const drawerCard = document.getElementById('drawerStoreStatus');
          const drawerTitle = document.getElementById('drawerStatusTitle');
          const drawerDot = document.getElementById('drawerPulseDot');
          if (drawerCard && drawerTitle) {
            drawerCard.className = 'drawer-status-card ' + (info.status === 'closing' ? 'closing' : (info.status === 'closed' ? 'closed' : ''));
            drawerTitle.textContent = info.subText;
            if (drawerDot) {
              drawerDot.className = 'status-pulse-dot ' + (info.status === 'closing' ? 'closing' : (info.status === 'closed' ? 'closed' : ''));
            }
          }
          const hoursBadge = document.getElementById('hoursStatusBadge');
          const hoursText = document.getElementById('hoursStatusText');
          const hoursDot = document.getElementById('hoursPulseDot');
          const atmosTime = document.getElementById('storeAtmosphereTime');
          const atmosDesc = document.getElementById('storeAtmosphereDesc');
          if (hoursBadge && hoursText) {
            hoursBadge.className = 'live-status-pill ' + (info.status === 'open' ? 'is-open' : (info.status === 'closing' ? 'is-closing' : 'is-closed'));
            hoursText.textContent = info.badgeText;
            if (hoursDot) {
              hoursDot.className = 'status-pulse-dot ' + (info.status === 'closing' ? 'closing' : (info.status === 'closed' ? 'closed' : ''));
            }
          }
          if (atmosTime) atmosTime.textContent = info.hoursSub;
          if (atmosDesc) atmosDesc.textContent = info.atmosphere;
        } catch (e) {
          console.warn('Lỗi updateOlionStoreStatus:', e);
        }
      }
      updateOlionStoreStatus();
      setInterval(updateOlionStoreStatus, 30000);
      let allMenuItemsCache = [];
      let activeTasteFilter = 'all';
      let previousActivePanelId = 'cat-coffee';
      function normalizeSearchString(str) {
        if (!str) return '';
        return str
          .toString()
          .toLowerCase()
          .normalize('NFD')
          .replace(/[\u0300-\u036f]/g, '')
          .replace(/đ/g, 'd')
          .replace(/Đ/g, 'd')
          .trim();
      }
      function getAllMenuItems() {
        if (allMenuItemsCache.length > 0) return allMenuItemsCache;
        try {
          const local = JSON.parse(localStorage.getItem('olion_menu_items') || '[]');
          if (Array.isArray(local) && local.length >= 30) {
            allMenuItemsCache = local;
            return allMenuItemsCache;
          }
        } catch (e) {}
        if (typeof DEFAULT_MENU_ITEMS !== 'undefined' && Array.isArray(DEFAULT_MENU_ITEMS)) {
          allMenuItemsCache = DEFAULT_MENU_ITEMS;
          return allMenuItemsCache;
        }
        return [];
      }
      function filterMenu(query = '', taste = 'all') {
        const searchInput = document.getElementById('menuSearchInput');
        const clearBtn = document.getElementById('menuSearchClear');
        const catSearchPanel = document.getElementById('cat-search');
        const searchGrid = document.getElementById('searchMenuGrid');
        const emptyState = document.getElementById('menuEmptyState');
        const countEl = document.getElementById('searchResultCount');
        const queryEl = document.getElementById('searchResultQuery');
        const emptyTermEl = document.getElementById('emptySearchTerm');
        const menuPanels = document.querySelectorAll('.menu-category-panel');
        const menuTabBtns = document.querySelectorAll('.menu-tab-btn[data-cat]');
        const trimmedQuery = query.trim();
        const normQuery = normalizeSearchString(trimmedQuery);
        if (clearBtn) {
          clearBtn.style.display = trimmedQuery ? 'flex' : 'none';
        }
        if (!trimmedQuery && taste === 'all') {
          if (catSearchPanel) catSearchPanel.classList.remove('active');
          menuPanels.forEach(p => {
            p.classList.toggle('active', p.id === previousActivePanelId);
          });
          menuTabBtns.forEach(btn => {
            btn.classList.toggle('active', `cat-${btn.getAttribute('data-cat')}` === previousActivePanelId);
          });
          return;
        }
        const currentActivePanel = Array.from(menuPanels).find(p => p.classList.contains('active') && p.id !== 'cat-search');
        if (currentActivePanel) previousActivePanelId = currentActivePanel.id;
        menuPanels.forEach(p => p.classList.remove('active'));
        if (catSearchPanel) catSearchPanel.classList.add('active');
        menuTabBtns.forEach(btn => btn.classList.remove('active'));
        const items = getAllMenuItems();
        const filtered = items.filter(item => {
          let matchTaste = true;
          const cat = item.category || '';
          const nameDesc = ((item.name || '') + ' ' + (item.description || '')).toLowerCase();
          const badge = (item.badge || '').toUpperCase();
          if (taste === 'signature') {
            matchTaste = Boolean(badge && (badge.includes('BEST') || badge.includes('HOT') || badge.includes('SIGNATURE') || badge.includes('NEW')));
          } else if (taste === 'coffee') {
            matchTaste = (cat === 'Cà phê' || cat === 'Cacao');
          } else if (taste === 'refreshing') {
            matchTaste = (cat === 'Trà trái cây' || cat === 'Nước ép');
          } else if (taste === 'creamy') {
            matchTaste = /latte|muoi|muối|sua|sữa|yagout|bac xiu|bạc xỉu|caramel|cacao|dua|dừa|beo|béo/i.test(normalizeSearchString(nameDesc));
          } else if (taste === 'plantmilk') {
            matchTaste = /oatside|hanh nhan|hạnh nhân|yen mach|yến mạch|thuc vat|thực vật/i.test(normalizeSearchString(nameDesc));
          }
          if (!matchTaste) return false;
          if (!normQuery) return true;
          const normName = normalizeSearchString(item.name || '');
          const normDesc = normalizeSearchString(item.description || '');
          const normCat = normalizeSearchString(item.category || '');
          return normName.includes(normQuery) || normDesc.includes(normQuery) || normCat.includes(normQuery);
        });
        if (countEl) countEl.textContent = `Tìm thấy ${filtered.length} món phù hợp`;
        if (queryEl) {
          const tasteLabel = document.querySelector(`.taste-pill[data-taste="${taste}"]`);
          const tasteText = (taste !== 'all' && tasteLabel) ? `[${tasteLabel.textContent.trim()}]` : '';
          queryEl.textContent = trimmedQuery ? `với từ khóa "${trimmedQuery}" ${tasteText}` : tasteText;
        }
        if (filtered.length === 0) {
          if (searchGrid) { searchGrid.innerHTML = ''; searchGrid.style.display = 'none'; }
          if (emptyState) {
            emptyState.style.display = 'block';
            if (emptyTermEl) emptyTermEl.textContent = trimmedQuery ? `"${trimmedQuery}"` : 'gu vị đã chọn';
          }
        } else {
          if (emptyState) emptyState.style.display = 'none';
          if (searchGrid) {
            searchGrid.style.display = 'grid';
            let html = '';
            filtered.forEach(item => {
              const isSoldOut = item.is_available === false;
              let badgeHtml = '';
              if (isSoldOut) {
                badgeHtml = '<span class="menu-badge badge-sold-out">HẾT MÓN</span>';
              } else if (item.badge) {
                const b = item.badge.toUpperCase();
                let bClass = 'badge-best';
                if (b.includes('HOT') || b.includes('CHẠY')) bClass = 'badge-hot';
                else if (b.includes('NEW') || b.includes('MỚI')) bClass = 'badge-new';
                else if (b.includes('SIGNATURE')) bClass = 'badge-signature';
                badgeHtml = `<span class="menu-badge ${bClass}">${escapeHtml(item.badge)}</span>`;
              }
              const priceFmt = (Number(item.price) || 0).toLocaleString('vi-VN') + 'đ';
              html += `
                <article class="menu-card ${isSoldOut ? 'is-sold-out' : ''}" id="card-item-${item.id}">
                  <div class="menu-card-img-wrap">
                    ${badgeHtml}
                    <img src="${escapeHtml(item.image_url || 'assets/menu/espresso.webp')}" alt="${escapeHtml(item.name)} — Olion Coffee" class="menu-card-img" width="300" height="300" loading="lazy" decoding="async" onerror="this.src='assets/menu/espresso.webp'" />
                  </div>
                  <div class="menu-card-body">
                    <h3 class="menu-card-name">${escapeHtml(item.name)}</h3>
                    <div class="menu-card-price">${priceFmt}</div>
                    <p class="menu-card-desc">${escapeHtml(item.description || '')}</p>
                  </div>
                </article>
              `;
            });
            searchGrid.innerHTML = html;
          }
        }
      }
      window.resetMenuSearch = function() {
        const searchInput = document.getElementById('menuSearchInput');
        const clearBtn = document.getElementById('menuSearchClear');
        if (searchInput) searchInput.value = '';
        if (clearBtn) clearBtn.style.display = 'none';
        activeTasteFilter = 'all';
        document.querySelectorAll('.taste-pill').forEach(p => {
          p.classList.toggle('active', p.getAttribute('data-taste') === 'all');
        });
        filterMenu('', 'all');
      };
      const menuSearchInput = document.getElementById('menuSearchInput');
      const menuSearchClear = document.getElementById('menuSearchClear');
      let searchDebounceTimer = null;
      if (menuSearchInput) {
        menuSearchInput.addEventListener('input', (e) => {
          clearTimeout(searchDebounceTimer);
          searchDebounceTimer = setTimeout(() => {
            filterMenu(e.target.value, activeTasteFilter);
          }, 180);
        });
      }
      if (menuSearchClear) {
        menuSearchClear.addEventListener('click', () => {
          if (menuSearchInput) menuSearchInput.value = '';
          menuSearchClear.style.display = 'none';
          filterMenu('', activeTasteFilter);
          if (menuSearchInput) menuSearchInput.focus();
        });
      }
      document.querySelectorAll('.taste-pill').forEach(pill => {
        pill.addEventListener('click', () => {
          document.querySelectorAll('.taste-pill').forEach(p => p.classList.remove('active'));
          pill.classList.add('active');
          activeTasteFilter = pill.getAttribute('data-taste') || 'all';
          const q = menuSearchInput ? menuSearchInput.value : '';
          filterMenu(q, activeTasteFilter);
        });
      });
      document.querySelectorAll('.menu-tab-btn[data-cat]').forEach(btn => {
        btn.addEventListener('click', () => {
          if (menuSearchInput) menuSearchInput.value = '';
          if (menuSearchClear) menuSearchClear.style.display = 'none';
          activeTasteFilter = 'all';
          document.querySelectorAll('.taste-pill').forEach(p => {
            p.classList.toggle('active', p.getAttribute('data-taste') === 'all');
          });
          const catSearchPanel = document.getElementById('cat-search');
          if (catSearchPanel) catSearchPanel.classList.remove('active');
        });
      });
      let quizAnswers = { mood: '', flavor: '', style: '' };
      let matchedQuizDrink = null;
      window.openTasteQuiz = function() {
        const modal = document.getElementById('tasteQuizModal');
        if (!modal) return;
        resetTasteQuiz();
        modal.classList.add('active');
        modal.setAttribute('aria-hidden', 'false');
        document.body.style.overflow = 'hidden';
        if (window.lucide) window.lucide.createIcons();
      };
      window.closeTasteQuiz = function() {
        const modal = document.getElementById('tasteQuizModal');
        if (!modal) return;
        modal.classList.remove('active');
        modal.setAttribute('aria-hidden', 'true');
        document.body.style.overflow = '';
      };
      window.selectQuizAnswer = function(step, val) {
        if (step === 1) {
          quizAnswers.mood = val;
          goToQuizStep(2);
        } else if (step === 2) {
          quizAnswers.flavor = val;
          goToQuizStep(3);
        } else if (step === 3) {
          quizAnswers.style = val;
          calculateQuizResult();
        }
      };
      window.prevQuizStep = function(step) {
        goToQuizStep(step);
      };
      function goToQuizStep(step) {
        for (let i = 1; i <= 3; i++) {
          const stepEl = document.getElementById(`quizStep${i}`);
          const dotEl = document.getElementById(`quizDot${i}`);
          const lineEl = document.getElementById(`quizLine${i - 1}`);
          if (stepEl) stepEl.style.display = (i === step) ? 'block' : 'none';
          if (dotEl) dotEl.classList.toggle('active', i <= step);
          if (lineEl) lineEl.classList.toggle('active', i <= step);
        }
        const resultEl = document.getElementById('quizResult');
        if (resultEl) resultEl.style.display = 'none';
      }
      window.resetTasteQuiz = function() {
        quizAnswers = { mood: '', flavor: '', style: '' };
        matchedQuizDrink = null;
        goToQuizStep(1);
      };
      function calculateQuizResult() {
        for (let i = 1; i <= 3; i++) {
          const stepEl = document.getElementById(`quizStep${i}`);
          if (stepEl) stepEl.style.display = 'none';
        }
        const resultEl = document.getElementById('quizResult');
        if (resultEl) resultEl.style.display = 'block';
        const items = getAllMenuItems();
        let targetId = 7; // Default: Cà phê muối
        let reason = "Sự kết hợp bùng nổ giữa vị đắng đậm đà của cà phê và lớp kem muối mặn béo ngậy giúp bạn bừng tỉnh cảm hứng!";
        const { mood, flavor, style } = quizAnswers;
        if (flavor === 'healthy_oats' || (style === 'balanced_mild' && mood === 'chill')) {
          targetId = 9; // ESPRESSO OATSIDE
          reason = "Vị thanh lành, thơm bùi của sữa yến mạch Oatside hòa quyện espresso giúp bạn thư giãn trọn vẹn mà cực kỳ êm bụng.";
        } else if (flavor === 'tea_floral' || mood === 'refresh') {
          if (mood === 'sweet') {
            targetId = 13; // TRÀ VẢI HOA HỒNG
            reason = "Vải ngọt mọng nước cùng hương hoa hồng thanh tao dịu nhẹ mang lại cảm giác ngọt ngào, thư thái đầy thi vị.";
          } else {
            targetId = 15; // TRÀ CHANH DÂY NHIỆT ĐỚI
            reason = "Vị chua ngọt bùng nổ của chanh dây tươi giúp bạn đập tan cơn khát và nạp lại năng lượng sảng khoái ngay tức thì!";
          }
        } else if (flavor === 'creamy_salt' || mood === 'sweet') {
          if (style === 'warm_comfort') {
            targetId = 10; // CACAO LATTE
            reason = "Cacao nguyên chất béo thơm, ấm áp xoa dịu tâm trí sau những giờ làm việc căng thẳng.";
          } else if (mood === 'chill') {
            targetId = 21; // MATCHA LATTE
            reason = "Matcha Nhật Bản thơm lừng hòa cùng sữa béo mịn, mang lại cảm giác bình yên, thư thái tuyệt đối.";
          } else {
            targetId = 7; // CÀ PHÊ MUỐI
            reason = "Lớp kem muối béo ngậy mằn mặn hòa cùng cà phê đậm đà — món Signature được yêu thích nhất tại Olion!";
          }
        } else if (flavor === 'coffee_aroma' || mood === 'focus') {
          if (style === 'warm_comfort') {
            targetId = 6; // AMERICANO
            reason = "Vị espresso thanh tao, sạch vị giúp giữ tinh thần tỉnh táo, minh mẫn cả ngày dài.";
          } else {
            targetId = 2; // ESPRESSO SỮA
            reason = "Espresso đậm đà hòa quyện cùng sữa đặc truyền thống tạo nên nốt vị ngọt đắng trọn vẹn, đánh thức mọi giác quan.";
          }
        }
        matchedQuizDrink = items.find(i => i.id === targetId) || items[0];
        const imgEl = document.getElementById('quizResultImg');
        const tagEl = document.getElementById('quizResultTag');
        const nameEl = document.getElementById('quizResultName');
        const priceEl = document.getElementById('quizResultPrice');
        const descEl = document.getElementById('quizResultDesc');
        const reasonEl = document.getElementById('quizResultReason');
        if (matchedQuizDrink) {
          if (imgEl) {
            imgEl.src = matchedQuizDrink.image_url || 'assets/menu/ca_phe_muoi.webp';
            imgEl.alt = matchedQuizDrink.name + ' — Olion Coffee';
          }
          if (tagEl) tagEl.textContent = matchedQuizDrink.badge || 'SIGNATURE';
          if (nameEl) nameEl.textContent = matchedQuizDrink.name;
          if (priceEl) priceEl.textContent = (Number(matchedQuizDrink.price) || 0).toLocaleString('vi-VN') + 'đ';
          if (descEl) descEl.textContent = matchedQuizDrink.description || '';
          if (reasonEl) reasonEl.innerHTML = `💡 <strong>Tại sao món này hợp với bạn:</strong> ${reason}`;
        }
        if (window.lucide) window.lucide.createIcons();
      }
      window.handleQuizBookTable = function() {
        if (!matchedQuizDrink) return;
        const drinkName = matchedQuizDrink.name;
        const drinkPrice = (Number(matchedQuizDrink.price) || 0).toLocaleString('vi-VN') + 'đ';
        closeTasteQuiz();
        openBookingModal('table', `Khách muốn đặt bàn trước & thưởng thức món ${drinkName} (${drinkPrice})! Nhờ Olion chuẩn bị nhé.`);
      };
      window.handleQuizViewInMenu = function() {
        if (!matchedQuizDrink) return;
        const drinkName = matchedQuizDrink.name;
        closeTasteQuiz();
        const menuSec = document.getElementById('menu');
        if (menuSec) {
          menuSec.scrollIntoView({ behavior: 'smooth' });
        }
        const searchInput = document.getElementById('menuSearchInput');
        if (searchInput) searchInput.value = drinkName;
        filterMenu(drinkName, 'all');
        setTimeout(() => {
          const card = document.querySelector('#searchMenuGrid .menu-card');
          if (card) {
            card.classList.add('menu-card-highlighted');
            setTimeout(() => card.classList.remove('menu-card-highlighted'), 2500);
          }
        }, 400);
      };
      window.addEventListener('storage', (e) => {
        if (e.key === 'olion_minigame') applyMinigameConfig();
      syncSiteSettingsFromCloud();
        if (e.key === 'olion_announcement') applyAnnouncementConfig();
        if (e.key === 'olion_store_settings') applyStoreSettings();
        if (e.key === 'olion_menu_items') syncMenuFromCloud();
      });
      async function syncSiteSettingsFromCloud() {
        console.log("FETCH FUNC TYPE:", typeof fetchSiteSettingsFromCloud); if (typeof fetchSiteSettingsFromCloud !== "function") return;
        const res = await fetchSiteSettingsFromCloud();
        if (res.error) console.log("FETCH ERROR", res.error); if (res.data) { console.log("SYNC SETTINGS_JSON", JSON.stringify(res.data));
           const s = res.data;
           const floatBtn = document.getElementById('wheelFloatBtn');
           if (floatBtn) {
             if (s.is_wheel_active === false) {
               console.log("SETTING NONE"); floatBtn.style.setProperty("display", "none", "important");
               if (typeof closeWheelModal === 'function') closeWheelModal();
             } else {
               floatBtn.style.removeProperty('display');
               floatBtn.style.display = 'flex';
             }
           }
           if (s.wheel_prizes && Array.isArray(s.wheel_prizes) && s.wheel_prizes.length >= 2) {
             prizes = s.wheel_prizes.map(p => ({
               text: p.text || 'Quà tặng',
               code: p.code || 'OLIONGIFT',
               color: p.color || '#E59A55',
               desc: p.desc || (p.text + ' từ Olion Coffee!')
             }));
             if (typeof drawWheel === 'function') drawWheel(0);
           }
           const banner = document.getElementById('announcementBanner');
           if (banner && sessionStorage.getItem('olion_announcement_dismissed') !== 'true') {
             if (s.is_notification_active === false) {
               banner.style.display = 'none';
             } else {
               const textEl = document.getElementById('announcementText');
               if (textEl && s.notification_text) textEl.textContent = s.notification_text;
               banner.style.display = 'block';
             }
           }
        }
      }
      const runDeferredSync = () => {
        applyMinigameConfig();
        syncSiteSettingsFromCloud();
        applyAnnouncementConfig();
        applyStoreSettings();
        syncMenuFromCloud();
        syncApprovedReviews();
        if (typeof supabaseClient !== 'undefined' && supabaseClient) {
          try {
            supabaseClient
              .channel('public:menu_items')
              .on('postgres_changes', { event: '*', schema: 'public', table: 'menu_items' }, payload => {
                syncMenuFromCloud();
              })
              .on('postgres_changes', { event: '*', schema: 'public', table: 'feedbacks' }, payload => {
                syncApprovedReviews();
              })
              .on('postgres_changes', { event: '*', schema: 'public', table: 'site_settings' }, payload => {
                syncSiteSettingsFromCloud();
              })
              .subscribe();
          } catch (e) {
          }
        }
      };
      const scheduleDeferredSync = () => {
        if (typeof window.loadSupabase === 'function') {
          window.loadSupabase(() => {
            if ('requestIdleCallback' in window) {
              requestIdleCallback(runDeferredSync, { timeout: 4000 });
            } else {
              setTimeout(runDeferredSync, 1500);
            }
          });
        } else {
          if ('requestIdleCallback' in window) {
            requestIdleCallback(runDeferredSync, { timeout: 4000 });
          } else {
            setTimeout(runDeferredSync, 2000);
          }
        }
      };
      if (document.readyState === 'complete') {
        setTimeout(scheduleDeferredSync, 2000);
      } else {
        window.addEventListener('load', () => setTimeout(scheduleDeferredSync, 2000), { passive: true, once: true });
      }
      if ('serviceWorker' in navigator) {
        window.addEventListener('load', () => {
          navigator.serviceWorker.register('service-worker.js')
            .then((registration) => {
              console.log('ServiceWorker registration successful');
            }, (err) => {
              console.log('ServiceWorker registration failed: ', err);
            });
        });
      }
      let deferredPrompt = null;
      let detectedPlatform = 'pc';
      const floatingInstallBtn = document.getElementById('floatingInstallBtn');
      const drawerInstallBtn = document.getElementById('drawerInstallBtn');
      window.addEventListener('beforeinstallprompt', (e) => {
        e.preventDefault();
        deferredPrompt = e;
      });
      function detectCurrentPlatform() {
        const ua = navigator.userAgent || navigator.vendor || window.opera || '';
        if (/iPad|iPhone|iPod/.test(ua) || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1)) {
          return 'ios';
        }
        if (/android/i.test(ua)) {
          return 'android';
        }
        return 'pc';
      }
      window.switchInstallPlatform = function(platform) {
        document.querySelectorAll('.app-platform-tab').forEach(tab => tab.classList.remove('active'));
        const activeTab = document.getElementById(
          platform === 'ios' ? 'tabBtnIos' : (platform === 'android' ? 'tabBtnAndroid' : 'tabBtnPc')
        );
        if (activeTab) activeTab.classList.add('active');
        document.querySelectorAll('.platform-content-panel').forEach(panel => panel.classList.remove('active'));
        const activePanel = document.getElementById(
          platform === 'ios' ? 'panelIos' : (platform === 'android' ? 'panelAndroid' : 'panelPc')
        );
        if (activePanel) activePanel.classList.add('active');
        if (window.lucide) window.lucide.createIcons();
      };
      const handleInstall = () => {
        const modal = document.getElementById('downloadAppModal');
        if (!modal) return;
        modal.classList.add('active');
        detectedPlatform = detectCurrentPlatform();
        const badgeIos = document.getElementById('badgeIos');
        const badgeAndroid = document.getElementById('badgeAndroid');
        const badgePc = document.getElementById('badgePc');
        if (badgeIos) badgeIos.style.display = (detectedPlatform === 'ios') ? 'inline-block' : 'none';
        if (badgeAndroid) badgeAndroid.style.display = (detectedPlatform === 'android') ? 'inline-block' : 'none';
        if (badgePc) badgePc.style.display = (detectedPlatform === 'pc') ? 'inline-block' : 'none';
        switchInstallPlatform(detectedPlatform);
      };
      window.showInstallGuideDetail = function(platform) {
        switchInstallPlatform(platform);
        if (window.showOlionToast) {
          window.showOlionToast('Đã mở hướng dẫn cài đặt iOS!', 'apple');
        }
      };
      window.handleAndroidInstall = async function() {
        if (typeof deferredPrompt !== 'undefined' && deferredPrompt !== null) {
          deferredPrompt.prompt();
          const { outcome } = await deferredPrompt.userChoice;
          if (outcome === 'accepted') {
            if (window.showOlionToast) window.showOlionToast('Cảm ơn bạn đã cài đặt Olion Coffee!', 'check-circle');
            document.getElementById('downloadAppModal')?.classList.remove('active');
          }
          deferredPrompt = null;
        } else {
          switchInstallPlatform('android');
          if (window.showOlionToast) {
            window.showOlionToast('Vui lòng làm theo hướng dẫn ở bên dưới để cài đặt!', 'smartphone');
          }
        }
      };
      window.handlePcInstall = async function() {
        if (typeof deferredPrompt !== 'undefined' && deferredPrompt !== null) {
          deferredPrompt.prompt();
          const { outcome } = await deferredPrompt.userChoice;
          if (outcome === 'accepted') {
            if (window.showOlionToast) window.showOlionToast('Cảm ơn bạn đã cài đặt App trên máy tính!', 'check-circle');
            document.getElementById('downloadAppModal')?.classList.remove('active');
          }
          deferredPrompt = null;
        } else {
          switchInstallPlatform('pc');
          if (window.showOlionToast) {
            window.showOlionToast('Xem hướng dẫn biểu tượng cài đặt [⊕] trên thanh địa chỉ URL!', 'monitor');
          }
        }
      };
      if (floatingInstallBtn) floatingInstallBtn.addEventListener('click', handleInstall);
      if (drawerInstallBtn) drawerInstallBtn.addEventListener('click', handleInstall);
      window.shareApp = async () => {
        if (navigator.share) {
          try {
            await navigator.share({
              title: 'Olion Coffee',
              text: 'Góc nhỏ bình yên giữa lòng Sài Gòn. Khám phá menu cà phê thủ công tinh tế ngay!',
              url: window.location.href,
            });
          } catch (err) {
            console.log('User cancelled share or error:', err);
          }
        } else {
          navigator.clipboard.writeText(window.location.href);
          showOlionToast('Đã sao chép link website!', '🔗');
        }
      };
    });