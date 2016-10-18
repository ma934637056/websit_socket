#coding:UTF-8

import ntplib
from time import ctime, localtime,strftime


def print_time():
    ntp_client = ntplib.NTPClient()
    # 创建ntp客户端
    response = ntp_client.request('europe.pool.ntp.org')
    # response.tx_time显示的是当前时间戳， 通过localtime转化成时间 经过strftime格式化
    print strftime('%Y-%m-%d %H:%M:%S',localtime(response.tx_time))
    # 同步时间
    ctime(response.tx_time)
