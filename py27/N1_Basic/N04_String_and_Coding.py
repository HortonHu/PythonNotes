#!/usr/bin/env python
# -*- coding:utf-8 -*-

# String and Coding
print ord('A')
print chr(65)
print u'中'
print u'\u4e2d'

# 把u'xxx'转换为UTF-8编码的'xxx'用encode('utf-8')方法：
print u'ABC'.encode('utf-8')
print u'中文'.encode('utf-8')

# UTF-8编码表示的字符串'xxx'转换为Unicode字符串u'xxx'用decode('utf-8')
'abc'.decode('utf-8')
'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

len(u'ABC')
len('ABC')
len(u'中文')
len('\xe4\xb8\xad\xe6\x96\x87')