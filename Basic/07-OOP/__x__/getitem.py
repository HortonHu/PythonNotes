# -*- coding:utf-8 -*-


# __getitem__
# 像list那样按照index取出元素，需要实现__getitem__()方法：
class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

f = Fib()
print f[0]
print f[1]
print f[2]
print f[5]
print f[10]
print f[100]

# 但是对于list的slice操作却会报错
# __getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断：
class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

f = Fib()
print f[0:5]
print f[:10]
# 但是也没有step参数和负数 要正确实现一个__getitem__()还是有很多工作要做的
