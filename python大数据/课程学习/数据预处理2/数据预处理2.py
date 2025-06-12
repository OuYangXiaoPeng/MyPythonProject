import numpy测试 as np
import pandas as pd

data = pd.read_csv("../data/台北房产数据集.csv")
# 1.替换法   mean()平均值，median()中位数，mode()众数
# mode = data['X4 附近便利店家数'].mode()[0]
# data['X4 附近便利店家数'].fillna(mode, inplace=True)  # 空值填充为一个value值，method='bfill'用下一个非空值来填充，'ffill'用上一个非空值来填充
# print(data)

# 2.线性插值法
from scipy.interpolate import interp1d

# 相似度corr()
rep = data.corr()['X4 附近便利店家数'].abs().sort_values()
print(rep)

# 相似度高的作为x
x_train = data['X3 最近公交站距离'][100:300]
y_train = data['X4 附近便利店家数'][100:300]

a = interp1d(x_train, y_train, kind='linear')  # 当数据足够，得到一个线性方程
index_data = np.arange(data['X3 最近公交站距离'].shape[0])[
    (data['X3 最近公交站距离'] == 306.5947) | (data['X3 最近公交站距离'] == 623.4731)]
# print(index_data)
b = a([306.5947, 623.4731])  # 用线性方程求的
for i in range(len(index_data)):
    data['X4 附近便利店家数'][index_data[i]] = b[i]


# print(b)
# j = 0
# for i in range(len(data['X4 附近便利店家数'])):
#     if pd.isna(data['X4 附近便利店家数'][i]):
#         # print(j)
#         data['X4 附近便利店家数'][i] = b[j]
#         j += 1


# print(data['X4 附近便利店家数'])

# 异常值
# 1. 下标法找异常值,挑选数据
# c = (data['X4 附近便利店家数'] >= 0) & (data['X4 附近便利店家数'] <= 5)
# print(data['X4 附近便利店家数'][c])

# 2. 用3σ(fai)法
# m = data['X4 附近便利店家数'].mean().round(2)
# s = data['X4 附近便利店家数'].std().round(2)


def outRange(Ser1):
    boolInd = (Ser1.mean() - 3 * Ser1.std() > Ser1) | (Ser1.mean() + 3 * Ser1.std() < Ser1)
    index = np.arange(Ser1.shape[0])[boolInd]  # 找到异常值的行的index
    for i in range(len(index)):
        Ser1[index] = np.nan
    # outrange = Ser1.iloc[index]
    return Ser1, index

outlier, index = outRange(data['X4 附近便利店家数'])
# print(outlier)

# 把异常值找到后，替换成空值，删除，替换，插值
# 用线性插值法
x_train = data['X3 最近公交站距离'][100:200]
y_train = data['X4 附近便利店家数'][100:200]
a = interp1d(x_train, y_train, kind='linear')  # 当数据足够，得到一个线性方程
# print(index_data)
x1 = data['X3 最近公交站距离'][index[0]]
x2 = data['X3 最近公交站距离'][index[1]]
b = a([x1, x2])  # 用线性方程求的
j = 0
for i in index:
    outlier[i] = b[j]
    j += 1

print(outlier[280:300])
