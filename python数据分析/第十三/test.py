# list = ['a','b','c','d']
# list.append('Baidu')
# print("更新后列表:",list)
# print("更新后列表:{}".format(list))
#
# list = ['a', 'b', 'c', 'd']
# list.insert(1, 'BaiDu')
# print("列表插入元素后为:", list)
# print("列表插入元素后为:{}".format(list))

# list = ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'a', 'c']
# print("c的出现次数是:", list.count("c"))
# print("list中一共有%d个a" % list.count('a'))
#
# list = ['a', 'b', 'c', 'd']
# list.sort(reverse=True)
# print(list)

# import random
#
# total = []
# for i in range(30):  # 随机生成30个1~150之间的整数
#     total.append(random.randint(1, 150))
# print("列表:", total)
# sum = 0
# for item in total:  # 列表元素求和
#     sum += item
# total_m = sum // len(total)  # 计算列表均值
# print("新列表:", [x - total_m for x in total])  # 得到数值重新构建列表
