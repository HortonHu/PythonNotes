# -*- coding:utf-8 -*-


import httplib

conn1 = None

try:
    # conn1 = httplib.HTTPConnection('121.40.213.161', 80, timeout=30)
    conn1 = httplib.HTTPConnection('www.baidu.com', timeout=30)
    conn1.request('GET', '/')
    response = conn1.getresponse()
    print response.status
    print response.reason
    print response.read()
except Exception, e:
    print e
finally:
    if conn1:
        conn1.close()