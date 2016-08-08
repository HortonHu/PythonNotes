解释一下 WSGI 和 FastCGI 的关系？

CGI全称是“公共网关接口”(CommonGateway Interface)，HTTP服务器与你的或其它机器上的程序进行“交谈”的一种工具，其程序须运行在网络服务器上。　
CGI可以用任何一种语言编写，只要这种语言具有标准输入、输出和环境变量。如php,perl,tcl等。
FastCGI像是一个常驻(long-live)型的CGI，它可以一直执行着，只要激活后，不会每次都要花费时间去fork一次(这是CGI最为人诟病的fork-and-execute模式)。
它还支持分布式的运算, 即 FastCGI 程序可以在网站服务器以外的主机上执行并且接受来自其它网站服务器来的请求。
FastCGI是语言无关的、可伸缩架构的CGI开放扩展，其主要行为是将CGI解释器进程保持在内存中并因此获得较高的性能。
众所周知，CGI解释器的反复加载是CGI性能低下的主要原因，如果CGI解释器保持在内存中并接受FastCGI进程管理器调度，则可以提供良好的性能、伸缩性、Fail- Over特性等等。
WSGI的全称为： PythonWeb Server Gateway Interface v1.0 （Python Web 服务器网关接口），

它是 Python 应用程序和 WEB 服务器之间的一种接口。
它的作用，类似于FCGI 或 FASTCGI 之类的协议的作用。
WSGI 的目标，是要建立一个简单的普遍适用的服务器与 WEB 框架之间的接口。
Flup就是使用 Python 语言对 WSGI 的一种实现，是可以用于 Python 的应用开发中的一种工具或者说是一种库。
Spawn-fcgi是一个小程序，这个程序的作用是管理fast-cgi进程，那么管理wsgi进程也是没有问题的，功能和php-fpm类似。
故，简单地说，WSGI和FastCGI都是一种CGI，用于连接WEB服务器与应用程序，而WSGI专指Python应用程序。
而flup是WSGI的一种实现，Spawn-fcgi是用于管理flup进程的一个工具，可以启动多个wsgi进程，并管理它们。