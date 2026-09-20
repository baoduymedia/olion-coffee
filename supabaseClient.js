/**
 * Olion Coffee - Supabase Integration Client & SDK
 * Hỗ trợ đồng bộ dữ liệu Realtime 2 chiều giữa Website (index.html), Admin Portal (admin.html) và Supabase Cloud Database.
 * Tích hợp cơ chế tự động Fallback về LocalStorage khi offline hoặc chưa nhập API Key.
 */

const DEFAULT_SUPABASE_URL = localStorage.getItem('olion_supabase_url') || 'https://xwbrbesgnwcngzohprxt.supabase.co';
const DEFAULT_SUPABASE_ANON_KEY = localStorage.getItem('olion_supabase_key') || 'sb_publishable_vWuV07_xPU0wNftK0lpnFQ_oA9XHPLS';

let supabaseClient = null;

/**
 * Khởi tạo hoặc cập nhật kết nối Supabase
 */
function initSupabase(customUrl, customKey) {
  const url = customUrl || localStorage.getItem('olion_supabase_url') || DEFAULT_SUPABASE_URL;
  const key = customKey || localStorage.getItem('olion_supabase_key') || DEFAULT_SUPABASE_ANON_KEY;

  if (window.supabase && url && key && !url.includes('your-project') && key !== 'your-anon-key') {
    try {
      supabaseClient = window.supabase.createClient(url, key);
      console.log('⚡ [Supabase] Đã kết nối cơ sở dữ liệu Cloud thành công:', url);
      return supabaseClient;
    } catch (e) {
      console.warn('⚠️ [Supabase] Lỗi khởi tạo client:', e.message);
      supabaseClient = null;
      return null;
    }
  } else {
    supabaseClient = null;
    return null;
  }
}

// Khởi tạo ngay khi tải file
if (typeof window !== 'undefined') {
  initSupabase();
}

// =========================================================================
// 0. SECURITY & DEVICE FINGERPRINTING & RATE LIMITING
// =========================================================================

/**
 * Tạo mã định danh phần cứng/trình duyệt (Device Fingerprint) an toàn
 */
function getDeviceFingerprint() {
  try {
    const screenRes = `${window.screen?.width || 0}x${window.screen?.height || 0}x${window.screen?.colorDepth || 0}`;
    const timeZone = Intl.DateTimeFormat().resolvedOptions().timeZone || '';
    const language = navigator.language || navigator.userLanguage || '';
    const hardwareConcurrency = navigator.hardwareConcurrency || '';
    const platform = navigator.platform || '';
    const ua = navigator.userAgent || '';
    
    // Thuật toán hash chuỗi đơn giản & nhanh DJB2
    const str = `${ua}|${screenRes}|${timeZone}|${language}|${hardwareConcurrency}|${platform}`;
    let hash = 5381;
    for (let i = 0; i < str.length; i++) {
      hash = ((hash << 5) + hash) + str.charCodeAt(i);
      hash = hash & hash; // Convert to 32bit integer
    }
    return 'fp_' + Math.abs(hash).toString(36);
  } catch (e) {
    return 'fp_fallback_' + Math.random().toString(36).substring(2, 10);
  }
}

/**
 * Lấy hoặc khởi tạo Device ID lưu đồng thời trong LocalStorage & Cookie bảo mật
 */
function getOrCreateDeviceId() {
  try {
    // 1. Kiểm tra LocalStorage
    let deviceId = localStorage.getItem('olion_device_id');
    
    // 2. Kiểm tra Cookie nếu LocalStorage bị xóa
    if (!deviceId) {
      const match = document.cookie.match(/(^|;)\s*olion_device_id\s*=\s*([^;]+)/);
      if (match) deviceId = match[2];
    }
    
    // 3. Nếu chưa có, tạo mới kết hợp Fingerprint + Random UUID
    if (!deviceId) {
      const fp = getDeviceFingerprint();
      const rand = Math.random().toString(36).substring(2, 9);
      const time = Date.now().toString(36);
      deviceId = `dev_${fp}_${time}_${rand}`;
    }
    
    // 4. Đồng bộ lưu lại cả LocalStorage và Cookie (hạn 365 ngày)
    localStorage.setItem('olion_device_id', deviceId);
    const expires = new Date(Date.now() + 365 * 24 * 60 * 60 * 1000).toUTCString();
    document.cookie = `olion_device_id=${deviceId}; expires=${expires}; path=/; SameSite=Lax`;
    
    return deviceId;
  } catch (e) {
    return 'dev_anon_' + Date.now();
  }
}

/**
 * Kiểm tra xem thiết bị / SĐT này đã quay Minigame trong 24h qua chưa
 */
async function canUserSpinToday(phone) {
  const deviceId = getOrCreateDeviceId();
  
  // 1. Kiểm tra nhanh LocalStorage Cooldown (24 giờ = 86400 giây)
  const lastSpinTime = localStorage.getItem('olion_last_spin_time');
  if (lastSpinTime) {
    const elapsedSec = Math.floor((Date.now() - parseInt(lastSpinTime, 10)) / 1000);
    if (elapsedSec < 86400) {
      const waitSec = 86400 - elapsedSec;
      const hours = Math.floor(waitSec / 3600);
      const mins = Math.floor((waitSec % 3600) / 60);
      return {
        can_spin: false,
        wait_seconds: waitSec,
        message: `Bạn đã sử dụng hết lượt quay hôm nay. Hãy quay lại vào ngày mai nhé! (Còn ${hours > 0 ? hours + 'h ' : ''}${mins} phút)`
      };
    }
  }

  // 2. Kiểm tra Database Supabase RPC (Server-side validation)
  const client = supabaseClient || initSupabase();
  if (client) {
    try {
      const { data, error } = await client.rpc('check_can_spin', {
        p_device_id: deviceId,
        p_phone: phone || ''
      });

      if (!error && data) {
        if (!data.can_spin) {
          return {
            can_spin: false,
            wait_seconds: data.wait_seconds || 86400,
            message: data.message || 'Bạn đã sử dụng hết lượt quay hôm nay. Hãy quay lại vào ngày mai nhé!'
          };
        }
      }
    } catch (err) {
      console.warn('⚠️ [Supabase RPC] Lỗi check_can_spin, fallback local:', err.message);
    }
  }

  return { can_spin: true, wait_seconds: 0, message: 'Được phép quay thưởng!' };
}

/**
 * Kiểm tra xem thiết bị / Liên hệ này có gửi góp ý quá nhanh không (Cooldown 5 phút)
 */
async function canUserSubmitFeedback(contact) {
  const deviceId = getOrCreateDeviceId();

  // 1. Kiểm tra nhanh LocalStorage Cooldown (5 phút = 300 giây)
  const lastFbTime = localStorage.getItem('olion_last_feedback_time');
  if (lastFbTime) {
    const elapsedSec = Math.floor((Date.now() - parseInt(lastFbTime, 10)) / 1000);
    if (elapsedSec < 300) {
      const waitSec = 300 - elapsedSec;
      const mins = Math.floor(waitSec / 60);
      const secs = waitSec % 60;
      return {
        can_submit: false,
        wait_seconds: waitSec,
        message: `Bạn vừa gửi đánh giá xong. Vui lòng đợi thêm ${mins > 0 ? mins + ' phút ' : ''}${secs}s trước khi gửi tiếp nhé!`
      };
    }
  }

  // 2. Kiểm tra Database Supabase RPC
  const client = supabaseClient || initSupabase();
  if (client) {
    try {
      const { data, error } = await client.rpc('check_can_feedback', {
        p_device_id: deviceId,
        p_contact: contact || ''
      });

      if (!error && data) {
        if (!data.can_submit) {
          return {
            can_submit: false,
            wait_seconds: data.wait_seconds || 300,
            message: data.message || 'Bạn thao tác quá nhanh! Vui lòng đợi thêm một chút.'
          };
        }
      }
    } catch (err) {
      console.warn('⚠️ [Supabase RPC] Lỗi check_can_feedback, fallback local:', err.message);
    }
  }

  return { can_submit: true, wait_seconds: 0, message: 'Được phép gửi góp ý!' };
}

/**
 * Thực thi Google reCAPTCHA v3 (nếu đã cấu hình Site Key)
 */
async function executeReCaptcha(action = 'submit_feedback') {
  if (typeof window !== 'undefined' && window.grecaptcha && window.RECAPTCHA_SITE_KEY && window.RECAPTCHA_SITE_KEY !== 'YOUR_RECAPTCHA_SITE_KEY') {
    try {
      return await new Promise((resolve) => {
        window.grecaptcha.ready(async () => {
          try {
            const token = await window.grecaptcha.execute(window.RECAPTCHA_SITE_KEY, { action });
            resolve(token);
          } catch (e) {
            console.warn('⚠️ [reCAPTCHA] Lỗi token:', e.message);
            resolve(null);
          }
        });
      });
    } catch (e) {
      return null;
    }
  }
  return null;
}

/**
 * Kiểm tra kết nối tới Supabase Cloud
 */
async function testSupabaseConnection(url, key) {
  if (!window.supabase) return { success: false, message: 'Thư viện Supabase JS chưa được tải!' };
  if (!url || !key) return { success: false, message: 'Vui lòng điền đầy đủ URL và Anon Key!' };

  try {
    const testClient = window.supabase.createClient(url, key);
    const { data, error } = await testClient.from('feedbacks').select('count', { count: 'exact', head: true });
    if (error) {
      return { success: false, message: 'Lỗi Supabase: ' + (error.message || error.details || 'Không thể truy vấn bảng') };
    }
    return { success: true, message: 'Kết nối Supabase Cloud thành công!' };
  } catch (err) {
    return { success: false, message: 'Không thể kết nối: ' + err.message };
  }
}

// =========================================================================
// 1. MODULE THỰC ĐƠN (MENU MANAGEMENT CRUD)
// =========================================================================

const DEFAULT_MENU_ITEMS = [
  // Cà phê
  { id: 1, name: 'ESPRESSO', price: 28000, category: 'Cà phê', image_url: 'assets/menu/espresso.webp', badge: 'BEST', description: 'Nóng / Đá. Espresso nguyên chất đậm đà, hương thơm nồng nàn.', is_available: true },
  { id: 2, name: 'ESPRESSO SỮA', price: 35000, category: 'Cà phê', image_url: 'assets/menu/espresso_sua.webp', badge: 'POPULAR', description: 'Nóng / Đá. Espresso kết hợp sữa tươi béo ngậy thơm lừng.', is_available: true },
  { id: 3, name: 'BẠC XỈU', price: 35000, category: 'Cà phê', image_url: 'assets/menu/bac_xiu.webp', badge: 'HOT', description: 'Nóng / Đá. Cà phê sữa đặc truyền thống đậm đà, ngọt thanh.', is_available: true },
  { id: 4, name: 'LATTE HẠNH NHÂN', price: 39000, category: 'Cà phê', image_url: 'assets/menu/latte_hanh_nhan.webp', badge: '', description: 'Nóng / Đá. Sữa hạnh nhân thơm béo quyện cùng espresso.', is_available: true },
  { id: 5, name: 'CARAMEL LATTE', price: 39000, category: 'Cà phê', image_url: 'assets/menu/caramel_latte.webp', badge: '', description: 'Nóng / Đá. Caramel ngọt thơm hòa quyện cùng latte mịn màng.', is_available: true },
  { id: 6, name: 'AMERICANO', price: 30000, category: 'Cà phê', image_url: 'assets/menu/americano.webp', badge: '', description: 'Nóng / Đá. Espresso pha loãng thanh nhẹ, vị đắng dịu dàng.', is_available: true },
  { id: 7, name: 'CÀ PHÊ MUỐI', price: 39000, category: 'Cà phê', image_url: 'assets/menu/ca_phe_muoi.webp', badge: 'SIGNATURE', description: 'Nóng / Đá. Cà phê đậm đà phủ lớp kem muối béo mặn đặc trưng.', is_available: true },
  { id: 8, name: 'CÀ PHÊ BẠC HÀ', price: 39000, category: 'Cà phê', image_url: 'assets/menu/ca_phe_bac_ha.webp', badge: '', description: 'Đá. Cà phê mát lạnh với hương bạc hà the mát sảng khoái.', is_available: true },
  { id: 9, name: 'CÀ PHÊ SỮA OATSIDE', price: 40000, category: 'Cà phê', image_url: 'assets/menu/ca_phe_sua_oatside.webp', badge: 'NEW', description: 'Nóng / Đá. Sữa yến mạch Oatside thanh nhẹ kết hợp espresso.', is_available: true },

  // Trà trái cây
  { id: 10, name: 'TRÀ VẢI HOA HỒNG', price: 40000, category: 'Trà trái cây', image_url: 'assets/menu/tra_vai_hoa_hong.webp', badge: 'BEST', description: 'Vải ngọt mọng nước kết hợp hương hoa hồng thanh tao dịu nhẹ.', is_available: true },
  { id: 11, name: 'TRÀ CHANH DÂY NHIỆT ĐỚI', price: 40000, category: 'Trà trái cây', image_url: 'assets/menu/tra_chanh_day_nhiet_doi.webp', badge: 'HOT', description: 'Chua ngọt bùng nổ, tươi mát sảng khoái ngày hè.', is_available: true },
  { id: 12, name: 'TRÀ BƯỞI HỒNG CHANH VÀNG', price: 40000, category: 'Trà trái cây', image_url: 'assets/menu/tra_buoi_hong_chanh_vang.webp', badge: '', description: 'Bưởi hồng mọng nước hòa cùng chanh vàng thơm mát.', is_available: true },
  { id: 13, name: 'TRÀ XOÀI CHANH DÂY', price: 40000, category: 'Trà trái cây', image_url: 'assets/menu/tra_xoai_chanh_day.webp', badge: '', description: 'Xoài chín ngọt thanh quyện cùng chanh dây đậm đà.', is_available: true },
  { id: 14, name: 'LỤC TRÀ NHÃN', price: 40000, category: 'Trà trái cây', image_url: 'assets/menu/luc_tra_nhan.webp', badge: '', description: 'Nhãn giòn ngọt ngào kết hợp nền lục trà lài thanh tao.', is_available: true },
  { id: 15, name: 'LỤC TRÀ TRÂN CHÂU TRẮNG', price: 35000, category: 'Trà trái cây', image_url: 'assets/menu/luc_tra_tran_chau_trang.webp', badge: '', description: 'Lục trà lài thanh mát cùng trân châu trắng giòn sần sật.', is_available: true },

  // Trà sữa & Matcha
  { id: 16, name: 'MATCHA LATTE', price: 39000, category: 'Trà sữa & Matcha', image_url: 'assets/menu/matcha_latte.webp', badge: 'SIGNATURE', description: 'Matcha Nhật Bản nguyên chất thơm lừng quyện sữa tươi béo dịu.', is_available: true },
  { id: 17, name: 'MATCHA CARAMEL', price: 45000, category: 'Trà sữa & Matcha', image_url: 'assets/menu/matcha_caramel.webp', badge: '', description: 'Matcha thơm đậm hòa quyện cùng sốt caramel béo ngậy ngọt ngào.', is_available: true },
  { id: 18, name: 'MATCHA BẠC HÀ', price: 45000, category: 'Trà sữa & Matcha', image_url: 'assets/menu/matcha_bac_ha.webp', badge: '', description: 'Sự kết hợp độc đáo giữa vị thanh của matcha và the mát của bạc hà.', is_available: true },
  { id: 19, name: 'MATCHA KEM MUỐI', price: 45000, category: 'Trà sữa & Matcha', image_url: 'assets/menu/matcha_kem_muoi.webp', badge: '', description: 'Lớp kem muối béo ngậy mằn mặn phủ trên nền matcha đậm đà.', is_available: true },
  { id: 20, name: 'MATCHA QUẾ HOA', price: 45000, category: 'Trà sữa & Matcha', image_url: 'assets/menu/matcha_que_hoa.webp', badge: '', description: 'Matcha cao cấp ướp hương hoa quế tự nhiên thanh tao quý phái.', is_available: true },
  { id: 21, name: 'MATCHA COLD WHISK', price: 45000, category: 'Trà sữa & Matcha', image_url: 'assets/menu/matcha_cold_whisk.webp', badge: '', description: 'Đánh bọt matcha lạnh thủ công truyền thống, chuẩn vị Nhật.', is_available: true },
  { id: 22, name: 'MATCHA DỪA', price: 45000, category: 'Trà sữa & Matcha', image_url: 'assets/menu/matcha_dua.webp', badge: '', description: 'Vị thơm bùi của nước cốt dừa tươi quyện cùng bột matcha thượng hạng.', is_available: true },
  { id: 23, name: 'MATCHA DÂU', price: 45000, category: 'Trà sữa & Matcha', image_url: 'assets/menu/matcha_dau.webp', badge: 'HOT', description: 'Sự hòa quyện tuyệt hảo giữa matcha thơm đắng và mứt dâu tây ngọt ngào.', is_available: true },
  { id: 24, name: 'MATCHA OATSIDE', price: 45000, category: 'Trà sữa & Matcha', image_url: 'assets/menu/matcha_oatside.webp', badge: '', description: 'Kết hợp sữa yến mạch Oatside thơm bùi thuần thực vật.', is_available: true },

  // Cacao
  { id: 25, name: 'CACAO LATTE', price: 35000, category: 'Cacao', image_url: 'assets/menu/cacao_latte.webp', badge: 'BEST', description: 'Cacao nguyên chất béo thơm, ấm áp và giàu năng lượng.', is_available: true },
  { id: 26, name: 'CACAO KEM MUỐI', price: 39000, category: 'Cacao', image_url: 'assets/menu/cacao_kem_muoi.webp', badge: 'HOT', description: 'Cacao đậm đà hòa quyện cùng lớp kem muối béo ngậy.', is_available: true },
  { id: 27, name: 'CACAO BẠC HÀ', price: 39000, category: 'Cacao', image_url: 'assets/menu/cacao_bac_ha.webp', badge: '', description: 'Hương bạc hà the mát sảng khoái quyện cùng vị ngọt đắng cacao.', is_available: true },

  // Nước ép
  { id: 28, name: 'NƯỚC ÉP CAM', price: 30000, category: 'Nước ép', image_url: 'assets/menu/nuoc_ep_cam.webp', badge: 'BEST', description: 'Cam sành tươi vắt nguyên chất, dồi dào Vitamin C.', is_available: true },
  { id: 29, name: 'NƯỚC ÉP CHANH DÂY', price: 30000, category: 'Nước ép', image_url: 'assets/menu/nuoc_ep_chanh_day.webp', badge: 'HOT', description: 'Chanh dây tươi thơm nồng, chua ngọt giải nhiệt cực đã.', is_available: true },

  // Sữa chua
  { id: 30, name: 'YAGOUT DÂU', price: 45000, category: 'Sữa chua', image_url: 'assets/menu/yagout_dau.webp', badge: 'BEST', description: 'Sữa chua sánh mịn kết hợp mứt dâu tây chua ngọt thanh mát.', is_available: true },
  { id: 31, name: 'YAGOUT VIỆT QUẤT', price: 45000, category: 'Sữa chua', image_url: 'assets/menu/yagout_viet_quat.webp', badge: 'HOT', description: 'Việt quất bổ dưỡng thơm lừng quyện cùng sữa chua tươi mát.', is_available: true },
  { id: 32, name: 'YAGOUT XOÀI CHANH DÂY', price: 45000, category: 'Sữa chua', image_url: 'assets/menu/yagout_xoai_chanh_day.webp', badge: '', description: 'Xoài chín thơm ngọt hòa quyện cùng chanh dây nhiệt đới.', is_available: true },
  { id: 33, name: 'YAGOUT ĐÀO CHANH DÂY', price: 45000, category: 'Sữa chua', image_url: 'assets/menu/yagout_dao_chanh_day.webp', badge: '', description: 'Đào mọng nước thơm ngọt hòa cùng vị chua dịu nhẹ của chanh dây.', is_available: true },

  // Topping
  { id: 34, name: 'TRÂN CHÂU TRẮNG', price: 7000, category: 'Topping', image_url: 'assets/menu/tran_chau_trang.webp', badge: '', description: 'Trân châu trắng ngọc trai giòn dai thơm ngon.', is_available: true },
  { id: 35, name: 'TRÂN CHÂU Ô LONG', price: 7000, category: 'Topping', image_url: 'assets/menu/tran_chau_o_long.webp', badge: '', description: 'Đậm hương trà ô long rang mộc, mềm dẻo.', is_available: true },
  { id: 36, name: 'THẠCH SƯƠNG SÁO', price: 7000, category: 'Topping', image_url: 'assets/menu/thach_suong_sao.webp', badge: '', description: 'Thạch sương sáo mềm mượt, thanh mát giải nhiệt tự nhiên.', is_available: true },
  { id: 37, name: 'THẠCH QUẾ HOA', price: 7000, category: 'Topping', image_url: 'assets/menu/thach_que_hoa.webp', badge: '', description: 'Thơm thanh hương hoa quế tự nhiên.', is_available: true },
  { id: 38, name: 'THẠCH VẢI HOA HỒNG', price: 7000, category: 'Topping', image_url: 'assets/menu/thach_vai_hoa_hong.webp', badge: '', description: 'Thạch giòn dai thơm ngát hương hoa hồng và vị vải ngọt thanh.', is_available: true },
  { id: 39, name: 'THẠCH CÀ PHÊ', price: 7000, category: 'Topping', image_url: 'assets/menu/thach_ca_phe.webp', badge: '', description: 'Thạch cà phê nấu thủ công giòn thơm đậm vị.', is_available: true }
];

/**
 * Lấy danh sách thực đơn từ Cloud hoặc Fallback LocalStorage
 */
async function fetchMenuItemsFromCloud() {
  const client = supabaseClient || initSupabase();

  if (client) {
    try {
      const { data, error } = await client
        .from('menu_items')
        .select('*')
        .order('id', { ascending: true });

      // Only accept cloud data if it is NOT the 8 old dummy test items!
      if (!error && data && data.length >= 30) {
        localStorage.setItem('olion_menu_items', JSON.stringify(data));
        return { source: 'supabase', data };
      } else if (!error && data && data.length > 0 && data.length < 30) {
        console.warn('⚠️ [Supabase] Detected outdated dummy test items in database (< 30 items). Using official 39 DEFAULT_MENU_ITEMS.');
        localStorage.removeItem('olion_menu_items');
        return { source: 'local_default', data: DEFAULT_MENU_ITEMS };
      }
    } catch (err) {
      console.warn('⚠️ [Supabase] Lỗi fetch menu_items:', err.message);
    }
  }

  // Fallback LocalStorage
  try {
    let local = JSON.parse(localStorage.getItem('olion_menu_items'));
    if (!local || !Array.isArray(local) || local.length < 30 || local.some(i => i.name === 'Trà Đào Cam Sả Tươi' || i.name === 'Bánh Croissant Bơ Pháp')) {
      local = DEFAULT_MENU_ITEMS;
      localStorage.setItem('olion_menu_items', JSON.stringify(local));
    }
    return { source: 'local', data: local };
  } catch (e) {
    return { source: 'local', data: DEFAULT_MENU_ITEMS };
  }
}

/**
 * Thêm mới hoặc Cập nhật món trong thực đơn
 */
async function saveMenuItemToCloud(menuItem) {
  const client = supabaseClient || initSupabase();

  // Cập nhật LocalStorage trước để phản hồi tức thì
  try {
    let local = JSON.parse(localStorage.getItem('olion_menu_items') || '[]');
    if (menuItem.id) {
      const idx = local.findIndex(m => m.id === menuItem.id);
      if (idx !== -1) local[idx] = { ...local[idx], ...menuItem, updated_at: new Date().toISOString() };
      else local.unshift(menuItem);
    } else {
      const newLocalItem = { ...menuItem, id: Date.now(), created_at: new Date().toISOString() };
      local.unshift(newLocalItem);
    }
    localStorage.setItem('olion_menu_items', JSON.stringify(local));
  } catch (e) {}

  if (client) {
    try {
      const payload = {
        name: menuItem.name,
        price: Number(menuItem.price) || 0,
        category: menuItem.category || 'Cà phê',
        image_url: menuItem.image_url || 'assets/news/news-1-drinks.webp',
        badge: menuItem.badge || '',
        description: menuItem.description || '',
        is_available: menuItem.is_available !== false,
        updated_at: new Date().toISOString()
      };

      if (menuItem.id && typeof menuItem.id === 'number' && menuItem.id < 100000000000) {
        // Update existing item
        const { data, error } = await client
          .from('menu_items')
          .update(payload)
          .eq('id', menuItem.id)
          .select();
        if (error) throw error;
        return { success: true, source: 'supabase', data: data[0] };
      } else {
        // Insert new item
        const { data, error } = await client
          .from('menu_items')
          .insert([payload])
          .select();
        if (error) throw error;
        return { success: true, source: 'supabase', data: data[0] };
      }
    } catch (err) {
      console.warn('⚠️ [Supabase] Lỗi lưu menu item:', err.message);
      return { success: true, source: 'local_fallback', error: err.message };
    }
  }

  return { success: true, source: 'local_only' };
}

/**
 * Xóa món khỏi thực đơn
 */
async function deleteMenuItemFromCloud(id) {
  const client = supabaseClient || initSupabase();

  try {
    let local = JSON.parse(localStorage.getItem('olion_menu_items') || '[]');
    local = local.filter(m => m.id !== id);
    localStorage.setItem('olion_menu_items', JSON.stringify(local));
  } catch (e) {}

  if (client) {
    try {
      const { error } = await client.from('menu_items').delete().eq('id', id);
      if (error) throw error;
      return { success: true, source: 'supabase' };
    } catch (err) {
      return { success: false, error: err.message };
    }
  }
  return { success: true, source: 'local' };
}

/**
 * Bật / tắt trạng thái Còn hàng / Hết hàng
 */
async function toggleMenuItemAvailabilityInCloud(id, isAvailable) {
  const client = supabaseClient || initSupabase();

  try {
    let local = JSON.parse(localStorage.getItem('olion_menu_items') || '[]');
    local = local.map(m => m.id === id ? { ...m, is_available: isAvailable } : m);
    localStorage.setItem('olion_menu_items', JSON.stringify(local));
  } catch (e) {}

  if (client) {
    try {
      const { error } = await client
        .from('menu_items')
        .update({ is_available: isAvailable, updated_at: new Date().toISOString() })
        .eq('id', id);
      if (error) throw error;
      return { success: true, source: 'supabase' };
    } catch (err) {
      return { success: false, error: err.message };
    }
  }
  return { success: true, source: 'local' };
}

// =========================================================================
// 2. MODULE KHÁCH HÀNG & TÍCH ĐIỂM (LOYALTY PROGRAM)
// =========================================================================

const DEFAULT_CUSTOMERS = [
  { id: 1, name: 'Nguyễn Minh Anh', contact: '0908123456', points: 150, tier: 'Vàng', source: 'Quầy thu ngân', notes: 'Khách ruột uống Cà phê Muối mỗi sáng', date: '20/09/2026' },
  { id: 2, name: 'Trần Hoàng Nam', contact: '0912334455', points: 80, tier: 'Bạc', source: 'Minigame Vòng Quay', notes: 'Đã trúng Voucher 20k', date: '19/09/2026' },
  { id: 3, name: 'Lê Thanh Trúc', contact: '0912345678', points: 220, tier: 'Kim Cương', source: 'Website Check-in', notes: 'VIP ghé quán làm việc cuối tuần', date: '18/09/2026' },
  { id: 4, name: 'Phạm Quốc Bảo', contact: '0978999888', points: 45, tier: 'Thành viên', source: 'Minigame Vòng Quay', notes: 'Khách mới ghé thử Matcha', date: '17/09/2026' }
];

/**
 * Xác định hạng thẻ thành viên theo điểm số
 */
function calculateCustomerTier(points) {
  const p = Number(points) || 0;
  if (p >= 200) return 'Kim Cương';
  if (p >= 100) return 'Vàng';
  if (p >= 50) return 'Bạc';
  return 'Thành viên';
}

/**
 * Lấy danh sách khách hàng và điểm tích lũy
 */
async function fetchCustomersFromCloud() {
  const client = supabaseClient || initSupabase();

  if (client) {
    try {
      const { data, error } = await client
        .from('customers')
        .select('*')
        .order('points', { ascending: false });

      if (!error && data && data.length > 0) {
        const mapped = data.map(c => ({
          id: c.id,
          name: c.name || 'Khách hàng',
          contact: c.contact,
          points: Number(c.points) || 0,
          tier: c.tier || calculateCustomerTier(c.points),
          source: c.source || 'Website',
          notes: c.notes || '',
          date: c.created_at ? new Date(c.created_at).toLocaleDateString('vi-VN') : 'Gần đây',
          created_at: c.created_at
        }));
        localStorage.setItem('olion_customers', JSON.stringify(mapped));
        return { source: 'supabase', data: mapped };
      }
    } catch (err) {
      console.warn('⚠️ [Supabase Admin] Lỗi tải customers:', err.message);
    }
  }

  // Fallback LocalStorage
  try {
    let local = JSON.parse(localStorage.getItem('olion_customers'));
    if (!local || local.length === 0) {
      local = DEFAULT_CUSTOMERS;
      localStorage.setItem('olion_customers', JSON.stringify(local));
    }
    return { source: 'local', data: local };
  } catch (e) {
    return { source: 'local', data: DEFAULT_CUSTOMERS };
  }
}

/**
 * Thêm hoặc Cập nhật Khách Hàng
 */
async function saveCustomerToCloud(cust) {
  const client = supabaseClient || initSupabase();
  const tier = calculateCustomerTier(cust.points || 0);

  // LocalStorage sync
  try {
    let local = JSON.parse(localStorage.getItem('olion_customers') || '[]');
    const idx = local.findIndex(c => c.contact === cust.contact || c.id === cust.id);
    if (idx !== -1) {
      local[idx] = { ...local[idx], ...cust, tier, date: local[idx].date || new Date().toLocaleDateString('vi-VN') };
    } else {
      local.unshift({ ...cust, id: Date.now(), tier, date: new Date().toLocaleDateString('vi-VN') });
    }
    localStorage.setItem('olion_customers', JSON.stringify(local));
  } catch (e) {}

  if (client) {
    try {
      const payload = {
        name: cust.name || 'Khách hàng',
        contact: cust.contact,
        points: Number(cust.points) || 0,
        tier: tier,
        source: cust.source || 'Quản trị viên tạo',
        notes: cust.notes || '',
        updated_at: new Date().toISOString()
      };

      if (cust.id && typeof cust.id === 'number' && cust.id < 100000000000) {
        const { data, error } = await client.from('customers').update(payload).eq('id', cust.id).select();
        if (error) throw error;
        return { success: true, source: 'supabase', data: data[0] };
      } else {
        const { data, error } = await client.from('customers').insert([payload]).select();
        if (error) throw error;
        return { success: true, source: 'supabase', data: data[0] };
      }
    } catch (err) {
      console.warn('⚠️ [Supabase] Lỗi lưu customer:', err.message);
      return { success: true, source: 'local_fallback', error: err.message };
    }
  }

  return { success: true, source: 'local_only' };
}

/**
 * Cộng / Trừ điểm cho Khách Hàng và lưu sổ giao dịch (Point Transactions)
 */
async function adjustCustomerPointsInCloud(customerId, phone, pointsDelta, reason, actionType = 'earn') {
  const client = supabaseClient || initSupabase();
  const delta = Number(pointsDelta) || 0;

  let newBalance = 0;
  let updatedCust = null;

  // 1. Cập nhật LocalStorage
  try {
    let localCusts = JSON.parse(localStorage.getItem('olion_customers') || '[]');
    let target = localCusts.find(c => c.id === customerId || c.contact === phone);
    if (target) {
      target.points = Math.max(0, (target.points || 0) + delta);
      target.tier = calculateCustomerTier(target.points);
      newBalance = target.points;
      updatedCust = target;
      localStorage.setItem('olion_customers', JSON.stringify(localCusts));
    }

    // Ghi sổ transaction local
    let txs = JSON.parse(localStorage.getItem('olion_point_transactions') || '[]');
    txs.unshift({
      id: Date.now(),
      customer_id: customerId,
      customer_contact: phone,
      action_type: actionType,
      points_change: delta,
      balance_after: newBalance,
      reason: reason || (delta > 0 ? 'Tích điểm mua nước' : 'Đổi thưởng voucher'),
      created_at: new Date().toISOString()
    });
    localStorage.setItem('olion_point_transactions', JSON.stringify(txs));
  } catch (e) {}

  // 2. Cập nhật Supabase Cloud
  if (client) {
    try {
      // Lấy balance hiện tại từ Supabase
      const { data: currCust, error: fetchErr } = await client
        .from('customers')
        .select('*')
        .eq('contact', phone)
        .maybeSingle();

      if (!fetchErr && currCust) {
        newBalance = Math.max(0, (currCust.points || 0) + delta);
        const newTier = calculateCustomerTier(newBalance);

        await client
          .from('customers')
          .update({ points: newBalance, tier: newTier, updated_at: new Date().toISOString() })
          .eq('id', currCust.id);

        // Lưu bản ghi point_transactions
        await client.from('point_transactions').insert([{
          customer_id: currCust.id,
          customer_contact: phone,
          action_type: actionType,
          points_change: delta,
          balance_after: newBalance,
          reason: reason || (delta > 0 ? 'Tích điểm hóa đơn' : 'Đổi ưu đãi')
        }]);

        return { success: true, source: 'supabase', newBalance, tier: newTier };
      }
    } catch (err) {
      console.warn('⚠️ [Supabase] Lỗi cập nhật điểm:', err.message);
      return { success: true, source: 'local_fallback', newBalance };
    }
  }

  return { success: true, source: 'local_only', newBalance };
}

/**
 * Lấy lịch sử giao dịch điểm của khách hàng
 */
async function fetchCustomerPointHistoryFromCloud(customerId, phone) {
  const client = supabaseClient || initSupabase();

  if (client && phone) {
    try {
      const { data, error } = await client
        .from('point_transactions')
        .select('*')
        .eq('customer_contact', phone)
        .order('created_at', { ascending: false })
        .limit(20);

      if (!error && data) return { source: 'supabase', data };
    } catch (err) {}
  }

  // Fallback Local
  try {
    const txs = JSON.parse(localStorage.getItem('olion_point_transactions') || '[]');
    const filtered = txs.filter(t => t.customer_contact === phone || t.customer_id === customerId);
    return { source: 'local', data: filtered };
  } catch (e) {
    return { source: 'local', data: [] };
  }
}

/**
 * Xóa khách hàng (Admin Portal)
 */
async function deleteCustomerFromCloud(id) {
  const client = supabaseClient || initSupabase();

  try {
    let local = JSON.parse(localStorage.getItem('olion_customers') || '[]');
    local = local.filter(c => c.id !== id);
    localStorage.setItem('olion_customers', JSON.stringify(local));
  } catch (e) {}

  if (client) {
    try {
      const { error } = await client.from('customers').delete().eq('id', id);
      if (error) throw error;
      return { success: true, source: 'supabase' };
    } catch (err) {
      return { success: false, error: err.message };
    }
  }
  return { success: true, source: 'local' };
}

// =========================================================================
// 3. GÓP Ý & ĐÁNH GIÁ (FEEDBACKS)
// =========================================================================

async function submitFeedbackToCloud(feedbackData) {
  const client = supabaseClient || initSupabase();
  const deviceId = getOrCreateDeviceId();

  // Ghi nhận cooldown 5 phút cho lượt gửi tiếp theo
  try {
    localStorage.setItem('olion_last_feedback_time', Date.now().toString());
    const localFeedbacks = JSON.parse(localStorage.getItem('olion_feedbacks') || '[]');
    localFeedbacks.unshift({ ...feedbackData, id: Date.now(), device_id: deviceId, localOnly: !client });
    localStorage.setItem('olion_feedbacks', JSON.stringify(localFeedbacks));
  } catch (e) {}

  if (client) {
    try {
      const { data, error } = await client.from('feedbacks').insert([{
        name: feedbackData.name || 'Khách ghé quán',
        contact: feedbackData.contact || '',
        rating: feedbackData.rating || 5,
        content: feedbackData.content || '',
        image_url: feedbackData.imageDataUrl || feedbackData.image_url || null,
        device_id: deviceId,
        approved: true
      }]).select();

      if (error) throw error;
      console.log('✅ [Supabase] Đã lưu đánh giá lên Cloud:', data);
      return { success: true, source: 'supabase', data };
    } catch (err) {
      console.warn('⚠️ [Supabase] Lỗi insert feedbacks:', err.message);
      return { success: true, source: 'local_fallback', error: err.message };
    }
  }

  return { success: true, source: 'local_only' };
}

async function fetchApprovedFeedbacksFromCloud() {
  const client = supabaseClient || initSupabase();

  if (client) {
    try {
      const { data, error } = await client
        .from('feedbacks')
        .select('*')
        .eq('approved', true)
        .order('created_at', { ascending: false })
        .limit(6);

      if (!error && data && data.length > 0) {
        return data.map(item => ({
          id: item.id,
          name: item.name,
          contact: item.contact,
          rating: item.rating,
          content: item.content,
          imageDataUrl: item.image_url,
          date: item.created_at ? new Date(item.created_at).toLocaleDateString('vi-VN') : 'Gần đây',
          approved: item.approved
        }));
      }
    } catch (err) {
      console.warn('⚠️ [Supabase] Không thể lấy feedbacks từ cloud:', err.message);
    }
  }

  try {
    const local = JSON.parse(localStorage.getItem('olion_feedbacks') || '[]');
    return local.filter(item => item.approved !== false);
  } catch (e) {
    return [];
  }
}

async function fetchAdminFeedbacksFromCloud() {
  const client = supabaseClient || initSupabase();

  if (client) {
    try {
      const { data, error } = await client
        .from('feedbacks')
        .select('*')
        .order('created_at', { ascending: false });

      if (!error && data) {
        return {
          source: 'supabase',
          data: data.map(item => ({
            id: item.id,
            name: item.name,
            contact: item.contact,
            rating: item.rating,
            content: item.content,
            imageDataUrl: item.image_url,
            date: item.created_at ? new Date(item.created_at).toLocaleString('vi-VN') : 'Gần đây',
            approved: item.approved,
            created_at: item.created_at
          }))
        };
      }
    } catch (err) {
      console.warn('⚠️ [Supabase Admin] Lỗi tải feedbacks từ cloud:', err.message);
    }
  }

  const local = JSON.parse(localStorage.getItem('olion_feedbacks') || '[]');
  return { source: 'local', data: local };
}

async function toggleFeedbackApprovalInCloud(id, newApprovedStatus) {
  const client = supabaseClient || initSupabase();

  try {
    let local = JSON.parse(localStorage.getItem('olion_feedbacks') || '[]');
    local = local.map(f => f.id === id ? { ...f, approved: newApprovedStatus } : f);
    localStorage.setItem('olion_feedbacks', JSON.stringify(local));
  } catch (e) {}

  if (client) {
    try {
      const { error } = await client
        .from('feedbacks')
        .update({ approved: newApprovedStatus })
        .eq('id', id);

      if (error) throw error;
      return { success: true, source: 'supabase' };
    } catch (err) {
      return { success: false, error: err.message };
    }
  }
  return { success: true, source: 'local' };
}

async function deleteFeedbackFromCloud(id) {
  const client = supabaseClient || initSupabase();

  try {
    let local = JSON.parse(localStorage.getItem('olion_feedbacks') || '[]');
    local = local.filter(f => f.id !== id);
    localStorage.setItem('olion_feedbacks', JSON.stringify(local));
  } catch (e) {}

  if (client) {
    try {
      const { error } = await client.from('feedbacks').delete().eq('id', id);
      if (error) throw error;
      return { success: true, source: 'supabase' };
    } catch (err) {
      return { success: false, error: err.message };
    }
  }
  return { success: true, source: 'local' };
}

// =========================================================================
// 4. VÒNG QUAY MINIGAME (LUCKY SPINS)
// =========================================================================

async function recordLuckySpinToCloud(spinData) {
  const client = supabaseClient || initSupabase();
  const deviceId = getOrCreateDeviceId();

  // Ghi nhận cooldown 24h vào LocalStorage
  try {
    localStorage.setItem('olion_last_spin_time', Date.now().toString());
    const localCustomers = JSON.parse(localStorage.getItem('olion_customers') || '[]');
    localCustomers.unshift({
      id: Date.now(),
      name: spinData.customer_name,
      contact: spinData.customer_phone,
      points: 10, // Tặng 10 điểm khi quay minigame!
      tier: 'Thành viên',
      source: `Minigame: ${spinData.prize_name} (Mã: ${spinData.promo_code})`,
      date: new Date().toLocaleDateString('vi-VN')
    });
    localStorage.setItem('olion_customers', JSON.stringify(localCustomers));
  } catch (e) {}

  if (client) {
    try {
      await client.from('lucky_spins').insert([{
        customer_name: spinData.customer_name || 'Khách quay minigame',
        customer_phone: spinData.customer_phone,
        prize_name: spinData.prize_name,
        promo_code: spinData.promo_code,
        device_id: deviceId
      }]);

      await client.from('customers').upsert([{
        name: spinData.customer_name || 'Khách quay minigame',
        contact: spinData.customer_phone,
        source: `Minigame: ${spinData.prize_name} (Mã: ${spinData.promo_code})`
      }], { onConflict: 'contact' });

      return { success: true, source: 'supabase' };
    } catch (err) {
      return { success: true, source: 'local_fallback' };
    }
  }

  return { success: true, source: 'local_only' };
}

async function fetchLuckySpinsFromCloud() {
  const client = supabaseClient || initSupabase();

  if (client) {
    try {
      const { data, error } = await client
        .from('lucky_spins')
        .select('*')
        .order('created_at', { ascending: false })
        .limit(100);

      if (!error && data) {
        return {
          source: 'supabase',
          data: data.map(s => ({
            id: s.id,
            name: s.customer_name,
            contact: s.customer_phone,
            source: `${s.prize_name} (Mã: ${s.promo_code})`,
            date: s.created_at ? new Date(s.created_at).toLocaleString('vi-VN') : 'Gần đây'
          }))
        };
      }
    } catch (err) {
      console.warn('⚠️ [Supabase Admin] Lỗi tải lucky_spins:', err.message);
    }
  }

  const customers = JSON.parse(localStorage.getItem('olion_customers') || '[]');
  const minigameLeads = customers.filter(c => (c.source || '').includes('Minigame'));
  return { source: 'local', data: minigameLeads };
}

// =========================================================================
// 5. MODULE THÀNH VIÊN TÍCH ĐIỂM (LOYALTY MEMBERS)
// =========================================================================

const DEFAULT_LOYALTY_MEMBERS = [
  { id: 1, phone_number: '0908123456', customer_name: 'Nguyễn Minh Anh', points: 80, total_visits: 5 },
  { id: 2, phone_number: '0912334455', customer_name: 'Trần Hoàng Nam', points: 35, total_visits: 2 },
  { id: 3, phone_number: '0912345678', customer_name: 'Lê Thanh Trúc', points: 120, total_visits: 9 },
  { id: 4, phone_number: '0978999888', customer_name: 'Phạm Quốc Bảo', points: 15, total_visits: 1 }
];

/**
 * Tra cứu thông tin điểm tích lũy của khách hàng theo số điện thoại
 */
async function lookupLoyaltyMember(phone) {
  const cleanPhone = (phone || '').replace(/[^0-9]/g, '').trim();
  if (!cleanPhone) {
    return { success: false, error: 'Vui lòng nhập số điện thoại hợp lệ.' };
  }

  const client = supabaseClient || initSupabase();

  // 1. Tìm trên Supabase table 'loyalty_members'
  if (client) {
    try {
      const { data, error } = await client
        .from('loyalty_members')
        .select('*')
        .eq('phone_number', cleanPhone)
        .maybeSingle();

      if (!error && data) {
        return {
          success: true,
          source: 'supabase',
          member: {
            id: data.id,
            phone_number: data.phone_number,
            customer_name: data.customer_name || 'Khách hàng thân thiết',
            points: Number(data.points) || 0,
            total_visits: Number(data.total_visits) || 1
          }
        };
      }

      // Fallback kiểm tra bảng 'customers' nếu chưa có trong 'loyalty_members'
      const { data: custData } = await client
        .from('customers')
        .select('*')
        .eq('contact', cleanPhone)
        .maybeSingle();

      if (custData) {
        return {
          success: true,
          source: 'supabase_customers',
          member: {
            id: custData.id,
            phone_number: custData.contact,
            customer_name: custData.name || 'Khách hàng thân thiết',
            points: Number(custData.points) || 0,
            total_visits: 1
          }
        };
      }
    } catch (err) {
      console.warn('⚠️ [Supabase] Lỗi tra cứu loyalty_members:', err.message);
    }
  }

  // 2. Fallback LocalStorage
  try {
    let local = JSON.parse(localStorage.getItem('olion_loyalty_members') || '[]');
    if (!local || local.length === 0) {
      local = DEFAULT_LOYALTY_MEMBERS;
      localStorage.setItem('olion_loyalty_members', JSON.stringify(local));
    }
    const match = local.find(m => m.phone_number === cleanPhone);
    if (match) {
      return { success: true, source: 'local', member: match };
    }

    // Kiểm tra olion_customers
    let localCusts = JSON.parse(localStorage.getItem('olion_customers') || '[]');
    const matchCust = localCusts.find(c => c.contact === cleanPhone);
    if (matchCust) {
      return {
        success: true,
        source: 'local_customers',
        member: {
          phone_number: matchCust.contact,
          customer_name: matchCust.name || 'Khách hàng thân thiết',
          points: Number(matchCust.points) || 0,
          total_visits: 1
        }
      };
    }
  } catch (e) {}

  return { success: false, not_found: true, message: 'Chưa tìm thấy thông tin tích điểm với số điện thoại này. Bạn có thể ghé quán order đồ uống để tích điểm ngay lần đầu tiên!' };
}

/**
 * Cộng điểm tích lũy cho khách hàng (khi mua nước)
 */
async function addLoyaltyMemberPoints(phone, pointsDelta, customerName = '') {
  const cleanPhone = (phone || '').replace(/[^0-9]/g, '').trim();
  const delta = Math.max(1, Number(pointsDelta) || 0);
  if (!cleanPhone) return { success: false, error: 'Số điện thoại không hợp lệ' };

  const client = supabaseClient || initSupabase();
  let updatedMember = null;

  // Cập nhật LocalStorage
  try {
    let local = JSON.parse(localStorage.getItem('olion_loyalty_members') || '[]');
    if (!local.length) local = DEFAULT_LOYALTY_MEMBERS;
    let idx = local.findIndex(m => m.phone_number === cleanPhone);
    if (idx !== -1) {
      local[idx].points = (Number(local[idx].points) || 0) + delta;
      local[idx].total_visits = (Number(local[idx].total_visits) || 1) + 1;
      if (customerName) local[idx].customer_name = customerName;
      updatedMember = local[idx];
    } else {
      updatedMember = {
        id: Date.now(),
        phone_number: cleanPhone,
        customer_name: customerName || 'Khách hàng thân thiết',
        points: delta,
        total_visits: 1
      };
      local.unshift(updatedMember);
    }
    localStorage.setItem('olion_loyalty_members', JSON.stringify(local));
  } catch (e) {}

  if (client) {
    try {
      const { data: existing } = await client
        .from('loyalty_members')
        .select('*')
        .eq('phone_number', cleanPhone)
        .maybeSingle();

      if (existing) {
        const newPoints = (Number(existing.points) || 0) + delta;
        const newVisits = (Number(existing.total_visits) || 1) + 1;
        const { data, error } = await client
          .from('loyalty_members')
          .update({
            points: newPoints,
            total_visits: newVisits,
            customer_name: customerName || existing.customer_name,
            updated_at: new Date().toISOString()
          })
          .eq('id', existing.id)
          .select()
          .single();

        if (!error && data) return { success: true, source: 'supabase', member: data };
      } else {
        const { data, error } = await client
          .from('loyalty_members')
          .insert([{
            phone_number: cleanPhone,
            customer_name: customerName || 'Khách hàng thân thiết',
            points: delta,
            total_visits: 1
          }])
          .select()
          .single();

        if (!error && data) return { success: true, source: 'supabase', member: data };
      }
    } catch (err) {
      console.warn('⚠️ [Supabase] Lỗi cộng điểm loyalty_members:', err.message);
    }
  }

  return { success: true, source: 'local', member: updatedMember };
}

/**
 * Đổi thưởng (Trừ điểm khi khách dùng voucher/ly miễn phí)
 */
async function redeemLoyaltyMemberPoints(phone, pointsToRedeem, rewardReason = 'Đổi quà') {
  const cleanPhone = (phone || '').replace(/[^0-9]/g, '').trim();
  const redeemAmount = Math.max(1, Number(pointsToRedeem) || 0);
  if (!cleanPhone) return { success: false, error: 'Số điện thoại không hợp lệ' };

  const client = supabaseClient || initSupabase();
  let updatedMember = null;

  // LocalStorage check & update
  try {
    let local = JSON.parse(localStorage.getItem('olion_loyalty_members') || '[]');
    if (!local.length) local = DEFAULT_LOYALTY_MEMBERS;
    let idx = local.findIndex(m => m.phone_number === cleanPhone);
    if (idx !== -1) {
      if ((local[idx].points || 0) < redeemAmount) {
        return { success: false, error: `Số điểm hiện tại (${local[idx].points}) không đủ để đổi ưu đãi này (${redeemAmount} điểm).` };
      }
      local[idx].points -= redeemAmount;
      updatedMember = local[idx];
      localStorage.setItem('olion_loyalty_members', JSON.stringify(local));
    }
  } catch (e) {}

  if (client) {
    try {
      const { data: existing, error: fetchErr } = await client
        .from('loyalty_members')
        .select('*')
        .eq('phone_number', cleanPhone)
        .maybeSingle();

      if (!fetchErr && existing) {
        if ((existing.points || 0) < redeemAmount) {
          return { success: false, error: `Số điểm hiện tại (${existing.points}) không đủ để đổi ưu đãi này (${redeemAmount} điểm).` };
        }
        const newPoints = existing.points - redeemAmount;
        const { data, error } = await client
          .from('loyalty_members')
          .update({ points: newPoints, updated_at: new Date().toISOString() })
          .eq('id', existing.id)
          .select()
          .single();

        if (!error && data) return { success: true, source: 'supabase', member: data };
      }
    } catch (err) {
      console.warn('⚠️ [Supabase] Lỗi trừ điểm loyalty_members:', err.message);
    }
  }

  if (updatedMember) {
    return { success: true, source: 'local', member: updatedMember };
  }
  return { success: false, error: 'Không tìm thấy khách hàng để trừ điểm.' };
}

/**
 * Lấy danh sách thành viên tích điểm cho Admin
 */
async function fetchLoyaltyMembersFromCloud() {
  const client = supabaseClient || initSupabase();
  if (client) {
    try {
      const { data, error } = await client
        .from('loyalty_members')
        .select('*')
        .order('points', { ascending: false });

      if (!error && data && data.length > 0) {
        localStorage.setItem('olion_loyalty_members', JSON.stringify(data));
        return { source: 'supabase', data };
      }
    } catch (err) {
      console.warn('⚠️ [Supabase] Lỗi tải danh sách loyalty_members:', err.message);
    }
  }

  try {
    let local = JSON.parse(localStorage.getItem('olion_loyalty_members') || '[]');
    if (!local || local.length === 0) {
      local = DEFAULT_LOYALTY_MEMBERS;
      localStorage.setItem('olion_loyalty_members', JSON.stringify(local));
    }
    return { source: 'local', data: local };
  } catch (e) {
    return { source: 'local', data: DEFAULT_LOYALTY_MEMBERS };
  }
}

// Gán các hàm lên window để truy cập từ index.html và admin.html
window.lookupLoyaltyMember = lookupLoyaltyMember;
window.addLoyaltyMemberPoints = addLoyaltyMemberPoints;
window.redeemLoyaltyMemberPoints = redeemLoyaltyMemberPoints;
window.fetchLoyaltyMembersFromCloud = fetchLoyaltyMembersFromCloud;

