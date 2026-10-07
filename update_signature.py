import re

with open('index.html', 'r') as f:
    c = f.read()

# 1. Update HTML tags
c = c.replace('src="assets/menu/ca_phe_muoi.webp"', 'src="assets/menu/matcha_que_hoa.webp"')
c = c.replace('alt="Cà Phê Muối Olion — Đồ uống Signature đậm đà béo ngậy"', 'alt="Matcha Quế Hoa — Đồ uống Signature thanh tao"')
c = c.replace('>CÀ PHÊ MUỐI OLION</h3>', '>MATCHA QUẾ HOA</h3>')
c = c.replace('>Cà phê Robusta rang mộc đậm đà hòa quyện cùng lớp kem muối béo mặn độc quyền của Olion, tạo nên trải nghiệm vị giác đầy lôi cuốn.</p>', '>Matcha cao cấp ướp hương hoa quế tự nhiên thanh tao quý phái, mang đến trải nghiệm hương vị Nhật Bản tinh tế.</p>')

c = c.replace('src="assets/menu/bac_xiu.webp" alt="Bạc Xỉu Kem Trứng', 'src="assets/menu/cacao_bac_ha.webp" alt="Cacao Bạc Hà')
c = c.replace('>BẠC XỈU KEM TRỨNG</h3>', '>CACAO BẠC HÀ</h3>')
c = c.replace('>Cà phê sữa thơm nồng kết hợp lớp foam kem trứng béo ngậy ngọt dịu, đánh thức mọi giác quan trong từng ngụm thưởng thức.</p>', '>Sự the mát sảng khoái của bạc hà hòa quyện hoàn hảo cùng vị đắng dịu của cacao nguyên chất béo thơm.</p>')

c = c.replace('src="assets/menu/matcha_latte.webp"', 'src="assets/menu/bac_xiu.webp"')
c = c.replace('alt="Matcha Latte Olion — Đồ uống Signature thanh mát chuẩn Nhật"', 'alt="Bạc Xỉu Olion — Đồ uống Signature ngọt ngào béo ngậy"')
c = c.replace('>MATCHA LATTE</h3>', '>BẠC XỈU</h3>')
c = c.replace('>Matcha Nhật Bản thượng hạng thơm thanh đậm vị quyện cùng sữa tươi béo dịu, tạo nên cảm giác thư thái tươi mát trọn vẹn.</p>', '>Cà phê sữa đặc truyền thống nhiều sữa ít cà phê, béo ngậy ngọt ngào đánh thức mọi giác quan trong từng ngụm thưởng thức.</p>')

# 2. Update i18n object (Vietnamese)
c = c.replace('sig_item_1_name: "CÀ PHÊ MUỐI OLION",', 'sig_item_1_name: "MATCHA QUẾ HOA",')
c = c.replace('sig_item_1_desc: "Cà phê Robusta rang mộc đậm đà hòa quyện cùng lớp kem muối béo mặn độc quyền của Olion, tạo nên trải nghiệm vị giác đầy lôi cuốn.",', 'sig_item_1_desc: "Matcha cao cấp ướp hương hoa quế tự nhiên thanh tao quý phái, mang đến trải nghiệm hương vị Nhật Bản tinh tế.",')

c = c.replace('sig_item_2_name: "BẠC XỈU KEM TRỨNG",', 'sig_item_2_name: "CACAO BẠC HÀ",')
c = c.replace('sig_item_2_desc: "Cà phê sữa thơm nồng kết hợp lớp foam kem trứng béo ngậy ngọt dịu, đánh thức mọi giác quan trong từng ngụm thưởng thức.",', 'sig_item_2_desc: "Sự the mát sảng khoái của bạc hà hòa quyện hoàn hảo cùng vị đắng dịu của cacao nguyên chất béo thơm.",')

c = c.replace('sig_item_3_name: "MATCHA LATTE",', 'sig_item_3_name: "BẠC XỈU",')
c = c.replace('sig_item_3_desc: "Matcha Nhật Bản thượng hạng thơm thanh đậm vị quyện cùng sữa tươi béo dịu, tạo nên cảm giác thư thái tươi mát trọn vẹn.",', 'sig_item_3_desc: "Cà phê sữa đặc truyền thống nhiều sữa ít cà phê, béo ngậy ngọt ngào đánh thức mọi giác quan trong từng ngụm thưởng thức.",')


# 3. Update i18n object (English)
c = c.replace('sig_item_1_name: "OLION SALTED CREAM COFFEE",', 'sig_item_1_name: "OSMANTHUS MATCHA",')
c = c.replace('sig_item_1_desc: "Bold artisanal Robusta coffee harmoniously blended with Olion\'s proprietary velvety salted cream, creating an irresistible flavor journey.",', 'sig_item_1_desc: "Premium matcha infused with the natural, elegant fragrance of osmanthus flowers, delivering a refined Japanese flavor experience.",')

c = c.replace('sig_item_2_name: "EGG FOAM WHITE COFFEE",', 'sig_item_2_name: "MINT CACAO",')
c = c.replace('sig_item_2_desc: "Aromatic sweet milk coffee topped with rich, airy egg custard foam, awakening every sensation with each velvety sip.",', 'sig_item_2_desc: "The refreshing coolness of mint perfectly blended with the gentle bitterness of pure, rich cacao.",')

c = c.replace('sig_item_3_name: "JAPANESE MATCHA LATTE",', 'sig_item_3_name: "BAC XIU (VIETNAMESE WHITE COFFEE)",')
c = c.replace('sig_item_3_desc: "Premium ceremonial-grade Japanese matcha infused with silky fresh milk, delivering a crisp, refreshing, and calming indulgence.",', 'sig_item_3_desc: "Traditional Vietnamese coffee with condensed milk, sweet and creamy to awaken all senses in every sip.",')

with open('index.html', 'w') as f:
    f.write(c)

