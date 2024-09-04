# 导入csv模块
import csv

info_dict = {'姓名': '徐小刚', '工号': '1005', '员工发展基金': '100', '员工签字': ''}

# 设置表头
headers = info_dict.keys()
print(headers)
# 创建并打开'./徐小刚信息.csv'
with open('./徐小刚信息.csv', 'w', encoding='GBK', newline='') as target_file:
    # 将文件对象转换为DictWriter对象
    target_writer = csv.DictWriter(target_file, fieldnames=headers)
    # 写入表头
    target_writer.writeheader()
    # 将字典写入csv文件
    target_writer.writerow(info_dict)
