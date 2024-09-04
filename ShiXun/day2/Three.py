# 导入csv模块
import csv

member_list = [
    ['邱大仁'],
    ['徐小刚', '陈知枫'],
    ['王晴', '廖雨']
]

# 打开并创建'writerow_demo.csv'文件，注意参数的设置，获取文件对象
with open('writerow_demo.csv', 'w', encoding='utf-8', newline='') as target_file:
    # 将文件对象转换为writer对象
    target_writer = csv.writer(target_file)

    # 循环遍历列表中的元素
    for csv_data in member_list:
        # 将列表中的元素写入csv文件中
        target_writer.writerow(csv_data)
