import csv
import json
import requests
import time
import random
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# 配置参数
BASE_URL = "https://www.v2ex.com/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Connection": "keep-alive",
    "Referer": "https://www.v2ex.com/",
}


def scrape_v2ex():
    """采集V2EX社区数据"""
    print("开始采集V2EX社区数据...")
    try:
        time.sleep(random.uniform(2, 5))  # 随机延迟

        session = requests.Session()
        session.headers.update(HEADERS)
        response = session.get(BASE_URL, timeout=30, verify=False)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        items = soup.select("div.cell.item")

        results = []
        for item in items:
            title_element = item.select_one('span.item_title a.topic-link')
            category_element = item.select_one('a.node')

            if title_element and category_element:
                results.append({
                    'title': title_element.get_text(strip=True),
                    'link': urljoin(BASE_URL, title_element['href']),
                    'category': category_element.get_text(strip=True)
                })

        return results

    except Exception as e:
        print(f"请求出错: {e}")
        return []


# 保存数据的函数（保持不变）
def save_to_csv(data, filename='v2ex_data.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['title', 'link', 'category'])
        writer.writeheader()
        writer.writerows(data)
    print(f"CSV 文件已保存: {filename}")


if __name__ == "__main__":
    data = scrape_v2ex()

    if data:
        # 打印前3条数据预览
        print("采集到的前3条数据:")
        for i, item in enumerate(data[:3], 1):
            print(f"{i}. 标题: {item['title']}")
            print(f"   链接: {item['link']}")
            print(f"   分类: {item['category']}")
            print("-" * 60)

    if data:
        save_to_csv(data)
        save_to_json(data)
        print(f"采集完成，共 {len(data)} 条数据")
    else:
        print("采集失败，请检查网络或反爬设置")