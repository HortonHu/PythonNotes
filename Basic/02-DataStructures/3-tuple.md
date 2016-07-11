例子：

    ('a', 'b', 'c')

1. Tuple和list非常类似，但是tuple一旦初始化就不能修改，更安全
2. tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。如果元素是可变的 则该元素可变 相当于tuple的内容还是改变了


    classmates = ('Michael', 'Bob', 'Tracy')
    print classmates[0], classmates[1]
    t = (1)                 # 特例，按照数学运算定义
    tt = (1,)               # 用,来消除歧义 因此tt是tuple
    print type(t), type(tt)
