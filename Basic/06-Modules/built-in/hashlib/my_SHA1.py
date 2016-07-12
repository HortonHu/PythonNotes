# -*- coding:utf-8 -*-


# SHA1
# 另一种常见的摘要算法是SHA1，调用SHA1和调用MD5完全类似：
# SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示
import hashlib

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in ')
sha1.update('python hashlib?')
print sha1.hexdigest()