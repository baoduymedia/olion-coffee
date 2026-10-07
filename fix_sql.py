import re

with open('supabase_schema.sql', 'r') as f:
    c = f.read()

new_sql = """INSERT INTO public.menu_items (id, name, price, category, image_url, badge, description, is_available, sort_order)
VALUES
    -- Cà phê
    (1, 'ESPRESSO', 30000, 'Cà phê', 'assets/menu/espresso.webp', '', 'Nóng / Đá. Cà phê nguyên chất đậm đà.', true, 1),
    (2, 'ESPRESSO SỮA', 35000, 'Cà phê', 'assets/menu/espresso_sua.webp', 'BEST', 'Nóng / Đá. Sự kết hợp hoàn hảo giữa espresso và sữa đặc.', true, 2),
    (3, 'BẠC XỈU', 35000, 'Cà phê', 'assets/menu/bac_xiu.webp', 'HOT', 'Nhiều sữa ít cà phê, béo ngậy ngọt ngào.', true, 3),
    (4, 'LATTE HẠNH NHÂN', 40000, 'Cà phê', 'assets/menu/latte_hanh_nhan.webp', '', 'Nóng / Đá. Vị bùi béo của hạnh nhân hòa quyện espresso.', true, 4),
    (5, 'CARAMEL LATTE', 40000, 'Cà phê', 'assets/menu/caramel_latte.webp', '', 'Latte ngọt ngào với lớp sốt caramel thơm lừng.', true, 5),
    (6, 'AMERICANO', 30000, 'Cà phê', 'assets/menu/americano.webp', '', 'Nóng / Đá. Espresso pha loãng thanh tao.', true, 6),
    (7, 'CÀ PHÊ MUỐI', 40000, 'Cà phê', 'assets/menu/ca_phe_muoi.webp', 'SIGNATURE', 'Đậm đà cà phê kết hợp lớp kem muối mặn béo.', true, 7),
    (8, 'CÀ PHÊ BẠC HÀ', 40000, 'Cà phê', 'assets/menu/ca_phe_bac_ha.webp', '', 'Sự the mát sảng khoái của bạc hà và cà phê.', true, 8),
    (9, 'ESPRESSO OATSIDE', 40000, 'Cà phê', 'assets/menu/ca_phe_sua_oatside.webp', 'NEW', 'Nóng / Đá. Sữa yến mạch Oatside kết hợp espresso.', true, 9),

    -- Cacao
    (10, 'CACAO LATTE', 35000, 'Cacao', 'assets/menu/cacao_latte.webp', 'BEST', 'Nóng / Đá. Cacao nguyên chất béo thơm.', true, 10),
    (11, 'CACAO KEM MUỐI', 40000, 'Cacao', 'assets/menu/cacao_kem_muoi.webp', 'HOT', 'Cacao đậm đà hòa quyện lớp kem muối béo ngậy.', true, 11),
    (12, 'CACAO BẠC HÀ', 40000, 'Cacao', 'assets/menu/cacao_bac_ha.webp', '', 'Hương bạc hà the mát sảng khoái quyện cùng vị ngọt đắng cacao.', true, 12),

    -- Trà trái cây
    (13, 'TRÀ VẢI HOA HỒNG', 40000, 'Trà trái cây', 'assets/menu/tra_vai_hoa_hong.webp', 'BEST', 'Vải ngọt mọng nước kết hợp hương hoa hồng thanh tao dịu nhẹ.', true, 13),
    (14, 'TRÀ BƯỞI HỒNG CHANH VÀNG', 40000, 'Trà trái cây', 'assets/menu/tra_buoi_hong_chanh_vang.webp', '', 'Bưởi hồng mọng nước hòa cùng chanh vàng thơm mát.', true, 14),
    (15, 'TRÀ CHANH DÂY NHIỆT ĐỚI', 40000, 'Trà trái cây', 'assets/menu/tra_chanh_day_nhiet_doi.webp', 'HOT', 'Chua ngọt bùng nổ, tươi mát sảng khoái ngày hè.', true, 15),
    (16, 'TRÀ XOÀI CHANH DÂY', 40000, 'Trà trái cây', 'assets/menu/tra_xoai_chanh_day.webp', '', 'Xoài chín ngọt thanh quyện cùng chanh dây đậm đà.', true, 16),
    (17, 'LỤC TRÀ NHÃN', 40000, 'Trà trái cây', 'assets/menu/luc_tra_nhan.webp', '', 'Nhãn giòn ngọt ngào kết hợp nền lục trà lài thanh tao.', true, 17),
    (18, 'LỤC TRÀ TRÂN CHÂU TRẮNG', 35000, 'Trà trái cây', 'assets/menu/luc_tra_tran_chau_trang.webp', '', 'Lục trà lài thanh mát cùng trân châu trắng giòn sần sật.', true, 18),

    -- Nước ép
    (19, 'NƯỚC ÉP CAM', 30000, 'Nước ép', 'assets/menu/nuoc_ep_cam.webp', 'BEST', 'Cam sành tươi vắt nguyên chất, dồi dào Vitamin C.', true, 19),
    (20, 'NƯỚC ÉP CHANH DÂY', 30000, 'Nước ép', 'assets/menu/nuoc_ep_chanh_day.webp', 'HOT', 'Chanh dây tươi thơm nồng, chua ngọt giải nhiệt cực đã.', true, 20),

    -- Trà sữa & Matcha
    (21, 'MATCHA LATTE', 40000, 'Trà sữa & Matcha', 'assets/menu/matcha_latte.webp', 'SIGNATURE', 'Nóng / Đá. Matcha Nhật Bản nguyên chất thơm lừng.', true, 21),
    (22, 'MATCHA CARAMEL', 45000, 'Trà sữa & Matcha', 'assets/menu/matcha_caramel.webp', '', 'Matcha thơm đậm hòa quyện cùng sốt caramel béo ngậy.', true, 22),
    (23, 'MATCHA BẠC HÀ', 45000, 'Trà sữa & Matcha', 'assets/menu/matcha_bac_ha.webp', '', 'Sự kết hợp độc đáo giữa vị thanh của matcha và the mát của bạc hà.', true, 23),
    (24, 'MATCHA KEM MUỐI', 45000, 'Trà sữa & Matcha', 'assets/menu/matcha_kem_muoi.webp', '', 'Lớp kem muối béo ngậy mằn mặn phủ trên nền matcha đậm đà.', true, 24),
    (25, 'MATCHA QUẾ HOA', 45000, 'Trà sữa & Matcha', 'assets/menu/matcha_que_hoa.webp', '', 'Matcha cao cấp ướp hương hoa quế tự nhiên thanh tao.', true, 25),
    (26, 'MATCHA COLD WHISK', 45000, 'Trà sữa & Matcha', 'assets/menu/matcha_cold_whisk.webp', '', 'Nóng / Đá. Đánh bọt matcha lạnh thủ công truyền thống.', true, 26),
    (27, 'MATCHA DỪA', 45000, 'Trà sữa & Matcha', 'assets/menu/matcha_dua.webp', '', 'Vị thơm bùi của nước cốt dừa tươi quyện cùng bột matcha thượng hạng.', true, 27),
    (28, 'MATCHA DÂU', 45000, 'Trà sữa & Matcha', 'assets/menu/matcha_dau.webp', 'HOT', 'Sự hòa quyện tuyệt hảo giữa matcha thơm đắng và mứt dâu tây.', true, 28),
    (29, 'MATCHA ESPRESSO LATTE', 45000, 'Trà sữa & Matcha', 'assets/menu/matcha_oatside.webp', '', 'Kết hợp hoàn hảo giữa Matcha và Espresso Latte.', true, 29),

    -- Sữa chua
    (30, 'YAGOUT ĐÀO CHANH DÂY', 45000, 'Sữa chua', 'assets/menu/yagout_dao_chanh_day.webp', '', 'Đào mọng nước thơm ngọt hòa cùng vị chua dịu nhẹ của chanh dây.', true, 30),
    (31, 'YAGOUT VIỆT QUẤT', 45000, 'Sữa chua', 'assets/menu/yagout_viet_quat.webp', 'HOT', 'Việt quất bổ dưỡng thơm lừng quyện cùng sữa chua tươi mát.', true, 31),
    (32, 'YAGOUT XOÀI CHANH DÂY', 45000, 'Sữa chua', 'assets/menu/yagout_xoai_chanh_day.webp', '', 'Xoài chín thơm ngọt hòa quyện cùng chanh dây nhiệt đới.', true, 32),
    (33, 'YAGOUT DÂU', 45000, 'Sữa chua', 'assets/menu/yagout_dau.webp', 'BEST', 'Sữa chua sánh mịn kết hợp mứt dâu tây chua ngọt thanh mát.', true, 33),

    -- Topping
    (34, 'TRÂN CHÂU TRẮNG', 5000, 'Topping', 'assets/menu/tran_chau_trang.webp', '', 'Trân châu trắng ngọc trai giòn dai thơm ngon.', true, 34),
    (35, 'TRÂN CHÂU Ô LONG', 5000, 'Topping', 'assets/menu/tran_chau_o_long.webp', '', 'Đậm hương trà ô long rang mộc, mềm dẻo.', true, 35),
    (36, 'THẠCH SƯƠNG SÁO', 5000, 'Topping', 'assets/menu/thach_suong_sao.webp', '', 'Thạch sương sáo mềm mượt, thanh mát giải nhiệt tự nhiên.', true, 36),
    (37, 'THẠCH QUẾ HOA', 5000, 'Topping', 'assets/menu/thach_que_hoa.webp', '', 'Thơm thanh hương hoa quế tự nhiên.', true, 37),
    (38, 'THẠCH VẢI HOA HỒNG', 5000, 'Topping', 'assets/menu/thach_vai_hoa_hong.webp', '', 'Thạch giòn dai thơm ngát hương hoa hồng và vị vải ngọt thanh.', true, 38),
    (39, 'THẠCH CÀ PHÊ', 5000, 'Topping', 'assets/menu/thach_ca_phe.webp', '', 'Thạch cà phê nấu thủ công giòn thơm đậm vị.', true, 39);"""

c = re.sub(r'INSERT INTO public\.menu_items.*?39\);', new_sql, c, flags=re.DOTALL)

with open('supabase_schema.sql', 'w') as f:
    f.write(c)
