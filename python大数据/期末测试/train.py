import matplotlib
matplotlib.use('TkAgg')
import pandas as pd
import matplotlib.pyplot as plt

# 避免中文乱码
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.size'] = 12
matplotlib.rcParams['axes.unicode_minus'] = False

data = pd.read_excel("train_no.xlsx")

# 筛选出 D04 车次的数据
a = data[data["车次"] == "D04"]
plt.scatter(a["日期"], a["上车人数"])
plt.xticks(rotation=60)
plt.title("D04车次每日上车人数")
plt.xlabel("日期")
plt.ylabel("人数")
plt.tight_layout()
plt.show()

# 筛选 b 和 c 车次
b = data[data["车次"] == "D05"]
c = data[data["车次"] == "D06"]
plt.plot(b["日期"], b["上车人数"], 'yo--', label="D05")
plt.plot(c["日期"], c["上车人数"], 'yo--', label="D06")
plt.title("上车人数走势图")
plt.xlabel("日期")
plt.ylabel("人数")
plt.xticks(rotation=60)
plt.legend()
plt.tight_layout()
plt.show()

# 选出 D02~D06
subset = data[data["车次"].isin(["D02", "D03", "D04", "D05", "D06"])]
# 统计总上车人数
total = subset.groupby("车次")["上车人数"].sum()
plt.pie(total, labels=total.index, autopct='%1.1f%%')
plt.title("D02~D06同期上车人数分布")
plt.tight_layout()
plt.show()

