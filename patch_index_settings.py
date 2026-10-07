import re

with open('index.html', 'r') as f:
    c = f.read()

sync_func = """
      async function syncSiteSettingsFromCloud() {
        if (typeof fetchSiteSettingsFromCloud !== 'function') return;
        const res = await fetchSiteSettingsFromCloud();
        if (res.data) {
           const s = res.data;
           
           // 1. Minigame Wheel
           const floatBtn = document.getElementById('wheelFloatBtn');
           if (floatBtn) {
             if (s.is_wheel_active === false) {
               floatBtn.style.setProperty('display', 'none', 'important');
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
           
           // 2. Announcement Banner
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
"""

# Inject before Initial Sync Calls
c = c.replace('// Initial Sync Calls', sync_func + '\n      // Initial Sync Calls')

# Add to Initial Sync Calls
c = c.replace('applyMinigameConfig();', 'applyMinigameConfig();\n      syncSiteSettingsFromCloud();')

# Add to Realtime
c = c.replace("table: 'feedbacks' }, payload => {", "table: 'feedbacks' }, payload => {\n            syncApprovedReviews();\n          })\n          .on('postgres_changes', { event: '*', schema: 'public', table: 'site_settings' }, payload => {\n            console.log('🔄 Site settings changed via Realtime!', payload);\n            syncSiteSettingsFromCloud();\n          })")

# Clean up duplicate syncApprovedReviews if I accidentally double-injected it
c = c.replace("syncApprovedReviews();\n          })\n          .on('postgres_changes', { event: '*', schema: 'public', table: 'site_settings' }, payload => {\n            console.log('🔄 Site settings changed via Realtime!', payload);\n            syncSiteSettingsFromCloud();\n          })\n            syncApprovedReviews();\n          })", "syncApprovedReviews();\n          })\n          .on('postgres_changes', { event: '*', schema: 'public', table: 'site_settings' }, payload => {\n            console.log('🔄 Site settings changed via Realtime!', payload);\n            syncSiteSettingsFromCloud();\n          })")

with open('index.html', 'w') as f:
    f.write(c)

