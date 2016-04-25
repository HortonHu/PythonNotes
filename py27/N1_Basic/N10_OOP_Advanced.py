#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 给所有实例都绑定方法，可以给class绑定方法：
class Student(object):
        pass

from types import MethodType


def set_score(self, score):
        self.score = score

Student.set_score = MethodType(set_score, None, Student)
# 给class绑定方法后，所有实例均可调用：
# 动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。


# 使用__slots__
# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class能添加的属性：
class Student(object):
        __slots__ = ('name', 'age')     # 用tuple定义允许绑定的属性名称

s = Student()
s.name = 'horton'
s.age = 22
s.score = 100       # 由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。


# __slots__定义的属性仅对当前类起作用，对继承的子类是不起作用的：
# 除非在子类中也定义__slots__，这样，子类允许定义的属性就是自身的__slots__加上父类的__slots__。
class A(object):
    __slots__ = ('name','age')
    pass


class B(A):
    __slots__ = ('score')
    pass

c = B()
c.name = 1
c.age = 2
c.score = 3


# 使用@property
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


# Python内置的@property装饰器就是负责把一个方法变成属性调用的：
# 把一个getter方法变成属性，只需要加上@property就可以
# @property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 60
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
        return 2014 - self._birth


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
        print('Running...')


class Flyable(object):      # 能飞
    def fly(self):
        print('Flying...')


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

# 以上的设计称为Mixin
# 由于Python允许使用多重继承，因此，Mixin就是一种常见的设计。
# 只允许单一继承的语言（如Java）不能使用Mixin的设计。


# 定制类
# __str__ 和 __repr__


# __iter__


# __getitem__


# __getattr__


#  __call__

# 使用元类







