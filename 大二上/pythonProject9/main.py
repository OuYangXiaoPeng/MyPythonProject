# 如何使用python应用库进行编程
# urllib#原始数据采集爬虫
# request#高效的数据采集爬虫
# webbrowser
import webbrowser
from urllib.request import Request

url = "https://www.ivsky.com/"
mypic = "https://img.ivsky.com/img/tupian/co/202108/25/xishui_laohu-009.jpg"
listpic = "https://img.ivsky.com/img/tupian/t/202108/25/xishui_laohu-001.jpg"


# web.open(mypic)
# # 爬虫1
from urllib import request as slow
# import requests as fast
# # open
# # get
# data = slow.urlopen(url)
# mydata = data.read()
# print(mydata)
# mydataf=fast.get(url).text
# print(mydataf)

# 抽取一个函数  专门生产访问链接
# def geturls
# def geturls(a):
#     for i in range(1,a+1):
#         url="https://img.ivsky.com/img/tupian/t/202108/25/xishui_laohu-00{}.jpg".format(i)
#         print(url)
#         webbrowser.open(url)
#     return
# geturls(int(input("请输入提取张数：")))

def geturl(num):
    return "https://img.ivsky.com/img/tupian/t/202108/25/xishui_laohu-00{}.jpg".format(num)

urls = map(geturl, [i for i in range(1, 10)])
for i in urls:
    print(i)

import time

num=0
for i in map(lambda x: "https://img.ivsky.com/img/tupian/t/202108/25/xishui_laohu-00{}.jpg".
        format(x), [i for i in range(1, 10)]):
    slow.urlretrieve(i,"{}.jpg".format(num))
    num+=1
    time.sleep(1000)
# 书写一个函数：为每个转入不同的域名+上[1,100].com的后缀
