import re

with open('index.html', 'r') as f:
    c = f.read()

c = c.replace('https://olion-coffee.vercel.app', 'https://www.olioncoffee.app')

# Let's also check if there is any other domain reference like baoduymedia.github.io
c = c.replace('https://baoduymedia.github.io/olion-coffee', 'https://www.olioncoffee.app')

with open('index.html', 'w') as f:
    f.write(c)

with open('service-worker.js', 'r') as f:
    sw = f.read()
sw = re.sub(r'CACHE_NAME = "olion-coffee-v[0-9.]+"', 'CACHE_NAME = "olion-coffee-v1.8"', sw)
with open('service-worker.js', 'w') as f:
    f.write(sw)
