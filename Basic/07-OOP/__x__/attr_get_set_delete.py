# -*- coding:utf-8 -*-


# __getattr__
# 从对象中读取某个属性时，首先需要从self.__dicts__中搜索该属性，再从__getattr__中查找
# 调用不存在的属性时 为避免错误写一个__getattr__()方法，动态返回一个属性
class Student(object):
    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr=='score':
            return 99

s = Student()
print s.name
print s.score
print s.abc
# 在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找
# 任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None。


# 要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误：
class Student(object):
    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
# 把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段


# __setattr__
# 用来设置对象的属性，通过object中的__setattr__函数来设置属性：
class A(object):
    def __setattr__(self, *args, **kwargs):
        print 'call func set attr'
        return object.__setattr__(self, *args, **kwargs)


# __delattr__
# 用来删除对象的属性：
class B(object):
    def __delattr__(self, *args, **kwargs):
        print 'call func del attr'
        return object.__delattr__(self, *args, **kwargs)