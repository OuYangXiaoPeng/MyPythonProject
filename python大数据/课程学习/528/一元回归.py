import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR  # 向量机
from sklearn.linear_model import LinearRegression  # x线性
from sklearn.neighbors import KNeighborsRegressor

dataset = pd.read_csv("../data/ODS_PROV_GDP_TAX_INFO.csv", encoding='gb2312')

dataset = dataset.iloc[:, 1:]
dataset = (dataset - dataset.min()) / (dataset.max() - dataset.min())
x = dataset[['gdp_value']]
y = dataset[['tax_value']]
# print(type(x))
# print(type(y))
# print(type(z))

train_x, x_test, train_y, y_test = train_test_split(x, y, train_size=0.7, random_state=10)
model = SVR()
model.fit(train_x, train_y)
a = model.predict(x_test)
print(y_test)
print(a)
print("模型评分:", model.score(x_test, y_test))


