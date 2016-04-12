#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 错误处理
# 高级语言通常都内置了一套try...except...finally...的错误处理机制，Python也不例外。
# 当我们认为某些代码可能会出错时，就可以用try来运行这段代码，
# 如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，
# 执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕。
try:
    print 'try...'
    r = 10 / 0
    print 'result:', r
except ZeroDivisionError, e:    # except捕获到ZeroDivisionError
    print 'except:', e
finally:                        # 不伦如何都会执行 可以没有finally
    print 'finally...'
print 'END'
# 可以有多个except来捕获不同类型的错误：
try:
    print 'try...'
    r = 10 / int('a')
    print 'result:', r
except ValueError, e:
    print 'ValueError:', e
except ZeroDivisionError, e:
    print 'ZeroDivisionError:', e
else:                   # 可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句
    print 'No Error!'
finally:
    print 'finally...'
print 'END'


# Python的错误其实也是class，所有的错误类型都继承自BaseException，
# 所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”。比如：
try:
    foo()
except StandardError, e:
    print 'StandardError'
except ValueError, e:
    print 'ValueError'
# 第二个except永远也捕获不到ValueError，因为ValueError是StandardError的子类，如果有，也被第一个except给捕获了。


# 使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，
# 比如函数main()调用foo()，foo()调用bar()，结果bar()出错了，这时，只要main()捕获到了，就可以处理
# 不需要在每个可能出错的地方去捕获错误，只要在合适的层次去捕获错误就可以了
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except StandardError, e:
        print 'Error!'
    finally:
        print 'finally...'

# 调用堆栈
# 如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    bar('0')

main()
# 错误信息
# 第1行：  Traceback (most recent call last):      告诉我们这是错误的跟踪信息。
# 第2行：  File "err.py", line 10, in <module>
# 第3行：  File "<input>", line 8, in main         调用main出错了
# 第4行：  File "<input>", line 5, in bar          调用bar出错了
# 第5行：  File "<input>", line 2, in foo          调用foo出错了
# 第6行：  ZeroDivisionError: integer division or modulo by zero   错误类型ZeroDivisionError


# 记录错误
# Python内置的logging模块可以非常容易地记录错误信息：
import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except StandardError, e:
        logging.exception(e)        # 记录错误原因，logging还可以把错误记录到日志文件里，方便事后排查

main()
print 'END'


# 抛出错误
# 错误是class，捕获一个错误就是捕获到该class的一个实例。因此，错误并不是凭空产生的，而是有意创建并抛出的。
# Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。
# 如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例：
class FooError(StandardError):
    pass

def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n
# 只有在必要的时候才定义我们自己的错误类型。
# 如果可以选择Python已有的内置的错误类型（比如ValueError，TypeError），尽量使用Python内置的错误类型。

# 另一种错误处理的方式：
def foo(s):
    n = int(s)
    return 10 / n

def bar(s):
    try:
        return foo(s) * 2
    except StandardError, e:
        print 'Error!'
        raise

def main():
    bar('0')

# 在bar()函数中，已经捕获了错误，但是，打印一个Error!后，又把错误通过raise语句抛出去了
# 这样做是因为捕获错误目的只是记录一下，便于后续追踪。
# 但是，由于当前函数不知道应该怎么处理该错误，所以，最恰当的方式是继续往上抛，让顶层调用者去处理。
# raise语句如果不带参数，就会把当前错误原样抛出。

# 在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：只要是合理的转换逻辑就可以
try:
    10 / 0
except ZeroDivisionError:
    raise ValueError('input error!')

main()


# 调试
# 方法一：print
# 方法二：断言    凡是用print来辅助查看的地方，都可以用断言（assert）来替代：
# 如果断言失败，assert语句本身就会抛出AssertionError：
# 启动Python解释器时可以用-O参数来关闭assert：
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')

# 方法三：logging
# 和assert比，logging不会抛出错误，而且可以输出到文件：
import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print 10 / n
# 输出 INFO:root:n = 0
# logging允许指定记录信息的级别，有debug，info，warning，error等几个级别，
# 当指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了。
# 这样一来，可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。
# logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。

# 方法四：pdb
s = '0'
n = int(s)
print 10 / n
# $ python -m pdb err.py

# pdb.set_trace()
# 也是用pdb，但是不需要单步执行，
# 只需要import pdb，然后，在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点：
import pdb

s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停
print 10 / n
# 运行代码，程序会自动在pdb.set_trace()暂停并进入pdb调试环境，可以用命令p查看变量，或者用命令c继续运行：




