#!/usr/bin/env python
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


# 调试 Debug
# 方法一：print
# 方法二：断言    凡是用print来辅助查看的地方，都可以用断言（assert）来替代：
# 如果断言false，assert语句本身就会抛出AssertionError：
# 启动Python解释器时可以用-O参数来关闭assert：
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'     # assert后的表达式为false时抛出错误 AssertionError
    return 10 / n

def main():
    foo('0')

# 方法三：logging
# 和assert比，logging不会抛出错误，而是输出到文件：
# logging允许指定记录信息的级别，日志级别大小关系为：
# CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET，当然也可以自己定义日志级别。
# 当指定level=INFO时，logging.debug就不起作用了。越往后级别越高，默认warning
# 这样一来，可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。
# logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。
import logging
# 指定级别 规定格式 输出文件名称方式
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='mylog.log',
                filemode='w')

logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')
# logging.basicConfig函数各参数:
# filename: 指定日志文件名
# filemode: 和file函数意义相同，指定日志文件的打开模式，’w'或’a’
# format: 指定输出的格式和内容，format可以输出很多有用信息，如上例所示:
# (levelno)s: 打印日志级别的数值
# (levelname)s: 打印日志级别名称
# (pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0
# (filename)s: 打印当前执行程序名
# (funcName)s: 打印日志的当前函数
# (lineno)d: 打印日志的当前行号
# (asctime)s: 打印日志的时间
# (thread)d: 打印线程ID
# (threadName)s: 打印线程名称
# (process)d: 打印进程ID
# (message)s: 打印日志信息
# datefmt: 指定时间格式，同time.strftime()
# level: 设置日志级别，默认为logging.WARNING
# stream: 指定将日志的输出流，可以指定输出到sys.stderr, sys.stdout或者文件，
# 默认输出到sys.stderr，当stream和filename同时指定时，stream被忽略

# 将日志同时输出到文件和屏幕
import logging

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='mylog.log',
                filemode='w')

# 定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)


logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')

# logging之日志回滚
import logging
from logging.handlers import RotatingFileHandler

# 定义一个RotatingFileHandler，最多备份5个日志文件，每个日志文件最大10M
Rthandler = RotatingFileHandler('myapp.log', maxBytes=10*1024*1024,backupCount=5)
Rthandler.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
Rthandler.setFormatter(formatter)
logging.getLogger('').addHandler(Rthandler)
# 从上例和本例可以看出，logging有一个日志处理的主对象，其它处理方式都是通过addHandler添加进去的。
# logging的几种handle方式如下：
# logging.StreamHandler: 日志输出到流，可以是sys.stderr、sys.stdout或者文件
# logging.FileHandler: 日志输出到文件
# 日志回滚方式，实际使用时用RotatingFileHandler和TimedRotatingFileHandler
# logging.handlers.BaseRotatingHandler
# logging.handlers.RotatingFileHandler
# logging.handlers.TimedRotatingFileHandler
# logging.handlers.SocketHandler: 远程输出日志到TCP/IP sockets
# logging.handlers.DatagramHandler:  远程输出日志到UDP sockets
# logging.handlers.SMTPHandler:  远程输出日志到邮件地址
# logging.handlers.SysLogHandler: 日志输出到syslog
# logging.handlers.NTEventLogHandler: 远程输出日志到Windows NT/2000/XP的事件日志
# logging.handlers.MemoryHandler: 日志输出到内存中的制定buffer
# logging.handlers.HTTPHandler: 通过"GET"或"POST"远程输出到HTTP服务器
# 由于StreamHandler和FileHandler是常用的日志处理方式，所以直接包含在logging模块中，而其他方式则包含在logging.handlers模块中，


# 方法四：pdb
# 命令 l 来查看代码
# 命令 n 可以单步执行代码
# 命令 c 继续运行
# 命令 p 变量名 来查看变量
# 命令 q 结束调试，退出程序
s = '0'
n = int(s)
print 10 / n


# pdb.set_trace()
# 也是用pdb，但是不需要单步执行
# 只需要import pdb，然后，在可能出错地方的前面放一个pdb.set_trace()，就可以设置一个断点：
import pdb

s = '0'
n = int(s)
pdb.set_trace()     # 运行到这里会自动暂停
print 10 / n
# 运行代码，程序会自动在pdb.set_trace()暂停并进入pdb调试环境，可以用命令p查看变量，或者用命令c继续运行：


# 方法五：IDE 可以比较爽地设置断点、单步执行
# 虽然用IDE调试起来比较方便，但是最后你会发现，logging才是终极武器。


# 单元测试 Unit Test
class Dict(dict):
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

d = Dict(a=1, b=2)

# 编写单元测试
# 以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。
# unittest.TestCase提供了很多内置的条件判断
# 调用这些方法就可以断言输出是否是我们所期望的。最常用的断言就是assertEquals()
import unittest


class TestDict(unittest.TestCase):
    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEquals(d.a, 1)
        self.assertEquals(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEquals(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEquals(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):           # 期待抛出指定类型的Error
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

# 运行单元测试
# 编写好单元测试，我们就可以运行单元测试。
# 最简单的运行方式是在mydict_test.py的最后加上两行代码：
if __name__ == '__main__':
    unittest.main()

# 另一种更常见的方法是在命令行通过参数-m unittest直接运行单元测试：
# python -m unittest mydict_test
# 这是推荐的做法，因为这样可以一次批量运行很多单元测试，并且，有很多工具可以自动来运行这些单元测试。


# setUp与tearDown
# 单元测试中编写两个特殊的setUp()和tearDown()方法 这两个方法会分别在每调用一个测试方法的前后分别被执行。
# 测试需要启动一个数据库，这时，就可以在setUp()方法中连接数据库，在tearDown()方法中关闭数据库
class TestDict(unittest.TestCase):
    def setUp(self):
        print 'setUp...'

    def tearDown(self):
        print 'tearDown...'
# 单元测试的测试用例要覆盖常用的输入组合、边界条件和异常。
# 单元测试通过了并不意味着程序就没有bug了，但是不通过程序肯定有bug。


# 文档测试
# Python内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试。
# doctest严格按照Python交互式命令行的输入和输出来判断测试结果是否正确。
# 只有测试异常的时候，可以用...表示中间一大段烦人的输出。
# 当模块正常导入时，doctest不会被执行。只有在命令行运行时，才执行doctest。所以，不必担心doctest会在非测试环境下执行
class Dict(dict):
    '''
    Example dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

if __name__=='__main__':
    import doctest
    doctest.testmod()




