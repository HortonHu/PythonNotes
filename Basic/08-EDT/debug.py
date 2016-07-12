# -*- coding:utf-8 -*-


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
                filemode='a')

logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')
# logging.basicConfig函数各参数:
# filename: 日志文件名
# filemode: 和file函数意义相同，指定日志文件的打开模式，’w'或’a’
# format: 指定输出的格式和内容，format可以输出很多有用信息，如上例所示:
#         (levelno)s:       打印日志级别的数值
#         (levelname)s:     打印日志级别名称
#         (pathname)s:      打印当前执行程序的路径，其实就是sys.argv[0]
#         (filename)s:      打印当前执行程序名
#         (funcName)s:      打印日志的当前函数
#         (lineno)d:        打印日志的当前行号
#         (asctime)s:       打印日志的时间
#         (thread)d:        打印线程ID
#         (threadName)s:    打印线程名称
#         (process)d:       打印进程ID
#         (message)s:       打印日志信息
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
                filemode='a')

# 定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象
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
Rthandler = RotatingFileHandler('myapp.log', maxBytes=10*1024*1024, backupCount=5)
Rthandler.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
Rthandler.setFormatter(formatter)
logging.getLogger('').addHandler(Rthandler)
# 从上例和本例可以看出，logging有一个日志处理的主对象，其它处理方式都是通过addHandler添加进去的。
# logging的几种handle方式如下：
# logging.StreamHandler:    日志输出到流，可以是sys.stderr、sys.stdout或者文件
# logging.FileHandler:      日志输出到文件
# 日志回滚方式，实际使用时用RotatingFileHandler和TimedRotatingFileHandler
# logging.handlers.BaseRotatingHandler
# logging.handlers.RotatingFileHandler
# logging.handlers.TimedRotatingFileHandler
# logging.handlers.SocketHandler:       远程输出日志到TCP/IP sockets
# logging.handlers.DatagramHandler:     远程输出日志到UDP sockets
# logging.handlers.SMTPHandler:         远程输出日志到邮件地址
# logging.handlers.SysLogHandler:       日志输出到syslog
# logging.handlers.NTEventLogHandler:   远程输出日志到Windows NT/2000/XP的事件日志
# logging.handlers.MemoryHandler:       日志输出到内存中的制定buffer
# logging.handlers.HTTPHandler:         通过"GET"或"POST"远程输出到HTTP服务器
# 由于StreamHandler和FileHandler是常用的日志处理方式，直接包含在logging模块中，其他方式则包含在logging.handlers模块中


# 方法四：pdb
# 在命令行中 python -m pdb filename.py 进入pdb调试
#       命令 l    查看代码
#       命令 n    可以单步执行代码(next)
#       命令 s    执行当前代码行，并停在第一个能停的地方(step in)
#       命令 c    继续运行(continue)
#       命令 p    变量名 来查看变量
#       命令 q    结束调试，退出程序
# 单步跳过（next）和单步进入（step）的区别在于
# 单步进入会进入当前行调用的函数内部并停在里面
# 而单步跳过会（几乎）全速执行完当前行调用的函数，并停在当前函数的下一行。

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
