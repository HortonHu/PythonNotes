#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！
# Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。
# 把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。
def add(x, y, f):
    return f(x) + f(y)
print add(-5, 6, abs)

# 函数名其实就是指向函数的变量


# map(function, sequence)
# 将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回
print map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# More than one sequence may be passed;
# the function must then have as many arguments as there are sequences
# and is called with the corresponding item from each sequence (or None if some sequence is shorter than another).


def add(x, y):
    return x + y
print map(add, range(8), range(8))


# reduce(function, sequence)
# reduce把一个函数作用在一个序列[x1, x2, x3   ]上，
# 把结果继续和序列的下一个元素做累积计算  reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
def add(x, y):
    return x + y
print reduce(add, range(1, 11))
# A third argument can be passed to indicate the starting value.


def fn(x, y):
    return x * 10 + y


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

print reduce(fn, map(char2num, '13579'))


# str2int的map\reduce实现
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))


# 加入lambda函数进一步化简
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


def str2int(s):
    return reduce(lambda x, y: x*10+y, map(char2num, s))

#  练习 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']。
# title()是string中的内建方法，使字符串转为标题格式：首字母大写，其他小写。
# capitalize()也有类似功能
print map(lambda s: s.title(), ['adam', 'LISA', 'barT'])


# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积。
def prod(l):
    return reduce(lambda x, y: x*y, l)
print prod([1, 2, 3, 4])


# filter(function, sequence)
# 把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
# If sequence is a str, unicode or tuple, the result will be of the same type; otherwise, it is always a list.
def f(x):
    return x % 3 == 0 or x % 5 == 0
print filter(f, range(2, 25))
# 请尝试用filter()删除1~100的素数。
filter(lambda x: not any(map(lambda y: x % y == 0, range(2, x))), range(2, 100))


# sorted
# 通常规定，对于两个元素x和y，如果认为x < y，则返回-1，如果认为x == y，则返回0，如果认为x > y，则返回1
# 也可以接收一个比较函数来实现自定义的排序
print sorted([36, 5, 12, 9, 21])


def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0
print sorted([36, 5, 12, 9, 21], reversed_cmp)


def cmp_ignore_case(s1, s2):    # 忽略大小写进行字符串排序
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0
print sorted(['bob', 'Boa', 'Bob',  'about', 'Zoo', 'Credit'])                     # 'Z'排在'a'前面
print sorted(['bob', 'Boa', 'Bob',  'about', 'Zoo', 'Credit'], cmp_ignore_case)    # 'Z'排在'a'后面


# 返回函数
def lazy_sum(*args):
    def my_sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return my_sum
f = lazy_sum(1, 3, 5, 7, 9)
print f         # 返回函数
print f()       # 返回结果
# 调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print f1 == f2


# 闭包 相关参数和变量都保存在返回的函数中
# 返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1, f2, f3 = count()
print f1(), f2(), f3()
# 返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。


# 如果一定要引用循环变量方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，
# 无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def count():
        fs = []
        for i in range(1, 4):
            def f(j):
                def g():                # 绑定循环变量当前的值
                    return j*j
                return g
            fs.append(f(i))
        return fs
f1, f2, f3 = count()
print f1(), f2(), f3()

# 或者修改为以下形式
f1, f2, f3 = [(lambda i=j: i ** 2) for j in range(1, 4)]

# lambda 函数
# 关键字lambda表示匿名函数，冒号前面的x表示函数参数。
# 匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数
# 也可以把匿名函数作为返回值返回
print map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
f = lambda x: x * x
print f(5)


def build(x, y):
    return lambda: x * x + y * y

# lambda后面有无参数区别
a, b = 1, 2
aa = lambda: a ** 2 + b ** 2        # 无参数时使用外部变量
aa = lambda a, b: a ** 2 + b ** 2   # 有参数时使用传入变量
print aa()

