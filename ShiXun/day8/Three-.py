import requests
from bs4 import BeautifulSoup
from lxml import etree


# 获取页面的html并返回etree
def get_html_tree(url, headers):
    resp = requests.get(url, headers=headers).text
    resp_tree = etree.HTML(resp)
    return resp_tree


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
url = 'http://list.mtime.com/movieDetail/300773'

# HtmlElement = get_html_tree(url, headers)
# HtmlStr = etree.tostring(HtmlElement,encoding='utf-8').decode()

res = requests.get(url, headers=headers, timeout=20)
res.encoding = 'utf-8'
HtmlStr = res.text
print(HtmlStr)

soup = BeautifulSoup(HtmlStr, 'html.parser')
name_list = soup.find_all('div', class_='tname')  # 存片名
print(name_list)
year_list = soup.find_all('div', class_='tdata')  # 存年代
print(year_list)
score_list = soup.find_all('div', class_='circle red')  # 存序号
print(score_list)

# day_pre = {}
# for i in range(7):
#     name = name_list[i].string
#     year = year_list[i].string
#     score = score_list[i].div.string
#     print(name)
#     print(year)
#     print(score)
