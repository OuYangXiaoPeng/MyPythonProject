import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd

# 避免中文乱码
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.size'] = 12
matplotlib.rcParams['axes.unicode_minus'] = False


def chart_pie(x, y):  # x传的是中间饼图计算百分比的值，y是饼图外面一圈的标签
    # 第一步，创建画板
    plt.figure()

    # 第二步，在画布上画图
    plt.pie(x, labels=y, colors=['r', 'g', 'b', 'y'], autopct='%.2f%%', shadow=True, startangle=90,
            explode=[0, 0, 0.1, 0],labeldistance=1.08)
    plt.axis('equal')  # 设置横轴和纵轴大小相等，这样饼才是圆的
    plt.title("重庆二手房销量", fontsize=20)
    plt.legend(bbox_to_anchor=(0, 1))  # 让图例生效，并设置图例显示位置

    # 第三步，需要在操作系统上显示
    plt.show()


if __name__ == "__main__":
    # 读取初步清洗后的数据
    data = pd.read_csv("../data/初步清洗.csv")

    # 常规清洗数据，去空值，去重复值，去异常值
    data.dropna(axis=0, how='any', inplace=True)  # 去空值   # axis 0：行来找，1：列来找
    data.drop_duplicates('标题', keep='first', inplace=True)  # 去重复值

    # 对需要数组计算的列转变数据类型

    # 分组统计
    data = data.groupby('地区').size()
    print(data)

    x = data.values
    y = data.index

    # chart_bar_price(x, y)#均价图
    # chart_bar_area(x1, y1)  # 平均面积图
    chart_pie(x, y)
