#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 文件读写

# 读文件
# 要以读文件的模式打开一个文件对象，使用Python内置的open()函数，传入文件名和标示符：
f = open('/Users/michael/test.txt', 'r')
# 调用read()方法可以一次读取文件的全部内容，Python把内容读到内存，用一个str对象表示：
f.read()
# 最后一步是调用close()方法关闭文件。
# 文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的：
f.close()
# 由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。
# 所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：
try:
    f = open('/path/to/file', 'r')
    print f.read()
finally:
    if f:
        f.close()

# Python引入了with语句来自动帮我们调用close()方法：
# 和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。
with open('/path/to/file', 'r') as f:
    print f.read()

# read()会一次性读取文件的全部内容 文件太大时 可以反复调用read(size) 每次最多读取size个字节的内容。
# readline()可以每次读取一行内容
# readlines()一次读取所有内容并按行返回list 如果是配置文件 调用readlines()最方便
for line in f.readlines():
    print(line.strip()) # 把末尾的'\n'删掉

# file-like Object
# 像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。
# 除了file外，还可以是内存的字节流，网络流，自定义流等等。
# file-like Object不要求从特定类继承，只要写个read()方法就行。
# StringIO就是在内存中创建的file-like Object，常用作临时缓冲。


# 二进制文件
# 要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可
f = open('/Users/michael/test.jpg', 'rb')
f.read()

# 字符编码
# 要读取非ASCII编码的文本文件，就必须以二进制模式打开，再解码。比如GBK编码的文件：
f = open('/Users/michael/gbk.txt', 'rb')
u = f.read().decode('gbk')
u
print u

# Python还提供了一个codecs模块帮我们在读文件时自动转换编码，直接读出unicode：
import codecs
with codecs.open('/Users/michael/gbk.txt', 'r', 'gbk') as f:
    f.read()    # u'\u6d4b\u8bd5'


# 写文件
# 写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：
f = open('/Users/michael/test.txt', 'w')
f.write('Hello, world!')
f.close()
# 可以反复调用write()来写入文件，但是务必要调用f.close()来关闭文件。
# 当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。
# 只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。
# 忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。
# 用with语句来得保险
with open('/Users/michael/test.txt', 'w') as f:
    f.write('Hello, world!')
# 在Python中，文件读写是通过open()函数打开的文件对象完成的。使用with语句操作文件IO是个好习惯。


# 操作文件和目录
# Python内置的os模块可以直接调用操作系统提供的接口函数。
import os
os.name     # 操作系统名字
# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
# 要获取详细的系统信息，可以调用uname()函数：
# uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。


# 环境变量
# 操作系统中定义的环境变量，全部保存在os.environ这个dict中
# 获取某个环境变量的值，可以调用os.getenv()


# 操作文件和目录
# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块
# 查看、创建和删除目录可以这么调用：
# 查看当前目录的绝对路径:
now_path = os.path.abspath('.')
# 在某个目录下创建一个新目录， 首先把新目录的完整路径表示出来:
# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。
true_path = os.path.join(now_path, 'testdir')
# 然后创建一个目录:
os.mkdir(true_path)
# 删掉一个目录:
os.rmdir(true_path)

# 同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()
# 把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
os.path.split('/Users/michael/testdir/file.txt')    # ('/Users/michael/testdir', 'file.txt')
# os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：
os.path.splitext('/path/to/file.txt')               # ('/path/to/file', '.txt')
# 这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。

# 假定当前目录下有一个test.txt文件：
# 对文件重命名:
os.rename('test.txt', 'test.py')
# 删掉文件:
os.remove('test.py')
# 复制文件的函数居然在os模块中不存在 因为复制文件并非由操作系统提供的系统调用
# shutil模块提供了copyfile()的函数 可以看做是os模块的补充。


# 列出当前目录下的所有目录
print [x for x in os.listdir('.') if os.path.isdir(x)]
# 列出所有的.py文件
print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']

# 练习：编写一个search(s)的函数，
# 能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出完整路径：
# $ python search.py test
# unit_test.log
# py/test.py
# py/test_os.py
# my/logs/unit-test-result.txt


# 序列化
