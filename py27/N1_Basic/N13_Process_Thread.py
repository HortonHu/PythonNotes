#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 一个任务就是一个进程（Process） 进程内的这些“子任务”称为线程（Thread）
# 多任务的实现有3种方式：
# 多进程模式；
# 多线程模式；
# 多进程+多线程模式。


# 多进程 multiprocessing
# Python的os模块封装了常见的系统调用，其中就包括fork，可以在Python程序中轻松创建子进程：
# Windows没有fork调用 这个例子只能用在linux下
# 子进程永远返回0，而父进程返回子进程的ID
# 父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID
# 有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务
# 常见的Apache服务器就是由父进程监听端口，每当有新的http请求时，就fork出子进程来处理新的http请求。
import os

print 'Process (%s) start...' % os.getpid()
pid = os.fork()
if pid == 0:
    print 'I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid())
else:
    print 'I (%s) just created a child process (%s).' % (os.getpid(), pid)

# multiprocessing模块是跨平台版本的多进程模块。
# multiprocessing模块提供了一个Process类来代表一个进程对象，下面的例子演示了启动一个子进程并等待其结束：
# 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动
from multiprocessing import Process
import os


# 子进程要执行的代码
def run_proc(name):
    print 'Run child process %s (%s)...' % (name, os.getpid())

if __name__ == '__main__':
    print 'Parent process %s.' % os.getpid()            # 当前进程 即父进程
    p = Process(target=run_proc, args=('test',))        # 创建子进程 运行run_proc  传入参数('test',)
    print 'Process will start.'
    p.start()                                           # 启动子进程
    p.join()                                            # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
    print 'Process end.'

# Pool
# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
from multiprocessing import Pool
import os, time, random


def long_time_task(name):
    print 'Run task %s (%s)...' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))

if __name__ == '__main__':
    print 'Parent process %s.' % os.getpid()
    p = Pool()                                      # 默认pool的大小是CPU的核数 可以改为其他数字
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print 'Waiting for all subprocesses done...'
    p.close()
    p.join()
    print 'All subprocesses done.'
# 对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，
# 调用close()之后就不能继续添加新的Process了。


# 进程间通信
# Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。
# 以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据：
from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码:
def write(q):
    for value in ['A', 'B', 'C']:
        print 'Put %s to queue...' % value
        q.put(value)
        time.sleep(random.random())             # 等待一段时间 让read进程读取

# 读数据进程执行的代码:
def read(q):
    while True:
        value = q.get(True)
        print 'Get %s from queue.' % value

if __name__ == '__main__':
    q = Queue()                                 # 父进程创建Queue，并传给各个子进程：
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()                                  # 启动子进程pw，写入:
    pr.start()                                  # 启动子进程pr，读取:
    pw.join()                                   # 等待pw结束:
    pr.terminate()                              # pr进程里是死循环，无法等待其结束，只能强行终止:

# 在Unix/Linux下，multiprocessing模块封装了fork()调用，使我们不需要关注fork()的细节。
# 由于Windows没有fork调用，因此，multiprocessing需要“模拟”出fork的效果，
# 父进程所有Python对象都必须通过pickle序列化再传到子进程去
# 所以，如果multiprocessing在Windows下调用失败了，要先考虑是不是pickle失败了。


# 多线程
# Python的线程是真正的Posix Thread，而不是模拟出来的线程。
# Python的标准库提供了两个模块：thread和threading，thread是低级模块，threading是高级模块，对thread进行了封装。
# 绝大多数情况下，我们只需要使用threading这个高级模块
# 启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行：
import time, threading

# 新线程执行的代码:
def loop():
    print 'thread %s is running...' % threading.current_thread().name
    n = 0
    while n < 5:
        n += 1
        print 'thread %s >>> %s' % (threading.current_thread().name, n)
        time.sleep(1)
    print 'thread %s ended.' % threading.current_thread().name

print 'thread %s is running...' % threading.current_thread().name
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print 'thread %s ended.' % threading.current_thread().name
# 任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程，
# Python的threading模块有个current_thread()函数，它永远返回当前线程的实例。
# 主线程实例的名字叫MainThread，子线程的名字在创建时指定， 如果不起名字Python就自动给线程命名为Thread-1，Thread-2
# 我们用LoopThread命名子线程。名字仅仅在打印时用来显示，完全没有其他意义


# Lock
# 多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，
# 而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改
# 线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱
import time, threading
balance = 0             # 假定这是你的银行存款:

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print balance
# 们要确保balance计算正确，就要给change_it()上一把锁，
# 当某个线程开始执行change_it()时，该线程因为获得了锁，因此其他线程不能同时执行change_it()，只能等待，
# 直到锁被释放后，获得该锁以后才能改。由于锁只有一个，无论多少线程，同一时刻最多只有一个线程持有该锁，
# 所以，不会造成修改的冲突。创建一个锁就是通过threading.Lock()来实现
import threading

balance = 0
lock = threading.Lock()

def run_thread(n):
    for i in range(100000):
        lock.acquire()                      # 先要获取锁:
        try:
            change_it(n)                    # 放心地改吧:
        finally:
            lock.release()                  # 改完了一定要释放锁:
# 获得锁的线程用完后一定要释放锁，否则那些苦苦等待锁的线程将永远等待下去，成为死线程。
# 所以我们用try...finally来确保锁一定会被释放
# 锁的好处就是确保了某段关键代码只能由一个线程从头到尾完整地执行
# 锁的坏处首先是阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了。
# 其次，由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁时，可能会造成死锁，
# 导致多个线程全部挂起，既不能执行，也无法结束，只能靠操作系统强制终止。


# 多核CPU
# GIL锁


# ThreadLocal


# 进程 vs. 线程


# 分布式进程


# 协程









