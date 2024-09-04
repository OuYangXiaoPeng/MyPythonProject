import os
import re

import requests
from bs4 import BeautifulSoup


def a():
    file = open("小说目录2.txt", encoding="utf-8")
    mulu = file.read()
    id = re.findall('<a href="(.*?)" target', mulu)
    name = re.findall('">第(.*?)</a>', mulu)
    # print(id)
    # print(name)

    h = []
    for i in id:
        h.append("https:" + i)

    n = []
    for i in name:
        n.append("第" + i)

    print(h)
    print(n)
    return h


def b(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42'}
    res = requests.get(url, headers=headers, timeout=20)
    res.encoding = 'utf-8'
    HtmlStr = res.text
    id = re.findall('<div class="read-content j_readContent" id="(.*?)">', HtmlStr)[0]
    soup = BeautifulSoup(HtmlStr, "html5lib")
    txt = []
    cnt = 0
    for i in (soup.select("#{}".format(id), encoding='utf-8')[0]):
        if cnt != 0 and cnt != len((soup.select("#{}".format(id), encoding='utf-8')[0])) - 1:
            txt.append(i.text)
        cnt += 1
    # print(txt)
    return txt

def getDir():
    # 如果存在，过
    if os.path.exists('目录'):
        pass
    # 否则创建
    else:
        os.mkdir('目录')


def c(filenames):
    for i in range(len(filenames)):
        print("正在写入第" + str(i + 1) + "章")
        file = open("目录/第{}章.txt".format(i + 1), "w", encoding="utf-8")
        for j in filenames[i]:
            file.writelines(j + "\n")
        print("第" + str(i + 1) + "章写入完成！")
    file.close()


if __name__ == "__main__":
    # 调用函数a()生成每章对应的链接和章节名
    aa = a()

    # 将章节链接保存在ZhangJIe列表
    ZhangJie = []
    for i in aa:
        ZhangJie.append(b(i))
    # print(ZhangJie)

    # 生成  目录 文件夹
    getDir()

    # 调用函数c()写入到目录下
    c(ZhangJie)
