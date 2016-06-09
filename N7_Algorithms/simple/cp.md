# 挑战Python题目 http://www.pythontip.com/ 
1. just print a+b
```
print a + b
```

2. 	list排序
```
L=[2,8,3,50]
L.sort()
print L
```

3. 字符串逆序
```
a=‘12345’
print a[::-1]
```

4. 输出字典key
```
a={1:1,2:2,3:3}
print ','.join(map(str,a.keys()))
```

5. 输出字符奇数位置的字符串
```
a=‘12345’
print a[::2]
```

6. 求解100以内的所有素数
```
l = []
for i in range(2, 100):
    for k in range(2, i):
        if i % k == 0:
            break
    else:
        l.append(i)
print ' '.join(map(str, l))
```

7. 求矩形面积
```
print a*b, 2*(a+b)
```

8. 求中位数
```
L.sort()
if len(L) % 2 == 0:
    temp = (L[len(L)/2] + L[len(L)/2-1])/2.0
else:
    temp = L[len(L)/2]
print temp
```

9. 最大公约数
```
def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)
print gcd(a, b)
```

10. 最小公倍数
```
def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)
print a*b/gcd(a, b)
```

11. 结尾0的个数
给你一个正整数列表 L, 如 L=[2,8,3,50], 输出L内所有数字的乘积末尾0的个数,
如样例L的结果为2.(提示:不要直接相乘,数字很多,可能溢出)
```
def countn(x, n):
    num = 0
    while x % n == 0:
        num += 1
        x = x / n
    return num
c2 = sum(map(countn, L, [2]*len(L)))
c5 = sum(map(countn, L, [5]*len(L)))
print min(c2, c5)
```

12. 结尾非零数的奇偶性
给你一个正整数列表 L, 如 L=[2,8,3,50], 判断列表内所有数字乘积的最后一个非零数字的奇偶性,
奇数输出1,偶数输出0. 如样例输出应为0
```
def countn(x, n):
    num = 0
    while x % n == 0:
        num += 1
        x = x / n
    return num
c2 = sum(map(countn, L, [2]*len(L)))
c5 = sum(map(countn, L, [5]*len(L)))
if c2 > c5:
    print 0
else:
    print 1
```

13. 光棍的悲伤
给你一个整数a，数出a在二进制表示下1的个数，并输出。
```
from collections import Counter
c = Counter(bin(a))
print c['1']
```

14. Python之美
输出Python之禅
注意：输出python之禅的源码即可，不用转换为英文。（小小的提示：print this.s)
```
import this
print this.s
```

15. 大小写转换
给定一个字符串a, 将a中的大写字母 转换成小写，其它字符不变，并输出。
```
print a.lower()
```

16. 人民币金额打印
银行在打印票据的时候，常常需要将阿拉伯数字表示的人民币金额转换为大写表示，现在请你来完成这样一个程序。
在中文大写方式中，0到10以及100、1000、10000被依次表示为：零壹贰叁肆伍陆柒捌玖拾佰仟万
以下的例子示范了阿拉伯数字到人民币大写的转换规则：
1	壹圆
11	壹拾壹圆
111	壹佰壹拾壹圆
101	壹佰零壹圆
-1000	负壹仟圆
1234567	壹佰贰拾叁万肆仟伍佰陆拾柒圆
现在给你一个整数a(|a|<100000000), 打印出人民币大写表示.
注意：请以Unicode的形式输出答案。你可以通过decode("utf8")来将utf8格式的字符串解码为Unicode，例如你要输出ans = "零圆", print ans.decode("utf8").
Note：数据已于2013-11-19日加强，原来通过的代码可能不能再次通过。
**尚未完成**
```
a0 = 0
a1 = 1
a2 = 11
a3 = 111
a4 = 101
a5 = -1000
a6 = 1234567
a7 = 12345678
a = [a0, a1, a2, a3, a4, a5, a6, a7]
# 拾佰仟万
bank_key = map(str, range(0, 10))
bank_value = list(u'零壹贰叁肆伍陆柒捌玖')
bank_d = dict(zip(bank_key, bank_value))
```

17. 公约数的个数
给你两个正整数a,b,  输出它们公约数的个数。
```
```

18. 逆解最大公约数与最小公倍数
我们经常遇到的问题是给你两个数，要你求最大公约数和最小公倍数。
今天我们反其道而行之，给你两个数a和b，计算出它们分别是哪两个数的最大公约数和最小公倍数。
输出这两个数，小的在前，大的在后，以空格隔开。若有多组解，输出它们之和最小的那组。
注：所给数据都有解，不用考虑无解的情况。
```
```

19. 单身情歌
给你一个字符串a,如果其中包含"LOVE"（love不区分大小写)则输出LOVE，否则输出SINGLE。
```
```

20. 信息加密
给你个小写英文字符串a和一个非负数b(0<=b<26), 将a中的每个小写字符替换成字母表中比它大b的字母。
这里将字母表的z和a相连，如果超过了z就回到了a。例如a="cagy",b=3, 则输出 fdjb
```
```
