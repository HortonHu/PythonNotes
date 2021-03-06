### 包结构
包package --> 模块module
每个包必须有__init__.py 否则当做普通目录
__init__.py可以是空文件，也可以有Python代码，本身就是一个模块


模块的导入
从模块中直接导入

    from Test_fibo import fib, fib2
    fib(500)

除了'_'开头的均导入

    from Test_fibo import *
    fib(500)
模块在导入时应该遵循以下规范
1.import 的次序：先 import Python 内置模块，再 import 第三方模块，最后 import 自己开发的项目中的其它模块；
    这几种模块中用空行分隔开来。
2.一条 import 语句 import 一个模块。
3.不要使用 from module import *，除非是 import 常量定义模块或其它你确保不会出现命名空间冲突的模块


模块搜索路径
Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中
添加自己的搜索目录，有两种方法：
一是直接修改sys.path，添加要搜索的目录： sys.path.append('')  运行结束后失效。
二是设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中。
设置方式与设置Path环境变量类似。注意只需要添加你自己的搜索路径，Python自己本身的搜索路径不受影响。

    import sys
    print sys.path

使用模块
sys.argv用list存储了命令行的所有参数 argv至少有一个元素，因为第一个参数永远是该.py文件的名称
运行python hello.py获得的sys.argv就是['server.py']；
运行python server.py Michael获得的sys.argv就是['server.py', 'Michael]。

别名
Python标准库一般会提供StringIO和cStringIO两个库，这两个库的接口和功能是一样的，但是cStringIO是C写的，速度更快

    try:
        import cStringIO as StringIO
    except ImportError:     # 导入失败会捕获到ImportError
        import StringIO


作用域
在一个模块中，但有的函数和变量我们希望给别人使用，有的函数和变量我们希望仅仅在模块内部使用。
在Python中，是通过_前缀来实现的。
类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，我们自己的变量一般不要用这种变量名；
似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；
之所以我们说，private函数和变量“不应该”被直接引用，而不是“不能”被直接引用，
因为Python并没有一种方法可以完全限制访问private函数或变量，但是，从编程习惯上不应该引用private函数或变量。

    def _private_1(name):
        return 'Hello, %s' % name
    
    
    def _private_2(name):
        return 'Hi, %s' % name


    def greeting(name):
        if len(name) > 3:
            return _private_1(name)
        else:
            return _private_2(name)
        pass
在模块里公开greeting()函数，而把内部逻辑用private函数隐藏起来了，
这样，调用greeting()函数不用关心内部的private函数细节，这也是一种非常有用的代码封装和抽象的方法，即：
外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。


__future__
使用__future__ 必须放在文件头 使整个文件使用新版本特性
例如通过unicode_literals来使用Python 3.x的新的语法

    from __future__ import unicode_literals
    print '\'xxx\' is unicode?', isinstance('xxx', unicode)
    print 'u\'xxx\' is unicode?', isinstance(u'xxx', unicode)
    print '\'xxx\' is str?', isinstance('xxx', str)
    print 'b\'xxx\' is str?', isinstance(b'xxx', str)

Python 2.x中，对于除法有两种情况，如果是整数相除，结果仍是整数，余数会被扔掉，这种除法叫“地板除”
在Python 3.x中，所有的除法都是精确除法，地板除用//表示：

    from __future__ import division
    print '10 / 3 =', 10 / 3
    print '10.0 / 3 =', 10.0 / 3
    print '10 // 3 =', 10 // 3

编译python文件
运行时候会尝试编译为pyc文件，如果已经存在pyc文件并且和py文件符合，就不会再编译py文件
使用-o选项可以生成pyo文件，去掉了所有assert语句，pyc文件被忽略，py被编译成pyo
使用-oo选项会去掉所有__doc__ string，生成pyo文件
不伦是pyc还是pyo都不会让程序运行加快，只是省去了编译的时间
