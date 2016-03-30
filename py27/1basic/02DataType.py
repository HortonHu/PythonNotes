#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Data type: integer\ float\ string\ boolean\ None
print 'integer:', 1
print 'float  :', 3.14, 1e-5
print 'string :', 'python'
print 'string :', 'I\'m OK'
print 'string :', '\\\n\\'
print 'string :', '\\\t\\'
print 'string :', r'\\\t\\'      # 此时\没有转义效果
print 'string :', '''line1
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
## set和dict类似，也是一组key的集合，但不存储value
## key不能重复
s = set([1, 2, 3])
print 'set:', s
s = set([1, 1, 2, 2, 3, 3])
print 'set:', s
s.add(4)            # 添加key
print 'set:', s
s.add(4)            # 重复添加无效
print 'set:', s
s.remove(4)         # 删除key
print 'set:', s
## set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print 'set:', s1 & s2
print 'set:', s1 | s2

## 可变对象：list\
## 不变对象：string\
## 对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容
a = ['c', 'b', 'a']
a.sort()
print 'a =', a
a = 'abc'
b = a.replace('a', 'A')
print b
print a