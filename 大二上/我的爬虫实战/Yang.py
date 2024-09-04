import re
import string
from collections import Counter

import pandas
import pyecharts.options as opts
import requests
import xlrd
import xlwt
from pyecharts.charts import WordCloud


def a(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42'}
    res = requests.get(url, headers=headers, timeout=20)
    res.encoding = 'utf-8'
    HtmlStr = res.text
    res = requests.get(url, headers=headers, timeout=20)
    res.encoding = 'utf-8'
    HtmlStr = res.text
    BV = re.findall('"bvid":"BV(.*?)",', HtmlStr)[0]
    cidURL = "https://api.bilibili.com/x/player/pagelist?bvid=" + BV + "&jsonp=jsonp"
    res = requests.get(cidURL, headers=headers, timeout=20)
    res.encoding = 'utf-8'
    HtmlStr2 = res.text
    Cid = re.findall('"cid":(.*?),', HtmlStr2)[0]
    DanMuurl = "https://comment.bilibili.com/" + Cid + ".xml"
    return DanMuurl


def b(url):
    DanMuurl = a(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42'}
    res = requests.get(DanMuurl, headers=headers, timeout=5)
    res.encoding = 'utf-8'
    HtmlStr1 = res.text
    # print(HtmlStr1)
    return HtmlStr1


# 处理完毕
def c(url):
    HtmlStr1 = b(url)
    DanMu = re.findall('">(.*?)</d>', HtmlStr1)
    # print(DanMu)
    for i in range(0, len(DanMu) - 1):
        flag = 0
        for j in range(0, len(DanMu) - 1 - i):
            if (len(DanMu[j]) > len(DanMu[j + 1])):
                temp = DanMu[j]
                DanMu[j] = DanMu[j + 1]
                DanMu[j + 1] = temp
                flag = 1
        if (flag == 0):
            break
    return DanMu


def d(url, a):
    DanMu = c(url)
    workbook = xlwt.Workbook(encoding='utf-8', style_compression=0)
    worksheet = workbook.add_sheet('sheet1', cell_overwrite_ok=True)
    worksheet.write(0, 0, "弹幕内容")
    for i in range(0, len(DanMu)):
        worksheet.write(i + 1, 0, DanMu[i])
    first_col = worksheet.col(0)
    first_col.width = 256 * 100
    workbook.save(a)


def e(p1):
    length = len(p1)
    p2 = ''
    for i in range(length - 1, -1, -1):
        if p1[i] == '.':
            break
    for j in range(0, i + 1):
        p2 = p2 + p1[j]
    p2 = p2 + 'txt'
    return p2


def f(p1, p2):
    df = pandas.read_excel(p1, header=None)
    df.to_csv(p2, header=None, sep=',', index=False)


def g(a):
    file = open(a + ".txt", encoding="utf-8")
    content = file.read()
    content = str.upper(content)
    connect = content.strip()
    words = connect.split()
    # print(words)
    data = []
    for word in words:
        connect = word.strip(string.punctuation)
        # print(connect)
        data.append((connect))

    d = Counter(data)
    # print(d)
    data2 = []
    for i in d:
        t = (i, d[i])
        data2.append(t)
    (
        WordCloud()
        .add(series_name="词云", data_pair=data2, word_size_range=[20, 3])
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="词云", title_textstyle_opts=opts.TextStyleOpts(font_size=50)
            ),
            tooltip_opts=opts.TooltipOpts(is_show=True),
        )
        .render(a + ".html")
    )


def h():
    DanMu = c(url)
    Name = []
    for i in DanMu:
        if "田小娥" in i:
            Name.append(i)
    # for i in range(0, len(Name) - 1):
    #     for j in range(i + 1, len(Name)):
    #         if (len(Name[i]) > len(Name[j])):
    #             temp = Name[i]
    #             Name[i] = Name[j]
    #             Name[j] = temp
    for i in range(0, len(Name) - 1):
        flag = 0
        for j in range(0, len(Name) - 1 - i):
            if (len(Name[j]) > len(Name[j + 1])):
                temp = Name[j]
                Name[j] = Name[j + 1]
                Name[j + 1] = temp
                flag = 1
        if (flag == 0):
            break
    workbook = xlwt.Workbook(encoding='utf-8', style_compression=0)
    worksheet = workbook.add_sheet('sheet1', cell_overwrite_ok=True)
    worksheet.write(0, 0, "弹幕内容")
    for i in range(0, len(Name)):
        worksheet.write(i + 1, 0, Name[i])
    first_col = worksheet.col(0)
    first_col.width = 256 * 100
    workbook.save('./生成/b站弹幕(田小娥).xls')


def a2(url, i):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42'}
    res = requests.get(url, headers=headers, timeout=20)
    res.encoding = 'utf-8'
    HtmlStr = res.text
    res = requests.get(url, headers=headers, timeout=20)
    res.encoding = 'utf-8'
    HtmlStr = res.text
    BV = re.findall('"bvid":"BV(.*?)",', HtmlStr)[i]
    cidURL = "https://api.bilibili.com/x/player/pagelist?bvid=" + BV + "&jsonp=jsonp"
    res = requests.get(cidURL, headers=headers, timeout=20)
    res.encoding = 'utf-8'
    HtmlStr2 = res.text
    Cid = re.findall('"cid":(.*?),', HtmlStr2)[0]
    DanMuurl = "https://comment.bilibili.com/" + Cid + ".xml"
    return DanMuurl


def b2(url, i):
    DanMuurl = a2(url, i)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42'}
    res = requests.get(DanMuurl, headers=headers, timeout=5)
    res.encoding = 'utf-8'
    HtmlStr1 = res.text
    # print(HtmlStr1)
    return HtmlStr1


# 处理完毕
def c2(url, i):
    HtmlStr1 = b2(url, i)
    DanMu = re.findall('">(.*?)</d>', HtmlStr1)
    # print(DanMu)
    for i in range(0, len(DanMu) - 1):
        flag = 0
        for j in range(0, len(DanMu) - 1 - i):
            if (len(DanMu[j]) > len(DanMu[j + 1])):
                temp = DanMu[j]
                DanMu[j] = DanMu[j + 1]
                DanMu[j + 1] = temp
                flag = 1
        if (flag == 0):
            break
    return DanMu


def d2(url, a, i):
    DanMu = c2(url, i)
    workbook = xlwt.Workbook(encoding='utf-8', style_compression=0)
    worksheet = workbook.add_sheet('sheet1', cell_overwrite_ok=True)
    worksheet.write(0, 0, "弹幕内容")
    for i in range(0, len(DanMu)):
        worksheet.write(i + 1, 0, DanMu[i])
    first_col = worksheet.col(0)
    first_col.width = 256 * 100
    workbook.save(a)


def d3(url, i):
    DanMu = c2(url, i)
    workbook = xlwt.Workbook(encoding='utf-8', style_compression=0)
    worksheet = workbook.add_sheet('sheet{}'.format(i), cell_overwrite_ok=True)
    worksheet.write(0, 0, "弹幕内容")
    for i in range(0, len(DanMu)):
        worksheet.write(i + 1, 0, DanMu[i])
    first_col = worksheet.col(0)
    first_col.width = 256 * 100
    workbook.save("./鬼灭之刃/总.xls")


def roww(f, num, row):
    file = xlrd.open_workbook(f)
    sheet = file.sheet_by_index(num)
    row = sheet.row_values(row)
    return row


def coll(f, num, col):
    file = xlrd.open_workbook(f)
    sheet = file.sheet_by_index(num)
    col = sheet.col_values(col)
    return col


if __name__ == '__main__':
    # url = "https://www.bilibili.com/bangumi/play/ep184661?theme=movie&spm_id_from=333.337.0.0"
    # # url="https://www.bilibili.com/video/BV1cd4y1v7uN/?spm_id_from=444.41.list.card_archive.click&vd_source=fb6e1ac116ccc9d971544c9e84cc2149"
    # d(url,'./生成/b站弹幕.xls')
    # p1 = './生成/b站弹幕.xls'
    # p2 = e(p1)
    # f(p1, p2)
    # g("./生成/b站弹幕")
    # h()
    # p1 = './生成/b站弹幕(田小娥).xls'
    # p2 = e(p1)
    # f(p1, p2)
    # g("./生成/b站弹幕(田小娥)")

    cnt = []
    for i in range(1, 10):
        url = "https://www.bilibili.com/bangumi/play/ep26785{}?from_spmid=666.25.episode.0".format(i)
        print(url)
        path1 = "./鬼灭之刃/第{}集.xls".format(i)
        path2 = "./鬼灭之刃/第{}集".format(i)
        d2(url, path1, i - 1)
        # d3(url, i)
        p1 = path1
        p2 = e(p1)
        f(p1, p2)
        g(path2)
        num = 0
        for p in coll(path1, 0, 0):
            num += 1
        cnt.append(num)
    for j in cnt:
        print(j)
    DanMu = cnt
    workbook = xlwt.Workbook(encoding='utf-8', style_compression=0)
    worksheet = workbook.add_sheet('sheet1', cell_overwrite_ok=True)
    worksheet.write(0, 0, "弹幕内容")
    for i in range(0, len(DanMu)):
        worksheet.write(i + 1, 0, DanMu[i])
    first_col = worksheet.col(0)
    first_col.width = 256 * 20
    workbook.save("./生成/弹幕数量.xls")
