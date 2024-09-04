# 导入csv模块
import csv
# 设置员工发展基金确认表路径
path= './表格等文件/员工发展基金确认表.csv'
# 打开员工发展基金确认表
with open(path, 'r', encoding='gb2312', newline='') as source_file:
    # 将文件对象转换成DictReader对象
    file_open=csv.DictReader(source_file)
    # 将csv的表头读取出来
    header=file_open.fieldnames

    # 循环处理确认表中除表头外的每一行数据
    for csv_row in file_open:

        # 打印数据
        print(csv_row)
