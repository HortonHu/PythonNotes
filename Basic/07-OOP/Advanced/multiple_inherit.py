# -*- coding:utf-8 -*-


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