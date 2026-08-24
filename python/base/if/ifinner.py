# 嵌套条件语句示例
x = 15

if x > 10:
    print("x is greater than 10")  # 输出: x is greater than 10
    if x > 20:
        print("x is also greater than 20")
    else:
        print("x is not greater than 20")  # 输出: x is not greater than 20
else:
    print("x is 10 or less")
