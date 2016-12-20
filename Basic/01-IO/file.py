# -*- coding:utf-8 -*-


# 打开文件：
# open(filename, mode)或者file(filename, mode),推荐使用open
# mode:
# r:读 w:覆盖写 a:添加
# 对于二进制文件，比如图片、视频等等，加上'b'即可
# 对于同时读写的 加上'+'
# r+ 读写         文件不存在时报错    打开后文件指针在开头 此时写会覆盖开头已有的内容
# w+ 覆盖读写     文件不存在时创建    打开后文件指针在开头 打开后即清空文件
# a+ 添加读写     文件不存在时创建    打开后文件指针在末尾 此时写会添加在文件末尾

# 读取文件：
# f.read(size)      读取size大小内容到一个string,缺省size则读取全部。位置指针已经到文件尾
# f.readline()      读取一行内容到一个string中，位置指针移动到下一行开头
# f.readlines()     读取多行内容，按行读取至一个list中，位置指针已经到文件尾
# 写入文件：
# 类似于读文件，但是python只有在close方法调用的时候才会完全写入，因此推荐使用with

# 关闭文件：
# f.close()


# 由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。
# 所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：
try:
    f = open('filename', 'r')
    print f.read()
finally:
    if f:           # 如果f打开过
        f.close()
# Python引入了with语句来自动帮我们调用close()方法：
# 和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。
# 在Python中，文件读写是通过open()函数打开的文件对象完成的。使用with语句操作文件IO是个好习惯。
with open('file', 'r') as f:
    print f.read()


# 要读取非ASCII编码的文本文件，就必须以二进制模式打开，再解码。比如GBK编码的文件：
f = open('/Users/michael/gbk.txt', 'rb')
u = f.read().decode('gbk')
print u
# Python还提供了一个codecs模块帮我们在读文件时自动转换编码，直接读出unicode：
import codecs
with codecs.open('/Users/michael/gbk.txt', 'r', 'gbk') as f:
    f.read()    # u'\u6d4b\u8bd5'