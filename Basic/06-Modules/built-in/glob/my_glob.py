# -*- coding:utf-8 -*-


# glob
# 查找匹配的文件
# 在查找的条件中，需要用到Unix shell中的匹配规则：
#   *    :   匹配所所有
#   ?    :   匹配一个字符
#   []   :   匹配指定范围内的字符 如：[0-9]匹配数字。
#   *.*  :   匹配如：[hello.txt,cat.xls,xxx234s.doc]
#   ?.*  :   匹配如：[1.txt,h.py]
#   ?.gif:   匹配如：[x.gif,2.gif]
import glob
all_txt_filename = glob.glob('c:\\users\\dell\\????.txt')
print all_txt_filename
