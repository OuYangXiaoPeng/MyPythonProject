# 网络爬虫入门
# 采集数据来源是 来源于我们的序列数据
# 网络数据上需分配来源
# 数据需要路沉淀 具体的页数和编号 连续的页面变化
# 找3个可以采集数据的页面
# 构造出不同的链接
# https://cq.lianjia.com/ershoufang/pg2/
def a():
    LianJia = []
    for i in range(0, 100):
        LianJia.append("https://cq.lianjia.com/ershoufang/pg{}/".format(i + 1))
    print(LianJia)
def b():
    URLS = map(lambda x: "https://cq.lianjia.com/ershoufang/pg{}/".format(x),
            [i for i in (1, 101)]
            )
    for url in URLS:
        print(url)
def c():
    import requests
    from bs4 import BeautifulSoup
    headers={
        "User-Agnet":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52"
    }
    data=requests.get("https://cq.lianjia.com/ershoufang/pg1/",headers=headers)
    text = data.text
    mysoup = BeautifulSoup(text,"html5lib")
    print(mysoup.text)

if __name__ == "__main__":
    # a()
    # b()
    c()