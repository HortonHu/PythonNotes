# -*- coding:utf-8 -*-


# __iter__
# 使对象可迭代，同时该对象应该有next方法
# 直到遇到StopIteration错误时退出循环。
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1       # 初始化两个计数器a，b

    def __iter__(self):
        return self                 # 实例本身就是迭代对象，故返回自己

    def next(self):
        self.a, self.b = self.b, self.a + self.b    # 计算下一个值
        if self.a > 100000:          # 退出循环的条件
            raise StopIteration()
        return self.a               # 返回下一个值

for n in Fib():
    print
