#!/usr/bin/env python
# -*- coding:utf-8 -*-

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
## continue 跳出当前循环
## break 跳出整个循环

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

## try ... except
try:
    f = file('non-exist.txt')
    print 'File opened!'
    f.close()
except:
    print 'File not exists.'
print 'Done'