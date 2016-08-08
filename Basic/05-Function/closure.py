# -*- coding:utf-8 -*-


# 闭包 closure
# 闭包(closure)是函数式编程的重要的语法结构。闭包也是一种组织代码的结构，它同样提高了代码的可重复使用性。
# 当一个内嵌函数引用其外部作作用域的变量,我们就会得到一个闭包. 总结一下,创建一个闭包必须满足以下几点:
# 必须有一个内嵌函数
# 内嵌函数必须引用外部函数中的变量
# 外部函数的返回值必须是内嵌函数
# 感觉闭包还是有难度的,几句话是说不明白的,还是查查相关资料.
# 重点是函数运行后并不会被撤销,就像16题的instance字典一样,当函数运行完后,instance并不被销毁,而是继续留在内存空间里.
# 这个功能类似类里的类变量,只不过迁移到了函数上.
# 闭包就像个空心球一样,你知道外面和里面,但你不知道中间是什么样.
# 相关参数和变量都保存在返回的函数中
# 返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
# 返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1, f2, f3 = count()
print f1(), f2(), f3()


# 如果一定要引用循环变量 可以再创建一个函数，用该函数的参数绑定循环变量当前的值，
# 无论该循环变量后续如何更改，已绑定到函数参数的值不变：
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

# 或者修改为以下形式
# 生成一个list 每个元素都是一个待执行的函数
f1, f2, f3 = [(lambda i=j: i ** 2) for j in range(1, 4)]


# 练习：
# 请实现函数 new_counter ，使得调用结果如下：
# c1 = new_counter(10)
# c2 = new_counter(20)
# print c1(), c2(), c1(), c2()
# outputs ：
# 11 21 12 22
