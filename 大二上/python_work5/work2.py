import requests#数据采集
import bs4#数据分析库
import xlrd#数据读取库
import xlwt#数据写入库
import requests as req
from bs4 import BeautifulSoup as soup
import xlwt as wt
url = "https://cq.lianjia.com/ershoufang/"
import requests as req
from bs4 import BeautifulSoup as soup
import xlwt as wt
mypagedata=req.get(url)
text = mypagedata.text#鸡汤全是杂志
cookies = mypagedata.cookies
souptext = soup(text,"html5lib")
name1 = souptext.select(".totalPrice")
for url in name1:
    print(url.text)
print("*"*100)
name1 = souptext.select(".houseInfo")
for url in name1:
    print(url.text.split("|")[1])
print("*"*100)
name1 = souptext.select(".houseInfo")
for url in name1:
    print(url.text)
