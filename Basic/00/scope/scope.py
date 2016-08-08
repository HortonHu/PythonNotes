# -*- coding:utf-8 -*-


# 作用域 scope
# Python 中，一个变量的作用域总是由在代码中被赋值的地方所决定的。
# 当 Python 遇到一个变量的话他会按照LEGB的顺序进行搜索：
# 本地作用域（Local）→当前作用域被嵌入的本地作用域（Enclosing locals）→全局/模块作用域（Global）→内置作用域（Built-in）
x = 10
def foo():
    x += 1
    return x

print foo()
# 此时会引发错误UnboundLocalError
# 因为在某个scope内为变量赋值的时候，该变量会被视为该scope的本地变量，并且会取代上一层scope中相同名字的变量


# 使用列表的时候更容易犯错
lst = [1, 2, 3]
def foo1():
    lst.append(4)

foo1()
print lst

def foo2():
    lst += 5

foo2()
print lst
# 在foo1中没有对lst赋值，而foo2中有赋值操作 此时lst还没有定义