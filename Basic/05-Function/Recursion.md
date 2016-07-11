# 递归函数
注意：次数太多会造成栈溢出 该次数可设置 最大1000

    def fact(n):
        if n == 1:
            return 1
        return n * fact(n - 1)
    print fact(5)


改用尾递归方式
尾递归调用时，如果做了优化,只占用一个栈帧多少次调用也不会导致栈溢出。
但是Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。

    def fact(n):
        return fact_iter(n, 1)

    def fact_iter(num, product):
        if num == 1:
            return product
        return fact_iter(num - 1, num * product)        
    print fact(5)
    # num - 1和num * product在函数调用前就会被计算，不影响函数调用。
