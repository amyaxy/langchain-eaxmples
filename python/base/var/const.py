# 定义常量
PI = 3.14159
GRAVITY = 9.81
MAX_CONNECTIONS = 100

# 输出常量的值
print(PI)  # 输出: 3.14159
print(GRAVITY)  # 输出: 9.81
print(MAX_CONNECTIONS)  # 输出: 100

# 使用常量计算圆的面积
radius = 5
area = PI * (radius**2)
print(f"The area of the circle is: {area}")  # 输出: The area of the circle is: 78.53975

# 使用常量进行条件判断
if MAX_CONNECTIONS > 50:
    print(
        "The server can handle many connections."
    )  # 输出: The server can handle many connections.
else:
    print("The server can handle only a few connections.")

# 合理的常量命名
SPEED_OF_LIGHT = 299792458  # 米每秒
PLANCK_CONSTANT = 6.62607015e-34  # 焦耳秒

# 不推荐的常量命名（不遵循约定）
# speed_of_light = 299792458
# planckConstant = 6.62607015e-34
