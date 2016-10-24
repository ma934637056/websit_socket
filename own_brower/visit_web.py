#coding:UTF-8
import httplib
import argparse

HTTP_HOST = "localhost"
PORT = 8888
REMOTE_PATH = "/"

class HTTPClient(object):

    def __init__(self, host):
        self.remote_host = host

    def fetch(self):
        conn = httplib.HTTP(self.remote_host, port=8888)

        # Prepare Header
        conn.putrequest("GET", REMOTE_PATH)
        conn.putheader("User_agent", __file__)
        conn.putheader("Host", self.remote_host)
        conn.putheader("Accept", "*/*")
        conn.endheaders()
        try:
            errcode, errmsg, headers = conn.getreply()
        except Exception, e:
            print "Client failed error code: %s message: %s, headers: %s" %(errcode, errmsg, headers)
        else:
            print "Got homepage from %s" %(self.remote_host)
            print headers
            file = conn.getfile()
            return file.read()

if __name__ == '__main__':
    client = HTTPClient(HTTP_HOST)
    test = client.fetch()
    print test