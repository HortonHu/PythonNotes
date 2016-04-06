#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。
def add(x, y, f):
    return f(x) + f(y)

print add(-5, 6, abs)


# filter(function, sequence)
# returns a sequence consisting of those items from the sequence for which function(item) is true.
# If sequence is a str, unicode or tuple, the result will be of the same type; otherwise, it is always a list.
def f(x):
    return x % 3 == 0 or x % 5 == 0
print filter(f, range(2, 25))

# map(function, sequence)
# calls function(item) for each of the sequence’s items and returns a list of the return values.
print map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# More than one sequence may be passed;
# the function must then have as many arguments as there are sequences
# and is called with the corresponding item from each sequence (or None if some sequence is shorter than another).
seq = range(8)


def add(x, y):
    return x + y
print map(add, seq, seq)


# reduce(function, sequence)
# reduce把一个函数作用在一个序列[x1, x2, x3...]上，
# returns a single value constructed by calling the binary function function on the first two items of the sequence,
# then on the result and the next item, and so on. like: reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
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
    return reduce(lambda x,y: x*10+y, map(char2num, s))

#  练习 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']。

# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积。


# sorted
# 也可以接收一个比较函数来实现自定义的排序
print sorted([36, 5, 12, 9, 21])


def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0
print sorted([36, 5, 12, 9, 21], reversed_cmp)

print sorted(['bob', 'about', 'Zoo', 'Credit'])


def cmp_ignore_case(s1, s2):    # 忽略大小写进行字符串排序
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0
print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)

