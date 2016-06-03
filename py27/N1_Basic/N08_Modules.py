#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 包结构
# 包package --> 模块module
# 每个包必须有__init__.py 否则当做普通目录
# __init__.py可以是空文件，也可以有Python代码，本身就是一个模块

import Test_fibo
Test_fibo.fib(1000)

# 从模块中直接导入
from Test_fibo import fib, fib2
fib(500)

# 除了下划线开头的均导入
from Test_fibo import *
fib(500)

# 模块搜索路径
# Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中
# 添加自己的搜索目录，有两种方法：
# 一是直接修改sys.path，添加要搜索的目录： sys.path.append('')  运行结束后失效。
# 二是设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中。
# 设置方式与设置Path环境变量类似。注意只需要添加你自己的搜索路径，Python自己本身的搜索路径不受影响。
import sys
print sys.path

# 使用模块
# sys.argv用list存储了命令行的所有参数 argv至少有一个元素，因为第一个参数永远是该.py文件的名称
# 运行python hello.py获得的sys.argv就是['server.py']；
# 运行python server.py Michael获得的sys.argv就是['server.py', 'Michael]。

# 别名
# Python标准库一般会提供StringIO和cStringIO两个库，这两个库的接口和功能是一样的，但是cStringIO是C写的，速度更快
try:
    import cStringIO as StringIO
except ImportError:     # 导入失败会捕获到ImportError
    import StringIO


# 作用域
# 在一个模块中，但有的函数和变量我们希望给别人使用，有的函数和变量我们希望仅仅在模块内部使用。
# 在Python中，是通过_前缀来实现的。
# 类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，我们自己的变量一般不要用这种变量名；
# 似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；
# 之所以我们说，private函数和变量“不应该”被直接引用，而不是“不能”被直接引用，
# 因为Python并没有一种方法可以完全限制访问private函数或变量，但是，从编程习惯上不应该引用private函数或变量。
def _private_1(name):
    return 'Hello, %s' % name


def _private_2(name):
    return 'Hi, %s' % name


def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
    pass
# 在模块里公开greeting()函数，而把内部逻辑用private函数隐藏起来了，
# 这样，调用greeting()函数不用关心内部的private函数细节，这也是一种非常有用的代码封装和抽象的方法，即：
# 外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。


# __future__
# 使用__future__ 必须放在文件头 使整个文件使用新版本特性
# 例如通过unicode_literals来使用Python 3.x的新的语法
from __future__ import unicode_literals
print '\'xxx\' is unicode?', isinstance('xxx', unicode)
print 'u\'xxx\' is unicode?', isinstance(u'xxx', unicode)
print '\'xxx\' is str?', isinstance('xxx', str)
print 'b\'xxx\' is str?', isinstance(b'xxx', str)

# Python 2.x中，对于除法有两种情况，如果是整数相除，结果仍是整数，余数会被扔掉，这种除法叫“地板除”
# 在Python 3.x中，所有的除法都是精确除法，地板除用//表示：
from __future__ import division
print '10 / 3 =', 10 / 3
print '10.0 / 3 =', 10.0 / 3
print '10 // 3 =', 10 // 3


# 常用内建模块
# collections 提供了额外的数据类型
# 1.namedtuple(): 生成可以使用名字来访问元素内容的tuple子类
# 2.deque: 双端队列，可以快速的从另外一侧追加和推出对象
# 3.Counter: 计数器，主要用来计数
# 4.OrderedDict: 有序字典
# 5.defaultdict: 带有默认值的字典

# namedtuple是一个函数，它用来创建一个自定义的tuple对象， namedtuple('名称', [属性list]):
# 并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
# 用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])         # 创建一个typename为point 属性值分别为 'x' 'y'的tuple对象
p = Point(1, 2)                                 # 创建一个实例
print p.x                                       # 可以通过属性访问
print isinstance(p, Point)                      # 创建的Point对象是tuple的一种子类
print isinstance(p, tuple)
Circle = namedtuple('Circle', ['x', 'y', 'r'])  # 用坐标和半径表示一个圆，也可以用namedtuple定义

# deque 双端队列
# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
# deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print q

# Counter 简单的计数器
from collections import Counter
# 获取出现频率最高的5个字符
s = '''asfdssdxcvgaggsllmpmgdslkgsdmlnlggadm;sdg;'''
c = Counter(s)
print c.most_common(5)
# 统计字符出现的个数
c = Counter()
for ch in 'programming':
    c[ch] += 1

# OrderedDict
# 如果要保持Key的顺序，可以用OrderedDict
# OrderedDict的Key会按照插入的顺序排列，不是Key本身排序
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print d                                             # dict的Key是无序的
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print od                                            # OrderedDict的Key是有序的

# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key
from collections import OrderedDict


class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print 'remove:', last
        if containsKey:
            del self[key]
            print 'set:', (key, value)
        else:
            print 'add:', (key, value)
        OrderedDict.__setitem__(self, key, value)

# defaultdict
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
# 除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')         # 默认值是调用函数返回的，而函数在创建defaultdict对象时传入
dd['key1'] = 'abc'
print dd['key1']        # key1存在
print dd['key2']        # key2不存在，返回默认值


# base64
# Base64是一种用64个字符来表示任意二进制数据的方法
# Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据。
# Base64的原理很简单，首先，准备一个包含64个字符的数组： ['A', 'B', 'C', ... 'a', 'b', 'c', ... '0', '1', ... '+', '/']
# 然后，对二进制数据进行处理，每3个字节一组，一共是3x8=24bit，划为4组，每组正好6个bit：
# 得到4个数字作为索引，然后查表，获得相应的4个字符，就是编码后的字符串
# Base64编码会把3字节的二进制数据编码为4字节的文本数据，长度增加33%，好处是编码后的文本数据可以在邮件正文、网页等直接显示
# 如果要编码的二进制数据不是3的倍数，最后会剩下1个或2个字节怎么办？
# Base64用\x00字节在末尾补足后，再在编码的末尾加上1个或2个=号，表示补了多少字节，解码的时候，会自动去掉。
# Python内置的base64可以直接进行base64的编解码：
import base64
print base64.b64encode('binary\x00string')      # 注意\x00长度为1  16进制的字符 总长度为13 补了两个=
print base64.b64decode('YmluYXJ5AHN0cmluZw==')
# 由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：
print base64.b64encode('i\xb7\x1d\xfb\xef\xff')
print base64.urlsafe_b64encode('i\xb7\x1d\xfb\xef\xff')
print base64.urlsafe_b64decode('abcd--__')
# Base64是一种通过查表的编码方法，不能用于加密，即使使用自定义的编码表也不行。
# Base64适用于小段内容的编码，比如数字证书签名、Cookie的内容等。

# 由于=字符也可能出现在Base64编码中，但=用在URL、Cookie里面会造成歧义，所以，很多Base64编码后会把=去掉：
# 标准Base64:     'abcd' -> 'YWJjZA=='
# 自动去掉=:      'abcd' -> 'YWJjZA'
# 需要加上=把Base64字符串的长度变为4的倍数，就可以正常解码了。
# 例如一个自动补全解码函数：
def bsdecode_add_eq(str):
    return base64.b64decode(str + '='*(4-len(str) % 4))   # 即使多4个=也不会影响解码结果


# struct
# Python没有专门处理字节的数据类型。但由于str既是字符串，又可以表示字节，
# 所以，字节数组＝str。而在C语言中，我们可以很方便地用struct、union来处理字节，以及字节和int，float的转换
# 在Python中，比方说要把一个32位无符号整数变成字节，也就是4个长度的str，你得配合位运算符这么写
n = 10240099
b1 = chr((n & 0xff000000) >> 24)
b2 = chr((n & 0xff0000) >> 16)
b3 = chr((n & 0xff00) >> 8)
b4 = chr(n & 0xff)
s = b1 + b2 + b3 + b4
print s

# Python提供了一个struct模块来解决str和其他二进制数据类型的转换
# struct的pack函数把任意数据类型变成字符串
import struct
struct.pack('>I', 10240099)
# pack的第一个参数是处理指令，'>I'的意思是：>表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
# 后面的参数个数要和处理指令一致。

# unpack把str变成相应的数据类型
struct.unpack('>IH', '\xf0\xf0\xf0\xf0\x80\x80')
# 根据>IH的说明，后面的str依次变为I：4字节无符号整数和H：2字节无符号整数
# 尽管Python不适合编写底层操作字节流的代码，但在对性能要求不高的地方，利用struct就方便多了


# hashlib
# Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等
# 摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。
# 摘要算法就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest，目的是为了发现原始数据是否被人篡改过
# 摘要算法之所以能指出数据是否被篡改过，就是因为摘要函数是一个单向函数，计算f(data)很容易，但通过digest反推data却非常困难。
# 而且，对原始数据做一个bit的修改，都会导致计算出的摘要完全不同。
# MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示。
# 以常见的摘要算法MD5为例，计算出一个字符串的MD5值
import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?')
print md5.hexdigest()

# 如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的
md5 = hashlib.md5()
md5.update('how to use md5 in ')
md5.update('python hashlib?')
print md5.hexdigest()

# 另一种常见的摘要算法是SHA1，调用SHA1和调用MD5完全类似：
# SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示
import hashlib

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in ')
sha1.update('python hashlib?')
print sha1.hexdigest()

# 比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法越慢，而且摘要长度更长。
# 两个不同的数据通过某个摘要算法得到了相同的摘要？
# 完全有可能，因为任何摘要算法都是把无限多的数据集合映射到一个有限的集合中。这种情况称为碰撞

# 摘要算法应用
# 任何允许用户登录的网站都会存储用户登录的用户名和口令。方法是存到数据库表中
# name    | password
# --------+----------
# michael | 123456
# bob     | abc999
# alice   | alice2008
# 如果以明文保存用户口令，如果数据库泄露，所有用户的口令就落入黑客的手里
# 正确的保存口令的方式是不存储用户的明文口令，而是存储用户口令的摘要，比如MD5
# 存储MD5的好处是即使运维人员能访问数据库，也无法获知用户的明文口令
# username | password
# ---------+---------------------------------
# michael  | e10adc3949ba59abbe56e057f20f883e
# bob      | 878ef96e86145580c38c87f0410ad153
# alice    | 99b1c2188db85afee403b1536010c2c9

# 练习
# 根据用户输入的口令，计算出存储在数据库中的MD5口令：
def calc_md5(password):
    pass

# 设计一个验证用户登录的函数，根据用户输入的口令是否正确，返回True或False
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(user, password):
    pass

# 由于常用口令的MD5值很容易被计算出来，所以，要确保存储的用户口令不是那些已经被计算出来的常用口令的MD5，
# 这一方法通过对原始口令加一个复杂字符串来实现，俗称“加盐”
def calc_md5(password):
    return get_md5(password + 'the-Salt')
# 经过Salt处理的MD5口令，只要Salt不被黑客知道，即使用户输入简单口令，也很难通过MD5反推明文口令。
# 但是如果有两个用户都使用了相同的简单口令比如123456，在数据库中，将存储两条相同的MD5值，这说明这两个用户的口令是一样的。
# 如果假定用户无法修改登录名，就可以通过把登录名作为Salt的一部分来计算MD5，从而实现相同口令的用户也存储不同的MD5。

# 练习
# 根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5：
db = {}

def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')

# 根据修改后的MD5算法实现用户登录的验证
def login(username, password):
    pass


# itertools
# Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数
# 首先，我们看看itertools提供的几个“无限”迭代器：
import itertools
natuals = itertools.count(1)
for n in natuals:
    print n
# 因为count()会创建一个无限的迭代器，所以上述代码会打印出自然数序列，根本停不下来，只能按Ctrl+C退出
# cycle()会把传入的一个序列无限重复下去：
import itertools
cs = itertools.cycle('ABC')         # 注意字符串也是序列的一种
for c in cs:
    print c
# repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
ns = itertools.repeat('A', 10)      # 打印10次'A'
for n in ns:
    print n
# 无限序列只有在for迭代时才会无限地迭代下去，
# 如果只是创建了一个迭代对象，它不会事先把无限个元素生成出来，事实上也不可能在内存中创建无限多个元素。
# 无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
for n in ns:        # 打印出1到10
    print n

# itertools提供的几个迭代器操作函数更加有用：
# chain()
# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
for c in itertools.chain('ABC', 'XYZ'):         # 迭代效果：'A' 'B' 'C' 'X' 'Y' 'Z'
    print c
# groupby()
# groupby()把迭代器中相邻的重复元素挑出来放在一起：
for key, group in itertools.groupby('AAABBBCCAAA'):
    print key, list(group)      # 用list()函数是为了显示出group内容 因为group是一个object
# 实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，这两个元素就被认为是在一组的，而函数返回值作为组的key。
# 如果我们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的key：
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print key, list(group)

# imap()
# imap()和map()的区别在于，imap()可以作用于无穷序列，并且，如果两个序列的长度不一致，以短的那个为准。
for x in itertools.imap(lambda x, y: x * y, [10, 20, 30], itertools.count(1)):
    print x
# 注意imap()返回一个迭代对象，而map()返回list。当你调用map()时，已经计算完毕：
r = map(lambda x: x*x, [1, 2, 3])
print r             # r已经计算出来了
# 调用imap()时，并没有进行任何计算：
r = itertools.imap(lambda x: x*x, [1, 2, 3])
print r             # r只是一个迭代对象
# 必须用for循环对r进行迭代，才会在每次循环过程中计算出下一个元素
for x in r:
    print x
# 说明imap()实现了“惰性计算”，也就是在需要获得结果的时候才计算。类似imap()这样能够实现惰性计算的函数就可以处理无限序列
r = itertools.imap(lambda x: x*x, itertools.count(1))
for n in itertools.takewhile(lambda x: x<100, r):
    print n
# 如果把imap()换成map()去处理无限序列会一直计算下去
r = map(lambda x: x*x, itertools.count(1))

# ifilter()
# ifilter()就是filter()的惰性实现。


# XML
# 操作XML有两种方法：DOM和SAX。
# DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。
# SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件
# 正常情况下，优先考虑SAX，因为DOM实在太占内存

# 在Python中使用SAX解析XML非常简洁，
# 通常我们关心的事件是start_element，end_element和char_data，准备好这3个函数，然后就可以解析xml了。
# 当SAX解析器读到一个节点时  <a href="/">python</a> 会产生3个事件：
# 1.start_element事件，在读取<a href="/">时；
# 2.char_data事件，在读取python时；
# 3.end_element事件，在读取</a>时。
from xml.parsers.expat import ParserCreate


class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''
handler = DefaultSaxHandler()
parser = ParserCreate()
parser.returns_unicode = True
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)
# 当设置returns_unicode为True时，返回的所有element名称和char_data都是unicode，处理国际化更方便
# 需要注意的是读取一大段字符串时，CharacterDataHandler可能被多次调用，所以需要自己保存起来，在EndElementHandler里面再合并

# 生成XML
# 最简单也是最有效的生成XML的方法是拼接字符串
L = []
L.append(r'<?xml version="1.0"?>')
L.append(r'<root>')
L.append(encode('some & data'))
L.append(r'</root>')
''.join(L)
# 要生成复杂的XML呢？建议你不要用XML，改成JSON
# 解析XML时，注意找出自己感兴趣的节点，响应事件时，把节点数据保存起来。解析完毕后，就可以处理数据

# 练习
# 解析Yahoo的XML格式的天气预报，获取当天和最近几天的天气
# http://weather.yahooapis.com/forecastrss?u=c&w=2151330
# 参数w是城市代码，要查询某个城市代码，可以在weather.yahoo.com搜索城市，浏览器地址栏的URL就包含城市代码。


# HTMLParser
# HTML本质上是XML的子集，但是HTML的语法没有XML那么严格，所以不能用标准的DOM或SAX来解析HTML。
# Python提供了HTMLParser来非常方便地解析HTML，只需简单几行代码
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print('data')

    def handle_comment(self, data):
        print('<!-- -->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

parser = MyHTMLParser()
parser.feed('<html><head></head><body><p>Some <a href=\"#\">html</a> tutorial...<br>END</p></body></html>')
# feed()方法可以多次调用，也就是不一定一次把整个HTML字符串都塞进去，可以一部分一部分塞进去
# 特殊字符有两种，一种是英文表示的&nbsp;，一种是数字表示的&#1234;，这两种字符都可以通过Parser解析出来

# 练习
# 找一个网页，例如https://www.python.org/events/python-events/，用浏览器查看源码并复制，
# 尝试解析一下HTML，输出Python官网发布的会议时间、名称和地点。


# glob
# 查找匹配的文件
# 在查找的条件中，需要用到Unix shell中的匹配规则：
#   *    :   匹配所所有
#   ?    :   匹配一个字符
#   []   :   匹配指定范围内的字符 如：[0-9]匹配数字。
#   *.*  :   匹配如：[hello.txt,cat.xls,xxx234s.doc]
#   ?.*  :   匹配如：[1.txt,h.py]
#   ?.gif:   匹配如：[x.gif,2.gif]
import glob
all_txt_filename = glob.glob('c:\\users\\dell\\????.txt')
print all_txt_filename


# 常用第三方模块
# PIL（Python Imaging Library） 现在已经用Pillow替代PIL了 因为PIL已经不再维护
from PIL import Image           # 不能用import image形式
im_local = 'C:\Users\dell\Documents\GitHub\PythonStudy\py27\N1_Basic\Pic.jpg'
im = Image.open(im_local)
print im.format, im.size, im.mode
im.show()
im.thumbnail((im.size[0]/2, im.size[1]/2))      # 缩放到50%:
im.show()

# 其他功能如切片、旋转、滤镜、输出文字、调色板等一应俱全
# 模糊效果
from PIL import Image
from PIL import ImageFilter
im = Image.open(im_local)
im2 = im.filter(ImageFilter.BLUR)
im2.show()


# PIL的ImageDraw提供了一系列绘图方法，让我们可以直接绘图
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色1
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 36)          # 创建Font对象
draw = ImageDraw.Draw(image)                        # 创建Draw对象
for x in range(width):                              # 填充每个像素
    for y in range(height):
        draw.point((x, y), fill=rndColor())
for t in range(4):                                  # 输出文字
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
image = image.filter(ImageFilter.BLUR)              # 模糊
image.show(image)




