#深化python应用实现爬虫的功能
shuangjiang1="https://img.ivsky.com/img/bizhi/shuangjiang_fengye_v59042"
shuangjiang2="https://img.ivsky.com/img/bizhi/zhiwu"
cq="https://cq.lianjia.com/ershoufang/rs%E9%87%8D%E5%BA%86/"

import requests as req
# 如何破解反爬虫 帮我们让浏览器实现认知
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.26"}
mypage = req.get(cq,headers)
# print(mypage)#200=成功;   403=失败;
# print(mypage.text)

# 抓取一张链家的图片
# 浏览器 挖掘链接信息 并且 陈列
url="https://image1.ljcdn.com/110000-inspection/ce55740d-7667-45be-9f4c-83b6e8f1af93_1000.jpg.296x216.jpg"
print(url)

from bs4 import BeautifulSoup as soup
souptext = soup(mypage.text,"html5lib")
selecter="#content > div.leftContent > ul > li:nth-child(1) > a > img.lj-lazy"
result = souptext.select(".lj-lazy")
print(result)