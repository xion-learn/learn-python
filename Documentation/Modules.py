import module.fibo as fibo
# fibo.fib(10)

# # 将模块名称引入到局部命名空间中
# from module.fibo import fib, fib2
# fib(500)


# # 将模块中所有不以_开头的名称引入到局部命名空间中
# from module.fibo import *
# fib(500)


# 一个模块只会导入一次，可通过特殊函数重新导入模块
import importlib
importlib.reload(fibo)


# 一些内置模块
import sys
print(sys.path)

# 内置函数dir()
print(dir(sys))
