import re
import requests
import random


def spiderPic(html,keyword):
    print('正在查找'+keyword+'对应的图片下载中，请稍后...')
    for addr in re.findall('"objURL":"(.*?)"', html, re.S):  #查找URL
        print('正在爬取URL地址：' + str(addr)[0:30] + '...')# 爬取的地址长度超过30时，用'...'代替后面的内容
        try:
         pics = requests.get(addr, timeout=100)  # 请求URL时间(最大10秒)
        except requests.exceptions.ConnectionError:
         print('您当前请求的URL地址出现错误')
         continue
    fq = open('C:\\Users\\OYXP\\Pictures\\网页图片' + (keyword + '_' + str(random.randrange(0, 1000, 4)) + '.jpg'), 'wb')
    # 下载图片，并保存和命名
    fq.write(pics.content)
    fq.close()
