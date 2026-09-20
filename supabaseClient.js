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
  { id: 1, name: 'Cà Phê Muối Olion', price: 35000, category: 'Cà phê', image_url: 'assets/news/news-1-drinks.webp', badge: 'Signature', description: 'Lớp kem muối béo mặn hòa quyện cà phê Robusta & Arabica đậm đà.', is_available: true },
  { id: 2, name: 'Matcha Latte Kem Trứng', price: 45000, category: 'Trà sữa & Matcha', image_url: 'assets/news/news-1-drinks.webp', badge: 'Bán chạy', description: 'Matcha Uji Nhật Bản kết hợp lớp foam kem trứng béo ngậy thủ công.', is_available: true },
  { id: 3, name: 'Bạc Xỉu Kem Béo', price: 32000, category: 'Cà phê', image_url: 'assets/hero1.jpg', badge: 'Bán chạy', description: 'Cà phê sữa tươi nhiều tầng ngọt dịu, thích hợp cho buổi sáng nhẹ nhàng.', is_available: true },
  { id: 4, name: 'Cà Phê Đen Đá Pha Phin', price: 25000, category: 'Cà phê', image_url: 'assets/news/news-1-barista.webp', badge: '', description: 'Hạt cà phê Cầu Đất rang mộc, đậm đà chuẩn vị truyền thống.', is_available: true },
  { id: 5, name: 'Trà Đào Cam Sả Tươi', price: 38000, category: 'Trà trái cây', image_url: 'assets/hero2.jpg', badge: 'Món mới', description: 'Trà đen hảo hạng ủ lạnh, cam vàng mọng nước và sả thơm ngát thanh nhiệt.', is_available: true },
  { id: 6, name: 'Trà Ô Long Dâu Tằm Macchiato', price: 42000, category: 'Trà trái cây', image_url: 'assets/hero3.jpg', badge: 'Signature', description: 'Trà Ô Long thượng hạng kết hợp sốt dâu tằm tự nhiên và kem cheese béo mịn.', is_available: true },
  { id: 7, name: 'Cold Brew Cam Vàng Hạnh Nhân', price: 45000, category: 'Cà phê', image_url: 'assets/news/news-1-serving.webp', badge: 'Món mới', description: 'Cà phê ủ lạnh 18 tiếng thanh khiết, điểm xuyết lát cam sấy thơm lừng.', is_available: true },
  { id: 8, name: 'Bánh Croissant Bơ Pháp', price: 30000, category: 'Bánh & Ăn vặt', image_url: 'assets/news/news-1-flowers.webp', badge: 'Bán chạy', description: 'Bánh sừng bò ngàn lớp thơm bơ giòn rụm nướng nóng mỗi sáng.', is_available: true }
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

      if (!error && data && data.length > 0) {
        localStorage.setItem('olion_menu_items', JSON.stringify(data));
        return { source: 'supabase', data };
      }
    } catch (err) {
      console.warn('⚠️ [Supabase] Lỗi fetch menu_items:', err.message);
    }
  }

  // Fallback LocalStorage
  try {
    let local = JSON.parse(localStorage.getItem('olion_menu_items'));
    if (!local || local.length === 0) {
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

  try {
    const localFeedbacks = JSON.parse(localStorage.getItem('olion_feedbacks') || '[]');
    localFeedbacks.unshift({ ...feedbackData, id: Date.now(), localOnly: !client });
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

  try {
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
        promo_code: spinData.promo_code
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
