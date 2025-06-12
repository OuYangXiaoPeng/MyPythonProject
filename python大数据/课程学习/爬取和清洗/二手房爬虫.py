import random
import time

import pandas as pd
import requests
from bs4 import BeautifulSoup

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
}

a = []
adr = ['江北区', '渝北区', '巴南区', '沙坪坝']


def get_data(url):
    # 1.获取整个网页，但是网页没有可是
    data = requests.get(url, headers=header)
    # 2.打网页内容转换或者解析成有格式的文本，html或者xml
    data_h = BeautifulSoup(data.text, 'lxml')
    # 3.选择在有格式的html文本里面，选择自己想要的数据,CSS路径     id使用#   div.title>
    title = data_h.select("div.title > a")
    address = data_h.select("div.positionInfo")
    info = data_h.select("div.houseInfo")
    time = data_h.select("div.followInfo")
    price = data_h.select("div.totalPrice.totalPrice2")
    unitprice = data_h.select("div.unitPrice")
    # 4.处理数据:strip()去空格，replace()替换,find()查找,split()分割,partiton()分割成3部分

    for title, address, info, time, total, price in zip(title, address, info, time, price, unitprice):
        add1 = address.get_text().split("-")
        info1 = info.get_text().split("|")
        # print(info1)
        time1 = time.get_text().split("/")
        b = {
            "标题": title.get_text().strip(),
            "总价": total.get_text().strip(),
            "单价": price.get_text().strip(),
            "小区": add1[0].strip(),
            "街道": add1[-1].strip(),
            "户型": info1[0].strip(),
            "面积": info1[1].strip(),
            "朝向": info1[2].strip(),
            "装修": info1[3].strip(),
            "楼层": info1[4].strip(),
            "楼型/时间": info1[5].strip(),
            "关注度": time1[0].strip(),
            "时间": time1[1].strip(),
            "地区": adr[random.randint(0, 3)]
        }
        a.append(b)


if __name__ == '__main__':
    page = int(input("请输入你要爬取多少页:"))
    for i in range(1, page + 1):
        url = "https://cq.lianjia.com/ershoufang/pg{}".format(str(i))
        time.sleep(2)
        get_data(url)
        print("第{}页爬取成功！".format(i))

        # df是自己取的名字，是已经把python的数据格式转换为pandas包要求的格式
        df = pd.DataFrame(a, columns=['标题', '总价', '单价', '小区', '街道',
                                      '户型', '面积', '朝向', '装修', '楼层', '楼型/时间',
                                      '关注度', '时间', '地区']
                          )
        # 保存的四个格式
        df.to_csv("../data/爬取数据.csv", mode='a', index=True, index_label='编号')  # mode模式中 ‘a’是追加
        # df.to_excel("爬取数据.xlsx")#需要额外安装连接office的包
        # df.to_json("爬取数据.json")
        # df.to_sql()
