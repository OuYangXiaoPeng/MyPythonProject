# 定义汇率
USD_TO_RMB = 6.78

# 获取用户输入
input_str = input("请输入金额及币种,请以RMB或USD开头：")

# 判断币种并提取金额
if input_str[0:3] in ["RMB"]:
    USD = float(input_str[3:]) / USD_TO_RMB
    print(f"USD{USD:.2f}")
elif input_str[0:3] in ["USD"]:
    RMB = float(input_str[3:]) * USD_TO_RMB
    print(f"RMB{RMB:.2f}")
else:
    print("输入格式错误,请以RMB或USD开头。")
