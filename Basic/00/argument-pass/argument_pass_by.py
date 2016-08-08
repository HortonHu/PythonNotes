# -*- coding:utf-8 -*-


# How are arguments passed - by reference of by value?
# The short answer is "neither", actually it is called "call by object” or “call by sharing"
# (you can check here for more info).
# The longer one starts with the fact that this terminology is probably not the best one to describe how Python works.
# In Python everything is an object and all variables hold references to objects.
# The values of these references are to the functions.
# As result you can not change the value of the reference but you can modify the object if it is mutable.
# Remember numbers, strings and tuples are immutable, list and dicts are mutable.

# 1 Python的函数参数传递
# 看两个例子:

a = 1
def fun(a):
    a = 2
print a  # 1
a = []
def fun(a):
    a.append(1)
print a  # [1]
# 所有的变量都可以理解是内存中一个对象的“引用”，或者，也可以看似c中void*的感觉。
# 这里记住的是类型是属于对象的，而不是变量。而对象有两种,“可更改”（mutable）与“不可更改”（immutable）对象。
# 在python中，strings, tuples, 和numbers是不可更改的对象，而list,dict等则是可以修改的对象。(这就是这个问题的重点)
# 当一个引用传递给函数的时候,函数自动复制一份引用,这个函数里的引用和外边的引用没有半毛关系了.
# 所以第一个例子里函数把引用指向了一个不可变对象,当函数返回的时候,外面的引用没半毛感觉.
# 而第二个例子就不一样了,函数内的引用指向的是可变对象,对它的操作就和定位了指针地址一样,在内存里进行修改.
# 如果还不明白的话,这里有更好的解释: http://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference
