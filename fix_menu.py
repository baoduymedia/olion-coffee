import re

with open('supabaseClient.js', 'r') as f:
    c = f.read()

# I will replace the DEFAULT_MENU_ITEMS block with the exact new one based on the image
new_default_menu = """const DEFAULT_MENU_ITEMS = [
  // Cà phê
  { id: 1, name: 'ESPRESSO', price: 30000, category: 'Cà phê', image_url: 'assets/menu/espresso.webp', badge: '', description: 'Nóng / Đá. Cà phê nguyên chất đậm đà.', is_available: true },
  { id: 2, name: 'ESPRESSO SỮA', price: 35000, category: 'Cà phê', image_url: 'assets/menu/espresso_sua.webp', badge: 'BEST', description: 'Nóng / Đá. Sự kết hợp hoàn hảo giữa espresso và sữa đặc.', is_available: true },
  { id: 3, name: 'BẠC XỈU', price: 35000, category: 'Cà phê', image_url: 'assets/menu/bac_xiu.webp', badge: 'HOT', description: 'Nhiều sữa ít cà phê, béo ngậy ngọt ngào.', is_available: true },
  { id: 4, name: 'LATTE HẠNH NHÂN', price: 40000, category: 'Cà phê', image_url: 'assets/menu/latte_hanh_nhan.webp', badge: '', description: 'Nóng / Đá. Vị bùi béo của hạnh nhân hòa quyện espresso.', is_available: true },
  { id: 5, name: 'CARAMEL LATTE', price: 40000, category: 'Cà phê', image_url: 'assets/menu/caramel_latte.webp', badge: '', description: 'Latte ngọt ngào với lớp sốt caramel thơm lừng.', is_available: true },
  { id: 6, name: 'AMERICANO', price: 30000, category: 'Cà phê', image_url: 'assets/menu/americano.webp', badge: '', description: 'Nóng / Đá. Espresso pha loãng thanh tao.', is_available: true },
  { id: 7, name: 'CÀ PHÊ MUỐI', price: 40000, category: 'Cà phê', image_url: 'assets/menu/ca_phe_muoi.webp', badge: 'SIGNATURE', description: 'Đậm đà cà phê kết hợp lớp kem muối mặn béo.', is_available: true },
  { id: 8, name: 'CÀ PHÊ BẠC HÀ', price: 40000, category: 'Cà phê', image_url: 'assets/menu/ca_phe_bac_ha.webp', badge: '', description: 'Sự the mát sảng khoái của bạc hà và cà phê.', is_available: true },
  { id: 9, name: 'ESPRESSO OATSIDE', price: 40000, category: 'Cà phê', image_url: 'assets/menu/ca_phe_sua_oatside.webp', badge: 'NEW', description: 'Nóng / Đá. Sữa yến mạch Oatside kết hợp espresso.', is_available: true },

  // Cacao
  { id: 10, name: 'CACAO LATTE', price: 35000, category: 'Cacao', image_url: 'assets/menu/cacao_latte.webp', badge: 'BEST', description: 'Nóng / Đá. Cacao nguyên chất béo thơm.', is_available: true },
  { id: 11, name: 'CACAO KEM MUỐI', price: 40000, category: 'Cacao', image_url: 'assets/menu/cacao_kem_muoi.webp', badge: 'HOT', description: 'Cacao đậm đà hòa quyện lớp kem muối béo ngậy.', is_available: true },
  { id: 12, name: 'CACAO BẠC HÀ', price: 40000, category: 'Cacao', image_url: 'assets/menu/cacao_bac_ha.webp', badge: '', description: 'Hương bạc hà the mát sảng khoái quyện cùng vị ngọt đắng cacao.', is_available: true },

  // Trà
  { id: 13, name: 'TRÀ VẢI HOA HỒNG', price: 40000, category: 'Trà trái cây', image_url: 'assets/menu/tra_vai_hoa_hong.webp', badge: 'BEST', description: 'Vải ngọt mọng nước kết hợp hương hoa hồng thanh tao dịu nhẹ.', is_available: true },
  { id: 14, name: 'TRÀ BƯỞI HỒNG CHANH VÀNG', price: 40000, category: 'Trà trái cây', image_url: 'assets/menu/tra_buoi_hong_chanh_vang.webp', badge: '', description: 'Bưởi hồng mọng nước hòa cùng chanh vàng thơm mát.', is_available: true },
  { id: 15, name: 'TRÀ CHANH DÂY NHIỆT ĐỚI', price: 40000, category: 'Trà trái cây', image_url: 'assets/menu/tra_chanh_day_nhiet_doi.webp', badge: 'HOT', description: 'Chua ngọt bùng nổ, tươi mát sảng khoái ngày hè.', is_available: true },
  { id: 16, name: 'TRÀ XOÀI CHANH DÂY', price: 40000, category: 'Trà trái cây', image_url: 'assets/menu/tra_xoai_chanh_day.webp', badge: '', description: 'Xoài chín ngọt thanh quyện cùng chanh dây đậm đà.', is_available: true },
  { id: 17, name: 'LỤC TRÀ NHÃN', price: 40000, category: 'Trà trái cây', image_url: 'assets/menu/luc_tra_nhan.webp', badge: '', description: 'Nhãn giòn ngọt ngào kết hợp nền lục trà lài thanh tao.', is_available: true },
  { id: 18, name: 'LỤC TRÀ TRÂN CHÂU TRẮNG', price: 35000, category: 'Trà trái cây', image_url: 'assets/menu/luc_tra_tran_chau_trang.webp', badge: '', description: 'Lục trà lài thanh mát cùng trân châu trắng giòn sần sật.', is_available: true },

  // Nước ép
  { id: 19, name: 'NƯỚC ÉP CAM', price: 30000, category: 'Nước ép', image_url: 'assets/menu/nuoc_ep_cam.webp', badge: 'BEST', description: 'Cam sành tươi vắt nguyên chất, dồi dào Vitamin C.', is_available: true },
  { id: 20, name: 'NƯỚC ÉP CHANH DÂY', price: 30000, category: 'Nước ép', image_url: 'assets/menu/nuoc_ep_chanh_day.webp', badge: 'HOT', description: 'Chanh dây tươi thơm nồng, chua ngọt giải nhiệt cực đã.', is_available: true },

  // Matcha
  { id: 21, name: 'MATCHA LATTE', price: 40000, category: 'Trà sữa & Matcha', image_url: 'assets/menu/matcha_latte.webp', badge: 'SIGNATURE', description: 'Nóng / Đá. Matcha Nhật Bản nguyên chất thơm lừng.', is_available: true },
  { id: 22, name: 'MATCHA CARAMEL', price: 45000, category: 'Trà sữa & Matcha', image_url: 'assets/menu/matcha_caramel.webp', badge: '', description: 'Matcha thơm đậm hòa quyện cùng sốt caramel béo ngậy.', is_available: true },
  { id: 23, name: 'MATCHA BẠC HÀ', price: 45000, category: 'Trà sữa & Matcha', image_url: 'assets/menu/matcha_bac_ha.webp', badge: '', description: 'Sự kết hợp độc đáo giữa vị thanh của matcha và the mát của bạc hà.', is_available: true },
  { id: 24, name: 'MATCHA KEM MUỐI', price: 45000, category: 'Trà sữa & Matcha', image_url: 'assets/menu/matcha_kem_muoi.webp', badge: '', description: 'Lớp kem muối béo ngậy mằn mặn phủ trên nền matcha đậm đà.', is_available: true },
  { id: 25, name: 'MATCHA QUẾ HOA', price: 45000, category: 'Trà sữa & Matcha', image_url: 'assets/menu/matcha_que_hoa.webp', badge: '', description: 'Matcha cao cấp ướp hương hoa quế tự nhiên thanh tao.', is_available: true },
  { id: 26, name: 'MATCHA COLD WHISK', price: 45000, category: 'Trà sữa & Matcha', image_url: 'assets/menu/matcha_cold_whisk.webp', badge: '', description: 'Nóng / Đá. Đánh bọt matcha lạnh thủ công truyền thống.', is_available: true },
  { id: 27, name: 'MATCHA DỪA', price: 45000, category: 'Trà sữa & Matcha', image_url: 'assets/menu/matcha_dua.webp', badge: '', description: 'Vị thơm bùi của nước cốt dừa tươi quyện cùng bột matcha thượng hạng.', is_available: true },
  { id: 28, name: 'MATCHA DÂU', price: 45000, category: 'Trà sữa & Matcha', image_url: 'assets/menu/matcha_dau.webp', badge: 'HOT', description: 'Sự hòa quyện tuyệt hảo giữa matcha thơm đắng và mứt dâu tây.', is_available: true },
  { id: 29, name: 'MATCHA ESPRESSO LATTE', price: 45000, category: 'Trà sữa & Matcha', image_url: 'assets/menu/matcha_oatside.webp', badge: '', description: 'Kết hợp hoàn hảo giữa Matcha và Espresso Latte.', is_available: true },

  // Sữa chua
  { id: 30, name: 'YAGOUT ĐÀO CHANH DÂY', price: 45000, category: 'Sữa chua', image_url: 'assets/menu/yagout_dao_chanh_day.webp', badge: '', description: 'Đào mọng nước thơm ngọt hòa cùng vị chua dịu nhẹ của chanh dây.', is_available: true },
  { id: 31, name: 'YAGOUT VIỆT QUẤT', price: 45000, category: 'Sữa chua', image_url: 'assets/menu/yagout_viet_quat.webp', badge: 'HOT', description: 'Việt quất bổ dưỡng thơm lừng quyện cùng sữa chua tươi mát.', is_available: true },
  { id: 32, name: 'YAGOUT XOÀI CHANH DÂY', price: 45000, category: 'Sữa chua', image_url: 'assets/menu/yagout_xoai_chanh_day.webp', badge: '', description: 'Xoài chín thơm ngọt hòa quyện cùng chanh dây nhiệt đới.', is_available: true },
  { id: 33, name: 'YAGOUT DÂU', price: 45000, category: 'Sữa chua', image_url: 'assets/menu/yagout_dau.webp', badge: 'BEST', description: 'Sữa chua sánh mịn kết hợp mứt dâu tây chua ngọt thanh mát.', is_available: true },

  // Topping
  { id: 34, name: 'TRÂN CHÂU TRẮNG', price: 5000, category: 'Topping', image_url: 'assets/menu/tran_chau_trang.webp', badge: '', description: 'Trân châu trắng ngọc trai giòn dai thơm ngon.', is_available: true },
  { id: 35, name: 'TRÂN CHÂU Ô LONG', price: 5000, category: 'Topping', image_url: 'assets/menu/tran_chau_o_long.webp', badge: '', description: 'Đậm hương trà ô long rang mộc, mềm dẻo.', is_available: true },
  { id: 36, name: 'THẠCH SƯƠNG SÁO', price: 5000, category: 'Topping', image_url: 'assets/menu/thach_suong_sao.webp', badge: '', description: 'Thạch sương sáo mềm mượt, thanh mát giải nhiệt tự nhiên.', is_available: true },
  { id: 37, name: 'THẠCH QUẾ HOA', price: 5000, category: 'Topping', image_url: 'assets/menu/thach_que_hoa.webp', badge: '', description: 'Thơm thanh hương hoa quế tự nhiên.', is_available: true },
  { id: 38, name: 'THẠCH VẢI HOA HỒNG', price: 5000, category: 'Topping', image_url: 'assets/menu/thach_vai_hoa_hong.webp', badge: '', description: 'Thạch giòn dai thơm ngát hương hoa hồng và vị vải ngọt thanh.', is_available: true },
  { id: 39, name: 'THẠCH CÀ PHÊ', price: 5000, category: 'Topping', image_url: 'assets/menu/thach_ca_phe.webp', badge: '', description: 'Thạch cà phê nấu thủ công giòn thơm đậm vị.', is_available: true }
];"""

c = re.sub(r'const DEFAULT_MENU_ITEMS = \[\n  // Cà phê.*?\];', new_default_menu, c, flags=re.DOTALL)

with open('supabaseClient.js', 'w') as f:
    f.write(c)

