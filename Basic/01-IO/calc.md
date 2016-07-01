操作符
---
/  除法
// 整除(地板除)

    print 5 / 4         # int / int     -> int   和//效果相同
    print 5.0 / 4       # int / float   -> float 精确除法
    print 5 // 4        # int / int     -> int
    print 5.1 // 4      # int / float   -> float 浮点数的整除

= 先算出右侧值 再赋给左边 并且右侧部分计算过程从左往右

    a = 1
    b = 2
    a, b = b, a + b
    print a, b

a = b = c被处理为a = (b = c)。

    c = 3
    a = b = c
    print a, b, c


交互模式下，最近的没有被赋值的计算结果被赋给_

    tax = 12.5 / 100
    price = 100.50
    price * tax
    price + _
