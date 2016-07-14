# -*- coding:utf-8 -*-


# 动态绑定
# 允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。
# 给一个实例绑定的方法，对另一个实例是不起作用的：
class Student(object):
        pass

# 绑定属性name
s = Student()
s.name = 'horton'
print s.name


def set_score(self, score):
    self.score = score

# 绑定方法set_score
from types import MethodType
s.set_score = MethodType(set_score, s, Student)
s.set_score(100)
print s.score


# 为了给所有实例都绑定方法，可以给class绑定方法 给class绑定方法后，所有实例均可调用：
def set_score(self, score):
        self.score = score

Student.set_score = MethodType(set_score, None, Student)


