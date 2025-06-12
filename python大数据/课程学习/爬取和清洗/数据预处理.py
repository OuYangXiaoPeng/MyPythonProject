# 读取初步清洗后的数据
import numpy as np
import pandas as pd

# detail = pd.read_csv("../data/detail.csv", encoding='gbk')

# 一、重复值处理
# 1.定义函数去重
# def delRep(list1):
#     list2 = []
#     for i in list1:
#         if i not in list2:
#             list2.append(i)
#     return list2


# 去重
# dishes = detail['dishes_name']  # 将dishes_name从数据中提取出来
# print('去重前菜品总数为：', len(dishes))
# dish = delRep(dishes)  # 使用自定义函数去重
# print('方法一去重前菜品总数为：', len(dish))
# print()

# 方法二
# print('去重前菜品总数为：', len(dishes))
# dish_set = set(dish)
# print('方法二去重前菜品总数为：', len(dish_set))
# print()

# 方法三
# dishes_name = detail['dishes_name'].drop_duplicates()
# print(dishes_name)
# print(detail.drop_duplicates('dishes_name', keep='last'))
# print('drop_duplicates方法去重之后菜品总数为：', len(dishes_name))
# print()

# 二、空值处理，删除法；替换法；插值法
# print(detail.isnull().sum())
# 删除法
# detail.dropna(axis=0, how='any', inplace=True)  # any:一个为空就删，all:全部为空才删
# print(detail)

# 替换法   mean()平均值，median()中位数，mode()众数
# data_mean = detail['amounts'].mode()[0]
# detail['amounts'].fillna(data_mean, inplace=True)  # 空值填充为一个value值，method='bfill'用下一个非空值来填充，'ffill'用上一个非空值来填充
# print(detail['amounts'].head(10))

# 插值法，线性插值法，多项式插值法（拉格朗日，牛顿），抽样插值法
from scipy.interpolate import interp1d,lagrange

# x = np.array([1, 2, 3, 4, 5, 8, 9, 10])  # 创建自变量x
# y1 = np.array([2, 8, 18, 32, 50, 128, 162, 200])  # 创建因变量y1
# y2 = np.array([3, 5, 7, 9, 11, 17, 19, 21])  # 创建因变量y2
#
# LinearInsValue1 = interp1d(x, y1, kind='linear')
# LinearInsValue2 = interp1d(x, y2, kind='linear')
#
# print('当x为6,7时，使用线性插值y1为', LinearInsValue1([6, 7]))
# print('当x为6,7时，使用线性插值y2为', LinearInsValue2([6, 7]))

data = pd.read_csv("../data/台北房产数据集.csv")
# 替换法   mean()平均值，median()中位数，mode()众数
# a = data['Y 单位面积房价'].mean()
# b = data['Y 单位面积房价'].median()
# c = data['Y 单位面积房价'].mode()[0]
# data['Y 单位面积房价'].fillna(c, inplace=True)  # 空值填充为一个value值，method='bfill'用下一个非空值来填充，'ffill'用上一个非空值来填充
# print(data['Y 单位面积房价'].head(10))

# 相似度
rep = data.corr().abs()['Y 单位面积房价'].sort_values()
# print(rep)

# 通过相似度计算后，把最相关的一列拿过来最为x
x_train = data['X3 最近公交站距离'][20:400].values
y_train = data['Y 单位面积房价'][20:400].values

LinearInsValue1 = interp1d(x_train, y_train, kind='linear')
x_test = data['X3 最近公交站距离'][2:8]
x_test = np.array(x_test)
# print(data['Y 单位面积房价'][2:8])
# print('预测后值：', LinearInsValue1(x_test))


x_train = np.array(x_train)
y_train = np.array(y_train)
LargeInsValue2 = lagrange(x_train, y_train)
print(LargeInsValue2(x_test))