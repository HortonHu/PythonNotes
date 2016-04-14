#!/usr/bin/env python
# -*- coding:utf-8 -*-

# TCP/IP简介
# 互联网协议包含了上百种协议标准，但是最重要的两个协议是TCP和IP协议，所以，大家把互联网的协议简称TCP/IP协议。
# IP协议负责把数据从一台计算机通过网络发送到另一台计算机。数据被分割成一小块一小块，然后通过IP包发送出去。
# 由于互联网链路复杂，两台计算机之间经常有多条线路，因此，路由器就负责决定如何把一个IP包转发出去。
# IP包的特点是按块发送，途径多个路由，但不保证能到达，也不保证顺序到达。
# TCP协议则是建立在IP协议之上的。TCP协议负责在两台计算机之间建立可靠连接，保证数据包按顺序到达。
# TCP协议会通过握手建立连接，然后，对每个IP包编号，确保对方按顺序收到，如果包丢掉了，就自动重发。
# 许多常用的更高级的协议都是建立在TCP协议基础上的，比如用于浏览器的HTTP协议、发送邮件的SMTP协议等。

# 端口有什么作用？在两台计算机通信时，只发IP地址是不够的，因为同一台计算机上跑着多个网络程序。
# 一个IP包来了之后，到底是交给浏览器还是QQ，就需要端口号来区分。每个网络程序都向操作系统申请唯一的端口号，
# 这样，两个进程在两台计算机之间建立网络连接就需要各自的IP地址和各自的端口号。
# 一个进程也可能同时与多个计算机建立链接，因此它会申请很多端口。


# TCP编程
# Socket是网络编程的一个抽象概念。通常我们用一个Socket表示“打开了一个网络链接”，
# 而打开一个Socket需要知道目标计算机的IP地址和端口号，再指定协议类型即可。

# 客户端
# 大多数连接都是可靠的TCP连接。创建TCP连接时，主动发起连接的叫客户端，被动响应连接的叫服务器。


# 创建一个基于TCP连接的Socket
# AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6。SOCK_STREAM指定使用面向流的TCP协议
# 导入socket库:
import socket
# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('www.sina.com.cn', 80))      # 参数是一个tuple，包含地址和端口号。

# 作为服务器，提供什么样的服务，端口号就必须固定下来
# 80端口是Web服务的标准端口。其他服务都有对应的标准端口号，例如SMTP服务是25端口，FTP服务是21端口
# 端口号小于1024的是Internet标准服务的端口，端口号大于1024的，可以任意使用。

# 建立TCP连接后，我们就可以向新浪服务器发送请求，要求返回首页的内容：
s.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# TCP连接创建的是双向通道，双方都可以同时给对方发数据。但是谁先发谁后发，怎么协调，要根据具体的协议来决定。
# 例如，HTTP协议规定客户端必须先发请求给服务器，服务器收到后才发数据给客户端。

# 接收新浪服务器返回的数据了
# 接收数据 反复接收，直到recv()返回空数据
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = ''.join(buffer)
# 关闭连接:
s.close()

# 接收到的数据包括HTTP头和网页本身，我们只需要把HTTP头和网页分离一下，把HTTP头打印出来，网页内容保存到文件：
header, html = data.split('\r\n\r\n', 1)
print header
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)


# 服务器端
# 服务器进程首先要绑定一个端口并监听来自其他客户端的连接。
# 如果某个客户端连接过来了，服务器就与该客户端建立Socket连接，随后的通信就靠这个Socket连接了
# 服务器会打开固定端口（比如80）监听，每来一个客户端连接，就创建该Socket连接。
# 由于服务器会有大量来自客户端的连接，所以，服务器要能够区分一个Socket连接是和哪个客户端绑定的。
# 一个Socket依赖4项：服务器地址、服务器端口、客户端地址、客户端端口来唯一确定一个Socket。
# 服务器还需要同时响应多个客户端的请求，所以，每个连接都需要一个新的进程或者新的线程来处理

# 编写一个简单的服务器程序，它接收客户端连接，把客户端发过来的字符串加上Hello再发回去。
# 创建一个基于IPv4和TCP协议的Socket：
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定监听的地址和端口。服务器可能有多块网卡，可以绑定到某一块网卡的IP地址上，
# 也可以用0.0.0.0绑定到所有的网络地址，还可以用127.0.0.1绑定到本机地址。
# 127.0.0.1是一个特殊的IP地址，表示本机地址，如果绑定到这个地址，客户端必须同时在本机运行才能连接，
# 也就是说，外部的计算机无法连接进来。
# 端口号需要预先指定。因为我们写的这个服务不是标准服务，所以用9999这个端口号
# 小于1024的端口号必须要有管理员权限才能绑定：

# 监听端口:
s.bind(('127.0.0.1', 9999))
# 调用listen()方法开始监听端口，传入的参数指定等待连接的最大数量：
s.listen(5)
print 'Waiting for connection...'
# 服务器程序通过一个永久循环来接受来自客户端的连接，accept()会等待并返回一个客户端的连接:
import threading
while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()

# 每个连接都必须创建新线程（或进程）来处理，否则，单线程在处理连接的过程中，无法接受其他客户端的连接：
import time
def tcplink(sock, addr):
    print 'Accept new connection from %s:%s...' % addr
    sock.send('Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if data == 'exit' or not data:
            break
        sock.send('Hello, %s!' % data)
    sock.close()
    print 'Connection from %s:%s closed.' % addr
# 连接建立后，服务器首先发一条欢迎消息，然后等待客户端数据，并加上Hello再发送给客户端。
# 如果客户端发送了exit字符串，就直接关闭连接。

# 要测试这个服务器程序，我们还需要编写一个客户端程序：
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 9999))
# 接收欢迎消息:
print s.recv(1024)
for data in ['Michael', 'Tracy', 'Sarah']:
    # 发送数据:
    s.send(data)
    print s.recv(1024)
s.send('exit')
s.close()


