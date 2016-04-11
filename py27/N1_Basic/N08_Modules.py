#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 包package --> 模块module
# 每个包必须有__init__.py 否则当做普通目录
# __init__.py可以是空文件，也可以有Python代码，本身就是一个模块

import Test_fibo
Test_fibo.fib(1000)

# imports names from a module directly into the importing module’s symbol table
from Test_fibo import fib, fib2
fib(500)

# There is even a variant to import all names that a module defines:
# This imports all names except those beginning with an underscore (_).
from Test_fibo import *
fib(500)

# 系统路径
import sys
print sys.path

# 使用模块





