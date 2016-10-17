# coding:UTF-8

import socket

def block_socket_build():
    """
        设置阻塞模式的套接字连接
    :return:
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 1为阻塞， 0 为非阻塞 
    s.setblocking(1)
    s.settimeout(0.5)
    s.bind(('127.0.0.1',0))
    socket_address = s.getsockname()
    print "Trivial Server launched on socket: %s" %str(socket_address)

    while True:
        s.listen(1)