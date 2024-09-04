#很低.-12月28号发打太作业
#2个题目:提交方式对分易交
#词频题，爬虫题，读取题
#读取题是核心最核心的题目
#数据读懂–按照读书的数据的方式–分析
#1.代码 2.画图 3.结果分析
#1.读取数据数据胾图利用读取代码
#2.完成以下的分析需求
#1.删除哪一行为什么蔡理好数据后可以读取
#本数拊集具有1.4列具有3423行
#所有的数据打印出
#东南朝向的别墅有几个字符串查找发含墅字或者拼这个两个字的信息
#看一下代有电梯和无电梯的房子的比声非老房子有电梯


import xlrd
def getvalue(filename,sheetnumb,colnum,rownum):
    file = xlrd.open_workbook(filename)
    sheet = file.sheet_by_index(sheetnumb)
    coldata = sheet.col_values(colnum)
    rowdata = sheet.row_values(rownum)
    return coldata,rowdata

data1=getvalue("data.xls",0,0,0)[0]
data2=getvalue("data.xls",0,2,0)[0]
data3=getvalue("data.xls",0,8,0)[0]
del data1[0]
print(data1)

# list=[]
# nums=0
# for i in getvalue("data.xls",0,0,nums)[1]:
#     list.append(i)
#     nums+=1

num1 = 0
num2 = 0
for i in data1:
    if "别墅" in i:
        num1 += 1
        # print(i)
    else:
        num2 += 1
print("含有别墅的有:"+str(num1))
print("非别墅:"+str(num2))


price2=0
NanBei = 0
for i,j in zip(data2,data3):
    if "南 北" in i:
        price2 += j
        NanBei += 1
print("南北平均价格为:"+str(price2/NanBei))


# from collections import Counter
# col = Counter(data1)
# print(col)