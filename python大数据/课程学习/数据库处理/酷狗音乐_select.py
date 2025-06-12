import time

import pandas as pd
import pymysql
import requests
from bs4 import BeautifulSoup

pymysql.install_as_MySQLdb()
from sqlalchemy import create_engine  # 写数据库

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}
a = []


def get_info(url):
    wb_data = requests.get(url, headers=headers)  # 爬取网站
    soup = BeautifulSoup(wb_data.text, 'lxml')  # 因为爬取后的wb_data保存的网站数据不是大家熟悉的html格式，需要解析
    ranks = soup.select('span.pc_temp_num')  # 解析成网页格式后，然后就可以选择想要的数据，给大家演示的是用select函数，请大家完成Xpath和findAll
    titles = soup.select('a.pc_temp_songname')
    times = soup.select('span.pc_temp_time')
    for rank, title, time in zip(ranks, titles, times):  # zip叫拉链函数，配对。循环次数由最少得那列决定
        b = title.get_text().split('-')
        data = {
            "排名": rank.get_text().strip(),
            "歌名": b[0].strip(),
            "歌手": b[-1].strip(),
            "时间": time.get_text().strip(),
            "歌曲链接": title['href'].strip()
        }
        a.append(data)


if __name__ == '__main__':
    urls = [
        'http://www.kugou.com/yy/rank/home/1-8888.html'
    ]
    for url in urls:
        get_info(url)
        time.sleep(1)
    # a是Python的变量，列表里面嵌套字典，c是pandas的数据格式，这个是表格数据格式,第一行，第2列的值
    c = pd.DataFrame(a, columns=['排名', '歌名', '歌手', '时间', '歌曲链接', 'data-active'])

    # c.to_csv("酷狗音乐.csv", mode='a', index=False)
    # c.to_json("酷狗音乐.json")
    # c.to_excel("酷狗音乐.xlsx", index=False)
    # 先连上数据库，再把转换好的数据存到数据库中
    db = create_engine("mysql+mysqldb://root:123456@localhost:3306/大数据分析?charset=utf8")
    c.to_sql(name='酷狗音乐_数管5班', con=db, if_exists="append", index=False)
    # # #从数据库读数据
    # d=pd.read_sql("select * from 酷狗音乐_select",db)
    # print(d)
    # m=pd.read_csv("酷狗音乐.csv")
    # m=pd.read_json("酷狗音乐.json")
    # m=pd.read_excel("酷狗音乐.xlsx")
    # m=pd.read_sql("select * from 酷狗音乐_数管5班",db)
    # print(m.tail(10))
    db.dispose()
    # db1=pymysql.connect(
    #     host='localhost',
    #     port=3306,
    #     user='root',
    #     passwd='123456',
    #     db='大数据采集',
    #     charset='utf8'
    # )
    # p=db1.cursor()
    # p.execute("select delete update insert ")
    # db1.commit()
    # db1.close()
