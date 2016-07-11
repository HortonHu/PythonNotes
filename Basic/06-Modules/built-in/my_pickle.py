# -*- coding:utf-8 -*-


# 序列化
# 把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling
# 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。

# Python提供两个模块来实现序列化：cPickle和pickle
# cPickle是C语言写的，速度快，pickle是纯Python写的，速度慢
# 用的时候，先尝试导入cPickle，如果失败，再导入pickle
try:
    import cPickle as pickle
except ImportError:
    import pickle

# 序列化
d = dict(name='Bob', age=20, score=88)
pickle.dumps(d)     # dumps把任意对象序列化成一个str，然后，就可以把这个str写入文件
# 或者用另一个方法pickle.dump()直接把对象序列化后写入一个file
with open('dump.txt', 'wb') as f:
    pickle.dump(d, f)           # 将d给pickle之后写入文件f

# 反序列化
# 把对象从磁盘读到内存时，可以先把内容读到一个str 然后用pickle.loads()方法反序列化出对象
with open('dump.txt', 'rb') as f:
    pickle_str = f.read()
    d = pickle.loads(pickle_str)
    print d
# 也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象
# 反序列化刚才保存的对象：
with open('dump.txt', 'rb') as f:
    d = pickle.load(f)          # 从文件f中反序列化给d
    print d

# 这个变量和原来的变量是完全不相干的对象，它们只是内容相同而已。
# Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，并且可能不同版本的Python彼此都不兼容，
# 因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。