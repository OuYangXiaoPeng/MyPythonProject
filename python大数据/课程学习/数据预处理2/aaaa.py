import pandas as pd
import numpy as np
#1模拟数据
np.random.seed(42)
dates = pd.date_range("2023-01-01", "2023-03-31")
products = ["A", "B", "C"]
regions = ["North", "South", "East", "West"]
salespeople = ["Alice", "Bob", "Charlie", "David"]

data = {
    "Date": np.random.choice(dates, 1000),
    "Product": np.random.choice(products, 1000),
    "Region": np.random.choice(regions, 1000),
    "Salesperson": np.random.choice(salespeople, 1000),
    "Units_Sold": np.random.randint(1, 20, 1000),
    "Unit_Price": np.random.uniform(10, 50, 1000).round(2)
}
df = pd.DataFrame(data)
df["Total_Sales"] = df["Units_Sold"] * df["Unit_Price"]
#2基础透视表
# pivot1 = pd.pivot_table(
#     df,
#     values="Total_Sales",
#     index="Product",  #不同的值比较少
#     columns="Region",
#     aggfunc="sum",
#     fill_value=0
# )
# print(pivot1)
# #3多级索引与多聚合函数
# # 提取月份
# df["Month"] = df["Date"].dt.month_name()
#
# pivot2 = pd.pivot_table(
#     df,
#     values=["Total_Sales", "Units_Sold"],
#     index=["Product", "Salesperson"],
#     columns="Month",
#     aggfunc={
#         "Total_Sales": [np.mean, np.max],
#         "Units_Sold": np.sum
#     },
#     margins=True,  # 添加总计行/列
#     margins_name="Total"
# )
# print(pivot2)
#
# #4自定义聚合函数
# def q90(x):
#     return np.quantile(x, 0.9)
#
# pivot3 = pd.pivot_table(
#     df,
#     values="Total_Sales",
#     index="Region",
#     aggfunc=[np.median, q90]
# )
# print(pivot3)
# #5处理缺失值与多层列
pivot4 = pd.pivot_table(
    df,
    values=["Total_Sales", "Unit_Price"],
    index="Product",
    columns=[df["Date"].dt.month, df["Date"].dt.day],
    aggfunc={"Total_Sales": np.sum, "Unit_Price": np.mean},
    fill_value=0
)
print(pivot4.head())
#
# #6结合可视化
# import seaborn as sns
# import matplotlib.pyplot as plt
#
# # 按产品和地区统计销售额
# pivot_heatmap = pd.pivot_table(
#     df,
#     values="Total_Sales",
#     index="Product",
#     columns="Region",
#     aggfunc="sum"
# )
#
# plt.figure(figsize=(10,6))
# sns.heatmap(pivot_heatmap, annot=True, fmt=".0f", cmap="Blues")
# plt.title("Total Sales by Product and Region")
# plt.show()