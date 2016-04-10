#!/usr/bin/env python
# -*- coding:utf-8 -*-


def not_su(n):
    for i in range(2, n/2):         # 判断只需要用一半的数
        if n % i == 0:
            return False
    else:
        return  True

l = range(1, 101)
print filter(not_su, l)
