例子：

 	{key: value}

dict具有极快的查找速度
list比较，dict有以下几个特点：
1.查找和插入的速度极快，不会随着key的增加而增加
2.需要占用大量的内存，内存浪费多
dict是用空间来换取时间的一种方法。

    d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
    print 'dict:', d
    print d['Bob']
    d['Adam'] = 67   # 通过key放入value值进入dict，同一个key放入多个value后面的会抵消前面的
    print 'dict:', d
要避免key不存在的错误，有两种办法：
一是通过in判断key是否存在：

    print 'Thomas' in d
二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value：

    print d.get('Thomas')
    print d.get('Thomas', -1)
    d.pop('Bob')    # 删除key 对应的value也会删除

使用zip来生产dict  `d = dict(zip(keys, values))`

    keys = ['Safe', 'Bob', 'Thomas']
    values = ['Hammad', 'Builder', 'Engine']
    d = dict(zip(keys, values))
    print d


迭代 Iteration
默认情况下，dict迭代的是key。
如果要迭代value，可以用for value in d.itervalues()
同时迭代key和value，可以用for k, v in d.iteritems()

    d = {'a': 1, 'b': 2, 'c': 3}
    for key in d.keys():            # 最好用d.keys()这个下标数组 防止出错 或者用d.iterkeys()
        print key
    # 迭代value
    for value in d.itervalues():  
        print value
    # 同时迭代key和value
    for k, v in d.iteritems():  
        print k, 'is the key of', v

通过collections模块的Iterable类型判断是否可迭代

    from collections import Iterable
    
    print isinstance('abc', Iterable)
    print isinstance([1, 2, 3], Iterable)
    print isinstance(123, Iterable)

enumerate函数可以把一个list变成索引-元素对
同时迭代index和元素本身

    for i, value in enumerate(['A', 'B', 'C']):
        print i, value

用zip压缩的方式来迭代
    
    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']
    for q, a in zip(questions, answers):
        print 'What is your {0}?  It is {1}.'.format(q, a)

字典生成式（dict comprehensions）
字典推导和列表推导的使用方法是类似的

    {x: x**2 for x in (2, 4, 6)}

    # 把同一个字母但不同大小写的值合并起来
    mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
    mcase_frequency = {
        k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)
        for k in mcase.keys()
    }

对换一个字典的键和值`{v: k for k, v in some_dict.items()}`
