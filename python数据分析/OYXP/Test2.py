import csv

import numpy as np

# 2
iris_data = []
with open('iris.csv', 'r') as csvfile:
    # 使用csv.reader 读取csvfile中的文件
    csv_reader = csv.reader(csvfile)
    # 读取第一行个标题
    birth_header = next(csv_reader)
    # 将csv文件中的数据保存到birth_data中
    for row in csv_reader:
        iris_data.append(row)

# 3
iris_list = []
for row in iris_data:
    iris_list.append(tuple(row))
# print(iris_list)

# 4.1
datatype = np.dtype([("Sepal.Length",np.str_,40),
                     ("Sepal.Width",np.str_,40),
                     ("Petal.Length",np.str_,40),
                     ("Petal.Width",np.str_,40),
                     ("Species",np.str_,40),
                     ])
# print(datatype)

#4.2
iris_data = np.array(iris_list, dtype=datatype)
print(iris_data)

#4.3
PetalLength = iris_data["Petal.Length"].astype(float)
# print(PetalLength)

#4.4
# print(np.sort(PetalLength))

#4.5
# print(np.unique(PetalLength))

#4.6
# print("求和:",np.sum(PetalLength))
# print("均值:",np.mean(PetalLength))
# print("标准差:",np.std(PetalLength))
# print("方差:",np.var(PetalLength))
# print("最小值:",np.min(PetalLength))
# print("最大值:",np.max(PetalLength))
