# -*- coding:utf-8 -*-


# metaclass 元类
# 先定义metaclass，就可以创建类，最后创建实例
# metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。


# metaclass是创建类，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)   # 给MyList增加一个add方法
        return type.__new__(cls, name, bases, attrs)


class MyList(list):
    __metaclass__ = ListMetaclass # 指示使用ListMetaclass来定制类
# 按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass：
# 写下__metaclass__ = ListMetaclass语句时，它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建
# __new__()方法接收到的参数依次是：
# 1.当前准备创建的类的对象；
# 2.类的名字；
# 3.类继承的父类集合；
# 4.类的方法集合。

# 测试一下MyList是否可以调用add()方法：
L = MyList()
L.add(1)
print L
# 普通的list没有add()方法：
l = list()
print l.add(1)
