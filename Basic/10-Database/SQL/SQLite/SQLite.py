#!/usr/bin/env python
# -*- coding:utf-8 -*-

# SQLite
# SQLite是一种嵌入式数据库，它的数据库就是一个文件。
# Python就内置了SQLite3，所以，在Python中使用SQLite，不需要安装任何东西，直接使用

# SQLite
import sqlite3
conn = sqlite3.connect('test.db')      # 连接到SQLite数据库文件test.db   如果文件不存在，会自动在当前目录创建:
cursor = conn.cursor()                 # 创建一个Cursor游标 通过Cursor执行SQL语句
cursor.execute('''create table %s (id varchar(20) primary key, name varchar(20))''' % 'test')    # 创建user表:
cursor.execute('insert into test (id, name) values (?, ?)', (1, u'昊天'))              # 插入一条记录
print 'inset row number is %s' % cursor.rowcount                                         # 通过rowcount获得插入的行数
cursor.execute('select * from user where id=?', ('1',))                                 # 传入参数执行查询语句
values = cursor.fetchall()                                                                # 获得查询结果集:
print 'the data id = 1 in table user is %s' % values
cursor.close()                          # 关闭Cursor:
conn.commit()                           # 提交
conn.close()                            # 关闭Connection
# 要确保打开的Connection对象和Cursor对象都正确地被关闭，否则，资源就会泄露。
# 为确保出错的情况下也关闭掉Connection对象和Cursor对象呢可以使用try:...except:...finally:...



