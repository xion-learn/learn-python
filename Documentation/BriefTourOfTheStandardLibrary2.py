# 格式化输出
import reprlib
print(reprlib.repr(set('supercalifragilisticexpialidocious')))  # 打印一个过长对象的缩略文本

import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]
pprint.pprint(t, width=120)  # 用指定宽度格式化内容
