# -*- coding:utf-8 -*-


# 链式调用 __call__
# 定义一个__call__()方法，就可以直接对实例进行调用
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

s = Student('Michael')
s()
# __call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，
# 所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。
# 能被调用的对象就是一个Callable对象，比如函数和我们上面定义的带有__call()__的类实例：
# 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象
print callable(Student())
print callable(max)
print callable([1, 2, 3])
print callable(None)
print callable('string')
