import xlrd
def getvalue(bookname,sheetnumb,colnum,rownum):
    file = xlrd.open_workbook(bookname)
    sheet = file.sheet_by_name(sheetnumb)
    coldata = sheet.col_values(colnum)
    rowdata = sheet.row_values(rownum)
    return coldata,rowdata

data1=getvalue("xiandata.xls","mydata",0,0)
data2=getvalue("xiandata.xls","mydata",1,0)
data3=getvalue("xiandata.xls","mydata",2,0)
# print(data1[0])

data11=data1[0]
del data11[0]
data22=data2[0]
del data22[0]
data33=data3[0]
del data33[0]

num = 0
num1 = 0
dianti=[]
louti=[]
for i in data11:
    if "电梯" in i:
        num = num + 1
        dianti.append(i)
    else:
        num1 = num1 + 1
        louti.append(i)
print(str(num)+"个电梯房")
# print(dianti)
print(str(num1)+"个楼梯房")
# print(louti)


print()
def getval(bookname,sheetnumb,colnum):
    file = xlrd.open_workbook(bookname)
    sheet = file.sheet_by_name(sheetnumb)
    coldata = sheet.col_values(colnum)
    return coldata
def getval2(bookname,sheetnumb,colnum):
    file = xlrd.open_workbook(bookname)
    sheet = file.sheet_by_name(sheetnumb)
    rowdata = sheet.row_values(colnum)
    return rowdata
nums = 0
max=0
for i in getval("xiandata.xls","mydata",0):
    if "电梯" in i:
        temp=int(getval2("xiandata.xls","mydata",nums)[2])
        if(max<temp):
            max=temp
    nums+=1
print(max)
nums = 0
min=300
for i in getval("xiandata.xls","mydata",0):
    if "电梯" in i:
        temp=int(getval2("xiandata.xls","mydata",nums)[2])
        if(min>temp):
            min=temp
    nums+=1
print(min)
print("差价"+str(max-min))

# 计数器
from collections import Counter
c=Counter(data22)
# print(c)

print()
maxNum=0
minNum=6
for k,v in c.items():
    if maxNum < int(v):
        maxNum = int(v)
        name = k
    if minNum > int(v):
        minNum = int(v)
print("最多次数：",end='')
print(maxNum)
print("名字为："+name)
print("最少次数：",end='')
print(minNum)
for k,v in c.items():
    if minNum == int(v):
        print(k)
