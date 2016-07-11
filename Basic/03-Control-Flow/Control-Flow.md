# 判断：if、elif
elif是switch的代替

# 循环: for x in y \ while
- continue  进入下一次循环
- break     跳出当前循环
- 循环后可以跟一个else 当循环中没有break发生的时候执行

不伦是if还是while，被判断的部分可以包含任何操作，不仅仅是比较 例如in/not in/is/is not/
**优先级**：布尔操作or and not < 比较符号 < 运算符号
在布尔符号中 or < and < not 因此有`A and not B or C` 相当于 `(A and (not B)) or C`