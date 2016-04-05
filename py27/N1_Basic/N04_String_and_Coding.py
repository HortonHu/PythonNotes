#!/usr/bin/env python
# -*- coding:utf-8 -*-

# String and Coding
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
