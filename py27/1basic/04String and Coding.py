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