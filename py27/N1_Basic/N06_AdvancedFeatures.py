#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 切片 Slice
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print L[0:3]
print L[1:3]
print L[-2:]
print L[::2]

# 迭代 Iteration
# 默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.itervalues()
# 如果要同时迭代key和value，可以用for k, v in d.iteritems()
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print key
    pass

for value in d.itervalues():  # 迭代value
    print value
    pass

for k, v in d.iteritems():  # 同时迭代key和value
    print k, 'is the key of', v
    pass

# 通过collections模块的Iterable类型判断是否可迭代
from collections import Iterable

print isinstance('abc', Iterable)
print isinstance([1, 2, 3], Iterable)
print isinstance(123, Iterable)

# 同时迭代索引和元素本身 enumerate函数可以把一个list变成索引-元素对
for i, value in enumerate(['A', 'B', 'C']):
    print i, value
    pass

# 列表生成式 List Comprehensions 替代简单的循环
print [x * x for x in range(1, 11)]
print [x * x for x in range(1, 11) if x % 2 == 0]  # 筛选出仅偶数的平方
print [m + n for m in 'ABC' for n in 'XYZ']  # 使用两层循环，可以生成全排列
print [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
d = {'x': 'A', 'y': 'B', 'z': 'C'}
print [k + '=' + v for k, v in d.iteritems()]  # 同时迭代k,v
L = ['Hello', 'World', 'IBM', 'Apple']
print [s.lower() for s in L]  # 改为小写
L = ['Hello', 'World', 18, 'Apple', None]
print [s.lower() if isinstance(s, str) else s for s in L]      # 引入判断 变成条件表达式

# 生成器 Generator
# generator保存的是算法  算完之后就没有了
# 创建L和g的区别仅在于最外层的[]和()
g = (x * x for x in range(5))
print g.next()
print g.next()
print g.next()
print g.next()
print g.next()

for n in g:
    print n


# 一个函数定义中包含yield关键字，那这个函数就编程 generater
# generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
# generator的工作原理，它是在for循环的过程中不断计算出下一个元素，并在适当的条件结束for循环。
# 对于函数改成的generator来说，遇到return语句或者执行到函数体最后一行语句，就是结束generator的指令，for循环随之结束
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1


a = fib(6)
print a.next()
print a.next()
print a.next()
print a.next()
print a.next()
print a.next()


def odd():
    print 'step 1'
    yield 1
    print 'step 2'
    yield 3
    print 'step 3'
    yield 5


o = odd()
o.next()
o.next()
o.next()



