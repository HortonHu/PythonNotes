# lambda函数
关键字lambda表示匿名函数，冒号前面的x表示函数参数。

    print map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    f = lambda x: x * x
    print f(5)


    def build(x, y):
        return lambda: x * x + y * y

lambda后面有无参数区别

    a, b = 1, 2
    aa = lambda: a ** 2 + b ** 2        # 无参数时使用外部变量
    aa = lambda a, b: a ** 2 + b ** 2   # 有参数时使用传入变量
    print aa()
