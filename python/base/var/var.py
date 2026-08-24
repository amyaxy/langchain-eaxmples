# 定义变量
x = 10
y = 3.14
name = "Alice"
is_active = True

# 输出变量的值和类型
print(x, type(x))  # 输出: 10 <class 'int'>
print(y, type(y))  # 输出: 3.14 <class 'float'>
print(name, type(name))  # 输出: Alice <class 'str'>
print(is_active, type(is_active))  # 输出: True <class 'bool'>

# 变量参与运算
result = x + y
print(result)  # 输出: 13.14


# 变量传递给函数
def greet(person):
    return f"Hello, {person}!"


message = greet(name)
print(message)  # 输出: Hello, Alice!

# 变量用于条件判断
if is_active:
    print("The user is active.")  # 输出: The user is active.
else:
    print("The user is not active.")

# 合法的变量名
my_var = 10
_my_var = 20
myVar2 = 30

# 非法的变量名（会引发语法错误）
# 2myVar = 40
# my-var = 50
# my var = 60
