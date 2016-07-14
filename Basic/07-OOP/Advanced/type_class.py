# -*- coding:utf-8 -*-


# type()
# 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。
# A是一个class 它的type就是type
# a是一个实例  它的type是class A
class A(object):
    pass

a = A()
print type(A)
print type(a)
# class的定义是运行时动态创建的，而创建class的方法就是使用type()函数


# type()函数既可以返回一个对象的类型，又可以创建出新的类型
# 可以通过type()函数创建出Hello类，而无需通过class Hello(object)的定义：
def fn(self, name='world'):     # 先定义函数
    print('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello=fn))    # 创建Hello class
h = Hello()
h.hello()
print type(Hello)
print type(h)
# 要创建一个class对象，type()函数依次传入3个参数：
# 1.class的名称；
# 2.继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# 3.class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
# 通过type()函数创建的类和直接写class是完全一样的，
# 因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。
# 正常情况下，我们都用class Xxx...来定义类，但是，type()函数也允许我们动态创建出类来，
# 也就是说，动态语言本身支持运行期动态创建类

