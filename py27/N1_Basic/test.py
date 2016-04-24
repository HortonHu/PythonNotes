#!/usr/bin/env python
# -*- coding: utf-8 -*-

a = 0
n = 10
while n > 0:
    a += n
    n -= 1
    if n == 9:
        continue

else:
    a = 1000

print a
