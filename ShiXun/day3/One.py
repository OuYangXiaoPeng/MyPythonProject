import csv
# 打开csv文件，写入表头
with open("./21计应301.csv","w+",encoding="GBK",newline="") as mbfile:
    xgj = csv.writer(mbfile,dialect="excel")
    header = ['序号','学年','学期','院(系)/部','行政班级','环节','学分','组次','学号','姓名','性别','成绩']
    xgj.writerow(header)
# 把固定不变的值输入到系统
xuenian = input("请输入学年：")
xueqi = input("请输入学期：")
yuanxibu = input("请输入院(系)/部：")
xingzhengbanji = input("请输入行政班级：")
huanjie = input("请输入环节：")
xuefen = input("请输入学分：")
# 准备数据容器
zuci_dict = {}
students_info = [[]]
student_info = []
# 组次循环
zuci_loop = True
while zuci_loop:
    zuci = input('请输入组次：')
    students_info = [[]]

    # 设计一个计数器，只允许输入最多4个学生信息
    num = 0
    student_loop = True
    while student_loop:
        student_info_xuehao= input("请输入学号：")
        student_info_name= input("请输入姓名：")
        student_info_sex= input("请输入性别：")
        student_info_cj= input("请输入成绩：")
        student_info = []
        student_info.append(student_info_xuehao)
        student_info.append(student_info_name)
        student_info.append(student_info_sex)
        student_info.append(student_info_cj)
        print(student_info)
        students_info.append(student_info)
        # 将当前组次值 赋值给学生们信息列表的第一个元素
        students_info[0] = zuci
        student_continue = input('是否需要输入下一个学生？按 n 停止单元输入，按其他任意键继续：')
        num = num + 1
        if num == 4:
            break

        if student_continue == 'n':
            student_loop = False
        else:
            student_loop = True
    print(students_info)
    # 将内循环输入的学生信息列表赋值给字典当前的主次
    zuci_dict[zuci] = students_info
    print(zuci_dict)

    for info in zuci_dict.values():
        print(info)
    zuci_continue = input('是否需要输入下一个组次？按 n 停止单元输入，按其他任意键继续：')
    if zuci_continue == 'n':
        zuci_loop = False
    else:
        zuci_loop = True


# 将所有学生信息写入csv
number = 0
with open('./21计应301.csv','a',encoding="GBK", newline='')as csvfile:
    writer = csv.writer(csvfile, dialect='excel')
    for info1 in zuci_dict.values():
        print(info1)
        for i in range(0,4):
            writer.writerow([(number+1),xuenian,xueqi,yuanxibu,xingzhengbanji,huanjie,xuefen,
                             info1[0],info1[i+1][0],info1[i+1][1],info1[i+1][2],info1[i+1][3]])
            number = number + 1






