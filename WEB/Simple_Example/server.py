#!/usr/bin/env python
# -*- coding:utf-8 -*-

from wsgiref.simple_server import make_server       # 从wsgiref模块导入:
from hello import application


httpd = make_server('', 8000, application)      # 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
print "Serving HTTP on port 8000..."
httpd.serve_forever()                           # 开始监听HTTP请求:

