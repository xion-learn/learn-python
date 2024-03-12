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
