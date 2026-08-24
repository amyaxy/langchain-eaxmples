# 使用单引号
str1 = "Hello, Python"
print(str1, type(str1))  # 输出: Hello, Python <class 'str'>

# 使用双引号
str2 = "Hello, World"
print(str2, type(str2))  # 输出: Hello, World <class 'str'>
# 拼接字符串
greeting = str1 + " " + str2
print(greeting)  # 输出: Hello, Python Hello, World

# 字符串切片
print(greeting[0:5])  # 输出: Hello

# 查找子串
print("Python" in greeting)  # 输出: True

# 获取长度
print(len(greeting))  # 输出: 26

# 转换大小写
print(str1.upper())  # 输出: HELLO, PYTHON
print(str2.lower())  # 输出: hello, world

# 格式化字符串
name = "Alice"
welcome_message = f"Hello, {name}!"
print(welcome_message)  # 输出: Hello, Alice!
