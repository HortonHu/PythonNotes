#!/usr/bin/env python
# -*- coding:utf-8 -*-

import MySQLdb
try:
    # 连接mysql 创建connection
    conn = MySQLdb.connect(host='localhost', user='hortonhu', passwd='123456', db='mysql', port=3306)
    # 创建cursor
    cur = conn.cursor()

    # 执行语句
    cur.execute('select * from user')
    info = cur.fetchall()
    print type(info)
    for i in info:
        print i[0]

    # 关闭cursor 关闭connection
    cur.close()
    conn.close()
except MySQLdb.Error, e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])


