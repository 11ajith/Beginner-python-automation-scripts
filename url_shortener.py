# URL shortener using tinyurl

import requests
from urllib import parse


def url_shortener(url):
    url = url.strip()
    if not parse.urlparse(url).scheme:
        url = 'http://' + url
    query_url = f'http://tinyurl.com/api-create.php?url={url}'
    return requests.get(query_url).text

print(url_shortener("enter the url to be shortened"))