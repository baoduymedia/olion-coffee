import re

with open('index.html', 'r') as f:
    lines = f.readlines()

# Remove the wrong button from index.html
new_lines = []
skip = False
for i, line in enumerate(lines):
    if '<div style="text-align: center; margin-top: 40px;">' in line and 'a href="news"' in lines[i+1]:
        skip = True
    if skip and '</div>' in line:
        skip = False
        continue
    if not skip:
        new_lines.append(line)

# Now we need to insert the button at the end of the news section
button_html = """
      <div style="text-align: center; margin-top: 40px;">
        <a href="news" class="btn btn-outline" style="border: 1px solid var(--accent-gold); color: var(--accent-gold); padding: 12px 24px; border-radius: 50px; font-family: var(--font-heading); letter-spacing: 0.05em; display: inline-flex; align-items: center; gap: 8px; transition: all 0.3s ease;">
          <i data-lucide="layout-grid" style="width:16px;height:16px;"></i> Xem toàn bộ Tin Tức & Mạng Xã Hội
        </a>
      </div>
"""

final_lines = []
for line in new_lines:
    if '<!-- ======== 9. FAQ ACCORDION ======== -->' in line:
        # We know the previous line is </section> (with some spacing), we should insert right before the closing of news shell.
        pass
    final_lines.append(line)

# A safer way to insert into index.html
text = "".join(new_lines)
news_end = """          </div>
        </div>
      </div>
    </section>

    <!-- ======== 9. FAQ ACCORDION ======== -->"""

new_news_end = f"""          </div>
        </div>
      </div>
{button_html}    </section>

    <!-- ======== 9. FAQ ACCORDION ======== -->"""

text = text.replace(news_end, new_news_end)

with open('index.html', 'w') as f:
    f.write(text)


# Now fix news.html navigation
with open('news.html', 'r') as f:
    news_html = f.read()

# Fix header links
news_html = news_html.replace('href="#', 'href="/#')
news_html = news_html.replace('href="#"', 'href="/"')

# Fix Logo link
news_html = re.sub(r'<a href="/" class="logo">', '<a href="/" class="logo">', news_html) # Just to be sure
news_html = news_html.replace('href="/"', 'href="/"') # This replaces href="#" if we missed any, wait, href="#" was already replaced.

# Wait, in the original header, Logo is `<a href="#" class="logo">`.
# So `href="#"` becomes `href="/#"` which is fine, but `/` is better.
news_html = news_html.replace('href="/#"', 'href="/"')

# We need to make sure the nav links point to /#section, e.g., /#menu
# Let's fix the footer links
# Original footer links:
# <li><a href="#">Trang chủ</a></li>
# <li><a href="#about">Về Olion</a></li>
# <li><a href="#signature">Thức uống Signature</a></li>
# <li><a href="#menu">Thực đơn đầy đủ</a></li>
# <li><a href="#news">Tin tức mới nhất</a></li>

# In news.html, they were changed to `href="/#"` and `href="/#about"`.
# Let's double check if we need to do it selectively.
# If I just do replace('href="#', 'href="/#') it will change all local anchors.
# That's perfectly correct for news.html because we want ALL anchors to go to the homepage's anchors!

with open('news.html', 'w') as f:
    f.write(news_html)

