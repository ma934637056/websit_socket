#coding:UTF-8

import asyncore
import socket
# 解析asyncore源码

class PortForwarder(asyncore.dispatcher):

    def __init__(self, ip, port, remote_ip, remote_port, backlog=5):
        super(PortForwarder, self).__init__()
        self.remote_ip = remote_ip
        self.remote_port = remote_port
        # create_socket 创建socket实例，设置非阻塞，并加入add_channel方法添加格式map[fd]=obj
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((ip, port))
        self.listen(backlog)

    def handle_accept(self):
        conn, addr = self.accept()
        print "Connect to : " + addr


