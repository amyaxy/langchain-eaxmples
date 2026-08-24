# 定义一个集合
my_set = {1, 2, 3, 4, 5}
print(my_set, type(my_set))  # 输出: {1, 2, 3, 4, 5} <class 'set'>

# 使用set()函数定义集合
another_set = set([3, 4, 5, 6, 7])
print(another_set, type(another_set))  # 输出: {3, 4, 5, 6, 7} <class 'set'>
# 添加新元素
my_set.add(6)
print(my_set)  # 输出: {1, 2, 3, 4, 5, 6}

# 集合的去重特性
my_set.add(3)
print(my_set)  # 输出: {1, 2, 3, 4, 5, 6}

# 删除元素
my_set.remove(4)
print(my_set)  # 输出: {1, 2, 3, 5, 6}

# 集合运算
print(my_set & another_set)  # 交集: {3, 5, 6}
print(my_set | another_set)  # 并集: {1, 2, 3, 5, 6, 7}
print(my_set - another_set)  # 差集: {1, 2}
print(my_set ^ another_set)  # 对称差集: {1, 2, 7}
