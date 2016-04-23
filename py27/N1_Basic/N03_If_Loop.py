#!/usr/bin/env python
# -*- coding:utf-8 -*-

# if
# elif是switch的代替
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

# x是非零数值、非空字符串、非空list等，为True，否则为False
x = raw_input('please input x to judge:')
if x:
    print 'True'

# 循环: for x in y \ while
# continue  跳出当前循环
# break     跳出整个循环

# for x in y
# 在循环内想要改变被循环的数据时，要创建一个拷贝
words = ['cat', 'window', 'defenestrate']
for w in words[:]:  # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0, w)
        pass

print words

# Loop statements may have an else clause, a loop’s else clause runs when no break occurs.
# it is executed when the loop terminates through exhaustion of the list (with for)
# or when the condition becomes false (with while), but not when the loop is terminated by a break statement.
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print n, 'equals', x, '*', n / x        # 在后面加上逗号可以不换行打印
            break
    else:
        # loop fell through without finding a factor
        # 从for或while循环中break终止 ，任何对应的循环else块将不执行
        print n, 'is a prime number'


temp = 0
for x in range(101):
    temp += x
print temp

# while
temp = 0
n = 99
while n > 0:
    sum += n
    n -= 2
print sum

