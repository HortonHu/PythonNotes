# -*- coding:utf-8 -*-


# 面向对象编程 Object Oriented Programming，简称OOP
# OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数。
# 面向过程的程序,为了表示一个学生的成绩可以用一个dict表示
# 面向对象的程序设计思想 Student这种数据类型应该被视为一个对象，这个对象拥有name和score这两个属性（Property）
# Class是一种抽象概念，比如我们定义的Class——Student，是指学生这个概念，而实例（Instance）则是一个个具体的Student
# 类是抽象的模板，而实例是根据类创建出来的一个个具体的“对象” 每个对象都拥有相同的方法，但各自的数据可能不同。
# class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的
# 如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
# 定义好了类，就可以根据类创建出实例，创建实例是通过类名+()实现的：

# OOP三大特点
# 封装
# 继承
# 多态


# 封装（encapsulation）
# 数据和逻辑被“封装”起来了，调用很容易，但却不用知道内部实现的细节。
# 访问限制：如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__
# 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
class Student(object):
    ans_to_everything = 42  # 类变量 如果定义了类变量，最好使用immutable对象

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print '%s: %s' % (self.__name, self.__score)

    # 外部代码要获取私有变量可以给类增加get_xxx这样的方法：
    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    # 允许外部代码修改私有变量可以给类增加set_xxx方法：
    def set_score(self, score):
        self.__score = score

    # 参数检查
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

bart = Student('Bart Simpson', 98)
print bart.get_score()      # 外部访问bart.__score则会报错
bart.set_score(100)
print bart.get_score()
# 需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，
# 是特殊变量，特殊变量是可以直接访问的，不是private变量，所以不能用__name__、__score__这样的变量名。
# 以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，
# 当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
# 双下划线开头的实例变量不能从外部访问是因为Python解释器对外把__name变量改成了_Student__name，
# 所以，仍然可以通过_Student__name来访问__name变量： print bart._Student__name
# 但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名。


# 继承和多态
# 在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，
# 新的class称为子类（Subclass），而被继承的class称为基类、父类或超类（Base class、Super class）。
# Animal是Dog、Cat的父类，Dog、Cat是Animal的子类
# 继承可以直接使用父类功能，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写
# 旧的方式定义Python类允许不从object类继承，但这种编程方式已经严重不推荐使用。
# 任何时候，如果没有合适的类可以继承，就继承自object类
class Animal(object):
    def run(self):
        print 'Animal is running   '


class Dog(Animal):
    def run(self):
        print 'Dog is running   '


class Cat(Animal):
    def run(self):
        print 'Cat is running   '

# 多态：当子类和父类都存在相同的run()方法时，子类的run()覆盖了父类的run()
dog = Dog()
cat = Cat()
dog.run()
cat.run()
# 在继承关系中，子类的实例也可以看做是父类的实例，反之不行
print isinstance(dog, Dog)
print isinstance(dog, Animal)


def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())     # 输出Animal is running
run_twice(Dog())        # 输出Dog is running
run_twice(Cat())        # 输出Cat is running
# 只要一个类里面定义了run方法，就可以被run_twice调用
# 实际上，任何依赖Animal作为参数的函数或者方法都可以不加修改地正常运行，原因就在于多态。
# 多态真正的威力：调用方只管调用，不管细节

# “开闭”原则：
# 对扩展开放：允许新增Animal子类；
# 对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。