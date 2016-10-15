# coding:UTF-8

import socket
import argparse
import sys
def error_handling():
    """
        处理创建套接字对象、 连接服务器、 发送数据、 等待应答 等时候发生的错误
        argparse 模块使用
    """
    parser = argparse.ArgumentParser(description="Socket Error Example")
    # help 是在--help中的输出， dest是在获取值时候需要的var_name, type格式， action ， required是否必须， default默认值
    parser.add_argument('--host', action="store", dest="host", help="连接的主机名" ,required=False)
    parser.add_argument('--port', action="store", dest="port", help="连接的端口号", type=int, required=False)
    parser.add_argument('--file', action="store", dest="filename", help="文件的名字", required=False)
    given_args = parser.parse_args()
    host = given_args.host
    port = given_args.port
    filename = given_args.filename
    # --create socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, e:
        print "Error create socket: %s" % (e,)
        sys.exit(1)
    # --get connect to given host/port
    try:
        s.connect(host, port)
    except socket.gaierror,e :
        print "Address-related error connecting to server :%s" % (e,)
        sys.exit(1)
    except socket.error, e:
        print "Connect error %s" % (e,)
        sys.exit(1)
    # --sending data
    try:
        s.sendall("GET %s HTTP/1.0\r\n\r\n") % (filename)
    except socket.error, e:
        print "Error sending data: %s" %(e,)
        sys.exit(1)
    # --waiting to receive  data from remote host
    while True:
        try:
            buf = s.recv(2048)
        except socket.error, e:
            print "Error receiving data : %s" %(e,)
            sys.exit(1)
        if not len(buf):
            break
        # write the received data
        sys.stdout.write(buf    )
error_handling()