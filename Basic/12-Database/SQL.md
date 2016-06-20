# SQL语法


# Python中的SQL
- Python定义了一套操作数据库的API接口，任何数据库要连接到Python，只需要提供符合Python标准的数据库驱动即可。
- 使用Python的DB-API时，只要搞清楚Connection和Cursor对象，打开后一定记得关闭，就可以放心地使用。
- 使用Cursor对象执行insert，update，delete语句时，执行结果由rowcount返回影响的行数，就可以拿到执行结果。
- 使用Cursor对象执行select语句时，通过featchall()可以拿到结果集。结果集是一个list，每个元素都是一个tuple，对应一行记录。
- 如果SQL语句带有参数，那么需要把参数按照位置传递给execute()方法，有几个?占位符就必须对应几个参数，如
- cursor.execute('select * from user where name=? and pwd=?', ('abc', '123456'))
- 注意sqlite中占位符是? mysql中占位符是%
- 在Python中操作数据库时，要先导入数据库对应的驱动，然后，通过Connection对象和Cursor对象操作数据。
- 要确保打开的Connection对象和Cursor对象都正确地被关闭，否则，资源就会泄露。
- 为确保出错的情况下也关闭掉Connection对象和Cursor对象呢可以使用try:...except:...finally:...


# ORM技术：Object-Relational Mapping
ORM就是把关系数据库的表结构映射到对象上,python中比较常用的是SQLAlchemy模块
数据库表是一个二维表，包含多行多列。把一个表的内容用Python的数据结构表示出来的话，
可以用一个list表示多行，list的每一个元素是tuple，表示一行记录，比如，包含id和name的user表：
```    
[
     ('1', 'Michael'),
     ('2', 'Bob'),
     ('3', 'Adam')
]
```
    
Python的DB-API返回的数据结构就是像上面这样表示的。
用tuple表示一行很难看出表的结构。如果把一个tuple用class实例来表示，就可以更容易地看出表的结构来：
```
class User(object):
     def __init__(self, id, name):
         self.id = id
         self.name = name
User('1', 'Michael')
User('2', 'Bob')
User('3', 'Adam')
```