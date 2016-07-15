# -*- coding:utf-8 -*-


# dict的子类如果定义了方法__missing__(self, key)
# 如果key不再dict中，那么d[key]就会调用__missing__方法
# 而且d[key]的返回值就是__missing__的返回值
class MyDict(dict):
    def __missing__(self, key):
        self[key] = rv = []
        return rv

m = MyDict()
m["foo"].append(1)
m["foo"].append(2)
print dict(m)


# 在collections模块下有一个叫defaultdict的dict子类
# 它与missing非常类似，但是对于不存在的项不需要传递参数。
from collections import defaultdict
m = defaultdict(list)
m["foo"].append(1)
m["foo"].append(2)
print dict(m)
