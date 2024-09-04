# 网络爬虫入门
# 采集数据来源是 来源于我们的序列数据
# 网络数据上需分配来源
# 数据需要路沉淀 具体的页数和编号 连续的页面变化
# 找3个可以采集数据的页面
# 构造出不同的链接

import requests

url="https://cq.lianjia.com/ershoufang/pg1/"
maoyan="https://www.maoyan.com/board/4?timeStamp=1669183298850&channelId=40011&index=7&signKey=7b76f0bc2dcf241c3578365b8306e94d&sVersion=1&webdriver=false&offset=0"
# map 为啥使用map函数意义

urls = map(lambda x: "https://cq.lianjia.com/ershoufang/pg{}/".format(x),(1,2,3,4,5,6))
headers={
        "User-Agnet":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52"
    }
urls = list(urls)
print(urls)
from bs4 import BeautifulSoup as soup, BeautifulSoup

mydata1=requests.get(url,headers=headers).text
souptext = soup(mydata1,"html5lib")
# print(souptext)

# #content > div.leftContent > ul > li:nth-child(1) > a
mytitle2 = souptext.select(".title a")
imgs = souptext.select("img.lj-lazy")

infos = souptext.select("li:nth-of-type(n+7) div.houseInfo")
# for i in mytitle2:
#     print(i)
# for i in imgs:
#     print(i)
# for i in infos:
#     print(i)
# for i,j,k in zip(mytitle2,imgs,infos):
#     print(i.text+j.text+k.text)


# mydata2=requests.get(maoyan,headers=headers,timeout=20)
# mydata2.encoding="utf-8"
# mydata2 = mydata2.text
# print(mydata1)
# print(mydata2)

def a(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52"
    }
    data = requests.get(url, headers=head)
    text = data.text
    soup = BeautifulSoup(text,"html5lib")
    title = soup.select(".title a")
    imgs = soup.select("img.lj-lazy")
    infos = soup.select("li:nth-of-type(n+7) div.houseInfo")
    for i,j,k in zip(title,imgs,infos):
        print(i.text)
        print("--------------------------------")
        print(j)
        print("--------------------------------")
        print(k.text)
        print()

if __name__ == '__main__':
    url="https://cq.lianjia.com/ershoufang/pg1/"
    a(url)