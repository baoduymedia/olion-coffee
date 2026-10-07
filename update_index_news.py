import re

with open('index.html', 'r') as f:
    c = f.read()

btn_html = """    </div>
    
    <div style="text-align: center; margin-top: 40px;">
      <a href="news.html" class="btn btn-primary" style="display: inline-flex; align-items: center; gap: 8px;">
        <i data-lucide="layout-grid" style="width:16px;height:16px;"></i> Xem tất cả trang Tin Tức & Sự Kiện
      </a>
    </div>

  </section>
"""

c = c.replace('    </div>\n  </section>', btn_html, 1) # Only first occurrence to be safe, wait, there are multiple </section>. Let's be specific.

# Let's search for the end of news grid in index.html
end_news_grid = """          </article>
        </div>
      </div>"""

new_end_news_grid = """          </article>
        </div>
      </div>
      
      <div style="text-align: center; margin-top: 40px;">
        <a href="news.html" class="btn btn-outline" style="border: 1px solid var(--accent-gold); color: var(--accent-gold); padding: 12px 24px; border-radius: 50px; font-family: var(--font-heading); letter-spacing: 0.05em; display: inline-flex; align-items: center; gap: 8px; transition: all 0.3s ease;">
          <i data-lucide="layout-grid" style="width:16px;height:16px;"></i> Xem toàn bộ Tin Tức & Mạng Xã Hội
        </a>
      </div>"""

c = c.replace(end_news_grid, new_end_news_grid)

with open('index.html', 'w') as f:
    f.write(c)

