# -*- coding:utf-8 -*-


# Python/C API可能是被最广泛使用的方法。它不仅简单，而且可以在C代码中操作你的Python对象。
# 这种方法需要以特定的方式来编写C代码以供Python去调用它。
# 所有的Python对象都被表示为一种叫做PyObject的结构体，并且Python.h头文件中提供了各种操作它的函数。
# 例如，如果PyObject表示为PyListType(列表类型)时，那么我们便可以使用PyList_Size()函数来获取该结构的长度，
# 类似Python中的len(list)函数。大部分对Python原生对象的基础函数和操作在Python.h头文件中都能找到。


