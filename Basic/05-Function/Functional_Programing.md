把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。
函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数
Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。
函数名其实就是指向函数的变量

    def my_add(x, y, f):
        return f(x) + f(y)
    print my_add(-5, 6, abs)


# 返回函数

    def lazy_sum(\*args):
        def my_sum():
            temp = 0
            for n in args:
                temp = temp + n
            return temp
        return my_sum
    f = lazy_sum(1, 3, 5, 7, 9)
    print f         # 返回函数
    print f()       # 此时才运行 返回结果
调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：

    f1 = lazy_sum(1, 3, 5, 7, 9)
    f2 = lazy_sum(1, 3, 5, 7, 9)
    print f1 == f2


**闭包**
closure
相关参数和变量都保存在返回的函数中
返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。

    def count():
        fs = []
        for i in range(1, 4):
            def f():
                return i*i
            fs.append(f)
        return fs
    f1, f2, f3 = count()
    print f1(), f2(), f3()


如果一定要引用循环变量 可以再创建一个函数，用该函数的参数绑定循环变量当前的值，
无论该循环变量后续如何更改，已绑定到函数参数的值不变：

    def count():
            fs = []
            for i in range(1, 4):
                def f(j):
                    def g():                # 绑定循环变量当前的值
                        return j*j
                    return g
                fs.append(f(i))
            return fs
    f1, f2, f3 = count()
    print f1(), f2(), f3()

或者修改为以下形式
生成一个list 每个元素都是一个待执行的函数

    f1, f2, f3 = [(lambda i=j: i ** 2) for j in range(1, 4)]

