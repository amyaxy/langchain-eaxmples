# 定义一个函数来计算两个数字的加减乘除并判断它们的大小关系
def calculate_and_compare(a, b):
    # 计算和
    sum_result = a + b
    # 计算差
    diff_result = a - b
    # 计算积
    prod_result = a * b
    # 计算商
    if b != 0:
        div_result = a / b
    else:
        div_result = None

    # 打印计算结果
    print(f"{a} + {b} = {sum_result}")
    print(f"{a} - {b} = {diff_result}")
    print(f"{a} * {b} = {prod_result}")
    if div_result is not None:
        print(f"{a} / {b} = {div_result}")
    else:
        print("除数不能为零")

    # 比较两个数字的大小
    if a > b:
        print(f"{a} 大于 {b}")
    elif a < b:
        print(f"{a} 小于 {b}")
    else:
        print(f"{a} 等于 {b}")


# 从用户获取输入
try:
    num1 = float(input("请输入第一个数字: "))
    num2 = float(input("请输入第二个数字: "))

    # 调用函数进行计算和比较
    calculate_and_compare(num1, num2)
except ValueError:
    print("请输入有效的数字")
