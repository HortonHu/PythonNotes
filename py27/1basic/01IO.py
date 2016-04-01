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



# operation
##  //get a integer  /divide
print 5 // 4
print 5.1 // 4
print 5 / 4
print 5.0 / 4

## **power
print 2 ** 3

print '123', '456'
print '123'+'456'

"""This is comment too"""

## =
## python中运算的顺序是，先把“=”右边的结果算出了，再赋值给左边的变量
a = 1
b = 2
a, b = b, a+b
print a, b

## % 格式化  %d 整数  %f 浮点数 %s 字符串
print 'My age is %d' % 1024
print 'Price is %.4f' % 4.99
print 'Today is %s.' % 'Friday'
print "%s's score is %d" % ('Mike', 87)

## file
f = open('data.txt','r')    # r: 读 w: 写入 会覆盖     a: 添加
data = f.read()
l = f.readline()    # 读取一行内容
ll = f.readlines()  # 把内容按行读取至一个list中
print data
print l, type(l)
print ll, type(ll)
f.close()

f = open('data.txt','a')    # w: 写入 会覆盖     a: 添加
f.write('\n987654321\n')
f.close()