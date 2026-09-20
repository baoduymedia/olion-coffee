# ☕ Olion Coffee Website & Admin Portal

> **"Elegance in Every Sip"** — Website giới thiệu quán cà phê Olion Coffee cùng Cổng Quản trị Admin tích hợp Vòng quay may mắn, hệ thống Đánh giá & Góp ý, Thực đơn động và Thư viện không gian.

---

## 🌟 Tính năng nổi bật

- **Landing Page cao cấp**:
  - Giao diện thiết kế theo phong cách Fine Dining / Boutique Cafe với bảng màu trầm ấm sang trọng (`#181009`, `#C4B29A`, `#E59A55`).
  - Trải nghiệm toàn màn hình (Full Screen Viewport 100vh) cho từng phân đoạn: *Về chúng tôi*, *Món Signature*, *Thực đơn*, *Không gian*, *Hỏi đáp*, *Đánh giá*, *Liên hệ*.
  - Hero slideshow hiệu ứng Ken Burns mượt mà.
  - Vòng quay may mắn (Lucky Wheel Minigame) quay trúng voucher ưu đãi thời gian thực.
  - Thanh Social Dock cố định bên phải với bộ nhận diện chuẩn SVG (Hotline, Zalo, Facebook, TikTok, Instagram, Google Maps).
  - Modal gửi góp ý / đánh giá sao kèm upload ảnh của khách hàng.
  - Preloader thương hiệu 2–3s cùng cơ chế tự ngắt an toàn tối đa 4s.

- **Admin Portal (`admin.html`)**:
  - Quản lý Vòng quay may mắn: Tùy chỉnh danh sách giải thưởng, mã voucher, xác suất trúng (%), màu sắc từng ô quay, thời gian quay và trạng thái bật/tắt.
  - Quản lý danh sách khách hàng tham gia Minigame (xuất file CSV / xóa / tìm kiếm).
  - Quản lý Đánh giá & Góp ý của khách hàng: Duyệt / Ẩn / Xóa bài đánh giá, xem ảnh đính kèm, phân biệt bài mẫu Admin và khách hàng thật.
  - Quản trị Thực đơn: Thêm / Sửa / Xóa món theo 7 danh mục, cập nhật giá tiền, hình ảnh và gắn badge *Bán chạy*, *Mới*, *Signature*.
  - Đăng nhập bảo mật (mật khẩu quản trị viên). Phím tắt: Click 3 lần vào logo ở footer của trang chủ để mở nhanh trang Admin.

---

## 🚀 Khởi chạy cục bộ (Local Run)

Bạn có thể mở trực tiếp tệp `index.html` trong trình duyệt hoặc sử dụng Python HTTP Server:

```bash
# Sử dụng Python 3
python3 -m http.server 8080
```

Truy cập:
- **Trang chủ**: `http://localhost:8080/index.html`
- **Quản trị viên**: `http://localhost:8080/admin.html` (Mật khẩu mặc định: `olion2024` hoặc `admin`)

---

## 📁 Cấu trúc thư mục

```
olion-coffee/
├── index.html            # Trang chủ Olion Coffee
├── admin.html            # Cổng Quản trị Admin Portal
├── assets/               # Hình ảnh không gian, đồ uống, logo chính thức
│   ├── logo-white.png
│   ├── logo-black.png
│   ├── zalo-logo.png
│   ├── space-1.jpg ~ space-7.jpg
│   └── ...
├── .gitignore
└── README.md
```

---

## ☕ Olion Coffee Information
- **Địa chỉ**: 80/64a, Dương Quảng Hàm, An Nhơn, TP. Hồ Chí Minh
- **Giờ mở cửa**: 8:00 — 21:00 (Thứ 2 — Chủ Nhật)
- **Hotline**: 0783 657 587
- **Email**: olioncoffee@gmail.com
