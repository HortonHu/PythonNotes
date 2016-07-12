# 判断：if、elif
elif是switch的代替
if...else可以组成三元运算符`condition_is_true if condition else condition_is_false`
一个晦涩的用法使用了元组、序列`(if_test_is_false, if_test_is_true)[test]`
为在Python中，True等于1，而False等于0，这就相当于在元组中使用0和1来选取数据。
另外一个不使用元组条件表达式的缘故是因为在元组中会把两个条件都执行
`print((1/0, 2)[condition])`就会抛出异常，因为在元组中是先建数据，然后用True(1)/False(0)来索引到数据


# 循环: for x in y \ while
- continue  进入下一次循环
- break     跳出当前循环
- 循环后可以跟一个else 当循环中没有break发生的时候执行

不伦是if还是while，被判断的部分可以包含任何操作，不仅仅是比较 例如in/not in/is/is not/
**优先级**：布尔操作or and not < 比较符号 < 运算符号
在布尔符号中 or < and < not 因此有`A and not B or C` 相当于 `(A and (not B)) or C`