import requests

def url_ok(url):
    r = requests.head(url)
    return r.status_code == 200
url_ok(www.duckduckgo.com)