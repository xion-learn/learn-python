# 列表详解
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

fruits.append('orange')  # 在列表末尾添加元素
fruits.extend(['yes'])  # 将列表与新列表连接
fruits.insert(1, 'no')  # 在列表指定位置插入元素
fruits.remove('orange')  # 删除列表中第一个值为orange的元素
fruits.pop(2)  # 删除指定位置的元素，若不指定则删除末尾元素
fruits.index('apple')  # 找到指定元素的index索引
fruits.count('orange')  # 返回指定元素出现的次数
fruits.sort()  # 就地排序列表
fruits.reverse()  # 翻转列表
fruits.copy()  # 返回列表的浅拷贝
fruits.clear()  # 清空删除列表


# 列表推导式
newList = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(newList)


# 嵌套的列表推导式
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print([[row[i] for row in matrix] for i in range(4)])


# del语句
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)

del a[2:4]
print(a)

del a[:]
print(a)

del a


# 元组
t = 12345, 54321, 'hello!'
print(t[0])

# 元组可嵌套
u = t, (1, 2, 3, 4, 5)
print(t[0])

# 元组元素是不可变的
# t[0] = 88888

# 元组可嵌套列表，列表可变
v = ([1, 2, 3], [3, 2, 1])


# 集合Set
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('orange' in basket, 'crabgrass' in basket)

# 支持交并补等操作
a = set('abracadabra')
b = set('alacazam')
print(a - b, a | b, a & b, a ^ b)


# 字典
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)

del tel['sape']
tel['irv'] = 4127
print('guido' in tel, 'jack' not in tel)
