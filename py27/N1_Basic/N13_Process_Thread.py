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
# 首先，要实现多任务，通常我们会设计Master-Worker模式，Master负责分配任务，Worker负责执行任务，
# 因此，多任务环境下，通常是一个Master，多个Worker。
# 如果用多进程实现Master-Worker，主进程就是Master，其他进程就是Worker。
# 如果用多线程实现Master-Worker，主线程就是Master，其他线程就是Worker。
# 多进程模式最大的优点就是稳定性高，因为一个子进程崩溃了，不会影响主进程和其他子进程。
# （当然主进程挂了所有进程就全挂了，但是Master进程只负责分配任务，挂掉的概率低）著名的Apache最早就是采用多进程模式。
# 多进程模式的缺点是创建进程的代价大，在Unix/Linux系统下，用fork调用还行，在Windows下创建进程开销巨大。
# 另外，操作系统能同时运行的进程数也是有限的，在内存和CPU的限制下，如果有几千个进程同时运行，操作系统连调度都会成问题。
# 多线程模式通常比多进程快一点，但是也快不到哪去，而且，多线程模式致命的缺点就是任何一个线程挂掉都可能直接造成整个进程崩溃，
# 因为所有线程共享进程的内存。在Windows上，如果一个线程执行的代码出了问题，你经常可以看到这样的提示：
# “该程序执行了非法操作，即将关闭”，其实往往是某个线程出了问题，但是操作系统会强制结束整个进程。
# 在Windows下，多线程的效率比多进程要高，所以微软的IIS服务器默认采用多线程模式。
# 由于多线程存在稳定性的问题，IIS的稳定性就不如Apache。
# 为了缓解这个问题，IIS和Apache现在又有多进程+多线程的混合模式，真是把问题越搞越复杂。

# 线程切换
# 多任务一旦多到一个限度，就会消耗掉系统所有的资源，结果效率急剧下降，所有任务都做不好。

# 计算密集型 vs. IO密集型
# 是否采用多任务的第二个考虑是任务的类型。我们可以把任务分为计算密集型和IO密集型。
# 计算密集型任务的特点是要进行大量的计算，消耗CPU资源，比如计算圆周率、对视频进行高清解码等等，全靠CPU的运算能力。
# 这种计算密集型任务虽然也可以用多任务完成，但是任务越多，花在任务切换的时间就越多，CPU执行任务的效率就越低，
# 所以，要最高效地利用CPU，计算密集型任务同时进行的数量应当等于CPU的核心数。
# 计算密集型任务由于主要消耗CPU资源，因此，代码运行效率至关重要。Python这样的脚本语言运行效率很低，完全不适合计算密集型任务。
# 对于计算密集型任务，最好用C语言编写。
# 第二种任务的类型是IO密集型，涉及到网络、磁盘IO的任务都是IO密集型任务，
# 这类任务的特点是CPU消耗很少，任务的大部分时间都在等待IO操作完成（因为IO的速度远远低于CPU和内存的速度）。
# 对于IO密集型任务，任务越多，CPU效率越高，但也有一个限度。常见的大部分任务都是IO密集型任务，比如Web应用。
# IO密集型任务执行期间，99%的时间都花在IO上，花在CPU上的时间很少，
# 因此，用运行速度极快的C语言替换用Python这样运行速度极低的脚本语言，完全无法提升运行效率。
# 对于IO密集型任务，最合适的语言就是开发效率最高（代码量最少）的语言，脚本语言是首选，C语言最差。

# 异步IO
# 考虑到CPU和IO之间巨大的速度差异，一个任务在执行的过程中大部分时间都在等待IO操作，单进程单线程模型会导致别的任务无法并行执行，
# 因此，我们才需要多进程模型或者多线程模型来支持多任务并发执行。
# 现代操作系统对IO操作已经做了巨大的改进，最大的特点就是支持异步IO。
# 如果充分利用操作系统提供的异步IO支持，就可以用单进程单线程模型来执行多任务，这种全新的模型称为事件驱动模型，
# Nginx就是支持异步IO的Web服务器，它在单核CPU上采用单进程模型就可以高效地支持多任务。
# 在多核CPU上，可以运行多个进程（数量与CPU核心数相同），充分利用多核CPU。由于系统总的进程数量十分有限，因此操作系统调度非常高效。
# 用异步IO编程模型来实现多任务是一个主要的趋势。对应到Python语言，单进程的异步编程模型称为协程


# 协程
# 协程，又称微线程，纤程。英文名Coroutine。
# 子程序，或者称为函数，在所有语言中都是层级调用，比如A调用B，B在执行过程中又调用了C，C执行完毕返回，B执行完毕返回，最后是A执行完毕。
# 所以子程序调用是通过栈实现的，一个线程就是执行一个子程序。子程序调用总是一个入口，一次返回，调用顺序是明确的。而协程的调用和子程序不同。
# 协程看上去也是子程序，但执行过程中，在子程序内部可中断，然后转而执行别的子程序，在适当的时候再返回来接着执行。
# 注意，在一个子程序中中断，去执行其他子程序，不是函数调用，有点类似CPU的中断。比如子程序A、B：
def A():
    print '1'
    print '2'
    print '3'

def B():
    print 'x'
    print 'y'
    print 'z'
# 假设由协程执行，在执行A的过程中，可以随时中断，去执行B，B也可能在执行过程中中断再去执行A 结果可能是：
# 1
# 2
# x
# y
# 3
# z
# 看起来A、B的执行有点像多线程，但协程的特点在于是一个线程执行，那和多线程比，协程有何优势？
# 最大的优势就是协程极高的执行效率。因为子程序切换不是线程切换，而是由程序自身控制，
# 因此，没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显。
# 第二大优势就是不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，
# 在协程中控制共享资源不加锁，只需要判断状态就好了，所以执行效率比多线程高很多。
# 因为协程是一个线程执行，那怎么利用多核CPU呢？
# 最简单的方法是多进程+协程，既充分利用多核，又充分发挥协程的高效率，可获得极高的性能。
# Python对协程的支持还非常有限，用在generator中的yield可以一定程度上实现协程。虽然支持不完全，但已经可以发挥相当大的威力了。
# 例如 传统的生产者-消费者模型是一个线程写消息，一个线程取消息，通过锁机制控制队列和等待，但一不小心就可能死锁。
# 如果改用协程，生产者生产消息后，直接通过yield跳转到消费者开始执行，待消费者执行完毕后，切换回生产者继续生产，效率极高：
import time

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        time.sleep(1)
        r = '200 OK'

def produce(c):
    c.next()
    n = 0
    while n < 5:
        n += 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

if __name__ == '__main__':
    c = consumer()
    produce(c)
# 注意到consumer函数是一个generator（生成器），把一个consumer传入produce后：
# 1. 首先调用c.next()启动生成器；
# 2. 然后，一旦生产了东西，通过c.send(n)切换到consumer执行；
# 3. consumer通过yield拿到消息，处理，又通过yield把结果传回；
# 4. produce拿到consumer处理的结果，继续生产下一条消息；
# 5. produce决定不生产了，通过c.close()关闭consumer，整个过程结束。
# 整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务。
# 最后套用Donald Knuth的一句话总结协程的特点：
# “子程序就是协程的一种特例。”

# gevent
# Python通过yield提供了对协程的基本支持，但是不完全。而第三方的gevent为Python提供了比较完善的协程支持。
# gevent是第三方库，通过greenlet实现协程，其基本思想是：
# 当一个greenlet遇到IO操作时，比如访问网络，就自动切换到其他的greenlet，等到IO操作完成，再在适当的时候切换回来继续执行。
# 由于IO操作非常耗时，经常使程序处于等待状态，有了gevent为我们自动切换协程，就保证总有greenlet在运行，而不是等待IO。
# 由于切换是在IO操作时自动完成，所以gevent需要修改Python自带的一些标准库，这一过程在启动时通过monkey patch完成：
from gevent import monkey; monkey.patch_socket()
import gevent

def f(n):
    for i in range(n):
        print gevent.getcurrent(), i

g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)
g1.join()
g2.join()
g3.join()
# 运行结果：
# <Greenlet at 0x10e49f550: f(5)> 0
# <Greenlet at 0x10e49f550: f(5)> 1
# <Greenlet at 0x10e49f550: f(5)> 2
# <Greenlet at 0x10e49f550: f(5)> 3
# <Greenlet at 0x10e49f550: f(5)> 4
# <Greenlet at 0x10e49f910: f(5)> 0
# <Greenlet at 0x10e49f910: f(5)> 1
# <Greenlet at 0x10e49f910: f(5)> 2
# <Greenlet at 0x10e49f910: f(5)> 3
# <Greenlet at 0x10e49f910: f(5)> 4
# <Greenlet at 0x10e49f4b0: f(5)> 0
# <Greenlet at 0x10e49f4b0: f(5)> 1
# <Greenlet at 0x10e49f4b0: f(5)> 2
# <Greenlet at 0x10e49f4b0: f(5)> 3
# <Greenlet at 0x10e49f4b0: f(5)> 4
# 可以看到，3个greenlet是依次运行而不是交替运行。
# 要让greenlet交替运行，可以通过gevent.sleep()交出控制权：
def f(n):
    for i in range(n):
        print gevent.getcurrent(), i
        gevent.sleep(0)
# 执行结果：
# <Greenlet at 0x10cd58550: f(5)> 0
# <Greenlet at 0x10cd58910: f(5)> 0
# <Greenlet at 0x10cd584b0: f(5)> 0
# <Greenlet at 0x10cd58550: f(5)> 1
# <Greenlet at 0x10cd584b0: f(5)> 1
# <Greenlet at 0x10cd58910: f(5)> 1
# <Greenlet at 0x10cd58550: f(5)> 2
# <Greenlet at 0x10cd58910: f(5)> 2
# <Greenlet at 0x10cd584b0: f(5)> 2
# <Greenlet at 0x10cd58550: f(5)> 3
# <Greenlet at 0x10cd584b0: f(5)> 3
# <Greenlet at 0x10cd58910: f(5)> 3
# <Greenlet at 0x10cd58550: f(5)> 4
# <Greenlet at 0x10cd58910: f(5)> 4
# <Greenlet at 0x10cd584b0: f(5)> 4
# 3个greenlet交替运行，
# 把循环次数改为500000，让它们的运行时间长一点，然后在操作系统的进程管理器中看，线程数只有1个。
# 当然，实际代码里，我们不会用gevent.sleep()去切换协程，而是在执行到IO操作时，gevent自动切换，代码如下：
from gevent import monkey; monkey.patch_all()
import gevent
import urllib2

def f(url):
    print('GET: %s' % url)
    resp = urllib2.urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))

gevent.joinall([
        gevent.spawn(f, 'https://www.python.org/'),
        gevent.spawn(f, 'https://www.yahoo.com/'),
        gevent.spawn(f, 'https://github.com/'),
])
# 运行结果：
# GET: https://www.python.org/
# GET: https://www.yahoo.com/
# GET: https://github.com/
# 45661 bytes received from https://www.python.org/.
# 14823 bytes received from https://github.com/.
# 304034 bytes received from https://www.yahoo.com/.
# 从结果看，3个网络操作是并发执行的，而且结束顺序不同，但只有一个线程。
# 使用gevent，可以获得极高的并发性能，但gevent只能在Unix/Linux下运行，在Windows下不保证正常安装和运行。
# 由于gevent是基于IO切换的协程，所以最神奇的是，我们编写的Web App代码，不需要引入gevent的包，也不需要改任何代码，
# 仅仅在部署的时候，用一个支持gevent的WSGI服务器，立刻就获得了数倍的性能提升。


# 分布式进程
# 在Thread和Process中，应当优选Process，因为Process更稳定，而且，Process可以分布到多台机器上，而Thread最多只能分布到同一台机器的多个CPU上。
# Python的multiprocessing模块不但支持多进程，其中managers子模块还支持把多进程分布到多台机器上。
# 一个服务进程可以作为调度者，将任务分布到其他多个进程中，依靠网络通信。由于managers模块封装很好，
# 不必了解网络通信的细节，就可以很容易地编写分布式多进程程序。
# 例子：如果我们已经有一个通过Queue通信的多进程程序在同一台机器上运行，
# 现在，由于处理任务的进程任务繁重，希望把发送任务的进程和处理任务的进程分布到两台机器上。怎么用分布式进程实现？
# 原有的Queue可以继续使用，但是，通过managers模块把Queue通过网络暴露出去，就可以让其他机器的进程访问Queue了。
# 先看服务进程，服务进程负责启动Queue，把Queue注册到网络上，然后往Queue里面写入任务：
import random, time, Queue
from multiprocessing.managers import BaseManager

# 发送任务的队列:
task_queue = Queue.Queue()
# 接收结果的队列:
result_queue = Queue.Queue()

# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass

# 把两个Queue都注册到网络上, callable参数关联了Queue对象:
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
# 绑定端口5000, 设置验证码'abc':
manager = QueueManager(address=('', 5000), authkey='abc')
# 启动Queue:
manager.start()
# 获得通过网络访问的Queue对象:
task = manager.get_task_queue()
result = manager.get_result_queue()
# 放几个任务进去:
for i in range(10):
    n = random.randint(0, 10000)
    print('Put task %d...' % n)
    task.put(n)
# 从result队列读取结果:
print('Try get results...')
for i in range(10):
    r = result.get(timeout=10)
    print('Result: %s' % r)
# 关闭:
manager.shutdown()

# 当我们在一台机器上写多进程程序时，创建的Queue可以直接拿来用，
# 但是，在分布式多进程环境下，添加任务到Queue不可以直接对原始的task_queue进行操作，
# 那样就绕过了QueueManager的封装，必须通过manager.get_task_queue()获得的Queue接口添加

# 另一台机器上启动任务进程（本机上启动也可以）：
import time, sys, Queue
from multiprocessing.managers import BaseManager

# 创建类似的QueueManager:
class QueueManager(BaseManager):
    pass

# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接到服务器，也就是运行taskmanager.py的机器:
server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr)
# 端口和验证码注意保持与taskmanager.py设置的完全一致:
m = QueueManager(address=(server_addr, 5000), authkey='abc')
# 从网络连接:
m.connect()
# 获取Queue的对象:
task = m.get_task_queue()
result = m.get_result_queue()
# 从task队列取任务,并把结果写入result队列:
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task queue is empty.')
# 处理结束:
print('worker exit.')










