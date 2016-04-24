#!/usr/bin/env python
# -*- coding: utf-8 -*-


def f(s1, s2):
    if s1 > s2:
        return True
    else:
        return False

print map(f, [1, 2, 3, 4, 5], [10, 6, 7, 8, 9])
