# -*- coding:utf-8 -*-

# 新式类（new-style classes）：所有从object继承的类都是，包括所有的内置类
# 旧式类（new-style classes）：没有从object继承的类
# Python2.2之前只有旧式类
# Python2.2才引入了新式类
# Python3以后 只有新式类


# 处理多重继承的时候，继承的属性MRO（Method Resolution Order）方法顺序有所不同
# 参考 http://www.xymlife.com/2016/05/22/python_mro/
# Python2.2以前（旧式类MRO为DFS）
# Python2.2版本（旧式类MRO为DFS）（新式类MRO为BFS）
# Python2.2以后（旧式类MRO为DFS）（新式类MRO为C3）
# Python3  以后（新式类MRO为C3）
# DFS算法（深度优先搜索（子节点顺序：从左到右））
# BFS算法（广度优先搜索（子节点顺序：从左到右））
# C3算法
class D(object):        # 此时D是新式类，如果去掉object就是旧式类
    def foo(self):
        print "class D"


class B(D):
    pass


class C(D):
    def foo(self):
        print "class C"


class A(B, C):
    pass

f = A()
f.foo()
# 新式类采用C3算法，输出"class C"
# Python2.7下旧式类采用MRO算法广度优先，输出"class D"


# 旧式类的type(instance)永远是<type 'instance'>
# 新式类的type(instance)和instance.__class__结果是一样的
class A():
    pass


class B(object):
    pass

a = A()
b = B()
print type(a), a.__class__
print type(b), b.__class__
