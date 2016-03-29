#!/usr/bin/env python
# -*- coding:utf-8 -*-

# IO
name = raw_input('Please input your name：')  # raw_input 返回的是string
print 'Hi', name

# Data type: Integer\ Float\ String\ Boolean\ None
print 'Integer:', 1
print 'Float  :', 3.14, 1e-5
print 'String :', 'python'
print 'String :', 'I\'m OK'
print 'String :', '\\\n\\'
print 'String :', '\\\t\\'
print 'String :', r'\\\t\\'      # 此时\没有转义效果
print 'String :', '''line1
... line2'''
print 'Boolean:', True, not True, True and False, True or False
print None

# Data type: List
classmates = ['Michael', 'Bob', 'Tracy']
print 'List:', classmates
print 'length of List:', len(classmates)
print u'List序号从0开始，最后一个为n-1或者-1，可类推-2'
print classmates[2], classmates[-1]
classmates.append('Adam')   # 末尾插入
print 'List:', classmates
classmates.insert(1, 'Jack')    # 指定位置插入
print 'List:', classmates
classmates.pop()    # 删除末尾元素
print 'List:', classmates
classmates.pop(1)   # 删除指定元素
print 'List:', classmates
classmates[1] = 'Sarah'     # 直接替换指定位置元素
print 'List:', classmates
s = ['python', 'java', ['asp', 'php'], 'scheme']    # list可嵌套

# Data type: Tuple
##  Tuple和list非常类似，但是tuple一旦初始化就不能修改，更安全
classmates = ('Michael', 'Bob', 'Tracy')
print 'Tuple:', classmates
print classmates[0], classmates[1]
t = (1)                 # 特例，按照数学运算定义
tt = (1,)               # 消除歧义
print type(t), type(tt)

# Data type: dict
## dict全称dictionary，在其他语言中也称为map，使用键-值（key:value）存储，具有极快的查找速度
## list比较，dict有以下几个特点：
## 1.查找和插入的速度极快，不会随着key的增加而增加
## 2.需要占用大量的内存，内存浪费多
## dict是用空间来换取时间的一种方法。
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print 'dict:', d
print d['Bob']
d['Adam'] = 67   # 通过key放入value值进入dict，同一个key放入多个value后面的会抵消前面的
print 'dict:', d
## 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
print 'Thomas' in d
## 二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value：
print d.get('Thomas')
print d.get('Thomas', -1)
d.pop('Bob')    # 删除key 对应的value也会删除

# Data type: set


# String and Coding

# if
age = 3
if age >= 18:
    print 'adult'
elif age >= 6:
    print 'teenager'
else:
    print 'kid'

age = 20
if age >= 6:
    print 'teenager'
elif age >= 18:
    print 'adult'
else:
    print 'kid'
## 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False
x = raw_input('please input x to judge:')
if x:
    print 'True'

# loop: for x in y \ while
## for x in y
names = ['Michael', 'Bob', 'Tracy']
for student in names:
    print student

sum = 0
for x in range(101):
    sum = sum + x
print sum

## while
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print sum

