#!/usr/bin/env python
# -*- coding:utf-8 -*-


def odd():
    print 'step 1'
    yield 1
    print 'step 2'
    yield 2
    print 'step 3'
    yield 3

if __name__ == '__main__':
    o = odd()
    while True:
        try:
            print o.next()
        except:
            break
