# 定义一个元组
my_tuple = (1, 2, 3, "Python", 3.14)
print(my_tuple, type(my_tuple))  # 输出: (1, 2, 3, 'Python', 3.14) <class 'tuple'>
# 访问元组元素
print(my_tuple[0])  # 输出: 1

# 元组切片
print(my_tuple[1:4])  # 输出: (2, 3, 'Python')

# 获取长度
print(len(my_tuple))  # 输出: 5

# 元组解包
a, b, c, d, e = my_tuple
print(a, b, c, d, e)  # 输出: 1 2 3 Python 3.14

# 元组的不可变特性
# my_tuple[1] = 'Changed'  # 这行代码会引发错误，因为元组不允许修改
