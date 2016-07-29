# -*- coding:utf-8 -*-


import socket
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
# 端口号需要预先指定。因为我们写的这个服务不是标准服务，所以用9999这个端口号
# 小于1024的端口号必须要有管理员权限才能绑定：

# 绑定端口:
s.bind(('127.0.0.1', 9999))
# 调用listen()方法开始监听端口，传入的参数指定等待连接的最大数量：
s.listen(5)
print 'Waiting for connection...'


# 连接建立后，服务器首先发一条欢迎消息，然后等待客户端数据，并加上Hello再发送给客户端。
# 如果客户端发送了exit字符串，就直接关闭连接。
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


# 服务器程序通过一个永久循环来接受来自客户端的连接，accept()会等待并返回一个客户端的连接:
# 每个连接都必须创建新线程（或进程）来处理，否则，单线程在处理连接的过程中，无法接受其他客户端的连接：
import threading
while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
