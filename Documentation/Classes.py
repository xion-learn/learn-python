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
