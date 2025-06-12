# svc向量机
# svr回归算法
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

dataset = pd.read_csv("../data/ods_bye_car_info.csv", encoding='gbk')
# print(dataset.head(10))
# print(dataset.info())
# print(dataset.describe())
# print(dataset[['buy_car_sign']].value_counts())

dataset = dataset.iloc[:,1:]
# print(dataset)
# a = OneHotEncoder()
encoder = OrdinalEncoder().fit_transform(dataset)
print(encoder)

te_array_deal = pd.DataFrame(encoder,columns=['age','gender','annual_income','marital_status','buy_car_sign'])
print(te_array_deal)
print(te_array_deal.corr()['buy_car_sign'].abs().sort_values())
