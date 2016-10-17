#coding:UTF-8

import socket
import time
import struct

TIME1970 = 2208988800L
NTP_SERVER = 'europe.pool.ntp.org'

def sntp_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = '\x1b' +47 * '\0'
    # 向ntp服务器发送data
    s.sendto(data, (NTP_SERVER, 123))
    # 接收response
    data, address = s.recvfrom(1024)
    if data:
        print "Response reseive from %s" % (address,)
        # 取出数据
        t = struct.unpack('!12L', data)[10]
        # 减去1970.1.1 得到时间戳
        t -= TIME1970
    # 打印
    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t))

sntp_client()