import csv

file = open(r"表格等文件/test1.txt", "r", encoding="utf-8")

with open('test1.csv', 'w', encoding='GBK', newline='') as target_file:
    # 将文件对象转换为writer对象
    target_writer = csv.writer(target_file)
    # 循环遍历列表中的元素
    for line in file.readlines():
          line = line.replace(',', '\t')
          list = line.split()
          target_writer.writerow(list)