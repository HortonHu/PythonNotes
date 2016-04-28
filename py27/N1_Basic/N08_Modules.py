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
# 运行python hello.py获得的sys.argv就是['hello.py']；
# 运行python hello.py Michael获得的sys.argv就是['hello.py', 'Michael]。

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
# collections 提供了许多有用的集合类
# namedtuple是一个函数，它用来创建一个自定义的tuple对象， namedtuple('名称', [属性list]):
# 并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
# 用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])         # 创建一个typename为point 属性值分别为 'x' 'y'的tuple对象
p = Point(1, 2)                                 # 创建一个实例
print p.x                                       # 通过属性访问

# 创建的Point对象是tuple的一种子类
print isinstance(p, Point)
print isinstance(p, tuple)

# 用坐标和半径表示一个圆，也可以用namedtuple定义
Circle = namedtuple('Circle', ['x', 'y', 'r'])

# deque
# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print q
# deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素

# defaultdict
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
# 除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')         # 默认值是调用函数返回的，而函数在创建defaultdict对象时传入
dd['key1'] = 'abc'
print dd['key1']        # key1存在
print dd['key2']        # key2不存在，返回默认值

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

# Counter
# Counter是一个简单的计数器
# 统计字符出现的个数
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] += 1

# base64
# Base64是一种用64个字符来表示任意二进制数据的方法


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
# pack的第一个参数是处理指令，'>I'的意思是：
# >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
# 后面的参数个数要和处理指令一致。

# unpack把str变成相应的数据类型
struct.unpack('>IH', '\xf0\xf0\xf0\xf0\x80\x80')
# 根据>IH的说明，后面的str依次变为I：4字节无符号整数和H：2字节无符号整数
# 尽管Python不适合编写底层操作字节流的代码，但在对性能要求不高的地方，利用struct就方便多了


# hashlib


# itertools


# XML


# HTMLParser


# 常用第三方模块
# PIL（Python Imaging Library） 现在已经用Pillow替代PIL了 因为PIL已经不再维护
from PIL import Image       # 不能用import image形式
im = Image.open('C:\Users\dell\Documents\GitHub\PythonStudy\py27\N1_Basic\Pic.jpg')
print im.format, im.size, im.mode
im.thumbnail((im.size[0]/2, im.size[1]/2))
im.show()





