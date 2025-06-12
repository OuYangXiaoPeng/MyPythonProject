import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd

# 避免中文乱码
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.size'] = 12
matplotlib.rcParams['axes.unicode_minus'] = False


# 均价积柱状图
def chart_bar_price(a, b):
    # 第一步，创建画板
    plt.figure()

    # 第二步，在画布上画图
    plt.title('均价积柱状图')
    plt.bar(a, b, color=['r', 'b', 'g', 'y'])
    plt.xlabel('地区')
    plt.ylabel('均价')
    plt.ylim(0, 13000)
    plt.xlim(-0.9, 4)

    for x, y in enumerate(b):
        plt.text(x, y + 100, str(y) + '元', ha='center')

    # 第三步，需要在操作系统上显示
    plt.show()


# 平均面积柱状图
def chart_bar_area(a, b):
    # 第一步，创建画板
    plt.figure()

    # 第二步，在画布上画图
    plt.title('平均面积柱状图')
    plt.bar(a, b, color=['r', 'b', 'g', 'y'])
    plt.xlabel('地区')
    plt.ylabel('平均面积')
    plt.ylim(0, 150)
    plt.xlim(-0.9, 4)

    for x, y in enumerate(b):
        plt.text(x, y + 2, str(y) + "平米", ha='center')

    # 第三步，需要在操作系统上显示
    plt.show()


if __name__ == "__main__":
    # 读取初步清洗后的数据
    data = pd.read_csv("../data/初步清洗.csv")

    #  常规清洗数据，去空值dropna,fillna(替换)，去重复值for,set,drop_duplicates，去异常值
    data.dropna(axis=0, how='any', inplace=True)  # 去空值   # axis 0：行来找，1：列来找
    data.drop_duplicates('标题', keep='first', inplace=True)  # 去重复值

    # 对需要数组计算的列转变数据类型/
    data['单价'] = data['单价'].str.replace(",", "")
    data['单价'] = data['单价'].str.replace("元/平", "").astype(int)

    data['总价'] = data['总价'].str.replace("万", "").astype(float)
    data['面积'] = data['面积'].str.replace("平米", "").astype(float)
    # print(data['总价'])

    # 挑选总价数据，满足100-120
    TotalPrice = data[(data['总价'] >= 100) & (data['总价'] <= 120)]
    print("筛选后的总价数据：")
    print(TotalPrice['总价'])

    # 分组统计
    data = data.groupby('地区')
    price = data['单价'].mean().round(2)  # 单价平均值
    area = data['面积'].mean().round(2)  # 面积平均值
    # print(data)

    x = price.index
    y = price.values

    x1 = area.index
    y1 = area.values

    # chart_bar_price(x, y)#均价图
    chart_bar_area(x1, y1)  # 平均面积图
