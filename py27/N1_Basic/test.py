#!/usr/bin/env python
# -*- coding:utf-8 -*-

x = ('a','b','c','d')
y = {'a':1,'b':2,'c':3}


def func(a, b, c=0, *args, **kw):
    print a
    print b
    print c
    print args
    print kw

func(1, 2, 3, x, *y)
