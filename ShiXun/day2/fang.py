import csv

# 打开assets.csv文件作为csvfile
with open('assets.csv', 'a', newline='') as csvfile:
    # 自动化写入数据
    writer = csv.writer(csvfile, dialect='excel')

    # 设置表头（键）
    header=['小区名称', '地址', '建筑年份', '楼栋', '单元', '户室', '朝向', '面积']
    # 将表头写入
    writer.writerow(header)

# 调用控制台输入键所对应的值
title=input('请输入小区名称：')
address = input('请输入小区地址：')
year = input('请输入小区建造年份：')
block = input('请输入楼栋号：')


unit_loop = True #设置unit_loop为true
while unit_loop:#外循环
    # 调用控制台输入键所对应的值
    unit=input('请输入单元号：')
    start_floor = input('请输入起始楼层：')
    end_floor = input('请输入终止楼层：')


    input('接下来请输入起始层每个房间的门牌号、南北朝向及面积，按任意键继续')

    # 创建一个起始楼层字典
    start_floor_rooms = {}
    # 创建一个起始尾号列表
    floor_last_number = []

    # 设置room_loop为true
    room_loop = True
    while room_loop:
        #调用控制台输入起始楼层户室的尾号
        last_number = input('请输入起始楼层户室的尾号:（如01，02）')
        # 将楼层户室的尾号加入列表
        floor_last_number.append(last_number)

        # 房间号=楼层号+尾号
        room_number = int(start_floor + last_number)

        # 调用控制台输入房间的房间的南北朝向
        direction = int(input('请输入 %d 的朝向(南北朝向输入1，东西朝向输入2)：' % room_number ))
        # 调用控制台输入房间的房间的面积
        area = int(input('请输入 %d 的面积，单位 ㎡ ：' % room_number))
        # 将房间的南北朝向和面积加入到对应起始楼层房间号的字典
        start_floor_rooms[room_number] = [direction,area]

        # 是否需要继续输入房间尾号
        continued= input('是否需要输入下一个尾号？按 n 停止输入，按其他任意键继续：')

        # 如果continue为n则将room_loop设为fales退出内循环
        if continued == 'n':
            room_loop = False
        else:
            # 否则room_loop为true，继续循环
            room_loop = True

    # 创建一个单元房间字典
    unit_rooms = {}
    # 将起始楼层房间赋值给单元房间字典的起始楼层
    unit_rooms[start_floor] = start_floor_rooms

    # 循环每层楼的信息赋值给unit_rooms
    for floor in range(int(start_floor) + 1, int(end_floor) + 1):

        #   创建一个楼层房间字典
        floor_rooms = {}

        for i in range(len(start_floor_rooms)):

            # number=楼层+尾号
            number = str(floor) + floor_last_number[i]
            # 将由起始楼层与房间尾号所对应的起始楼房间赋值给info
            info = start_floor_rooms[int(start_floor + floor_last_number[i])]
            # 将info赋值给每个number所对应的楼层号
            floor_rooms[int(number)] = info

        # 将每个楼层房间的信息赋值给楼层所对应的单元房间
        unit_rooms[floor] = floor_rooms

    # 创建新文件并添加数据
    with open('assets.csv', 'a', newline='')as csvfile:

        writer = csv.writer(csvfile, dialect='excel')
        for sub_dict in unit_rooms.values():
            for room,info in sub_dict.items():
                dire = ['', '南北', '东西']
                writer.writerow([title,address,year,block,unit,room,dire[info[0]],info[1]])

     # 是否需要继续输入下一个单元
    unit_continue = input('是否需要输入下一个单元？按 n 停止单元输入，按其他任意键继续：')
    # 如果unit_continue为n则将 unit_loop设为fales退出外循环
    if unit_continue == 'n':
        unit_loop = False
    else:
        # 否则 unit_loop为true，继续循环
        unit_loop = True

print('恭喜你，楼宇数据录入工作完成！')
