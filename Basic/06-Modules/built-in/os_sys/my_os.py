# -*- coding:utf-8 -*-


# 操作文件和目录
# Python内置的os模块可以直接调用操作系统提供的接口函数。
import os
print os.name     # 操作系统名字
# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
# 要获取详细的系统信息，可以调用uname()函数 该函数在Windows上不提供

# 环境变量
print os.environ                # 操作系统中定义的环境变量，全部保存在os.environ这个dict中
print os.getenv('PATH')         # 获取某个环境变量的值，可以调用os.getenv()


# os.name字符串指示你正在使用的平台。比如对于Windows，它是'nt'，而对于Linux/Unix用户，它是'posix'。
# os.getcwd()函数得到当前工作目录，即当前Python脚本工作的目录路径。
# os.getenv()和os.putenv()函数分别用来读取和设置环境变量。
# os.listdir()返回指定目录下的所有文件和目录名。
# os.remove()函数用来删除一个文件。
# os.system()函数用来运行shell命令。
# os.linesep字符串给出当前平台使用的行终止符。例如，Windows使用'\r\n'，Linux使用'\n'而Mac使用'\r'。
# os.path.split()函数返回一个路径的目录名和文件名。


# 操作文件和目录
# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块
# 查看、创建和删除目录可以这么调用：
now_path = os.path.abspath('.')         # 查看当前目录的绝对路径:
# 在某个目录下创建一个新目录， 首先把新目录的完整路径表示出来:
# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。
true_path = os.path.join(now_path, 'testdir')
os.mkdir(true_path)         # 然后创建一个目录:
os.rmdir(true_path)         # 删掉一个目录:
# 同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()
# 把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
(a, b) = os.path.split('/Users/michael/testdir/file.txt')    # ('/Users/michael/testdir', 'file.txt')
print a
print b
# os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：
os.path.splitext('/path/to/file.txt')
# 这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。

# 假定当前目录下有一个test.txt文件：
os.rename('test.txt', 'horton.py')      # 对文件重命名:
os.remove('horton.py')                  # 删掉文件:
# 复制文件的函数在os模块中不存在 因为复制文件并非由操作系统提供的系统调用
# shutil模块提供了copyfile()的函数 可以看做是os模块的补充。
print os.getcwd()                       # 获取当前目录
os.chdir( "C:\\123")    # 更改当前目录 将当前目录设为 "C:\123", 相当于DOC命令的 CD C:\123
print [x for x in os.listdir('.') if os.path.isdir(x)]  # 列出当前目录下的所有目录
print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']  # 列出所有的.py文件

# os常用方法
# os.remove()           删除文件
# os.rename()           重命名文件
# os.walk()             生成目录树下的所有文件名
# os.chdir()            改变目录
# os.mkdir/makedirs     创建目录/多层目录
# os.rmdir/removedirs   删除目录/多层目录
# os.listdir()          列出指定目录的文件
# os.getcwd()           取得当前工作目录
# os.chmod()            改变目录权限
# os.path.basename()    去掉目录路径，返回文件名
# os.path.dirname()     去掉文件名，返回目录路径
# os.path.join()        将分离的各部分组合成一个路径名
# os.path.split()       返回（dirname(),basename())元组
# os.path.splitext()    返回(filename,extension)元组
# os.path.getatime\ctime\mtime分别返回最近访问、创建、修改时间
# os.path.getsize()     返回文件大小
# os.path.exists()      是否存在
# os.path.isabs()       是否为绝对路径
# os.path.isdir()       是否为目录
# os.path.isfile()      是否为文件

# 练习：编写一个search(s)的函数，
# 能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出完整路径：
# $ python search.py test
# unit_test.log
# py/test.py
# py/test_os.py
# my/logs/unit-test-result.txt
