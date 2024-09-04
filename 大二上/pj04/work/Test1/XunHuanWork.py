#
# for i in range(len(input("请输入内容：")),0):
#     print(i)
#
# #列表推导式
# for i in [i for i in range(1,10) if i > 5]:
#     print(i**2)

#导入数据管道
#openpyxl
import xlrd as xd
file = xd.open_workbook("mydata2.xls")
mysheet = file.sheet_by_name("Sheet1")
mydata1 = mysheet.col_values(0)
mydata2 = mysheet.row_values(0)
mydata3 = mysheet.cell_value(2,1)

print(mydata1)
print(mydata2)
print(mydata3)