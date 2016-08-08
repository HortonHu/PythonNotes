# -*- coding:utf-8 -*-


# socket
# Python的socket模块提供了类方法和实例方法 区别是类方法使用时不需要创建套接字对象
import socket
host_name = socket.gethostname()                # 返回本地主机IP名字
IP_address = socket.gethostbyname(host_name)    # 返回对应IP地址
print host_name
print IP_address

# 获取远程设备IP地址
remote_host = 'www.python.org'
try:
    print "IP address of %s: %s" % (remote_host, socket.gethostbyname(remote_host))
except socket.error, err_msg:
    print "%s: %s" % (remote_host, err_msg)

# IPv4地址转换为不同格式
import socket
from binascii import hexlify


def convert_ip4_address():
    for ip_addr in ['127.0.0.1', '192.168.0.1']:
        packed_ip_addr = socket.inet_aton(ip_addr)                  # 转换为打包后的32位二进制格式
        unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)         # 转换为IP地址格式
        print "IP Address: %s => Packed: %s, Unpacked: %s" % (ip_addr, hexlify(packed_ip_addr), unpacked_ip_addr)

# 通过指定的端口和协议找到服务名 getservbyport(port, protocolname=None)
import socket


def find_service_name():
    protocolname = 'tcp'
    for port in [80, 25]:
        print "Port: %s => service name: %s" % (port, socket.getservbyport(port, protocolname))

    print "Port: %s => service name: %s" % (53, socket.getservbyport(53, 'udp'))

# 主机字节序和网络字节序之间相互转换
# 在底层网络应用时，需要把主机操作系统发出的数据转换为网络格式或者叫逆向转换 因为这两种数据表示方式不一样
# socket.ntohl(integer)     socket.ntohs(data)      n表示网络 h表示主机 l表示长整形 即32位 s表示短整形 即16位
import socket

def convert_integer():
    data = 1234
    # 32-bit    网络字节序转换为长整形主机字节序
    print "Original: %s => Long  host byte order: %s, Network byte order: %s" % (data, socket.ntohl(data), socket.htonl(data))
    # 16-bit
    print "Original: %s => Short  host byte order: %s, Network byte order: %s" % (data, socket.ntohs(data), socket.htons(data))

convert_integer()

# 设定并获取默认的套接字超时时间
import socket

def test_socket_timeout():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Default socket timeout: %s" %s.gettimeout()
    s.settimeout(100)
    print "Current socket timeout: %s" %s.gettimeout()

test_socket_timeout()
