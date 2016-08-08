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
