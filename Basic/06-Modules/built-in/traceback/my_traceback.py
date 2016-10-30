# -*- coding:utf-8 -*-
import traceback


def zerodiv():
    return 10/0


try:
    # zerodiv()
    raise Exception("qwe")
except Exception ,e:
    print e
    traceback.print_exc()

print 123