import matplotlib
matplotlib.use('TkAgg')
import pandas as pd
import matplotlib.pyplot as plt

# 避免中文乱码
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.size'] = 12
matplotlib.rcParams['axes.unicode_minus'] = False

# 读取频道数据
df = pd.read_excel("channel_data.xlsx")
fig, ax1 = plt.subplots()

ax1.bar(df["频道名称"], df["观看次数"], color='skyblue', label="观看次数")
ax1.set_xlabel("频道名称")
ax1.set_ylabel("观看次数", color='skyblue')
ax1.tick_params(axis='y', labelcolor='skyblue')

ax2 = ax1.twinx()
ax2.plot(df["频道名称"], df["观看时长"], color='orange', marker='o', label="观看时长")
ax2.set_ylabel("观看时长（分钟）", color='orange')
ax2.tick_params(axis='y', labelcolor='orange')

plt.title("频道观看次数与观看时长对比图")
plt.xticks(rotation=45)
fig.tight_layout()
plt.show()
