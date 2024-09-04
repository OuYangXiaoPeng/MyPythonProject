# 学习一个实战数据结构
# 叫做字典或者  json
# 打开有道-检查-network
# 打开xhr-响应
mydata = {"errorCode": 0,
          "translateResult": [[{"tgt": "my", "src": "我的"}]],
          "type": "zh-CHS2en",
          "smartResult": {"entries": ["", "my\r\n", "mine\r\n"],
                          "type": 1}}
# 完成
jingdong = {"code": 0, "whwswswws":
    "wFXh7Rhq4xcmFFmcMMIcQRQ",
            "openall": 1,
            "openalltouch": 1,
            "processtype": 1,
            "appidStatuscode": 0}
# 自己书写一个字典
info = {'name': '班长',
        'id': 100,
        'sex': 'f',
        'address': '地球亚洲中国北京'}
# 字典结构
# java map
# 键：值
# name : 键
# 班长: 值
# for i in info.keys():
#     print(i)
# print()
# for i in info.values():
#     print(i)
# print()
# for i in info.items():
#     print(i)
# print()
# for i,j in info.items():
#     print(i,j)
# print()
# 使用以上循环
# 遍历挖掘的2个数据 打印出来
# for i,j in mydata.items():
#     print(i,j)
#
# mydata = {"errorCode": 0,
#           "translateResult": [[{"tgt": "my", "src": "我的"}]],
#           "type": "zh-CHS2en",
#           "smartResult": {"entries": ["", "my\r\n", "mine\r\n"],
#                           "type": 1}}
# print(mydata["errorCode"])
# print(mydata["translateResult"][0][0])
# print(mydata["translateResult"][0][0]["tgt"])

jingdong = {"code": 0, "whwswswws":
    "wFXh7Rhq4xcmFFmcMMIcQRQ",
            "openall": 1,
            "openalltouch": 1,
            "processtype": 1,
            "appidStatuscode": 0}
print(jingdong["code"])
print(jingdong["openall"])
print(jingdong["openalltouch"])
print(jingdong["processtype"])
print(jingdong["appidStatuscode"])
# 挖掘一个淘宝的数据-打印xhr
