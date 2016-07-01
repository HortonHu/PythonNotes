判断：if
-----
elif是switch的代替

    age = 3
    if age >= 18:
        print 'adult'
    elif age >= 6:
        print 'teenager'
    else:
        print 'kid'

x是非零数值、非空字符串、非空list等，为True，否则为False

    x = raw_input('please input x to judge:')
    if x:
        print 'True'

循环: for x in y \ while 
----------------------
continue  进入下一次循环
break     跳出当前循环

for x in y
在循环内想要改变被循环的数据时，要创建一个拷贝

    words = ['cat', 'window', 'defenestrate']
    for w in words[:]:  # 创建拷贝
        if len(w) > 6:
            words.insert(0, w)
            pass
    print words

循环后可以跟一个else 当循环中没有break发生的时候执行
如果是else 同样是在没有break的情况下执行（即没有遇到false情况）
在for中：

    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print n, 'equals', x, '*', n / x        # 在后面加上逗号可以不换行打印
                break
        else:
            # 从for或while循环中break终止 ，任何对应的循环else块将不执行
            print n, 'is a prime number'
在while中：

    while
    temp = 0
    n = 99
    while n > 0:
        sum += n
        n -= 2
    print sum

不伦是if还是while，被判断的部分可以包含任何操作，不仅仅是比较
例如 in/not in/is/is not/
优先级：布尔操作or and not < 比较符号 < 运算符号
在布尔符号中 or < and < not 因此有`A and not B or C` 相当于 `(A and (not B)) or C`
and和or被称为短路操作，因为他们从左往右运算，在得出结果的时候就停止