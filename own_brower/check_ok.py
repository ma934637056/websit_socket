# coding:UTF-8

import httplib
import urlparse

URL = "https://github.com/"
# URL = "http://www.python.org"
HTTP_GOOD_CODES = [httplib.OK, httplib.FOUND, httplib.MOVED_PERMANENTLY]

def status_web():
    host, path = urlparse.urlparse(URL)[1:3]
    print host , path
    conn = httplib.HTTPConnection(host)
    conn.request("GET", path)
    resp = conn.getresponse()
    print resp.read(), resp.reason, resp.status, resp.version
    return resp.status


if status_web() in HTTP_GOOD_CODES:
    print "OK"
else:
    print "Failed"