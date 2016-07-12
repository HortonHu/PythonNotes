# -*- coding:utf-8 -*-

# itertools
# Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数

# itertools提供的几个“无限”迭代器：
# count()
# 创建一个无限的迭代器，代码会一直打印出自然数序列
import itertools
natuals = itertools.count(1)
for n in natuals:
    print n

# cycle()
# 把传入的一个序列无限重复下去：
import itertools
cs = itertools.cycle('ABC')
for c in cs:
    print c

# repeat()
# 把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
ns = itertools.repeat('A', 10)      # 打印10次'A'
for n in ns:
    print n
# 无限序列只有在for迭代时才会无限地迭代下去，
# 如果只是创建了一个迭代对象，它不会事先把无限个元素生成出来，事实上也不可能在内存中创建无限多个元素。


# 无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
for n in ns:        # 打印出1到10
    print n


# itertools提供的几个迭代器操作函数更加有用：
# chain()
# 把一组迭代对象串联起来，形成一个更大的迭代器：
# 迭代效果：'A' 'B' 'C' 'X' 'Y' 'Z'
for c in itertools.chain('ABC', 'XYZ'):
    print c
# itertools包中的itertools.chain.from_iterable轻松快速的辗平一个列表
a_list = [[1, 2], [3, 4], [5, 6]]
print list(itertools.chain.from_iterable(a_list))
print list(itertools.chain(*a_list))   # 另一种写法

# groupby()
# 把迭代器中相邻的重复元素挑出来放在一起：
for key, group in itertools.groupby('AAABBBCCAAA'):
    print key, list(group)      # 用list()函数是为了显示出group内容 因为group是一个object
# 实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，这两个元素就被认为是在一组的
# 而函数返回值作为组的key。
# 如果我们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的key：
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print key, list(group)

# imap()
# imap()和map()的区别在于，imap()可以作用于无穷序列
# 并且，如果两个序列的长度不一致，以短的那个为准。
for x in itertools.imap(lambda x, y: x * y, [10, 20, 30], itertools.count(1)):
    print x
# 注意imap()返回一个迭代对象，而map()返回list。当你调用map()时，已经计算完毕：
r = map(lambda x: x*x, [1, 2, 3])
print r             # r已经计算出来了
# 调用imap()时，并没有进行任何计算：
r = itertools.imap(lambda x: x*x, [1, 2, 3])
print r             # r只是一个迭代对象
# 必须用for循环对r进行迭代，才会在每次循环过程中计算出下一个元素
for x in r:
    print x
# 说明imap()实现了“惰性计算”，也就是在需要获得结果的时候才计算。
# 类似imap()这样能够实现惰性计算的函数就可以处理无限序列
r = itertools.imap(lambda x: x*x, itertools.count(1))
for n in itertools.takewhile(lambda x: x<100, r):
    print n
# 如果把imap()换成map()去处理无限序列会一直计算下去

# ifilter()
# ifilter()就是filter()的惰性实现。
