Data type: dict 	{key: value}
-----------------------------
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
使用zip来生产dict  d = dict(zip(keys, values))

    keys = ['Safe', 'Bob', 'Thomas']
    values = ['Hammad', 'Builder', 'Engine']
    d = dict(zip(keys, values))
    print d
