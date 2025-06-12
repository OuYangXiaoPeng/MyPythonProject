import numpy as np
import pandas as pd

data = pd.read_csv("../data/datafile.csv", encoding='gbk')


# a = data.groupby('性别').sum()
# b = data.groupby('性别').mean()
# print(a[['身高','体重']])
# print(b[['身高','体重']])
# print(data.groupby('性别').agg((np.std,np.mean))[['身高','体重']])

# print(data.dtypes)
# # 数据透视表
# a = pd.pivot_table(data[['Unnamed: 0', '性别', '年龄', '身高']],
#                    index=['Unnamed: 0'],
#                    values='年龄',
#                    aggfunc=np.sum)
#


# 离差标准化[0,1]
# def MinMaxScaler(data):
#     data = (data - data.min()) / (data.max()-data.min())
#     return data

# 标准差标准化
# def StandardScaler(data):
#     data = (data - data.mean()) / data.std()
#     return data

# 小数标准化[-1,1)
# def DecimalScaling(data):
#     data = data / 10 ** np.ceil(np.log10(data.abs().max()))
#     return data


#
# data1 = MinMaxScaler(data['年龄'])
# data2 = MinMaxScaler(data['身高'])
# print(data1)
# print

def DecimalScaler(data):
    data = data / 10 ** np.ceil(data.log10(data.abs().max()))
    return data

# 哑元变量
# get_dummies
# cut
