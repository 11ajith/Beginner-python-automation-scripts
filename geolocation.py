# Get the geolocation details of the specific website or IP 

from urllib import parse
from urllib import request
import json

def geolocation(url):
    url = url.strip()
    if not parse.urlparse(url).scheme:
        url = 'http://' + url
    parsed = parse.urlparse(url)
    resp = request.urlopen(f'http://ip-api.com/json/{parsed.netloc}')
    data = resp.read().decode('utf-8')
    print(json.loads(data))

geolocation("Enter the website url or IP address")