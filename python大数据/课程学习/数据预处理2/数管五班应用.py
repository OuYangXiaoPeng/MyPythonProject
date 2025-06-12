import pandas as pd

# DataFrame

data = pd.read_csv('../data/datafile.csv', encoding='gbk')
# 切片，三种方法，下标法，loc[列，行]，iloc[行的索引，列的索引]
# 1 切第二列到第五列，行的数据要求，年龄只要20-25岁的
# a = (data['年龄'] <= 25) & (data['年龄'] >= 20) & (data['年龄'] % 2 == 0)
# print(data[['性别', '年龄', '身高', '体重']][a])

# 2 loc 行的编号是3和5的公倍数，列表推导式
# b = data.loc[[i for i in range(len(data)) if (i % 3 == 0) and (i % 5 == 0)], ['性别', '年龄', '身高', '体重']]
# b = data.loc[(data['体重'] <= 130) & (data['体重'] >= 100) & (data['年龄'] == 21), ['性别', '年龄', '身高', '体重']]
# print(b)

# 3 iloc
# print(data.iloc[[3,4,5,9],1:5])

# drop() 删除
# print(data.drop(labels=[i for i in range(len(data)-100)],axis=0))
# print(data.drop(columns=['性别', '年龄', '身高', '体重'], axis=1))

# describe
print(data.describe())
print(data.quantile(1))
