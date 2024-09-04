import requests#数据采集
import bs4#数据分析库
import xlrd#数据读取库
import xlwt#数据写入库
import requests as req
from bs4 import BeautifulSoup as soup
import xlwt as wt
#任何采集的网页都是一个资源
#采集的网页需要拿到url
url = "https://cq.lianjia.com/ershoufang/"
url2 = "http://www.weather.com.cn/weather1d/101040700.shtml#input"
#如何获取这个 https://cq.lianjia.com/ershoufang/
#每个资源都是网页链接
#所以针对每个页面req抓取的页面的html代码所以展示的
#形式也是代码
import requests as req
from bs4 import BeautifulSoup as soup
import xlwt as wt
mypagedata=req.get(url2)
# print(mypagedata)
#<Response [200]>200 404 403(服务器被禁止了，一般封15分钟) 503 500
#主机：switch ps5 xbox -ban
text = mypagedata.text#鸡汤全是杂志
cookies = mypagedata.cookies
# print("*"*100)
# print(cookies)
# print("*"*100)
# print(text)
souptext = soup(text,"html5lib")
# print(souptext)
#soup.select方法是来筛选你要的数据
#请务必下载chorm
name1 = souptext.select(".t")
for url in name1:
    print(url)
# print("*"*100)
# name1 = souptext.select(".houseInfo")
# for url in name1:
#     print(url.text.split("|")[1])
# print("*"*100)
# name1 = souptext.select(".houseInfo")
# for url in name1:
#     print(url.text)