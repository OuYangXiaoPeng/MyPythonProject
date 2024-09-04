import xlrd as xd
file = xd.open_workbook("作业数据.xls")
mysheet = file.sheet_by_name("Sheet1")
mydata1 = mysheet.cell_value(1,1)
mydata2 = mysheet.cell_value(2,1)
mydata3 = mysheet.cell_value(3,1)
mydata4 = mysheet.cell_value(4,1)

print(mydata1.split(".")[1])
print(mydata2.split(".")[1]+mydata2.split(".")[3])
print(mydata3.split(".")[0].replace("123",""))
print(mydata4.split(".")[2]+mydata4.split(".")[0])
import webbrowser as chrom
chrom.open("https://www."+mydata1.split(".")[1]+".com")