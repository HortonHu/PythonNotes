# -*- coding:utf-8 -*-


# struct
# Python没有专门处理字节的数据类型。但由于str既是字符串，又可以表示字节，
# 所以，字节数组＝str。而在C语言中，我们可以很方便地用struct、union来处理字节，以及字节和int，float的转换
# 在Python中，比方说要把一个32位无符号整数变成字节，也就是4个长度的str，你得配合位运算符这么写
n = 10240099
b1 = chr((n & 0xff000000) >> 24)
b2 = chr((n & 0xff0000) >> 16)
b3 = chr((n & 0xff00) >> 8)
b4 = chr(n & 0xff)
s = b1 + b2 + b3 + b4
print s


# Python提供了一个struct模块来解决str和其他二进制数据类型的转换
# struct的pack函数把任意数据类型变成字符串
import struct
print struct.pack('>I', 10240099)
# pack的第一个参数是处理指令，'>I'的意思是：>表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
# 后面的参数个数要和处理指令一致。

# unpack把str变成相应的数据类型
print struct.unpack('>IH', '\xf0\xf0\xf0\xf0\x80\x80')
# 根据>IH的说明，后面的str依次变为I：4字节无符号整数和H：2字节无符号整数
# 尽管Python不适合编写底层操作字节流的代码，但在对性能要求不高的地方，利用struct就方便多了
