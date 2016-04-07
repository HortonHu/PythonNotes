#!/usr/bin/env python
# -*- coding:utf-8 -*-
import Test_fibo
Test_fibo.fib(1000)

# imports names from a module directly into the importing module’s symbol table
from Test_fibo import fib, fib2
fib(500)

# There is even a variant to import all names that a module defines:
# This imports all names except those beginning with an underscore (_).
from Test_fibo import *
fib(500)

# The Module Search Path
import sys
print sys.path



