# # 触发语法错误SyntaxError
# while True print('Hello world')
#
#
# # 执行时出错，统称为异常
# 10 * (1 / 0)
# 4 + spam * 3
# '2' + 2


# 当异常是except子句中的类，或是其基类时，执行子句
class B(Exception):
    pass


class C(B):
    pass


class D(C):
    pass


for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")


# 异常通常会携带参数
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))
    print(inst.args)
    print(inst)

    x, y = inst.args
    print('x =', x)
    print('y =', y)


# 因调用其他函数产生的异常，也会被捕获
def this_fails():
    x = 1 / 0

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)


# raise语句手动触发异常
def new_error():
    try:
        raise NameError('err1')
    except NameError:
        print('except1!')


# 底层处理异常后，异常不会传递到上层
try:
    new_error()
except NameError:
    print('except2!')
    raise


# finally子句
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")


divide(2, 1)
divide(2, 0)


# 同时抛出多个异常
def f():
    raise ExceptionGroup('group1', [OSError(1), SystemError(2), ExceptionGroup('group2', [OSError(3)])])

try:
    f()
except* OSError as e:
    print('OSError', e)
except* SystemError as e:
    print('SystemError', e)
