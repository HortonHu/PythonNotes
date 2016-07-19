# -*- coding:utf-8 -*-


# codecs模块
# 提供了一个open函数，可以直接指定好编码打开一个文本文件，读取到的文件内容则直接是一个unicode字符串。
import codecs

with codecs.open('test.txt', 'w', 'utf-8') as f:
    f.write(u'测试')

with codecs.open('test.txt', 'r', 'utf-8') as f:
    data = f.read()
    print 'type: ', type(data)