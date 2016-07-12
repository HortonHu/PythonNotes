# -*- coding:utf-8 -*-


# glob
# 查找匹配的文件
# 在查找的条件中，需要用到Unix shell中的匹配规则：
#   *    :   匹配0个或多个字符
#   ?    :   匹配一个字符
#   []   :   匹配指定范围内的字符 如：[0-9]匹配数字。
#   *.*  :   匹配如：[hello.txt,cat.xls,xxx234s.doc]
#   ?.*  :   匹配如：[1.txt,h.py]
#   ?.gif:   匹配如：[x.gif,2.gif]
import glob

print glob.glob(r'*.txt')               # 当前位置
print glob.glob(r'../*.md')             # 相对位置 上级目录
print glob.glob(r'C:\Python27\*.*')     # 绝对位置
