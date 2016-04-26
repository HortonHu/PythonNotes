#!/usr/bin/env python
# -*- coding: utf-8 -*-


class A(object):
    __slots__ = ('name', 'age')
    pass


class B(A):
    __slots__ = ('score')
    pass

c = B()
c.name = 1
c.age = 2
c.score = 3
c.data = 4