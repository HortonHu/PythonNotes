# map/reduce/filter/sorted
1.map(function, sequence)
将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回
当传入多个list时候 传入函数的变量数必须和list数字相同 如果list长度不等则会补上None

    print map(str, [1, 2, 3])    
    print map(lambda x, y: x==y, range(8), range(6))


2.reduce(function, sequence, initial=None)
第三个参数被当做初始值 默认不存在
reduce把一个函数作用在一个序列[x1, x2, x3]上，
把结果继续和序列的下一个元素做累积计算`reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)`

例如：str2int的map reduce实现

    def str2int(s):
        return reduce(lambda x, y: 10*x+y, map(int, list(s)))

练习
利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']。
title()是string中的内建方法，使字符串转为标题格式：首字母大写，其他小写。
capitalize()也有类似功能

    print map(lambda s: s.title(), ['adam', 'LISA', 'barT'])


练习
Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积。

    def prod(l):
        return reduce(lambda x, y: x*y, l)
    print prod([1, 2, 3, 4])


3.filter(function, sequence)
把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
如果序列是str、unicode或者tuple，返回类型将与输入相同，否则均返回list

    def f(x):
        return x % 3 == 0 or x % 5 == 0
    print filter(f, range(2, 25))

练习
请尝试用filter()删除1~100的素数。

    filter(lambda x: not any(map(lambda y: x % y == 0, range(2, x))), range(2, 100))


4.sorted(iterable, cmp=None, key=None, reverse=False)
通常规定，对于两个元素x和y，如果认为x < y，则返回-1，如果认为x == y，则返回0，如果认为x > y，则返回1
也可以接收一个比较函数来实现自定义的排序

    def reversed_cmp(x, y):
        if x > y:
            return -1
        if x < y:
            return 1
        return 0
    print sorted([36, 5, 12, 9, 21], reversed_cmp)


    def cmp_ignore_case(s1, s2):    # 忽略大小写进行字符串排序
        u1 = s1.upper()
        u2 = s2.upper()
        if u1 < u2:
            return -1
        if u1 > u2:
            return 1
        return 0
    print sorted(['bob', 'Boa', 'Bob',  'about', 'Zoo', 'Credit'])                     # 'Z'排在'a'前面
    print sorted(['bob', 'Boa', 'Bob',  'about', 'Zoo', 'Credit'], cmp_ignore_case)    # 'Z'排在'a'后面
