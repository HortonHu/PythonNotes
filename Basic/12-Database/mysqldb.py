#!/usr/bin/env python
# -*- coding:utf-8 -*-

# MySQLdb模块
# 命令行启动MySQL: net start mysql 关闭 net stop MySQL
import MySQLdb
try:
    conn = MySQLdb.connect(host='localhost', user='hortonhu', passwd='123456', db='mysql', port=3306)
    cur = conn.cursor()

    cur.execute('select * from user')
    info = cur.fetchall()
    print type(info)
    for i in info:
        print i[0]

    cur.close()
    conn.close()
except MySQLdb.Error, e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])


