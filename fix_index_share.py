import re

with open('index.html', 'r') as f:
    html = f.read()

share_html = """      <div style="margin-top: 24px; padding-top: 20px; border-top: 1px solid rgba(255,255,255,0.1); display: flex; justify-content: space-between; align-items: center;">
        <span style="color: var(--text-muted); font-size: 14px;">Chia sẻ bài viết này:</span>
        <div style="display: flex; gap: 12px;">
          <button onclick="shareToFB()" style="background: #1877F2; border: none; width: 36px; height: 36px; border-radius: 50%; color: white; cursor: pointer; display: flex; align-items: center; justify-content: center;"><i data-lucide="facebook" style="width: 18px; height: 18px;"></i></button>
          <button onclick="copyLink()" style="background: #E59A55; border: none; width: 36px; height: 36px; border-radius: 50%; color: white; cursor: pointer; display: flex; align-items: center; justify-content: center;"><i data-lucide="link" style="width: 18px; height: 18px;"></i></button>
        </div>
      </div>
"""

# inject share buttons into news modal
# The news modal ends with:
#       <div id="newsModalBody" class="news-modal-body"></div>
#     </div>
#   </div>
# </div>
if 'shareToFB()' not in html:
    html = html.replace('<div id="newsModalBody" class="news-modal-body"></div>\n    </div>\n  </div>\n</div>', f'<div id="newsModalBody" class="news-modal-body"></div>\n{share_html}    </div>\n  </div>\n</div>')

# also inject the JS functions
js_code = """
  let currentNewsId = '';
  const originalOpenNewsModal = openNewsModal;
  window.openNewsModal = function(id) {
    currentNewsId = id;
    originalOpenNewsModal(id);
  };

  function shareToFB() {
    const url = encodeURIComponent(window.location.origin + "/news?article=" + currentNewsId);
    window.open(`https://www.facebook.com/sharer/sharer.php?u=${url}`, '_blank', 'width=600,height=400');
  }

  function copyLink() {
    const url = window.location.origin + "/news?article=" + currentNewsId;
    navigator.clipboard.writeText(url).then(() => {
      alert("Đã sao chép đường link bài viết!");
    });
  }
</script>"""
if 'function shareToFB()' not in html:
    html = html.replace('</script>', js_code + '\n</script>', 1)

with open('index.html', 'w') as f:
    f.write(html)

