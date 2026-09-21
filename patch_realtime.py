with open('index.html', 'r') as f:
    c = f.read()

realtime_code = """      syncMenuFromCloud();
      syncApprovedReviews();

      // H. Supabase Realtime Subscription
      if (typeof supabaseClient !== 'undefined' && supabaseClient) {
        supabaseClient
          .channel('public:menu_items')
          .on('postgres_changes', { event: '*', schema: 'public', table: 'menu_items' }, payload => {
            console.log('🔄 Menu changed via Realtime!', payload);
            syncMenuFromCloud();
          })
          .on('postgres_changes', { event: '*', schema: 'public', table: 'feedbacks' }, payload => {
            syncApprovedReviews();
          })
          .subscribe((status) => {
             console.log('Realtime status:', status);
          });
      }
"""
c = c.replace("      syncMenuFromCloud();\n      syncApprovedReviews();\n", realtime_code)

with open('index.html', 'w') as f:
    f.write(c)

