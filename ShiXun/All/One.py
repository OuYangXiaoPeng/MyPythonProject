import re
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42'}
url = 'https://www.bilibili.com/v/popular/rank/all/'
res = requests.get(url, headers=headers, timeout=20)
res.encoding = 'utf-8'
# 获取所需数据
HtmlStr = res.text
print(HtmlStr)
# 去除取到数据中的换行
html = HtmlStr.replace('\n', '')
# print(html)

# 视频名
PianMing = re.findall('class="title">(.*?)</a>', html)
print(PianMing)

# up主
Up = re.findall('alt="up">(.*?)</span>', html)
New_list=[]
for i in Up:
      New_list.append(i.replace(" ",""))
Up = New_list
print(Up)

# 播放量
BoFangLiang = re.findall('alt="play">(.*?)万', html)
New_list22=[]
for i in BoFangLiang:
      New_list22.append(i.replace(" ",""))
BoFangLiang = New_list22
print(BoFangLiang)

# 取整播放量，为方便制作图表
BoFangLiang2=[]
for i in BoFangLiang:
    data_list = re.findall(r"\d+", i)
    data_list = list(map(int, data_list[:]))
    str1 = data_list[0]
    BoFangLiang2.append(str1)
print(BoFangLiang2)

# 弹幕数
DanMuShu = re.findall('alt="like">(.*?)</span>', html)
New_list3=[]
for i in DanMuShu:
      New_list3.append(i.replace(" ",""))
DanMuShu = New_list3
print(DanMuShu)