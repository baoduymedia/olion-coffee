import re

with open('index.html', 'r') as f:
    c = f.read()

c = c.replace('Đổi 1 ly Signature miễn phí (Cà Phê Muối hoặc Bạc Xỉu Kem Trứng)', 'Đổi 1 ly Signature miễn phí (Matcha Quế Hoa, Cacao Bạc Hà, Bạc Xỉu)')

with open('index.html', 'w') as f:
    f.write(c)

