import pandas as pd
data1 = pd.read_csv("data1.csv",encoding='gbk')
data2 = pd.read_csv("data2.csv",encoding='gbk')
merged = pd.merge(data1, data2, on="商品", how="left")
merged.to_excel("hb.xlsx", index=False)
print("合并完成，已保存为hb.xlsx")
