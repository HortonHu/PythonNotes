# -*- coding:utf-8 -*-


# ORM：Object-Relational Mapping
# ORM就是把关系数据库的表结构映射到对象上, python中比较常用的是SQLAlchemy模块
# 数据库表是一个二维表，包含多行多列。把一个表的内容用Python的数据结构表示出来的话，
# 可以用一个list表示多行，list的每一个元素是tuple，表示一行记录
# 比如，包含id和name的user表：
table_User = [('1', 'Michael'), ('2', 'Bob'), ('3', 'Adam')]


# Python的DB - API返回的数据结构就是像上面这样表示的。
# 用tuple表示一行很难看出表的结构。如果把一个tuple用class实例来表示，就可以更容易地看出表的结构来：
class User(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name

User('1', 'Michael')
User('2', 'Bob')
User('3', 'Adam')
