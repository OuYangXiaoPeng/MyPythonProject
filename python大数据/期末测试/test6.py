import numpy as np
from sklearn.preprocessing import StandardScaler
data = np.load("data.npy", allow_pickle=True)
# 因为原来的数据集中包含字符串列不能进行均值-方差规范化处理，所以我这里切片出对数值型列处理
data_num = data[:, [0, 2, 3]].astype(float)
scaler = StandardScaler()
normalized_data = scaler.fit_transform(data_num)
print(normalized_data)

