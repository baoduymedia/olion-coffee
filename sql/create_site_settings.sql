-- 1. Create site_settings table
CREATE TABLE public.site_settings (
  id INT PRIMARY KEY DEFAULT 1,
  is_wheel_active BOOLEAN DEFAULT true,
  is_notification_active BOOLEAN DEFAULT true,
  notification_text TEXT,
  wheel_prizes JSONB,
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now())
);

-- 2. Insert default row (Single-row pattern)
INSERT INTO public.site_settings (id, is_wheel_active, is_notification_active, notification_text)
VALUES (1, true, true, '🔥 ƯU ĐÃI KHAI TRƯƠNG: Giảm 20% toàn bộ Menu đến 31/10 🔥')
ON CONFLICT (id) DO NOTHING;

-- 3. Enable RLS
ALTER TABLE public.site_settings ENABLE ROW LEVEL SECURITY;

-- 4. Allow public read access (for customers to read config)
CREATE POLICY "Cho phép tất cả mọi người đọc site_settings" 
ON public.site_settings FOR SELECT 
USING (true);

-- 5. Allow public update access (for admin functionality via Anon key)
CREATE POLICY "Cho phép cập nhật site_settings" 
ON public.site_settings FOR UPDATE 
USING (true);
