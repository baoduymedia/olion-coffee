import urllib.request
url = "https://maps.google.com/maps?width=100%&height=600&hl=en&q=80/64a%20Dương%20Quảng%20Hàm,%20Gò%20Vấp+(Olion%20Coffee)&t=&z=17&ie=UTF8&iwloc=B&output=embed"
# url encode
import urllib.parse
url = "https://maps.google.com/maps?width=100%25&height=600&hl=en&q=" + urllib.parse.quote("80/64a Dương Quảng Hàm, Gò Vấp") + "+(" + urllib.parse.quote("Olion Coffee") + ")&t=&z=18&ie=UTF8&iwloc=B&output=embed"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        print(response.getcode())
        html = response.read().decode('utf-8')
        print(len(html))
except Exception as e:
    print(e)
