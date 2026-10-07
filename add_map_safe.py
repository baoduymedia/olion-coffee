import re

with open('index.html', 'r') as f:
    c = f.read()

contact_end_regex = r'(<h3 class="hours-title"[^>]*>Giờ mở cửa</h3>.*?</div>\n          </div>\n        </div>)\n      </div>\n    </section>'

map_html = r"""\1
        
        <!-- Google Map Embedded -->
        <div class="map-container" style="margin-top: 40px; border-radius: var(--radius-lg); overflow: hidden; border: 1px solid var(--border-subtle); box-shadow: 0 8px 30px rgba(0,0,0,0.15); width: 100%; height: clamp(350px, 45vh, 450px); background: #222; position: relative; z-index: 1;">
          <iframe 
            src="https://maps.google.com/maps?q=Olion%20Coffee,%2080/64a%20Dương%20Quảng%20Hàm,%20Gò%20Vấp&t=&z=16&ie=UTF8&iwloc=&output=embed" 
            width="100%" 
            height="100%" 
            style="border:0; filter: contrast(1.05) opacity(0.9);" 
            allowfullscreen="" 
            loading="lazy" 
            referrerpolicy="no-referrer-when-downgrade">
          </iframe>
        </div>
      </div>
    </section>"""

c = re.sub(contact_end_regex, map_html, c, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(c)
