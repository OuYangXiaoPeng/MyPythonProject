#我们的爬虫项目实战
# 熟悉使用的爬虫库
# 熟悉爬虫的规律
# 熟悉爬虫的数据方法
# 熟悉爬虫的具体解析过程
import re

import requests
from  bs4 import BeautifulSoup as soup
import xlwt
headers={
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46"
}
# 根据需求采集批量化网页信息
# 找到接口根据结果解释信息
# 采集url 只要是浏览器可以解决的我们都可以采集
# 采集过程复杂
# 1.伪装 2.找到真实的接口 3.找到变换规律 4.批量采集
# 2做爬虫很复杂 接口不是固定的 斗智斗勇的过程
# 3.去网站找成熟的代码调试后根据结果来运营分析程序内容
# 采集一下链家重庆二手房 打印信息发截图
# https://cq.lianjia.com/ershoufang/rs%E5%A4%A7%E6%B8%A1%E5%8F%A3/

url="https://cq.lianjia.com/ershoufang/rs%E5%A4%A7%E6%B8%A1%E5%8F%A3/"
url2="https://cq.lianjia.com/ershoufang/rs/"
mytext=requests.get(url2,headers=headers).text
# print(mytext)
# 页面信息可以承载 有连续的变化 根据信息可以跳转
# bs4 格式化网页
cleardata = soup(mytext,"html5lib")#所有要去解析的文件
# select方法选择器
title = cleardata.select(".title a")
imgs = cleardata.select("img.lj-lazy")
infos = cleardata.select("li:nth-of-type(n+7) div.houseInfo")


list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
for i in infos:
    j=i.text.split("|")
    list1.append(j[0])
    list2.append(j[1])
    list3.append(j[2])
    list4.append(j[3])
    list5.append(j[4])
    print(j)

# webscraper
workbook = xlwt.Workbook(encoding='utf-8',style_compression=0)
worksheet = workbook.add_sheet('这是sheet1',cell_overwrite_ok=True)

header=['几室几厅','面积','朝向','装修程度','楼层']
for i in range(0,len(header)):
    worksheet.write(0,i,header[i])

for i in range(0,len(list1)):
    worksheet.write(i+1,0,list1[i])
    worksheet.write(i+1,1,list2[i])
    worksheet.write(i+1,2,list3[i])
    worksheet.write(i+1,3,list4[i])
    worksheet.write(i+1,4,list5[i])

workbook.save('测试文件.xls')

# b站弹幕，并保存在本地

# 当下最热电影弹幕分析：
# 采集清洗+画图 不需要原创 只要调试
# 主角 田小娥 保存在单独文件