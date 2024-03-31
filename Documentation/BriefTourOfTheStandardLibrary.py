# 操作系统接口
import os
print(os.getcwd())  # 返回当前工作目录

import shutil
shutil.move('file.txt', 'module')  # 将文件移动至另一个目录


# 文件通配符
import glob
print(glob.glob('*.py'))  # 返回文件名匹配指定规则的文件列表


# 命令行参数
import sys
print(sys.argv)  # 使用命令行处理本文件时，返回参数列表

import argparse  # 用于声明并处理更复杂的参数
parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)


# 错误输出和终止程序(二者均会终止程序)
sys.stderr.write('Warning, log file not found starting a new one\n')
sys.exit()


# 使用正则匹配指定字符串内容
import re
print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
print('tea for too'.replace('too', 'two'))  # 字符串内置替换函数


# 数学
import math
print(math.cos(math.pi / 4))

import random
print(random.random())


# 互联网访问
from urllib.request import urlopen
with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:  # 访问指定url内容
    for line in response:
        line = line.decode()
        if line.startswith('datetime'):
            print(line.rstrip())


# 日期和时间
from datetime import date
print(date.today())


# 数据压缩
import zlib
s = b'hello world hello world hello world'
print(len(s))
print(len(zlib.compress(s)))


# 性能测量
from timeit import Timer
print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())  # 打印代码执行所花费时间


# 质量控制(测试)
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()  # 通过文档字符串测试整个python文件而不是指定函数
