# -*- coding:utf-8 -*-

# abs(x)

# all(iterable)
# Return True if all elements of the iterable are true (or if the iterable is empty). Equivalent to:
# def all(iterable):
#     for element in iterable:
#         if not element:
#             return False
#     return True


# any(iterable)
# Return True if any element of the iterable is true. If the iterable is empty, return False. Equivalent to:
# def any(iterable):
#     for element in iterable:
#         if element:
#             return True
#     return False

# basestring()
# This abstract type is the superclass for str and unicode.
# It cannot be called or instantiated, but it can be used to test whether an object is an instance of str or unicode.
# isinstance(obj, basestring) is equivalent to isinstance(obj, (str, unicode)).

# bin(x)
# Convert an integer number to a binary string.
# The result is a valid Python expression.
# If x is not a Python int object, it has to define an __index__() method that returns an integer.

# class bool([x])
# Return a Boolean value, i.e. one of True or False. x is converted using the standard truth testing procedure.
# If x is false or omitted, this returns False; otherwise it returns True.
# bool is also a class, which is a subclass of int. Class bool cannot be subclassed further.
# Its only instances are False and True.

# class bytearray([source[, encoding[, errors]]])


# callable(object)
# 判断callable 能返回True 不能返回False
# 即使返回True 也可能无法调用 但是只要返回False就肯定无法调用
# class是可调用的 返回实例instance
# instance是否可调用要看有没有__call__()方法

# chr(i)
# 返回整数i对应的ASCII码 i属于[0...255]
# chr(97) returns the string 'a'

# classmethod(function)


# cmp(x, y)
#  The return value is negative if x < y, zero if x == y and strictly positive if x > y.

# compile(source, filename, mode[, flags[, dont_inherit]])


# class complex([real[, imag]])
# Return a complex number with the value real + imag*1j or convert a string or number to a complex number.
# If the first parameter is a string, it will be interpreted as a complex number
# and the function must be called without a second parameter.
# complex(1,2)
# complex('1+2j')

# delattr(object, name)


# class dict(**kwarg)
# class dict(mapping, **kwarg)
# class dict(iterable, **kwarg)


# dir([object])


# divmod(a, b)


# enumerate(sequence, start=0)
# Equivalent to:
# def enumerate(sequence, start=0):
#     n = start
#     for elem in sequence:
#         yield n, elem
#         n += 1


# eval(expression[, globals[, locals]])


# execfile(filename[, globals[, locals]])


# file(name[, mode[, buffering]])


# filter(function, iterable)


# class float([x])


# format(value[, format_spec])


# class frozenset([iterable])


# getattr(object, name[, default])


# globals()


# hasattr(object, name)


# hash(object)


# help([object])


# hex(x)
















