-- ==============================================================================
-- BẢNG: news_items (Quản lý Tin Tức & Sự Kiện)
-- ==============================================================================
CREATE TABLE IF NOT EXISTS public.news_items (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    title TEXT NOT NULL,
    date TEXT NOT NULL,
    category TEXT NOT NULL,
    cover_image TEXT NOT NULL,
    description TEXT,
    content_html TEXT,
    is_featured BOOLEAN DEFAULT false,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL
);

-- Bật RLS
ALTER TABLE public.news_items ENABLE ROW LEVEL SECURITY;

-- Policy: Ai cũng có thể xem tin tức
DROP POLICY IF EXISTS "Allow read news_items" ON public.news_items;
CREATE POLICY "Allow read news_items" ON public.news_items
    FOR SELECT TO anon, authenticated, service_role
    USING (true);

-- Policy: Chỉ định quyền quản lý (Thêm/Sửa/Xóa) cho ẩn danh (tạm thời)
DROP POLICY IF EXISTS "Allow manage news_items" ON public.news_items;
CREATE POLICY "Allow manage news_items" ON public.news_items
    FOR ALL TO anon, authenticated, service_role
    USING (true)
    WITH CHECK (true);

-- Dữ liệu mẫu
INSERT INTO public.news_items (title, date, category, cover_image, description, content_html, is_featured)
VALUES 
('OLION’S FIRST WEEK — NHẬT KÝ TUẦN ĐẦU TIÊN', '19/09/2026', 'Sự kiện đặc biệt', 'assets/news/news-1-flowers.webp', 'Tuần đầu tiên mở cửa đã khép lại với biết bao cung bậc cảm xúc! Olion Coffee vô cùng trân trọng...', '<p>Tuần đầu tiên mở cửa đã khép lại với biết bao cung bậc cảm xúc! Olion Coffee vô cùng trân trọng và biết ơn những lẵng hoa tươi thắm, những lời chúc mừng chân thành từ quý đối tác, bạn bè và đặc biệt là sự ủng hộ nhiệt tình của hàng trăm lượt khách hàng đã ghé thăm quán mỗi ngày.</p><p>Mỗi ly cà phê trao đi là một lời cảm ơn sâu sắc. Chúng tôi cam kết sẽ tiếp tục hoàn thiện không gian và chất lượng đồ uống để mang đến những trải nghiệm tuyệt vời nhất cho bạn.</p>', true),

('Khám Phá Bộ Đôi Matcha Latte & Cà Phê Muối Chuẩn Vị', '18/09/2026', 'Thực Đơn Signature', 'assets/news/news-1-drinks.webp', 'Tại Olion Coffee, mỗi ly thức uống đều được pha chế bằng cả sự nâng niu và tỉ mỉ. Lớp bọt kem muối béo mặn...', '<p>Tại Olion Coffee, mỗi ly thức uống đều được pha chế bằng cả sự nâng niu và tỉ mỉ.</p><div class="news-quote-box">"Lớp bọt kem muối béo mặn sánh mịn hòa cùng cốt cà phê đậm đà tạo nên hương vị bùng nổ ngay từ ngụm đầu tiên."</div><p>Bên cạnh đó, dòng Matcha Latte sử dụng 100% bột trà xanh nhập khẩu từ Shizuoka Nhật Bản, mang hương thơm thanh nhã và vị đắng dịu êm ái.</p>', true),

('Góc Yên Bình Giữa Lòng Gò Vấp Cho Những Buổi Chiều Làm Việc', '15/09/2026', 'Không Gian Quán', 'assets/news/news-1-space.webp', 'Bước qua cánh cửa Olion, bạn sẽ cảm nhận ngay một không gian tách biệt khỏi nhịp sống vội vã ngoài phố thị...', '<p>Bước qua cánh cửa Olion, bạn sẽ cảm nhận ngay một không gian tách biệt khỏi nhịp sống vội vã ngoài phố thị.</p><p>Tông màu gỗ ấm cúng, hệ thống đèn lồng giấy dịu mắt cùng những chậu cây xanh mướt tạo nên một chốn dừng chân hoàn hảo để đọc sách, làm việc hay trò chuyện cùng bạn bè.</p>', true),

('Grand Opening Recap — Tuần Lễ Khai Trương Rực Rỡ Ưu Đãi', '12/09/2026', 'Chương Trình Khuyến Mãi', 'assets/news/news-1-recap.webp', 'Nhìn lại những khoảnh khắc tuyệt vời trong tuần lễ Grand Opening! Khách hàng không chỉ được thưởng thức...', '<p>Nhìn lại những khoảnh khắc tuyệt vời trong tuần lễ Grand Opening! Khách hàng không chỉ được thưởng thức menu giảm giá 20% mà còn nhận được hàng trăm phần quà thú vị từ Vòng Quay May Mắn.</p><p>Đừng quên Olion Coffee vẫn đang áp dụng chương trình Tích điểm Loyalty: 10 ly tặng 1 ly hoàn toàn miễn phí nhé!</p>', true);
