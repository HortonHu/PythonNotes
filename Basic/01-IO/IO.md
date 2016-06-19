## IO
- raw_input()   返回 string  
- input()       返回 value  
```
    name = raw_input('Please input your name：')
    print 'Hi', name
    age = input('Please input your age：')
    print 'the type of age is ', type(age)
```

## 格式化
1. 旧式：
```
    %d  整数
    %f  浮点数
    %s  字符串
    %x  十六进制整数
    %r  变量,获取某些东西的 debug 信息
```
其中%s永远起作用，它会把任何数据类型转换为字符串  
格式化整数和浮点数还可以指定是否补0和整数与小数的位数  
字符串里面的%是一个普通字符时候需要转义: %%  
```
    print 'My age is %d' % 22
    print 'Price is %.4f' % 4.99
    print 'Today is %s.' % 'Friday'
    print "%s's score is %d" % ('Mike', 87)
    print 'growth rate: %d %%' % 7
```
2. 新式：  
从2.6以后开始引入format()进行格式化 操作更方便  
大括号和其中的字符会被替换成传入 str.format() 的参数。大括号中的数值指明使用传入 str.format() 方法的对象中的对应的一个  
```
    print 'We are the {} who say "{}!"'.format('knights', 'Ni')
    print '{0} and {1}'.format('spam', 'eggs')
    print '{1} and {0}'.format('spam', 'eggs')
```
如果在 str.format() 调用时使用关键字参数，可以通过参数名来引用值:
```
    print 'This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible')
```
定位和关键字参数可以组合使用
```
    print 'The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg')
```
'!s' (应用 str() )和 '!r' (应用 repr())可以在格式化之前转换值:
```
    import math
    print 'The value of PI is approximately {}.'.format(math.pi)
    print 'The value of PI is approximately {!r}.'.format(math.pi)
```
字段名后允许可选的 ':' 和格式指令。这允许对值的格式化加以更深入的控制。
```
    print('The value of PI is approximately {0:.3f}.'.format(math.pi))
```
在字段后的 ':' 后面加一个整数会限定该字段的最小宽度，这在美化表格时很有用:
```
    table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
    for name, phone in table.items():
        print '{0:10} ==> {1:10d}'.format(name, phone)
```
传入一个字典，用中括号( '[]' )访问它的键
```
    table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
    print 'Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table)
```
用 `**` 标志将这个字典以关键字参数的方式传入
```
    table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
    print 'Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table)
```


