# 定义一个字典
my_dict = {"name": "Python", "version": 3.9}
print(my_dict, type(my_dict))  # 输出: {'name': 'Python', 'version': 3.9} <class 'dict'>
# 访问字典元素
print(my_dict["name"])  # 输出: Python

# 修改字典元素
my_dict["version"] = 3.10
print(my_dict)  # 输出: {'name': 'Python', 'version': 3.10}

# 添加新元素
my_dict["creator"] = "Guido van Rossum"
print(
    my_dict
)  # 输出: {'name': 'Python', 'version': 3.10, 'creator': 'Guido van Rossum'}

# 删除元素
del my_dict["version"]
print(my_dict)  # 输出: {'name': 'Python', 'creator': 'Guido van Rossum'}

# 获取所有键
print(my_dict.keys())  # 输出: dict_keys(['name', 'creator'])

# 获取所有值
print(my_dict.values())  # 输出: dict_values(['Python', 'Guido van Rossum'])

# 获取所有键值对
print(
    my_dict.items()
)  # 输出: dict_items([('name', 'Python'), ('creator', 'Guido van Rossum')])
