# python中的函数设置
# java
# 权限 返回值 函数名 参数 作用域{
#    函数体
#      return;
# }
# python
# 关键字 函数名 参数：
#        函数体
# def getresult(a,b):
#     print(a+b)
# getresult(1,2)

# 函数的设计和函数的调用
# def getCompare(num1,num2):
#     if num1>num2:
#         print(num1)
#         return num1
#     else:
#         print(num2)
#         return num2
# 比较结果之后 拿到更大的数
# 使用return关键字可以把 函数运算的结果
# 保存在一个变量中 可以用来后续的计算和处理
# getCompare(getCompare(1,2),getCompare(3,4))

# 计算器
# def getJiSuna(num3,num4):
#     print("加:"+str(num3+num4))
#     print("减:"+str(num3-num4))
#     print("乘:"+str(num3*num4))
#     print("除:"+str(num3/num4))
# aa = int(input("请输入第一个数字："))
# bb = int(input("请输入第二个数字："))
# getJiSuna(aa,bb)

# 预定值
# def getsum(a=1,b=2,c="+"):
#     print(a+b)
# getsum(2,3)

# 日常消费
# c = int(input("请输入你消费的次数："))
# def getXiaoFei(a1,b1):
#     b1 = b1 + b1
#     print("你消费的总金额为"+str(b1))
# for i in range(0,c):
#     getXiaoFei(input("请输入商品名："),b1=int(input("请输入金额：")))

# lambda匿名函数
# def关键字 return 参数 ：
# x= lambda a : a + 10
# print(x(5))
# x=lambda a:a*a
# print(x(10))
# print(x(100))
