#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 用chardet判断字符编码
# confidence是预测这种编码的可能性，encoding是编码名称。
import chardet
s = u'abc'.encode('utf-8')
print chardet.detect(s)

# ASCII 转换
print ord('A')
print chr(65)
# Unicode
print u'中'
print u'\u4e2d'

# Unicode to UTF-8 : encode('utf-8')
print u'ABC'.encode('utf-8')
print u'中文'.encode('utf-8')
# UTF-8 to Unicode : decode('utf-8')
'abc'.decode('utf-8')
'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

# 各种编码方式字节大小
len(u'ABC')				# unicode
len('ABC')				# ASCII
len(u'中')				# Unicode 中
len('\xe4\xb8\xad')		# UTF-8 中

# 2.x里的字符串用'xxx'表示str，Unicode字符串用u'xxx'表示unicode
# 而在3.x中，所有字符串都被视为unicode
# 2.x中以'xxx'表示的str在3.x中就必须写成b'xxx'，以此表示“二进制字符串”。