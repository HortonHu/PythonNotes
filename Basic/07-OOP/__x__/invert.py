# -*- coding:utf-8 -*-


# 定义了__invert__就可以支持~操作
class X(object):
    def __invert__(self):
        return 42
x = X()

print ~x
# 42
