# 算术运算符
a = 10
b = 3

print(a + b)  # 输出: 13
print(a - b)  # 输出: 7
print(a * b)  # 输出: 30
print(a / b)  # 输出: 3.3333333333333335
print(a // b)  # 输出: 3
print(a % b)  # 输出: 1
print(a**b)  # 输出: 100


# 比较运算符
a = 10
b = 3

print(a == b)  # 输出: False
print(a != b)  # 输出: True
print(a > b)  # 输出: True
print(a < b)  # 输出: False
print(a >= b)  # 输出: True
print(a <= b)  # 输出: False

# 逻辑运算符
a = True
b = False

print(a and b)  # 输出: False
print(a or b)  # 输出: True
print(not a)  # 输出: False

# 赋值运算符
a = 10
b = 3

a += b  # 等价于 a = a + b
print(a)  # 输出: 13

a -= b  # 等价于 a = a - b
print(a)  # 输出: 10

a *= b  # 等价于 a = a * b
print(a)  # 输出: 30

a /= b  # 等价于 a = a / b
print(a)  # 输出: 10.0

a //= b  # 等价于 a = a // b
print(a)  # 输出: 3.0

a %= b  # 等价于 a = a % b
print(a)  # 输出: 0.0

a **= b  # 等价于 a = a ** b
print(a)  # 输出: 0.0


# 位运算符
a = 10  # 二进制: 1010
b = 4  # 二进制: 0100

print(a & b)  # 输出: 0  (二进制: 0000)
print(a | b)  # 输出: 14 (二进制: 1110)
print(a ^ b)  # 输出: 14 (二进制: 1110)
print(~a)  # 输出: -11 (二进制: -1011)

print(a << 2)  # 输出: 40 (二进制: 101000)
print(a >> 2)  # 输出: 2  (二进制: 0010)
