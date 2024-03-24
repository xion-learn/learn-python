# 控制字符串最小长度
table = {'Sjoerd': 417, 'Jack': 4098, 'Dcab': 768}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')


# 使用修饰符
animals = 'eels'
print(f'My hovercraft is full of {animals!s}.')
print(f'My hovercraft is full of {animals!r}.')


# 等号说明符
bugs = 'roaches'
count = 13
area = 'living room'
print(f'Debugging {bugs=} {count=} {area=}')


# 通过指定参数位置输出指定内容
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))


# 使用rjust函数自定义格式化
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), repr(x*x*x).rjust(4))


with open('file.txt', 'r+', encoding="utf-8") as f:
    f.write('\n33333333333333')
    for line in f:
        print(line)

# 查看文件是否被正确关闭
print(f.closed)


# JSON将字典转换为字符串
import json
x = [1, 'simple', 'list']
print(json.dumps(x))
