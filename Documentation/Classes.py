# 作用域
def scope_test():
    def do_local():
        spam = 'local spam'

    def do_nonlocal():
        nonlocal spam
        spam = 'nonlocal spam'

    def do_global():
        global spam
        spam = 'global spam'

    spam = 'test spam'
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)


# 定义类
class MyClass:
    """A simple example class"""
    def __init__(self, some):
        self.some = some

    i = 12345

    def f(self):
        return 'hello world'


print(MyClass.i)
my_class = MyClass('some')
print(my_class.some)

my_class_1 = MyClass('1')
my_class_2 = MyClass('2')
my_class_1.i = 'i1'
my_class_2.i = 'i2'
print(my_class_1.i)
print(my_class_2.i)


# 类的继承
class MySubClass(MyClass):
    def __int__(self, some):
        super.__init__(some)

    def f(self):
        return 'hello MySubClass'


my_sub_class = MySubClass('')
print(my_sub_class.f())


# 子类重写父类方法
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        # 使用双下划线开头的副本方法，确保子类重写update时仍然调用父类update
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update


class MappingSubclass(Mapping):
    # 重写父类update方法
    def update(self, keys, values):
        for item in zip(keys, values):
            self.items_list.append(item)


# 用于声明一个数据结构
from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    dept: str
    salary: int