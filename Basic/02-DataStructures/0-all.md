| Type | string | list | tuple | dict | set |
|:---:|:------:|:---:|:-----:|:---:|:--:|
| example|'abc'|[1, 2] ['1', '2'] [1, '2']|('a', 'b', 'c')|{key: value}|{key}|
|mutable|False|True|False|<br>key:False</br><br>整体:True</br>|True|
|+ \* 顺序 切片 嵌套|True|True|True|False|False|
|迭代|True|True|True|True|True|
|methods|split join|append extend insert remove pop index count sort reverse |pass|pass|pass|

对于不变对象如`string`来说，调用对象自身的任意方法，也不会改变该对象自身的内容  
相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。

    a = ['c', 'b', 'a']
    a.sort()
    print 'a =', a
    a = 'abc'
    b = a.replace('a', 'A')
    print b
    print a


对象变动(Mutation)
将一个变量赋值为另一个可变类型的变量时，对这个数据的任意改动会同时反映到这两个变量上去。
新变量只不过是老变量的一个别名而已。

    a = 1
    def fun(a):
        a = 2
    fun(a)
    print a  # 1

    a = []
    def fun(a):
        a.append(1)
    fun(a)
    print a  # [1]
所有的变量都可以理解是内存中一个对象的“引用”,当一个引用传递给函数的时候,函数自动复制一份引用,
这个函数里的引用和外边的引用没有关系了.所以第一个例子里函数把引用指向了一个不可变对象,
当函数返回的时候,外面的引用没半毛感觉.
而第二个例子就不一样了,函数内的引用指向的是可变对象,对它的操作就和定位了指针地址一样,在内存里进行修改.