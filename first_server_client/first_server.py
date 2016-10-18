#coding:UTF-8

import socket
import argparse
import sys

IP_ADDR = '127.0.0.1'
data_payload = 4096
backlog = 5

def echo_server(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, e:
        print "Socket create failed cause of %s" % (e,)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    ip_port = (IP_ADDR, port)
    sock.bind(ip_port)
    sock.listen(backlog)
    while True:
        try:
            print "Wait for client connect......"
            client, address = sock.accept()
            print "Connected client address : %s:%s" % (address[0], address[1])
            data = client.recv(data_payload)
            if data:
                print "data : %s" % (data)
                client.sendall(data)
                print "Send %s bytes back to client %s" % (data, address)
        except KeyboardInterrupt, e:
            break
        # end connection
        client.close()
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', action="store", dest="port", type=int, help="server socket port", required=False)
    args_given = parser.parse_args()
    port = args_given.port
    echo_server(port)