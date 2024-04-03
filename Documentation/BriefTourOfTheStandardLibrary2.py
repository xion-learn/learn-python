# 格式化输出
import reprlib
print(reprlib.repr(set('supercalifragilisticexpialidocious')))  # 打印一个过长对象的缩略文本

import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]
pprint.pprint(t, width=120)  # 用指定宽度格式化内容


# 模板
from string import Template
t = Template('${village}folk send $$10 to $cause.')
print(t.substitute(village='Nottingham', cause='the ditch fund'))
print(t.safe_substitute(cause='the ditch fund'))  # 若未提供指定值，则占位符将保留原样


# 使用二进制数据记录格式
import struct
print(struct.pack('<H', 11))


# 日志记录
import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')


# 十进制浮点运算(更精确的浮点运算)
from decimal import *
print(Decimal('1.00') % Decimal('.10'))
print(1.00 % 0.10)

print(sum([Decimal('0.1')]*10) == Decimal('1.0'))
print(0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 == 1.0)
