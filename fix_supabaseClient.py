import re

with open('supabaseClient.js', 'r') as f:
    c = f.read()

settings_js = """
// =======================================================
// SITE SETTINGS (ANNOUNCEMENT & WHEEL TOGGLE)
// =======================================================
async function fetchSiteSettingsFromCloud() {
  const client = supabaseClient || initSupabase();
  if (!client) return { error: 'No client' };
  try {
    const { data, error } = await client.from('site_settings').select('*').eq('id', 1).single();
    if (error) return { error };
    return { data };
  } catch (err) {
    return { error: err };
  }
}

async function updateSiteSettingsToCloud(updates) {
  const client = supabaseClient || initSupabase();
  if (!client) return { error: 'No client' };
  try {
    const { data, error } = await client.from('site_settings').update(updates).eq('id', 1).select();
    if (error) return { error };
    return { data };
  } catch (err) {
    return { error: err };
  }
}
"""

c = c + '\n' + settings_js

with open('supabaseClient.js', 'w') as f:
    f.write(c)
