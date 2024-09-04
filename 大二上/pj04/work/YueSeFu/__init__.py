print("请输入人数：")
n = int(input())
print("请输入报数数：")
k = int(input())
a = 0
b = 0
while n - a > 0:
    a = a + 1
    b = b + k
    while b - a > 0:
        b = b - a
print("活下来的人是第" + str(b) + "号")
