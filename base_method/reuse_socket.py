#coding:UTF-8

import socket

def reuse_socket_addr():
    """
        当你需要在同一端口运行套接字服务，或者客户端程序需要一直
        连接制定服务端口 需要socket重用
    """
    local_port = 6553
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 开启套接字重用选项, 如果没有这个选项，当python脚本接收ctrl+c 结束后，此地址不能重用
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('',local_port))
    s.listen(1)
    print "Socket listen to port %s" % (local_port)
    while True:
        try:
            connection, addr = s.accept()
            print "Connected by %s:%s" % (addr[0], addr[1])
        # 捕获ctrl+c 异常，不会显示异常信息
        except KeyboardInterrupt, e:
            break
        except socket.error, msg:
            print "%s" % (msg,)

reuse_socket_addr()
