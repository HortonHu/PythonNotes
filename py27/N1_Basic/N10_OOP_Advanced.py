#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。
# 给一个实例绑定的方法，对另一个实例是不起作用的：
class Student(object):
        pass

s = Student()
s.name = 'horton'
print s.name


def set_score(self, score):
    self.score = score

from types import MethodType
s.set_score = MethodType(set_score, s, Student)
s.set_score(100)
print s.score


# 为了给所有实例都绑定方法，可以给class绑定方法 给class绑定方法后，所有实例均可调用：
def set_score(self, score):
        self.score = score

Student.set_score = MethodType(set_score, None, Student)


# __slots__
# 为了限制class的属性
# Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class能添加的属性：
class Student(object):
        __slots__ = ('name', 'age')     # 用tuple定义允许绑定的属性名称

s = Student()
s.name = 'horton'
s.age = 22
s.score = 100       # 由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。


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


# 为了限制score的范围，可以通过一个set_score()方法来设置成绩，再通过一个get_score()来获取成绩，
# 这样，在set_score()方法里，就可以检查参数：
class Student(object):
    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.set_score(60)
s.get_score()
s.set_score(999)        # error


# @property装饰器
# Python内置的property装饰器就是负责把一个方法变成属性调用的：
# 把一个getter方法变成属性，只需要加上@property就可以
# @property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
class Student(object):
    @property
    def score(self):        # 这是一个getter方法
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 60        # 方法编程属性
s.score
s.score = 999       # error


# 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
# birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来。
class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2016 - self._birth


# 多重继承
class Animal(object):       # 整体
    pass


# 大类:
class Mammal(Animal):       # 哺乳动物
    def mam(self):
        print 'It is mammal.'
    pass


class Bird(Animal):         # 鸟类
    def bir(self):
        print 'It is bird'
    pass


# 各种动物:
class Dog(Mammal):          # 狗
    pass


class Bat(Mammal):          # 蝙蝠
    pass


class Parrot(Bird):         # 鹦鹉
    pass


class Ostrich(Bird):        # 鸵鸟
    pass


class Runnable(object):     # 能跑
    def run(self):
        print('Running   ')


class Flyable(object):      # 能飞
    def fly(self):
        print('Flying   ')


# 多重继承
# 对于需要Runnable功能的动物，就多继承一个Runnable，例如Dog：
class Dog(Mammal, Runnable):
    pass


# 对于需要Flyable功能的动物，就多继承一个Flyable，例如Bat：
class Bat(Mammal, Flyable):
    pass

d = Dog()
d.mam()
d.run()

# Mixin：多重继承的设计
# 由于Python允许使用多重继承，因此，Mixin就是一种常见的设计。
# 只允许单一继承的语言（如Java）不能使用Mixin的设计。
# 在设计类的时候，我们优先考虑通过多重继承来组合多个Mixin的功能，而不是设计多层次的复杂的继承关系。


# 定制类
# __str__   返回用户看到的字符串
# __repr__  返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__      # 偷懒写法 因为通常__repr__和__str__内容一致

print Student('Horton')


# __iter__
# 如果一个类想被用于for ... in循环，就必须实现一个__iter__()方法，该方法返回一个迭代对象
# 然后，Python的for循环就会不断调用该迭代对象的next()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1       # 初始化两个计数器a，b

    def __iter__(self):
        return self                 # 实例本身就是迭代对象，故返回自己

    def next(self):
        self.a, self.b = self.b, self.a + self.b    # 计算下一个值
        if self.a > 100000:          # 退出循环的条件
            raise StopIteration()
        return self.a               # 返回下一个值

for n in Fib():
    print


# __getitem__
# 像list那样按照下标取出元素，需要实现__getitem__()方法：
class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

f = Fib()
print f[0]
print f[1]
print f[2]
print f[5]
print f[10]
print f[100]

# 但是对于list的slice操作却会报错
# __getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断：
class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

f = Fib()
print f[0:5]
print f[:10]
# 但是也没有step参数和负数 要正确实现一个__getitem__()还是有很多工作要做的


# __getattr__
# 调用不存在的属性时 为避免错误写一个__getattr__()方法，动态返回一个属性
class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr=='score':
            return 99

s = Student()
print s.name
print s.score
print s.abc
# 在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找
# 任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None。


# 要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误：
class Student(object):
    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
# 把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段



#  __call__

# 使用元类







