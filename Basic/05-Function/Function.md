函数定义
----

    def my_abs(x):
        # 参数检查
        if not isinstance(x, (int, float)):
            raise TypeError('bad operand type')
        if x >= 0:
            return x
        else:
            return -x


pass可以充当占位符

    def nop():
        pass


函数参数（必选、默认、可变 `*args`、关键字 `**kw`）
-----------------------------

通常将变化少的参数当做**默认参数**
函数内部的变量是局部变量 除非声明了 `global var`

    def power(x, n=2):              # n为默认参数 不修改默认为2
        s = 1
        while n > 0:
            n -= 1
            s = s * x
        return s
    
    print power(5)
    print power(5, 2)


默认参数必须指向不变对象！
默认参数为可变对象可能引入错误
下例默认参数是[]，但是函数似乎每次都“记住了”上次添加了'END'后的list
因为默认参数L也是一个变量，它指向对象[] Python函数在定义的时候，默认参数L的值就被计算出来了
即默认变量的值在函数定义的时候就已经计算出来而且仅计算这一次 L = [] 仅作用一次
每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了

    def add_end(L = []):
        L.append('END')
        return L
    
    print add_end([1, 2, 3])
    print add_end()
    print add_end()
    print add_end()


改进写法如下

    def add_end(L = None):
        if L is None:
            L = []
        L.append('END')
        return L

    print add_end()
    print add_end()
    
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
    print f(5)
因为默认变量的初始化只是被执行了一次(第一次使用默认值调用)
初始化执行开辟的内存区（我们可以称之为默认变量）没有被改变，所以最后的输出结果是“[1, 2, 3, 5]”


**可变参数**
*args是可变参数，args接收的是一个tuple 可变参数在函数调用时自动组装为一个tuple
定义可变参数和定义list或tuple参数相比，仅仅在参数前面加了一个*号。

    def calc2(*numbers):
        temp = 0
        for n in numbers:
            temp = temp + n * n
        return temp
    
    print calc2(1, 2, 3)    # 接收后转为tuple

对于已有的list或tuple 在前面加一个*号，把其中的元素变成可变参数传入

    nums = [1, 2, 3]
    print calc2(*nums)


**关键字参数**
扩展函数的参数 带有参数名字的和参数值的整体
**kw是关键字参数，kw接收的是一个dict。
关键字参数在函数内部自动组装为一个dict

    def person(name, age, **kw):
        print 'name:', name, 'age:', age, 'other:', kw
        pass
    
    person('Michael', 30)
    person('Bob', 35, city='Beijing')
    person('Adam', 45, gender='M', job='Engineer')
    
    d = {'city': 'Beijing', 'job': 'Engineer'}
    person('Jack', 24, city=d['city'], job=d['job'])
    person('Jack', 24, **d)                             # 简化写法 类似于可变参数用法


**参数组合**

    def func(a, b, c=0, *args, **kw):
        print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw
        pass
    
    func(1, 2)
    func(1, 2, c=3)
    func(1, 2, 3, 'a', 'b')             # 此时args接收('a', 'b') kw接收{}
    func(1, 2, 3, 'a', 'b', x=99)       # 此时args接收('a', 'b') kw接收{'x': 99}

对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。

    args = (1, 2, 3, 4)
    kw = {'x': 99}
    func(*args, **kw)       # 此时args接收(4, ) 取来区分（4）


递归函数
----
注意：次数太多会造成栈溢出 该次数可设置 最大1000

    def fact(n):
        if n == 1:
            return 1
        return n * fact(n - 1)
    print fact(5)


改用尾递归方式 
尾递归调用时，如果做了优化,只占用一个栈帧多少次调用也不会导致栈溢出。
但是Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。

    def fact(n):
        return fact_iter(n, 1)
    
    def fact_iter(num, product):
        if num == 1:
            return product
        return fact_iter(num - 1, num * product)        # num - 1和num * product在函数调用前就会被计算，不影响函数调用。
    print fact(5)

**any**   
any(iterable) -> bool
相当于与 传入可迭代对象 全bool()返回False则False 否则True

    print any('123')    # True
    print any([0, 1])   # True
    print any([0, ''])  # False


**all**   
all(iterable) -> bool
相当于和 传入可迭代对象 全bool()返回True则True 否则False

    print all('123')    # True
    print all([0, 1])   # False
    print all([1, 2])   # True

可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：

    a = abs
    print a(-1)
    
