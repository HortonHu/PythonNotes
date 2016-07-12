# -*- coding:utf-8 -*-


# 由于常用口令的MD5值很容易被计算出来，所以，要确保存储的用户口令不是那些已经被计算出来的常用口令的MD5，
# 这一方法通过对原始口令加一个复杂字符串来实现，俗称“加盐”
def calc_md5(password):
    return get_md5(password + 'the-Salt')
# 经过Salt处理的MD5口令，只要Salt不被黑客知道，即使用户输入简单口令，也很难通过MD5反推明文口令。
# 但是如果有两个用户都使用了相同的简单口令比如123456，在数据库中，将存储两条相同的MD5值，这说明这两个用户的口令是一样的。
# 如果假定用户无法修改登录名，就可以通过把登录名作为Salt的一部分来计算MD5，从而实现相同口令的用户也存储不同的MD5。

# 练习
# 根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5：
db = {}


def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')


# 根据修改后的MD5算法实现用户登录的验证
def login(username, password):
    pass
