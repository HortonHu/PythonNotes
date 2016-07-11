# 偏函数 Partial function
functools.partial的作用是把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数
当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数
这个新函数可以固定住原函数的部分参数，从而在调用时更简单。

    import functools
    int2 = functools.partial(int, base=2)   # 将base进制数转化为10进制 base=2
    print int2('100')

也可以在函数调用时传入其他值： 要写明变量名`print int2('100', base=10)`
创建偏函数时，实际上可以接收函数对象、\*args和\**kw这3个参数
对于如下表示

    int2 = functools.partial(int, base=2)
    print int2('100')
实际上设定

    kw = { base: 2 }
    int('100', \**kw)

当如下设置的时候 实际上会把10作为*args的一部分自动加到左边`max2 = functools.partial(max, 10)`即`max2(5, 6, 7)`
相当于结果为10

    args = (10, 5, 6, 7)
    print max(\*args)
