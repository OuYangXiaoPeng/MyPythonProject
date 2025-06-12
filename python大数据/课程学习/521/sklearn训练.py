from sklearn.datasets import load_iris,load_breast_cancer
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler, Normalizer, OrdinalEncoder, Binarizer,FunctionTransformer,OneHotEncoder
from sklearn.model_selection import train_test_split # 测试训练切片
from sklearn.decomposition import PCA # 降维
PCA(n_components=5)

# 产生一个数据集，分类，聚集
cancer = load_breast_cancer()

# 标准差标准化[-1,1]
# def StandardScaler(data):
#     data = (data - data.mean()) / data.std()
#     return data


# 切割
# a = StandardScaler(cancer['data'])
train_data, test_data = train_test_split(cancer['data'], train_size=0.8, random_state=10)
# print(len(train_data))
# print(len(test_data))

Scaler = MinMaxScaler().fit_transform(train_data)  # 生成规则
print(Scaler)
Scaler2 = StandardScaler().fit_transform(train_data)  # 生成规则
print(Scaler2)
Scaler3 = Normalizer().fit_transform(train_data)  # 生成规则
print(Scaler3)
Scaler4 = Binarizer().fit_transform(train_data)  # 生成规则
print(Scaler4)
Scaler5 = OrdinalEncoder().fit_transform(train_data)  # 生成规则
print(Scaler5)
Scaler6 = OneHotEncoder().fit_transform(train_data)  # 生成规则
print(Scaler6)
Scaler7 = PCA(n_components=10).fit_transform(train_data)  # 生成规则
print(Scaler7)




# 将规则应用与训练集
# cancer_trainScaler = Scaler.transform(train_data)
# print(cancer_trainScaler)

