# -*- coding:utf-8 -*-

# 新式类（new-style classes）：所有从object继承的类都是，包括所有的内置类
# 旧式类（new-style classes）：没有从object继承的类


# 处理多重继承的时候，继承的属性方法等的顺序有所不同
# 旧式类（old-style classes）是按照深度优先。MRO（Method Resolution Order）方法
# 新式类（new-style classes）的按照广度优先。C3算法
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
# 新式类采用C3算法广度优先，输出"class C"
# 旧式类采用MRO算法广度优先，输出"class D"


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
