const DEFAULT_SUPABASE_URL=localStorage.getItem("olion_supabase_url")||"https://xwbrbesgnwcngzohprxt.supabase.co",DEFAULT_SUPABASE_ANON_KEY=localStorage.getItem("olion_supabase_key")||"sb_publishable_vWuV07_xPU0wNftK0lpnFQ_oA9XHPLS";let supabaseClient=null;function initSupabase(e,t){const a=e||localStorage.getItem("olion_supabase_url")||DEFAULT_SUPABASE_URL,n=t||localStorage.getItem("olion_supabase_key")||DEFAULT_SUPABASE_ANON_KEY;if(!(window.supabase&&a&&n)||a.includes("your-project")||"your-anon-key"===n)return supabaseClient=null,window.supabaseClient=null,window._supabase=null,null;try{return supabaseClient=window.supabase.createClient(a,n),window.supabaseClient=supabaseClient,window._supabase=supabaseClient,console.log("⚡ [Supabase] Đã kết nối cơ sở dữ liệu Cloud thành công:",a),supabaseClient}catch(e){return console.warn("⚠️ [Supabase] Lỗi khởi tạo client:",e.message),supabaseClient=null,window.supabaseClient=null,window._supabase=null,null}}function getDeviceFingerprint(){try{const e=`${window.screen?.width||0}x${window.screen?.height||0}x${window.screen?.colorDepth||0}`,t=Intl.DateTimeFormat().resolvedOptions().timeZone||"",a=navigator.language||navigator.userLanguage||"",n=navigator.hardwareConcurrency||"",s=navigator.platform||"",o=`${navigator.userAgent||""}|${e}|${t}|${a}|${n}|${s}`;let i=5381;for(let e=0;e<o.length;e++)i=(i<<5)+i+o.charCodeAt(e),i&=i;return"fp_"+Math.abs(i).toString(36)}catch(e){return"fp_fallback_"+Math.random().toString(36).substring(2,10)}}function getOrCreateDeviceId(){try{let e=localStorage.getItem("olion_device_id");if(!e){const t=document.cookie.match(/(^|;)\s*olion_device_id\s*=\s*([^;]+)/);t&&(e=t[2])}if(!e){const t=getDeviceFingerprint(),a=Math.random().toString(36).substring(2,9);e=`dev_${t}_${Date.now().toString(36)}_${a}`}localStorage.setItem("olion_device_id",e);const t=new Date(Date.now()+31536e6).toUTCString();return document.cookie=`olion_device_id=${e}; expires=${t}; path=/; SameSite=Lax`,e}catch(e){return"dev_anon_"+Date.now()}}async function canUserSpinToday(e){const t=getOrCreateDeviceId(),a=localStorage.getItem("olion_last_spin_time");if(a){const e=Math.floor((Date.now()-parseInt(a,10))/1e3);if(e<86400){const t=86400-e,a=Math.floor(t/3600);return{can_spin:!1,wait_seconds:t,message:`Bạn đã sử dụng hết lượt quay hôm nay. Hãy quay lại vào ngày mai nhé! (Còn ${a>0?a+"h ":""}${Math.floor(t%3600/60)} phút)`}}}const n=supabaseClient||initSupabase();if(n)try{const{data:a,error:s}=await n.rpc("check_can_spin",{p_device_id:t,p_phone:e||""});if(!s&&a&&!a.can_spin)return{can_spin:!1,wait_seconds:a.wait_seconds||86400,message:a.message||"Bạn đã sử dụng hết lượt quay hôm nay. Hãy quay lại vào ngày mai nhé!"}}catch(e){console.warn("⚠️ [Supabase RPC] Lỗi check_can_spin, fallback local:",e.message)}return{can_spin:!0,wait_seconds:0,message:"Được phép quay thưởng!"}}async function canUserSubmitFeedback(e){const t=getOrCreateDeviceId(),a=localStorage.getItem("olion_last_feedback_time");if(a){const e=Math.floor((Date.now()-parseInt(a,10))/1e3);if(e<300){const t=300-e,a=Math.floor(t/60);return{can_submit:!1,wait_seconds:t,message:`Bạn vừa gửi đánh giá xong. Vui lòng đợi thêm ${a>0?a+" phút ":""}${t%60}s trước khi gửi tiếp nhé!`}}}const n=supabaseClient||initSupabase();if(n)try{const{data:a,error:s}=await n.rpc("check_can_feedback",{p_device_id:t,p_contact:e||""});if(!s&&a&&!a.can_submit)return{can_submit:!1,wait_seconds:a.wait_seconds||300,message:a.message||"Bạn thao tác quá nhanh! Vui lòng đợi thêm một chút."}}catch(e){console.warn("⚠️ [Supabase RPC] Lỗi check_can_feedback, fallback local:",e.message)}return{can_submit:!0,wait_seconds:0,message:"Được phép gửi góp ý!"}}async function executeReCaptcha(e="submit_feedback"){if("undefined"!=typeof window&&window.RECAPTCHA_SITE_KEY&&"YOUR_RECAPTCHA_SITE_KEY"!==window.RECAPTCHA_SITE_KEY)try{if(window.grecaptcha||await new Promise(e=>{const t=document.createElement("script");t.src=`https://www.google.com/recaptcha/api.js?render=${window.RECAPTCHA_SITE_KEY}`,t.async=!0,t.onload=()=>e(!0),t.onerror=()=>e(!1),document.head.appendChild(t)}),window.grecaptcha)return await new Promise(t=>{window.grecaptcha.ready(async()=>{try{const a=await window.grecaptcha.execute(window.RECAPTCHA_SITE_KEY,{action:e});t(a)}catch(e){console.warn("⚠️ [reCAPTCHA] Lỗi token:",e.message),t(null)}})})}catch(e){return null}return null}async function testSupabaseConnection(e,t){if(!window.supabase)return{success:!1,message:"Thư viện Supabase JS chưa được tải!"};if(!e||!t)return{success:!1,message:"Vui lòng điền đầy đủ URL và Anon Key!"};try{const a=window.supabase.createClient(e,t),{data:n,error:s}=await a.from("feedbacks").select("count",{count:"exact",head:!0});return s?{success:!1,message:"Lỗi Supabase: "+(s.message||s.details||"Không thể truy vấn bảng")}:{success:!0,message:"Kết nối Supabase Cloud thành công!"}}catch(e){return{success:!1,message:"Không thể kết nối: "+e.message}}}window.initSupabase=initSupabase,"undefined"!=typeof window&&initSupabase();const DEFAULT_MENU_ITEMS=[{id:1,name:"ESPRESSO",price:3e4,category:"Cà phê",image_url:"assets/menu/espresso.webp",badge:"",description:"Nóng / Đá. Cà phê nguyên chất đậm đà.",is_available:!0},{id:2,name:"ESPRESSO SỮA",price:35e3,category:"Cà phê",image_url:"assets/menu/espresso_sua.webp",badge:"BEST",description:"Nóng / Đá. Sự kết hợp hoàn hảo giữa espresso và sữa đặc.",is_available:!0},{id:3,name:"BẠC XỈU",price:35e3,category:"Cà phê",image_url:"assets/menu/bac_xiu.webp",badge:"HOT",description:"Nhiều sữa ít cà phê, béo ngậy ngọt ngào.",is_available:!0},{id:4,name:"LATTE HẠNH NHÂN",price:4e4,category:"Cà phê",image_url:"assets/menu/latte_hanh_nhan.webp",badge:"",description:"Nóng / Đá. Vị bùi béo của hạnh nhân hòa quyện espresso.",is_available:!0},{id:5,name:"CARAMEL LATTE",price:4e4,category:"Cà phê",image_url:"assets/menu/caramel_latte.webp",badge:"",description:"Latte ngọt ngào với lớp sốt caramel thơm lừng.",is_available:!0},{id:6,name:"AMERICANO",price:3e4,category:"Cà phê",image_url:"assets/menu/americano.webp",badge:"",description:"Nóng / Đá. Espresso pha loãng thanh tao.",is_available:!0},{id:7,name:"CÀ PHÊ MUỐI",price:4e4,category:"Cà phê",image_url:"assets/menu/ca_phe_muoi.webp",badge:"SIGNATURE",description:"Đậm đà cà phê kết hợp lớp kem muối mặn béo.",is_available:!0},{id:8,name:"CÀ PHÊ BẠC HÀ",price:4e4,category:"Cà phê",image_url:"assets/menu/ca_phe_bac_ha.webp",badge:"",description:"Sự the mát sảng khoái của bạc hà và cà phê.",is_available:!0},{id:9,name:"ESPRESSO OATSIDE",price:4e4,category:"Cà phê",image_url:"assets/menu/ca_phe_sua_oatside.webp",badge:"NEW",description:"Nóng / Đá. Sữa yến mạch Oatside kết hợp espresso.",is_available:!0},{id:10,name:"CACAO LATTE",price:35e3,category:"Cacao",image_url:"assets/menu/cacao_latte.webp",badge:"BEST",description:"Nóng / Đá. Cacao nguyên chất béo thơm.",is_available:!0},{id:11,name:"CACAO KEM MUỐI",price:4e4,category:"Cacao",image_url:"assets/menu/cacao_kem_muoi.webp",badge:"HOT",description:"Cacao đậm đà hòa quyện lớp kem muối béo ngậy.",is_available:!0},{id:12,name:"CACAO BẠC HÀ",price:4e4,category:"Cacao",image_url:"assets/menu/cacao_bac_ha.webp",badge:"",description:"Hương bạc hà the mát sảng khoái quyện cùng vị ngọt đắng cacao.",is_available:!0},{id:13,name:"TRÀ VẢI HOA HỒNG",price:4e4,category:"Trà trái cây",image_url:"assets/menu/tra_vai_hoa_hong.webp",badge:"BEST",description:"Vải ngọt mọng nước kết hợp hương hoa hồng thanh tao dịu nhẹ.",is_available:!0},{id:14,name:"TRÀ BƯỞI HỒNG CHANH VÀNG",price:4e4,category:"Trà trái cây",image_url:"assets/menu/tra_buoi_hong_chanh_vang.webp",badge:"",description:"Bưởi hồng mọng nước hòa cùng chanh vàng thơm mát.",is_available:!0},{id:15,name:"TRÀ CHANH DÂY NHIỆT ĐỚI",price:4e4,category:"Trà trái cây",image_url:"assets/menu/tra_chanh_day_nhiet_doi.webp",badge:"HOT",description:"Chua ngọt bùng nổ, tươi mát sảng khoái ngày hè.",is_available:!0},{id:16,name:"TRÀ XOÀI CHANH DÂY",price:4e4,category:"Trà trái cây",image_url:"assets/menu/tra_xoai_chanh_day.webp",badge:"",description:"Xoài chín ngọt thanh quyện cùng chanh dây đậm đà.",is_available:!0},{id:17,name:"LỤC TRÀ NHÃN",price:4e4,category:"Trà trái cây",image_url:"assets/menu/luc_tra_nhan.webp",badge:"",description:"Nhãn giòn ngọt ngào kết hợp nền lục trà lài thanh tao.",is_available:!0},{id:18,name:"LỤC TRÀ TRÂN CHÂU TRẮNG",price:35e3,category:"Trà trái cây",image_url:"assets/menu/luc_tra_tran_chau_trang.webp",badge:"",description:"Lục trà lài thanh mát cùng trân châu trắng giòn sần sật.",is_available:!0},{id:19,name:"NƯỚC ÉP CAM",price:3e4,category:"Nước ép",image_url:"assets/menu/nuoc_ep_cam.webp",badge:"BEST",description:"Cam sành tươi vắt nguyên chất, dồi dào Vitamin C.",is_available:!0},{id:20,name:"NƯỚC ÉP CHANH DÂY",price:3e4,category:"Nước ép",image_url:"assets/menu/nuoc_ep_chanh_day.webp",badge:"HOT",description:"Chanh dây tươi thơm nồng, chua ngọt giải nhiệt cực đã.",is_available:!0},{id:21,name:"MATCHA LATTE",price:4e4,category:"Trà sữa & Matcha",image_url:"assets/menu/matcha_latte.webp",badge:"SIGNATURE",description:"Nóng / Đá. Matcha Nhật Bản nguyên chất thơm lừng.",is_available:!0},{id:22,name:"MATCHA CARAMEL",price:45e3,category:"Trà sữa & Matcha",image_url:"assets/menu/matcha_caramel.webp",badge:"",description:"Matcha thơm đậm hòa quyện cùng sốt caramel béo ngậy.",is_available:!0},{id:23,name:"MATCHA BẠC HÀ",price:45e3,category:"Trà sữa & Matcha",image_url:"assets/menu/matcha_bac_ha.webp",badge:"",description:"Sự kết hợp độc đáo giữa vị thanh của matcha và the mát của bạc hà.",is_available:!0},{id:24,name:"MATCHA KEM MUỐI",price:45e3,category:"Trà sữa & Matcha",image_url:"assets/menu/matcha_kem_muoi.webp",badge:"",description:"Lớp kem muối béo ngậy mằn mặn phủ trên nền matcha đậm đà.",is_available:!0},{id:25,name:"MATCHA QUẾ HOA",price:45e3,category:"Trà sữa & Matcha",image_url:"assets/menu/matcha_que_hoa.webp",badge:"",description:"Matcha cao cấp ướp hương hoa quế tự nhiên thanh tao.",is_available:!0},{id:26,name:"MATCHA COLD WHISK",price:45e3,category:"Trà sữa & Matcha",image_url:"assets/menu/matcha_cold_whisk.webp",badge:"",description:"Nóng / Đá. Đánh bọt matcha lạnh thủ công truyền thống.",is_available:!0},{id:27,name:"MATCHA DỪA",price:45e3,category:"Trà sữa & Matcha",image_url:"assets/menu/matcha_dua.webp",badge:"",description:"Vị thơm bùi của nước cốt dừa tươi quyện cùng bột matcha thượng hạng.",is_available:!0},{id:28,name:"MATCHA DÂU",price:45e3,category:"Trà sữa & Matcha",image_url:"assets/menu/matcha_dau.webp",badge:"HOT",description:"Sự hòa quyện tuyệt hảo giữa matcha thơm đắng và mứt dâu tây.",is_available:!0},{id:29,name:"MATCHA ESPRESSO LATTE",price:45e3,category:"Trà sữa & Matcha",image_url:"assets/menu/matcha_oatside.webp",badge:"",description:"Kết hợp hoàn hảo giữa Matcha và Espresso Latte.",is_available:!0},{id:30,name:"YAGOUT ĐÀO CHANH DÂY",price:45e3,category:"Sữa chua",image_url:"assets/menu/yagout_dao_chanh_day.webp",badge:"",description:"Đào mọng nước thơm ngọt hòa cùng vị chua dịu nhẹ của chanh dây.",is_available:!0},{id:31,name:"YAGOUT VIỆT QUẤT",price:45e3,category:"Sữa chua",image_url:"assets/menu/yagout_viet_quat.webp",badge:"HOT",description:"Việt quất bổ dưỡng thơm lừng quyện cùng sữa chua tươi mát.",is_available:!0},{id:32,name:"YAGOUT XOÀI CHANH DÂY",price:45e3,category:"Sữa chua",image_url:"assets/menu/yagout_xoai_chanh_day.webp",badge:"",description:"Xoài chín thơm ngọt hòa quyện cùng chanh dây nhiệt đới.",is_available:!0},{id:33,name:"YAGOUT DÂU",price:45e3,category:"Sữa chua",image_url:"assets/menu/yagout_dau.webp",badge:"BEST",description:"Sữa chua sánh mịn kết hợp mứt dâu tây chua ngọt thanh mát.",is_available:!0},{id:34,name:"TRÂN CHÂU TRẮNG",price:5e3,category:"Topping",image_url:"assets/menu/tran_chau_trang.webp",badge:"",description:"Trân châu trắng ngọc trai giòn dai thơm ngon.",is_available:!0},{id:35,name:"TRÂN CHÂU Ô LONG",price:5e3,category:"Topping",image_url:"assets/menu/tran_chau_o_long.webp",badge:"",description:"Đậm hương trà ô long rang mộc, mềm dẻo.",is_available:!0},{id:36,name:"THẠCH SƯƠNG SÁO",price:5e3,category:"Topping",image_url:"assets/menu/thach_suong_sao.webp",badge:"",description:"Thạch sương sáo mềm mượt, thanh mát giải nhiệt tự nhiên.",is_available:!0},{id:37,name:"THẠCH QUẾ HOA",price:5e3,category:"Topping",image_url:"assets/menu/thach_que_hoa.webp",badge:"",description:"Thơm thanh hương hoa quế tự nhiên.",is_available:!0},{id:38,name:"THẠCH VẢI HOA HỒNG",price:5e3,category:"Topping",image_url:"assets/menu/thach_vai_hoa_hong.webp",badge:"",description:"Thạch giòn dai thơm ngát hương hoa hồng và vị vải ngọt thanh.",is_available:!0},{id:39,name:"THẠCH CÀ PHÊ",price:5e3,category:"Topping",image_url:"assets/menu/thach_ca_phe.webp",badge:"",description:"Thạch cà phê nấu thủ công giòn thơm đậm vị.",is_available:!0}];async function fetchMenuItemsFromCloud(){const e=supabaseClient||initSupabase();if(e)try{const{data:t,error:a}=await e.from("menu_items").select("*").order("id",{ascending:!0});if(!a&&t&&t.length>=30)return localStorage.setItem("olion_menu_items",JSON.stringify(t)),{source:"supabase",data:t};if(!a&&t&&t.length>0&&t.length<30)return console.warn("⚠️ [Supabase] Detected outdated dummy test items in database (< 30 items). Using official 39 DEFAULT_MENU_ITEMS."),localStorage.removeItem("olion_menu_items"),{source:"local_default",data:DEFAULT_MENU_ITEMS}}catch(e){console.warn("⚠️ [Supabase] Lỗi fetch menu_items:",e.message)}try{let e=JSON.parse(localStorage.getItem("olion_menu_items"));return(!e||!Array.isArray(e)||e.length<30||e.some(e=>"Trà Đào Cam Sả Tươi"===e.name||"Bánh Croissant Bơ Pháp"===e.name))&&(e=DEFAULT_MENU_ITEMS,localStorage.setItem("olion_menu_items",JSON.stringify(e))),{source:"local",data:e}}catch(e){return{source:"local",data:DEFAULT_MENU_ITEMS}}}async function saveMenuItemToCloud(e){const t=supabaseClient||initSupabase();try{let t=JSON.parse(localStorage.getItem("olion_menu_items")||"[]");if(e.id){const a=t.findIndex(t=>t.id===e.id);-1!==a?t[a]={...t[a],...e,updated_at:(new Date).toISOString()}:t.unshift(e)}else{const a={...e,id:Date.now(),created_at:(new Date).toISOString()};t.unshift(a)}localStorage.setItem("olion_menu_items",JSON.stringify(t))}catch(e){}if(t)try{const a={name:e.name,price:Number(e.price)||0,category:e.category||"Cà phê",image_url:e.image_url||"assets/news/news-1-drinks.webp",badge:e.badge||"",description:e.description||"",is_available:!1!==e.is_available,updated_at:(new Date).toISOString()};if(e.id&&"number"==typeof e.id&&e.id<1e11){const{data:n,error:s}=await t.from("menu_items").update(a).eq("id",e.id).select();if(s)throw s;return{success:!0,source:"supabase",data:n[0]}}{const{data:e,error:n}=await t.from("menu_items").insert([a]).select();if(n)throw n;return{success:!0,source:"supabase",data:e[0]}}}catch(e){return console.warn("⚠️ [Supabase] Lỗi lưu menu item:",e.message),{success:!0,source:"local_fallback",error:e.message}}return{success:!0,source:"local_only"}}async function deleteMenuItemFromCloud(e){const t=supabaseClient||initSupabase();try{let t=JSON.parse(localStorage.getItem("olion_menu_items")||"[]");t=t.filter(t=>t.id!==e),localStorage.setItem("olion_menu_items",JSON.stringify(t))}catch(e){}if(t)try{const{error:a}=await t.from("menu_items").delete().eq("id",e);if(a)throw a;return{success:!0,source:"supabase"}}catch(e){return{success:!1,error:e.message}}return{success:!0,source:"local"}}async function toggleMenuItemAvailabilityInCloud(e,t){const a=supabaseClient||initSupabase();try{let a=JSON.parse(localStorage.getItem("olion_menu_items")||"[]");a=a.map(a=>String(a.id)===String(e)?{...a,is_available:t}:a),localStorage.setItem("olion_menu_items",JSON.stringify(a))}catch(e){}if(a)try{const{error:n}=await a.from("menu_items").update({is_available:t,updated_at:(new Date).toISOString()}).eq("id",e);if(n)throw n;return{success:!0,source:"supabase"}}catch(e){return{success:!1,error:e.message}}return{success:!0,source:"local"}}const DEFAULT_CUSTOMERS=[
  {id:1,name:"Nguyễn Minh Anh",contact:"0908123456",member_code:"OLION-3456",stamps_count:5,total_stamps:15,free_drinks_earned:1,points:150,tier:"Vàng",source:"Quầy thu ngân",notes:"Khách ruột uống Cà phê Muối mỗi sáng",date:"20/09/2026"},
  {id:2,name:"Trần Hoàng Nam",contact:"0912334455",member_code:"OLION-4455",stamps_count:8,total_stamps:8,free_drinks_earned:0,points:80,tier:"Bạc",source:"Minigame Vòng Quay",notes:"Đủ 8 tem! Sẵn sàng đổi 1 ly miễn phí",date:"19/09/2026"},
  {id:3,name:"Lê Thanh Trúc",contact:"0912345678",member_code:"OLION-5678",stamps_count:3,total_stamps:22,free_drinks_earned:2,points:220,tier:"Kim Cương",source:"Website Check-in",notes:"VIP ghé quán làm việc cuối tuần",date:"18/09/2026"},
  {id:4,name:"Phạm Quốc Bảo",contact:"0978999888",member_code:"OLION-9888",stamps_count:1,total_stamps:1,free_drinks_earned:0,points:10,tier:"Thành viên",source:"Popup Chào Mừng",notes:"Khách mới gia nhập nhận 1 tem",date:"17/09/2026"}
];

function generateMemberCode(phone){
  const clean=(phone||"").replace(/[^0-9]/g,"");
  if(clean.length>=4){
    return "OLION-"+clean.slice(-4);
  }
  return "OLION-"+Math.floor(1000+Math.random()*9000);
}

function calculateCustomerTier(points,totalStamps=0){
  const s=Math.max(Number(totalStamps)||0,Math.floor((Number(points)||0)/10));
  const p=Number(points)||0;
  if(s>=20||p>=200)return"Kim Cương";
  if(s>=10||p>=100)return"Vàng";
  if(s>=5||p>=50)return"Bạc";
  return"Thành viên";
}

async function fetchCustomersFromCloud(){
  const client=supabaseClient||initSupabase();
  if(client)try{
    const{data,error}=await client.from("customers").select("*").order("created_at",{ascending:false});
    if(!error&&data&&data.length>0){
      const mapped=data.map(c=>({
        id:c.id,
        name:c.name||"Khách hàng",
        contact:c.contact||"",
        member_code:c.member_code||generateMemberCode(c.contact),
        stamps_count:Number(c.stamps_count!=null?c.stamps_count:Math.min(8,Math.floor((c.points||0)/10))),
        total_stamps:Number(c.total_stamps!=null?c.total_stamps:(c.stamps_count||1)),
        free_drinks_earned:Number(c.free_drinks_earned||0),
        points:Number(c.points||0),
        tier:c.tier||calculateCustomerTier(c.points,c.total_stamps),
        source:c.source||"Website",
        notes:c.notes||"",
        date:c.created_at?new Date(c.created_at).toLocaleDateString("vi-VN"):"Gần đây",
        created_at:c.created_at
      }));
      localStorage.setItem("olion_customers",JSON.stringify(mapped));
      return{source:"supabase",data:mapped};
    }
  }catch(e){
    console.warn("⚠️ [Supabase Admin] Lỗi tải customers:",e.message);
  }
  try{
    let local=JSON.parse(localStorage.getItem("olion_customers"));
    if(!local||!Array.isArray(local)||local.length===0){
      local=DEFAULT_CUSTOMERS;
      localStorage.setItem("olion_customers",JSON.stringify(local));
    }
    return{source:"local",data:local};
  }catch(e){
    return{source:"local",data:DEFAULT_CUSTOMERS};
  }
}

async function saveCustomerToCloud(customer){
  const client=supabaseClient||initSupabase();
  const phone=(customer.contact||customer.phone_number||"").replace(/[^0-9]/g,"").trim();
  const name=(customer.name||customer.customer_name||"Khách hàng Olion").trim();
  const memberCode=customer.member_code||generateMemberCode(phone);
  const stampsCount=Math.max(0,Math.min(8,Number(customer.stamps_count!=null?customer.stamps_count:1)));
  const totalStamps=Math.max(stampsCount,Number(customer.total_stamps||stampsCount));
  const freeDrinks=Math.max(0,Number(customer.free_drinks_earned||0));
  const points=Number(customer.points!=null?customer.points:(totalStamps*10));
  const tier=customer.tier||calculateCustomerTier(points,totalStamps);
  const source=customer.source||"Đăng ký Web";
  const notes=customer.notes||"";

  const updatedObj={
    ...customer,
    name,
    contact:phone,
    member_code:memberCode,
    stamps_count:stampsCount,
    total_stamps:totalStamps,
    free_drinks_earned:freeDrinks,
    points,
    tier,
    source,
    notes,
    date:customer.date||new Date().toLocaleDateString("vi-VN"),
    updated_at:new Date().toISOString()
  };

  // 1. Cập nhật LocalStorage
  try{
    let localCusts=JSON.parse(localStorage.getItem("olion_customers")||"[]");
    const idx=localCusts.findIndex(c=>c.contact===phone||String(c.id)===String(customer.id));
    if(idx!==-1){
      localCusts[idx]={...localCusts[idx],...updatedObj};
      updatedObj.id=localCusts[idx].id;
    }else{
      updatedObj.id=updatedObj.id||("cust_"+Date.now());
      localCusts.unshift(updatedObj);
    }
    localStorage.setItem("olion_customers",JSON.stringify(localCusts));

    // Đồng bộ vào olion_loyalty_members
    let localLoyalty=JSON.parse(localStorage.getItem("olion_loyalty_members")||"[]");
    const lIdx=localLoyalty.findIndex(l=>l.phone_number===phone);
    const loyaltyItem={id:updatedObj.id,phone_number:phone,customer_name:name,points,stamps_count:stampsCount,member_code:memberCode,total_visits:totalStamps};
    if(lIdx!==-1){
      localLoyalty[lIdx]={...localLoyalty[lIdx],...loyaltyItem};
    }else{
      localLoyalty.unshift(loyaltyItem);
    }
    localStorage.setItem("olion_loyalty_members",JSON.stringify(localLoyalty));
  }catch(e){}

  // 2. Đồng bộ lên Supabase Cloud
  if(client){
    try{
      const payload={
        name,
        contact:phone,
        member_code:memberCode,
        stamps_count:stampsCount,
        total_stamps:totalStamps,
        free_drinks_earned:freeDrinks,
        points,
        tier,
        source,
        notes,
        updated_at:new Date().toISOString()
      };
      const{data,error}=await client.from("customers").upsert([payload],{onConflict:"contact"}).select();
      if(!error&&data&&data.length>0){
        // Đồng thời cập nhật bảng loyalty_members để đảm bảo tính tương thích
        try{
          await client.from("loyalty_members").upsert([{
            phone_number:phone,
            customer_name:name,
            points
          }],{onConflict:"phone_number"});
        }catch(e){}
        return{success:true,source:"supabase",data:data[0]};
      }
    }catch(e){
      console.warn("⚠️ [Supabase] Lỗi lưu customer lên Cloud:",e.message);
    }
  }
  return{success:true,source:"local_only",data:updatedObj};
}

async function addCustomerStampInCloud(customerId,phone,stampDelta=1,reason="Cộng tem mua nước"){
  const client=supabaseClient||initSupabase();
  const clean=(phone||"").replace(/[^0-9]/g,"").trim();
  const delta=Number(stampDelta)||1;
  let updatedMember=null;

  try{
    let list=JSON.parse(localStorage.getItem("olion_customers")||"[]");
    let cust=list.find(c=>c.contact===clean||c.id===customerId);
    if(cust){
      let currentStamps=Number(cust.stamps_count!=null?cust.stamps_count:0);
      let newStamps=Math.max(0,Math.min(8,currentStamps+delta));
      cust.stamps_count=newStamps;
      if(delta>0){
        cust.total_stamps=(Number(cust.total_stamps)||currentStamps)+delta;
        cust.points=(Number(cust.points)||0)+(delta*10);
      }
      cust.tier=calculateCustomerTier(cust.points,cust.total_stamps);
      cust.updated_at=new Date().toISOString();
      updatedMember=cust;
      localStorage.setItem("olion_customers",JSON.stringify(list));
    }
  }catch(e){}

  if(client&&clean){
    try{
      const{data:existing}=await client.from("customers").select("*").eq("contact",clean).maybeSingle();
      if(existing){
        const curStamps=Number(existing.stamps_count!=null?existing.stamps_count:0);
        const newStamps=Math.max(0,Math.min(8,curStamps+delta));
        const totalStamps=delta>0?((Number(existing.total_stamps)||curStamps)+delta):(Number(existing.total_stamps)||curStamps);
        const newPoints=(Number(existing.points)||0)+(delta*10);
        const newTier=calculateCustomerTier(newPoints,totalStamps);
        const{data,error}=await client.from("customers").update({
          stamps_count:newStamps,
          total_stamps:totalStamps,
          points:newPoints,
          tier:newTier,
          updated_at:new Date().toISOString()
        }).eq("id",existing.id).select().single();
        if(!error&&data){
          updatedMember=data;
        }
      }
    }catch(e){
      console.warn("⚠️ [Supabase] Lỗi cập nhật tem:",e.message);
    }
  }

  return{success:true,member:updatedMember,rewardReady:updatedMember&&(updatedMember.stamps_count>=8)};
}

async function redeemCustomerDrinkInCloud(customerId,phone,reason="Đổi 1 ly nước miễn phí (8 tem)"){
  const client=supabaseClient||initSupabase();
  const clean=(phone||"").replace(/[^0-9]/g,"").trim();
  let updatedMember=null;

  try{
    let list=JSON.parse(localStorage.getItem("olion_customers")||"[]");
    let cust=list.find(c=>c.contact===clean||c.id===customerId);
    if(cust){
      if((cust.stamps_count||0)<8){
        return{success:false,error:"Khách hàng chưa đủ 8 tem để đổi ly miễn phí!"};
      }
      cust.stamps_count=Math.max(0,(cust.stamps_count||0)-8);
      cust.free_drinks_earned=(Number(cust.free_drinks_earned)||0)+1;
      cust.notes=(cust.notes||"")+" | Đổi 1 ly free lúc "+new Date().toLocaleDateString("vi-VN");
      cust.updated_at=new Date().toISOString();
      updatedMember=cust;
      localStorage.setItem("olion_customers",JSON.stringify(list));
    }
  }catch(e){}

  if(client&&clean){
    try{
      const{data:existing}=await client.from("customers").select("*").eq("contact",clean).maybeSingle();
      if(existing){
        if((existing.stamps_count||0)<8){
          return{success:false,error:"Khách hàng chưa đủ 8 tem để đổi ly miễn phí!"};
        }
        const newStamps=Math.max(0,(existing.stamps_count||0)-8);
        const newFree=(Number(existing.free_drinks_earned)||0)+1;
        const notes=(existing.notes||"")+" | Đổi 1 ly free lúc "+new Date().toLocaleDateString("vi-VN");
        const{data,error}=await client.from("customers").update({
          stamps_count:newStamps,
          free_drinks_earned:newFree,
          notes,
          updated_at:new Date().toISOString()
        }).eq("id",existing.id).select().single();
        if(!error&&data){
          updatedMember=data;
        }
      }
    }catch(e){
      console.warn("⚠️ [Supabase] Lỗi đổi ly miễn phí:",e.message);
    }
  }

  return{success:true,member:updatedMember};
}

async function adjustCustomerPointsInCloud(e,t,a,n,s="earn"){
  const o=supabaseClient||initSupabase(),i=Number(a)||0;let r=0,c=null;
  try{
    let a=JSON.parse(localStorage.getItem("olion_customers")||"[]"),o=a.find(a=>a.id===e||a.contact===t);
    if(o){
      o.points=Math.max(0,(o.points||0)+i);
      o.tier=calculateCustomerTier(o.points,o.total_stamps);
      r=o.points;
      c=o;
      localStorage.setItem("olion_customers",JSON.stringify(a));
    }
    let u=JSON.parse(localStorage.getItem("olion_point_transactions")||"[]");
    u.unshift({id:Date.now(),customer_id:e,customer_contact:t,action_type:s,points_change:i,balance_after:r,reason:n||(i>0?"Tích điểm mua nước":"Đổi thưởng voucher"),created_at:new Date().toISOString()});
    localStorage.setItem("olion_point_transactions",JSON.stringify(u));
  }catch(e){}
  if(o)try{
    const{data:e,error:a}=await o.from("customers").select("*").eq("contact",t).maybeSingle();
    if(!a&&e){
      r=Math.max(0,(e.points||0)+i);
      const a=calculateCustomerTier(r,e.total_stamps);
      await o.from("customers").update({points:r,tier:a,updated_at:new Date().toISOString()}).eq("id",e.id);
      await o.from("point_transactions").insert([{customer_id:e.id,customer_contact:t,action_type:s,points_change:i,balance_after:r,reason:n||(i>0?"Tích điểm hóa đơn":"Đổi ưu đãi")}]);
      return{success:true,source:"supabase",newBalance:r,tier:a};
    }
  }catch(e){
    return console.warn("⚠️ [Supabase] Lỗi cập nhật điểm:",e.message),{success:true,source:"local_fallback",newBalance:r};
  }
  return{success:true,source:"local_only",newBalance:r};
}

async function fetchCustomerPointHistoryFromCloud(e,t){
  const a=supabaseClient||initSupabase();
  if(a&&t)try{
    const{data:e,error:n}=await a.from("point_transactions").select("*").eq("customer_contact",t).order("created_at",{ascending:false}).limit(20);
    if(!n&&e)return{source:"supabase",data:e};
  }catch(e){}
  try{
    const a=JSON.parse(localStorage.getItem("olion_point_transactions")||"[]");
    return{source:"local",data:a.filter(a=>a.customer_contact===t||a.customer_id===e)};
  }catch(e){
    return{source:"local",data:[]};
  }
}

async function deleteCustomerFromCloud(e){
  const t=supabaseClient||initSupabase();
  try{
    let t=JSON.parse(localStorage.getItem("olion_customers")||"[]");
    t=t.filter(t=>t.id!==e);
    localStorage.setItem("olion_customers",JSON.stringify(t));
  }catch(e){}
  if(t)try{
    const{error:a}=await t.from("customers").delete().eq("id",e);
    if(a)throw a;
    return{success:true,source:"supabase"};
  }catch(e){
    return{success:false,error:e.message};
  }
  return{success:true,source:"local"};
}

async function submitFeedbackToCloud(e){
  const t=supabaseClient||initSupabase(),a=getOrCreateDeviceId();
  try{
    localStorage.setItem("olion_last_feedback_time",Date.now().toString());
    const n=JSON.parse(localStorage.getItem("olion_feedbacks")||"[]");
    n.unshift({...e,id:Date.now(),device_id:a,localOnly:!t});
    localStorage.setItem("olion_feedbacks",JSON.stringify(n));
  }catch(e){}
  if(t)try{
    const{data:n,error:s}=await t.from("feedbacks").insert([{name:e.name||"Khách ghé quán",contact:e.contact||"",rating:e.rating||5,content:e.content||"",image_url:e.imageDataUrl||e.image_url||null,device_id:a,approved:true}]).select();
    if(s)throw s;
    return{success:true,source:"supabase",data:n};
  }catch(e){
    return{success:true,source:"local_fallback",error:e.message};
  }
  return{success:true,source:"local_only"};
}

async function fetchApprovedFeedbacksFromCloud(){
  const e=supabaseClient||initSupabase();
  if(e)try{
    const{data:t,error:a}=await e.from("feedbacks").select("*").eq("approved",true).order("created_at",{ascending:false}).limit(6);
    if(!a&&t&&t.length>0)return t.map(e=>({id:e.id,name:e.name,contact:e.contact,rating:e.rating,content:e.content,imageDataUrl:e.image_url,date:e.created_at?new Date(e.created_at).toLocaleDateString("vi-VN"):"Gần đây",approved:e.approved}));
  }catch(e){}
  try{
    return JSON.parse(localStorage.getItem("olion_feedbacks")||"[]").filter(e=>false!==e.approved);
  }catch(e){
    return[];
  }
}

async function fetchAdminFeedbacksFromCloud(){
  const e=supabaseClient||initSupabase();
  if(e)try{
    const{data:t,error:a}=await e.from("feedbacks").select("*").order("created_at",{ascending:false});
    if(!a&&t)return{source:"supabase",data:t.map(e=>({id:e.id,name:e.name,contact:e.contact,rating:e.rating,content:e.content,imageDataUrl:e.image_url,date:e.created_at?new Date(e.created_at).toLocaleString("vi-VN"):"Gần đây",approved:e.approved,created_at:e.created_at}))};
  }catch(e){}
  return{source:"local",data:JSON.parse(localStorage.getItem("olion_feedbacks")||"[]")};
}

async function toggleFeedbackApprovalInCloud(e,t){
  const a=supabaseClient||initSupabase();
  try{
    let a=JSON.parse(localStorage.getItem("olion_feedbacks")||"[]");
    a=a.map(a=>String(a.id)===String(e)?{...a,approved:t}:a);
    localStorage.setItem("olion_feedbacks",JSON.stringify(a));
  }catch(e){}
  if(a)try{
    const{error:n}=await a.from("feedbacks").update({approved:t}).eq("id",e);
    if(n)throw n;
    return{success:true,source:"supabase"};
  }catch(e){
    return{success:false,error:e.message};
  }
  return{success:true,source:"local"};
}

async function deleteFeedbackFromCloud(e){
  const t=supabaseClient||initSupabase();
  try{
    let t=JSON.parse(localStorage.getItem("olion_feedbacks")||"[]");
    t=t.filter(t=>t.id!==e);
    localStorage.setItem("olion_feedbacks",JSON.stringify(t));
  }catch(e){}
  if(t)try{
    const{error:a}=await t.from("feedbacks").delete().eq("id",e);
    if(a)throw a;
    return{success:true,source:"supabase"};
  }catch(e){
    return{success:false,error:e.message};
  }
  return{success:true,source:"local"};
}

async function recordLuckySpinToCloud(e){
  const t=supabaseClient||initSupabase(),a=getOrCreateDeviceId();
  try{
    localStorage.setItem("olion_last_spin_time",Date.now().toString());
    const t=JSON.parse(localStorage.getItem("olion_customers")||"[]");
    t.unshift({id:Date.now(),name:e.customer_name,contact:e.customer_phone,member_code:generateMemberCode(e.customer_phone),stamps_count:1,total_stamps:1,points:10,tier:"Thành viên",source:`Minigame: ${e.prize_name} (Mã: ${e.promo_code})`,date:new Date().toLocaleDateString("vi-VN")});
    localStorage.setItem("olion_customers",JSON.stringify(t));
  }catch(e){}
  if(t)try{
    const{data:n,error:s}=await t.from("lucky_spins").insert([{customer_name:e.customer_name||"Khách quay minigame",customer_phone:e.customer_phone,prize_name:e.prize_name,promo_code:e.promo_code,device_id:a}]).select("*");
    return!s&&n&&n.length>0?n[0]:(await t.from("customers").upsert([{name:e.customer_name||"Khách quay minigame",contact:e.customer_phone,source:`Minigame: ${e.prize_name} (Mã: ${e.promo_code})`}],{onConflict:"contact"}),{success:true,source:"supabase"});
  }catch(e){
    return{success:true,source:"local_fallback"};
  }
  return{success:true,source:"local_only"};
}

async function fetchLuckySpinsFromCloud(){
  const e=supabaseClient||initSupabase();
  if(e)try{
    const{data:t,error:a}=await e.from("lucky_spins").select("*").order("created_at",{ascending:false}).limit(100);
    if(!a&&t)return{source:"supabase",data:t.map(e=>({id:e.id,name:e.customer_name,contact:e.customer_phone,source:`${e.prize_name} (Mã: ${e.promo_code})`,date:e.created_at?new Date(e.created_at).toLocaleString("vi-VN"):"Gần đây"}))};
  }catch(e){}
  return{source:"local",data:JSON.parse(localStorage.getItem("olion_customers")||"[]").filter(e=>(e.source||"").includes("Minigame"))};
}

const DEFAULT_LOYALTY_MEMBERS=DEFAULT_CUSTOMERS.map(c=>({
  id:c.id,
  phone_number:c.contact,
  customer_name:c.name,
  member_code:c.member_code,
  stamps_count:c.stamps_count,
  total_stamps:c.total_stamps,
  free_drinks_earned:c.free_drinks_earned,
  points:c.points,
  tier:c.tier,
  total_visits:c.total_stamps||5
}));

async function lookupLoyaltyMember(phone){
  const clean=(phone||"").replace(/[^0-9]/g,"").trim();
  if(!clean)return{success:false,error:"Vui lòng nhập số điện thoại hợp lệ (10 số)."};

  const client=supabaseClient||initSupabase();
  if(client){
    try{
      // 1. Kiểm tra bảng customers
      const{data:cust,error:cErr}=await client.from("customers").select("*").eq("contact",clean).maybeSingle();
      if(!cErr&&cust){
        const stamps=Number(cust.stamps_count!=null?cust.stamps_count:Math.min(8,Math.floor((cust.points||0)/10)));
        const totalStamps=Number(cust.total_stamps||stamps||1);
        const freeDrinks=Number(cust.free_drinks_earned||0);
        const pts=Number(cust.points||0);
        return{
          success:true,
          source:"supabase",
          member:{
            id:cust.id,
            name:cust.name||"Khách hàng thân thiết",
            customer_name:cust.name||"Khách hàng thân thiết",
            contact:cust.contact||clean,
            phone_number:cust.contact||clean,
            member_code:cust.member_code||generateMemberCode(clean),
            stamps_count:stamps,
            total_stamps:totalStamps,
            free_drinks_earned:freeDrinks,
            points:pts,
            tier:cust.tier||calculateCustomerTier(pts,totalStamps),
            total_visits:totalStamps,
            source:cust.source||"Website",
            notes:cust.notes||""
          }
        };
      }

      // 2. Kiểm tra bảng loyalty_members nếu có
      const{data:lMember,error:lErr}=await client.from("loyalty_members").select("*").eq("phone_number",clean).maybeSingle();
      if(!lErr&&lMember){
        const pts=Number(lMember.points||0);
        const stamps=Math.min(8,Math.floor(pts/10));
        return{
          success:true,
          source:"supabase_loyalty",
          member:{
            id:lMember.id,
            name:lMember.customer_name||"Khách hàng thân thiết",
            customer_name:lMember.customer_name||"Khách hàng thân thiết",
            contact:clean,
            phone_number:clean,
            member_code:generateMemberCode(clean),
            stamps_count:stamps,
            total_stamps:stamps,
            free_drinks_earned:0,
            points:pts,
            tier:calculateCustomerTier(pts),
            total_visits:Number(lMember.total_visits||1)
          }
        };
      }
    }catch(e){
      console.warn("⚠️ [Supabase] Lỗi tra cứu member:",e.message);
    }
  }

  // 3. Fallback LocalStorage
  try{
    const custs=JSON.parse(localStorage.getItem("olion_customers")||"[]");
    const found=custs.find(c=>c.contact===clean);
    if(found){
      return{
        success:true,
        source:"local",
        member:{
          id:found.id,
          name:found.name||"Khách hàng thân thiết",
          customer_name:found.name||"Khách hàng thân thiết",
          contact:found.contact||clean,
          phone_number:found.contact||clean,
          member_code:found.member_code||generateMemberCode(clean),
          stamps_count:Number(found.stamps_count!=null?found.stamps_count:Math.min(8,Math.floor((found.points||0)/10))),
          total_stamps:Number(found.total_stamps||1),
          free_drinks_earned:Number(found.free_drinks_earned||0),
          points:Number(found.points||0),
          tier:found.tier||calculateCustomerTier(found.points),
          total_visits:Number(found.total_stamps||1)
        }
      };
    }
  }catch(e){}

  return{
    success:false,
    not_found:true,
    phone:clean,
    message:"Chưa tìm thấy thông tin thành viên với số điện thoại này. Bạn có thể đăng ký thẻ thành viên ngay bên dưới!"
  };
}

async function addLoyaltyMemberPoints(phone,pointsDelta,name=""){
  const clean=(phone||"").replace(/[^0-9]/g,"").trim();
  const s=Math.max(1,Number(pointsDelta)||0);
  if(!clean)return{success:false,error:"Số điện thoại không hợp lệ"};
  return adjustCustomerPointsInCloud(null,clean,s,name||"Tích điểm","earn");
}

async function redeemLoyaltyMemberPoints(phone,pointsDelta,reason="Đổi quà"){
  const clean=(phone||"").replace(/[^0-9]/g,"").trim();
  const s=Math.max(1,Number(pointsDelta)||0);
  if(!clean)return{success:false,error:"Số điện thoại không hợp lệ"};
  return adjustCustomerPointsInCloud(null,clean,-s,reason,"redeem");
}

async function fetchLoyaltyMembersFromCloud(){
  return fetchCustomersFromCloud();
}
async function fetchSiteSettingsFromCloud(){const e=supabaseClient||initSupabase();if(!e)return{error:"No client"};try{const{data:t,error:a}=await e.from("site_settings").select("*").eq("id",1).single();return a?{error:a}:{data:t}}catch(e){return{error:e}}}async function updateSiteSettingsToCloud(e){const t=supabaseClient||initSupabase();if(!t)return{error:"No client"};try{const{data:a,error:n}=await t.from("site_settings").update(e).eq("id",1).select();return n?{error:n}:{data:a}}catch(e){return{error:e}}}async function markSpinAsUsed(e){const t=supabaseClient||initSupabase();if(!t)return{error:"No client"};try{const{data:a,error:n}=await t.from("lucky_spins").update({status:"used"}).eq("id",e).select();return n?{error:n}:{data:a}}catch(e){return{error:e}}}async function getSpinDetails(e){const t=supabaseClient||initSupabase();if(!t)return{error:"No client"};try{const{data:a,error:n}=await t.from("lucky_spins").select("*").eq("id",e).single();return n?{error:n}:{data:a}}catch(e){return{error:e}}}async function saveBookingToStorage(e){const t="bk_"+Date.now()+"_"+Math.random().toString(36).substring(2,7),a={id:e.id||t,customer_name:(e.customer_name||e.name||"Khách hàng").trim(),phone:(e.phone||"").trim(),booking_type:e.booking_type||"table",guests_count:parseInt(e.guests_count||e.guests,10)||1,booking_date:e.booking_date||e.date||"",booking_time:e.booking_time||e.time||"",notes:(e.notes||e.note||"").trim(),status:e.status||"pending",created_at:e.created_at||(new Date).toISOString()};try{const e=JSON.parse(localStorage.getItem("olion_bookings")||"[]");e.some(e=>e.id===a.id)||(e.unshift(a),localStorage.setItem("olion_bookings",JSON.stringify(e)))}catch(e){console.warn("⚠️ Lỗi lưu booking vào LocalStorage:",e)}const n=supabaseClient||initSupabase();if(n)try{const e={customer_name:a.customer_name,phone:a.phone,booking_type:a.booking_type,guests_count:a.guests_count,booking_date:a.booking_date,booking_time:a.booking_time,notes:a.notes,status:a.status,created_at:a.created_at},{data:t,error:s}=await n.from("bookings").insert([e]).select();if(!s&&t&&t.length>0){try{await n.from("customers").upsert([{name:a.customer_name,contact:a.phone,source:"space"===a.booking_type?"Thuê không gian":"Đặt bàn trước",notes:`Đặt lúc ${(new Date).toLocaleString("vi-VN")} - Ngày ${a.booking_date} (${a.booking_time}), ${a.guests_count} khách.`}],{onConflict:"contact"})}catch(e){console.warn("⚠️ [CRM Sync] Lỗi upsert customer:",e)}try{const e=JSON.parse(localStorage.getItem("olion_bookings")||"[]"),n=e.findIndex(e=>e.id===a.id);if(-1!==n)return e[n]={...e[n],...t[0]},localStorage.setItem("olion_bookings",JSON.stringify(e)),{success:!0,source:"supabase",data:e[n]}}catch(e){}return{success:!0,source:"supabase",data:t[0]}}s&&console.warn("⚠️ [Supabase Bookings] Lỗi insert:",s.message)}catch(e){console.warn("⚠️ [Supabase Bookings] Exception insert:",e.message)}return{success:!0,source:"local",data:a}}async function fetchBookingsFromStorage(){const e=supabaseClient||initSupabase();if(e)try{const{data:t,error:a}=await e.from("bookings").select("*").order("created_at",{ascending:!1});if(!a&&t)try{const e=JSON.parse(localStorage.getItem("olion_bookings")||"[]"),a=new Set(t.map(e=>String(e.id))),n=[...e.filter(e=>!a.has(String(e.id))),...t];return localStorage.setItem("olion_bookings",JSON.stringify(n)),{source:"supabase",data:n}}catch(e){return localStorage.setItem("olion_bookings",JSON.stringify(t)),{source:"supabase",data:t}}}catch(e){console.warn("⚠️ [Supabase Bookings] Lỗi tải từ cloud:",e.message)}try{return{source:"local",data:JSON.parse(localStorage.getItem("olion_bookings")||"[]")}}catch(e){return{source:"local",data:[]}}}async function updateBookingStatusInStorage(e,t){try{let a=JSON.parse(localStorage.getItem("olion_bookings")||"[]");a=a.map(a=>String(a.id)===String(e)?{...a,status:t}:a),localStorage.setItem("olion_bookings",JSON.stringify(a))}catch(e){}const a=supabaseClient||initSupabase();if(a)try{const{error:n}=await a.from("bookings").update({status:t}).eq("id",e);if(!n)return{success:!0,source:"supabase"}}catch(e){console.warn("⚠️ [Supabase Bookings] Lỗi update trạng thái:",e.message)}return{success:!0,source:"local"}}async function deleteBookingFromStorage(e){try{let t=JSON.parse(localStorage.getItem("olion_bookings")||"[]");t=t.filter(t=>String(t.id)!==String(e)),localStorage.setItem("olion_bookings",JSON.stringify(t))}catch(e){}const t=supabaseClient||initSupabase();if(t)try{const{error:a}=await t.from("bookings").delete().eq("id",e);if(!a)return{success:!0,source:"supabase"}}catch(e){console.warn("⚠️ [Supabase Bookings] Lỗi xóa booking:",e.message)}return{success:!0,source:"local"}}function setupAdminRealtime(){const e=supabaseClient||initSupabase();e&&e.channel("admin-channel").on("postgres_changes",{event:"INSERT",schema:"public",table:"feedbacks"},e=>{console.log("New feedback:",e.new),"function"==typeof playNotificationSound&&playNotificationSound(),"function"==typeof showToast&&showToast("🔔 Có góp ý mới từ khách hàng!"),"function"==typeof loadFeedbacks&&loadFeedbacks()}).on("postgres_changes",{event:"INSERT",schema:"public",table:"lucky_spins"},e=>{console.log("New lucky spin:",e.new),"function"==typeof playNotificationSound&&playNotificationSound(),"function"==typeof showToast&&showToast("🎁 Khách hàng vừa quay trúng thưởng!"),"function"==typeof loadMinigame&&loadMinigame()}).on("postgres_changes",{event:"*",schema:"public",table:"bookings"},e=>{if(console.log("Bookings update:",e),"INSERT"===e.eventType){"function"==typeof playNotificationSound&&playNotificationSound();const t=e.new?.customer_name||"Khách hàng";"function"==typeof showToast&&showToast(`🔔 Đơn đặt bàn mới từ ${t}!`)}else"function"==typeof showToast&&showToast("📅 Cập nhật thông tin đơn đặt chỗ");"function"==typeof loadBookings&&loadBookings()}).subscribe()}window.generateMemberCode=generateMemberCode,window.calculateCustomerTier=calculateCustomerTier,window.addCustomerStampInCloud=addCustomerStampInCloud,window.redeemCustomerDrinkInCloud=redeemCustomerDrinkInCloud,window.fetchCustomersFromCloud=fetchCustomersFromCloud,window.saveCustomerToCloud=saveCustomerToCloud,window.deleteCustomerFromCloud=deleteCustomerFromCloud,window.adjustCustomerPointsInCloud=adjustCustomerPointsInCloud,window.fetchCustomerPointHistoryFromCloud=fetchCustomerPointHistoryFromCloud,window.lookupLoyaltyMember=lookupLoyaltyMember,window.addLoyaltyMemberPoints=addLoyaltyMemberPoints,window.redeemLoyaltyMemberPoints=redeemLoyaltyMemberPoints,window.fetchLoyaltyMembersFromCloud=fetchLoyaltyMembersFromCloud,window.saveBookingToStorage=saveBookingToStorage,window.fetchBookingsFromStorage=fetchBookingsFromStorage,window.updateBookingStatusInStorage=updateBookingStatusInStorage,window.deleteBookingFromStorage=deleteBookingFromStorage;