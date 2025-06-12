import random
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

# 设置请求头
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
}

# 线程安全的列表用于存储结果
a = []
lock = threading.Lock()

def get_data(url):
    try:
        # 随机延迟防止被封
        time.sleep(random.uniform(1, 2))

        # 1.获取整个网页
        data = requests.get(url, headers=header, timeout=10)
        data.raise_for_status()  # 检查请求是否成功

        # 2.解析网页内容
        data_h = BeautifulSoup(data.text, 'lxml')

        # 3.选择需要的数据
        title = data_h.select("div.title > a")
        address = data_h.select("div.positionInfo")
        info = data_h.select("div.houseInfo")
        time_info = data_h.select("div.followInfo")
        price = data_h.select("div.totalPrice.totalPrice2")
        unitprice = data_h.select("div.unitPrice")

        page_data = []

        for t, addr, inf, tm, total, uprice in zip(title, address, info, time_info, price, unitprice):
            add1 = addr.get_text().split("-")
            info1 = inf.get_text().split("|")
            time1 = tm.get_text().split("/")

            b = {
                "标题": t.get_text().strip(),
                "总价": total.get_text().strip(),
                "单价": uprice.get_text().strip(),
                "小区": add1[0].strip(),
                "街道": add1[-1].strip(),
                "户型": info1[0].strip(),
                "面积": info1[1].strip(),
                "朝向": info1[2].strip(),
                "装修": info1[3].strip(),
                "楼层": info1[4].strip(),
                "楼型/时间": info1[5].strip(),
                "关注度": time1[0].strip(),
                "时间": time1[1].strip(),
            }
            page_data.append(b)

        # 使用锁保证线程安全
        with lock:
            a.extend(page_data)

        print(f"成功采集: {url}")
        return True

    except Exception as e:
        print(f"采集{url}时出错: {e}")
        return False


def save_to_csv():
    """保存数据到CSV文件"""
    df = pd.DataFrame(a, columns=['标题', '总价', '单价', '小区', '街道',
                                  '户型', '面积', '朝向', '装修', '楼层', '楼型/时间',
                                  '关注度', '时间'])
    df.to_csv("爬取数据.csv", index=True, index_label='编号')
    print("数据已保存到CSV文件")


if __name__ == '__main__':
    page = int(input("请输入你要爬取多少页: "))

    # 创建线程池 (建议4-8个线程)
    with ThreadPoolExecutor(max_workers=4) as executor:
        # 提交所有任务
        futures = []
        for i in range(1, page + 1):
            url = f"https://cq.lianjia.com/ershoufang/pg{i}"
            futures.append(executor.submit(get_data, url))

        # 等待所有任务完成
        for future in as_completed(futures):
            future.result()  # 可以获取返回值或处理异常

    # 所有线程完成后保存数据
    save_to_csv()
    print(f"共爬取{len(a)}条数据")