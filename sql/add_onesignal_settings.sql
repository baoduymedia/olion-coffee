-- ==============================================================================
-- OLION COFFEE - ONESIGNAL & SHARE EARN SETTINGS MIGRATION
-- Copy và dán toàn bộ đoạn mã này vào Supabase Dashboard -> SQL Editor -> Run
-- ==============================================================================

-- 1. Thêm các cột lưu trữ cấu hình OneSignal & Tính năng Chia Sẻ
ALTER TABLE public.site_settings 
ADD COLUMN IF NOT EXISTS onesignal_api_key TEXT,
ADD COLUMN IF NOT EXISTS onesignal_app_id TEXT DEFAULT '09a8fa7b-6ea9-40b7-b5d5-25dd2ffed24b',
ADD COLUMN IF NOT EXISTS is_share_earn_active BOOLEAN DEFAULT false,
ADD COLUMN IF NOT EXISTS share_earn_settings JSONB;

-- 2. Đảm bảo bản ghi id=1 có sẵn App ID mặc định
UPDATE public.site_settings 
SET onesignal_app_id = COALESCE(onesignal_app_id, '09a8fa7b-6ea9-40b7-b5d5-25dd2ffed24b')
WHERE id = 1;
