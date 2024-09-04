import re


import requests


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
    #获取BV号
    BV=re.findall('BV(.*?)[/"]',HtmlStr)[0]
    print("BV号:"+BV)
    # 将BV号拼接成cid号所在的网址
    cidURL = "https://api.bilibili.com/x/player/pagelist?bvid="+BV+"&jsonp=jsonp"
    print(cidURL)

    # 读取网址中的cid
    res = requests.get(cidURL, headers=headers, timeout=20)
    res.encoding = 'utf-8'
    HtmlStr2 = res.text
    Cid = re.findall('"cid":(.*?),',HtmlStr2)[0]
    print("Cid:"+Cid)

    # 拼成弹幕链接
    DanMuurl="https://comment.bilibili.com/"+Cid+".xml"
    print("弹幕链接:"+DanMuurl)

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
    print("字符串从短到长:")
    print(DanMu)

    # 选择排序
    # for i in range(0, len(DanMu) - 1):
    #     for j in range(i + 1, len(DanMu)):
    #         if(len(DanMu[i])>len(DanMu[j])):
    #             temp=DanMu[i]
    #             DanMu[i] = DanMu[j]
    #             DanMu[j]=temp
    # print(DanMu)

    # 冒泡排序
    # for i in range(0, len(DanMu) - 1):
    #     flag = 0
    #     for j in range(0, len(DanMu) - 1 - i):
    #         if (len(DanMu[j]) > len(DanMu[j + 1])):
    #             temp = DanMu[j]
    #             DanMu[j] = DanMu[j + 1]
    #             DanMu[j + 1] = temp
    #             flag = 1
    #     if (flag == 0):
    #         break
    # print(DanMu)

    # 筛选田小娥并加入Name
    Name=[]
    for i in DanMu:
        if "田小娥" in i:
            Name.append(i)
    print(Name)


    # 生成xls表
    import xlwt

    workbook = xlwt.Workbook(encoding='utf-8', style_compression=0)
    worksheet = workbook.add_sheet('sheet1', cell_overwrite_ok=True)
    worksheet2 = workbook.add_sheet('田小娥', cell_overwrite_ok=True)

    # 加入表头
    worksheet.write(0,0,"弹幕内容")
    worksheet2.write(0,0,"有田小娥的")

    # 写入弹幕
    for i in range(0, len(DanMu)):
        worksheet.write(i + 1, 0, DanMu[i])

    # 写入有关田小娥的弹幕
    for i in range(0, len(Name)):
        worksheet2.write(i + 1, 0, Name[i])

    # xls的行距设置
    first_col = worksheet.col(0)  # 从零开始算，第一列
    first_col.width = 256 * 50

    # 保存文件
    workbook.save('白鹿原弹幕.xls')



if __name__ == '__main__':

    # 放入b站视频链接
    url="https://www.bilibili.com/bangumi/play/ep184661?theme=movie&spm_id_from=333.337.0.0"
    getDanMU(url)


