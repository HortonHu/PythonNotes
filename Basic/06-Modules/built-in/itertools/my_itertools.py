# -*- coding:utf-8 -*-

import itertools

# itertools包中的itertools.chain.from_iterable轻松快速的辗平一个列表
a_list = [[1, 2], [3, 4], [5, 6]]
print(list(itertools.chain.from_iterable(a_list)))
print(list(itertools.chain(*a_list)))   # 另一种写法