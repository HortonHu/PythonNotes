# -*- coding:utf-8 -*-


# __str__   返回用户看到的字符串
# __repr__  返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__      # 偷懒写法 因为通常__repr__和__str__内容一致

print Student('Horton')
