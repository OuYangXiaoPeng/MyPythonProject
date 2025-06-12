import matplotlib
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, explained_variance_score
from sklearn.model_selection import train_test_split

matplotlib.use('TkAgg')

plt.rcParams['font.sans-serif'] = ['KaiTi', 'SimHei', 'FangSong']
plt.rcParams['font.size'] = 12
plt.rcParams['axes.unicode_minus'] = False

# 读数据
data = pd.read_excel("datafile.xlsx")


# print(data.head(10))
# print(data.tail(10))
# print(data.dtypes)
# print(data.info)
# print(data.describe().T)


# print(data['体重'])

# 3Q处理异常值，将其换为np.nan
def outRange(Ser1):
    boolInd = (Ser1.mean() - 3 * Ser1.std() > Ser1) | (Ser1.mean() + 3 * Ser1.std() < Ser1)
    index = np.arange(Ser1.shape[0])[boolInd]  # 找到异常值的行的index
    for i in index:
        Ser1[i] = np.nan
    # outrange = Ser1.iloc[index]
    return Ser1, index


# 测试单个列
# d = data['体重']
# d = outRange(d)[0]
# d.fillna(d.mean(), inplace=True)
# print(d)

# 获取表格头
cols = data.columns[1:]
# print(cols)
# 用平均值填充空值
for col in cols:
    data[col] = data[col].astype(str)
    data[col] = data[col].replace("NA.0", np.nan)
    data[col] = data[col].astype(float)

    data[col] = outRange(data[col])[0]
    data[col].fillna(data[col].mean(), inplace=True)
# print(data.isnull().sum())  # 查看空值

data = data.iloc[:, 1:]
# print(data.dtypes)
# print(data.corr()['肥胖等级'].abs())

# 数据标准化,离差
# std_mod = StandardScaler().fit_transform(data)
# print(std_mod)

# 用自己写的公式计算后的数据仍然是二维表格（有列的名字）
std_mod = (data - data.mean()) / data.std()  # 标准差
# print(std_mod.dtypes)
train_std_mod, test_std_mod = train_test_split(std_mod, test_size=2 / 3, random_state=10)

# 自变量之间的相关性
sim = std_mod[['性别', '年龄', '身高', '体重', '家族肥胖史', '经常吃高热量食物', '是否吃零食', '多久进行体育锻炼',
               '每天使用电子设备', '喝酒的频率', '通常使用交通工具', '肥胖等级']].corr()['肥胖等级'].abs().sort_values()
# print(sim)

# 解释变量数据间的相关性，以热力图表现
# plt.figure(figsize=(14,14))
# sns.heatmap(sim,annot=True,vmax=1,square=True)
# plt.show()

train_std_mod_x = train_std_mod[['体重', '家族肥胖史', '是否吃零食', '年龄', '经常吃高热量食物', '喝酒的频率', '身高']]
train_std_mod_y = train_std_mod[['肥胖等级']]
test_std_mod_x = test_std_mod[['体重', '家族肥胖史', '是否吃零食', '年龄', '经常吃高热量食物', '喝酒的频率', '身高']]
test_std_mod_y = test_std_mod[['肥胖等级']]


# 1.线性回归LinearRegression预测
LR = LinearRegression()
LR.fit(train_std_mod_x, train_std_mod_y)
prd_y = LR.predict(test_std_mod_x)
# print("预测的值",prd_y[1:10])
# print("真实的值",test_std_mod_y[1:10])
print("模型评分:", LR.score(test_std_mod_x, test_std_mod_y))
print("mean_absolute_error评分:",mean_absolute_error(test_std_mod_y,prd_y))
print("explained_variance_score评分:",explained_variance_score(test_std_mod_y,prd_y))

# Regularized Linearn Models
# model2 = Ridge(alpha=1, solver="cholesky")
# model2.fit(x_train, y_train)
# pre2 = model2.predict(x_test)
# print("相关性:", model2.coef_)
# print("截距:", model2.intercept_)
# print("拟合:", model2.score(x_test, y_test))
# print("*************************")
# plt.figure(figsize=(5, 5))
# sns.regplot(x=y_test, y=pre2)

# BayesianRidge
# model3 = BayesianRidge()
# model3.fit(x_train, y_train)
# pre3 = model3.predict(x_test)
# print("相关性:", model3.coef_)
# print("截距:", model3.intercept_)
# print("拟合:", model3.score(x_test, y_test))
# print("*************************")
# plt.figure(figsize=(5, 5))
# sns.regplot(x=y_test, y=pre3)

# Lasso回归
# model4 = Lasso(alpha=0.2)
# model4.fit(x_train, y_train)
# pre4 = model4.predict(x_test)
# print("相关性:", model4.coef_)
# print("截距:", model4.intercept_)
# print("拟合:", model4.score(x_test, y_test))
# print("**************************")
# plt.figure(figsize=(5, 5))
# sns.regplot(x=y_test, y=pre4)

# SVR 向量机
# model5 = SVR(kernel='rbf', C=10, gamma=0.01)
# model5.fit(x_train, y_train)
# pre5 = model5.predict(x_test)
# print("截距:", model5.intercept_)
# print("拟合:", model5.score(x_test, y_test))
# print("***********************")
# plt.figure(figsize=(5, 5))
# sns.regplot(x=y_test, y=pre5)

# RandomForestRegressor 随机森林回归模型
# model6 = RandomForestRegressor(n_estimators=100)
# model6.fit(x_train, y_train)
# pre6 = model6.predict(x_test)
# print("拟合:", model6.score(x_test, y_test))
# print("***********************")
# plt.figure(figsize=(5, 5))
# sns.regplot(x=y_test, y=pre6)

# 调用sklearn中逻辑回归模块
# from sklearn import linear_model

#
# Lmodel1 = linear_model.LogisticRegression()
# 拟合
# Lmodel1.fit(x_train, y_train)
# print(Lmodel1.coef_)
# print(Lmodel1.intercept_)
# # 通过训练集和测试集的自变量x，分别计算出对应的预测值
# y_pred_train = Lmodel1.predict(x_train)
# y_pred_test = Lmodel1.predict(x_test)
# 搭建训练集混淆矩阵
# from sklearn import metrics

#
# metrics.confusion_matrix(y_train, y_pred_train)
# 查看训练集准确率
# print(metrics.accuracy_score(y_train, y_pred_train))
# 搭建测试集混淆矩阵
# metrics.confusion_matrix(y_test, y_pred_test)
# 查看测试集准确率
# print(metrics.accuracy_score(y_test, y_pred_test))

# final = []


# def jy(name, y_test, pre):
# r2 = name.score(x_test, y_test)
# n = x_test.shape[e]
# m = x_test.shape[1]
# name_adjusted_r2 = 1 - (1 - r2) * (n - 1) / (n - m - 1)
# name_RMSE = np.sqrt(metrics.mean_squared_error(y_test, pre))
# name_R2 = name.score(x_test, y_test)
# name_mae = mean_absolute_error(y_test, pre)
# name_mse = MSE(pre, y_test)
# mess = {'均方误差': MSE(pre, y_test), '校正决定系数': name_adjusted_r2, '均方根误差': name_RMSE,
#         '决定系数': name_R2, '平均绝对误差': name_mae}
# return mess


# a = jy(model1, y_test, pre1)
# final.append(a)
# b = jy(model2, y_test, pre2)
# final.append(b)
# c = jy(model3, y_test, pre3)
# final.append(c)
# d = jy(model4, y_test, pre4)
# final.append(d)
# e = jy(model5, y_test, pre5)
# final.append(e)
# f = jy(model6, y_test, pre6)
# final.append(f)
# messes = pd.DataFrame(final, columns=['均方误差', '校正决定系数', '均方根误差', '决定系数', '平均绝对误差'])
# messes.index = ["Linearn", "Regularized Linearn Models", "BayesianRidge", "Lasso", "SvR", "RandomForestRegressor"]
# messes.to_excel("误差分析.xlsx")

# 模型检验
# import statsmodels.api as sm
#
# X2 = sm.add_constant(x_train)
# print(X2.head(5))
# est = sm.OLS(y_train, X2).fit()
# print(est.summary())

# 报告回归结果
# LinearRegression
# fig = plt.figure(figsize=(20, 6))
# pred1 = model1.predict(x_test)
# plt.plot(range(y_test.shape[0]), y_test, color="blue", linewidth=1.6, linestyle="-")
# plt.plot(range(y_test.shape[0]), pred1, color="red", linewidth=1.6, linestyle="--")
# plt.legend(['real values', 'predict values'])
# plt.show()

# Regularized Linearn Models
# fig = plt.figure(figsize=(20, 6))
# pred2 = model2.predict(x_test)
# plt.plot(range(y_test.shape[0]), y_test, color="blue", linewidth=1.6, linestyle="-")
# plt.plot(range(y_test.shape[0]), pred2, color="red", linewidth=1.6, linestyle="--")
# plt.legend(['real values', 'predict values'])
# plt.show()

# BayesianRidge
# fig = plt.figure(figsize=(20, 6))
# pred3 = model3.predict(x_test)
# plt.plot(range(y_test.shape[0]), y_test, color="blue", linewidth=1.6, linestyle="-")
# plt.plot(range(y_test.shape[0]), pred3, color="red", linewidth=1.6, linestyle="--")
# plt.legend(['real values', 'predict values'])
# plt.show()

# Lasso
# fig = plt.figure(figsize=(20, 6))
# pred4 = model4.predict(x_test)
# plt.plot(range(y_test.shape[0]), y_test, color="blue", linewidth=1.6, linestyle="-")
# plt.plot(range(y_test.shape[0]), pred4, color="red", linewidth=1.6, linestyle="--")
# plt.legend(['real values', 'predict values'])
# plt.show()

# SVR
# fig = plt.figure(figsize=(20, 6))
# pred5 = model5.predict(x_test)
# plt.plot(range(y_test.shape[0]), y_test, color="blue", linewidth=1.6, linestyle="-")
# plt.plot(range(y_test.shape[0]), pred5, color="red", linewidth=1.6, linestyle="--")
# plt.legend(['real values', 'predict values'])
# plt.show()

# RandomForestRegressor
# fig = plt.figure(figsize=(20, 6))
# plt.plot(range(y_test.shape[0]), y_test, color="blue", linewidth=1.6, linestyle="-")
# plt.plot(range(y_test.shape[0]), pre6, color="red", linewidth=1.6, linestyle="--")
# plt.legend(['real', 'predict'])
# plt.show()

# 根据模型产生的均方误差降序排列
# f, axe = plt.subplots(figsize=(28, 4))
# messes.sort_values(by=['均方误差'], ascending=False, inplace=True)
# sns.barplot(x='均方误差', y=messes.index, data=messes, ax=axe)
# axe.set_xlabel('均方误差', size=14)
# axe.set_ylabel('模型', size=14)
# axe.set_xlim(0.1, 0.6)
# plt.show()

# 根据模型的平均绝对误差升序排列
# f, axe = plt.subplots(figsize=(28, 4))
# messes.sort_values(by=['平均绝对误差'], ascending=True, inplace=True)
# sns.barplot(x='平均绝对误差', y=messes.index, data=messes, ax=axe)
# axe.set_xlabel('平均绝对误差', size=14)
# axe.set_ylabel('模型', size=14)
# axe.set_x1im(0.3, 0.7)
# plt.show()
