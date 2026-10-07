import re

with open('index.html', 'r') as f:
    c = f.read()

# Replace the previous src with the correct pb= url
bad_src = 'https://maps.google.com/maps?width=100%25&amp;height=600&amp;hl=vi&amp;q=80/64a%20Dương%20Quảng%20Hàm,%20Gò%20Vấp+(Olion%20Coffee)&amp;t=&amp;z=18&amp;ie=UTF8&amp;iwloc=B&amp;output=embed'
good_src = 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1959.3512!2d106.6977984!3d10.8267018!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3175294b803d0b41%3A0x58d79ca538a1312c!2sOLION%20COFFEE!5e0!3m2!1svi!2sVN!4v1700000000000!5m2!1svi!2sVN'

c = c.replace(bad_src, good_src)

with open('index.html', 'w') as f:
    f.write(c)

