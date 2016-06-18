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
# 同时迭代key和value，可以用for k, v in d.iteritems()
d = {'a': 1, 'b': 2, 'c': 3}
for key in d.keys():            # 最好用d.keys()这个下标数组 防止出错 或者用d.iterkeys()
    print key

for value in d.itervalues():  # 迭代value
    print value

for k, v in d.iteritems():  # 同时迭代key和value
    print k, 'is the key of', v

# 通过collections模块的Iterable类型判断是否可迭代
from collections import Iterable

print isinstance('abc', Iterable)
print isinstance([1, 2, 3], Iterable)
print isinstance(123, Iterable)

# enumerate函数可以把一个list变成索引-元素对
# 同时迭代index和元素本身
for i, value in enumerate(['A', 'B', 'C']):
    print i, value

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print 'What is your {0}?  It is {1}.'.format(q, a)


# 列表生成式 List Comprehensions
# 替代简单的循环
print [x * x for x in range(1, 11)]
print [x * x for x in range(1, 11) if x % 2 == 0]   # 筛选出仅偶数的平方
print [m + n for m in 'ABC' for n in 'XYZ']         # 使用两层循环，可以生成全排列
print [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]

d = {'x': 'A', 'y': 'B', 'z': 'C'}
print [k + '=' + v for k, v in d.iteritems()]       # 同时迭代k,v
L = ['Hello', 'World', 'IBM', 'Apple']
print [s.lower() for s in L]  # 改为小写
L = ['Hello', 'World', 18, 'Apple', None]
print [s.lower() if isinstance(s, str) else s for s in L]      # 引入判断 变成条件表达式

# 生成器 Generator
# generator保存的是算法  算完之后就没有了
# 相比列表生成式更节约空间 适用于较大的生成
# 方法一：把一个列表生成式的[]改成()，就创建了一个generator：
g = (x * x for x in range(5))
print g.next()
print g.next()
print g.next()
for n in g:         # 通常都是用for来迭代出generator而不是用next()
    print n


# generator的另一种生成方式：通过函数
# 一个函数定义中包含yield关键字，那这个函数就变成generator
# generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
# generator的工作原理，它是在for循环的过程中不断计算出下一个元素，并在适当的条件结束for循环。
# 对于函数改成的generator来说，遇到return语句或者执行到函数体最后一行语句，就是结束generator的指令，for循环随之结束
def fib(max):               # 生成小于max的fib数列
    n, a, b = 0, 0, 1
    while n < max:
        yield b             # 中断 并返回b
        a, b = b, a + b
        n += 1

# 要用创建一个generator的方法而不是fib(6).next() 否则一直停在第一步
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



