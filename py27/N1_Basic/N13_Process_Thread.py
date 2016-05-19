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
import threading, multiprocessing

def loop():
    x = 0
    while True:
        x = x ^ 1

for i in range(100):
    t = threading.Thread(target=loop)
    t.start()
# CPU占用率达不到全部
# 因为Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global InterpreterLock，
# 任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。
# 这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在Python中只能交替执行，
# 即使100个线程跑在100核CPU上，也只能用到1个核。
# 所以，在Python中，可以使用多线程，但不要指望能有效利用多核。
# 如果一定要通过多线程利用多核，那只能通过C扩展来实现，不过这样就失去了Python简单易用的特点。
# 不过，也不用过于担心，Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。
# 多个Python进程有各自独立的GIL锁，互不影响。


# ThreadLocal
# 在多线程环境下，每个线程都有自己的数据。一个线程使用自己的局部变量比使用全局变量好，
# 因为局部变量只有线程自己能看见，不会影响其他线程，而全局变量的修改必须加锁。
# 但是局部变量也有问题，就是在函数调用的时候，传递起来很麻烦：
# def process_student(name):
#     std = Student(name)
#     # std是局部变量，但是每个函数都要用它，因此必须传进去：
#     do_task_1(std)
#     do_task_2(std)
#
# def do_task_1(std):
#     do_subtask_1(std)
#     do_subtask_2(std)
#
# def do_task_2(std):
#     do_subtask_2(std)
#     do_subtask_2(std)
# 如果用一个全局dict存放所有的Student对象，然后以thread自身作为key获得线程对应的Student对象如何？
# global_dict = {}
#
# def std_thread(name):
#     std = Student(name)
#     # 把std放到全局变量global_dict中：
#     global_dict[threading.current_thread()] = std
#     do_task_1()
#     do_task_2()
#
# def do_task_1():
#     # 不传入std，而是根据当前线程查找：
#     std = global_dict[threading.current_thread()]
#     ...
#
# def do_task_2():
#     # 任何函数都可以查找出当前线程的std变量：
#     std = global_dict[threading.current_thread()]
#     ...
# 这种方式理论上是可行的，它最大的优点是消除了std对象在每层函数中的传递问题，但是，每个函数获取std的代码有点丑。
# ThreadLocal应运而生，不用查找dict，ThreadLocal帮你自动做这件事：
import threading

# 创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
    print 'Hello, %s (in %s)' % (local_school.student, threading.current_thread().name)

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()

t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
# 全局变量local_school就是一个ThreadLocal对象，每个Thread对它都可以读写student属性，但互不影响。
# 你可以把local_school看成全局变量，但每个属性如local_school.student都是线程的局部变量，
# 可以任意读写而互不干扰，也不用管理锁的问题，ThreadLocal内部会处理。
# 可以理解为全局变量local_school是一个dict，不但可以用local_school.student，还可以绑定其他变量，如local_school.teacher等等。
# ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，
# 这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。


# 进程 vs. 线程



# 分布式进程


# 协程









