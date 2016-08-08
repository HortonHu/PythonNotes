# -*- coding:utf-8 -*-

# /  除法
# // 整除(地板除)
print 5 / 4         # int / int     -> int   和//效果相同
print 5.0 / 4       # int / float   -> float 精确除法
print 5 // 4        # int / int     -> int
print 5.1 // 4      # int / float   -> float 浮点数的整除

# << 左移     >> 右移
print 2 << 2, 11 >> 1

# 按位与   &
# 按位或   |
# 按位异或  ^
# 按位翻转  ~   x的按位翻转是-(x+1)
print 5 & 3
print 5 | 3
print 5 ^ 3
print ~5


# = 先算出右侧值 再赋给左边 并且右侧部分计算过程从左往右
a = 1
b = 2
a, b = b, a + b
print a, b
# 因此a = b = c被处理为a = (b = c)。
c = 3
a = b = c
print a, b, c

# == 对比的是值
# is 对比的是id()
# Python解释器对于小整数和短字符串分配了同样的id 因此出现了 is和==效果相同

# 交互模式下，最近的没有被赋值的计算结果被赋给_
# 如果输入 10*10 则100被赋给_
