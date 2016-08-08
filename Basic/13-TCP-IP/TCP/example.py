# -*- coding:utf-8 -*-


# 创建一个基于TCP连接的Socket
# AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6。
# SOCK_STREAM指定使用面向流的TCP协议
# 作为服务器，提供什么样的服务，端口号就必须固定下来
# 80端口是Web服务的标准端口。其他服务都有对应的标准端口号，例如SMTP服务是25端口，FTP服务是21端口
# 端口号小于1024的是Internet标准服务的端口，端口号大于1024的，可以任意使用。
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)           # 创建一个socket
s.connect(('www.sina.com.cn', 80))          # 建立连接:参数是一个tuple，包含地址和端口号。


# 建立TCP连接后，向新浪服务器发送请求
# TCP连接创建的是双向通道，双方都可以同时给对方发数据。但是谁先发谁后发，怎么协调，要根据具体的协议来决定。
# 例如，HTTP协议规定客户端必须先发请求给服务器，服务器收到后才发数据给客户端。
s.send(r'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')


# 接收新浪服务器返回的数据 反复接收，直到recv()返回空数据
buffer = []
while True:
    d = s.recv(1024)        # 每次最多接收1k字节:
    if d:
        buffer.append(d)
    else:
        break
data = ''.join(buffer)
s.close()

# 接收到的数据包括HTTP头和网页本身
# 我们只需要把HTTP头和网页分离一下，把HTTP头打印出来，网页内容保存到文件：
header, html = data.split('\r\n\r\n', 1)
print header
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)