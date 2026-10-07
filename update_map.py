import re

with open('index.html', 'r') as f:
    c = f.read()

# Replace iframe src
# The current src is the bad pb= one
bad_src = 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3918.730219504561!2d106.68536107584144!3d10.831940989320295!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3175290076bf2d09%3A0xc3bba4d6ef2c56a8!2sOlion%20Coffee!5e0!3m2!1svi!2s!4v1726915061611!5m2!1svi!2s'
good_src = 'https://maps.google.com/maps?width=100%25&amp;height=600&amp;hl=vi&amp;q=80/64a%20Dương%20Quảng%20Hàm,%20Gò%20Vấp+(Olion%20Coffee)&amp;t=&amp;z=18&amp;ie=UTF8&amp;iwloc=B&amp;output=embed'

c = c.replace(bad_src, good_src)

with open('index.html', 'w') as f:
    f.write(c)

