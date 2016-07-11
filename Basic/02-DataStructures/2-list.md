例子：
    
    classmates = ['Michael', 'Bob', 'Tracy']
    print 'length of List:', len(classmates)
    classmates.append('Adam')   	# 末尾插入
    classmates.insert(1, 'Jack')    # 指定位置插入
    classmates.pop()                # 删除末尾元素
    classmates.pop(1)               # 删除指定元素
    classmates[1] = 'Sarah'         # 直接替换指定位置元素
    s = ['python', 'java', ['asp', 'php'], 'scheme']    # list可嵌套
    print list('abc')               # 得到一个list['a', 'b', 'c']

- list中item的type没有限制
- 遍历list的时候如果想要修改，可以用`list[:]`复制一个相同的list来遍历

切片 Slice

    s = 'hello world!'
    print s[0:3]
    print s[-2:]
    print s[::2]
    
列表生成式 List Comprehensions
组成结构`[表达式 0个或者更多的for和if]`

    print [x * x for x in range(1, 11)]
    print [x * x for x in range(1, 11) if x % 2 == 0]   # 筛选出仅偶数的平方
    print [m + n for m in 'ABC' for n in 'XYZ']         # 使用两层循环，可以生成全排列
    print [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]

    d = {'x': 'A', 'y': 'B', 'z': 'C'}
    print [k + '=' + v for k, v in d.iteritems()]       # 同时迭代k,v
    L = ['Hello', 'World', 'IBM', 'Apple']
    print [s.lower() for s in L]  # 改为小写
    L = ['Hello', 'World', 18, 'Apple', None]
    print [s.lower() if isinstance(s, str) else s for s in L]      # 引入判断 变成条件表达式
    vec = [[1,2,3], [4,5,6], [7,8,9]]
    print [num for elem in vec for num in elem]


嵌套列表生成式

    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]

    print [[row[i] for row in matrix] for i in range(4)]
    # 也可以用zip()
    print zip(*matrix)

del语句
和remove方法的区别是del可以删除片段或者整个list