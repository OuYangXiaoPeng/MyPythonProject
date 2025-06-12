# # 读取数据
# data = pd.read_csv("../data/data.csv")
# X = data.iloc[:,1:3]
# print(X)
# # from sklearn.metrics import fowlkes_mallows_score
# a=KMeans(n_clusters=5)  #a变量就相当于创建了一个聚类模型，该模型指数或者系数都是未知
# b=a.fit(X)  #b变量相当于有了确定的系数值的聚类方程 X1  X2
# c=b.transform(X)  #c就相当于聚类方程中带入x所求出来的y值
# # kmeans = KMeans(n_clusters = 5).fit_transform(X)
#
# print(c)
import matplotlib
import matplotlib.pyplot as plt
from sklearn.metrics import fowlkes_mallows_score,adjusted_mutual_info_score,adjusted_rand_score,calinski_harabasz_score

matplotlib.use('TkAgg')
import pandas as pd
from sklearn.cluster import KMeans

# 读取数据
data = pd.read_csv("../data/篮球.csv")
X = data.iloc[:, 1:]
print(X)

# K-means聚类
clf = KMeans(n_clusters=5)  # 表示输出将数据集分成类簇数为5的聚类
# 输出聚类预测结果，对X聚类，20行数据，每个y_pred对应X的一行或一个孩子，聚成3类，类标为0、1、2
a = clf.fit(X)
y_pred = a.predict(X)
print(y_pred)  # 输出结果





# x_pred = clf.fit_transform(X)
# print(x_pred)  # 输出结果

# x = X.iloc[:, 0]  # 获取第1列的值
# print(x)
# y = X.iloc[:, 1]  # 获取第2列的值
# print(y)
#
# # 可视化操作
# 绘制散点图（scatter），横轴为x，获取的第1列数据；纵轴为y，获取的第2列数据；
# c=y_pred对聚类的预测结果画出散点图，marker='o'说明用点表示图形
# plt.scatter(x, y, c=y_pred, marker='o')
# plt.title("Kmeans-Basketball Data")  # 表示图形的标题为Kmeans-heightweight Data
# plt.xlabel("assists_per_minute")  # 表示图形x轴的标题
# plt.ylabel("points_per_minute")  # 表示图形y轴的标题
# plt.legend(["Rank"])  # 设置右上角图例
# plt.show()  # 显示图形
score = adjusted_rand_score(clf.labels_,clf.labels_)
print(score)
score = fowlkes_mallows_score(clf.labels_,clf.labels_)
print(score)
score = calinski_harabasz_score(clf.labels_,clf.labels_)
print(score)
