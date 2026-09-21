import re

with open('supabaseClient.js', 'r') as f:
    c = f.read()

realtime_code = """
// =======================================================
// REALTIME SUBSCRIPTIONS (ADMIN ONLY)
// =======================================================
function setupAdminRealtime() {
  const client = supabaseClient || initSupabase();
  if (!client) return;
  
  client
    .channel('admin-feedbacks')
    .on('postgres_changes', { event: 'INSERT', schema: 'public', table: 'feedbacks' }, payload => {
      console.log('New feedback:', payload.new);
      if (typeof showToast === 'function') showToast('🔔 Có góp ý mới từ khách hàng!');
      if (typeof loadFeedbacks === 'function') loadFeedbacks();
    })
    .on('postgres_changes', { event: 'INSERT', schema: 'public', table: 'lucky_spins' }, payload => {
      console.log('New lucky spin:', payload.new);
      if (typeof showToast === 'function') showToast('🎁 Khách hàng vừa quay trúng thưởng!');
      if (typeof loadMinigame === 'function') loadMinigame();
    })
    .subscribe();
}
"""

c = c + '\n' + realtime_code

with open('supabaseClient.js', 'w') as f:
    f.write(c)

with open('admin.html', 'r') as f:
    html = f.read()

# Add to loadAllData
html = html.replace('function loadAllData() {', 'function loadAllData() {\n      if (typeof setupAdminRealtime === \'function\') setupAdminRealtime();')

with open('admin.html', 'w') as f:
    f.write(html)
