# -*- coding:utf-8 -*-


# 生成器也是一种迭代器，但是你只能对其迭代一次。这是因为它们并没有把所有的值存在内存中，而是在运行时生成值。
# 大多数时候生成器是以函数来实现的。然而，它们并不返回一个值，而是yield(暂且译作“生出”)一个值。
# 许多Python 2里的标准库函数都会返回列表，而Python 3都修改成了返回生成器，因为生成器占用更少的资源。
def generator_function():
    for i in range(3):
        yield i

# 用for循环来迭代
gen = generator_function()
for item in generator_function():
    print(item)

# 用next()来迭代
gen = generator_function()
print next(gen)
print next(gen)
print next(gen)
print next(gen)
# 在yield掉所有的值后，next()触发了一个StopIteration的异常。
# 在使用for循环时没有这个异常是因为for循环会自动捕捉到这个异常并停止调用next()


# Python中一些内置数据类型也支持迭代
# 可迭代对象意味着它支持迭代，但不能直接对其进行迭代操作，通过内置函数iter来完成生成一个迭代器
my_string = "Yasoob"
my_iter = iter(my_string)
next(my_iter)
