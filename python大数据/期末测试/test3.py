import pandas as pd

data = pd.read_excel("grade1.xlsx")
data.drop(data.columns[0], axis=1, inplace=True)
gre = data.sort_values(by="成绩",ascending=False)
# print(gre)

# 取各学生成绩
gr1 = gre[gre["姓名"] == "小红"]
gr2 = gre[gre["姓名"] == "小明"]
gr3 = gre[gre["姓名"] == "小张"]
gr4 = gre[gre["姓名"] == "小王"]
# print(gr1)
# print(gr2)
# print(gr3)
# print(gr4)

# M1 = gr1.drop(columns=["姓名"]).mean(axis=1).values[0]
# M2 = gr2.drop(columns=["姓名"]).mean(axis=1).values[0]
# M3 = gr3.drop(columns=["姓名"]).mean(axis=1).values[0]
# M4 = gr4.drop(columns=["姓名"]).mean(axis=1).values[0]
# print("小红平均分:", M1)
# print("张明平均分:", M2)
# print("小江平均分:", M3)
# print("小李平均分:", M4)
