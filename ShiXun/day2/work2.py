import csv

# 设置学生成绩表路径
source_path = './表格等文件/环节成绩登记册20221106093434.csv'
# 设置存放拆分结果文件的文件夹路径
result_path = './学号分类/'

# 打开学生成绩表
with open(source_path, 'r', encoding='gb2312', newline='') as source_file:
    # 将文件对象转换为DictReader对象
    source_csv = csv.DictReader(source_file)
    # 将csv对象的表头读取出来
    headers = source_csv.fieldnames

    # 循环处理确认表中除表头外的每一行数据
    for csv_row in source_csv:
        # 根据获取的学生学号拼接新文件名
        file_name = csv_row['学号'] + '.csv'
        # 拼接新文件路径
        file_path = result_path + file_name

        # 创建新文件并添加数据
        with open(file_path, 'w', encoding='GBK', newline='') as target_file:
            # 将文件对象转换为DictWriter对象
            target_writer = csv.DictWriter(target_file, fieldnames=headers)
            # 写入表头
            target_writer.writeheader()
            # 写入数据
            target_writer.writerow(csv_row)
