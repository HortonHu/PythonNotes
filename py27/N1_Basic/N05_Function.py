#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 调用函数
# 可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
a = abs
print a(-1)


# 定义函数 def ...():
def my_abs(x):
    # 参数检查
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# pass可以充当占位符
def nop():
    pass


# 函数的参数 必选参数、默认参数、可变参数 *args、关键字参数 **kw
# 通常将变化少的参数当做默认参数
def power(x, n=2):              # n为默认参数 不修改默认为2
    s = 1
    while n > 0:
        n -= 1
        s = s * x
    return s

print power(5)
print power(5, 2)


# 默认参数必须指向不变对象！
# 默认参数是[]，但是函数似乎每次都“记住了”上次添加了'END'后的list
# 因为默认参数L也是一个变量，它指向对象[] Python函数在定义的时候，默认参数L的值就被计算出来了
# 每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了
def add_end(L = []):
    L.append('END')
    return L

print add_end([1, 2, 3])
print add_end()
print add_end()
print add_end()


# 改进写法如下
def add_end(L = None):
    if L is None:
        L = []
    L.append('END')
    return L

print add_end()
print add_end()


# 可变参数
# *args是可变参数，args接收的是一个tuple 可变参数在函数调用时自动组装为一个tuple
# 定义可变参数和定义list或tuple参数相比，仅仅在参数前面加了一个*号。
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print calc([1, 2, 3])


def calc2(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print calc2(1, 2, 3)    # 接收后转为tuple
# 对于已有的list或tuple 在前面加一个*号，把其中的元素变成可变参数传入
nums = [1, 2, 3]
print calc2(*nums)


# 关键字参数 扩展函数的参数 带有参数名字的和参数值的整体
# **kw是关键字参数，kw接收的是一个dict。
# 关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw
    pass

person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')
d = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=d['city'], job=d['job'])
person('Jack', 24, **d)                             # 简化写法


# 参数组合
def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw
    pass

func(1, 2)
func(1, 2, c=3)
func(1, 2, 3, 'a', 'b')             # 此时args接收('a', 'b')
func(1, 2, 3, 'a', 'b', x=99)       # 此时kw接收{'x': 99}

# 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。
args = (1, 2, 3, 4)
kw = {'x': 99}
func(*args, **kw)       # 此时args接收(4, )


# 递归函数 次数太多会造成栈溢出
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)
print fact(5)
# 改用尾递归方式
# 尾递归调用时，如果做了优化,只占用一个栈帧多少次调用也不会导致栈溢出。
# 但是Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。


def fact(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
print fact(5)

# Lambda Expressions: Small anonymous functions
