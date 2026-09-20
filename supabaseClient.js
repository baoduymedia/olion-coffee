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

/**
 * 1. Gửi đánh giá / góp ý của khách hàng (Frontend)
 */
async function submitFeedbackToCloud(feedbackData) {
  const client = supabaseClient || initSupabase();

  // Lưu bản sao LocalStorage dự phòng
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
      console.warn('⚠️ [Supabase] Lỗi insert, đã lưu LocalStorage dự phòng:', err.message);
      return { success: true, source: 'local_fallback', error: err.message };
    }
  }

  return { success: true, source: 'local_only' };
}

/**
 * 2. Ghi nhận lượt quay trúng thưởng Lucky Wheel (Frontend)
 */
async function recordLuckySpinToCloud(spinData) {
  const client = supabaseClient || initSupabase();

  // Lưu bản sao LocalStorage
  try {
    const localCustomers = JSON.parse(localStorage.getItem('olion_customers') || '[]');
    localCustomers.unshift({
      id: Date.now(),
      name: spinData.customer_name,
      contact: spinData.customer_phone,
      source: `Minigame: ${spinData.prize_name} (Mã: ${spinData.promo_code})`,
      date: new Date().toLocaleDateString('vi-VN')
    });
    localStorage.setItem('olion_customers', JSON.stringify(localCustomers));
  } catch (e) {}

  if (client) {
    try {
      // 1. Lưu vào bảng lucky_spins
      await client.from('lucky_spins').insert([{
        customer_name: spinData.customer_name || 'Khách quay minigame',
        customer_phone: spinData.customer_phone,
        prize_name: spinData.prize_name,
        promo_code: spinData.promo_code
      }]);

      // 2. Lưu vào bảng customers (Leads)
      await client.from('customers').insert([{
        name: spinData.customer_name || 'Khách quay minigame',
        contact: spinData.customer_phone,
        source: `Minigame: ${spinData.prize_name} (Mã: ${spinData.promo_code})`
      }]);

      console.log('✅ [Supabase] Đã ghi nhận vòng quay may mắn lên Cloud!');
      return { success: true, source: 'supabase' };
    } catch (err) {
      console.warn('⚠️ [Supabase] Lỗi insert minigame, đã lưu LocalStorage:', err.message);
      return { success: true, source: 'local_fallback' };
    }
  }

  return { success: true, source: 'local_only' };
}

/**
 * 3. Lấy danh sách đánh giá đã duyệt hiển thị ngoài trang chủ (Frontend)
 */
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
      console.warn('⚠️ [Supabase] Không thể lấy feedbacks từ cloud, dùng fallback:', err.message);
    }
  }

  // Fallback về LocalStorage
  try {
    const local = JSON.parse(localStorage.getItem('olion_feedbacks') || '[]');
    return local.filter(item => item.approved !== false);
  } catch (e) {
    return [];
  }
}

/**
 * 4. Lấy TOÀN BỘ đánh giá cho trang Admin (Admin Portal)
 */
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

  // Fallback về LocalStorage
  const local = JSON.parse(localStorage.getItem('olion_feedbacks') || '[]');
  return { source: 'local', data: local };
}

/**
 * 5. Bật / Tắt trạng thái duyệt đánh giá (Admin Portal)
 */
async function toggleFeedbackApprovalInCloud(id, newApprovedStatus) {
  const client = supabaseClient || initSupabase();

  // Cập nhật LocalStorage
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
      console.warn('⚠️ [Supabase Admin] Lỗi update approved status:', err.message);
      return { success: false, error: err.message };
    }
  }
  return { success: true, source: 'local' };
}

/**
 * 6. Xóa đánh giá khỏi Cloud và LocalStorage (Admin Portal)
 */
async function deleteFeedbackFromCloud(id) {
  const client = supabaseClient || initSupabase();

  // Xóa LocalStorage
  try {
    let local = JSON.parse(localStorage.getItem('olion_feedbacks') || '[]');
    local = local.filter(f => f.id !== id);
    localStorage.setItem('olion_feedbacks', JSON.stringify(local));
  } catch (e) {}

  if (client) {
    try {
      const { error } = await client
        .from('feedbacks')
        .delete()
        .eq('id', id);

      if (error) throw error;
      return { success: true, source: 'supabase' };
    } catch (err) {
      console.warn('⚠️ [Supabase Admin] Lỗi delete feedback:', err.message);
      return { success: false, error: err.message };
    }
  }
  return { success: true, source: 'local' };
}

/**
 * 7. Lấy lịch sử quay Minigame cho trang Admin (Admin Portal)
 */
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

  // Fallback từ LocalStorage
  const customers = JSON.parse(localStorage.getItem('olion_customers') || '[]');
  const minigameLeads = customers.filter(c => (c.source || '').includes('Minigame'));
  return { source: 'local', data: minigameLeads };
}

/**
 * 8. Lấy danh sách Khách Hàng / Leads cho trang Admin (Admin Portal)
 */
async function fetchCustomersFromCloud() {
  const client = supabaseClient || initSupabase();

  if (client) {
    try {
      const { data, error } = await client
        .from('customers')
        .select('*')
        .order('created_at', { ascending: false })
        .limit(200);

      if (!error && data) {
        return {
          source: 'supabase',
          data: data.map(c => ({
            id: c.id,
            name: c.name || 'Khách hàng',
            contact: c.contact,
            source: c.source || 'Website',
            date: c.created_at ? new Date(c.created_at).toLocaleString('vi-VN') : 'Gần đây'
          }))
        };
      }
    } catch (err) {
      console.warn('⚠️ [Supabase Admin] Lỗi tải customers:', err.message);
    }
  }

  // Fallback LocalStorage
  const customers = JSON.parse(localStorage.getItem('olion_customers') || '[]');
  return { source: 'local', data: customers };
}

/**
 * 9. Xóa khách hàng (Admin Portal)
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
