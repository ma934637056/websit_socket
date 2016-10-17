# coding:UTF-8

import socket

SEND_BUF_SIZE = 4096
RECV_BUF_SIZE =4096

def modify_buff_size():
    """
        更改套接字的接/收buff size
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # get sed buffer
    # getsockopt(level, optname, value)  level所在的协议层level（SOL_SOCKET/SOL_TCP） ,
    # optname （SO_SNDBUF/SO_RCVBUF）
    # value 值的大小
    buf_size = s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print "Buffer size [before]: %d" %(buf_size,)
    s.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, SEND_BUF_SIZE)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, RECV_BUF_SIZE)
    print "Buffer size [after]: %s" %(s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF))


