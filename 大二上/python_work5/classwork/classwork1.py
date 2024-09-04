# 长度len
# 角标index
# 切片
# 综合概念
photonumber="13778333602"
# 求长度：
print(len(photonumber))
print(photonumber[0])
print(photonumber[len(photonumber)-1])
print(photonumber[-1])
# 切片 --从当前数组中取出一个范围
# 137
# 3602
print(photonumber[0:3])
print(photonumber[7:11])
print(photonumber[7:])#冒号后取完
print(photonumber[:12])#取到12
phone="12121212"
print(phone[::1]==phone[0:])#步长
url1="https://www.baidu123mis.com"
print(url1[12:17])
print(phone[::])

