#coding:UTF-8

import argparse
import sys


DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 80
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        # 服务端的响应码，记录服务端日志 ，可根据响应码的不同 定义不同的响应
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("From server msg!")
        return

class CustomServer(HTTPServer):

    def __init__(self):
        addr = (DEFAULT_HOST, DEFAULT_PORT)
        HTTPServer.__init__(self, addr, RequestHandler)

def run_server():
    try:
        server = CustomServer()
        server.serve_forever()
    except Exception, e:
        print "ERROR %s" %(e)
    else:
        print "Server interrupted and is shutting down ..."
        server.socket.close()

if __name__ == '__main__':
    run_server()
