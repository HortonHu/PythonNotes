#!/usr/bin/env python
# -*- coding:utf-8 -*-

# SQLite
# Python定义了一套操作数据库的API接口，任何数据库要连接到Python，只需要提供符合Python标准的数据库驱动即可。
# 由于SQLite的驱动内置在Python标准库中，所以我们可以直接来操作SQLite数据库。

import sqlite3                        # 导入SQLite驱动:
conn = sqlite3.connect('test.db')      # 连接到SQLite数据库文件test.db   如果文件不存在，会自动在当前目录创建:
cursor = conn.cursor()                 # 创建一个Cursor:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')  # 执行一条SQL语句，创建user表:
cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')           # 继续执行一条SQL语句，插入一条记录:
print cursor.rowcount                  # 通过rowcount获得插入的行数:
cursor.close()                          # 关闭Cursor:
conn.commit()                           # 提交事务
conn.close()                            # 关闭Connection

# 查询记录
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('select * from user where id=?', ('1',))     # 执行查询语句
values = cursor.fetchall()                                  # 获得查询结果集:
print values
cursor.close()
conn.close()

# 使用Python的DB-API时，只要搞清楚Connection和Cursor对象，打开后一定记得关闭，就可以放心地使用。
# 使用Cursor对象执行insert，update，delete语句时，执行结果由rowcount返回影响的行数，就可以拿到执行结果。
# 使用Cursor对象执行select语句时，通过featchall()可以拿到结果集。结果集是一个list，每个元素都是一个tuple，对应一行记录。
# 如果SQL语句带有参数，那么需要把参数按照位置传递给execute()方法，有几个?占位符就必须对应几个参数
cursor.execute('select * from user where name=? and pwd=?', ('abc', '123456'))


# 在Python中操作数据库时，要先导入数据库对应的驱动，然后，通过Connection对象和Cursor对象操作数据。
# 要确保打开的Connection对象和Cursor对象都正确地被关闭，否则，资源就会泄露。
# 如何才能确保出错的情况下也关闭掉Connection对象和Cursor对象呢？请回忆try:...except:...finally:...的用法。


