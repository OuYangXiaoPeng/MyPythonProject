# python语法的判断语句
# 目标如何利用判断语句进行编程
# if-else else-if
# a = int(input("请输入变量："))
# b = int(input("请输入变量："))
# if a==b:
#     print("a==b")
# if a>b:
#     print("a>b")
# if a<b:
#     print("a<b")
#
# if a==b:
#     print("a==b")
# elif a>b:
#     print("a>b")
# else:
#     print("a<b")
# 休眠
import time

print("欢迎参与一个猜拳游戏，利用键盘输入："
      "\n石头 剪刀 布 内容 进行胜负判断" +
      "\n（1.石头，2.剪刀，3.布）")
# 设计一个电脑端：自动生成结果
# 设计一个玩家端：人为输入结果
import random

a = 1
while a < 10:
    b = 1
    computernum = random.randint(1, 3)
    playernum = int(input("请输入您的数字:"))
    while b == 1:
        if playernum ==1 or playernum ==2 or playernum ==3:
            b = 0
        else:
            print('输入错误')
            print("请输入1,2,3")
            playernum = int(input())
    if computernum == playernum:
        print(str(computernum) + "  " + str(playernum) +
              "\n平手")
    elif (computernum - playernum) == -1 or (computernum - playernum) == 2:
        print(str(computernum) + "  " + str(playernum) +
              "\n电脑获胜")
    else:
        print(str(computernum) + "  " + str(playernum) +
              "\n玩家获胜")
    a = a + 1
