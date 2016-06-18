#!/usr/bin/env python
# -*- coding:utf-8 -*-

# MySQLdb
# 命令行启动MySQL: net start mysql 关闭 net stop MySQL
import MySQLdb
try:
    conn = MySQLdb.connect(host='localhost', user='root', passwd=raw_input('DB password:'), db='mysql', port=3306)
    cur = conn.cursor()
    cur.execute('select * from user')
    cur.close()
    conn.close()
except MySQLdb.Error, e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])


# MySQL connector
import mysql.connector              # 导入MySQL驱动
# 把password设为你的root口令，在连接MySQL时传入use_unicode=True，让MySQL的DB-API始终返回Unicode
conn = mysql.connector.connect(user='root', password=raw_input('DB password:'), database='test', use_unicode=True)
cursor = conn.cursor()
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')    # 创建user表
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])       # 插入一行记录，注意MySQL的占位符是%s:
print cursor.rowcount
conn.commit()                       # 提交事务:
cursor.close()                      # 关闭cursor
# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print values                        # 输出[(u'1', u'Michael')]
cursor.close()                      # 关闭Cursor和Connection:
conn.close()
