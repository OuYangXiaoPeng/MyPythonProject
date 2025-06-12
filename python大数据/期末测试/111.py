import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
from typing import List, Dict


# 全局样式配置
def configure_plot_settings():
    """配置全局绘图参数"""
    try:
        # 尝试使用seaborn风格，如果不可用则使用默认风格
        plt.style.use('seaborn-v0_8')  # 新版本Matplotlib使用这个
    except:
        plt.style.use('ggplot')  # 回退样式

    plt.rcParams.update({
        'font.sans-serif': ['SimHei'],  # 中文显示
        'axes.unicode_minus': False,  # 负号显示
        'font.size': 12,
        'figure.autolayout': True  # 自动调整布局
    })


class TrainDataVisualizer:
    """高铁车次数据可视化分析类"""

    def __init__(self, data_path: str):
        try:
            self.data = pd.read_excel(data_path)
            self._validate_data()
        except FileNotFoundError:
            raise FileNotFoundError(f"无法找到数据文件: {data_path}")
        except Exception as e:
            raise Exception(f"数据加载失败: {str(e)}")

    def _validate_data(self):
        """数据验证"""
        required_columns = {'车次', '日期', '上车人数'}
        if not required_columns.issubset(self.data.columns):
            missing = required_columns - set(self.data.columns)
            raise ValueError(f"数据缺失必要列: {missing}")

    def plot_daily_passengers(self, train_number: str):
        """绘制指定车次每日上车人数散点图"""
        subset = self._filter_by_train_number(train_number)

        plt.figure(figsize=(12, 6))
        plt.scatter(
            subset['日期'],
            subset['上车人数'],
            color='royalblue',
            alpha=0.7,
            edgecolors='w',
            s=100
        )

        self._decorate_plot(
            title=f"{train_number}车次每日上车人数",
            xlabel="日期",
            ylabel="人数",
            rotate_xticks=45
        )

    def compare_multiple_trains(self, train_numbers: List[str]):
        """对比多个车次的上车人数趋势"""
        plt.figure(figsize=(12, 6))

        colors = plt.cm.tab10.colors
        markers = ['o', 's', '^', 'D', 'v']

        for i, number in enumerate(train_numbers):
            subset = self._filter_by_train_number(number)
            plt.plot(
                subset['日期'],
                subset['上车人数'],
                color=colors[i],
                marker=markers[i % len(markers)],
                linestyle='--',
                linewidth=2,
                markersize=8,
                label=number
            )

        self._decorate_plot(
            title="车次上车人数对比",
            xlabel="日期",
            ylabel="人数",
            rotate_xticks=45,
            legend=True
        )

    def plot_passenger_distribution(self, train_numbers: List[str]):
        """绘制上车人数分布饼图"""
        subset = self.data[self.data['车次'].isin(train_numbers)]
        totals = subset.groupby('车次')['上车人数'].sum()

        plt.figure(figsize=(8, 8))
        plt.pie(
            totals,
            labels=totals.index,
            autopct='%1.1f%%',
            startangle=90,
            counterclock=False,
            wedgeprops={'edgecolor': 'white', 'linewidth': 1},
            colors=plt.cm.Pastel1.colors,
            textprops={'fontsize': 12}
        )

        self._decorate_plot(  # 修正了这里的拼写错误
            title=f"{'、'.join(train_numbers)}车次上车人数分布",
            legend=False
        )

    def _filter_by_train_number(self, number: str) -> pd.DataFrame:
        """按车次号过滤数据"""
        return self.data[self.data['车次'] == number].copy()

    @staticmethod
    def _decorate_plot(
            title: str = None,
            xlabel: str = None,
            ylabel: str = None,
            rotate_xticks: int = 0,
            legend: bool = False
    ):
        """统一美化图表"""
        if title:
            plt.title(title, pad=20, fontsize=14)
        if xlabel:
            plt.xlabel(xlabel, labelpad=10)
        if ylabel:
            plt.ylabel(ylabel, labelpad=10)
        if rotate_xticks:
            plt.xticks(rotation=rotate_xticks)
        if legend:
            plt.legend(
                loc='upper left',
                bbox_to_anchor=(1, 1),
                frameon=True,
                shadow=True
            )
        plt.grid(True, alpha=0.3)

        plt.tight_layout()


def main():
    # 初始化配置
    configure_plot_settings()

    try:
        # 创建可视化实例
        visualizer = TrainDataVisualizer("train_no.xlsx")

        # 1. D04车次每日上车人数散点图
        visualizer.plot_daily_passengers("D04")
        plt.show()

        # 2. D05和D06车次对比折线图
        visualizer.compare_multiple_trains(["D05", "D06"])
        plt.show()

        # 3. D02-D06车次分布饼图
        visualizer.plot_passenger_distribution(
            [f"D0{i}" for i in range(2, 7)]
        )
        plt.show()

    except FileNotFoundError as e:
        print(f"错误: {str(e)}")
        print("请确保数据文件'train_no.xlsx'存在于当前目录")
    except Exception as e:
        print(f"程序执行出错: {str(e)}")


if __name__ == "__main__":
    main()