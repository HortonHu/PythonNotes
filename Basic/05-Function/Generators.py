# -*- coding:utf-8 -*-


# 生成器
# https://wiki.python.org/moin/Generators
# 也是一种迭代器，但是你只能对其迭代一次。这是因为它们并没有把所有的值存在内存中，而是在运行时生成值。
# 大多数时候生成器是以函数中yield语句来实现的。调用该函数返回的是一个生成器。
# 它们并不返回一个值，而是yield(暂且译作“生出”)一个值。
# 许多Python 2里的标准库函数都会返回列表，而Python 3都修改成了返回生成器，因为生成器占用更少的资源。
def fib(n):
    a,b = 0, 1
    while b < n:
        yield b
        a, b = b, a+b

# 用for循环来迭代
fib100 = fib(100)
for item in fib100:
    print item

# 用next()来迭代
fib100 = fib(100)
print next(fib100)
print next(fib100)
print next(fib100)
print next(fib100)
# 每执行一次next就执行到一次yield所在的位置,返回yield的内容，并停在下一步之前
# 在yield掉所有的值后，next()触发了一个StopIteration的异常。
# 在使用for循环时没有这个异常是因为for循环会自动捕捉到这个异常并停止调用next()


# 生成器表达式
# 将列表生成式的[]改为()也就得到了一个生成器表达式
a = (x for x in range(10))
print a.next()
print a.next()
print a.next()


# 发送值到生成器函数
def mygen():
    """Yield 5 until something else is passed back via send()"""
    a = 5
    while True:
        f = (yield a)   # yield a and possibly get f in return
        if f is not None:
            a = f       # store the new value

g = mygen()
print g.next()
print g.next()
g.send(7)
print g.next()
