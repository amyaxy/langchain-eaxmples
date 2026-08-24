# 函数
def greet():
    print("Hello, welcome to Python programming!")


greet()


# 带参数的函数
def greet_user(name):
    print(f"Hello, {name}, welcome to Python programming!")


greet_user("Alice")  # 输出: Hello, Alice, welcome to Python programming!


# 带返回值的函数
def add(a, b):
    return a + b


result = add(3, 5)
print(result)  # 输出: 8
