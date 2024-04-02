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
