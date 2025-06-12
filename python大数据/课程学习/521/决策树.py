# 导入模块
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
from sklearn.tree import DecisionTreeClassifier


# 读数据
dataset = pd.read_csv('../data/ods_bye_car_info.csv', encoding='gbk')
# print(dataset.dtypes)
# print(dataset.head(10))
# print(dataset.info())
# print(dataset.describe())
# print(dataset[['buy_car_sign']].value_counts())
# 分析谁作为y 谁作为x 该模型按照那些项来创建
dataset = dataset.iloc[:, 1:]
# print(dataset)

# a=OrdinalEncoder() #引入公司，创建公式，公式里的系数，指数是未知
# b=a.fit(dataset) #求出公司的系数
# c=b.transform(dataset)
encoder = OrdinalEncoder().fit_transform(dataset)
# print(encoder)

# encoder1=OneHotEncoder().fit_transform(dataset)
# print(encoder1)
# # a=encoder.transform(dataset)
# # print(a)
# # dataset_Ord=encoder.transform(dataset)
# # # print(dataset_Ord)
te_array_deal = pd.DataFrame(encoder, columns=['age', 'gender', 'annual_income', 'marital_status', 'buy_car_sign'])
# print(te_array_deal)
# print(te_array_deal.corr()['buy_car_sign'].abs().sort_values())
# # # train_test_split()

x = te_array_deal[['age', 'gender', 'annual_income', 'marital_status']]
y = te_array_deal['buy_car_sign']
train_x, test_x, train_y, test_y = train_test_split(x, y, train_size=0.7, random_state=10)
# 标准化处理的动作
a = DecisionTreeClassifier()
b = a.fit(train_x,train_y)
c = b.predict(test_x)
print(c)
print(test_y)

