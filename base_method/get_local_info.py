# coding:UTF-8

import socket
from binascii import hexlify

def convert_ipv4_address():
    """
        讲IP地址进行 打包 解包并格式输出
    """
    for ip_addr in ["127.0.0.1", "192.168.8.101"]:
        # 将IP地址打包成32位的二进制格式
        pack_ip_addr = socket.inet_aton(ip_addr)
        # 解包必须根据打包的地址进行
        unpack_ip_addr = socket.inet_ntoa(pack_ip_addr)
        # 输出时讲二进制转化为十六进制表示，进行输出
        print "IP Address : %s => packed: %s , Unpacked: %s" \
        % (ip_addr, hexlify(pack_ip_addr), unpack_ip_addr)

def find_server_name():
    """
        根据PORT 找到对应的服务名称
    :return:
    """
    protocol_name = "TCP"
    for port in [80, 25 ,21, 53]:
        server_name = socket.getservbyport(port)
        print "PORT : %s , SERVER_NAME : %s" % (port, server_name, )

def convert_integer():
    """
        主机字节序和网络字节序之间的相互转换
    """
    # 数据只能是int类型
    data = 1234
    # 32-bit
    n_h_l = socket.ntohl(data)
    h_n_l = socket.htonl(data)
    print "Original: %s, Long host byte order : %s, Long Network byte order : %s" \
          % (data, n_h_l, h_n_l,)
    # 16-bit
    n_h_s = socket.ntohs(data)
    h_n_s = socket.ntohs(data)
    print "Original: %s, Long host byte order : %s, Long Network byte order : %s" \
           % (data, n_h_s, h_n_s,)


def socket_timeout():
    """
        更改套接字超时时间
    """
    # 第一个参数： 地址族、第二个参数：套接字类型
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    timeout = s.gettimeout()
    print timeout
    s.settimeout(5)
    print s.gettimeout()


i