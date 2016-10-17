# coding:UTF-8

import socket
import sys
import argparse

server_host = '127.0.0.1'

def echo_client(port):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, e:
        print "Create client socket failed cause of %s" % (e,)
        sys.exit(1)
    ip_addr = (server_host, port)
    try:
        client.connect(ip_addr)
    except socket.gaierror, e:
        print "Address-related error connecting to server :%s" % (e,)
        sys.exit(1)
    except socket.error, e:
        print "Connect error %s" % (e,)
        sys.exit(1)
    print "Connect to Server %s " % (ip_addr,)
    try:
        message = 'Test Message , This will be echoed '
        client.sendall(message)
        amount_reseived = 0
        amount_expected = len(message)
        temp = ''
        while amount_reseived < amount_expected:
            data = client.recv(16)
            amount_reseived += len(data)
            temp += data
        print "Get data : %s from server " % (temp)
    except socket.errno, e:
        print "Socket error: %s" % (e,)
    except Exception, e:
        print "Other exception %s" % (str(e),)
    finally:
        print "Closing connection to the server"
        client.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', action="store", dest="port", type=int, help="server socket port", required=False)
    args_given = parser.parse_args()
    port = args_given.port
    echo_client(port)