#!/usr/bin/env python
# -*- coding:utf-8 -*-

# IO
# raw_input()   返回 string
# input()       返回 value
name = raw_input('Please input your name：')
print 'Hi', name
age = input('Please input your age：')
print 'the type of age is ', type(age)

# 在交互模式下不用print, \n 等表示为原型
# 用了print则发挥特定的作用
s = '1\n2'
s
print s

# import
from math import pi as math_pi
print math_pi

# 操作符
# / 除法      // 地板除 整除
print 5 / 4         # int / int     -> int   和//效果相同
print 5.0 / 4       # int / float   -> float 精确除法
print 5 // 4        # int / int     -> int
print 5.1 // 4      # int / float   -> float 浮点数的整除


# ** power
print 2 ** 3

print '123', '456'
print '123' + '456'     # 和'123''456' 效果相同

# 三引号注释 内部均不转义
"""This is comment too"""

# = 先算出右侧值 再赋给左边 计算过程从左往右
a = 1
b = 2
a, b = b, a + b
print a, b

# a = b = c被处理为a = (b = c)。
c = 3
a = b = c
print a, b, c

# 交互模式下，最近的没有被赋值的计算结果被赋给_.
tax = 12.5 / 100
price = 100.50
price * tax
price + _


# % 格式化  %d 整数  %f 浮点数 %s 字符串   %x 十六进制整数
# %s永远起作用，它会把任何数据类型转换为字符串
# 格式化整数和浮点数还可以指定是否补0和整数与小数的位数
# 字符串里面的%是一个普通字符时候需要转义: %%
print 'My age is %d' % 22
print 'Price is %.4f' % 4.99
print 'Today is %s.' % 'Friday'
print "%s's score is %d" % ('Mike', 87)
print 'growth rate: %d %%' % 7


# file
f = open('Data_scores.txt', 'r')  # r:读 w:写(覆盖) a:添加
data = f.read()
l = f.readline()  # 读取一行内容
ll = f.readlines()  # 把内容按行读取至一个list中
print data
print l, type(l)
print ll, type(ll)
f.close()

f = open('Data_scores.txt', 'a')  # w: 写入 会覆盖     a: 添加
f.write('\n987654321\n')
f.close()

f = file(r'C:\Users\dell\Documents\GitHub\PythonStudy\py27\N1_Basic\Data_scores.txt', 'r')
lines = f.readlines()
# print lines
f.close()

results = []

for line in lines:
    print line
    data = line.split()
    # print data

    sum = 0
    for score in data[1:]:
        sum += int(score)
    result = '%s \t: %d\n' % (data[0], sum)
    # print result

    results.append(result)

print results
output = file(r'C:\Users\dell\Documents\GitHub\PythonStudy\py27\N1_Basic\Data_result.txt', 'w')  # 注意r
output.writelines(results)
output.close()
