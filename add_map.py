import re

with open('index.html', 'r') as f:
    c = f.read()

map_html = """
        <div class="map-container" style="margin-top: 32px; border-radius: var(--radius-lg); overflow: hidden; border: 1px solid var(--border-subtle); box-shadow: 0 4px 20px rgba(0,0,0,0.15); width: 100%; height: clamp(350px, 45vh, 450px); background: #222;">
          <iframe 
            src="https://maps.google.com/maps?q=Olion%20Coffee,%2080/64a%20Dương%20Quảng%20Hàm,%20Gò%20Vấp&t=&z=16&ie=UTF8&iwloc=&output=embed" 
            width="100%" 
            height="100%" 
            style="border:0; filter: contrast(1.1) grayscale(0.2);" 
            allowfullscreen="" 
            loading="lazy" 
            referrerpolicy="no-referrer-when-downgrade">
          </iframe>
        </div>
      </div>
    </section>"""

# Replace the closing div of contact-grid and the closing section tags
c = re.sub(r'        </div>\n      </div>\n    </section>', '        </div>\n' + map_html, c, count=1)

with open('index.html', 'w') as f:
    f.write(c)
