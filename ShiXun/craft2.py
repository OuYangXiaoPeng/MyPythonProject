from openpyxl.chart import BarChart, Reference
from openpyxl.reader.excel import load_workbook
wb = load_workbook('C:\\Users\\OYXP\\Documents\\Tencent Files\\2096008975\\FileRecv\\第十三季第二十五期 个人明细.xlsx')
# 读取工作簿中的活跃工作表
ws = wb.active
# 实例化 LineChart类，得到LineChart对象
chart = BarChart()
# 引用工作表的部分数据
data = Reference(worksheet=ws, min_row=1, max_row=2, min_col=8, max_col=8)
# 添加被引用的数据到LineChart对象
chart.add_data(data, from_rows=False, titles_from_data=False)
# 添加LineChart对象到工作表中，指定折线图的位置
ws.add_chart(chart, "F5")
# 引用工作表的表头数据
cats = Reference(worksheet=ws, min_row=1, max_row=2, min_col=7, max_col=7)
# 设置类别轴的标签
chart.set_categories(cats)
# 设置x轴的标题
chart.x_axis.title = "视频TOP10"
# 设置y轴的标题
chart.y_axis.title = "播放量(万)"
# 改变线条颜色
chart.style = 10
chart.style = 18
chart.style = 28
# 保存文件
wb.save('C:\\Users\\OYXP\\Documents\\Tencent Files\\2096008975\\FileRecv\\第十三季第二十五期 个人明细.xlsx')