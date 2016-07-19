# -*- coding:utf-8 -*-


# type() 获取对象信息
import types
print type('abc') == types.StringType
print type(u'abc') == types.UnicodeType
print type([])==types.ListType
print type(str)==types.TypeType
print type(int)==type(str)==types.TypeType      # 所有类型本身的类型就是TypeType