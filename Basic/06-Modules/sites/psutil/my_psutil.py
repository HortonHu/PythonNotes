# -*- coding:utf-8 -*-

import psutil

# 获得所有进程列表
psutil.pids()

# 获得一个对象
p = psutil.Process(3215)
# 进程名
p.name()
# 进程pid
print p.pid
# 父进程pid
print p.ppid
# 进程可执行程序名
p.exe()
# 当前目录
p.cwd()
# 进程用户名
p.username()
# 进程状态
p.status()
# 进程创造时间
p.create_time()
# 进程uid
p.uids()
# 进程CPU时间
p.cpu_times()
# 进程内存占用百分比
p.memory_percent()
# 进程内存使用信息
p.memory_info()
# 进程线程数
p.num_threads()
# 进程连接情况
p.connections()
