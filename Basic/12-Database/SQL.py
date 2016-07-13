# -*- coding:utf-8 -*-

# SQL语法


# 数据库
# SQLite
# SQLite是一种嵌入式数据库，它的数据库就是一个文件。
# Python就内置了SQLite3，所以，在Python中使用SQLite，不需要安装任何东西，直接使用

# MySQL
# 由于MySQL服务器以独立的进程运行，并通过网络对外服务，所以，需要支持Python的MySQL驱动来连接到MySQL服务器。
# 目前有两个MySQL驱动
# mysql-connector-python：是MySQL官方的纯Python驱动；
# MySQL-python：是封装了MySQL C驱动的Python驱动。


# Python中的SQL
# Python定义了一套操作数据库的API接口，任何数据库要连接到Python，只需要提供符合Python标准的数据库驱动即可。
# 在Python中操作数据库时，要先导入数据库对应的驱动，然后，通过Connection对象和Cursor对象操作数据。
# 使用Python的DB-API时，只要搞清楚Connection和Cursor对象，打开后一定记得关闭，就可以放心地使用。

# 使用Cursor对象执行insert，update，delete语句时，执行结果由rowcount返回影响的行数，就可以拿到执行结果。
# 使用Cursor对象执行select语句时，通过featchall()可以拿到结果集。结果集是一个list，每个元素都是一个tuple，对应一行记录。
# 如果SQL语句带有参数，那么需要把参数按照位置传递给execute()方法，有几个?占位符就必须对应几个参数，如
# cursor.execute('select * from user where name=? and pwd=?', ('abc', '123456'))
# 注意sqlite中占位符是? mysql中占位符是%

