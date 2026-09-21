import re

with open('admin.html', 'r') as f:
    c = f.read()

# Modify loadMinigame and loadAnnouncement
new_load_logic = """
    async function loadMinigame() {
      if (typeof fetchSiteSettingsFromCloud === 'function') {
        const { data } = await fetchSiteSettingsFromCloud();
        if (data) {
          if (minigameToggle) minigameToggle.checked = data.is_wheel_active !== false;
          if (data.wheel_prizes && Array.isArray(data.wheel_prizes) && data.wheel_prizes.length >= 2) {
            currentPrizes = data.wheel_prizes.map(p => ({...p}));
          }
          if (document.getElementById('announcementEnableToggle')) document.getElementById('announcementEnableToggle').checked = !!data.is_notification_active;
          if (document.getElementById('announcementTextInput')) document.getElementById('announcementTextInput').value = data.notification_text || '';
        }
      }
      renderPrizeRows();

      const tbody = document.getElementById('minigameLeadsTable');
      tbody.innerHTML = '<tr><td colspan="4" style="text-align: center; color: var(--text-muted); padding: 15px;">⏳ Đang tải...</td></tr>';
      const res = await fetchLuckySpinsFromCloud();
      cachedSpins = res.data || [];
      tbody.innerHTML = '';
      if (cachedSpins.length === 0) {
        tbody.innerHTML = `<tr><td colspan="4" style="text-align: center; color: var(--text-muted); padding: 20px;">Chưa có lượt quay nào</td></tr>`;
      } else {
        cachedSpins.forEach(spin => {
          tbody.innerHTML += `
            <tr style="border-bottom:1px solid rgba(255,255,255,0.05);">
              <td style="padding:12px;color:#fff;">${escapeHtml(spin.customer_name || 'Khách ẩn danh')}</td>
              <td style="padding:12px;color:#E59A55;">${escapeHtml(spin.customer_phone)}</td>
              <td style="padding:12px;color:#2ECC71;">${escapeHtml(spin.prize_name)}</td>
              <td style="padding:12px;color:var(--text-muted);font-size:12.5px;">${new Date(spin.created_at).toLocaleString('vi-VN')}</td>
            </tr>
          `;
        });
      }
    }

    document.getElementById('saveMinigameBtn').addEventListener('click', async () => {
      const is_wheel_active = minigameToggle ? minigameToggle.checked : true;
      if (currentPrizes.length < 2) { showToast('Cần ít nhất 2 ô quà!'); return; }
      
      const btn = document.getElementById('saveMinigameBtn');
      btn.textContent = 'Đang lưu...';
      if (typeof updateSiteSettingsToCloud === 'function') {
        await updateSiteSettingsToCloud({ is_wheel_active, wheel_prizes: currentPrizes });
      }
      btn.textContent = 'Lưu cấu hình';
      showToast('✅ Đã lưu cấu hình Minigame lên Supabase!');
    });

    document.getElementById('saveAnnouncementBtn').addEventListener('click', async () => {
      const is_notification_active = document.getElementById('announcementEnableToggle').checked;
      const notification_text = document.getElementById('announcementTextInput').value.trim();
      
      const btn = document.getElementById('saveAnnouncementBtn');
      btn.textContent = 'Đang lưu...';
      if (typeof updateSiteSettingsToCloud === 'function') {
        await updateSiteSettingsToCloud({ is_notification_active, notification_text });
      }
      btn.textContent = 'Lưu thông báo';
      showToast('Đã cập nhật thông báo lên Supabase thành công!');
    });
"""

c = re.sub(r'    async function loadMinigame\(\) \{.*?showToast\(\'Đã cập nhật thông báo lên website thành công!\'\);\n    \}\);', new_load_logic, c, flags=re.DOTALL)

with open('admin.html', 'w') as f:
    f.write(c)
