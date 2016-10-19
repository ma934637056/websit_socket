#coding:UTF-8

import os
import argparse
import cPickle
import select
import socket
import signal
import struct
import sys
ADDR = "localhost"

#套接字建立连接是一次IO，连接的数据抵达也是一次IO


def send(channel, **kwargs):
    buffer = cPickle.dumps(kwargs)
    value = socket.htonl(len(buffer))
    size = struct.pack("L", value)
    channel.send(size)
    channel.send(buffer)


def receive(channel):
    size = struct.calcsize("L")
    size = channel.resv(size)
    try:
        size = socket.htonl(struct.unpack("L", size)[0])
    except struct.error, e:
        return ''
    buf = ''
    while len(buf) < size:
        buf += channel.resv(size - len(buf))
    return cPickle.loads(buf)


class ChatServer(object):

    def __init__(self, port, backlog):
        self.client = 0
        self.clientmap = {}
        self.outputs = []
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((ADDR, port))
        self.sock.listen(backlog)
        signal.signal(signal.SIGINT, self.signalhandler)

    def signalhandler(self):
        print "Server is stopping !"
        for output in self.outputs:
            output.close()
        self.sock.close()

    def get_client_name(self, client,):
        info = self.clientmap[client]
        host_add, cname = info[0][0], info[1]
        return '@'.join(cname, host_add)

    def run(self):
        input = [self.sock, sys.stdin]
        running = True
        while running:
            try:
                readable, writeable, errorable = select.select(input, self.outputs, [])
            except select.error, e:
                break
            for sock in readable:
                if sock == self.sock:
                    connction, address = sock.accept()
                    print "Char Server get connection %d from %s " %(connction.nofile, address)
                    cname = receive(connction).split("NAME: ")[1]
                    self.client += 1
                    input.append(connction)
                    client_msg = "CLIENT: " + str(address[0])
                    send(connction, client_msg)
                    self.clientmap[connction] = [address, cname]
                    msg = "\n Connected: New client (%d) from %s" % (self.client, self.get_client_name(connction))
                    for output in self.outputs:
                        send(output, msg)
                    self.outputs.append(connction)
                elif sock == sys.stdin:
                    junk = sys.stdin.readline()
                    running = False
                else:
                    try:
                        data = receive(sock)
                        if data:
                            msg = '\n #[' + self.get_client_name(sock) + ']>>' + data
                            for output in self.outputs:
                                if output != sock:
                                    send(sock, msg)
                        else:
                            print "Chat server: %d hung up " % (sock.fileno())
                            self.client -= 1
                            sock.close()
                            input.remove(sock)
                            self.outputs.remove(sock)
                            msg = "\n (Now hung up : (Client from %s)" % (self.get_client_name(sock))
                            for output in self.outputs:
                                if output != sock:
                                    send(output, msg)
                    except socket.error, e:
                        input.remove(sock)
                        self.outputs.remove(sock)
        self.sock.close()