# while 循环示例
count = 0

while count < 5:
    print(count)
    count += 1
# 输出:
# 0
# 1
# 2
# 3
# 4


# 嵌套 for 循环
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
# 输出:
# i=0, j=0
# i=0, j=1
# i=1, j=0
# i=1, j=1
# i=2, j=0
# i=2, j=1


# 嵌套 while 循环
i = 0
while i < 3:
    j = 0
    while j < 2:
        print(f"i={i}, j={j}")
        j += 1
    i += 1
# 输出:
# i=0, j=0
# i=0, j=1
# i=1, j=0
# i=1, j=1
# i=2, j=0
# i=2, j=1


# break 示例
for i in range(5):
    if i == 3:
        break
    print(i)
# 输出:
# 0
# 1
# 2

# continue 示例
for i in range(5):
    if i == 3:
        continue
    print(i)
# 输出:
# 0
# 1
# 2
# 4

# pass 示例
for i in range(5):
    if i == 3:
        pass  # 这里可以放置以后需要的代码
    print(i)
# 输出:
# 0
# 1
# 2
# 3
# 4
