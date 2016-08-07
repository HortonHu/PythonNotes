#!/usr/bin/env python
# -*- coding:utf-8 -*-

# MySQL
# 由于MySQL服务器以独立的进程运行，并通过网络对外服务，所以，需要支持Python的MySQL驱动来连接到MySQL服务器。
# 目前有两个MySQL驱动
# mysql-connector-python：是MySQL官方的纯Python驱动；
# MySQL-python：是封装了MySQL C驱动的Python驱动。

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


