import re
import requests
#from bs4 import BeautifulSoup
#引入requests库和BeautifulSoup库
headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
#封装headers
url='http://www.weather.com.cn/weather1d/101040700.shtml#input'
#把URL链接赋值到变量url上。
res=requests.get(url,headers=headers)
#发送requests请求，并把响应的内容赋值到变量res中。
res.encoding='utf-8'
print(res.status_code)
#检查响应状态是否正常
print(res.text)
str1 = res.text
#打印出res对象的网页源代码
print(re.findall('''<div class="sk\smySkyNull"\w.*?</a></div>''',str1))
print(re.findall('<span class="name">.*?</span>',str1))


# import requests
# from bs4 import BeautifulSoup
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
# url = 'http://www.weather.com.cn/weather/101280601.shtml'
# res = requests.get(url, headers=headers, timeout=20)
# res.encoding = 'utf-8'
# # print(res.status_code)
# soup = BeautifulSoup(res.text, 'html.parser')
# tem_list = soup.find_all('p', class_='tem')  # 存温度
# # print(tem_list)
# day = soup.find('ul', class_='t clearfix')  # 存日期
# day_list = day.find_all('h1')
# # print(day_list)
# wealist = soup.find_all('p', class_='wea')  # 存天气
# day_pre = {}
# for i in range(1):
#     try:
#         temHigh = tem_list[i].span.string  # 有时候没有最高温度，用第二天的代替
#     except AttributeError as e:
#         temHigh = tem_list[i + 1].span.string
#     temLow = tem_list[i].i.string
#     wea = wealist[i].string
#     day_pre[day_list[i].string] = '最高温度：' + temHigh + ' 最低温度：' + temLow + ' 天气：' + wea
# print(day_pre)
