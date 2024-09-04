import xlrd
def getvalue(filename,sheetnumb,colnum,rownum):
    file = xlrd.open_workbook(filename)
    sheet = file.sheet_by_index(sheetnumb)
    coldata = sheet.col_values(colnum)
    rowdata = sheet.row_values(rownum)
    return coldata,rowdata

data1=getvalue("泰坦尼克号的数据.xls",0,0,0)[0]
data2=getvalue("泰坦尼克号的数据.xls",0,1,0)[0]
data3=getvalue("泰坦尼克号的数据.xls",0,3,0)[0]
del data1[0]
del data2[0]

sc1=0
sw1=0
sc2=0
sw2=0
sc3=0
sw3=0
nv1=0
nv2=0
nv3=0
nvw1=0
nvw2=0
nvw3=0
nan1=0
nan2=0
nan3=0
for i in range(0,len(data1)):
    if data1[i]==1:
        if data2[i]==1 and data3[i]=='female' :
            sc1+=1
            nv1+=1
        elif data2[i]==0 and data3[i]=='female' :
            sw1+=1
            nvw1+=1
        if data2[i]==1 and data3[i]=='male' :
            sc1+=1
            nan1+=1
        else:
            sw1+=1
    if data1[i]==2 :
        if data2[i]==1 and data3[i]=='female' :
            sc2+=1
            nv2+=1
        elif data2[i] == 0 and data3[i] == 'female':
            sw2+=1
            nvw2+=1
        if data2[i]==1 and data3[i]=='male' :
            sc2+=1
            nan2+=1
        else:
            sw2 += 1
    if data1[i]==3:
        if data2[i]==1 and data3[i]=='female' :
            sc3+=1
            nv3+=1
        elif data2[i] == 0 and data3[i] == 'female':
            sw3+=1
            nvw3+=1
        if data2[i]==1 and data3[i]=='male' :
            sc3+=1
            nan3+=1
        else:
            sw3+=1
print("1号仓生存人数："+str(sc1)+"\t死亡人数："+str(sw1))
print("2号仓生存人数："+str(sc2)+"\t死亡人数："+str(sw2))
print("3号仓生存人数："+str(sc3)+"\t死亡人数："+str(sw3))
print("一号仓女生存活："+str(nv1)+"\t死亡："+str(nvw1))
print("二号仓女生存活："+str(nv2)+"\t死亡："+str(nvw2))
print("三号仓女生存活："+str(nv3)+"\t死亡："+str(nvw3))
print("一号仓男生存活："+str(nan1)+"\t死亡"+str(sw1-nvw1))
print("二号仓男生存活："+str(nan2)+"\t死亡"+str(sw2-nvw2))
print("三号仓男生存活："+str(nan3)+"\t死亡"+str(sw3-nvw3))
# print("生存与死亡的比率："+str(round(num1/num0,3)))


from collections import Counter
BiLv = Counter(data2)
print(BiLv)

CangWei = Counter(data1)
print(CangWei)

result1 = Counter(data2[1:324])
print(result1)




# list=[]
# for i in range(len(data1[0])):
#     list.append(getvalue("泰坦尼克号的数据.xls",0,0,i)[1])
# del list[0]
# print(list)