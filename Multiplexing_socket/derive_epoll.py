#coding:UTF-8

import select
import socket
import struct
import cPickle
import argparse

SERVER_HOST = "localhost"
EOL1 = b'\n\n'
EOL2 = b'\n\r\n'
SERVER_RESPONSE = b"""HTTP/1.1 200 OK\r\nDate: Mon, 1 Apr 2013 01:01:01\
GMT\r\nContent-type: text/plain\r\nContent-Length: 25\r\n\r\n
Hello from Epoll Server!"""

# def send(channel, **kwargs):
#     num = len(kwargs)
#     data = cPickle.dumps(kwargs)
#     value = socket.htonl(len(data))
#     size = struct.pack("L", value)
#     channel.send(size)
#     channel.send(data)
#     return num
#
#
# def receive(channel):
#     size = struct.calcsize("L")
#     size = channel.recv(size)
#     try:
#         size = socket.ntohl(struct.unpack("L", size)[0])
#     except struct.error, e:
#         return ''
#     buff = ''
#     print size
#     while len(buff) < size:
#         buff += channel.recv(size - len(buff))
#     return cPickle.loads(buff)[0]


class EpollServer(object):

    def __init__(self, host, port):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
        self.server.setblocking(0)
        self.server.bind((host, port))
        self.server.listen(1)
        print "Start epoll ........"
        self.epoll = select.epoll()
        self.epoll.register(self.server.fileno(), select.EPOLLIN)


    def run(self):
        try:
            requests = {}; responses = {}; connections = {}
            while True:
                events = self.epoll.poll(1)
                for fb, event in events:
                    if fb == self.server.fileno():
                        connection, address = self.server.accept()
                        connection.setblocking(0)
                        self.epoll.register(connection.fileno(), select.EPOLLIN)
                        connections[connection.fileno()] = connection
                        requests[connection.fileno()] = b''
                        responses[connection.fileno()] = SERVER_RESPONSE
                    elif event & select.EPOLLIN:
                        requests[fb] += connections[fb].recv(1024)
                        if EOL1 in requests[fb] or EOL2 in requests[fb]:
                            self.epoll.modify(fb, select.EPOLLOUT)
                            print ('-'*40 + '\n'+ requests[fb].decode()[:-2])
                    elif event & select.EPOLLOUT:
                        byteswritten = connections[fb].send(responses[fb])
                        responses[fb] = responses[fb][byteswritten:]
                        if len(responses[fb]) == 0:
                            self.epoll.modify(fb, 0)
                            connections[fb].shutdown(socket.SHUT_RDWR)
                    elif event & select.EPOLLHUP:
                        self.epoll.unregister(fb)
                        connections[fb].close()
                        del connections[fb]
        except KeyboardInterrupt, e:
            pass
        finally:
            self.epoll.unregister(self.server.fileno())
            self.epoll.close()
            self.server.close()

if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--port', action="store", dest="port", type=int, help="server port", required=True)
    # given_args = parser.parse_args()
    # port = given_args.port
    port = 8090
    server = EpollServer(SERVER_HOST, port)
    server.run()









