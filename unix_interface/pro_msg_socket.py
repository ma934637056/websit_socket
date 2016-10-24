#coding:UTF-8

import socket
import os
import time

def socket_msg():
    parent, child = socket.socketpair()
    pid = os.fork()
    if pid:
        child.close()
        print "@Parent sending msg!"
        parent.sendall("Hello child !!!")
        reponse =parent.recv(1024)
        print "Parent reponse: %s" % (reponse,)
    else:
        print "Child waiting"
        parent.close()
        response = child.recv(1024)
        print "Child response : %s" %(response)
        print "@Child sending msg !"
        child.sendall("Hello parent !!!")


if __name__ == '__main__':
    socket_msg()