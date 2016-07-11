装饰器 Decorator: 在代码运行期间动态增加功能但又不会修改原定义
本质上，decorator就是一个返回函数的高阶函数。
Python的decorator可以用函数实现，也可以用类实现。

    def log(func):
        def wrapper(*args, **kw):                   # 在wrapper()函数内，首先打印日志，再紧接着调用原始函数。
            print 'call %s():' % func.__name__      # 通过__name__属性，可以拿到函数的名字
            return func(*args, **kw)
        return wrapper
wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。


把decorator置于函数的定义处 相当于执行了语句：now = log(now)    @要放在 def 前

    @log
    def now():
        print '2016-04-11'
        print 'After decorator now.__name__ =:', now.__name__   # 经过装饰后，now()的name变成wrapper
    now()


decorator需要参数时：

    def log(text):
        def decorator(func):
            def wrapper(*args, **kw):
                print '%s %s():' % (text, func.__name__)
                return func(*args, **kw)
            return wrapper
        return decorator

    @log('Executing')     # 相当于 now = log('execute')(now)
    def now():
        print '2016-04-11'
    now()

需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
Python内置的functools.wraps可以完成这个工作
一个完整的decorator的写法如下

    import functools

    def log(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print 'call %s():' % func.__name__
            return func(*args, **kw)
        return wrapper


对于带参数的装饰器

    def log(text):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print '%s %s():' % (text, func.__name__)
                return func(*args, **kw)
            return wrapper
        return decorator

练习：
请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
能否写出一个@log的decorator，使它既支持：@log和@log('execute')

    import functools


    def log(text):
        if callable(text):
            @functools.wraps(text)      # text 作为函数名
            def wrapper(*args, **kw):
                print 'Begin call:' + text.__name__
                text(*args, **kw)
                print 'End call:' + text.__name__
            return wrapper
        else:
            def decorator(func):        # text作为字符
                @functools.wraps(func)
                def wrapper(*args, **kw):
                    print 'Begin call:' + text + func.__name__
                    func(*args, **kw)
                    print 'End call:' + text + func.__name__
                return wrapper
            return decorator


    @log
    def f1():
        print 'f1 is running.'


    @log('horton\'s ')
    def f2():
        print 'f2 is running.'

    f1()
    f2()
