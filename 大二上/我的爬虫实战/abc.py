import xlrd as xd
data =xd.open_workbook ('期末作业.xls') #打开excel表所在路径
sheet = data.sheet_by_name('sheet1')  #读取数据，以excel表名来打开
d = []
for r in range(sheet.nrows): #将表中数据按行逐步添加到列表中，最后转换为list结构
    data1 = []
    for c in range(sheet.ncols):
        data1.append(sheet.cell_value(r,c))
    d.append(list(data1))
for i in range(1,31):
    for c in d[i][2]:
        if c in '!"#$%&\'()*+,-./:；<=>?@[\\]^_`{|}~':
            d[i][2] = d[i][2].replace(c, '')
# print(d)
b=[]
for i in range(1,31):
    b=d[i][0]
    a=b[11:]
    d[i].append(a)
print(d)
import xlwt
workbook = xlwt.Workbook(encoding='utf-8', style_compression=0)
worksheet = workbook.add_sheet('sheet1', cell_overwrite_ok=True)
# 加入表头
worksheet.write(0,3,"编号")
worksheet.write(0,2,"信息")
worksheet.write(0,1,"网址")
worksheet.write(0,0,"号码")
for i in range(1, len(d)):
    worksheet.write(i , 0, d[i][0])
for i in range(1, len(d)):
    worksheet.write(i , 1, d[i][1])
for i in range(1, len(d)):
    worksheet.write(i , 2, d[i][2])
for i in range(1, len(d)):
    worksheet.write(i , 3, d[i][3])
workbook.save('测试.xls')

import xlrd
import pandas as pd
df = pd.read_excel("测试.xls", index_col='号码')
df.sort_values(by='编号',inplace=True,ascending=True)
df.to_excel('测试2.xls')
