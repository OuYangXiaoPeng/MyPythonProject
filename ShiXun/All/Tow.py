#导入One.py中的变量
from All.One import PianMing, Up, BoFangLiang, BoFangLiang2, DanMuShu
# 第二步
# 生成xls表
import xlwt

f = xlwt.Workbook('encoding = utf-8')  # 设置工作簿编码
sheet1 = f.add_sheet('sheet1', cell_overwrite_ok=True)  # 创建sheet工作表，并设为可覆盖单元格
# 表头
late_header = ["排名", "视频名", "up主", "现目前播放量(万)", "播放量取整(万)", "弹幕数"]
# 表头加入
for i in range(len(late_header)):
    sheet1.write(0, i, late_header[i])

# 表中内容加入
for i in range(len(PianMing)):
    sheet1.write(i + 1, 0, i + 1)  # 写入数据参数对应 行, 列, 值
    sheet1.write(i + 1, 1, PianMing[i])  # 写入数据参数对应 行, 列, 值
    sheet1.write(i + 1, 2, Up[i])  # 写入数据参数对应 行, 列, 值
    sheet1.write(i + 1, 3, BoFangLiang[i])  # 写入数据参数对应 行, 列, 值
    sheet1.write(i + 1, 4, BoFangLiang2[i])  # 写入数据参数对应 行, 列, 值
    sheet1.write(i + 1, 5, DanMuShu[i])  # 写入数据参数对应 行, 列, 值
# xls的行距设置
sec_col = sheet1.col(1)  # 从零开始算，第二列
sec_col.width = 256 * 120
three_col = sheet1.col(2)  # 第三列
three_col.width = 256 * 25
four_col = sheet1.col(3)  # 第四列
four_col.width = 256 * 15
five_col = sheet1.col(4)  # 第五列
five_col.width = 256 * 15
# 保存
f.save('./热门榜Top100.xls')
