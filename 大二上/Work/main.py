#期末考试方式，大作业，3个题目
# 对函数的考核-map
# 对函数参数的考核-map函数的参数
# 拼接字符串，
# 解释一下如何使用map函数

# import xlrd
# file = xlrd.open_workbook("myurl.xls")
# sheet = file.sheet_by_index(0)
# sheet1 = file.sheet_by_index(1)
# sheet2 = file.sheet_by_index(2)
# col1 = sheet.col_values(0,0)[0]+"www."
# col2 = sheet1.col_values(0,0)[0]+"."
# col3 = sheet2.col_values(0,0)[0]
# colurl = col1 + col2 + col3
# print(colurl)#读取信息-完善拼接数据后清洗存到变量
# urls = map(lambda x: "https://www.baidu.mypic0{}".format(x),
#            [i for i in range(1,11)])
# for url in urls:
#     print(url)

# map解释
# map() 会根据提供的函数对指定序列做映射。
# lamda解释
# lambda 函数可接受任意数量的参数，但只能有一个表达式。
# 是指一类无需定义标识符（函数名）的函数或子程序。
# lambda 函数可以接收任意多个参数 (包括可选参数) 并且返回单个表达式的值。

# 抽1个函数操作
import xlrd
def getvalue(bookname,sheetnumb,colnum):
    file = xlrd.open_workbook(bookname)
    sheet = file.sheet_by_name(sheetnumb)
    coldata = sheet.col_values(colnum)
    return coldata

data1=getvalue("myurl.xls","sheet1",0)
data2=getvalue("myurl.xls","Sheet3",0)
data3=getvalue("myurl.xls","Sheet2",0)
print(data1[0]+"www."+data2[0]+"."+data3[0])

# xlsx，xlrd版本1.2
data4=getvalue("mymath.xlsx","Sheet1",0)
print(data4)
print()
urls = map(lambda x: "https://www.baidu.mypic0{}".format(x),
           [i for i in range(1,11)])
for url in urls:
    print(url)
