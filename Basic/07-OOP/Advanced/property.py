# -*- coding:utf-8 -*-


# property 装饰器
# 把一个方法变成属性来调用的
# getter方法变成属性，只需要加上@property就可以
# property可以创建装饰器@score.setter，负责把一个setter方法变成属性赋值
# property可以创建装饰器@score.deleter，负责把属性删除
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

    @score.deleter
    def score(self):
        raise TypeError('Can \'t delete score!')

s = Student()
s.score = 60        # 把方法作为属性调用 setter
print s.score       # getter
s.score = 999       # error
del s.score         # error deleter


# 定义只读属性
# 只定义getter方法，不定义setter方法就是一个只读属性：
# 例如： birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来。
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
