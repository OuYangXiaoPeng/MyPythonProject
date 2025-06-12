import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

url = 'https://m.che168.com/carlist/index'

try:
    # 发送请求
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    # 解析HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    data = []
    car_cards = soup.find_all('div', class_='css-175oi2r', recursive=True)

    for card in car_cards:
        try:
            # 提取车辆标题
            title_elem = card.find('div', class_=lambda x: x and 'r-8akbws' in x)
            title = title_elem.get_text(strip=True) if title_elem else ""

            # 提取详细信息
            details_elem = card.find('div', style=lambda x: x and 'color: rgb(102, 109, 127)' in x)
            details = details_elem.get_text(strip=True) if details_elem else ""

            # 分割详细信息
            details_parts = details.split(' / ') if details else []
            year = details_parts[0] if len(details_parts) > 0 else ""
            mileage = details_parts[1] if len(details_parts) > 1 else ""
            shop_info = details_parts[2] if len(details_parts) > 2 else ""

            # 提取价格
            price_elem = card.find('div', style=lambda x: x and 'color: rgb(255, 102, 0)' in x)
            price = price_elem.get_text(strip=True) if price_elem else ""

            # 提取城市
            city_elem = card.find('div', style=lambda
                x: x and 'background: linear-gradient(rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.6))' in x)
            city = city_elem.get_text(strip=True) if city_elem else ""

            if title:
                data.append({
                    '标题': title,
                    '上牌年份': year,
                    '行驶里程': mileage,
                    '城市': city,
                    '店铺信息': shop_info,
                    '价格(万)': price
                })
        except Exception as e:
            print(f"提取车辆信息时出错: {e}")
            continue

    # 保存数据
    df = pd.DataFrame(data)
    if not df.empty:
        df.to_csv('che168_car_list.csv', index=False, encoding='utf_8_sig')
        print(f"成功爬取{len(data)}条数据")
        print(df.head())
    else:
        print("未找到有效数据")

except requests.exceptions.RequestException as e:
    print(f"请求出错: {e}")
except Exception as e:
    print(f"其他错误: {e}")