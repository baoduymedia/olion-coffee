import re

with open('admin.html', 'r') as f:
    c = f.read()

js_html = """    async function restoreDefaultMenu() {
      if (!confirm('Hành động này sẽ XÓA TOÀN BỘ menu hiện tại trên Supabase Cloud và khôi phục lại 39 món mặc định mới nhất. Bạn có chắc chắn?')) return;
      
      try {
        if (!supabaseClient) throw new Error('Chưa kết nối Supabase!');
        
        // Delete all
        const { error: delErr } = await supabaseClient.from('menu_items').delete().neq('id', 0);
        if (delErr) throw delErr;
        
        // Insert defaults
        const { error: insErr } = await supabaseClient.from('menu_items').insert(DEFAULT_MENU_ITEMS);
        if (insErr) throw insErr;
        
        showToast('Đã khôi phục Menu gốc thành công!', 'success');
        if (typeof fetchMenuAdmin === 'function') fetchMenuAdmin();
      } catch (e) {
        showToast('Lỗi khôi phục: ' + e.message, 'error');
      }
    }
"""

c = re.sub(r'(</script>\s*</body>)', js_html + r'\1', c)

with open('admin.html', 'w') as f:
    f.write(c)

