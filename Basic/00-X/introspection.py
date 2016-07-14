# -*- coding:utf-8 -*-


# type() 获取对象信息
import types
print type('abc') == types.StringType
print type(u'abc') == types.UnicodeType
print type([])==types.ListType
print type(str)==types.TypeType
print type(int)==type(str)==types.TypeType      # 所有类型本身的类型就是TypeType


# 配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
class MyObject(object):
        def __init__(self):
            self.x = 9

        def power(self):
            return self.x * self.x

obj = MyObject()
hasattr(obj, 'x')           # 有属性'x'吗？
obj.x
hasattr(obj, 'y')           # 有属性'y'吗？
setattr(obj, 'y', 19)       # 设置一个属性'y'为19
hasattr(obj, 'y')           # 有属性'y'吗？
getattr(obj, 'y')           # 获取属性'y'
hasattr(obj, 'power')       # 有方法'power'吗？
getattr(obj, 'power')       # 获取方法'power'
fn = getattr(obj, 'power')  # 获取方法'power'并赋值到变量fn
fn
fn()
obj.y                   # 获取属性'y'
# 可以传入一个default参数，如果属性不存在，就返回默认值
getattr(obj, 'z', 404)  # 获取属性'z'，如果不存在，返回默认值404


# 只有在不知道对象信息的时候，我们才会去获取对象信息。
# 如果可以直接写： sum = obj.x + obj.y 就不要写 sum = getattr(obj, 'x') + getattr(obj, 'y')
# 假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，
# 如果存在，则该对象是一个流，如果不存在，则无法读取。hasattr()就派上了用场。
def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None
