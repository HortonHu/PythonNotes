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


set与frozenset
set有两种类型，set和frozenset
set是可变的，有add（），remove（）等方法。既然是可变的，所以它不存在哈希值。
frozenset是冻结的集合，它是不可变的，存在哈希值，好处是它可以作为字典的key，也可以作为其它集合的元素。
缺点是一旦创建便不能更改，没有add，remove方法。

    fza=frozenset('a')
    adict={fza:1,'b':2} #正确
    setb=set('a')
    bdict={setb:1,'b':2} #错误

不管是set还是frozenset，Python都不支持只创建一个整数的集合。

    seta=set(1) #错误
    setb=set（'1'）#正确

集合生成式（set comprehensions）
跟列表推导式也是类似的。 唯一的区别在于它们使用大括号{}
`{x**2 for x in [1, 1, 2]}`