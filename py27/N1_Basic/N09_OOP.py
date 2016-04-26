#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 面向对象编程 Object Oriented Programming，简称OOP
# OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数。
# 面向过程的程序,为了表示一个学生的成绩可以用一个dict表示：
def print_score(std):
    print '%s: %s' % (std['name'], std['score'])
std1 = {'name': 'Michael', 'score': 98}
std2 = {'name': 'Bob', 'score': 81}


# 面向对象的程序设计思想
# Student这种数据类型应该被视为一个对象，这个对象拥有name和score这两个属性（Property）
class Student(object):
    def __init__(self, name, score):    # 如果没有加self则会报错TypeError: Student() takes no arguments (1 given)
        self.name = name
        self.score = score

    def print_score(self):
        print '%s: %s' % (self.name, self.score)

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()

# 面向对象的设计思想是从自然界中来的，因为在自然界中，类（Class）和实例（Instance）的概念是很自然的。
# Class是一种抽象概念，比如我们定义的Class——Student，是指学生这个概念，而实例（Instance）则是一个个具体的Student
# 比如，Bart Simpson和Lisa Simpson是两个具体的Student：面向对象的设计思想是抽象出Class，根据Class创建Instance。
# 面向对象的抽象程度又比函数要高，因为一个Class既包含数据，又包含操作数据的方法。
# 数据封装、继承和多态是面向对象的三大特点


# 类（Class）和实例（Instance）
# 类是抽象的模板，而实例是根据类创建出来的一个个具体的“对象”
# 每个对象都拥有相同的方法，但各自的数据可能不同。
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print '%s: %s' % (self.name, self.score)

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'
# class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的
# 如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
# 定义好了类，就可以根据类创建出实例，创建实例是通过类名+()实现的：
# 类中定义的函数(method)只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。
# 类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数和关键字参数。
bart = Student('Bart Simpson', 59)
print bart
print Student


# 数据封装
# 外部看Student类，就只需要知道，创建实例需要给出name和score，而如何打印，都是在Student类的内部定义的，
# 这些数据和逻辑被“封装”起来了，调用很容易，但却不用知道内部实现的细节。
bart.print_score()
bart.get_grade()


# 访问限制
# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__
# 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print '%s: %s' % (self.__name, self.__score)

    # 如果外部代码要获取name和score怎么办？可以给Student类增加get_name和get_score这样的方法：
    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    # 如果又要允许外部代码修改score怎么办？可以给Student类增加set_score方法：
    def set_score(self, score):
        self.__score = score

    # 参数检查
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

bart = Student('Bart Simpson', 98)
# bart.__name 外部访问则会报错
print bart.get_score()
bart.set_score(100)
print bart.get_score()
# 需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，
# 是特殊变量，特殊变量是可以直接访问的，不是private变量，
# 所以，不能用__name__、__score__这样的变量名。
# 以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，
# 当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
# 双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。
# 不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，
# 所以，仍然可以通过_Student__name来访问__name变量：
# print bart._Student__name
# 但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名。


# 继承和多态
# 在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，
# 新的class称为子类（Subclass），而被继承的class称为基类、父类或超类（Base class、Super class）。
# 对于Dog来说，Animal就是它的父类，对于Animal来说，Dog就是它的子类。Cat和Dog类似。
class Animal(object):
    def run(self):
        print 'Animal is running   '


class Dog(Animal):
    def run(self):
        print 'Dog is running   '


class Cat(Animal):
    def run(self):
        print 'Cat is running   '

# 多态： 当子类和父类都存在相同的run()方法时，子类的run()覆盖了父类的run()
dog = Dog()
cat = Cat()
dog.run()
cat.run()

# 在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。但是，反过来就不行：
# c是Dog类型 也是Animal类型
c = Dog()
print isinstance(c, Dog)
print isinstance(c, Animal)


def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())     # 输出Animal is running   
run_twice(Dog())        # 输出Dog is running   
run_twice(Cat())        # 输出Cat is running   


# 如果我们再定义一个Tortoise类型，也从Animal派生：
class Tortoise(Animal):
    def run(self):
        print 'Tortoise is running slowly   '

run_twice(Tortoise())
# 新增一个Animal的子类，不必对run_twice()做任何修改，
# 实际上，任何依赖Animal作为参数的函数或者方法都可以不加修改地正常运行，原因就在于多态。
# 多态真正的威力：调用方只管调用，不管细节
# “开闭”原则：
# 对扩展开放：允许新增Animal子类；
# 对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。

# 继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，
# 子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写；

# 旧的方式定义Python类允许不从object类继承，但这种编程方式已经严重不推荐使用。
# 任何时候，如果没有合适的类可以继承，就继承自object类


# 因为python新式类的继承用了新的MRO方法，处理多重继承的时候，继承的属性、方法等是按照（P1，P2）从左往右搜索的，
# 比如说run()，如果在P1中搜索到了此方法，那么子类Man的run()就会调用P1的
class Animal(object):
    def run(self):
        print 'Animal is running   '


class People(object):
    def run(self):
        print 'People is running   '


class Man(People, Animal):      # 继承了People和Animal
     pass
mine = Man()
mine.run()          # 按照顺序继承 会输出People is running   


# run_twice函数并不依赖Animal类，只要是拥有run方法的类的实例都可以作为其参数。 如下例子
# http://blog.csdn.net/shangzhihaohao/article/details/7065675
class Animal(object):
    def run(self):
        print 'Animal is running   '


class Dog(Animal):
    def run(self):
        print 'Dog is running   '

    def eat(self):
        print 'Eating meat'


class Cat(Animal):
    def run(self):
        print 'Cat is running..'

    def eat(self):
        print 'Eating pis..'


class Bee(object):
    def run(self):
        print 'Actually is flying..'

    def sleep(self):
        print 'take a nap..'


def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(Dog())
run_twice(Bee())

print isinstance(Bee(), Animal)
print isinstance(Cat(), Animal)


# type() 获取对象信息
import types
print type('abc') == types.StringType
print type(u'abc') == types.UnicodeType
print type([])==types.ListType
print type(str)==types.TypeType
print type(int)==type(str)==types.TypeType      # 所有类型本身的类型就是TypeType

# isinstance(object, class-or-type-or-tuple) 用于继承关系判断 一个对象是否是某种类型
# object -> Animal -> Dog
a = Animal()
d = Dog()
isinstance(d, Dog)
isinstance(d, Animal)
isinstance(a, Dog)

isinstance('a', (str, unicode))
isinstance(u'a', (str, unicode))
# 由于str和unicode都是从basestring继承下来的，所以，还可以把上面的代码简化为：
isinstance(u'a', basestring)


# dir() :获得一个对象的所有属性和方法 返回一个包含字符串的list
print dir('ABC')

# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。
# 在Python中，如果你调用len()函数试图获取一个对象的长度，
# 实际上，在len()函数内部，它自动去调用该对象的__len__()方法 所以，下面的代码是等价的：
print len('ABC')
print 'ABC'.__len__()


# 配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
class MyObject(object):
        def __init__(self):
            self.x = 9

        def power(self):
            return self.x * self.x

obj = MyObject()
hasattr(obj, 'x')           # 有属性'x'吗？
obj.x
hasattr(obj, 'y')           # 有属性'y'吗？
setattr(obj, 'y', 19)       # 设置一个属性'y'为19
hasattr(obj, 'y')           # 有属性'y'吗？
getattr(obj, 'y')           # 获取属性'y'
hasattr(obj, 'power')       # 有方法'power'吗？
getattr(obj, 'power')       # 获取方法'power'
fn = getattr(obj, 'power')  # 获取方法'power'并赋值到变量fn
fn
fn()
obj.y                   # 获取属性'y'
# 可以传入一个default参数，如果属性不存在，就返回默认值
getattr(obj, 'z', 404)  # 获取属性'z'，如果不存在，返回默认值404


# 只有在不知道对象信息的时候，我们才会去获取对象信息。
# 如果可以直接写： sum = obj.x + obj.y 就不要写 sum = getattr(obj, 'x') + getattr(obj, 'y')
# 假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，
# 如果存在，则该对象是一个流，如果不存在，则无法读取。hasattr()就派上了用场。
def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None


