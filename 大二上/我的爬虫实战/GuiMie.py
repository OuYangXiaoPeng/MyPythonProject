import re
import requests

def getDanMU(url,JiShu):
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
    BV = re.findall('BV(.*?)[/"]', HtmlStr)
    # print(BV)

    # 将BV号拼接成cid号所在的网址
    cidlist = []
    for i in range(0,JiShu):
        cidURL = "https://api.bilibili.com/x/player/pagelist?bvid=" + BV[i] + "&jsonp=jsonp"
        # print(cidURL)

        # 读取网址中的cid
        res = requests.get(cidURL, headers=headers, timeout=20)
        res.encoding = 'utf-8'
        HtmlStr2 = res.text
        Cid = re.findall('"cid":(.*?),', HtmlStr2)[0]
        cidlist.append(Cid)
        print("第"+str(i+1)+"集Cid:" + Cid)
    # print(cidlist)
    return cidlist


def getDM(Cid):
    # 拼成弹幕链接
    DanMuurl = "https://comment.bilibili.com/" + Cid + ".xml"
    # print("弹幕链接:" + DanMuurl)

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

    # 放入b站连续剧视频链接
    url="https://www.bilibili.com/bangumi/play/ep267851?spm_id_from=333.337.0.0"
    # (url,集数)
    aa = getDanMU(url,26)
    # 将获取到的所有弹幕保存在dm列表
    dm=[]
    num = 0
    for i in aa:
        # print("第"+str(num+1)+"集:")
        bb=getDM(i)
        dm.append(bb)
        num += 1
    # print(dm)



    # 获取每集弹幕数
    DMSMax=0
    Ji=0
    for j in range(0, len(dm)):
        print("第"+str(j+1)+"集，弹幕数量："+str(len(dm[j])))
        if len(dm[j]) > DMSMax:
            DMSMax = len(dm[j])
            Ji = j
    print("第"+str(Ji+1)+"集最受欢迎，弹幕数量最多为:"+str(DMSMax))

    # 生成批量ecxel表
    for j in range(0, len(dm)):
        # 生成xls表
        import xlwt

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
        workbook.save('鬼灭之刃弹幕/弹幕{}.xls'.format(j+1))
