# -*- coding:utf-8 -*-

# 迭代器
# 迭代器有两个基本的方法
# next方法：返回迭代器的下一个元素
# __iter__方法：返回迭代器对象本身

# Python中一些内置数据类型也支持迭代 对象可迭代意味着它支持迭代，但不能直接对其进行迭代操作
# 通过内置函数iter来完成生成一个迭代器
my_string = "Yasoob"
my_iter = iter(my_string)
next(my_iter)

# python专门为for关键字做了迭代器的语法糖。
# 在for循环中，Python将自动调用工厂函数iter()获得迭代器，自动调用next()获取元素，还完成了检查StopIteration异常的工作。
for c in iter('abc'):
    print c
