import re

with open('index.html', 'r') as f:
    c = f.read()

# Replace local minigame and announcement config with fetchSiteSettings
new_logic = """
      async function applySiteSettings() {
        if (typeof fetchSiteSettingsFromCloud === 'function') {
          const { data } = await fetchSiteSettingsFromCloud();
          if (data) {
            // Minigame Wheel
            const floatBtn = document.getElementById('wheelFloatBtn');
            if (floatBtn) {
              if (data.is_wheel_active === false) {
                floatBtn.style.setProperty('display', 'none', 'important');
              } else {
                floatBtn.style.setProperty('display', 'inline-flex', 'important');
              }
            }
            if (data.wheel_prizes && Array.isArray(data.wheel_prizes) && data.wheel_prizes.length >= 2) {
              prizes = data.wheel_prizes;
            }

            // Announcement Banner
            const topBanner = document.getElementById('topAnnouncement');
            if (topBanner) {
              if (data.is_notification_active === false) {
                topBanner.style.setProperty('display', 'none', 'important');
                document.documentElement.style.setProperty('--announcement-h', '0px');
              } else {
                topBanner.style.setProperty('display', 'flex', 'important');
                document.documentElement.style.setProperty('--announcement-h', '40px');
                if (data.notification_text) {
                  const textEl = topBanner.querySelector('.announcement-text');
                  if (textEl) textEl.textContent = data.notification_text;
                }
              }
            }
          }
        }
      }
      
      applySiteSettings();
"""

c = re.sub(r'      function applyMinigameConfig\(\) \{.*?if \(rawText\) topBanner.querySelector\(\'\.announcement-text\'\)\.textContent = rawText;\n        \} catch\(e\) \{\}\n      \}\n      applyAnnouncementConfig\(\);', new_logic, c, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(c)
