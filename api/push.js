export default async function handler(req, res) {
  // CORS setup
  res.setHeader('Access-Control-Allow-Credentials', 'true');
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET,OPTIONS,PATCH,DELETE,POST,PUT');
  res.setHeader(
    'Access-Control-Allow-Headers',
    'X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version, Authorization'
  );

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  // 1. Resolve Authorization Header & API Key
  const rawAuth = req.headers.authorization || (req.body && req.body.api_key) || (req.query && req.query.api_key) || process.env.ONESIGNAL_REST_API_KEY;
  if (!rawAuth) {
    return res.status(401).json({
      success: false,
      error: 'Missing API Key',
      message: 'Chưa có OneSignal REST API Key. Vui lòng cấu hình trong Admin hoặc đặt biến môi trường ONESIGNAL_REST_API_KEY trên Vercel.'
    });
  }

  // Clean key: strip redundant Basic/Key prefixes and whitespaces
  let cleanKey = String(rawAuth).trim();
  while (/^(Basic|Key)\s+/i.test(cleanKey)) {
    cleanKey = cleanKey.replace(/^(Basic|Key)\s+/i, '').trim();
  }
  const authHeader = `Basic ${cleanKey}`;

  // 2. Resolve OneSignal App ID
  const appId = (req.body && req.body.app_id) || (req.query && req.query.app_id) || process.env.ONESIGNAL_APP_ID || "09a8fa7b-6ea9-40b7-b5d5-25dd2ffed24b";

  // 3. ACTION: Test Connection
  const isTestAction = (req.query && req.query.action === 'test') || (req.body && req.body.action === 'test');
  if (isTestAction || req.method === 'GET') {
    try {
      const checkRes = await fetch(`https://api.onesignal.com/apps/${encodeURIComponent(appId)}`, {
        method: 'GET',
        headers: {
          'Authorization': authHeader,
          'Accept': 'application/json'
        }
      });

      const checkData = await checkRes.json();
      if (!checkRes.ok) {
        if (checkRes.status === 401) {
          return res.status(401).json({
            success: false,
            status: 401,
            error: 'OneSignal Auth Failed',
            message: 'REST API Key không chính xác hoặc đã bị thu hồi. Vui lòng kiểm tra lại trong OneSignal Settings > Keys & IDs.'
          });
        }
        if (checkRes.status === 404) {
          return res.status(404).json({
            success: false,
            status: 404,
            error: 'App Not Found',
            message: `Không tìm thấy OneSignal App ID "${appId}". Vui lòng kiểm tra lại App ID.`
          });
        }
        return res.status(checkRes.status).json({
          success: false,
          status: checkRes.status,
          error: 'OneSignal API Error',
          details: checkData
        });
      }

      return res.status(200).json({
        success: true,
        app_id: appId,
        app_name: checkData.name || 'Olion Coffee',
        players: checkData.players || 0,
        messageable_players: checkData.messageable_players || 0,
        message: `Kết nối OneSignal thành công! Ứng dụng "${checkData.name}" hiện có ${checkData.messageable_players || 0} thiết bị sẵn sàng nhận tin.`
      });
    } catch (err) {
      return res.status(500).json({
        success: false,
        error: 'Network Error',
        message: 'Không thể kết nối đến OneSignal API: ' + err.message
      });
    }
  }

  // 4. ACTION: Send Notification (POST)
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method Not Allowed' });
  }

  try {
    const body = req.body || {};
    const title = body.title || (body.headings && (body.headings.vi || body.headings.en)) || 'Thông báo từ Olion Coffee';
    const message = body.message || (body.contents && (body.contents.vi || body.contents.en)) || '';
    const url = body.url || 'https://www.olioncoffee.app';

    if (!message && !body.contents) {
      return res.status(400).json({
        success: false,
        error: 'Missing Content',
        message: 'Nội dung thông báo không được để trống.'
      });
    }

    const payload = {
      app_id: appId,
      included_segments: body.included_segments || ['Subscribed Users'],
      headings: body.headings || { "en": title, "vi": title },
      contents: body.contents || { "en": message, "vi": message },
      url: url
    };

    if (body.big_picture) payload.big_picture = body.big_picture;
    if (body.chrome_web_image) payload.chrome_web_image = body.chrome_web_image;
    if (body.ios_attachments) payload.ios_attachments = body.ios_attachments;

    const response = await fetch('https://api.onesignal.com/notifications', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': authHeader
      },
      body: JSON.stringify(payload)
    });

    const data = await response.json();

    // Check for "no subscribed players" special case
    if (!response.ok) {
      const errorStr = JSON.stringify(data);
      if (errorStr.includes('not subscribed') || errorStr.includes('All included players are not subscribed')) {
        return res.status(200).json({
          success: true,
          warning: 'NO_SUBSCRIBERS',
          recipients: 0,
          data: data,
          message: 'Lệnh gửi thành công nhưng hiện tại chưa có khách hàng nào đăng ký nhận thông báo trên website (0 subscribers).'
        });
      }

      return res.status(response.status).json({
        success: false,
        status: response.status,
        error: 'OneSignal API Error',
        details: data,
        message: (data && data.errors && data.errors[0]) || 'Gửi thông báo thất bại từ OneSignal API'
      });
    }

    const recipients = data.recipients || 0;
    return res.status(200).json({
      success: true,
      recipients: recipients,
      id: data.id,
      data: data,
      message: recipients > 0 
        ? `Đã gửi thông báo thành công đến ${recipients} thiết bị!`
        : 'Lệnh gửi đã phát đi, hiện có 0 thiết bị kích hoạt nhận tin.'
    });

  } catch (error) {
    return res.status(500).json({
      success: false,
      error: 'Internal Server Error',
      message: error.message
    });
  }
}
