# -*- coding:utf-8 -*-


# property 装饰器
# Python内置的property装饰器就是负责把一个方法变成属性调用的：
# 把一个getter方法变成属性，只需要加上@property就可以
# property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
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
s.score = 60        # 方法作为属性调用
s.score
s.score = 999       # error


# 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
# 例如：
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
