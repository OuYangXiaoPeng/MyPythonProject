import random
import time

import pandas as pd
import requests
from bs4 import BeautifulSoup

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.95 Safari/537.36"
}
a = []
adr = ['江北区', '渝北区', '巴南区', '沙坪坝']


def get_data(url):
    # 第一步，获取整个网页，但是网页没有格式
    data = requests.get(url, headers=header)
    # 第二步，把网页的文本内容转换或者解析成有格式的文本，html或者xml
    data_h = BeautifulSoup(data.text, "lxml")
    # 第三步，在有格式的html文本里，选择自己想要的数据,CSS路径    id使用#   div.title>
    标题 = data_h.select("div.title>a")
    地址 = data_h.select("div.positionInfo")
    信息 = data_h.select("div.houseInfo")
    时间 = data_h.select("div.followInfo")
    总价 = data_h.select("div.totalPrice.totalPrice2")
    单价 = data_h.select("div.unitPrice")
    # 第四步，处理数据

    for title, addr, info, time, total, price in zip(标题, 地址, 信息, 时间, 总价, 单价):  # replace strip() split()
        地址1 = addr.get_text().split('-')
        信息1 = info.get_text().split('|')
        时间1 = time.get_text().split('/')
        b = {
            "标题": title.get_text().strip(),
            "总价": total.get_text().strip(),
            "单价": price.get_text().strip(),
            "小区": 地址1[0].strip(),
            "街道": 地址1[-1].strip(),
            "户型": 信息1[0].strip(),
            "面积": 信息1[1].strip(),
            "朝向": 信息1[2].strip(),
            "装修": 信息1[3].strip(),
            "楼层": 信息1[4].strip(),
            "建筑时间": 信息1[5].strip(),
            "楼型": 信息1[-1].strip(),
            "关注": 时间1[0].strip(),
            "发布时间": 时间1[-1].strip(),
            "地区": addr[random.randint(0, 3)]
        }
        a.append(b)


if __name__ == '__main__':  # 对每个模块执行的时候，如果是自己运行，它下面管住的代码就会运行，如果是其他来调用这个模块，里面的代码被隐藏，不执行
    page = int(input("请输入你要爬取多少页："))
    for i in range(1, page + 1):
        # print("值为：{1},{0}".format(i,j))
        # print("值为：%d"%(i))
        url = "https://cq.lianjia.com/ershoufang/pg{}".format(str(i))  # 这是单页面爬取，后面要实现多页面自动爬取
        get_data(url)
        time.sleep(2)
        print("第{}页爬取成功。".format(i))
    # df是自己取的名字，是已经把Python的数据格式转换为pandas包要求的格式
    df = pd.DataFrame(a, columns=['标题', '总价', '单价', '小区', '街道', '户型', '面积', '朝向', '装修', '楼层',
                                  '建筑时间', '楼型', '关注', '发布时间', '评价', '地区'])
    df.to_csv("../data/数管5班爬虫数据.csv", mode='a', index=True, index_label='编号')
    # df.to_excel("数管5班爬虫数据.xlsx")    #这个是需要额外安装链接office的包
    # df.to_json("数管5班爬虫数据.json")
    # df.to_sql("数管5班爬虫数据.sql")
