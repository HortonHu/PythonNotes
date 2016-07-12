# -*- coding:utf-8 -*-


# 错误处理
# 高级语言通常都内置了一套try...except...finally...的错误处理机制，Python也不例外。
# 当我们认为某些代码可能会出错时，就可以用try来运行这段代码，
# 如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，
# 执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕。
# 注意except写法
try:
    print 'try...'
    r = 10 / 0                  # 遇到错误 接着执行except
    print 'result:', r
except ZeroDivisionError, e:    # except捕获到ZeroDivisionError
    print 'except:', e          # e的type是<type 'exceptions.ZeroDivisionError'>
finally:                        # 不伦如何都会执行 可以没有finally
    print 'finally...'
print 'END'

# 可以有多个except来捕获不同类型的错误：
try:
    print 'try...'
    r = 10 / int('a')
    print 'result:', r
except ValueError, e:               # 数值错误
    print 'ValueError:', e
except ZeroDivisionError, e:        # 除零错误
    print 'ZeroDivisionError:', e
else:                   # 可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句
    print 'No Error!'
finally:
    print 'finally...'
print 'END'

# 捕获所有异常
try:
    file = open('test.txt', 'rb')
except Exception:
    # 打印一些异常日志，如果你想要的话
    raise

# Python的错误其实也是class，所有的错误类型都继承自BaseException，
# 所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类都包含
try:
    foo()
except StandardError, e:
    print 'StandardError', e
except ValueError, e:
    print 'ValueError', e
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
        print 'Error!', e
    finally:
        print 'finally...'

# 在没有触发异常的时候执行一些代码，通过一个else从句来实现
# 只是想让一些代码在没有触发异常的情况下执行，同时这段代码中的任意异常不会被try捕获
try:
    print('I am sure no exception is going to occur!')
except Exception:
    print('exception')
else:
    # 这里的代码只会在try语句里没有触发异常时运行,
    # 但是这里的异常将 *不会* 被捕获
    print('This would only run if no exception occurs. And an error here '
          'would NOT be caught.')
finally:
    print('This would be printed in every case.')

# 获得更详细的错误信息
import traceback
try:
    a = 1 / 0                       # some error
except ZeroDivisionError, e:
    print 'Error:', e
    traceback.print_exc()           # 会提示相应的位置


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
# 第1行：  Traceback (most recent call last):                      告诉我们这是错误的跟踪信息。
# 第2行：  File "err.py", line 7, in <module>
# 第3行：  File "<input>", line 6, in main                         调用main出错了
# 第4行：  File "<input>", line 4, in bar                          调用bar出错了
# 第5行：  File "<input>", line 2, in foo                          调用foo出错了
# 第6行：  ZeroDivisionError: integer division or modulo by zero   错误类型ZeroDivisionError


# 记录错误
# Python内置的logging模块可以非常容易地记录错误信息
# logging还可以把错误记录到日志文件里，方便事后排查（作为文件运行时）
import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except StandardError, e:
        logging.exception(e)        # 记录错误原因

main()
print 'END'


# 抛出错误 raise
# 错误是class，捕获一个错误就是捕获到该class的一个实例。因此，错误并不是凭空产生的，而是有意创建并抛出的。
# Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。
# 如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例
# 只有在必要的时候才定义我们自己的错误类型。
# 如果可以选择Python已有的内置的错误类型（比如ValueError，TypeError），尽量使用Python内置的错误类型。
class FooError(StandardError):      # 继承StandardError
    pass

def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n


# 另一种错误处理的方式：
# 在bar()函数中，已经捕获了错误，但是，打印一个Error!后，又把错误通过raise语句抛出去了
# 这样做是因为捕获错误目的只是记录一下，便于后续追踪。
# 但是，由于当前函数不知道应该怎么处理该错误，所以，最恰当的方式是继续往上抛，让顶层调用者去处理。
# raise语句如果不带参数，就会把当前错误原样抛出。
def foo(s):
    n = int(s)
    return 10 / n

def bar(s):
    try:
        return foo(s) * 2
    except StandardError, e:
        print 'Error!'
        raise           # 向上抛出

def main():
    bar('0')

main()


# 在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：只要是合理的转换逻辑就可以
try:
    10 / 0
except ZeroDivisionError:
    raise ValueError('input error!')


# try except finally中出现了return的执行顺序
# 无论是在try还是在except中，遇到return时，只要设定了finally语句，就会中断当前的return语句，跳转到finally中执行，
# 如果finally中遇到return语句，就直接返回，不再跳转回try/excpet中被中断的return语句
# http://www.cnblogs.com/ybwang/archive/2015/08/18/4738621.html
# http://www.2cto.com/kf/201405/304975.html
# http://www.jb51.net/article/65487.htm
