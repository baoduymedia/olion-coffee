import re

with open('index.html', 'r') as f:
    c = f.read()

old_src = 'https://maps.google.com/maps?q=Olion%20Coffee,%2080/64a%20Dương%20Quảng%20Hàm,%20Gò%20Vấp&t=&z=16&ie=UTF8&iwloc=&output=embed'
new_src = 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3918.730219504561!2d106.68536107584144!3d10.831940989320295!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3175290076bf2d09%3A0xc3bba4d6ef2c56a8!2sOlion%20Coffee!5e0!3m2!1svi!2s!4v1726915061611!5m2!1svi!2s'

c = c.replace(old_src, new_src)

with open('index.html', 'w') as f:
    f.write(c)

