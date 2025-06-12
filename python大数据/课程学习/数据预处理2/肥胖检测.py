import numpy测试 as np
import pandas as pd

data = pd.read_csv("../data/datafile.csv", encoding='gbk')


# print(data.head())

# 找出异常值，并把异常值处理成空值，求出异常值索引  体重
# 异常值
# 1. 下标法找异常值,挑选数据
# index_f = (data['体重'] < 0) | (data['体重'] > 200)
# data['体重'][index_f] = np.nan
# print(data['体重'])

# 根据经验
# 2. 用3σ(fai)法
def A(a):
    b = a.mean() - 3 * a.std()
    c = a.mean() + 3 * a.std()
    index_t = (b <= a) & (a <= c)
    data['体重'] = data['体重'][index_t]
    # 异常值，就是数据为假的索引
    index_f = (b > a) | (a > c)
    index_m = np.arange(len(a))[index_f]  # 找到异常值的行的index
    return index_m


m = A(data['体重'])
print(m)
# print(data['体重'])

# 把体重这一列的空值  全部用线性插值法进行预测
from scipy.interpolate import interp1d

# 相似度
rep = data.corr().abs()['体重'].sort_values()
# print(rep)

# 通过相似度计算后，把最相关的一列拿过来最为x
x_train = data['肥胖等级'][20:200]
y_train = data['体重'][20:200]
LinearInsValue1 = interp1d(x_train, y_train, kind='linear')
x_test = data['肥胖等级'][m]
print('预测后值：', LinearInsValue1(x_test))