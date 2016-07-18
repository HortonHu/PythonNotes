# -*- coding:utf-8 -*-


# __new__(cls, *args, **kwargs)
# 在创造一个新实例时被调用，新式类才有,通常用于定制不变对象类的子类和实现自定义的metaclass
# 如果__new__返回了一个实例则会调用__init__，如果没有返回实例则不回调用__init__
# 如果要得到当前类的实例，应当在当前类中的__new__方法语句中调用当前类的父类的__new__方法。
# 如果当前类没有定义__new__则会自动返回父类的__new__一直到object的__new__
# 注意不能返回自身的__new__否则会造成死循环
class A(object):
    def __init__(self):
        print "init"

    def __new__(cls, *args, **kwargs):
        print "new %s" % cls
        return object.__new__(cls, *args, **kwargs)

a = A()

# __init__(self)
# 从__new__方法接收创造出的实例作为self即第一个参数 然后进行初始化
