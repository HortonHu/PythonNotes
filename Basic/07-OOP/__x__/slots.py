# -*- coding:utf-8 -*-


# __slots__ 槽
# 为了限制class的属性
# Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class能添加的属性：
class Student(object):
        __slots__ = ('name', 'age')     # 用tuple定义允许绑定的属性名称

s = Student()
s.name = 'horton'
s.age = 22
s.score = 100       # 由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。

# 在Python中，每个类都有实例属性。默认情况下Python用一个字典来保存一个对象的实例属性。
# 对于有着已知属性的小类来说，它可能是个瓶颈。这个字典浪费了很多内存。
# Python不能在对象创建时直接分配一个固定量的内存来保存所有的属性。
# 因此如果你创建许多对象（我指的是成千上万个），它会消耗掉很多内存。
# 使用__slots__来告诉Python不要使用字典，而且只给一个固定集合的属性分配空间。因此可以减少内存消耗。


# __slots__定义的属性仅对当前类起作用，对继承的子类是不起作用的：
# 即如果子类没有__slots__则可以随意定义属性 如果有则只能定义自身的__slots__和父类的__slots__之和
class A(object):
    __slots__ = ('name', 'age')
    pass


class B(A):
    __slots__ = ('score')
    pass

c = B()
c.name = 1
c.age = 2
c.score = 3


# http://tech.oyster.com/save-ram-with-python-slots/
