#!/usr/bin/env python
# -*- coding:utf-8 -*-

import functools


def log(text):
    if callable(text):
        @functools.wraps(text)      # text 作为函数名
        def wrapper(*args, **kw):
            print 'Begin call:' + text.__name__
            text(*args, **kw)
            print 'End call:' + text.__name__
        return wrapper
    else:
        def decorator(func):        # text作为字符
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print 'Begin call:' + text + func.__name__
                func(*args, **kw)
                print 'End call:' + text + func.__name__
            return wrapper
        return decorator


@log
def f1():
    print 'f1 is running.'


@log('horton\'s ')
def f2():
    print 'f2 is running.'

f1()
f2()
