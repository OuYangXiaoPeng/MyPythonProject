import matplotlib
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge, BayesianRidge, Lasso, LogisticRegression
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, explained_variance_score
from sklearn.model_selection import train_test_split

matplotlib.use('TkAgg')

plt.rcParams['font.sans-serif'] = ['KaiTi', 'SimHei', 'FangSong']
plt.rcParams['font.size'] = 12
plt.rcParams['axes.unicode_minus'] = False

# 读数据
data = pd.read_excel("datafile.xlsx")

# 处理异常值
def outRange(Ser1):
    boolInd = (Ser1.mean() - 3 * Ser1.std() > Ser1) | (Ser1.mean() + 3 * Ser1.std() < Ser1)
    index = np.arange(Ser1.shape[0])[boolInd]
    for i in index:
        Ser1[i] = np.nan
    return Ser1, index

# 数据预处理
cols = data.columns[1:]
for col in cols:
    data[col] = data[col].astype(str).replace("NA.0", np.nan).astype(float)
    data[col] = outRange(data[col])[0]
    data[col].fillna(data[col].mean(), inplace=True)

data = data.iloc[:, 1:]

# 标准化数据
std_mod = (data - data.mean()) / data.std()
train_std_mod, test_std_mod = train_test_split(std_mod, test_size=2/3, random_state=10)

# 定义特征和目标变量
features = ['体重', '家族肥胖史', '是否吃零食', '年龄', '经常吃高热量食物', '喝酒的频率', '身高']
target = ['肥胖等级']

train_x, train_y = train_std_mod[features], train_std_mod[target]
test_x, test_y = test_std_mod[features], test_std_mod[target]

# 预测结果可视化
def broken_line(y_real, y_pred, title):
    plt.figure()
    plt.plot(y_real, color='r', marker='o', label='真实数据')
    plt.plot(y_pred, color='b', marker='*', label='预测数据')
    plt.xlabel('样本索引')
    plt.ylabel('肥胖等级')
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.show()

# 1. 线性回归
linear_reg = LinearRegression()
linear_reg.fit(train_x, train_y)
linear_pred = linear_reg.predict(test_x)
broken_line(test_y[1:10].values.flatten(), linear_pred[1:10].flatten(), '线性回归预测')

# 2. 正则化线性回归 (Ridge & Lasso)
ridge = Ridge(alpha=1.0)
ridge.fit(train_x, train_y)
ridge_pred = ridge.predict(test_x)
broken_line(test_y[1:10].values.flatten(), ridge_pred[1:10].flatten(), 'Ridge 正则回归预测')

lasso = Lasso(alpha=0.1)
lasso.fit(train_x, train_y)
lasso_pred = lasso.predict(test_x)
broken_line(test_y[1:10].values.flatten(), lasso_pred[1:10].flatten(), 'Lasso 回归预测')

# 3. 贝叶斯线性回归
bayes_ridge = BayesianRidge()
bayes_ridge.fit(train_x, train_y)
bayes_pred = bayes_ridge.predict(test_x)
broken_line(test_y[1:10].values.flatten(), bayes_pred[1:10].flatten(), '贝叶斯 Ridge 回归预测')

# 4. 支持向量机回归 (SVR)
svr = SVR(kernel='rbf', C=100, gamma=0.1, epsilon=0.1)
svr.fit(train_x, train_y.values.ravel())
svr_pred = svr.predict(test_x)
broken_line(test_y[1:10].values.flatten(), svr_pred[1:10].flatten(), '支持向量机 (SVR) 预测')

# 5. 随机森林回归
rf = RandomForestRegressor(n_estimators=100, random_state=10)
rf.fit(train_x, train_y.values.ravel())
rf_pred = rf.predict(test_x)
broken_line(test_y[1:10].values.flatten(), rf_pred[1:10].flatten(), '随机森林回归预测')


# 计算模型评分
models = {
    "Linear Regression": linear_reg,
    "Ridge Regression": ridge,
    "Lasso Regression": lasso,
    "Bayesian Ridge Regression": bayes_ridge,
    "SVR": svr,
    "Random Forest": rf,
}

for name, model in models.items():
    score = model.score(test_x, test_y)

    print(f"{name} 模型评分:", score)
    print(f"{name} mean_absolute_error:", mean_absolute_error(test_y, model.predict(test_x)))
    print(f"{name} explained_variance_score:", explained_variance_score(test_y, model.predict(test_x)))
    print("-" * 50)
