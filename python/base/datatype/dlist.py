# 定义一个列表
my_list = [1, 2, 3, "Python", 3.14]
print(my_list, type(my_list))  # 输出: [1, 2, 3, 'Python', 3.14] <class 'list'>
# 访问列表元素
print(my_list[0])  # 输出: 1

# 修改列表元素
my_list[1] = "Changed"
print(my_list)  # 输出: [1, 'Changed', 3, 'Python', 3.14]

# 添加新元素
my_list.append("New Element")
print(my_list)  # 输出: [1, 'Changed', 3, 'Python', 3.14, 'New Element']

# 删除元素
my_list.remove("Python")
print(my_list)  # 输出: [1, 'Changed', 3, 3.14, 'New Element']

# 获取长度
print(len(my_list))  # 输出: 5

# 列表切片
print(my_list[1:4])  # 输出: ['Changed', 3, 3.14]
