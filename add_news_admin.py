import re

with open('admin.html', 'r') as f:
    html = f.read()

# Add nav-item
nav_item = """
        <div class="nav-item" data-tab="news">
          <span class="nav-icon">📰</span>
          <span class="nav-text">Tin tức & Sự kiện</span>
        </div>"""
html = html.replace('<div class="nav-item" data-tab="promotions">', nav_item + '\n        <div class="nav-item" data-tab="promotions">')

# Add tab-pane
tab_pane = """
        <!-- TAB: NEWS -->
        <section class="tab-content" id="tab-news">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
            <p style="color: var(--text-muted);">Quản lý các bài viết trên trang chủ và trang Tin Tức. Dữ liệu được đồng bộ trực tiếp lên Cloud.</p>
            <button class="btn btn-primary" onclick="openNewsFormModal()">+ Viết bài mới</button>
          </div>
          <div class="card">
            <div style="overflow-x: auto;">
              <table class="table">
                <thead>
                  <tr>
                    <th>Ảnh Bìa</th>
                    <th>Tiêu Đề</th>
                    <th>Ngày Đăng</th>
                    <th>Danh Mục</th>
                    <th>Nổi Bật</th>
                    <th>Thao Tác</th>
                  </tr>
                </thead>
                <tbody id="newsTableBody">
                  <tr><td colspan="6" style="text-align: center; color: var(--text-muted); padding: 25px;">Chưa kết nối CSDL Supabase</td></tr>
                </tbody>
              </table>
            </div>
          </div>
        </section>
"""

html = html.replace('<section class="tab-content" id="tab-promotions">', tab_pane + '\n        <section class="tab-content" id="tab-promotions">')

# Add Modal for adding/editing news
modal_html = """
  <!-- NEWS FORM MODAL -->
  <div class="modal-overlay" id="newsFormModal">
    <div class="modal-content" style="max-width: 700px;">
      <h2 style="margin-bottom: 20px;" id="newsFormTitle">Thêm bài viết mới</h2>
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-bottom: 15px;">
        <div>
          <label style="display: block; margin-bottom: 5px; color: var(--text-muted);">Tiêu đề bài viết</label>
          <input type="text" id="newsFormInputTitle" style="width: 100%; padding: 10px; border-radius: 8px; border: 1px solid var(--border-dark); background: var(--bg-dark); color: white;" placeholder="VD: Khai trương cơ sở mới">
        </div>
        <div>
          <label style="display: block; margin-bottom: 5px; color: var(--text-muted);">Danh mục</label>
          <input type="text" id="newsFormInputCategory" style="width: 100%; padding: 10px; border-radius: 8px; border: 1px solid var(--border-dark); background: var(--bg-dark); color: white;" placeholder="VD: Sự kiện đặc biệt">
        </div>
        <div>
          <label style="display: block; margin-bottom: 5px; color: var(--text-muted);">Ngày đăng</label>
          <input type="text" id="newsFormInputDate" style="width: 100%; padding: 10px; border-radius: 8px; border: 1px solid var(--border-dark); background: var(--bg-dark); color: white;" placeholder="VD: 19/09/2026">
        </div>
        <div>
          <label style="display: block; margin-bottom: 5px; color: var(--text-muted);">Ảnh bìa (URL)</label>
          <input type="text" id="newsFormInputImage" style="width: 100%; padding: 10px; border-radius: 8px; border: 1px solid var(--border-dark); background: var(--bg-dark); color: white;" placeholder="VD: assets/news/news-1.webp">
        </div>
      </div>
      
      <div style="margin-bottom: 15px;">
        <label style="display: block; margin-bottom: 5px; color: var(--text-muted);">Đoạn mô tả ngắn (Hiển thị trên danh sách)</label>
        <textarea id="newsFormInputDesc" style="width: 100%; padding: 10px; border-radius: 8px; border: 1px solid var(--border-dark); background: var(--bg-dark); color: white; min-height: 60px;" placeholder="Tóm tắt ngắn gọn bài viết..."></textarea>
      </div>

      <div style="margin-bottom: 15px;">
        <label style="display: block; margin-bottom: 5px; color: var(--text-muted);">Nội dung bài viết (Hỗ trợ HTML: <p>, <strong>, vv)</label>
        <textarea id="newsFormInputContent" style="width: 100%; padding: 10px; border-radius: 8px; border: 1px solid var(--border-dark); background: var(--bg-dark); color: white; min-height: 150px;" placeholder="<p>Nội dung chi tiết...</p>"></textarea>
      </div>

      <div style="margin-bottom: 25px; display: flex; align-items: center; gap: 10px;">
        <input type="checkbox" id="newsFormInputFeatured" style="width: 18px; height: 18px;">
        <label for="newsFormInputFeatured" style="color: var(--text-white);">⭐ Đánh dấu là bài viết Nổi Bật (Sẽ ghim lên Trang Chủ)</label>
      </div>

      <div style="display: flex; justify-content: flex-end; gap: 10px;">
        <button class="btn btn-secondary" onclick="closeNewsFormModal()">Hủy</button>
        <button class="btn btn-primary" onclick="saveNewsArticle()">Lưu Bài Viết</button>
      </div>
    </div>
  </div>
"""

html = html.replace('<!-- SUPABASE SETUP MODAL -->', modal_html + '\n  <!-- SUPABASE SETUP MODAL -->')

# Add Tab title logic
title_map = """      news: '📰 Quản lý Tin tức & Sự kiện',"""
html = html.replace("promotions: '🎁 Chương trình ưu đãi',", title_map + "\n      promotions: '🎁 Chương trình ưu đãi',")

# Add JS logic for News CRUD
js_news = """
    // ==========================================
    // QUẢN LÝ TIN TỨC (NEWS CRUD)
    // ==========================================
    let cachedNewsItems = [];
    let editingNewsId = null;

    async function loadNewsFromCloud() {
      if (!isSupabaseConfigured()) {
        document.getElementById('newsTableBody').innerHTML = '<tr><td colspan="6" style="text-align: center; color: var(--text-muted); padding: 25px;">Chưa cấu hình Supabase. Vui lòng vào tab Cơ sở dữ liệu Cloud.</td></tr>';
        return;
      }
      try {
        const { data, error } = await _supabase.from('news_items').select('*').order('created_at', { ascending: false });
        if (error) throw error;
        cachedNewsItems = data || [];
        renderNewsTable();
      } catch (e) {
        console.error("Lỗi tải tin tức:", e);
      }
    }

    function renderNewsTable() {
      const tbody = document.getElementById('newsTableBody');
      if (cachedNewsItems.length === 0) {
        tbody.innerHTML = '<tr><td colspan="6" style="text-align: center; color: var(--text-muted); padding: 25px;">Chưa có bài viết nào.</td></tr>';
        return;
      }
      
      tbody.innerHTML = cachedNewsItems.map(item => `
        <tr>
          <td><img src="${item.cover_image}" style="width: 50px; height: 40px; border-radius: 4px; object-fit: cover;"></td>
          <td style="font-weight: 500;">${item.title}</td>
          <td>${item.date}</td>
          <td><span style="background: rgba(229,154,85,0.1); color: var(--accent-gold); padding: 4px 8px; border-radius: 4px; font-size: 12px;">${item.category}</span></td>
          <td>${item.is_featured ? '⭐ Nổi bật' : ''}</td>
          <td>
            <button class="btn btn-secondary" style="padding: 6px 12px; font-size: 12px; margin-right: 5px;" onclick="editNews('${item.id}')">Sửa</button>
            <button class="btn btn-secondary" style="padding: 6px 12px; font-size: 12px; color: #ff4757;" onclick="deleteNews('${item.id}')">Xóa</button>
          </td>
        </tr>
      `).join('');
    }

    function openNewsFormModal() {
      editingNewsId = null;
      document.getElementById('newsFormTitle').textContent = 'Thêm bài viết mới';
      document.getElementById('newsFormInputTitle').value = '';
      document.getElementById('newsFormInputCategory').value = '';
      
      const today = new Date();
      const dd = String(today.getDate()).padStart(2, '0');
      const mm = String(today.getMonth() + 1).padStart(2, '0');
      const yyyy = today.getFullYear();
      document.getElementById('newsFormInputDate').value = `${dd}/${mm}/${yyyy}`;
      
      document.getElementById('newsFormInputImage').value = '';
      document.getElementById('newsFormInputDesc').value = '';
      document.getElementById('newsFormInputContent').value = '';
      document.getElementById('newsFormInputFeatured').checked = false;
      document.getElementById('newsFormModal').classList.add('open');
    }

    function closeNewsFormModal() {
      document.getElementById('newsFormModal').classList.remove('open');
    }

    function editNews(id) {
      const item = cachedNewsItems.find(i => i.id === id);
      if(!item) return;
      editingNewsId = id;
      document.getElementById('newsFormTitle').textContent = 'Chỉnh sửa bài viết';
      document.getElementById('newsFormInputTitle').value = item.title;
      document.getElementById('newsFormInputCategory').value = item.category;
      document.getElementById('newsFormInputDate').value = item.date;
      document.getElementById('newsFormInputImage').value = item.cover_image;
      document.getElementById('newsFormInputDesc').value = item.description || '';
      document.getElementById('newsFormInputContent').value = item.content_html || '';
      document.getElementById('newsFormInputFeatured').checked = item.is_featured;
      document.getElementById('newsFormModal').classList.add('open');
    }

    async function saveNewsArticle() {
      if (!isSupabaseConfigured()) return alert('Chưa kết nối Supabase!');
      
      const title = document.getElementById('newsFormInputTitle').value.trim();
      const category = document.getElementById('newsFormInputCategory').value.trim();
      const date = document.getElementById('newsFormInputDate').value.trim();
      const cover_image = document.getElementById('newsFormInputImage').value.trim() || 'assets/logo-white.webp';
      const description = document.getElementById('newsFormInputDesc').value.trim();
      const content_html = document.getElementById('newsFormInputContent').value.trim();
      const is_featured = document.getElementById('newsFormInputFeatured').checked;
      
      if (!title || !category || !date) return alert('Vui lòng điền đủ Tiêu đề, Danh mục và Ngày đăng!');
      
      const payload = { title, category, date, cover_image, description, content_html, is_featured };
      
      try {
        if (editingNewsId) {
          const { error } = await _supabase.from('news_items').update(payload).eq('id', editingNewsId);
          if (error) throw error;
          showToast('Đã cập nhật bài viết thành công!');
        } else {
          const { error } = await _supabase.from('news_items').insert([payload]);
          if (error) throw error;
          showToast('Đã thêm bài viết thành công!');
        }
        closeNewsFormModal();
        loadNewsFromCloud();
      } catch (e) {
        alert('Lỗi lưu bài viết: ' + e.message);
      }
    }

    async function deleteNews(id) {
      if(!confirm('Bạn có chắc chắn muốn xóa bài viết này không?')) return;
      if (!isSupabaseConfigured()) return;
      try {
        const { error } = await _supabase.from('news_items').delete().eq('id', id);
        if (error) throw error;
        showToast('Đã xóa bài viết!');
        loadNewsFromCloud();
      } catch(e) {
        alert('Lỗi: ' + e.message);
      }
    }
"""

html = html.replace('// --- LOYALTY LOGIC ---', js_news + '\n    // --- LOYALTY LOGIC ---')

# also call loadNewsFromCloud when initialized
if 'loadMenu();' in html:
    html = html.replace('loadMenu();', 'loadMenu();\n          loadNewsFromCloud();')


with open('admin.html', 'w') as f:
    f.write(html)

