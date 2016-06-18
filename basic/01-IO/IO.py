# -*- coding:utf-8 -*-

# IO
# raw_input()   返回 string
# input()       返回 value
name = raw_input('Please input your name：')
print 'Hi', name
age = input('Ple    ase input your age：')
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
# / 除法      // 整除 地板除
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


# % 格式化  %d 整数  %f 浮点数 %s 字符串   %x 十六进制整数 %r 变量 获取某些东西的 debug 信息
# %s永远起作用，它会把任何数据类型转换为字符串
# 格式化整数和浮点数还可以指定是否补0和整数与小数的位数
# 字符串里面的%是一个普通字符时候需要转义: %%
print 'My age is %d' % 22
print 'Price is %.4f' % 4.99
print 'Today is %s.' % 'Friday'
print "%s's score is %d" % ('Mike', 87)
print 'growth rate: %d %%' % 7

# 从2.6以后开始引入format()进行格式化 操作更方便
# 大括号和其中的字符会被替换成传入 str.format() 的参数。大括号中的数值指明使用传入 str.format() 方法的对象中的哪一个
print 'We are the {} who say "{}!"'.format('knights', 'Ni')
print '{0} and {1}'.format('spam', 'eggs')
print '{1} and {0}'.format('spam', 'eggs')
# 如果在 str.format() 调用时使用关键字参数，可以通过参数名来引用值:
print 'This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible')
# 定位和关键字参数可以组合使用
print 'The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg')
# '!s' (应用 str() )和 '!r' (应用 repr())可以在格式化之前转换值:
import math
print 'The value of PI is approximately {}.'.format(math.pi)
print 'The value of PI is approximately {!r}.'.format(math.pi)
# 字段名后允许可选的 ':' 和格式指令。这允许对值的格式化加以更深入的控制。
print('The value of PI is approximately {0:.3f}.'.format(math.pi))
# 在字段后的 ':' 后面加一个整数会限定该字段的最小宽度，这在美化表格时很有用:
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print '{0:10} ==> {1:10d}'.format(name, phone)
# 传入一个字典，用中括号( '[]' )访问它的键
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print 'Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table)
# 用 ‘**’ 标志将这个字典以关键字参数的方式传入
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print 'Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table)


