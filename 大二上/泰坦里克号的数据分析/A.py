import xlrd


def col(filename, sheetnumb, colnum):
    file = xlrd.open_workbook(filename)
    sheet = file.sheet_by_index(sheetnumb)
    coldata = sheet.col_values(colnum)
    return coldata


def row(filename, sheetnumb, rownum):
    file = xlrd.open_workbook(filename)
    sheet = file.sheet_by_index(sheetnumb)
    rowdata = sheet.row_values(rownum)
    return rowdata


level1 = []
level2 = []
level3 = []
data1 = col("泰坦尼克号的数据.xls", 0, 0)
del data1[0]
num = 1
for i in data1:
    if i == 1:
        level1.append(row("泰坦尼克号的数据.xls", 0, num))
    if i == 2:
        level2.append(row("泰坦尼克号的数据.xls", 0, num))
    if i == 3:
        level3.append(row("泰坦尼克号的数据.xls", 0, num))
    num += 1
print(level3)
