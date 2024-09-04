import xlrd
def getvalue(filename,sheetnumb,colnum,rownum):
    file = xlrd.open_workbook(filename)
    sheet = file.sheet_by_index(sheetnumb)
    coldata = sheet.col_values(colnum)
    rowdata = sheet.row_values(rownum)
    return coldata,rowdata

data1=getvalue("films.xls",0,0,0)
data2=getvalue("films.xls",0,1,0)
data3=getvalue("films.xls",0,2,0)
del data1[0][0]
del data2[0][0]
del data3[0][0]

print(data2[0])
print(data3[0])

list=[]
for i in range(len(data1[0])):
    list.append(getvalue("films.xls",0,0,i)[1])
del list[0]
print(list)

# 平均分
print()
num = 0
for i in data2[0]:
    num = num + i
# round(值,保留小数位数)  ----四舍五入
print("平均值为:"+str(round(num/len(data2[0]),1)))


# from collections import Counter
# c=Counter(data3[0])
# print(c)

print()
nums = 0
for i in data3[0]:
    if "周星驰" in i:
        nums = nums + 1
print("周星驰的电影有"+str(nums)+"部:")
num1 = 0
for i in list:
    str = data3[0][num1]
    # print(str)
    if "周星驰" in str:
        print(i)
    num1 = num1 + 1

# print()
# for i in data3[0][1:]:
#     if len(i.lstrip("主演：").split(","))<=3:
#         print(i.lstrip("主演：").split(","))

print()
print("参演人数有3人及以上的有：")
num2 = 0
for i in list:
    str = data3[0][num2]
    # print(str)
    if len(str.lstrip("主演：").split(","))<=3:
        print(i)
    num2 = num2 + 1