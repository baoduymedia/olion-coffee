-- ==============================================================================
-- OLION COFFEE - WEBSITE STATUS & MAINTENANCE SWITCH (KILL-SWITCH MIGRATION)
-- Copy và dán toàn bộ đoạn mã này vào Supabase Dashboard -> SQL Editor -> Run
-- ==============================================================================

-- 1. Thêm các cột quản lý trạng thái Tắt/Bật và Chế độ bảo trì vào bảng site_settings
ALTER TABLE public.site_settings 
ADD COLUMN IF NOT EXISTS is_site_online BOOLEAN DEFAULT true,
ADD COLUMN IF NOT EXISTS maintenance_title TEXT DEFAULT 'Olion Coffee Tạm Đóng Cửa Để Nâng Cấp Dịch Vụ',
ADD COLUMN IF NOT EXISTS maintenance_message TEXT DEFAULT 'Hệ thống website đang tạm ngưng phục vụ để bảo trì & nâng cấp trải nghiệm tốt nhất cho quý khách. Rất mong quý khách thông cảm và hẹn sớm gặp lại!',
ADD COLUMN IF NOT EXISTS maintenance_expected_time TEXT DEFAULT 'Dự kiến mở lại: Sớm nhất',
ADD COLUMN IF NOT EXISTS maintenance_hotline TEXT DEFAULT '0783 657 587',
ADD COLUMN IF NOT EXISTS maintenance_updated_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now());

-- 2. Đảm bảo bản ghi id=1 luôn có giá trị mặc định là Online (true)
UPDATE public.site_settings 
SET 
  is_site_online = COALESCE(is_site_online, true),
  maintenance_title = COALESCE(maintenance_title, 'Olion Coffee Tạm Đóng Cửa Để Nâng Cấp Dịch Vụ'),
  maintenance_message = COALESCE(maintenance_message, 'Hệ thống website đang tạm ngưng phục vụ để bảo trì & nâng cấp trải nghiệm tốt nhất cho quý khách. Rất mong quý khách thông cảm và hẹn sớm gặp lại!'),
  maintenance_expected_time = COALESCE(maintenance_expected_time, 'Dự kiến mở lại: Sớm nhất'),
  maintenance_hotline = COALESCE(maintenance_hotline, '0783 657 587')
WHERE id = 1;
