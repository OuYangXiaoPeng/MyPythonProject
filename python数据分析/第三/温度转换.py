while True:
    temp = input("请输入一个带单位符号的温度:")
    if temp[-1] in ['F', 'f']:
        C = (eval(temp[0:-1]) - 32) / 1.8
        print("转换后为{:.2f}C".format(C))
        break
    elif temp[-1] in ['C', 'c']:
        F = eval(temp[0:-1]) * 1.8 + 32
        print("转换后为{:.2f}F".format(F))
        break
    else:
        print("输入有误，", end='')
