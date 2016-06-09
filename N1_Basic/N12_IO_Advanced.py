#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 文件读写

# 读文件
# 要以读文件的模式打开一个文件对象，使用Python内置的open()函数，传入文件名和标示符：
f = open('test.txt', 'r')
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
    if f:           # 如果f打开过
        f.close()

# Python引入了with语句来自动帮我们调用close()方法：
# 和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。
with open('C:\Users\dell\Documents\GitHub\PythonStudy\py27\N1_Basic\Data.txt', 'r') as f:
    print f.read()

# read()会一次性读取文件的全部内容 文件太大时 可以反复调用read(size) 每次最多读取size个字节的内容。
# readline()可以每次读取一行内容
# readlines()一次读取所有内容并按行返回list 如果是配置文件 调用readlines()最方便
with open('C:\Users\dell\Documents\GitHub\PythonStudy\py27\N1_Basic\Data.txt', 'r') as f:
    for line in f.readlines():
        print line.strip()  # 把末尾的'\n'删掉

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
print os.environ
print os.getenv('PATH')


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
(a, b) = os.path.split('/Users/michael/testdir/file.txt')    # ('/Users/michael/testdir', 'file.txt')
print a
print b
# os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：
os.path.splitext('/path/to/file.txt')               # ('/path/to/file', '.txt')
# 这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。

# 假定当前目录下有一个test.txt文件：
# 对文件重命名:
os.rename('test.txt', 'horton.py')
# 删掉文件:
os.remove('horton.py')
# 复制文件的函数在os模块中不存在 因为复制文件并非由操作系统提供的系统调用
# shutil模块提供了copyfile()的函数 可以看做是os模块的补充。

# 获取当前目录
print os.getcwd()
# 更改当前目录
os.chdir( "C:\\123")    # 将当前目录设为 "C:\123", 相当于DOC命令的 CD C:\123

# 列出当前目录下的所有目录
print [x for x in os.listdir('.') if os.path.isdir(x)]
# 列出所有的.py文件
print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']

# 练习：编写一个search(s)的函数，
# 能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出完整路径：
# $ python search.py test
# unit_test.log
# py/test.py
# py/test_os.py
# my/logs/unit-test-result.txt


# 序列化
# 把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling
# 在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。
# 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
# 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
# Python提供两个模块来实现序列化：cPickle和pickle
# 区别在于cPickle是C语言写的，速度快，pickle是纯Python写的，速度慢，跟cStringIO和StringIO一个道理
# 用的时候，先尝试导入cPickle，如果失败，再导入pickle
try:
    import cPickle as pickle
except ImportError:
    import pickle

# 把一个对象序列化并写入文件：
d = dict(name='Bob', age=20, score=88)
pickle.dumps(d)
# pickle.dumps()方法把任意对象序列化成一个str，然后，就可以把这个str写入文件
# 或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
f = open('dump.txt', 'wb')
pickle.dump(d, f)           # 将d给pickle之后写入文件f
f.close()

# 把对象从磁盘读到内存时，可以先把内容读到一个str 然后用pickle.loads()方法反序列化出对象
# 也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象
# 反序列化刚才保存的对象：
f = open('dump.txt', 'rb')
d = pickle.load(f)          # 从文件f中反序列化给d
f.close()
print d
# 这个变量和原来的变量是完全不相干的对象，它们只是内容相同而已。
# Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，并且可能不同版本的Python彼此都不兼容，
# 因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。


# JSON  （JavaScript Object Notation）
# 在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，但更好的方法是序列化为JSON，
# 因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。
# JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。
# JSON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的数据类型对应如下：
# JSON类型	    Python类型
# {}	        dict
# []	        list
# "string"	    'str'或u'unicode'
# 1234.56	    int或float
# true/false	True/False
# null	        None

# Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。
# 把Python对象变成一个JSON：
import json
d = dict(name='Bob', age=20, score=88)
json.dumps(d)
# dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。
# 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，
# 前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
json.loads(json_str)
# 反序列化得到的所有字符串对象默认都是unicode而不是str。
# 由于JSON标准规定JSON编码是UTF-8，所以我们总是能正确地在Python的str或unicode与JSON的字符串之间转换。

# JSON进阶
# Python的dict对象可以直接序列化为JSON的{}，
# 不过，很多时候，我们更喜欢用class表示对象，比如定义Student类，然后序列化：
import json


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)      # 得到一个TypeError
print json.dumps(s)
# 报错是因为默认情况下，dumps()方法不知道如何将Student实例变为一个JSON的{}对象。
# dumps()方法还提供了一大堆的可选参数
# 可选参数default就是把任意一个对象变成一个可序列为JSON的对象，


# 我们只需要为Student专门写一个转换函数，再把函数传进去即可
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

print json.dumps(s, default=student2dict)   # 传入转化函数student2dict
# Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON

# 如果遇到一个Teacher类的实例，照样无法序列化为JSON。我们可以偷个懒，把任意class的实例变为dict：
# 因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class
print json.dumps(s, default=lambda obj: obj.__dict__)


# 同样的道理，如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，
# 然后，我们传入的object_hook函数负责把dict转换为Student实例：
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))

