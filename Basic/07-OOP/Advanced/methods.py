# -*- coding:utf-8 -*-


# Python的方法分类
# Python其实有3种方法,即
# 静态方法(staticmethod)    使用@staticmethod装饰器
# 类方法(classmethod)       使用@classmethod装饰器
# 实例方法
class A(object):
    def foo(self,x):
        print "executing foo(%s,%s)"%(self, x)

    @classmethod
    def class_foo(cls, x):
        print "executing class_foo(%s,%s)" % (cls, x)

    @staticmethod
    def static_foo(x):
        print "executing static_foo(%s)" % x

a = A()
# 对于实例方法,我们知道在类里每次定义方法的时候都需要绑定这个实例,就是foo(self, x)
# 为什么要这么做呢?因为实例方法的调用离不开实例,我们需要把实例自己传给函数
# 调用的时候是这样的a.foo(x)(其实是foo(a, x)).
# 类方法一样,只不过它传递的是类而不是实例,A.class_foo(x).
# 注意这里的self和cls可以替换别的参数,但是python的约定是这俩,还是不要改的好.
# 对于静态方法其实和普通的方法一样,不需要对谁进行绑定,
# 唯一的区别是调用的时候需要使用a.static_foo(x)或者A.static_foo(x)来调用.
