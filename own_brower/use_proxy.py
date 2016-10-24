# coding:UTF-8

import urllib
import requests
URL = 'https://www.github.com'
PROXY_URL = '165.24.10.8:8080'


def url_proxy():
    resp = urllib.urlopen(URL, proxies  = {"http" : PROXY_URL})
    print resp.headers


# requests 不支持https访问
def req_proxy():
    proxies = {"http" : PROXY_URL}
    resp = requests.get(URL, proxies = proxies)
    print resp



