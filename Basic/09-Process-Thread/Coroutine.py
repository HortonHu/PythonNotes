# -*- coding:utf-8 -*-


# 协程
# 协程，又称微线程，纤程。英文名Coroutine。
# 子程序，或者称为函数，在所有语言中都是层级调用，
# 比如A调用B，B在执行过程中又调用了C，C执行完毕返回，B执行完毕返回，最后是A执行完毕。
# 所以子程序调用是通过栈实现的，一个线程就是执行一个子程序。子程序调用总是一个入口，一次返回，调用顺序是明确的。
# 而协程的调用和子程序不同。# 协程看上去也是子程序，但执行过程中，在子程序内部可中断，然后转而执行别的子程序，
# 在适当的时候再返回来接着执行。
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

# Python中的协程和生成器很相似但又稍有不同。主要区别在于：
# 生成器是数据的生产者
# 协程则是数据的消费者

# 首先我们先来回顾下生成器的创建过程。我们可以这样去创建一个生成器:
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# 然后我们经常在for循环中这样使用它:
for i in fib():
    print i

# 这样做不仅快而且不会给内存带来压力，因为我们所需要的值都是动态生成的而不是将他们存储在一个列表中。
# 更概括的说如果现在我们在上面的例子中使用yield便可获得了一个协程。
# 协程会消费掉发送给它的值。Python实现的grep就是个很好的例子：
def grep(pattern):
    print("Searching for", pattern)
    while True:
        line = (yield)          # 此处yield后面没有参数 不产生数据 只消费传入的数据
        if pattern in line:
            print(line)

# yield返回了什么？啊哈，我们已经把它变成了一个协程。
# 它将不再包含任何初始值，相反要从外部传值给它。我们可以通过send()方法向它传值。这有个例子：
search = grep('coroutine')
next(search)
# output: Searching for coroutine
search.send("I love you")
search.send("Don't you love me?")
search.send("I love coroutine instead!")
# output: I love coroutine instead!

# 发送的值会被yield接收。我们为什么要运行next()方法呢？这样做正是为了启动一个协程。
# 就像协程中包含的生成器并不是立刻执行，而是通过next()方法来响应send()方法。因此，你必须通过next()方法来执行yield表达式。

# 我们可以通过调用close()方法来关闭一个协程
search = grep('coroutine')
search.close()







