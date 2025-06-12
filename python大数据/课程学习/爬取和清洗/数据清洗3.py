import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd

# 避免中文乱码
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.size'] = 12
matplotlib.rcParams['axes.unicode_minus'] = False


def chart_barh(x, y):
    # 第一步，创建画板
    plt.figure()

    # 第二步，在画布上画图
    plt.title('热门户型')
    plt.barh(y, x, height=0.5, color=['r', 'b', 'g', 'y'], alpha=0.8)
    plt.xlim(0, 15000)
    plt.xlabel('均价')
    # plt.ylabel('均价')

    for a, b in enumerate(x):
        plt.text(b + 10, a, str(b) + '元', va='center')

    # 第三步，需要在操作系统上显示
    plt.show()


if __name__ == "__main__":
    # 读取初步清洗后的数据
    data = pd.read_csv("../data/初步清洗.csv")

    # 常规清洗数据，去空值dropna,fillna(替换)，去重复值for   not in; set集合;  drop_duplicates 去异常值
    data.dropna(axis=0, how='any', inplace=True)  # 去空值   # axis 0：行来找，1：列来找
    data.drop_duplicates('标题', keep='first', inplace=True)  # 去重复值

    # 对需要数组计算的列转变数据类型
    data['单价'] = data['单价'].str.replace(",", "")
    data['单价'] = data['单价'].str.replace("元/平", "").astype(int)

    # 分组统计
    data_g = data.groupby('户型').size()
    data_sort = data_g.sort_values(ascending=False)

    data_hot = data_sort.head(4)
    x = data_hot.index

    data_price = data.groupby('户型')['单价'].mean().round(2)
    y = data_price[x].values
    print(x)
    print(y)

    chart_barh(y, x)
