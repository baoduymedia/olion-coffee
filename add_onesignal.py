import re

with open('index.html', 'r') as f:
    c = f.read()

onesignal_script = """
  <!-- OneSignal Push Notifications (Placeholder) -->
  <script src="https://cdn.onesignal.com/sdks/web/v16/OneSignalSDK.page.js" defer></script>
  <script>
    window.OneSignalDeferred = window.OneSignalDeferred || [];
    OneSignalDeferred.push(function(OneSignal) {
      OneSignal.init({
        appId: "YOUR-ONESIGNAL-APP-ID",
      });
    });
  </script>
"""

c = c.replace('</head>', onesignal_script + '</head>')

with open('index.html', 'w') as f:
    f.write(c)
