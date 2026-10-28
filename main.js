document.addEventListener("DOMContentLoaded",()=>{const e=()=>{window.lucide&&"function"==typeof window.lucide.createIcons&&(window.lucide.createIcons(),window._lucideReady=!0)};"requestIdleCallback"in window?requestIdleCallback(e,{timeout:1200}):setTimeout(e,100);const t={vi:{nav_amenities:"Tiện ích",nav_about:"Về Olion",nav_signature:"Signature",nav_menu:"Thực đơn",nav_spaces:"Không gian",nav_services:"Đặt bàn & Dịch vụ",nav_news:"Tin tức",nav_faq:"Hỏi đáp",nav_contact:"Liên hệ",nav_feedback:"Góp ý quán",nav_loyalty:"Tích điểm",drawer_home:"Trang chủ",drawer_amenities:"Tiện ích & Không gian",drawer_about:"Về Olion Coffee",drawer_signature:"Món Signature",drawer_menu:"Thực đơn đồ uống",drawer_menu_board:"Bảng Menu Tổng (Toàn Trang)",drawer_spaces:"Không gian quán",drawer_services:"Đặt bàn & Thuê không gian",drawer_news:"Tin tức & Sự kiện",drawer_faq:"Hỏi đáp",drawer_contact:"Thông tin liên hệ",drawer_call:"Gọi Hotline: 0783 657 587",drawer_feedback:"Góp ý & Đánh giá",drawer_loyalty:"Tra Cứu Điểm Tích Lũy",drawer_lang_label:"Ngôn ngữ / Language:",dock_home:"Trang chủ",dock_menu:"Thực đơn",dock_spaces:"Không gian",dock_contact:"Liên hệ",hero_eyebrow:"OLION COFFEE · ELEGANCE IN EVERY SIP",hero_title:'OLION COFFEE <span style="color: var(--accent-gold); font-weight: 300;">—</span><br><span class="italic-gold">Cà Phê Gò Vấp Không Gian Yên Tĩnh & Fine Dining</span>',hero_subtitle:"Quán cà phê đẹp ở Dương Quảng Hàm, Gò Vấp với không gian sang trọng và đồ uống thủ công tinh tế. Thưởng thức hương vị nguyên bản, đắm chìm trong góc nhỏ tĩnh lặng giữa lòng Sài Gòn.",hero_cta_menu:"Khám phá thực đơn →",hero_cta_about:"Câu chuyện quán",stats_items_count:"Món trong menu",stats_categories:"Danh mục đồ uống",stats_handcrafted:"Pha thủ công",stats_days_open:"Ngày mở cửa/năm",about_eyebrow:"● Về Olion Coffee",about_title:'Chắt chiu từng giọt,<br><span class="accent">trao hương vị tinh tế</span>.',about_desc:"Trời trưa hơi gắt, ghé OLION thả lưng xuống chiếc ghế quen, ngắm ánh đèn vàng dịu mắt và làm ngụm nước mát lạnh rồi tỉnh tiếp nha. Không chỉ là cà phê, OLION muốn đem tới trải nghiệm trọn vẹn: đồ uống pha tay tỉ mỉ, không gian ấm cúng và những khoảnh khắc thật chậm.",about_feat_1_title:"Pha thủ công",about_feat_1_desc:"Từng ly được pha chế tỉ mỉ tại quầy",about_feat_2_title:"Nguyên liệu chọn lọc",about_feat_2_desc:"Hạt mộc rang xay & trà cao cấp",about_feat_3_title:"Không gian yên tĩnh",about_feat_3_desc:"Góc làm việc & thư giãn ấm cúng",about_feat_4_title:"Phục vụ tận tâm",about_feat_4_desc:"Nụ cười và sự chu đáo mỗi ngày",sig_eyebrow:"Món Bán Chạy",sig_title:'Món <span class="accent">Signature</span> của quán',sig_desc:"Ba công thức độc quyền được khách hàng yêu thích nhất tại Olion Coffee.",sig_item_1_name:"MATCHA LATTE",sig_item_1_desc:"Matcha Nhật Bản thượng hạng thơm thanh đậm vị quyện cùng sữa tươi béo dịu, tạo nên cảm giác thư thái tươi mát trọn vẹn.",sig_item_2_name:"CACAO BẠC HÀ",sig_item_2_desc:"Sự the mát sảng khoái của bạc hà hòa quyện hoàn hảo cùng vị đắng dịu của cacao nguyên chất béo thơm.",sig_item_3_name:"CÀ PHÊ MUỐI OLION",sig_item_3_desc:"Cà phê Robusta rang mộc đậm đà hòa quyện cùng lớp kem muối béo mặn độc quyền của Olion, tạo nên trải nghiệm vị giác đầy lôi cuốn.",menu_eyebrow:"● Thực Đơn Đa Dạng",menu_title:'Khám phá <span class="accent">món ngon</span> yêu thích',menu_desc:"Cà phê rang xay, trà sữa đậm vị, nước ép và sữa chua tươi mát — chọn danh mục để xem chi tiết.",menu_tab_board:"MENU TỔNG",menu_tab_coffee:"Cà Phê",menu_tab_tea:"Trà Trái Cây",menu_tab_matcha:"Matcha",menu_tab_cacao:"Cacao",menu_tab_juice:"Nước Ép",menu_tab_yagout:"Sữa Chua",menu_tab_topping:"Topping",spaces_eyebrow:"● Không Gian Quán",spaces_title:'Nơi dừng chân <span class="accent">ấm áp</span>',spaces_desc:"Góc nhỏ tĩnh lặng để làm việc, trò chuyện cùng bạn bè hoặc đơn giản là ngắm nhìn phố thị qua khung kính.",space_card_1:"Quầy pha chế thủ công",space_card_2:"Góc thư giãn & chuyện trò",space_card_3:"Góc làm việc yên tĩnh",space_card_4:"Toàn cảnh ấm cúng",news_eyebrow:"● Bản Tin & Sự Kiện",news_title:'Tin tức & <span class="accent">Sự kiện</span>',news_desc:"Khám phá những khoảnh khắc đáng nhớ, câu chuyện thức uống và các hoạt động mới nhất tại Olion Coffee.",news_read_more:"Xem chi tiết →",faq_eyebrow:"● Hỏi Đáp Nhanh",faq_title:'Bạn <span class="accent">thắc mắc?</span>',faq_q1:"OLION COFFEE có giao hàng tận nơi không?",faq_a1:"Dịch vụ giao tận nơi đang được Olion chuẩn bị và sẽ sớm ra mắt trong thời gian tới! Hiện tại, Olion tập trung mang đến trải nghiệm không gian tốt nhất khi bạn ghé quán trực tiếp hoặc đặt bàn trước qua website / hotline 0783 657 587.",faq_q2:"Nguyên liệu và Cà phê của OLION có gì đặc biệt?",faq_a2:"Olion Coffee sử dụng 100% hạt Robusta & Arabica rang mộc nguyên chất từ nông trại Cầu Đất, bột Matcha nhập khẩu Nhật Bản và trái cây tươi mỗi ngày, tuyệt đối không sử dụng hương liệu nhân tạo hay chất bảo quản.",faq_q3:"Có thể điều chỉnh độ ngọt và lượng đá theo khẩu vị không?",faq_a3:"Hoàn toàn được! Bạn có thể yêu cầu barista gia giảm mức ngọt (0%, 30%, 50%, 70%, 100%) và lượng đá tùy thích, hoặc yêu cầu đổi sang sữa yến mạch Oatside để phù hợp với chế độ ăn uống của mình.",reviews_eyebrow:"● Cảm Nhận Khách Hàng",reviews_title:'Khách hàng <span class="accent">nói gì</span> về Olion?',reviews_desc:"Được chấm 4.9/5.0 từ hơn 280+ đánh giá thực tế trên Google Maps và Facebook.",review_1_quote:'"Quán nằm trong hẻm yên tĩnh ở Dương Quảng Hàm, bước vào cảm giác như tách biệt khỏi xô bồ ngoài kia. Đèn vàng ấm mắt, bàn ghế gỗ cao ngồi làm việc cả buổi rất thoải mái. Cà phê muối béo mặn cực kỳ vừa miệng!"',review_1_role:"Sinh viên ĐH Văn Lang",review_2_quote:'"Matcha latte ở đây chuẩn vị Nhật, thơm đắng thanh nhẹ và không bị ngọt gắt như nhiều chỗ khác. Tụi mình hay ghé đây đọc sách và trò chuyện cuối tuần vì nhạc mở vừa phải rất dễ chịu."',review_2_role:"Graphic Designer",review_3_quote:'"Bạc xỉu kem trứng ngon đỉnh chóp! Lớp bọt trứng béo mịn uống tới đâu dính tới đó. Nhân viên thân thiện, nhiệt tình châm trà liên tục. Chắc chắn sẽ là quán ruột của mình."',review_3_role:"Freelancer Gò Vấp",review_btn:"Gửi đánh giá của bạn →",contact_eyebrow:"● Thông Tin Liên Hệ",contact_title:'Bạn <span class="accent">muốn ghé</span> chơi?',contact_addr_title:"Địa chỉ quán",contact_hotline_title:"Hotline đặt bàn & hỗ trợ",contact_social_title:"Kênh mạng xã hội",hours_title:"Giờ mở cửa",hours_weekday_label:"Thứ 2 — Thứ 7",hours_weekend_label:"Chủ Nhật",hours_holiday_label:"Các ngày Lễ / Tết",hours_holiday_val:"Mở cửa bình thường",hours_quote:'"Trời trưa hơi gắt, ghé OLION thả lưng xuống chiếc ghế quen, ngắm ánh đèn vàng dịu mắt và làm ngụm nước mát lạnh rồi tỉnh tiếp nha."',footer_explore:"Khám Phá",footer_links:"Liên Kết",footer_rights:"© 2024 Olion Coffee. All rights reserved.",footer_credit:"Thiết kế & Vận hành bởi Olion Creative Studio",loyalty_eyebrow:"Thành Viên Olion",loyalty_title:"Tra Cứu Điểm Tích Lũy",loyalty_desc:"Nhập số điện thoại để kiểm tra số điểm hiện có và các ưu đãi đang chờ bạn!",loyalty_input_label:"Số điện thoại của bạn",loyalty_phone_placeholder:"Ví dụ: 0908123456",loyalty_btn_lookup:"Tra Cứu",loyalty_current_points:"Điểm tích lũy",wheel_float:"Quay Nhận Quà",back_to_top:"Lên đầu trang",amenities_eyebrow:'<span class="eyebrow-num">✦</span> Tiện Ích & Không Gian Làm Việc',amenities_title:'Tiện Nghi Hoàn Hảo Cho <span class="accent">Làm Việc & Thư Giãn</span>',amenities_desc:"Không gian tĩnh lặng, trang bị đầy đủ ổ điện từng bàn, wifi 5G cực nhanh và bãi đỗ xe an ninh — sẵn sàng đồng hành cùng bạn học tập, chạy deadline và thưởng thức cà phê."},en:{nav_amenities:"Amenities",nav_about:"About Us",nav_signature:"Signatures",nav_menu:"Menu",nav_spaces:"Ambiance",nav_services:"Booking & Space",nav_news:"News",nav_faq:"FAQ",nav_contact:"Contact",nav_feedback:"Feedback",nav_loyalty:"Loyalty",drawer_home:"Home",drawer_amenities:"Amenities & Workspaces",drawer_about:"About Olion Coffee",drawer_signature:"Signature Drinks",drawer_menu:"Beverage Menu",drawer_menu_board:"Full Menu Board (Fullscreen)",drawer_spaces:"Our Spaces",drawer_services:"Table Booking & Space Rental",drawer_news:"News & Events",drawer_faq:"FAQ",drawer_contact:"Contact Info",drawer_call:"Call Hotline: 0783 657 587",drawer_feedback:"Feedback & Reviews",drawer_loyalty:"Check Loyalty Points",drawer_lang_label:"Ngôn ngữ / Language:",dock_home:"Home",dock_menu:"Menu",dock_spaces:"Spaces",dock_contact:"Contact",hero_eyebrow:"OLION COFFEE · ELEGANCE IN EVERY SIP",hero_title:'OLION COFFEE <span style="color: var(--accent-gold); font-weight: 300;">—</span><br><span class="italic-gold">Fine Dining & Quiet Coffee Sanctuary in Go Vap</span>',hero_subtitle:"An exquisite boutique cafe on Duong Quang Ham, Go Vap, offering a luxurious ambiance and meticulously handcrafted beverages. Taste authentic flavors and immerse in serene tranquility in the heart of Saigon.",hero_cta_menu:"Explore Menu →",hero_cta_about:"Our Story",stats_items_count:"Items in Menu",stats_categories:"Drink Categories",stats_handcrafted:"Handcrafted",stats_days_open:"Days Open / Year",about_eyebrow:"● About Olion Coffee",about_title:'Crafting every drop,<br><span class="accent">delivering pure elegance</span>.',about_desc:"When noon gets too hectic, drop by OLION, sink into your favorite armchair, admire the gentle amber glow, and enjoy a crisp iced beverage before continuing your day. More than just coffee, OLION is dedicated to a complete experience: meticulously handcrafted drinks, cozy space, and slow, meaningful moments.",about_feat_1_title:"Handcrafted",about_feat_1_desc:"Every single cup prepared with care at the bar",about_feat_2_title:"Selected Ingredients",about_feat_2_desc:"Artisan roasted beans & premium whole-leaf tea",about_feat_3_title:"Tranquil Space",about_feat_3_desc:"Cozy nook for productive work & gentle relaxation",about_feat_4_title:"Heartfelt Service",about_feat_4_desc:"Warm smiles and attentive care every day",sig_eyebrow:"Bestsellers",sig_title:'House <span class="accent">Signature</span> Drinks',sig_desc:"Three exclusive recipes most beloved by guests at Olion Coffee.",sig_item_1_name:"JAPANESE MATCHA LATTE",sig_item_1_desc:"Premium ceremonial-grade Japanese matcha infused with silky fresh milk, delivering a crisp, refreshing, and calming indulgence.",sig_item_2_name:"MINT CACAO",sig_item_2_desc:"The refreshing coolness of mint perfectly blended with the gentle bitterness of pure, rich cacao.",sig_item_3_name:"OLION SALTED CREAM COFFEE",sig_item_3_desc:"Bold artisanal Robusta coffee harmoniously blended with Olion's proprietary velvety salted cream, creating an irresistible flavor journey.",menu_eyebrow:"● Diverse Menu",menu_title:'Discover your <span class="accent">favorite drink</span>',menu_desc:"From bold traditional coffee and refreshing fruit teas to creamy ice-blended frappes and delightful snacks.",menu_tab_board:"FULL MENU",menu_tab_coffee:"Coffee",menu_tab_tea:"Fruit Tea",menu_tab_matcha:"Matcha",menu_tab_cacao:"Cacao",menu_tab_juice:"Juice",menu_tab_yagout:"Yogurt",menu_tab_topping:"Topping",spaces_eyebrow:"● Our Spaces",spaces_title:'A <span class="accent">warm & cozy</span> sanctuary',spaces_desc:"A serene corner to work, catch up with friends, or simply gaze out at the city streets through the glass window.",space_card_1:"Artisanal Brew Bar",space_card_2:"Cozy Chat & Relax Corner",space_card_3:"Quiet Workspace Corner",space_card_4:"Panoramic Cozy Atmosphere",news_eyebrow:"● News & Events",news_title:'Life at <span class="accent">Olion</span>',news_desc:"Stay updated with promotions, acoustic nights, and stories behind every cup of coffee.",news_read_more:"Read more →",faq_eyebrow:"● FAQ",faq_title:'Frequently Asked <span class="accent">Questions</span>',faq_q1:"Does OLION COFFEE offer delivery?",faq_a1:"Our delivery service is currently in preparation and will launch soon! At the moment, Olion focuses on providing the best experience at the cafe or via advance table booking through our website or hotline 0783 657 587.",faq_q2:"What is special about OLION's ingredients and coffee?",faq_a2:"Olion Coffee uses 100% pure roasted Robusta & Arabica beans from Cau Dat farm, imported Japanese Matcha powder, and fresh fruit daily. We absolutely do not use artificial flavors or preservatives.",faq_q3:"Can I adjust the sweetness and ice level?",faq_a3:"Absolutely! You can ask the barista to adjust the sweetness level (0%, 30%, 50%, 70%, 100%) and ice amount as you prefer, or request a switch to Oatside oat milk to suit your diet.",reviews_eyebrow:"● Customer Voices",reviews_title:'Guest <span class="accent">Impressions</span>',reviews_desc:"Heartfelt thoughts and genuine shares from friends who visit and love Olion.",review_1_quote:'"The cafe is nestled in a quiet alley on Duong Quang Ham, stepping in feels like you\'re separated from the hustle and bustle outside. Warm amber lights, tall wooden chairs that are comfortable to sit and work in all day. The salted coffee is perfectly balanced!"',review_1_role:"Van Lang University Student",review_2_quote:'"The matcha latte here tastes authentically Japanese, refreshingly bitter and not overly sweet like many other places. We often drop by to read books and chat on weekends because the music is set at a very comfortable volume."',review_2_role:"Graphic Designer",review_3_quote:'"The egg cream bac xiu is top-notch! The creamy egg foam is addictive. The staff is friendly and enthusiastically refills our tea constantly. Will definitely be a regular here."',review_3_role:"Freelancer in Go Vap",review_btn:"Send your feedback →",contact_eyebrow:"● Visit Us",contact_title:'Connect with <span class="accent">Olion</span>',contact_addr_title:"Our Address",contact_hotline_title:"Hotline Booking & Support",contact_social_title:"Social Media Channels",hours_title:"Opening Hours",hours_weekday_label:"Mon — Sat",hours_weekend_label:"Sunday",hours_holiday_label:"Public Holidays / Tet",hours_holiday_val:"Open as Normal",hours_quote:'"When noon gets too hectic, drop by OLION, sink into your favorite armchair, admire the gentle amber glow, and enjoy a crisp iced beverage before continuing your day."',footer_explore:"Explore",footer_links:"Links",footer_rights:"© 2024 Olion Coffee. All rights reserved.",footer_credit:"Designed & Operated by Olion Creative Studio",loyalty_eyebrow:"Olion Member Club",loyalty_title:"Check Loyalty Points",loyalty_desc:"Enter your phone number to check your current points and available rewards!",loyalty_input_label:"Your Phone Number",loyalty_phone_placeholder:"e.g. 0908123456",loyalty_btn_lookup:"Check Points",loyalty_current_points:"Current Points",loyalty_pts_unit:"pts",wheel_float:"Spin & Win",back_to_top:"Back to top",amenities_eyebrow:'<span class="eyebrow-num">✦</span> Amenities & Workspaces',amenities_title:'Perfect Amenities For <span class="accent">Work & Relaxation</span>',amenities_desc:"A serene atmosphere equipped with individual table power outlets, ultra-fast 5G Wifi, and secure parking — ready to support your study sessions, deadlines, and coffee moments."}};let n=localStorage.getItem("olion_lang")||"vi";function o(e,t){const n=document.createElement("textarea");n.value=e,n.style.position="fixed",n.style.left="-9999px",document.body.appendChild(n),n.select();try{document.execCommand("copy"),window.showOlionToast&&window.showOlionToast(t,"wifi")}catch(t){window.showOlionToast&&window.showOlionToast("Mật khẩu Wifi: "+e,"wifi")}document.body.removeChild(n)}window.setLanguage=function(e){t[e]||(e="vi"),n=e,localStorage.setItem("olion_lang",e);const o=t[e];document.querySelectorAll("[data-i18n]").forEach(e=>{const t=e.getAttribute("data-i18n");void 0!==o[t]&&(e.innerHTML=o[t])}),document.querySelectorAll("[data-i18n-placeholder]").forEach(e=>{const t=e.getAttribute("data-i18n-placeholder");void 0!==o[t]&&(e.placeholder=o[t])}),document.querySelectorAll("[data-i18n-title]").forEach(e=>{const t=e.getAttribute("data-i18n-title");void 0!==o[t]&&(e.setAttribute("title",o[t]),e.setAttribute("aria-label",o[t]))});const a="vi"===e,i=document.getElementById("langPillVi"),c=document.getElementById("langPillEn"),s=document.getElementById("langPillViMobile"),l=document.getElementById("langPillEnMobile");i&&i.classList.toggle("active",a),c&&c.classList.toggle("active",!a),s&&s.classList.toggle("active",a),l&&l.classList.toggle("active",!a),document.documentElement.setAttribute("lang",e),"function"==typeof window.updateDynamicGreeting&&window.updateDynamicGreeting(e)},window.copyWifiPassword=function(){const e=document.getElementById("wifiPassCodeVal")?.textContent.trim()||"12345678@",t="vi"===n?"Đã sao chép mật khẩu Wifi: "+e:"Wifi password copied: "+e;navigator.clipboard&&navigator.clipboard.writeText?navigator.clipboard.writeText(e).then(()=>{window.showOlionToast&&window.showOlionToast(t,"wifi")}).catch(()=>{o(e,t)}):o(e,t)};try{let e=parseInt(localStorage.getItem("olion_visit_count")||"0",10)+1;localStorage.setItem("olion_visit_count",e.toString())}catch(e){}window.updateDynamicGreeting=function(e=n){if(!document.getElementById("dynamicQuoteBox"))return;const t=function(e=n){const t=new Date,o=t.getHours()+t.getMinutes()/60;let a="";try{if(a=(localStorage.getItem("olion_customer_name")||"").trim(),!a){const e=JSON.parse(localStorage.getItem("olion_feedbacks")||"[]");e.length>0&&e[0].name&&"Khách ghé quán"!==e[0].name&&(a=e[0].name.trim())}}catch(e){}const i="vi"===e,c=a?i?`Chào ${a}! `:`Hi ${a}! `:"";return o>=6&&o<10.5?{icon:"sunrise",tag:i?"Chào Buổi Sáng":"Good Morning",quote:i?`${c}"Sáng sớm trong lành, ghé OLION nhâm nhi một tách cà phê thơm nồng, khởi động ngày mới tràn đầy hứng khởi và năng lượng tích cực nhé!"`:`${c}"Crisp morning air pairs best with a fragrant brew at OLION. Kick off your brand-new day filled with positive energy and clarity!"`}:o>=10.5&&o<13.5?{icon:"sun",tag:i?"Buổi Trưa Mát Lành":"Midday Cool Breeze",quote:i?`${c}"Trời trưa hơi gắt, ghé OLION thả lưng xuống chiếc ghế quen, ngắm ánh đèn vàng dịu mắt và làm ngụm nước mát lạnh rồi tỉnh tiếp nha."`:`${c}"When the midday sun gets a bit intense, find your nook at OLION, unwind in a cozy chair, and recharge with an icy crisp beverage."`}:o>=13.5&&o<17?{icon:"sun-medium",tag:i?"Xế Chiều Năng Lượng":"Afternoon Boost",quote:i?`${c}"Đầu giờ chiều hơi uể oải, hãy tự thưởng cho mình một ly Trà Trái Cây mát lạnh hoặc Cà Phê Muối đậm vị để nạp lại 100% cảm hứng làm việc nhé."`:`${c}"Beat the afternoon slump with a refreshing fruit tea or our signature salted cream coffee. 100% inspiration restored!"`}:o>=17&&o<19?{icon:"sunset",tag:i?"Chiều Tà Thảnh Thơi":"Golden Hour Dusk",quote:i?`${c}"Tan ca rồi, bỏ lại sau lưng mọi deadline bộn bề. Ghé OLION chuyện trò cùng bạn bè hoặc ngắm phố xá lên đèn bên ly Bạc Xỉu ngọt ngào nhé."`:`${c}"Clock-out time! Leave the deadlines behind, gather with friends, or watch the city lights awaken over a sweet, soothing egg-foam coffee."`}:o>=19&&o<21.5?{icon:"moon",tag:i?"Buổi Tối Ấm Cúng":"Cozy Evening Vibe",quote:i?`${c}"Phố xá về đêm thật đẹp. Trong không gian đèn vàng ấm cúng và giai điệu nhạc êm đềm tại OLION, cùng nhâm nhi ly nước yêu thích và chill thôi nào."`:`${c}"The city glimmers at night. Sink into our warm amber glow, enjoy mellow acoustic tunes, and savor your favorite handcrafted drink."`}:{icon:"sparkles",tag:i?"Chúc Bạn Ngủ Ngon":"Good Night & Sweet Dreams",quote:i?`${c}"OLION đã khép lại sau một ngày phục vụ thân thương. Chúc bạn một giấc ngủ thật ngon và hẹn gặp lại bạn vào sớm mai với những tách cà phê thơm lừng!"`:`${c}"OLION has closed for the night. Rest well tonight, and we look forward to welcoming you tomorrow morning with fresh artisanal brews!"`}}(e),o=document.getElementById("quoteIcon"),a=document.getElementById("quoteTimeLabel"),i=document.getElementById("quoteText");o&&(o.innerHTML=`<i data-lucide="${t.icon}" style="width:16px;height:16px;"></i>`,window._lucideReady&&window.lucide&&window.lucide.createIcons()),a&&(a.textContent=t.tag),i&&(i.textContent=t.quote)},window.toggleLanguage=function(){const e="vi"===n?"en":"vi";window.setLanguage(e),window.showOlionToast&&window.showOlionToast("vi"===e?"Đã đổi sang Tiếng Việt 🇻🇳":"Switched to English 🇬🇧","🌐")},setLanguage(n),updateDynamicGreeting(n),setInterval(()=>{"function"==typeof window.updateDynamicGreeting&&window.updateDynamicGreeting(n)},3e5);let a=null,i=null;const c=[{name:"Gò Vấp",lat:10.8386,lon:106.6653,isHome:!0},{name:"Bình Thạnh",lat:10.8106,lon:106.7091},{name:"Phú Nhuận",lat:10.7992,lon:106.6802},{name:"Tân Bình",lat:10.8015,lon:106.655},{name:"Tân Phú",lat:10.79,lon:106.628},{name:"Quận 12",lat:10.8672,lon:106.6412},{name:"Thủ Đức",lat:10.8494,lon:106.7537},{name:"Quận 1",lat:10.7756,lon:106.7004},{name:"Quận 3",lat:10.7844,lon:106.6844},{name:"Quận 10",lat:10.7716,lon:106.6674},{name:"Quận 5",lat:10.7554,lon:106.6631},{name:"Quận 7",lat:10.734,lon:106.7218},{name:"Bình Tân",lat:10.7653,lon:106.6037},{name:"Hóc Môn",lat:10.8841,lon:106.5925}];async function s(){let e=10.8231,t=106.6297,n="TP.HCM",o=!1,a=!0;try{const i=await fetch("https://get.geojs.io/v1/ip/geo.json");if(i.ok){const s=await i.json();if(s.latitude&&s.longitude){e=parseFloat(s.latitude),t=parseFloat(s.longitude);const i=function(e,t){let n="TP.HCM",o=999999,a=!1;return c.forEach(i=>{const c=Math.hypot(e-i.lat,t-i.lon);c<o&&(o=c,n=i.name,a=Boolean(i.isHome))}),o>.4?{district:"TP.HCM",isHome:!1,isNear:!1}:{district:n,isHome:a||"Gò Vấp"===n,isNear:["Gò Vấp","Bình Thạnh","Phú Nhuận","Tân Bình","Quận 12","Tân Phú"].includes(n)}}(e,t);n=i.district,o=i.isHome,a=i.isNear}}}catch(e){}try{const c=await fetch(`https://api.open-meteo.com/v1/forecast?latitude=${e}&longitude=${t}&current=temperature_2m,weather_code,is_day,relative_humidity_2m&timezone=Asia%2FHo_Chi_Minh`);if(!c.ok)throw new Error("Weather fetch failed");const s=await c.json(),l=Math.round(s.current.temperature_2m),r=s.current.weather_code,d=s.current.is_day;let u="trời đẹp",m=d?"sun":"moon",h=!1,g=l>=32;return 0===r?(u=d?"trời nắng trong":"trời quang đãng",m=d?"sun":"sparkles"):[1,2,3].includes(r)?(u="trời mát mẻ có mây",m="cloud-sun"):[51,53,55,61,63,65,80,81,82].includes(r)?(u="trời đang mưa rào",m="cloud-rain",h=!0):[95,96,99].includes(r)&&(u="trời có dông mưa",m="cloud-lightning",h=!0),i={temp:l,statusText:u,icon:m,isRain:h,isHot:g,locationName:n,isHome:o,isNear:a},i}catch(e){return i={temp:27,statusText:"mát dịu",icon:"sun-medium",isRain:!1,isHot:!1,locationName:n,isHome:o,isNear:a},i}}async function l(){if(/Lighthouse|HeadlessChrome|Chrome-Lighthouse|bot/i.test(navigator.userAgent)||window.location.search.includes("no_welcome"))return;await new Promise(e=>setTimeout(e,3500));const e=document.getElementById("welcomeModal");if(!e)return;const t=await s(),n=(localStorage.getItem("olion_customer_name")||"").trim(),o=Boolean(n),i=function(e,t){const n=(new Date).getHours(),{temp:o,statusText:a,isRain:i,isHot:c,locationName:s,isHome:l}=t;let r="",d="";return n>=5&&n<8?(r="Sáng Sớm",d=i?`Khu vực ${s} sáng sớm trời mưa nhẹ ${o}°C. Ghé Olion trú mưa nhâm nhi tách Cà phê nóng đánh thức mọi giác quan nhé!`:l?`Sáng sớm Gò Vấp trong lành ${o}°C! Quán ở 80/64A Dương Quảng Hàm rất gần bạn đấy, ghé Olion làm ly Espresso pha thủ công thức tỉnh ngày mới nhé.`:`Sáng sớm tại ${s} thật trong lành (${o}°C). Một ly Cà phê mộc pha thủ công tại Olion sẽ nạp đầy năng lượng cho bạn!`):n>=8&&n<11?(r="Buổi Sáng",d=i?`Trời ${s} đang mưa rào (${o}°C). Trú mưa tại góc quán ấm cúng Olion cùng một ly Cà Phê Muối béo mặn nhé!`:l?`Buổi sáng Gò Vấp đầy hứng khởi (${o}°C, ${a})! Ghé ngay 80/64A Dương Quảng Hàm nạp năng lượng với Cà Phê Muối hay Bạc Xỉu Olion nha.`:`Buổi sáng tại ${s} ngập tràn hứng khởi (${o}°C, ${a}). Nạp 100% năng lượng ngày mới cùng Cà Phê Muối độc quyền Olion!`):n>=11&&n<14?(r="Buổi Trưa",d=c?`Trời ${s} trưa nay khá oi bức (${o}°C). Ghé Olion trốn nắng trong không gian mát lành và thưởng thức ly Trà Trái Cây mát lạnh giải nhiệt tức thì!`:l?`Trưa nay ở Gò Vấp (${o}°C), ghé Olion thả lưng xuống chiếc ghế quen, ngắm ánh đèn vàng dịu mắt và làm ngụm nước mát lạnh rồi tiếp tục ngày dài nhé.`:`Trời trưa ${s} êm dịu ${o}°C. Ghé Olion thả lưng xuống chiếc ghế quen, thưởng thức đồ uống mát lạnh và nạp lại năng lượng nhé.`):n>=14&&n<17?(r="Xế Chiều",d=i?`Chiều ${s} có mưa lất phất (${o}°C). Một ly Matcha Latte ấm thơm sẽ giúp bạn thư giãn và xua tan mệt mỏi!`:`Xế chiều tại ${s} dễ uể oải (${o}°C). Tự thưởng cho mình một ly Matcha Latte thanh mát hay Trà Đào thanh dịu để lấy lại cảm hứng làm việc nhé!`):n>=17&&n<19?(r="Chiều Tối",d=l?`Tan tầm rồi! Gác lại deadline, ghé ngay Olion 80/64A Dương Quảng Hàm (${o}°C) ngắm phố xá lên đèn và thưởng thức ly Bạc Xỉu ngọt ngào xả stress nhé.`:`Tan tầm rồi (${s} ${o}°C)! Gác lại mọi deadline, cùng bạn bè ghé Olion ngắm phố xá lên đèn và thưởng thức ly Bạc Xỉu ngọt ngào xả stress thôi nào.`):n>=19&&n<22?(r="Buổi Tối",d=`Phố đêm ${s} lung linh trong tiết trời ${o}°C dễ chịu. Không gian đèn vàng ấm cúng và những giai điệu êm dịu tại Olion đang chờ bạn ghé chơi.`):(r="Đêm Muộn",d=`Đêm muộn tại ${s} thật yên tĩnh (${o}°C). Chúc bạn một buổi tối an lành, thư thái và có một giấc ngủ thật ngon nhé!`),{timeSlot:r,title:e?`Chào mừng ${e} trở lại!`:"Chào mừng bạn ghé chơi!",message:`${e?`Chào ${e}`:"Chào bạn"}! ${d}`}}(n,t),c=document.getElementById("welcomeWeatherIcon"),l=document.getElementById("welcomeWeatherText"),d=document.getElementById("welcomeTitle"),u=document.getElementById("welcomeMessage");c&&(c.innerHTML=`<i data-lucide="${t.icon}" style="width:18px;height:18px;"></i>`,window.lucide&&window.lucide.createIcons()),l&&(l.textContent=`${t.locationName} ${t.temp}°C • ${i.timeSlot}`),d&&(d.textContent=i.title),u&&(u.textContent=i.message);const m=document.getElementById("welcomeNewUserArea"),h=document.getElementById("welcomeReturningUserArea"),g=document.getElementById("welcomeProgressBar");o?(m&&(m.style.display="none"),h&&(h.style.display="block"),g&&(g.style.display="block"),function(e=1e4){const t=document.getElementById("welcomeProgressBar");t&&(t.classList.remove("paused"),t.style.animation="none",requestAnimationFrame(()=>{requestAnimationFrame(()=>{t&&(t.style.animation=`welcomeCountdown ${e/1e3}s linear forwards`,t.style.display="block")})}));clearTimeout(a),a=setTimeout(()=>{closeWelcomeModal()},e)}(1e4)):(m&&(m.style.display="block"),h&&(h.style.display="none"),g&&(g.style.display="none"),clearTimeout(a),a=null),e.classList.add("active"),e.setAttribute("aria-hidden","false");const y=document.getElementById("welcomeBox")||e.querySelector(".welcome-box");if(y){["focusin","click","keydown","touchstart","input","mouseenter"].forEach(e=>{y.addEventListener(e,r,{passive:!0})})}const p=document.getElementById("welcomeName"),w=document.getElementById("welcomePhone");p&&(p.addEventListener("focus",r,{passive:!0}),p.addEventListener("input",r,{passive:!0})),w&&(w.addEventListener("focus",r,{passive:!0}),w.addEventListener("input",r,{passive:!0}))}function r(){a&&(clearTimeout(a),a=null);const e=document.getElementById("welcomeProgressBar");e&&(e.classList.add("paused"),e.style.display="none")}window.closeWelcomeModal=function(){const e=document.getElementById("welcomeModal");e&&(e.classList.remove("active"),e.setAttribute("aria-hidden","true"),clearTimeout(a),a=null)},window.welcomeExploreMenu=function(){closeWelcomeModal();const e=document.getElementById("menu");e&&e.scrollIntoView({behavior:"smooth"})},window.handleWelcomeSubmit=async function(e){e.preventDefault();const t=document.getElementById("welcomeName"),n=document.getElementById("welcomePhone"),o=document.getElementById("welcomeSubmitBtn"),a=(t?.value||"").trim(),i=(n?.value||"").trim();if(!/^(03|05|07|08|09)[0-9]{8}$/.test(i))return window.showOlionToast&&window.showOlionToast("Vui lòng nhập đúng số điện thoại (10 số)!","alert-circle"),void n?.focus();o&&(o.disabled=!0,o.textContent="Đang lưu...");try{localStorage.setItem("olion_customer_name",a),localStorage.setItem("olion_customer_phone",i)}catch(e){}try{const e=window.supabaseClient||("function"==typeof initSupabase?initSupabase():null);e&&await e.from("customers").upsert([{name:a,contact:i,source:"Smart Welcome Popup",notes:`Đăng ký qua Smart Welcome Popup lúc ${(new Date).toLocaleString("vi-VN")}`}],{onConflict:"contact"})}catch(e){console.warn("Supabase customer insert error:",e)}const notifCb=document.getElementById("welcomeNotifCheckbox");if(!notifCb||notifCb.checked){"function"==typeof window.triggerPushNotificationOptIn&&window.triggerPushNotificationOptIn("welcome_popup");}o&&(o.disabled=!1,o.textContent="Bắt đầu trải nghiệm"),closeWelcomeModal(),window.showOlionToast&&window.showOlionToast(`Chào mừng ${a} đến với OLION COFFEE!`,"coffee"),"function"==typeof window.updateDynamicGreeting&&window.updateDynamicGreeting()},document.getElementById("welcomeModal")?.addEventListener("click",e=>{e.target===document.getElementById("welcomeModal")&&closeWelcomeModal()});const d=()=>{"requestIdleCallback"in window?requestIdleCallback(()=>setTimeout(l,1200),{timeout:3e3}):setTimeout(l,2e3)};"complete"===document.readyState?d():window.addEventListener("load",d,{passive:!0});const u=document.getElementById("loyaltyLookupModal"),m=document.getElementById("loyaltySearchPhone"),h=document.getElementById("loyaltyResultCard"),g=document.getElementById("loyaltyErrorCard"),y=document.getElementById("loyaltySearchBtn");/* unified loyalty handled below */;const p=document.getElementById("scrollProgress"),w=document.getElementById("siteHeader"),f=document.getElementById("backToTopBtn"),b=document.getElementById("backToTopProgress"),v=2*Math.PI*20;let _=!1;window.addEventListener("scroll",()=>{_||(window.requestAnimationFrame(()=>{const e=window.scrollY||document.documentElement.scrollTop,t=document.documentElement.scrollHeight-window.innerHeight,n=t>0?e/t*100:0;if(p&&(p.style.width=n+"%"),w&&w.classList.toggle("scrolled",e>60),f&&(f.classList.toggle("is-visible",e>320),b&&t>0)){const e=v-n/100*v;b.style.strokeDashoffset=Math.max(0,e)}_=!1}),_=!0)},{passive:!0}),f&&f.addEventListener("click",e=>{e.preventDefault(),window.scrollTo({top:0,behavior:"smooth"})});const E=document.getElementById("burgerBtn"),I=document.getElementById("mobileDrawer"),C=document.getElementById("drawerOverlay"),T=document.getElementById("drawerClose");window.toggleDrawer=function(e=null){if(!I||!C)return;const t=null!==e?e:!I.classList.contains("active");I.classList.toggle("active",t),C.classList.toggle("active",t),document.body.style.overflow=t?"hidden":""},E&&E.addEventListener("click",()=>toggleDrawer(!0)),T&&T.addEventListener("click",()=>toggleDrawer(!1)),C&&C.addEventListener("click",()=>toggleDrawer(!1)),document.querySelectorAll(".drawer-link").forEach(e=>{e.addEventListener("click",()=>toggleDrawer(!1))});const k=document.querySelectorAll(".hero-slide"),B=document.querySelectorAll(".hero-dot");let L=0,S=null;function M(e){k.forEach((t,n)=>t.classList.toggle("active",n===e)),B.forEach((t,n)=>t.classList.toggle("active",n===e)),L=e}function x(){M((L+1)%k.length)}B.forEach((e,t)=>{e.addEventListener("click",()=>{clearInterval(S),M(t),S=setInterval(x,5e3)})}),k.length>1&&(S=setInterval(x,5e3));const O=document.querySelectorAll(".menu-tab-btn[data-cat]"),A=document.querySelectorAll(".menu-category-panel"),N=document.getElementById("openMenuBoardBtn"),q=document.getElementById("menuBoardModal"),$=document.getElementById("menuBoardCloseBtn"),H=document.getElementById("menuBoardViewport"),F=document.getElementById("menuBoardImg"),P=document.getElementById("menuBoardZoomBtn"),G=document.getElementById("menuBoardZoomText");O.forEach(e=>{e.addEventListener("click",()=>{const t=e.getAttribute("data-cat");t&&(O.forEach(e=>e.classList.remove("active")),e.classList.add("active"),A.forEach(e=>{e.classList.toggle("active",e.id===`cat-${t}`)}))})}),window.openMenuBoard=function(){q&&(q.classList.add("active"),q.setAttribute("aria-hidden","false"),document.body.style.overflow="hidden")},window.closeMenuBoard=function(){q&&(q.classList.remove("active"),q.setAttribute("aria-hidden","true"),H&&H.classList.remove("zoomed"),G&&(G.textContent="Phóng to"),document.body.style.overflow="")},window.toggleMenuBoardZoom=function(){if(!H)return;const e=H.classList.toggle("zoomed");G&&(G.textContent=e?"Thu nhỏ":"Phóng to")},N&&N.addEventListener("click",openMenuBoard),$&&$.addEventListener("click",closeMenuBoard),P&&P.addEventListener("click",toggleMenuBoardZoom),F&&F.addEventListener("click",e=>{e.stopPropagation(),toggleMenuBoardZoom()}),H&&H.addEventListener("click",e=>{e.target===H&&closeMenuBoard()}),document.addEventListener("keydown",e=>{"Escape"===e.key&&q&&q.classList.contains("active")&&closeMenuBoard()}),document.querySelectorAll(".faq-trigger").forEach(e=>{e.addEventListener("click",()=>{const t=e.closest(".faq-item"),n=t.classList.contains("active");document.querySelectorAll(".faq-item").forEach(e=>{e.classList.remove("active"),e.querySelector(".faq-trigger")?.setAttribute("aria-expanded","false")}),n||(t.classList.add("active"),e.setAttribute("aria-expanded","true"))})});let D=null;window.showOlionToast=function(e,t="✨"){const n=document.getElementById("olionToast"),o=document.getElementById("olionToastMsg"),a=document.getElementById("olionToastIcon");n&&o?(o.textContent=e,a&&(a.textContent=t),n.classList.add("show"),D&&clearTimeout(D),D=setTimeout(()=>{n.classList.remove("show")},4e3)):alert(e)};let R="space";window.lastFormattedBookingMsg="",window.openBookingModal=function(e="space",t=""){const n=document.getElementById("bookingModal");if(!n)return;const o=document.getElementById("bkFormArea"),a=document.getElementById("bkSuccessArea");o&&(o.style.display="block"),a&&(a.style.display="none");const i=document.getElementById("bkName"),c=document.getElementById("bkPhone");const _rec=document.getElementById("recentBookingNotice");if(_rec){try{const _bks=JSON.parse(localStorage.getItem("olion_bookings")||"[]");if(_bks.length>0){const _b=_bks[0];_rec.innerHTML=`💡 <strong>Đơn đặt gần nhất:</strong> Ngày ${_b.booking_date||_b.date} (${_b.booking_time||_b.time}) cho ${_b.guests_count||_b.guests||1} khách. Trạng thái: <span style="color:#2ecc71;font-weight:700;">Đã tiếp nhận</span>.`;_rec.style.display="block"}else{_rec.style.display="none"}}catch(e){_rec.style.display="none"}}i&&!i.value&&(i.value=localStorage.getItem("olion_customer_name")||""),c&&!c.value&&(c.value=localStorage.getItem("olion_customer_phone")||"");const s=document.getElementById("bkTime"),l=document.getElementById("bkCustomTimeWrap"),r=document.getElementById("bkCustomTime");if(l&&(l.style.display="none"),r&&(r.value=""),s&&(s.value="10:00 - 12:00"),window.selectBookingType(e),t){const e=document.getElementById("bkNote");e&&(e.value=t)}const d=document.getElementById("bkDate");if(d){const t=new Date,n="space"===e?3:1,o=new Date(t.getFullYear(),t.getMonth(),t.getDate()+n),a=o.getFullYear(),i=String(o.getMonth()+1).padStart(2,"0"),c=String(o.getDate()).padStart(2,"0");d.min=`${a}-${i}-${c}`,(!d.value||d.value<d.min)&&(d.value=`${a}-${i}-${c}`)}n.classList.add("active"),n.setAttribute("aria-hidden","false"),document.body.style.overflow="hidden",window.lucide&&window.lucide.createIcons()},window.handleTimeSelectChange=function(e){const t="modal"===e,n=document.getElementById(t?"bkTime":"pTime"),o=document.getElementById(t?"bkCustomTimeWrap":"pCustomTimeWrap"),a=document.getElementById(t?"bkCustomTime":"pCustomTime");n&&o&&("custom"===n.value?(o.style.display="block",a&&a.focus()):o.style.display="none")},window.closeBookingModal=function(){const e=document.getElementById("bookingModal");e&&(e.classList.remove("active"),e.setAttribute("aria-hidden","true"),document.body.style.overflow="")},window.backToBookingForm=function(){const e=document.getElementById("bkFormArea"),t=document.getElementById("bkSuccessArea");e&&(e.style.display="block"),t&&(t.style.display="none"),window.lucide&&window.lucide.createIcons()},window.selectBookingType=function(e){R=e;const t=document.getElementById("bkTypeSpace"),n=document.getElementById("bkTypeTable"),o=document.getElementById("bkNoticeText"),a=document.getElementById("bkGuests"),i=document.getElementById("bkNote"),c=document.getElementById("bkTime");c&&!c.value&&(c.value="10:00 - 12:00"),"space"===e?(t&&t.classList.add("active"),n&&n.classList.remove("active"),o&&(o.innerHTML="Liên hệ trước ít nhất <strong>1 tuần</strong> để Olion sắp xếp không gian chu đáo và phù hợp nhất."),a&&(a.value="10"),i&&(i.value="Mình muốn đăng ký thuê không gian tổ chức Workshop / Họp nhóm. Nhờ Olion tư vấn gói dịch vụ, sắp xếp bàn ghế và hỗ trợ kết nối máy chiếu / âm thanh.")):(t&&t.classList.remove("active"),n&&n.classList.add("active"),o&&(o.innerHTML="Vui lòng đặt bàn trước ít nhất <strong>1 ngày</strong>. <em>(Lưu ý: Chỉ xác nhận khi quán phản hồi)</em>."),a&&(a.value="4"),i&&(i.value="Mình muốn đặt bàn trước cho nhóm học tập / gặp gỡ bạn bè. Nhờ quán ưu tiên giữ giúp mình góc ngồi yên tĩnh, gần ổ cắm điện nhé."))},window.copyCurrentBookingMsg=function(){const e=window.lastFormattedBookingMsg;if(e){try{if(navigator.clipboard&&navigator.clipboard.writeText)navigator.clipboard.writeText(e);else{const t=document.createElement("textarea");t.value=e,document.body.appendChild(t),t.select(),document.execCommand("copy"),document.body.removeChild(t)}}catch(e){}alert("📋 Đã sao chép lại toàn bộ nội dung yêu cầu! Bạn có thể dán (Paste) vào khung chat bất cứ lúc nào.")}},window.quickConsultMessenger=function(e="all"){let t="Chào Olion Coffee! Mình muốn được tư vấn thông tin về dịch vụ Cho thuê không gian & Đặt bàn trước tại quán.";"space"===e?t="Chào Olion Coffee! Mình muốn tư vấn dịch vụ Cho thuê không gian để tổ chức Workshop / Họp nhóm / CLB tại quán.":"table"===e&&(t="Chào Olion Coffee! Mình muốn tư vấn đặt bàn trước cho nhóm học tập / gặp gỡ bạn bè tại quán.");try{if(navigator.clipboard&&navigator.clipboard.writeText)navigator.clipboard.writeText(t);else{const e=document.createElement("textarea");e.value=t,document.body.appendChild(e),e.select(),document.execCommand("copy"),document.body.removeChild(e)}}catch(e){}alert(`📋 Đã tự động sao chép nội dung:\n"${t}"\n\nKhi Messenger mở ra, bạn chỉ cần bấm DÁN (Paste) để gửi ngay cho Olion nhé!`),window.open("https://m.me/61594159312837","_blank")},window.handleBookingSubmit=async function(e){e&&e.preventDefault();const t=document.getElementById("bkSubmitBtn"),n=t?t.textContent:"";t&&(t.disabled=!0,t.textContent="Đang lưu yêu cầu...");const o=(document.getElementById("bkName")?.value||"").trim(),a=(document.getElementById("bkPhone")?.value||"").trim(),i=(document.getElementById("bkGuests")?.value||"").trim(),c=document.getElementById("bkDate")?.value||"";let s=document.getElementById("bkTime")?.value||"";const l=(document.getElementById("bkNote")?.value||"").trim();if("custom"===s){const e=(document.getElementById("bkCustomTime")?.value||"").trim();if(!e)return alert("Vui lòng nhập khung giờ riêng bạn mong muốn (Ví dụ: 09:30 - 11:30)."),t&&(t.disabled=!1,t.textContent=n),void document.getElementById("bkCustomTime")?.focus();s=e}if(!(o&&a&&c&&s))return alert("Vui lòng điền đầy đủ các thông tin bắt buộc (*)"),void(t&&(t.disabled=!1,t.textContent=n));const r=`Chào Olion Coffee! Mình muốn đăng ký:\n• Dịch vụ: ${"space"===R?"01 - CHO THUÊ KHÔNG GIAN (Workshop / Họp nhóm / CLB / Sự kiện)":"02 - ĐẶT BÀN TRƯỚC (Học tập / Hẹn bạn bè / Làm việc)"}\n• Khách hàng: ${o} (${a})\n• Số lượng người: ${i||"1"} người\n• Thời gian dự kiến: ${s} ngày ${c}\n`+(l?`• Yêu cầu chi tiết: ${l}\n`:"")+"Olion tư vấn và xác nhận giúp mình nhé! Cảm ơn quán.";window.lastFormattedBookingMsg=r;try{if(navigator.clipboard&&navigator.clipboard.writeText)navigator.clipboard.writeText(r);else{const e=document.createElement("textarea");e.value=r,document.body.appendChild(e),e.select(),document.execCommand("copy"),document.body.removeChild(e)}}catch(e){}try{const e={customer_name:o,phone:a,booking_type:R,guests_count:parseInt(i,10)||1,booking_date:c,booking_time:s,notes:l,status:"pending",created_at:(new Date).toISOString()};if("function"==typeof saveBookingToStorage)await saveBookingToStorage(e);else if(window.saveBookingToStorage)await window.saveBookingToStorage(e);else{const t=JSON.parse(localStorage.getItem("olion_bookings")||"[]");e.id="bk_"+Date.now(),t.unshift(e),localStorage.setItem("olion_bookings",JSON.stringify(t))}}catch(e){console.warn("Booking save error:",e)}finally{t&&(t.disabled=!1,t.textContent=n)}try{localStorage.setItem("olion_customer_name",o),localStorage.setItem("olion_customer_phone",a)}catch(e){}const d=document.getElementById("bkFormArea"),u=document.getElementById("bkSuccessArea"),m=document.getElementById("bkPreviewBox");m&&(m.textContent=r),d&&(d.style.display="none"),u&&(u.style.display="block"),window.lucide&&window.lucide.createIcons(),window.open("https://m.me/61594159312837","_blank")};const V=document.getElementById("feedbackModal");let z=5;window.openFeedbackModal=function(){"function"==typeof window.loadReCaptcha&&window.loadReCaptcha(),V&&(V.classList.add("active"),V.setAttribute("aria-hidden","false"),document.body.style.overflow="hidden")},window.closeFeedbackModal=function(){V&&(V.classList.remove("active"),V.setAttribute("aria-hidden","true"),document.body.style.overflow="",setTimeout(()=>{const e=document.getElementById("feedbackFormArea"),t=document.getElementById("feedbackSuccessArea");e&&(e.style.display="block"),t&&(t.style.display="none");const n=document.getElementById("feedbackForm");n&&n.reset()},300))};const Q=document.querySelectorAll(".star-btn");Q.forEach(e=>{e.addEventListener("click",()=>{z=parseInt(e.getAttribute("data-star"),10),Q.forEach((e,t)=>{e.classList.toggle("active",t<z)})})});const W=document.getElementById("btnSubmitFeedback");W&&W.addEventListener("click",async()=>{if((document.getElementById("fb_website_hp")?.value||"").trim())return console.warn("🤖 [Security] Bot phát hiện qua Honeypot Trap!"),document.getElementById("feedbackFormArea").style.display="none",void(document.getElementById("feedbackSuccessArea").style.display="block");const e=document.getElementById("fbName"),t=(e?e.value:"").trim()||"Khách ghé quán";if(t&&"Khách ghé quán"!==t)try{localStorage.setItem("olion_customer_name",t),"function"==typeof window.updateDynamicGreeting&&window.updateDynamicGreeting()}catch(e){}const n=document.getElementById("fbContact"),o=(n?n.value:"").trim(),a=document.getElementById("fbMessage"),i=(a?a.value:"").trim(),c=document.getElementById("fbImageDataUrl"),s=c?c.value:"";if(!i&&!s)return showOlionToast("Vui lòng chia sẻ đôi lời cảm nhận hoặc hình ảnh của bạn nhé!","✍️"),void(a&&a.focus());if("function"==typeof canUserSubmitFeedback){const e=await canUserSubmitFeedback(o);if(!e.can_submit)return void showOlionToast(e.message,"clock")}W.disabled=!0,W.innerHTML='<i data-lucide="loader-2" class="icon-spinner" style="width:16px;height:16px;margin-right:6px;"></i> Đang gửi...',lucide.createIcons(),"function"==typeof executeReCaptcha&&await executeReCaptcha("submit_feedback"),"function"==typeof submitFeedbackToCloud&&await submitFeedbackToCloud({name:t,contact:o,rating:z,content:i,imageDataUrl:s}),W.disabled=!1,W.textContent="Gửi đánh giá ngay","function"==typeof removeFeedbackImage&&removeFeedbackImage();const l=document.getElementById("feedbackFormArea");l&&(l.style.display="none");const r=document.getElementById("feedbackSuccessArea");r&&(r.style.display="block"),showOlionToast("Cảm ơn bạn đã gửi đánh giá quý báu cho Olion Coffee!","check-circle")}),V&&V.addEventListener("click",e=>{e.target===V&&closeFeedbackModal()});const U=document.getElementById("wheelModal"),K=document.getElementById("wheelCanvas"),Y=document.getElementById("spinBtn");window.openWheelModal=function(){U&&(U.classList.add("active"),document.body.style.overflow="hidden",Z(0))},window.closeWheelModal=function(){U&&(U.classList.remove("active"),document.body.style.overflow="")};let J=[{text:"Giảm 10% Tổng Bill",code:"OLION10",color:"#E59A55"},{text:"Tặng 1 Topping Free",code:"FREETOP",color:"var(--bg-card)"},{text:"Giảm 15% Cà Phê Muối",code:"MUOI15",color:"#D86326"},{text:"Voucher 20.000đ",code:"GIFT20K",color:"#1D5A38"},{text:"Tặng 1 Ly Bạc Xỉu",code:"FREEBACXIU",color:"#E59A55"},{text:"Chúc Bạn May Mắn",code:"THANKYOU",color:"var(--bg-card)"}];function j(){try{const e=localStorage.getItem("olion_minigame"),t=document.getElementById("wheelFloatBtn");if(!t)return;if(e){const n=JSON.parse(e);if(!1===n.enabled)return console.log("SETTING NONE"),t.style.setProperty("display","none","important"),void("function"==typeof closeWheelModal&&closeWheelModal());if(t.style.removeProperty("display"),t.style.display="flex",n.floatLabel){const e=t.querySelector('[data-i18n="wheel_float"]')||t.querySelector("span:last-child");e&&(e.textContent=n.floatLabel)}if(n.title){const e=document.getElementById("wheelTitle");e&&(e.textContent=n.title)}n.prizes&&Array.isArray(n.prizes)&&n.prizes.length>=2&&(J=n.prizes.map(e=>({text:e.text||"Quà tặng",code:e.code||"OLIONGIFT",color:e.color||"#E59A55",desc:e.desc||e.text+" từ Olion Coffee!"})),Z(0))}else t.style.removeProperty("display"),t.style.display="flex"}catch(e){console.warn("Lỗi applyMinigameConfig:",e)}}let X=!1;function Z(e){if(!K)return;const t=K.getContext("2d"),n=J.length,o=2*Math.PI/n,a=140,i=140;t.clearRect(0,0,280,280);for(let c=0;c<n;c++){const n=e+c*o;t.beginPath(),t.fillStyle=J[c].color,t.moveTo(a,i),t.arc(a,i,135,n,n+o),t.lineTo(a,i),t.fill(),t.strokeStyle="rgba(229,154,85,0.4)",t.lineWidth=2,t.stroke(),t.save(),t.translate(a,i),t.rotate(n+o/2),t.textAlign="right",t.fillStyle="#FFFFFF",t.font="bold 11px Plus Jakarta Sans, sans-serif",t.fillText(J[c].text,120,4),t.restore()}t.beginPath(),t.arc(a,i,20,0,2*Math.PI),t.fillStyle="#E59A55",t.fill(),t.strokeStyle="#FFFFFF",t.lineWidth=3,t.stroke()}Y&&Y.addEventListener("click",async()=>{if(X)return;const e=document.getElementById("wheelName"),t=document.getElementById("wheelPhone"),n=(e?e.value:"").trim(),o=(t?t.value:"").trim();if(!o)return showOlionToast("Vui lòng nhập số điện thoại để nhận quà nhé!","phone"),void(t&&t.focus());if(o.replace(/[^0-9]/g,"").length<9)return showOlionToast("Số điện thoại không hợp lệ (tối thiểu 9-10 chữ số)!","alert-circle"),void(t&&t.focus());if("function"==typeof canUserSpinToday){Y.disabled=!0,Y.innerHTML='<i data-lucide="loader-2" class="icon-spinner" style="width:16px;height:16px;margin-right:6px;"></i> Đang tải...',lucide.createIcons();const e=await canUserSpinToday(o);if(!e.can_spin)return Y.disabled=!1,Y.textContent="QUAY NGAY",void showOlionToast(e.message,"clock")}X=!0,Y.disabled=!0,Y.textContent="ĐANG QUAY...";const a=Math.floor(Math.random()*(J.length-1)),i=2*Math.PI/J.length,c=1.5*Math.PI-(a*i+i/2),s=2*(6+Math.floor(3*Math.random()))*Math.PI+c,l=performance.now();requestAnimationFrame(async function e(t){const i=t-l,c=Math.min(i/4e3,1),r=1-Math.pow(1-c,3);if(Z(s*r),c<1)requestAnimationFrame(e);else{X=!1,Y.disabled=!1,Y.textContent="QUAY NGAY";const e=J[a];if(document.getElementById("wheelPrizeTitle").textContent=`Chúc Mừng ${n||"Bạn"}!`,document.getElementById("wheelPrizeDesc").textContent=`Bạn đã trúng thưởng: ${e.text}`,document.getElementById("wheelCode").textContent=e.code,document.getElementById("wheelFormArea").style.display="none",document.getElementById("wheelResultArea").style.display="block","function"==typeof recordLuckySpinToCloud){const t=await recordLuckySpinToCloud({customer_name:n||"Khách quay minigame",customer_phone:o,prize_name:e.text,promo_code:e.code}),a=document.getElementById("qrCodeContainer");a.innerHTML="",t&&t.id&&new QRCode(a,{text:"olion-voucher:"+t.id,width:150,height:150,colorDark:"#190D07",colorLight:"#ffffff",correctLevel:QRCode.CorrectLevel.H})}showOlionToast(`Chúc mừng bạn nhận được ưu đãi ${e.code}!`,"coffee")}})});const ee=document.getElementById("footerBrandLogo"),te=document.getElementById("longPressProgress");let ne=null,oe=null,ae=0,ie=0,ce=null;function se(){clearTimeout(ne),clearInterval(oe),te&&(te.style.width="0%")}ee&&(ee.addEventListener("touchstart",function(){ae=0,te&&(te.style.width="0%"),oe=setInterval(()=>{ae+=5,te&&(te.style.width=ae+"%")},100),ne=setTimeout(()=>{clearInterval(oe),navigator.vibrate&&navigator.vibrate(100),window.location.href="admin"},2e3)},{passive:!0}),ee.addEventListener("touchend",se),ee.addEventListener("touchcancel",se),ee.addEventListener("click",()=>{ie++,clearTimeout(ce),ie>=3?(ie=0,window.location.href="admin"):ce=setTimeout(()=>{ie=0},1200)})),document.addEventListener("keydown",e=>{!e.ctrlKey&&!e.metaKey||!e.shiftKey||"a"!==e.key&&"A"!==e.key||(e.preventDefault(),window.location.href="admin")});let le={};window.loadFeaturedNews=async function(){try{const e=window.supabaseClient||window._supabase||("undefined"!=typeof supabaseClient?supabaseClient:null)||(window.supabase?window.supabase.createClient("https://xwbrbesgnwcngzohprxt.supabase.co","sb_publishable_vWuV07_xPU0wNftK0lpnFQ_oA9XHPLS"):null);let t=null;if(e){const n=await e.from("news_items").select("*").order("created_at",{ascending:!1});if(!n.error&&n.data&&n.data.length>0){t=n.data;try{localStorage.setItem("olion_cached_news",JSON.stringify(t))}catch(e){}}}if(!t||0===t.length)try{t=JSON.parse(localStorage.getItem("olion_cached_news")||"[]")}catch(e){}t&&0!==t.length||(t=[{id:"e6cff902-fbd7-4668-b3eb-0d30708fe79e",title:"CARAMEL LATTE — Sự Hòa Quyện Ngọt Ngào & Đậm Đà Cuốn Hút",date:"21/10/2026",category:"Thực Đơn Signature",cover_image:"assets/news/caramel-latte.webp",description:"Một chút caramel ngọt ngào, một chút espresso đậm đà, hòa quyện cùng sữa béo mịn — tạo nên Caramel Latte đầy cuốn hút tại Olion Coffee.",content_html:"<p>Một chút caramel ngọt ngào, một chút espresso đậm đà, hòa quyện cùng sữa béo mịn — tạo nên <strong>Caramel Latte</strong> đầy cuốn hút. ☕🤎</p><p>Sự kết hợp mượt mà giữa espresso đậm đà, sữa béo ngậy và caramel ngọt ngào sẽ mang đến cho bạn trải nghiệm vị giác vô cùng trọn vẹn.</p><p>Ghé <strong>Olion Coffee</strong>, thưởng thức một ly ngọt ngào và tận hưởng chút bình yên giữa ngày nhé! ❤️</p>",is_featured:!1},{id:"70d3d568-c478-40ef-a066-7e0cfc6f1982",title:"CÓ THÊM ĐIỀU MỚI: CHO THUÊ KHÔNG GIAN & ĐẶT BÀN TRƯỚC",date:"21/10/2026",category:"Không Gian & Dịch Vụ",cover_image:"assets/banner-booking.webp",description:"Tại Olion Coffee, chúng mình hiểu rằng mỗi khoảnh khắc học tập, hội họp hay gặp gỡ bạn bè đều cần một không gian đủ ấm cúng, đủ yên tĩnh và trọn vẹn sự tinh tế.",content_html:"<p>Tại Olion Coffee, chúng mình hiểu rằng mỗi khoảnh khắc học tập, hội họp hay gặp gỡ bạn bè đều cần một không gian đủ ấm cúng, đủ yên tĩnh và trọn vẹn sự tinh tế.</p>",is_featured:!0},{id:"8b0a9a12-5d25-44be-ad3e-780161daa6c6",title:"OLION’S FIRST WEEK — NHẬT KÝ TUẦN ĐẦU TIÊN",date:"19/09/2026",category:"Sự kiện đặc biệt",cover_image:"assets/news/news-1-flowers.webp",description:"Tuần đầu tiên mở cửa đã khép lại với biết bao cung bậc cảm xúc! Olion Coffee vô cùng trân trọng...",content_html:"<p>Tuần đầu tiên mở cửa đã khép lại với biết bao cung bậc cảm xúc! Olion Coffee vô cùng trân trọng...</p>",is_featured:!1}]);const n=t.find(e=>e.is_featured)||t[0],o=t.filter(e=>e.id!==n.id).slice(0,4);t.forEach(e=>{le[e.id]={title:e.title,date:e.date,category:e.category,images:[e.cover_image],desc:e.description,contentHtml:e.content_html}});let a="";o.forEach(e=>{a+=`\n              <article class="news-sub-card" onclick="openNewsModal('${e.id}')">\n                <div class="news-sub-img-wrap">\n                  <img src="${e.cover_image}" alt="${e.title}" class="news-sub-img" loading="lazy" />\n                </div>\n                <div class="news-sub-content">\n                  <div class="news-meta">\n                    <span class="news-date">${e.date}</span>\n                    <span class="news-category" style="color:var(--accent-gold);">${e.category}</span>\n                  </div>\n                  <h4 class="news-sub-title" style="margin-bottom:8px; line-height: 1.4;">${e.title}</h4>\n                  <p class="news-sub-desc">${e.description?e.description.substring(0,80)+"...":""}</p>\n                  <span class="news-sub-link">Xem chi tiết &rarr;</span>\n                </div>\n              </article>\n            `});const i=`\n            <div class="news-featured">\n              <article class="news-featured-card" onclick="openNewsModal('${n.id}')">\n                <div class="news-featured-img-wrap">\n                  <img src="${n.cover_image}" alt="${n.title}" class="news-featured-img" loading="lazy" />\n                  <div class="news-featured-badge"><i data-lucide="award" style="width:13px;height:13px;"></i> Nổi bật</div>\n                </div>\n                <div class="news-featured-content">\n                  <div class="news-meta">\n                    <span class="news-date"><i data-lucide="calendar" style="width:12px;height:12px;margin-right:4px;"></i>${n.date}</span>\n                    <span class="news-category">${n.category}</span>\n                  </div>\n                  <h3 class="news-featured-title">${n.title}</h3>\n                  <p class="news-featured-excerpt">${n.description||""}</p>\n                  <div class="news-featured-footer">\n                    <button class="btn-read-more">Xem bài viết <i data-lucide="arrow-right" style="width:16px;height:16px;"></i></button>\n                  </div>\n                </div>\n              </article>\n            </div>\n            <div class="news-sub">\n              <div class="news-sub-grid">\n                ${a}\n              </div>\n            </div>\n          `,c=document.getElementById("homepageNewsGrid");c&&(c.innerHTML=i),window.lucide&&"function"==typeof window.lucide.createIcons&&window.lucide.createIcons()}catch(e){}},setTimeout(()=>{window.loadFeaturedNews&&window.loadFeaturedNews();const e=new URLSearchParams(window.location.search).get("article");e&&setTimeout(()=>{window.openNewsModal&&window.openNewsModal(e)},600)},500),window.openNewsModal=function(e){currentNewsId=e;const t=le[e];newsModal&&t&&(newsModalTitle.textContent=t.title,newsModalDate.textContent=t.date,newsModalCategory.textContent=t.category,newsModalMainImg.src=t.images[0]||"assets/logo-white.webp",newsModalBody.innerHTML=t.contentHtml,newsModalThumbs&&(newsModalThumbs.innerHTML="",newsModalThumbs.style.display="none"),newsModalMainImg.style.opacity="1",newsModalMainImg.style.transform="scale(1)",newsModal.classList.add("active"),newsModal.setAttribute("aria-hidden","false"),document.body.style.overflow="hidden")},window.closeNewsModal=function(){newsModal&&(newsModal.classList.remove("active"),newsModal.setAttribute("aria-hidden","true"),document.body.style.overflow="")},newsModal&&newsModal.addEventListener("click",e=>{e.target===newsModal&&closeNewsModal()}),window.shareNewsArticle=function(){const e={title:newsModalTitle.textContent,text:"Xem tin tức mới nhất từ Olion Coffee!",url:window.location.href.split("#")[0]+"#news"};navigator.share?navigator.share(e).catch(()=>{}):(navigator.clipboard.writeText(e.url),alert("Đã sao chép liên kết bài viết vào bộ nhớ tạm!"))};const re=document.querySelectorAll(".section-header, .stat-card, .feature-pill, .signature-card, .menu-card, .space-card, .review-card, .faq-item, .contact-card, .hours-card, .news-card-main, .news-card-side, .service-feature-card, .news-featured-card, .news-sub-card");if("IntersectionObserver"in window){const e=new IntersectionObserver(t=>{t.forEach(t=>{t.isIntersecting&&(t.target.classList.add("visible"),e.unobserve(t.target))})},{threshold:.12,rootMargin:"0px 0px -40px 0px"});re.forEach((t,n)=>{t.classList.add("reveal");const o=n%4;o>0&&t.classList.add(`reveal-delay-${o}`),e.observe(t)})}else re.forEach(e=>e.classList.add("reveal","visible"));const de=document.querySelectorAll(".header-nav .nav-link"),ue=["#about","#signature","#menu","#spaces","#news","#faq","#contact"].map(e=>document.querySelector(e)).filter(Boolean);if("IntersectionObserver"in window&&ue.length){const e=new IntersectionObserver(e=>{e.forEach(e=>{if(e.isIntersecting){const t="#"+e.target.id;de.forEach(e=>{e.classList.toggle("active",e.getAttribute("href")===t)})}})},{rootMargin:"-30% 0px -60% 0px"});ue.forEach(t=>e.observe(t))}function me(e){return e?String(e).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;"):""}function he(){try{const e=document.getElementById("announcementBanner");if(!e)return;if("true"===sessionStorage.getItem("olion_announcement_dismissed"))return void(e.style.display="none");const t=localStorage.getItem("olion_announcement");if(t){const n=JSON.parse(t);if(n.enabled&&n.text){const t=document.getElementById("announcementBadge"),o=document.getElementById("announcementText"),a=document.getElementById("announcementLink");return t&&(t.textContent=n.badge||"ƯU ĐÃI"),o&&(o.textContent=n.text),a&&(a.href=n.link||"#menu",a.style.display=n.link?"inline":"none"),void(e.style.display="block")}}e.style.display="none"}catch(e){console.warn("Lỗi applyAnnouncementConfig:",e)}}function ge(){try{const e=localStorage.getItem("olion_store_settings");if(!e)return;const t=JSON.parse(e);if(t.hotline){const e=t.hotline.replace(/\s+/g,"");document.querySelectorAll('a[href^="tel:"]').forEach(n=>{n.href="tel:"+e;const o=n.querySelector("span:last-child");o&&!n.classList.contains("btn")&&(o.textContent=t.hotline)});const n=document.querySelector('.contact-item a[href^="tel:"]');n&&(n.textContent=t.hotline)}if(t.address){const e=document.querySelectorAll(".contact-item-text");e.length>0&&(e[0].textContent=t.address)}if(t.hours){const e=document.querySelector(".hours-badge");e&&(e.textContent=t.hours)}t.accentColor&&document.documentElement.style.setProperty("--accent-gold",t.accentColor)}catch(e){console.warn("Lỗi applyStoreSettings:",e)}}window.dismissAnnouncement=function(){const e=document.getElementById("announcementBanner");e&&(e.style.display="none"),sessionStorage.setItem("olion_announcement_dismissed","true")};const ye={"Cà phê":"cat-coffee","Trà trái cây":"cat-tea","Trà sữa & Matcha":"cat-matcha",Matcha:"cat-matcha",Cacao:"cat-cacao","Nước ép":"cat-juice","Sữa chua":"cat-yagout",Topping:"cat-topping"};
function renderMenuPanels(itemsToRender){
  const e=itemsToRender||be||Ie();
  if(!e||!Array.isArray(e)||0===e.length)return;
  const t={};
  e.forEach(e=>{
    const n=e.category||"Cà phê",o=ye[n]||"cat-coffee";
    t[o]||(t[o]=[]),t[o].push(e);
  });
  const favs=JSON.parse(localStorage.getItem("olion_fav_drinks")||"[]");
  Object.keys(t).forEach(panelId=>{
    const panel=document.getElementById(panelId);
    if(!panel)return;
    const grid=panel.querySelector(".menu-grid");
    if(!grid)return;
    const catItems=t[panelId];
    let html="";
    catItems.forEach(item=>{
      const isSoldOut=!1===item.is_available;
      let badgeHtml="";
      if(isSoldOut){
        badgeHtml='<span class="menu-badge badge-sold-out">HẾT MÓN</span>';
      }else if(item.badge){
        const b=item.badge.toUpperCase();
        let bClass="badge-best";
        b.includes("HOT")||b.includes("CHẠY")?bClass="badge-hot":
        b.includes("NEW")||b.includes("MỚI")?bClass="badge-new":
        b.includes("SIGNATURE")&&(bClass="badge-signature");
        badgeHtml=`<span class="menu-badge ${bClass}">${me(item.badge)}</span>`;
      }
      const priceStr=(Number(item.price)||0).toLocaleString("vi-VN")+"đ";
      const isFav=favs.includes(item.name);
      html+=`
        <article class="menu-card ${isSoldOut?"is-sold-out":""}" id="menu-card-${item.id||""}">
          <div class="menu-card-img-wrap">
            ${badgeHtml}
            <button type="button" class="btn-fav-card ${isFav?"active":""}" aria-label="Lưu món yêu thích" onclick="toggleFavoriteDrink(this, event)"><svg viewBox="0 0 24 24" width="16" height="16" fill="${isFav?"#fff":"none"}" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg></button>
            <img src="${item.image_url||"assets/menu/espresso.webp"}" alt="${me(item.name)} — Olion Coffee" class="menu-card-img" width="300" height="300" loading="lazy" decoding="async" onerror="this.src='assets/menu/espresso.webp'" />
          </div>
          <div class="menu-card-body">
            <h3 class="menu-card-name">${me(item.name)}</h3>
            <div class="menu-card-price">${priceStr}</div>
            <p class="menu-card-desc">${me(item.description||"")}</p>
          </div>
        </article>
      `;
    });
    grid.innerHTML=html;
  });
}
async function pe(){
  try{
    if("function"!=typeof fetchMenuItemsFromCloud)return;
    const res=await fetchMenuItemsFromCloud();
    const e=res&&res.data;
    if(!e||!Array.isArray(e)||0===e.length)return;
    be=e;
    renderMenuPanels(e);
  }catch(e){console.warn("Lỗi syncMenuFromCloud:",e)}
}
async function we(){try{if("function"!=typeof fetchApprovedFeedbacksFromCloud)return;const e=(await fetchApprovedFeedbacksFromCloud()).data;if(!e||!Array.isArray(e)||0===e.length)return;const t=document.getElementById("reviewsGrid");if(!t)return;e.slice(0,4).reverse().forEach(e=>{const n="fb-card-"+e.id;if(document.getElementById(n))return;const o=document.createElement("article");o.id=n,o.className="review-card reveal visible";const a=Math.min(5,Math.max(1,e.rating||5)),i=`<span style='color:var(--accent-gold);letter-spacing:2px;'>${"★".repeat(a)}</span>`,c=["user","user-check","smile","award","heart"],s=c[Math.floor(Math.random()*c.length)];o.innerHTML=`\n              <div class="review-stars" aria-label="${e.rating||5} trên 5 sao">${i}</div>\n              <p class="review-quote">"${me(e.content)}"</p>\n              <div class="review-author">\n                <div class="review-avatar">${s}</div>\n                <div>\n                  <h3 class="review-name">${me(e.name||"Khách ghé quán")}</h3>\n                  <p class="review-role">Đánh giá xác thực tại quán</p>\n                </div>\n              </div>\n            `,t.prepend(o)})}catch(e){console.warn("Lỗi syncApprovedReviews:",e)}}function fe(){try{const e=function(){const e=(new Date).toLocaleString("en-US",{timeZone:"Asia/Ho_Chi_Minh"}),t=new Date(e),n=60*t.getHours()+t.getMinutes(),o=1200;if(n>=480&&n<1170)return{status:"open",badgeText:"ĐANG MỞ CỬA",subText:"Đang mở cửa • 08:00 - 20:00",hoursSub:"Thời gian thực (GMT+7) • Mở đến 20:00",atmosphere:"Quán đang phục vụ. Không gian máy lạnh mát rượi, âm nhạc êm dịu, sẵn sàng đón bạn đến làm việc & thưởng thức cà phê!"};if(n>=1170&&n<o){const e=o-n;return{status:"closing",badgeText:"SẮP ĐÓNG CỬA",subText:`Sắp đóng cửa • Còn ${e} phút`,hoursSub:`Thời gian thực (GMT+7) • Đóng cửa sau ${e} phút`,atmosphere:"Quán nhận order mang đi & chốt bàn cuối trong ngày đến 20:00. Bạn vẫn có thể đặt bàn trước cho ngày mai!"}}return{status:"closed",badgeText:"TẠM NGHỈ",subText:"Tạm nghỉ • Mở lại 08:00 sáng mai",hoursSub:"Thời gian thực (GMT+7) • Mở lại lúc 08:00",atmosphere:"Olion đang nghỉ ngơi để chuẩn bị nguyên liệu tươi ngon nhất. Bạn vẫn có thể Đặt Bàn Giữ Chỗ trước trực tuyến!"}}(),t=document.getElementById("headerStoreBadge"),n=document.getElementById("headerStatusText"),o=document.getElementById("headerPulseDot");t&&n&&(t.className="header-store-badge "+("closing"===e.status?"closing":"closed"===e.status?"closed":""),n.textContent=e.badgeText,o&&(o.className="status-pulse-dot "+("closing"===e.status?"closing":"closed"===e.status?"closed":"")));const a=document.getElementById("drawerStoreStatus"),i=document.getElementById("drawerStatusTitle"),c=document.getElementById("drawerPulseDot");a&&i&&(a.className="drawer-status-card "+("closing"===e.status?"closing":"closed"===e.status?"closed":""),i.textContent=e.subText,c&&(c.className="status-pulse-dot "+("closing"===e.status?"closing":"closed"===e.status?"closed":"")));const s=document.getElementById("hoursStatusBadge"),l=document.getElementById("hoursStatusText"),r=document.getElementById("hoursPulseDot"),d=document.getElementById("storeAtmosphereTime"),u=document.getElementById("storeAtmosphereDesc");s&&l&&(s.className="live-status-pill "+("open"===e.status?"is-open":"closing"===e.status?"is-closing":"is-closed"),l.textContent=e.badgeText,r&&(r.className="status-pulse-dot "+("closing"===e.status?"closing":"closed"===e.status?"closed":""))),d&&(d.textContent=e.hoursSub),u&&(u.textContent=e.atmosphere)}catch(e){console.warn("Lỗi updateOlionStoreStatus:",e)}}fe(),setInterval(fe,3e4);DEFAULT_MENU_ITEMS=[{id:1,name:"ESPRESSO",price:3e4,category:"Cà phê",image_url:"assets/menu/espresso.webp",badge:"",description:"Nóng / Đá. Cà phê nguyên chất đậm đà.",is_available:!0},{id:2,name:"ESPRESSO SỮA",price:35e3,category:"Cà phê",image_url:"assets/menu/espresso_sua.webp",badge:"BEST",description:"Nóng / Đá. Sự kết hợp hoàn hảo giữa espresso và sữa đặc.",is_available:!0},{id:3,name:"BẠC XỈU",price:35e3,category:"Cà phê",image_url:"assets/menu/bac_xiu.webp",badge:"HOT",description:"Nhiều sữa ít cà phê, béo ngậy ngọt ngào.",is_available:!0},{id:4,name:"LATTE HẠNH NHÂN",price:4e4,category:"Cà phê",image_url:"assets/menu/latte_hanh_nhan.webp",badge:"",description:"Nóng / Đá. Vị bùi béo của hạnh nhân hòa quyện espresso.",is_available:!0},{id:5,name:"CARAMEL LATTE",price:4e4,category:"Cà phê",image_url:"assets/menu/caramel_latte.webp",badge:"",description:"Latte ngọt ngào với lớp sốt caramel thơm lừng.",is_available:!0},{id:6,name:"AMERICANO",price:3e4,category:"Cà phê",image_url:"assets/menu/americano.webp",badge:"",description:"Nóng / Đá. Espresso pha loãng thanh tao.",is_available:!0},{id:7,name:"CÀ PHÊ MUỐI",price:4e4,category:"Cà phê",image_url:"assets/menu/ca_phe_muoi.webp",badge:"SIGNATURE",description:"Đậm đà cà phê kết hợp lớp kem muối mặn béo.",is_available:!0},{id:8,name:"CÀ PHÊ BẠC HÀ",price:4e4,category:"Cà phê",image_url:"assets/menu/ca_phe_bac_ha.webp",badge:"",description:"Sự the mát sảng khoái của bạc hà và cà phê.",is_available:!0},{id:9,name:"ESPRESSO OATSIDE",price:4e4,category:"Cà phê",image_url:"assets/menu/ca_phe_sua_oatside.webp",badge:"NEW",description:"Nóng / Đá. Sữa yến mạch Oatside kết hợp espresso.",is_available:!0},{id:10,name:"CACAO LATTE",price:35e3,category:"Cacao",image_url:"assets/menu/cacao_latte.webp",badge:"BEST",description:"Nóng / Đá. Cacao nguyên chất béo thơm.",is_available:!0},{id:11,name:"CACAO KEM MUỐI",price:4e4,category:"Cacao",image_url:"assets/menu/cacao_kem_muoi.webp",badge:"HOT",description:"Cacao đậm đà hòa quyện lớp kem muối béo ngậy.",is_available:!0},{id:12,name:"CACAO BẠC HÀ",price:4e4,category:"Cacao",image_url:"assets/menu/cacao_bac_ha.webp",badge:"",description:"Hương bạc hà the mát sảng khoái quyện cùng vị ngọt đắng cacao.",is_available:!0},{id:13,name:"TRÀ VẢI HOA HỒNG",price:4e4,category:"Trà trái cây",image_url:"assets/menu/tra_vai_hoa_hong.webp",badge:"BEST",description:"Vải ngọt mọng nước kết hợp hương hoa hồng thanh tao dịu nhẹ.",is_available:!0},{id:14,name:"TRÀ BƯỞI HỒNG CHANH VÀNG",price:4e4,category:"Trà trái cây",image_url:"assets/menu/tra_buoi_hong_chanh_vang.webp",badge:"",description:"Bưởi hồng mọng nước hòa cùng chanh vàng thơm mát.",is_available:!0},{id:15,name:"TRÀ CHANH DÂY NHIỆT ĐỚI",price:4e4,category:"Trà trái cây",image_url:"assets/menu/tra_chanh_day_nhiet_doi.webp",badge:"HOT",description:"Chua ngọt bùng nổ, tươi mát sảng khoái ngày hè.",is_available:!0},{id:16,name:"TRÀ XOÀI CHANH DÂY",price:4e4,category:"Trà trái cây",image_url:"assets/menu/tra_xoai_chanh_day.webp",badge:"",description:"Xoài chín ngọt thanh quyện cùng chanh dây đậm đà.",is_available:!0},{id:17,name:"LỤC TRÀ NHÃN",price:4e4,category:"Trà trái cây",image_url:"assets/menu/luc_tra_nhan.webp",badge:"",description:"Nhãn giòn ngọt ngào kết hợp nền lục trà lài thanh tao.",is_available:!0},{id:18,name:"LỤC TRÀ TRÂN CHÂU TRẮNG",price:35e3,category:"Trà trái cây",image_url:"assets/menu/luc_tra_tran_chau_trang.webp",badge:"",description:"Lục trà lài thanh mát cùng trân châu trắng giòn sần sật.",is_available:!0},{id:19,name:"NƯỚC ÉP CAM",price:3e4,category:"Nước ép",image_url:"assets/menu/nuoc_ep_cam.webp",badge:"BEST",description:"Cam sành tươi vắt nguyên chất, dồi dào Vitamin C.",is_available:!0},{id:20,name:"NƯỚC ÉP CHANH DÂY",price:3e4,category:"Nước ép",image_url:"assets/menu/nuoc_ep_chanh_day.webp",badge:"HOT",description:"Chanh dây tươi thơm nồng, chua ngọt giải nhiệt cực đã.",is_available:!0},{id:21,name:"MATCHA LATTE",price:4e4,category:"Trà sữa & Matcha",image_url:"assets/menu/matcha_latte.webp",badge:"SIGNATURE",description:"Nóng / Đá. Matcha Nhật Bản nguyên chất thơm lừng.",is_available:!0},{id:22,name:"MATCHA CARAMEL",price:45e3,category:"Trà sữa & Matcha",image_url:"assets/menu/matcha_caramel.webp",badge:"",description:"Matcha thơm đậm hòa quyện cùng sốt caramel béo ngậy.",is_available:!0},{id:23,name:"MATCHA BẠC HÀ",price:45e3,category:"Trà sữa & Matcha",image_url:"assets/menu/matcha_bac_ha.webp",badge:"",description:"Sự kết hợp độc đáo giữa vị thanh của matcha và the mát của bạc hà.",is_available:!0},{id:24,name:"MATCHA KEM MUỐI",price:45e3,category:"Trà sữa & Matcha",image_url:"assets/menu/matcha_kem_muoi.webp",badge:"",description:"Lớp kem muối béo ngậy mằn mặn phủ trên nền matcha đậm đà.",is_available:!0},{id:25,name:"MATCHA QUẾ HOA",price:45e3,category:"Trà sữa & Matcha",image_url:"assets/menu/matcha_que_hoa.webp",badge:"",description:"Matcha cao cấp ướp hương hoa quế tự nhiên thanh tao.",is_available:!0},{id:26,name:"MATCHA COLD WHISK",price:45e3,category:"Trà sữa & Matcha",image_url:"assets/menu/matcha_cold_whisk.webp",badge:"",description:"Nóng / Đá. Đánh bọt matcha lạnh thủ công truyền thống.",is_available:!0},{id:27,name:"MATCHA DỪA",price:45e3,category:"Trà sữa & Matcha",image_url:"assets/menu/matcha_dua.webp",badge:"",description:"Vị thơm bùi của nước cốt dừa tươi quyện cùng bột matcha thượng hạng.",is_available:!0},{id:28,name:"MATCHA DÂU",price:45e3,category:"Trà sữa & Matcha",image_url:"assets/menu/matcha_dau.webp",badge:"HOT",description:"Sự hòa quyện tuyệt hảo giữa matcha thơm đắng và mứt dâu tây.",is_available:!0},{id:29,name:"MATCHA ESPRESSO LATTE",price:45e3,category:"Trà sữa & Matcha",image_url:"assets/menu/matcha_oatside.webp",badge:"",description:"Kết hợp hoàn hảo giữa Matcha và Espresso Latte.",is_available:!0},{id:30,name:"YAGOUT ĐÀO CHANH DÂY",price:45e3,category:"Sữa chua",image_url:"assets/menu/yagout_dao_chanh_day.webp",badge:"",description:"Đào mọng nước thơm ngọt hòa cùng vị chua dịu nhẹ của chanh dây.",is_available:!0},{id:31,name:"YAGOUT VIỆT QUẤT",price:45e3,category:"Sữa chua",image_url:"assets/menu/yagout_viet_quat.webp",badge:"HOT",description:"Việt quất bổ dưỡng thơm lừng quyện cùng sữa chua tươi mát.",is_available:!0},{id:32,name:"YAGOUT XOÀI CHANH DÂY",price:45e3,category:"Sữa chua",image_url:"assets/menu/yagout_xoai_chanh_day.webp",badge:"",description:"Xoài chín thơm ngọt hòa quyện cùng chanh dây nhiệt đới.",is_available:!0},{id:33,name:"YAGOUT DÂU",price:45e3,category:"Sữa chua",image_url:"assets/menu/yagout_dau.webp",badge:"BEST",description:"Sữa chua sánh mịn kết hợp mứt dâu tây chua ngọt thanh mát.",is_available:!0},{id:34,name:"TRÂN CHÂU TRẮNG",price:5e3,category:"Topping",image_url:"assets/menu/tran_chau_trang.webp",badge:"",description:"Trân châu trắng ngọc trai giòn dai thơm ngon.",is_available:!0},{id:35,name:"TRÂN CHÂU Ô LONG",price:5e3,category:"Topping",image_url:"assets/menu/tran_chau_o_long.webp",badge:"",description:"Đậm hương trà ô long rang mộc, mềm dẻo.",is_available:!0},{id:36,name:"THẠCH SƯƠNG SÁO",price:5e3,category:"Topping",image_url:"assets/menu/thach_suong_sao.webp",badge:"",description:"Thạch sương sáo mềm mượt, thanh mát giải nhiệt tự nhiên.",is_available:!0},{id:37,name:"THẠCH QUẾ HOA",price:5e3,category:"Topping",image_url:"assets/menu/thach_que_hoa.webp",badge:"",description:"Thơm thanh hương hoa quế tự nhiên.",is_available:!0},{id:38,name:"THẠCH VẢI HOA HỒNG",price:5e3,category:"Topping",image_url:"assets/menu/thach_vai_hoa_hong.webp",badge:"",description:"Thạch giòn dai thơm ngát hương hoa hồng và vị vải ngọt thanh.",is_available:!0},{id:39,name:"THẠCH CÀ PHÊ",price:5e3,category:"Topping",image_url:"assets/menu/thach_ca_phe.webp",badge:"",description:"Thạch cà phê nấu thủ công giòn thơm đậm vị.",is_available:!0}];
let be=DEFAULT_MENU_ITEMS,ve="all",_e="cat-coffee";window.DEFAULT_MENU_ITEMS=DEFAULT_MENU_ITEMS;window.renderMenuPanels=renderMenuPanels;try{renderMenuPanels(window.DEFAULT_MENU_ITEMS);}catch(e){console.warn(e);}function Ee(e){return e?e.toString().toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g,"").replace(/đ/g,"d").replace(/Đ/g,"d").trim():""}function Ie(){if(be.length>0)return be;try{const e=JSON.parse(localStorage.getItem("olion_menu_items")||"[]");if(Array.isArray(e)&&e.length>=30)return be=e,be}catch(e){}return"undefined"!=typeof DEFAULT_MENU_ITEMS&&Array.isArray(DEFAULT_MENU_ITEMS)?(be=DEFAULT_MENU_ITEMS,be):[]}function Ce(e="",t="all"){document.getElementById("menuSearchInput");const n=document.getElementById("menuSearchClear"),o=document.getElementById("cat-search"),a=document.getElementById("searchMenuGrid"),i=document.getElementById("menuEmptyState"),c=document.getElementById("searchResultCount"),s=document.getElementById("searchResultQuery"),l=document.getElementById("emptySearchTerm"),r=document.querySelectorAll(".menu-category-panel"),d=document.querySelectorAll(".menu-tab-btn[data-cat]"),u=e.trim(),m=Ee(u);if(n&&(n.style.display=u?"flex":"none"),!u&&"all"===t)return o&&o.classList.remove("active"),r.forEach(e=>{e.classList.toggle("active",e.id===_e)}),void d.forEach(e=>{e.classList.toggle("active",`cat-${e.getAttribute("data-cat")}`===_e)});const h=Array.from(r).find(e=>e.classList.contains("active")&&"cat-search"!==e.id);h&&(_e=h.id),r.forEach(e=>e.classList.remove("active")),o&&o.classList.add("active"),d.forEach(e=>e.classList.remove("active"));const g=Ie().filter(e=>{let n=!0;const o=e.category||"",a=((e.name||"")+" "+(e.description||"")).toLowerCase(),i=(e.badge||"").toUpperCase();if("signature"===t?n=Boolean(i&&(i.includes("BEST")||i.includes("HOT")||i.includes("SIGNATURE")||i.includes("NEW"))):"coffee"===t?n="Cà phê"===o||"Cacao"===o:"refreshing"===t?n="Trà trái cây"===o||"Nước ép"===o:"creamy"===t?n=/latte|muoi|muối|sua|sữa|yagout|bac xiu|bạc xỉu|caramel|cacao|dua|dừa|beo|béo/i.test(Ee(a)):"plantmilk"===t?n=/oatside|hanh nhan|hạnh nhân|yen mach|yến mạch|thuc vat|thực vật/i.test(Ee(a)):"decaf"===t?n=Boolean(o!=="Cà phê"&&o!=="Cacao"&&o!=="Trà sữa & Matcha"&&!/ca phe|coffee|espresso|americano|bac xiu|cold brew|cacao|chocolate|thach ca phe/i.test(Ee(e.name||""))&&["Trà trái cây","Nước ép","Sữa chua","Topping"].includes(o)):"favorites"===t&&(n=(JSON.parse(localStorage.getItem("olion_fav_drinks")||"[]")).includes(e.name)),!n)return!1;if(!m)return!0;const c=Ee(e.name||""),s=Ee(e.description||""),l=Ee(e.category||"");return c.includes(m)||s.includes(m)||l.includes(m)});if(c&&(c.textContent=`Tìm thấy ${g.length} món phù hợp`),s){const e=document.querySelector(`.taste-pill[data-taste="${t}"]`),n="all"!==t&&e?`[${e.textContent.trim()}]`:"";s.textContent=u?`với từ khóa "${u}" ${n}`:n}if(0===g.length)a&&(a.innerHTML="",a.style.display="none"),i&&(i.style.display="block",l&&(l.textContent=u?`"${u}"`:"gu vị đã chọn"));else if(i&&(i.style.display="none"),a){a.style.display="grid";let e="";g.forEach(t=>{const n=!1===t.is_available;let o="";if(n)o='<span class="menu-badge badge-sold-out">HẾT MÓN</span>';else if(t.badge){const e=t.badge.toUpperCase();let n="badge-best";e.includes("HOT")||e.includes("CHẠY")?n="badge-hot":e.includes("NEW")||e.includes("MỚI")?n="badge-new":e.includes("SIGNATURE")&&(n="badge-signature"),o=`<span class="menu-badge ${n}">${me(t.badge)}</span>`}const a=(Number(t.price)||0).toLocaleString("vi-VN")+"đ";e+=`\n                <article class="menu-card ${n?"is-sold-out":""}" id="card-item-${t.id}">\n                  <div class="menu-card-img-wrap">\n                    ${o}\n                    <button type="button" class="btn-fav-card ${(JSON.parse(localStorage.getItem('olion_fav_drinks')||'[]')).includes(t.name)?'active':''}" aria-label="Lưu món yêu thích" onclick="toggleFavoriteDrink(this, event)"><svg viewBox="0 0 24 24" width="16" height="16" fill="${(JSON.parse(localStorage.getItem('olion_fav_drinks')||'[]')).includes(t.name)?'#fff':'none'}" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg></button>\n                    <img src="${me(t.image_url||"assets/menu/espresso.webp")}" alt="${me(t.name)} — Olion Coffee" class="menu-card-img" width="300" height="300" loading="lazy" decoding="async" onerror="this.src='assets/menu/espresso.webp'" />\n                  </div>\n                  <div class="menu-card-body">\n                    <h3 class="menu-card-name">${me(t.name)}</h3>\n                    <div class="menu-card-price">${a}</div>\n                    <p class="menu-card-desc">${me(t.description||"")}</p>\n                  </div>\n                </article>\n              `}),a.innerHTML=e}}window.resetMenuSearch=function(){const e=document.getElementById("menuSearchInput"),t=document.getElementById("menuSearchClear");e&&(e.value=""),t&&(t.style.display="none"),ve="all",document.querySelectorAll(".taste-pill").forEach(e=>{e.classList.toggle("active","all"===e.getAttribute("data-taste"))}),Ce("","all")};const Te=document.getElementById("menuSearchInput"),ke=document.getElementById("menuSearchClear");let Be=null;Te&&Te.addEventListener("input",e=>{clearTimeout(Be),Be=setTimeout(()=>{Ce(e.target.value,ve)},180)}),ke&&ke.addEventListener("click",()=>{Te&&(Te.value=""),ke.style.display="none",Ce("",ve),Te&&Te.focus()}),document.querySelectorAll(".taste-pill").forEach(e=>{e.addEventListener("click",()=>{document.querySelectorAll(".taste-pill").forEach(e=>e.classList.remove("active")),e.classList.add("active"),ve=e.getAttribute("data-taste")||"all";Ce(Te?Te.value:"",ve)})}),document.querySelectorAll(".menu-tab-btn[data-cat]").forEach(e=>{e.addEventListener("click",()=>{Te&&(Te.value=""),ke&&(ke.style.display="none"),ve="all",document.querySelectorAll(".taste-pill").forEach(e=>{e.classList.toggle("active","all"===e.getAttribute("data-taste"))});const e=document.getElementById("cat-search");e&&e.classList.remove("active")})});let Le={mood:"",flavor:"",style:""},Se=null;function Me(e){for(let t=1;t<=3;t++){const n=document.getElementById(`quizStep${t}`),o=document.getElementById(`quizDot${t}`),a=document.getElementById("quizLine"+(t-1));n&&(n.style.display=t===e?"block":"none"),o&&o.classList.toggle("active",t<=e),a&&a.classList.toggle("active",t<=e)}const t=document.getElementById("quizResult");t&&(t.style.display="none")}async function xe(){if(console.log("FETCH FUNC TYPE:",typeof fetchSiteSettingsFromCloud),"function"!=typeof fetchSiteSettingsFromCloud)return;const e=await fetchSiteSettingsFromCloud();if(e.error&&console.log("FETCH ERROR",e.error),e.data){console.log("SYNC SETTINGS_JSON",JSON.stringify(e.data));const t=e.data,n=document.getElementById("wheelFloatBtn");n&&(!1===t.is_wheel_active?(console.log("SETTING NONE"),n.style.setProperty("display","none","important"),"function"==typeof closeWheelModal&&closeWheelModal()):(n.style.removeProperty("display"),n.style.display="flex")),t.wheel_prizes&&Array.isArray(t.wheel_prizes)&&t.wheel_prizes.length>=2&&(J=t.wheel_prizes.map(e=>({text:e.text||"Quà tặng",code:e.code||"OLIONGIFT",color:e.color||"#E59A55",desc:e.desc||e.text+" từ Olion Coffee!"})),Z(0));const o=document.getElementById("announcementBanner");if(o&&"true"!==sessionStorage.getItem("olion_announcement_dismissed"))if(!1===t.is_notification_active)o.style.display="none";else{const e=document.getElementById("announcementText");e&&t.notification_text&&(e.textContent=t.notification_text),o.style.display="block"}}}window.openTasteQuiz=function(){const e=document.getElementById("tasteQuizModal");e&&(resetTasteQuiz(),e.classList.add("active"),e.setAttribute("aria-hidden","false"),document.body.style.overflow="hidden",window.lucide&&window.lucide.createIcons())},window.closeTasteQuiz=function(){const e=document.getElementById("tasteQuizModal");e&&(e.classList.remove("active"),e.setAttribute("aria-hidden","true"),document.body.style.overflow="")},window.selectQuizAnswer=function(e,t){1===e?(Le.mood=t,Me(2)):2===e?(Le.flavor=t,Me(3)):3===e&&(Le.style=t,function(){for(let e=1;e<=3;e++){const t=document.getElementById(`quizStep${e}`);t&&(t.style.display="none")}const e=document.getElementById("quizResult");e&&(e.style.display="block");const t=Ie();let n=7,o="Sự kết hợp bùng nổ giữa vị đắng đậm đà của cà phê và lớp kem muối mặn béo ngậy giúp bạn bừng tỉnh cảm hứng!";const{mood:a,flavor:i,style:c}=Le;"healthy_oats"===i||"balanced_mild"===c&&"chill"===a?(n=9,o="Vị thanh lành, thơm bùi của sữa yến mạch Oatside hòa quyện espresso giúp bạn thư giãn trọn vẹn mà cực kỳ êm bụng."):"tea_floral"===i||"refresh"===a?"sweet"===a?(n=13,o="Vải ngọt mọng nước cùng hương hoa hồng thanh tao dịu nhẹ mang lại cảm giác ngọt ngào, thư thái đầy thi vị."):(n=15,o="Vị chua ngọt bùng nổ của chanh dây tươi giúp bạn đập tan cơn khát và nạp lại năng lượng sảng khoái ngay tức thì!"):"creamy_salt"===i||"sweet"===a?"warm_comfort"===c?(n=10,o="Cacao nguyên chất béo thơm, ấm áp xoa dịu tâm trí sau những giờ làm việc căng thẳng."):"chill"===a?(n=21,o="Matcha Nhật Bản thơm lừng hòa cùng sữa béo mịn, mang lại cảm giác bình yên, thư thái tuyệt đối."):(n=7,o="Lớp kem muối béo ngậy mằn mặn hòa cùng cà phê đậm đà — món Signature được yêu thích nhất tại Olion!"):"coffee_aroma"!==i&&"focus"!==a||("warm_comfort"===c?(n=6,o="Vị espresso thanh tao, sạch vị giúp giữ tinh thần tỉnh táo, minh mẫn cả ngày dài."):(n=2,o="Espresso đậm đà hòa quyện cùng sữa đặc truyền thống tạo nên nốt vị ngọt đắng trọn vẹn, đánh thức mọi giác quan."));Se=t.find(e=>e.id===n)||t[0];const s=document.getElementById("quizResultImg"),l=document.getElementById("quizResultTag"),r=document.getElementById("quizResultName"),d=document.getElementById("quizResultPrice"),u=document.getElementById("quizResultDesc"),m=document.getElementById("quizResultReason");Se&&(s&&(s.src=Se.image_url||"assets/menu/ca_phe_muoi.webp",s.alt=Se.name+" — Olion Coffee"),l&&(l.textContent=Se.badge||"SIGNATURE"),r&&(r.textContent=Se.name),d&&(d.textContent=(Number(Se.price)||0).toLocaleString("vi-VN")+"đ"),u&&(u.textContent=Se.description||""),m&&(m.innerHTML=`💡 <strong>Tại sao món này hợp với bạn:</strong> ${o}`));window.lucide&&window.lucide.createIcons()}())},window.prevQuizStep=function(e){Me(e)},window.resetTasteQuiz=function(){Le={mood:"",flavor:"",style:""},Se=null,Me(1)},window.handleQuizBookTable=function(){if(!Se)return;const e=Se.name,t=(Number(Se.price)||0).toLocaleString("vi-VN")+"đ";closeTasteQuiz(),openBookingModal("table",`Khách muốn đặt bàn trước & thưởng thức món ${e} (${t})! Nhờ Olion chuẩn bị nhé.`)},window.handleQuizViewInMenu=function(){if(!Se)return;const e=Se.name;closeTasteQuiz();const t=document.getElementById("menu");t&&t.scrollIntoView({behavior:"smooth"});const n=document.getElementById("menuSearchInput");n&&(n.value=e),Ce(e,"all"),setTimeout(()=>{const e=document.querySelector("#searchMenuGrid .menu-card");e&&(e.classList.add("menu-card-highlighted"),setTimeout(()=>e.classList.remove("menu-card-highlighted"),2500))},400)},window.addEventListener("storage",e=>{"olion_minigame"===e.key&&j(),xe(),"olion_announcement"===e.key&&he(),"olion_store_settings"===e.key&&ge(),"olion_menu_items"===e.key&&pe()});const Oe=()=>{if(j(),xe(),he(),ge(),pe(),we(),"undefined"!=typeof supabaseClient&&supabaseClient)try{supabaseClient.channel("public:menu_items").on("postgres_changes",{event:"*",schema:"public",table:"menu_items"},e=>{pe()}).on("postgres_changes",{event:"*",schema:"public",table:"feedbacks"},e=>{we()}).on("postgres_changes",{event:"*",schema:"public",table:"site_settings"},e=>{xe()}).subscribe()}catch(e){}},Ae=()=>{"function"==typeof window.loadSupabase?window.loadSupabase(()=>{"requestIdleCallback"in window?requestIdleCallback(Oe,{timeout:4e3}):setTimeout(Oe,1500)}):"requestIdleCallback"in window?requestIdleCallback(Oe,{timeout:4e3}):setTimeout(Oe,2e3)};"complete"===document.readyState?setTimeout(Ae,2e3):window.addEventListener("load",()=>setTimeout(Ae,2e3),{passive:!0,once:!0}),"serviceWorker"in navigator&&window.addEventListener("load",()=>{setTimeout(()=>{document.querySelectorAll(".hero-slide").forEach(e=>e.classList.add("zooming"))},2000),setTimeout(()=>{navigator.serviceWorker.register("service-worker.js").then(e=>{console.log("ServiceWorker registration successful")}).catch(e=>{console.log("ServiceWorker registration failed: ",e)})},4000)});let Ne=null,qe="pc";const $e=document.getElementById("floatingInstallBtn"),He=document.getElementById("drawerInstallBtn");window.addEventListener("beforeinstallprompt",e=>{e.preventDefault(),Ne=e}),window.switchInstallPlatform=function(e){document.querySelectorAll(".app-platform-tab").forEach(e=>e.classList.remove("active"));const t=document.getElementById("ios"===e?"tabBtnIos":"android"===e?"tabBtnAndroid":"tabBtnPc");t&&t.classList.add("active"),document.querySelectorAll(".platform-content-panel").forEach(e=>e.classList.remove("active"));const n=document.getElementById("ios"===e?"panelIos":"android"===e?"panelAndroid":"panelPc");n&&n.classList.add("active"),window.lucide&&window.lucide.createIcons()};const Fe=()=>{const e=document.getElementById("downloadAppModal");if(!e)return;e.classList.add("active"),qe=function(){const e=navigator.userAgent||navigator.vendor||window.opera||"";return/iPad|iPhone|iPod/.test(e)||"MacIntel"===navigator.platform&&navigator.maxTouchPoints>1?"ios":/android/i.test(e)?"android":"pc"}();const t=document.getElementById("badgeIos"),n=document.getElementById("badgeAndroid"),o=document.getElementById("badgePc");t&&(t.style.display="ios"===qe?"inline-block":"none"),n&&(n.style.display="android"===qe?"inline-block":"none"),o&&(o.style.display="pc"===qe?"inline-block":"none"),switchInstallPlatform(qe)};window.showInstallGuideDetail=function(e){switchInstallPlatform(e),window.showOlionToast&&window.showOlionToast("Đã mở hướng dẫn cài đặt iOS!","apple")},window.handleAndroidInstall=async function(){if(null!=Ne){Ne.prompt();const{outcome:e}=await Ne.userChoice;"accepted"===e&&(window.showOlionToast&&window.showOlionToast("Cảm ơn bạn đã cài đặt Olion Coffee!","check-circle"),document.getElementById("downloadAppModal")?.classList.remove("active")),Ne=null}else switchInstallPlatform("android"),window.showOlionToast&&window.showOlionToast("Vui lòng làm theo hướng dẫn ở bên dưới để cài đặt!","smartphone")},window.handlePcInstall=async function(){if(null!=Ne){Ne.prompt();const{outcome:e}=await Ne.userChoice;"accepted"===e&&(window.showOlionToast&&window.showOlionToast("Cảm ơn bạn đã cài đặt App trên máy tính!","check-circle"),document.getElementById("downloadAppModal")?.classList.remove("active")),Ne=null}else switchInstallPlatform("pc"),window.showOlionToast&&window.showOlionToast("Xem hướng dẫn biểu tượng cài đặt [⊕] trên thanh địa chỉ URL!","monitor")},$e&&$e.addEventListener("click",Fe),He&&He.addEventListener("click",Fe),window.shareApp=async()=>{if(navigator.share)try{await navigator.share({title:"Olion Coffee",text:"Góc nhỏ bình yên giữa lòng Sài Gòn. Khám phá menu cà phê thủ công tinh tế ngay!",url:window.location.href})}catch(e){console.log("User cancelled share or error:",e)}else navigator.clipboard.writeText(window.location.href),showOlionToast("Đã sao chép link website!","🔗")}});
// ======== WISHLIST & DIGITAL STAMP CARD FUNCTIONS ========
window.toggleFavoriteDrink = function(btn, evt) {
  if (evt) evt.stopPropagation();
  const card = btn.closest('.menu-card');
  if (!card) return;
  const nameEl = card.querySelector('.menu-card-name');
  if (!nameEl) return;
  const name = nameEl.textContent.trim();
  let favs = JSON.parse(localStorage.getItem('olion_fav_drinks') || '[]');
  const idx = favs.indexOf(name);
  let isAdd = false;
  if (idx > -1) {
    favs.splice(idx, 1);
  } else {
    favs.push(name);
    isAdd = true;
  }
  localStorage.setItem('olion_fav_drinks', JSON.stringify(favs));

  document.querySelectorAll('.menu-card').forEach(c => {
    const n = c.querySelector('.menu-card-name');
    if (n && n.textContent.trim() === name) {
      const b = c.querySelector('.btn-fav-card');
      if (b) {
        b.classList.toggle('active', isAdd);
        const svg = b.querySelector('svg');
        if (svg) svg.setAttribute('fill', isAdd ? '#fff' : 'none');
      }
    }
  });

  const badge = document.getElementById('favCount');
  if (badge) badge.textContent = favs.length;

  if (window.showOlionToast) {
    window.showOlionToast(isAdd ? `Đã lưu "${name}" vào món yêu thích! ❤️` : `Đã bỏ "${name}" khỏi yêu thích`, isAdd ? 'heart' : 'check');
  }

  const activePill = document.querySelector('.taste-pill.active');
  if (activePill && activePill.getAttribute('data-taste') === 'favorites') {
    if (typeof Ce === 'function') Ce(document.getElementById('menuSearchInput')?.value || '', 'favorites');
  }
};

window.renderUnifiedLoyaltyCard = async function(phone = '') {
  let activePhone = (phone || localStorage.getItem('olion_customer_phone') || '').replace(/[^0-9]/g, '').trim();
  let member = null;

  if (activePhone && window.lookupLoyaltyMember) {
    try {
      const res = await window.lookupLoyaltyMember(activePhone);
      if (res && res.success && res.member) {
        member = res.member;
      }
    } catch(e) {}
  }

  // Fallback to local member profile or defaults
  if (!member) {
    const localName = localStorage.getItem('olion_customer_name') || 'Khách hàng thân thiết';
    const localCode = localStorage.getItem('olion_member_code') || ('OLION-' + (activePhone ? activePhone.slice(-4) : Math.floor(1000 + Math.random() * 9000)));
    let localStamps = parseInt(localStorage.getItem('olion_stamps') || '1', 10);
    if (isNaN(localStamps) || localStamps < 0) localStamps = 1;
    if (localStamps > 8) localStamps = 8;
    member = {
      customer_name: localName,
      phone_number: activePhone || 'Chưa đăng ký SĐT',
      member_code: localCode,
      tier: 'Thành viên',
      stamps_count: localStamps,
      total_stamps: localStamps,
      free_drinks_earned: 0,
      points: localStamps * 10
    };
  }

  // Cache active member details
  if (member.member_code) localStorage.setItem('olion_member_code', member.member_code);
  localStorage.setItem('olion_stamps', String(member.stamps_count || 0));

  // Render Card Elements
  const nameEl = document.getElementById('loyaltyCardHolderName');
  if (nameEl) nameEl.textContent = member.customer_name || 'Khách hàng thân thiết';

  const phoneEl = document.getElementById('loyaltyCardPhone');
  if (phoneEl) phoneEl.textContent = member.phone_number && member.phone_number !== 'Chưa đăng ký SĐT' ? `SĐT: ${member.phone_number}` : '';

  const codeEl = document.getElementById('loyaltyMemberCode');
  if (codeEl) codeEl.textContent = member.member_code || 'OLION-8869';

  const tierBadge = document.getElementById('loyaltyCardTierBadge');
  if (tierBadge) {
    tierBadge.textContent = member.tier || 'Thành viên';
    if (member.tier === 'Kim Cương') {
      tierBadge.style.background = 'rgba(155, 89, 182, 0.25)';
      tierBadge.style.color = '#d2a8e8';
    } else if (member.tier === 'Vàng') {
      tierBadge.style.background = 'rgba(241, 196, 15, 0.25)';
      tierBadge.style.color = '#f1c40f';
    } else if (member.tier === 'Bạc') {
      tierBadge.style.background = 'rgba(189, 195, 199, 0.25)';
      tierBadge.style.color = '#ecf0f1';
    } else {
      tierBadge.style.background = 'rgba(46, 204, 113, 0.2)';
      tierBadge.style.color = '#2ecc71';
    }
  }

  const statCurrent = document.getElementById('loyaltyStatCurrentStamps');
  if (statCurrent) statCurrent.textContent = `${member.stamps_count}/8`;

  const statTotal = document.getElementById('loyaltyStatTotalStamps');
  if (statTotal) statTotal.textContent = `${member.total_stamps || member.stamps_count} tem`;

  const statFree = document.getElementById('loyaltyStatFreeDrinks');
  if (statFree) statFree.textContent = `${member.free_drinks_earned || 0} ly`;

  // Render 8 Stamps Grid
  const grid = document.getElementById('stampGrid');
  if (grid) {
    let html = '';
    const stamps = member.stamps_count || 0;
    for (let i = 1; i <= 8; i++) {
      const isStamped = i <= stamps;
      if (i === 8) {
        html += `<div class="stamp-slot reward ${isStamped ? 'stamped' : ''}"><span class="stamp-icon">🎁</span><span>${isStamped ? 'ĐỦ ĐIỀU KIỆN!' : 'Tặng 1 ly'}</span></div>`;
      } else {
        html += `<div class="stamp-slot ${isStamped ? 'stamped' : ''}"><span class="stamp-icon">☕</span><span>Tem ${i}</span></div>`;
      }
    }
    grid.innerHTML = html;
  }

  // Update Status Text
  const statusEl = document.getElementById('stampStatusText');
  if (statusEl) {
    const stamps = member.stamps_count || 0;
    if (stamps >= 8) {
      statusEl.innerHTML = `🎉 <strong>Chúc mừng!</strong> Bạn đã tích đủ 8 tem! Hãy đưa mã thẻ cho thu ngân để nhận <strong>1 ly nước miễn phí</strong> ngay hôm nay!`;
    } else {
      const remain = 8 - stamps;
      statusEl.innerHTML = `Bạn đã tích được <span id="currentStampCount" style="color:#2ecc71; font-size:15px; font-weight:800;">${stamps}</span> / 8 tem! (Còn ${remain} tem nữa để nhận quà 🎁)`;
    }
  }

  return member;
};

window.renderLoyaltyStamps = function() {
  return window.renderUnifiedLoyaltyCard();
};

window.openLoyaltyModal = function(phone = '') {
  const modal = document.getElementById('loyaltyLookupModal');
  if (!modal) return;
  modal.classList.add('active');
  modal.setAttribute('aria-hidden', 'false');
  document.body.style.overflow = 'hidden';

  const inlineReg = document.getElementById('loyaltyRegisterInlineArea');
  if (inlineReg) inlineReg.style.display = 'none';

  const errCard = document.getElementById('loyaltyErrorCard');
  if (errCard) errCard.style.display = 'none';

  const searchInput = document.getElementById('loyaltySearchPhone');
  if (searchInput) {
    const initialPhone = phone || localStorage.getItem('olion_customer_phone') || '';
    if (initialPhone) searchInput.value = initialPhone;
  }

  window.renderUnifiedLoyaltyCard(phone);
};

window.closeLoyaltyModal = function() {
  const modal = document.getElementById('loyaltyLookupModal');
  if (!modal) return;
  modal.classList.remove('active');
  modal.setAttribute('aria-hidden', 'true');
  document.body.style.overflow = '';
};

window.handleLoyaltyLookup = async function(e) {
  if (e && e.preventDefault) e.preventDefault();
  const searchInput = document.getElementById('loyaltySearchPhone');
  const btn = document.getElementById('loyaltySearchBtn');
  const inlineReg = document.getElementById('loyaltyRegisterInlineArea');
  const errCard = document.getElementById('loyaltyErrorCard');
  const phone = (searchInput?.value || '').replace(/[^0-9]/g, '').trim();

  if (!phone || phone.length < 10) {
    if (errCard) {
      errCard.textContent = 'Vui lòng nhập số điện thoại hợp lệ (10 số)!';
      errCard.style.display = 'block';
    }
    return;
  }

  if (btn) {
    btn.disabled = true;
    btn.textContent = 'Đang tìm...';
  }
  if (errCard) errCard.style.display = 'none';
  if (inlineReg) inlineReg.style.display = 'none';

  try {
    const res = await window.lookupLoyaltyMember(phone);
    if (res && res.success && res.member) {
      localStorage.setItem('olion_customer_phone', phone);
      localStorage.setItem('olion_customer_name', res.member.customer_name);
      await window.renderUnifiedLoyaltyCard(phone);
      if (window.showOlionToast) window.showOlionToast(`Đã tìm thấy Thẻ Thành Viên của ${res.member.customer_name}! 👑`, 'award');
    } else {
      // Phone not found -> Show inline registration!
      if (inlineReg) {
        inlineReg.style.display = 'block';
        const inlineName = document.getElementById('loyaltyInlineName');
        if (inlineName) {
          inlineName.value = '';
          setTimeout(() => inlineName.focus(), 100);
        }
      }
      if (window.showOlionToast) window.showOlionToast('Số điện thoại chưa có thẻ. Hãy tạo thẻ ngay bên dưới!', 'sparkles');
    }
  } catch(err) {
    if (errCard) {
      errCard.textContent = 'Có lỗi xảy ra khi tra cứu. Vui lòng thử lại sau.';
      errCard.style.display = 'block';
    }
  } finally {
    if (btn) {
      btn.disabled = false;
      btn.textContent = 'Tra Cứu';
    }
  }
};

window.handleInlineLoyaltyRegister = async function(e) {
  if (e && e.preventDefault) e.preventDefault();
  const searchInput = document.getElementById('loyaltySearchPhone');
  const nameInput = document.getElementById('loyaltyInlineName');
  const btn = document.getElementById('loyaltyInlineRegisterBtn');
  const inlineReg = document.getElementById('loyaltyRegisterInlineArea');

  const phone = (searchInput?.value || '').replace(/[^0-9]/g, '').trim();
  const name = (nameInput?.value || '').trim();

  if (!name) return alert('Vui lòng nhập họ và tên của bạn!');
  if (!phone || phone.length < 10) return alert('Vui lòng nhập đúng số điện thoại (10 số)!');

  if (btn) {
    btn.disabled = true;
    btn.textContent = 'Đang kích hoạt...';
  }

  const memberCode = window.generateMemberCode ? window.generateMemberCode(phone) : ('OLION-' + phone.slice(-4));
  const newMember = {
    name,
    contact: phone,
    member_code: memberCode,
    stamps_count: 1,
    total_stamps: 1,
    free_drinks_earned: 0,
    points: 10,
    tier: 'Thành viên',
    source: 'Đăng Ký Tại Thẻ Web',
    notes: 'Kích hoạt thẻ thành viên tại Thẻ Web'
  };

  try {
    if (window.saveCustomerToCloud) {
      await window.saveCustomerToCloud(newMember);
    }
  } catch(err) {
    console.warn('Lỗi lưu cloud:', err);
  }

  localStorage.setItem('olion_customer_name', name);
  localStorage.setItem('olion_customer_phone', phone);
  localStorage.setItem('olion_member_code', memberCode);
  localStorage.setItem('olion_stamps', '1');

  if (inlineReg) inlineReg.style.display = 'none';
  if (btn) {
    btn.disabled = false;
    btn.textContent = 'Kích Hoạt Ngay';
  }

  await window.renderUnifiedLoyaltyCard(phone);
  if (window.showOlionToast) {
    window.showOlionToast(`🎉 Chúc mừng ${name} đã kích hoạt Thẻ Thành Viên! Tặng bạn 1 tem ☕`, 'award');
  }
};

window.handleWelcomeSubmit = async function(e) {
  if (e && e.preventDefault) e.preventDefault();
  const nameInput = document.getElementById('welcomeName');
  const phoneInput = document.getElementById('welcomePhone');
  const submitBtn = document.getElementById('welcomeSubmitBtn');

  const name = (nameInput?.value || '').trim();
  const phone = (phoneInput?.value || '').replace(/[^0-9]/g, '').trim();

  if (!name) return alert('Vui lòng nhập họ và tên của bạn!');
  if (!/^(03|05|07|08|09)[0-9]{8}$/.test(phone)) {
    if (window.showOlionToast) window.showOlionToast('Vui lòng nhập đúng số điện thoại (10 số)!', 'alert-circle');
    phoneInput?.focus();
    return;
  }

  if (submitBtn) {
    submitBtn.disabled = true;
    submitBtn.textContent = 'Đang kích hoạt thẻ...';
  }

  const memberCode = window.generateMemberCode ? window.generateMemberCode(phone) : ('OLION-' + phone.slice(-4));
  const newMember = {
    name,
    contact: phone,
    member_code: memberCode,
    stamps_count: 1,
    total_stamps: 1,
    free_drinks_earned: 0,
    points: 10,
    tier: 'Thành viên',
    source: 'Popup Chào Mừng',
    notes: 'Đăng ký qua Popup Chào Mừng'
  };

  try {
    if (window.saveCustomerToCloud) {
      await window.saveCustomerToCloud(newMember);
    }
  } catch(err) {
    console.warn('Lỗi lưu cloud:', err);
  }

  localStorage.setItem('olion_customer_name', name);
  localStorage.setItem('olion_customer_phone', phone);
  localStorage.setItem('olion_member_code', memberCode);
  localStorage.setItem('olion_stamps', '1');

  // Trigger push notification opt-in if pre-checked
  const notifCb = document.getElementById('welcomeNotifCheckbox');
  if (!notifCb || notifCb.checked) {
    if (typeof window.triggerPushNotificationOptIn === 'function') {
      window.triggerPushNotificationOptIn('welcome_popup');
    }
  }

  if (submitBtn) {
    submitBtn.disabled = false;
    submitBtn.textContent = '☕ Kích Hoạt Thẻ & Nhận 1 Tem Ngay';
  }

  if (typeof window.closeWelcomeModal === 'function') window.closeWelcomeModal();
  if (typeof window.updateDynamicGreeting === 'function') window.updateDynamicGreeting();

  if (window.showOlionToast) {
    window.showOlionToast(`🎉 Chúc mừng ${name} đã gia nhập Thành Viên Olion! Tặng bạn 1 tem ☕`, 'award');
  }

  // Tự động mở Thẻ Thành Viên Điện Tử ngay cho khách
  setTimeout(() => {
    if (typeof window.openLoyaltyModal === 'function') {
      window.openLoyaltyModal(phone);
    }
  }, 400);
};

window.simulateAddStamp = async function() {
  let stamps = parseInt(localStorage.getItem('olion_stamps') || '1', 10);
  if (stamps >= 8) {
    alert('Bạn đã tích đủ 8 tem! Hãy đổi ly nước miễn phí hoặc đưa mã cho thu ngân nhé.');
    return;
  }
  stamps += 1;
  localStorage.setItem('olion_stamps', String(stamps));

  const phone = localStorage.getItem('olion_customer_phone');
  if (phone && window.addCustomerStampInCloud) {
    try {
      await window.addCustomerStampInCloud(null, phone, 1, 'Thử tích tem');
    } catch(e) {}
  }

  await window.renderUnifiedLoyaltyCard();
  if (window.showOlionToast) {
    window.showOlionToast(stamps === 8 ? '🎉 Chúc mừng bạn đã tích đủ 8 tem nhận quà!' : `Tích thành công tem thứ ${stamps}! ☕`, 'award');
  }
};

window.resetLoyaltyStamps = async function() {
  if (confirm('Bạn có muốn đặt lại thẻ tích điểm mới (bắt đầu lại từ 0 tem)?')) {
    localStorage.setItem('olion_stamps', '0');
    const phone = localStorage.getItem('olion_customer_phone');
    if (phone && window.saveCustomerToCloud) {
      try {
        await window.saveCustomerToCloud({ contact: phone, stamps_count: 0 });
      } catch(e) {}
    }
    await window.renderUnifiedLoyaltyCard();
    if (window.showOlionToast) window.showOlionToast('Đã làm mới thẻ tích điểm!', 'rotate-ccw');
  }
};
// Toast Notification Handler
let toastTimer = null;
window.showOlionToast = function(msg, icon = 'sparkles') {
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
  }
  toast.classList.add('show');
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => {
    toast.classList.remove('show');
  }, 3200);
};

// Standard Sharing Function (Default)
window.standardShareApp = async function() {
  const shareTitle = 'Olion Coffee';
  const shareText = 'Góc nhỏ bình yên giữa lòng Sài Gòn. Khám phá menu cà phê thủ công tinh tế ngay!';
  const shareUrl = window.location.href;
  if (navigator.share) {
    try {
      await navigator.share({ title: shareTitle, text: shareText, url: shareUrl });
    } catch(e) {}
  } else {
    if (navigator.clipboard) navigator.clipboard.writeText(shareUrl);
    if (window.showOlionToast) window.showOlionToast('Đã sao chép link website!', 'link');
  }
};
window.shareApp = window.standardShareApp;

// Share & Earn Referral System (Managed from Admin - DEFAULT OFF)
window.syncShareEarnState = function() {
  let settings = null;
  try {
    settings = JSON.parse(localStorage.getItem('olion_share_earn_settings'));
  } catch(e) {}

  // MẶC ĐỊNH LÀ TẮT (DEFAULT: FALSE)
  const isActive = !!(settings && settings.is_active === true);

  const headerEarnBtn = document.getElementById('headerShareEarnBtn');
  const headerNormalBtn = document.getElementById('headerNormalShareBtn');
  const drawerEarnBtn = document.getElementById('drawerShareEarnBtn');
  const loyaltyBanner = document.getElementById('loyaltyShareEarnBanner');
  const modal = document.getElementById('shareEarnModal');

  if (isActive) {
    if (headerEarnBtn) {
      headerEarnBtn.style.removeProperty('display');
      headerEarnBtn.style.display = 'inline-flex';
    }
    if (headerNormalBtn) {
      headerNormalBtn.style.setProperty('display', 'none', 'important');
    }
    if (drawerEarnBtn) {
      drawerEarnBtn.style.removeProperty('display');
      drawerEarnBtn.style.display = 'flex';
    }
    if (loyaltyBanner) {
      loyaltyBanner.style.removeProperty('display');
      loyaltyBanner.style.display = 'flex';
    }

    if (settings && settings.voucher_code) {
      const vEl = document.getElementById('shareVoucherCode');
      if (vEl) vEl.textContent = settings.voucher_code;
    }
    window.shareApp = window.openShareEarnModal;
  } else {
    if (headerEarnBtn) {
      headerEarnBtn.style.setProperty('display', 'none', 'important');
    }
    if (headerNormalBtn) {
      headerNormalBtn.style.removeProperty('display');
    }
    if (drawerEarnBtn) {
      drawerEarnBtn.style.setProperty('display', 'none', 'important');
    }
    if (loyaltyBanner) {
      loyaltyBanner.style.setProperty('display', 'none', 'important');
    }
    if (modal) {
      modal.classList.remove('active');
      modal.setAttribute('aria-hidden', 'true');
    }
    window.shareApp = window.standardShareApp;
  }
};

window.openShareEarnModal = function() {
  let settings = null;
  try { settings = JSON.parse(localStorage.getItem('olion_share_earn_settings')); } catch(e) {}
  if (!settings || settings.is_active !== true) {
    if (typeof window.standardShareApp === 'function') window.standardShareApp();
    return;
  }
  const modal = document.getElementById('shareEarnModal');
  if (!modal) return;
  modal.classList.add('active');
  modal.setAttribute('aria-hidden', 'false');
  document.body.style.overflow = 'hidden';
  if (localStorage.getItem('olion_share_rewarded')) {
    const statusEl = document.getElementById('shareRewardClaimStatus');
    if (statusEl) statusEl.innerHTML = '✓ <strong>Bạn đã nhận ưu đãi!</strong> Tiếp tục chia sẻ để bạn bè cùng nhận mã giảm giá nhé.';
  }
  if (window.lucide) window.lucide.createIcons();
};

window.closeShareEarnModal = function() {
  const modal = document.getElementById('shareEarnModal');
  if (!modal) return;
  modal.classList.remove('active');
  modal.setAttribute('aria-hidden', 'true');
  document.body.style.overflow = '';
};

function rewardShareBonus() {
  let settings = null;
  try { settings = JSON.parse(localStorage.getItem('olion_share_earn_settings')); } catch(e) {}
  if (!settings || settings.is_active !== true) return;

  // Track stats
  try {
    const curCount = parseInt(localStorage.getItem('olion_share_stats_count') || '0', 10);
    localStorage.setItem('olion_share_stats_count', String(curCount + 1));
  } catch(e) {}

  const stampBonus = typeof settings.stamp_bonus !== 'undefined' ? parseInt(settings.stamp_bonus, 10) : 1;
  if (!localStorage.getItem('olion_share_rewarded')) {
    localStorage.setItem('olion_share_rewarded', 'true');
    if (stampBonus > 0) {
      let stamps = parseInt(localStorage.getItem('olion_stamps') || '2', 10);
      if (isNaN(stamps) || stamps < 0) stamps = 2;
      if (stamps < 8) {
        stamps = Math.min(8, stamps + stampBonus);
        localStorage.setItem('olion_stamps', stamps);
        if (typeof window.renderLoyaltyStamps === 'function') window.renderLoyaltyStamps();
      }
    }
    const statusEl = document.getElementById('shareRewardClaimStatus');
    if (statusEl) statusEl.innerHTML = '🎉 <strong>Tuyệt vời!</strong> Bạn vừa nhận được ưu đãi độc quyền!';
    if (window.showOlionToast) {
      setTimeout(() => {
        window.showOlionToast(stampBonus > 0 ? `🎉 Tặng bạn +${stampBonus} tem vào Thẻ tích điểm!` : '🎉 Đã nhận ưu đãi chia sẻ!', 'award');
      }, 500);
    }
  }
}

window.copyShareVoucher = function() {
  let settings = null;
  try { settings = JSON.parse(localStorage.getItem('olion_share_earn_settings')); } catch(e) {}
  const code = (settings && settings.voucher_code) || 'OLIONBANBE15';
  rewardShareBonus();
  const finishCopy = () => {
    const btnText = document.getElementById('copyVoucherBtnText');
    if (btnText) {
      btnText.textContent = '✓ Đã chép!';
      setTimeout(() => { btnText.textContent = 'Sao chép'; }, 2000);
    }
    if (window.showOlionToast) window.showOlionToast(`Đã sao chép mã: ${code}`, 'check');
  };
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(code).then(finishCopy).catch(finishCopy);
  } else {
    finishCopy();
  }
};

window.handleShareAction = function(platform) {
  let settings = null;
  try { settings = JSON.parse(localStorage.getItem('olion_share_earn_settings')); } catch(e) {}
  const shareUrl = (settings && settings.target_url) || 'https://www.olioncoffee.app/?ref=share';
  const shareTitle = (settings && settings.share_title) || 'Olion Coffee — Quán Cà Phê Yên Tĩnh Fine Dining Gò Vấp';
  const shareText = (settings && settings.share_message) || 'Ghé Olion Coffee thưởng thức Cà Phê Muối Fine Dining và không gian yên tĩnh tuyệt đẹp! Nhập mã OLIONBANBE15 để được giảm 15% nhé:';

  rewardShareBonus();

  if (platform === 'zalo') {
    window.open(`https://zalo.me/share?url=${encodeURIComponent(shareUrl)}`, '_blank');
  } else if (platform === 'facebook') {
    window.open(`https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(shareUrl)}`, '_blank', 'width=600,height=500');
  } else if (platform === 'native') {
    if (navigator.share) {
      navigator.share({ title: shareTitle, text: shareText, url: shareUrl }).catch(() => {});
    } else {
      if (navigator.clipboard) navigator.clipboard.writeText(shareUrl);
      if (window.showOlionToast) window.showOlionToast('Đã sao chép link website Olion!', 'link');
    }
  } else if (platform === 'copy') {
    const finishCopy = () => {
      const btnText = document.getElementById('copyLinkBtnText');
      if (btnText) {
        btnText.textContent = '✓ Đã chép!';
        setTimeout(() => { btnText.textContent = 'Sao chép link'; }, 2000);
      }
      if (window.showOlionToast) window.showOlionToast('Đã sao chép link chia sẻ!', 'link');
    };
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(shareUrl).then(finishCopy).catch(finishCopy);
    } else {
      finishCopy();
    }
  }
};

// Storage event listener for Realtime sync
window.addEventListener('storage', (e) => {
  if (e.key === 'olion_share_earn_settings') {
    if (typeof window.syncShareEarnState === 'function') window.syncShareEarnState();
  }
});

// Initialize Favs count & render stamps on ready
document.addEventListener('DOMContentLoaded', () => {
  try {
    if (typeof renderMenuPanels === 'function' && typeof be !== 'undefined') renderMenuPanels(be);
    const favs = JSON.parse(localStorage.getItem('olion_fav_drinks') || '[]');
    const badge = document.getElementById('favCount');
    if (badge) badge.textContent = favs.length;
    document.querySelectorAll('.menu-card').forEach(c => {
      const n = c.querySelector('.menu-card-name');
      if (n && favs.includes(n.textContent.trim())) {
        const b = c.querySelector('.btn-fav-card');
        if (b) {
          b.classList.add('active');
          const svg = b.querySelector('svg');
          if (svg) svg.setAttribute('fill', '#fff');
        }
      }
    });
    if (typeof renderLoyaltyStamps === 'function') renderLoyaltyStamps();

    // Sync Share & Earn state on load (Default is OFF)
    if (typeof window.syncShareEarnState === 'function') window.syncShareEarnState();

    // Check referral visitor (Only show welcome if Share & Earn is active)
    let seSettings = null;
    try { seSettings = JSON.parse(localStorage.getItem('olion_share_earn_settings')); } catch(e) {}
    if (seSettings && seSettings.is_active === true) {
      const urlParams = new URLSearchParams(window.location.search);
      if (urlParams.get('ref')) {
        setTimeout(() => {
          const vCode = seSettings.voucher_code || 'OLIONBANBE15';
          if (window.showOlionToast) window.showOlionToast(`🎁 Chào mừng bạn! Mã giảm giá: ${vCode}`, 'gift');
        }, 1500);
      }
    }
  } catch(e) { console.warn("Init error:", e); }
});

window.closeMobileDrawer = function() {
  if (typeof toggleDrawer === 'function') toggleDrawer(false);
  const drawer = document.getElementById('mobileDrawer');
  const overlay = document.getElementById('mobileDrawerOverlay');
  if (drawer) drawer.classList.remove('active');
  if (overlay) overlay.classList.remove('active');
  document.body.style.overflow = '';
};


// ==============================================================================
// SMART PWA DIRECT AUTO-INSTALL & PUSH NOTIFICATION SYSTEM
// ==============================================================================
window.triggerPwaInstall = async function() {
  if (window.matchMedia('(display-mode: standalone)').matches || window.navigator.standalone === true) {
    if (window.showOlionToast) window.showOlionToast('Bạn đang sử dụng App Olion Coffee rồi! ☕', 'check-circle');
    return;
  }

  const isIos = /iPad|iPhone|iPod/.test(navigator.userAgent) && !window.MSStream;
  if (isIos) {
    const modal = document.getElementById('downloadAppModal');
    if (modal) {
      modal.classList.add('active');
      if (typeof window.switchInstallPlatform === 'function') window.switchInstallPlatform('ios');
    }
    return;
  }

  if (/FBAN|FBAV|Zalo|Line/i.test(navigator.userAgent)) {
    alert('Bạn đang xem web trong ứng dụng Zalo/Facebook!\n\nĐể tự động cài App:\n1. Bấm dấu 3 chấm (...) ở góc trên.\n2. Chọn "Mở bằng trình duyệt" (Chrome / Safari).\n3. Bấm lại nút "Cài đặt" để máy tự động cài App nhé!');
    return;
  }

  const promptEvent = window.deferredInstallPrompt || window.Ne;
  if (promptEvent) {
    try {
      promptEvent.prompt();
      const choiceResult = await promptEvent.userChoice;
      if (choiceResult && choiceResult.outcome === 'accepted') {
        if (window.showOlionToast) window.showOlionToast('Đang cài đặt App Olion Coffee vào thiết bị của bạn...', 'smartphone');
        window.deferredInstallPrompt = null;
        window.Ne = null;
      }
      return;
    } catch(err) {
      console.warn('triggerPwaInstall error:', err);
    }
  }

  const isAndroid = /android/i.test(navigator.userAgent);
  if (isAndroid) {
    if (window.showOlionToast) window.showOlionToast('Bấm dấu 3 chấm ⋮ ở góc trên Chrome ➔ Chọn "Cài đặt ứng dụng"!', 'smartphone');
  } else {
    if (window.showOlionToast) window.showOlionToast('Bấm biểu tượng Cài đặt [⊕] trên thanh địa chỉ URL để cài App!', 'monitor');
  }
  const modal = document.getElementById('downloadAppModal');
  if (modal) {
    modal.classList.add('active');
    if (typeof window.switchInstallPlatform === 'function') window.switchInstallPlatform(isAndroid ? 'android' : 'pc');
  }
};

window.openDownloadAppModal = function(platform) {
  window.triggerPwaInstall();
};

window.triggerPushNotificationOptIn = async function(source = 'general') {
  try {
    localStorage.setItem('olion_notif_requested', 'true');
    localStorage.setItem('olion_notif_source', source);

    if (/FBAN|FBAV|Zalo|Line/i.test(navigator.userAgent)) {
      alert('Bạn đang xem trong ứng dụng Zalo/Facebook!\n\nVui lòng mở bằng trình duyệt (Chrome/Safari) để bật thông báo và nhận mã giảm giá.');
      return;
    }

    if (!('Notification' in window)) {
      if (window.showOlionToast) window.showOlionToast('Trình duyệt này không hỗ trợ thông báo.', 'alert-circle');
      return;
    }

    if (Notification.permission === 'granted') {
      if (window.showOlionToast) window.showOlionToast('Bạn đã bật nhận thông báo Olion Coffee rồi! Cảm ơn bạn.', 'bell');
      return;
    }

    if (Notification.permission === 'denied') {
      alert('Bạn đang chặn thông báo trên trình duyệt web này!\n\nĐể nhận thông báo món mới và sự kiện từ Olion:\n1. Bấm vào biểu tượng 🔒 (hoặc Cài đặt trang web) bên trái thanh địa chỉ URL.\n2. Bật "Cho phép" (Allow) mục Thông báo.\n3. Tải lại trang web là xong!');
      return;
    }

    if (window.OneSignal && window.OneSignal.Notifications && typeof window.OneSignal.Notifications.requestPermission === 'function') {
      try {
        const granted = await window.OneSignal.Notifications.requestPermission();
        if (granted) {
          if (window.showOlionToast) window.showOlionToast('Đã bật thông báo thành công! Olion sẽ cập nhật món mới & sự kiện đến bạn.', 'bell');
          return;
        }
      } catch (err) {
        console.warn('OneSignal Notifications error:', err);
      }
    }

    const permission = await Notification.requestPermission();
    if (permission === 'granted') {
      if (window.showOlionToast) window.showOlionToast('Đã bật thông báo thành công! Olion sẽ cập nhật món mới & sự kiện đến bạn.', 'bell');
      if (window.OneSignalDeferred) {
        window.OneSignalDeferred.push(async function(OneSignal) {
          try {
            if (OneSignal.Notifications && OneSignal.Notifications.requestPermission) {
              await OneSignal.Notifications.requestPermission();
            }
          } catch(e) {}
        });
      }
    } else if (permission === 'denied') {
      if (window.showOlionToast) window.showOlionToast('Bạn đã từ chối nhận thông báo.', 'alert-circle');
    }
  } catch(e) {
    console.error('Push notification opt-in error:', e);
  }
};

window.triggerWelcomePushOptIn = function() {
  if (typeof window.closeWelcomeModal === 'function') window.closeWelcomeModal();
  window.triggerPushNotificationOptIn('welcome_returning');
};

window.triggerSmartPerkNotif = function() {
  window.dismissSmartPerkBar();
  window.triggerPushNotificationOptIn('smart_perk_bar');
};

window.triggerSmartPerkApp = function() {
  window.dismissSmartPerkBar();
  window.triggerPwaInstall();
};

window.dismissSmartPerkBar = function() {
  const bar = document.getElementById('smartPerkBar');
  if (bar) {
    bar.classList.remove('visible');
    sessionStorage.setItem('olion_smart_perk_dismissed', 'true');
  }
};

function initSmartPerkBar() {
  if (sessionStorage.getItem('olion_smart_perk_dismissed') === 'true') return;
  setTimeout(() => {
    const bar = document.getElementById('smartPerkBar');
    if (bar && sessionStorage.getItem('olion_smart_perk_dismissed') !== 'true') {
      bar.classList.add('visible');
      if (window.lucide && window.lucide.createIcons) window.lucide.createIcons();
    }
  }, 12000);
}
if ('requestIdleCallback' in window) {
  requestIdleCallback(() => setTimeout(initSmartPerkBar, 1500));
} else {
  setTimeout(initSmartPerkBar, 3000);
}
