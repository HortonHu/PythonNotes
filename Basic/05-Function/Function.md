# 函数定义
可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：

    a = abs
    print a(-1)

参数检查功能

    def my_abs(x):
        if not isinstance(x, (int, float)):     # 参数检查
            raise TypeError('bad operand type')
        return x if x >= 0 else -x

pass充当占位符

    def nop():
        pass

# 函数参数（必选、默认、可变 `*args`、关键字 `**kw`）
1.必选参数必选在最前面，依次是默认、可变、关键字
2.通常将变化少的参数当做默认参数

    def power(x, n=2):              # n为默认参数 不修改默认为2
        s = 1
        while n > 0:
            n -= 1
            s = s * x
        return s

    print power(5)
    print power(5, 2)
默认参数必须指向不变对象，默认参数如果指向可变对象可能引入错误

    def add_end(L = []):
        L.append('END')
        return L

    print add_end([1, 2, 3])    # 传入[1,2,3]的时候L指向了它
    print add_end()             # 没有传入值的时候L的指向一直是[]所在的位置
    print add_end()             # L仍然指向那个位置，只是那个位置存储的值已经变成了['END']
    print add_end()             # L仍然指向那个位置，只是那个位置存储的值已经变成了['END', 'END']

因为默认参数L也是一个变量，它指向对象[] Python函数在定义的时候，默认参数L的值就被计算出来了
即默认变量的值在函数定义的时候就已经计算出来而且仅计算这一次 L = [] 仅作用一次
每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了
改进写法如下

    def add_end(L = None):
        if L is None:
            L = []
        L.append('END')
        return L

    print add_end()
    print add_end()

在函数定义的时候，函数内部定义的变量L就已经指向了None这个不可变对象
在每次调用f()的时候，L都是None，到判断这一步的时候就会创建一个新的内部的变量L来指向[]，函数作用完成后这个L就被销毁
因此在下次调用的时候，L的指向还是None

使用函数默认值来实现函数静态变量的功能
Python中是不支持静态变量的，但是我们可以通过函数的默认值来实现静态变量的功能。
当函数的默认值是内容是可变的类时，类的内容可变，而类的名字没变。（相当于开辟的内存区域没有变，而其中内容可以变化）。
这是因为python中函数的默认值只会被执行一次，(和静态变量一样，静态变量初始化也是被执行一次。）这就是她们的共同点。

    def f(a, L=[]):
        L.append(a)
        return L

    print f(1)
    print f(2)
    print f(3)
    print f(4, ['x'])
    print f(5)      # L重新指向一开始开辟内存空间就确定的位置
因为默认变量的初始化只是被执行了一次(第一次使用默认值调用)
初始化执行开辟的内存区（我们可以称之为默认变量）没有被改变，所以最后的输出结果是“[1, 2, 3, 5]”


3.可变参数
`*args`是可变参数，args接收的是一个tuple 可变参数在函数调用时自动组装为一个tuple
定义可变参数和定义list或tuple参数相比，仅仅在参数前面加了一个*号。

    def calc2(\*numbers):
        temp = 0
        for n in numbers:
            temp = temp + n * n
        return temp

    print calc2(1, 2, 3)    # 接收后转为tuple

对于已有的list或tuple 在前面加一个*号，把其中的元素变成可变参数传入

    nums = [1, 2, 3]
    print calc2(\*nums)


4.关键字参数
扩展函数的参数 带有参数名字的和参数值的整体
\**kw是关键字参数，kw接收的是一个dict。
关键字参数在函数内部自动组装为一个dict
一个变量只能接受一次赋值

    def person(name, age, \**kw):
        print 'name:', name, 'age:', age, 'other:', kw
        pass

    person('Michael', 30)
    person('Bob', 35, city='Beijing')
    person('Adam', 45, gender='M', job='Engineer')

    d = {'city': 'Beijing', 'job': 'Engineer'}
    person('Jack', 24, city=d['city'], job=d['job'])
    person('Jack', 24, \**d)                             # 简化写法 类似于可变参数用法


5.参数组合

    def func(a, b, c=0, \*args, \**kw):
        print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw
        pass

    func(1, 2)
    func(1, 2, c=3)
    func(1, 2, 3, 'a', 'b')             # 此时args接收('a', 'b') kw接收{}
    func(1, 2, 3, 'a', 'b', x=99)       # 此时args接收('a', 'b') kw接收{'x': 99}

对于任意函数，都可以通过类似func(\*args, \**kw)的形式调用它，无论它的参数是如何定义的。

    args = (1, 2, 3, 4)
    kw = {'x': 99}
    func(\*args, \**kw)       # 此时args接收(4, ) 取来区分（4）

# 函数返回
函数没有返回值的时候会返回None
可以返回多个值`return a,b,c`实际上是返回了一个tuple
