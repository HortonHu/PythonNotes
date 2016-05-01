#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 网络通信是两台计算机上的两个进程之间的通信
# 用Python进行网络编程，就是在Python程序本身这个进程内，连接别的服务器进程的通信端口进行通信。


# TCP/IP简介
# 互联网协议包含了上百种协议标准，但是最重要的两个协议是TCP和IP协议，所以，大家把互联网的协议简称TCP/IP协议。
# IP协议负责把数据从一台计算机通过网络发送到另一台计算机。数据被分割成一小块一小块，然后通过IP包发送出去。
# 由于互联网链路复杂，两台计算机之间经常有多条线路，因此，路由器就负责决定如何把一个IP包转发出去。
# IP包的特点是按块发送，途径多个路由，但不保证能到达，也不保证顺序到达。
# TCP协议则是建立在IP协议之上的。TCP协议负责在两台计算机之间建立可靠连接，保证数据包按顺序到达。
# TCP协议会通过握手建立连接，然后，对每个IP包编号，确保对方按顺序收到，如果包丢掉了，就自动重发。
# 许多常用的更高级的协议都是建立在TCP协议基础上的，比如用于浏览器的HTTP协议、发送邮件的SMTP协议等。

# 端口
# 有什么作用？在两台计算机通信时，只发IP地址是不够的，因为同一台计算机上跑着多个网络程序。
# 一个IP包来了之后，到底是交给浏览器还是QQ，就需要端口号来区分。每个网络程序都向操作系统申请唯一的端口号，
# 这样，两个进程在两台计算机之间建立网络连接就需要各自的IP地址和各自的端口号。
# 一个进程也可能同时与多个计算机建立链接，因此它会申请很多端口。


# TCP编程
# Socket是网络编程的一个抽象概念。通常我们用一个Socket表示“打开了一个网络链接”，
# 而打开一个Socket需要知道目标计算机的IP地址和端口号，再指定协议类型即可。

# 客户端
# 大多数连接都是可靠的TCP连接。创建TCP连接时，主动发起连接的叫客户端，被动响应连接的叫服务器。


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




