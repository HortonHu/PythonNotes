Data type: List ['a', 'b', 'c'] or [1, 2, 3] or [1, 2, 'a', 'b']
----------------------------------------------------------------
不用的item的type可以不同
遍历list的时候如果想要修改，可以用list[:]复制一个相同的list来遍历  
    
    classmates = ['Michael', 'Bob', 'Tracy']
    print 'List:', classmates
    print 'length of List:', len(classmates)
    classmates.append('Adam')   	# 末尾插入
    print 'List:', classmates
    classmates.insert(1, 'Jack')    # 指定位置插入
    print 'List:', classmates
    classmates.pop()    # 删除末尾元素
    print 'List:', classmates
    classmates.pop(1)   # 删除指定元素
    print 'List:', classmates
    classmates[1] = 'Sarah'     # 直接替换指定位置元素
    print 'List:', classmates
    s = ['python', 'java', ['asp', 'php'], 'scheme']    # list可嵌套
    print list('abc')       # 得到一个list['a', 'b', 'c']

用collections.deque构造双端队列来快速的从任意方向pop或append

    from collections import deque
    queue = deque(["Eric", "John", "Michael"])
    queue.append("Terry")           # Terry arrives
    queue.append("Graham")          # Graham arrives
    queue.popleft()                 # The first to arrive now leaves
    queue.popleft()                 # The second to arrive now leaves
    print queue