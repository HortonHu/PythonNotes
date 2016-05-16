# Framework
常见的Python Web框架还有：
Flask
Django：全能型Web框架；
web.py：一个小巧的Web框架；
Bottle：和Flask类似的Web框架；
Tornado：Facebook的开源异步Web框架。


# Model
# MVC：Model-View-Controller，中文名“模型-视图-控制器”
Python处理URL的函数就是C：Controller，Controller负责业务逻辑，比如检查用户名是否存在，取出用户信息等等
包含变量{{ name }}的模板就是V：View，View负责显示逻辑，通过简单地替换一些变量，View最终输出的就是用户看到的HTML。
Model是用来传给View的，这样View在替换变量的时候，就可以从Model中取出相应的数据。
因为Python支持关键字参数，很多Web框架允许传入关键字参数，然后，在框架内部组装出一个dict作为Model。