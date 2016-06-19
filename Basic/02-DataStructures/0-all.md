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


