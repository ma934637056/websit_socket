#coding:UTF-8

import argparse
import string
import os
import sys
import gzip
import cStringIO
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

DEFAULT_HOST = '127.0.0.1'
DEFAULT_PORT = 8888
# HTML_CONTENT = """<html><body><h1>Compressed Hello  World!</h1></body></html>"""
HTML_CONTENT = """Compressed Hello  World!"""


class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Accept-type', 'text/html')
        self.send_header('Content-Encoding', 'gzip')
        zbuf = self.compress_buffer(HTML_CONTENT)
        self.send_header('Content-Length', len(zbuf))
        self.end_headers()
        # 客户端输出
        sys.stdout.write("Accept-Encoding: gzip\r\n")
        sys.stdout.write("Content-Length: %d\r\n" % (len(zbuf)))
        self.wfile.write(zbuf)

    def compress_buffer(self, buf):
        zbuf = cStringIO.StringIO()
        zfile = gzip.GzipFile(mode="wb", fileobj=zbuf, compresslevel=6)
        zfile.write(buf)
        zfile.close()
        return zbuf.getvalue()

if __name__ == '__main__':
    test = HTTPServer((DEFAULT_HOST, DEFAULT_PORT), RequestHandler)
    test.serve_forever()
