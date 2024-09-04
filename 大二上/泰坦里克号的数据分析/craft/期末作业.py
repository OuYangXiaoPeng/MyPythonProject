from collections import Counter

import xlrd


def row(f, row):
    file = xlrd.open_workbook(f)
    sheet = file.sheet_by_index(0)
    row = sheet.row_values(row)
    return row


def col(f, col):
    file = xlrd.open_workbook(f)
    sheet = file.sheet_by_index(0)
    # 跳过头部文件
    col = sheet.col_values(col, start_rowx=1)
    return col


if __name__ == "__main__":
    file = '西安房屋数据_7fd52073644585a6962f (1).xls'

    # 最受欢迎户型
    p = Counter(col(file, 2))
    most_common = p.most_common(1)[0][0]
    print("最受欢迎户型:", end="")
    print(most_common)

    # 最受欢迎区域
    p = Counter(col(file, 3))
    most_common = p.most_common(1)[0][0]
    print("最受欢迎区域:", end="")
    print(most_common)

    # 房子平均价格
    list = col(file, 4)
    len = len(list)
    sum = sum(list)
    avg_price = sum / len
    avg_price_rounded = round(avg_price, 2)
    print("房子平均价格:", end="")
    print(avg_price_rounded, end="")
    print("万")

    # 电梯房个数
    num = 0
    for j in col(file, 2):
        if ("电梯" in j):
            num += 1
    print("电梯房个数:", end="")
    print(num, end="")
    print("个")
