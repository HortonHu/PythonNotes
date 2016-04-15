#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 正则表达式
# 正则表达式是一种用来匹配字符串的强有力的武器。它的设计思想是用一种描述性的语言来给字符串定义一个规则，
# 凡是符合规则的字符串，我们就认为它“匹配”了，否则，该字符串就是不合法的。


# 用正则表达式匹配网页中的中文内容
# Python 2.x版本，需要用unicode来匹配。正则表达式的字符串前要加上u，待匹配的文本要decode()。例如：
import re
text = "你好吗？我很好！"
m = re.findall(ur"你好", text.decode("utf8"))
if m:
    print m[0].encode('utf8')
else:
    print 'not match'




