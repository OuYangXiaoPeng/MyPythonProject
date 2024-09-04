import os
import re

import requests


def getDir():
    # 如果存在，过
    if os.path.exists('白鹿原弹幕'):
        pass
    # 否则创建
    else:
        os.mkdir('白鹿原弹幕')


def getDanMU(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42'}
    res = requests.get(url, headers=headers, timeout=20)
    res.encoding = 'utf-8'
    # 获取所需数据
    HtmlStr = res.text
    # print(HtmlStr)

    # 获取cid
    # 获取BV号
    BV = re.findall('BV(.*?)[/"]', HtmlStr)[0]
    # print(BV)

    # 将BV号拼接成cid号所在的网址
    cidURL = "https://api.bilibili.com/x/player/pagelist?bvid=" + BV + "&jsonp=jsonp"
    # print(cidURL)

    # 读取网址中的cid
    res = requests.get(cidURL, headers=headers, timeout=20)
    res.encoding = 'utf-8'
    HtmlStr2 = res.text
    Cid = re.findall('"cid":(.*?),', HtmlStr2)
    print(Cid)
    # print(cidlist)
    return Cid


def getDM(Cid):
    # 拼成弹幕链接
    DanMuurl = "https://comment.bilibili.com/" + Cid + ".xml"
    print("弹幕链接:" + DanMuurl)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42'}
    res = requests.get(DanMuurl, headers=headers, timeout=20)
    res.encoding = 'utf-8'
    # 获取所需数据
    HtmlStr3 = res.text
    # print(HtmlStr1)

    # 弹幕
    DanMu = re.findall('">(.*?)</d>', HtmlStr3)
    # print(DanMu)

    # python自带的排序方法
    DanMu.sort(key=len)
    # print("字符串从短到长:")
    # print(DanMu)

    return DanMu


if __name__ == '__main__':

    # 生成目录
    getDir()

    # 放入b站连续剧视频链接
    url = "https://www.bilibili.com/video/BV1vx411a7Au/?p=1&vd_source=fb6e1ac116ccc9d971544c9e84cc2149"
    # (url,集数)
    aa = getDanMU(url)
    # 将获取到的所有弹幕保存在dm列表
    dm = []
    for i in aa:
        bb = getDM(i)
        dm.append(bb)
    # print(dm)

    # 获取每集弹幕数
    DMSMax = 0
    Ji = 0
    for j in range(0, len(dm)):
        print("第" + str(j + 1) + "集，弹幕数量：" + str(len(dm[j])))
        if len(dm[j]) > DMSMax:
            DMSMax = len(dm[j])
            Ji = j
    print("第" + str(Ji + 1) + "集最受欢迎，弹幕数量最多为:" + str(DMSMax))

    # 生成批量ecxel表
    import xlwt
    for j in range(0, 6):
        # 生成xls表

        workbook = xlwt.Workbook(encoding='utf-8', style_compression=0)
        worksheet = workbook.add_sheet('sheet1', cell_overwrite_ok=True)
        # 加入表头
        worksheet.write(0, 0, "弹幕内容")
        # 写入弹幕
        num = 0
        for i in range(0, len(dm[j])):
            worksheet.write(i + 1, 0, dm[j][i])

        # xls的行距设置
        first_col = worksheet.col(0)  # 从零开始算，第一列
        first_col.width = 256 * 50

        # 保存文件
        workbook.save('白鹿原弹幕/弹幕{}.xls'.format(j + 1))
