Data type: set{key}
-------------------
set和dict类似，也是一组key的集合，但不存储value, key不能重复
常用来清理重复元素

    s = set([1, 2, 3]) 也可以这样定义
    s = {'1', '2', '3'}
    print 'set:', s
    s = {'1', '2', '1', '1', '2', '3', '3'}
    print 'set:', s
    s.add(4)            # 添加key
    print 'set:', s
    s.add(4)            # 重复添加无效
    print 'set:', s
    s.remove(4)         # 删除key
    print 'set:', s
set可以看成数学意义上的无序和无重复元素的集合
因此，两个set可以做数学意义上的相减、交集、并集等操作

    s1 = {'1', '2', '3'}
    s2 = {'2', '3', '4'}
    print 'set:', s1 & s2
    print 'set:', s1 | s2
