#coding:UTF-8

import cookielib
import urllib
import urllib2

ID_USERNAME = 'id_username'
ID_PASSWORD = 'id_password'
USERNAME = "vindictu@sina.com"
PASSWORD = "ma467677062"
LOGIN_URL = "http://mail.sina.com.cn/?from=mail"
NORMAL_URL = "http://mail.sina.com.cn"
def extract_cookie_info():
    cj = cookielib.CookieJar()
    loging_data = urllib.urlencode({ID_USERNAME: USERNAME, ID_PASSWORD: PASSWORD})
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

    resp = opener.open(LOGIN_URL, loging_data)
    print resp.headers
    for cookie in cj:
        print cookie.name+ "--->" +cookie.value
    resp = opener.open(NORMAL_URL)
    print resp.headers
    for cookie in cj:
        print cookie.name + "--->" + cookie.value

extract_cookie_info()