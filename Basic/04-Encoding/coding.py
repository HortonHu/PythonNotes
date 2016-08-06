# -*- coding:utf-8 -*-

# 编码方式
# ASCII     1个字节[0~255]
# Unicode   通常2个字节[0~65535]
# UTF-8     1~6个字节 常用的英文字母1个字节，汉字通常是3个字节，生僻字符4-6个字节。ASCII可被看做是UTF-8的一部分。
# 内存中统一使用Unicode，保存或者传输的时候需要转换为UTF-8


# ASCII(str)编码、字符转换
print ord('A')
print chr(65)
# Unicode编码、字符转换
print ord(u'A')
print unichr(65)

# Unicode   汉字u'中'  即u'\u4e2d'
# UTF-8     汉字'中    即'\xe4\xb8\xad' 用3个16进制数表示
# Unicode编码为UTF-8 : encode('utf-8')
u'中'                    # u'\u4e2d'
u'中'.encode('utf-8')    # '\xe4\xb8\xad'
# UTF-8解编码为Unicode : decode('utf-8')
'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')  # u'\u4e2d\u6587'
# 例如在写入文件的时候，unicode就要编码为utf-8不然就会报错
with open('a.txt', 'w') as f:
    f.write(u'测试'.encode('utf-8'))

import chardet
with open('a.txt', 'r') as f:
    s = f.read()
    print s
    print chardet.detect(s)


# python 2.x里的字符串用'xxx'表示str，Unicode字符串用u'xxx'表示unicode，在2.x中最好都使用unicode
# 而在3.x中，所有字符串都被视为unicode
# 2.x中以'xxx'表示的str在3.x中就必须写成b'xxx'，以此表示“二进制字符串”。

# 用chardet判断字符编码方式
# confidence是预测这种编码的可能性，encoding是编码名称。
import chardet
s = u'abc'.encode('utf-8')
print chardet.detect(s)