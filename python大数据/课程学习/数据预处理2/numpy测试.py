import numpy as np

# numpy的四个方向
# 1.清洗数据和预处理
# 2.数据统计和分析（mean,）
# 3.数据可视化
# 4.在机器学习中的应用

# a = [[1, "1111", 3.22, 4], [4, 5, "ggg", 7], [7, 8, 9, 10]]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(a)
# 1.array() 转换
# c = np.array(b).reshape(3, 3, 1)

# flatten平铺(可以按列)
# c = np.array(a)
# print(c)
# print(c.itemsize)

# 2.arange 要写步长
# c = np.arange(1, 50, 2).reshape(5, 5)
# print(c)

# 3.linspace 等分
# c = np.linspace(1, 10,20)
# print(c)

# 4.logspace 等比
# c = np.logspace(1, 10,20)
# print(c)

# 5.zeros
# c = np.zeros((4,5))
# print(c)

# 6.eye 几行几列，全为1
# c = np.eye(5)
# print(c)

# 7.diag
# c = np.diag([1, 2, 3, 4, 5, 6])
# print(c)

# 8.ones
# c = np.ones((3,6))
# print(c)

# 9.R
# a = np.random.randint(0, 10, 24).reshape(4, 6)
# c = np.random.randint(0, 99, 20).reshape(5, 4)
# print(a)
# print(np.repeat(a, 2, axis=1))
# print(np.mean(a))
# print(np.max(a))
# print(np.max(a, axis=0))

# print(np.sort(a))  # 排序 axis=0按列
# print(np.unique(a))  # 去重+降维成一维
# 保存为文本
# np.savetxt("../data/cc.csv", a, fmt="%d", delimiter=",")
# print(np.loadtxt("../data/cc.csv", delimiter=","))
# 保存为二进制
# np.savez("../data/aa.npy", a, c)
# d = np.load("../data/aa.npy.npz")
# for i in range(len(d)):
#     print(d['arr_{}'.format(i)])

# print(a + [5])
# print(np.any(a))

# print(c.ravel())  #
# print(c.flatten('F'))  # F列平铺，不加是行平铺
# b = np.split(a, 2, axis=1)  # split切割数组，行或者列要整除
# print(b[0])
# 合并数组，行合并，多个数组的列数量要相同，列合并，多个数组的行数量要相同
# print(np.concatenate((b[0], b[1]), axis=1))

# b = np.asmatrix(a)  # 矩阵
# d = np.asmatrix(c)
# print(b.T)

# a = np.random.randint(-1000, 1000, 100)
# print(a)
# b = (a <= 120) & (a >= 0)
# c = a[b]
# print(c)