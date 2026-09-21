import re

with open('supabaseClient.js', 'r') as f:
    c = f.read()

old_insert = """      await client.from('lucky_spins').insert([{
        customer_name: spinData.customer_name || 'Khách quay minigame',
        customer_phone: spinData.customer_phone,
        prize_name: spinData.prize_name,
        promo_code: spinData.promo_code,
        device_id: deviceId
      }]);"""

new_insert = """      const { data, error } = await client.from('lucky_spins').insert([{
        customer_name: spinData.customer_name || 'Khách quay minigame',
        customer_phone: spinData.customer_phone,
        prize_name: spinData.prize_name,
        promo_code: spinData.promo_code,
        device_id: deviceId
      }]).select('*');
      if (!error && data && data.length > 0) return data[0];"""

c = c.replace(old_insert, new_insert)

# Add fallback return
old_fallback = """      console.error('Supabase error inserting spin:', err);
    }
  }
}"""
new_fallback = """      console.error('Supabase error inserting spin:', err);
    }
  }
  return { id: 'LOCAL-' + Date.now(), ...spinData };
}"""

c = c.replace(old_fallback, new_fallback)

# Update markSpinAsUsed
c += """
// =======================================================
// MARK SPIN AS USED (E-VOUCHER)
// =======================================================
async function markSpinAsUsed(spinId) {
  const client = supabaseClient || initSupabase();
  if (!client) return { error: 'No client' };
  try {
    const { data, error } = await client.from('lucky_spins').update({ status: 'used' }).eq('id', spinId).select();
    if (error) return { error };
    return { data };
  } catch (err) {
    return { error: err };
  }
}

async function getSpinDetails(spinId) {
  const client = supabaseClient || initSupabase();
  if (!client) return { error: 'No client' };
  try {
    const { data, error } = await client.from('lucky_spins').select('*').eq('id', spinId).single();
    if (error) return { error };
    return { data };
  } catch (err) {
    return { error: err };
  }
}
"""

with open('supabaseClient.js', 'w') as f:
    f.write(c)
