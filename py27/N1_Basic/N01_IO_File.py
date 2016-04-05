#!/usr/bin/env python
# -*- coding:utf-8 -*-

# IO
# raw_input（） return string
# input() return value
# input equal to eval(raw_input(prompt))
name = raw_input('Please input your name：')
print 'Hi', name
age = input('Please input your age：')
print 'the type of age is ', type(age)

# without print, \n is included in the output
# with print, \n produces a new line
s = '1\n2'
s
print s

# import
from math import pi as math_pi

print math_pi

# operation
# / division	// floor division
print 5 / 4  # int / int -> int
print 5.0 / 4  # int / float -> float
print 5 // 4		 # explicit floor division discards the fractional part
print 5.1 // 4


# **power
print 2 ** 3

print '123', '456'
print '123' + '456'

"""This is comment too"""

# =
# The expressions on the right-hand side are all evaluated first before any of the assignments take place.
# The right-hand side expressions are evaluated from the left to the right.
a = 1
b = 2
a, b = b, a + b
print a, b

# In interactive mode, the last printed expression is assigned to the variable _.
tax = 12.5 / 100
price = 100.50
price * tax
price + _


# % 格式化  %d 整数  %f 浮点数 %s 字符串   %x	十六进制整数
# 格式化整数和浮点数还可以指定是否补0和整数与小数的位数
# %s永远起作用，它会把任何数据类型转换为字符串
# 字符串里面的%是一个普通字符时候需要转义: 	 %%
print 'My age is %d' % 1024
print 'Price is %.4f' % 4.99
print 'Today is %s.' % 'Friday'
print "%s's score is %d" % ('Mike', 87)
print 'growth rate: %d %%' % 7
# file
f = open('data.txt', 'r')  # r: 读 w: 写入 会覆盖     a: 添加
data = f.read()
l = f.readline()  # 读取一行内容
ll = f.readlines()  # 把内容按行读取至一个list中
print data
print l, type(l)
print ll, type(ll)
f.close()

f = open('data.txt', 'a')  # w: 写入 会覆盖     a: 添加
f.write('\n987654321\n')
f.close()

f = file(r'F:\Python\PythonStudy\py27\N1_Basic\scores.txt', 'r')
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
output = file(r'F:\Python\PythonStudy\py27\N1_Basic\result.txt', 'w')  # 注意r
output.writelines(results)
output.close()
