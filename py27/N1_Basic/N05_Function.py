#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 调用函数
# 可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
a = abs
print a(-1)


# 定义函数 def ...():
def my_abs(x):
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
def add_end(L = []):
    L.append('END')
    return L

# 默认参数是[]，但是函数似乎每次都“记住了”上次添加了'END'后的list
# 因为默认参数L也是一个变量，它指向对象[]
# 每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了
print add_end([1, 2, 3])
print add_end()
print add_end()
print add_end()


def add_end(L = None):
    if L is None:
        L = []
    L.append('END')
    return L

print add_end()
print add_end()


# 可变参数 可变参数在函数调用时自动组装为一个tuple
# *args是可变参数，args接收的是一个tuple
# 定义可变参数和定义list或tuple参数相比，仅仅在参数前面加了一个*号。
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print calc([1, 2, 3])


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print calc(1, 2, 3)
# 在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传入
nums = [1, 2, 3]
print calc(*nums)


# 关键字参数 扩展函数的功能
# **kw是关键字参数，kw接收的是一个dict。
# 关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw
    pass

person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')
kw = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=kw['city'], job=kw['job'])
person('Jack', 24, **kw)


# 参数组合
def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw
    pass

func(1, 2)
func(1, 2, c=3)
func(1, 2, 3, 'a', 'b')

# 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。
args = (1, 2, 3, 4)
kw = {'x': 99}
func(*args, **kw)


# 递归函数
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)











