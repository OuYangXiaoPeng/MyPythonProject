import os
import random
import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# 设置浏览器
options = Options()
options.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
options.add_argument('--disable-blink-features=AutomationControlled')
service = Service()

# 创建浏览器对象
driver = webdriver.Chrome(options=options, service=service)
driver.maximize_window()

# 打开网页
url = 'http://film.mtime.com/all/filmair'
driver.get(url)

# 等待页面加载完全
time.sleep(random.uniform(2, 4))

# 保存数据的列表
movie_data = []

# 如果已有CSV文件，则读取已有数据
csv_file = '时光电影top.csv'
if os.path.exists(csv_file):
    existing_df = pd.read_csv(csv_file)
    movie_data = existing_df.to_dict('records')
else:
    movie_data = []


def get_movie_details(detail_url):
    """获取电影详情页的额外信息"""
    details = {
        '剧情简介': '',
        '上映时间': '',
        '片长': '',
        '类型': '',
        '制片国家': '',
        '编剧': '',
        '更多片名': '',
        '发行公司': '',
        '主演详情': '',
        '导演': ''  # 添加导演字段
    }

    try:
        # 在新标签页中打开详情页
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(detail_url)

        # 等待详情页加载
        time.sleep(random.uniform(3, 5))

        try:
            # 获取头部信息 - 包含片长、类型和上映时间
            header = driver.find_element(By.CSS_SELECTOR, 'div.m_head')

            # 片长 (格式如"142分钟")
            try:
                duration = header.find_element(By.CSS_SELECTOR, 'div.otherbox > span:first-child').text
                if '分钟' in duration:
                    details['片长'] = duration.strip()
                else:
                    details['片长'] = ''
            except:
                pass

            # 类型 (可能有多个类型，用斜杠分隔)
            try:
                genres = [a.text for a in header.find_elements(By.CSS_SELECTOR, 'div.otherbox > span > a')]
                details['类型'] = '/'.join(genres)
            except:
                pass

            # 上映时间 (格式如"1994年9月23日")
            try:
                release_date = header.find_element(By.CSS_SELECTOR, 'div.otherbox > a').text
                details['上映时间'] = release_date.strip()
            except:
                pass

            # 制片国家/地区
            try:
                country = header.find_element(By.CSS_SELECTOR, 'div.otherbox > span:last-child').text
                details['制片国家'] = country.strip()
            except:
                pass

        except Exception as e:
            print(f"获取头部信息失败: ")

        try:
            # 获取剧情简介 - 更新选择器以匹配新结构
            plot_element = driver.find_element(By.CSS_SELECTOR, 'dt h4.px14.mt12 + p.mt6.moreEllipsis')
            details['剧情简介'] = plot_element.text
        except Exception as e:
            print(f"获取剧情简介失败:")

        try:
            # 获取左侧信息栏的所有dd元素
            info_items = driver.find_elements(By.CSS_SELECTOR, 'dl.info_l > dd')
            for item in info_items:
                text = item.text
                if '导演：' in text:
                    # 获取导演信息
                    directors = [a.text for a in item.find_elements(By.CSS_SELECTOR, 'a')]
                    details['导演'] = '/'.join(directors)
                elif '编剧：' in text:
                    # 获取所有编剧链接的文本
                    writers = [a.text for a in item.find_elements(By.CSS_SELECTOR, 'a')]
                    details['编剧'] = '/'.join(writers)
                elif '国家地区：' in text:
                    details['制片国家'] = item.find_element(By.CSS_SELECTOR, 'a.country').text.strip()
                elif '发行公司：' in text:
                    # 获取所有发行公司链接的文本
                    companies = [a.text for a in item.find_elements(By.CSS_SELECTOR, 'a')]
                    details['发行公司'] = '/'.join(companies)
                elif '更多片名：' in text:
                    details['更多片名'] = item.find_element(By.CSS_SELECTOR, 'span').text.strip()
        except Exception as e:
            print(f"获取左侧信息栏失败: ")

        try:
            # 获取右侧主演信息 - 更新选择器以匹配新结构
            actors = driver.find_elements(By.CSS_SELECTOR, 'ul.main_actor li')
            actors_list = []
            for actor in actors:
                try:
                    # 获取中文名
                    name_cn = actor.find_element(By.CSS_SELECTOR, 'dd p.__r_c_:first-child a').text
                    # 获取角色信息
                    role = actor.find_element(By.CSS_SELECTOR, 'dd p.__r_c_:last-child').text.replace('饰', '').strip()
                    actors_list.append(f"{name_cn} 饰 {role}")
                except:
                    continue
            details['主演详情'] = '; '.join(actors_list)
            # 同时设置主演字段为前几个主演名字
            details['主演'] = '; '.join([actor.split(' 饰')[0] for actor in actors_list[:3]])
        except Exception as e:
            print(f"获取主演信息失败:")

        # 关闭详情页标签，返回列表页
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(random.uniform(1, 2))

    except Exception as e:
        print(f"获取详情页信息失败: {str(e)}")
        # 确保返回主窗口
        if len(driver.window_handles) > 1:
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

    return details


# 等待电影列表加载
WebDriverWait(driver, 15).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.film_item'))
)

# 抓取电影榜单数据
movies = driver.find_elements(By.CSS_SELECTOR, 'div.film_item')

for idx, movie in enumerate(movies, 1):
    try:
        # 获取基础信息
        title = movie.find_element(By.CSS_SELECTOR, 'div.film_name a').text.strip()

        # 尝试获取评分
        try:
            score = movie.find_element(By.CSS_SELECTOR, 'div.film_score').text.strip()
        except:
            score = ''

        detail_url = movie.find_element(By.CSS_SELECTOR, 'div.img_content a').get_attribute('href')

        # 尝试获取图片URL
        try:
            img_url = movie.find_element(By.CSS_SELECTOR, 'div.img_content img').get_attribute('src')
        except:
            img_url = ''

        # 获取详情页信息
        print(f"正在获取《{title}》的详情信息...")
        details = get_movie_details(detail_url)

        # 合并数据
        movie_info = {
            '电影名称': title,
            '评分': score,
            '详情页URL': detail_url,
            '图片URL': img_url,
            '页码': "1",
            '本页序号': idx,
            **details  # 合并详情页信息
        }

        movie_data.append(movie_info)
        print(f"✓ 成功爬取: 《{title}》 (第{idx}部)")

    except Exception as e:
        print(f"× 第{idx}部电影爬取失败:")

# 保存数据
if movie_data:
    df = pd.DataFrame(movie_data)
    # 重新排列列顺序
    columns_order = ['电影名称', '导演', '主演', '评分', '类型', '上映时间', '片长', '制片国家',
                     '剧情简介', '编剧', '更多片名', '发行公司', '主演详情', '详情页URL', '图片URL',
                     '页码', '本页序号']
    # 只保留存在的列
    columns_order = [col for col in columns_order if col in df.columns]
    df = df[columns_order]

    # 追加模式写入CSV
    if os.path.exists(csv_file):
        # 读取现有数据
        existing_df = pd.read_csv(csv_file)
        # 合并新旧数据并去重
        combined_df = pd.concat([existing_df, df]).drop_duplicates(subset=['电影名称', '详情页URL'], keep='last')
        combined_df.to_csv(csv_file, index=False, encoding='utf-8-sig')
        print(f"\n✅ 成功追加 {len(df)} 条数据，总数据 {len(combined_df)} 条，已保存到 {csv_file}")
    else:
        df.to_csv(csv_file, index=False, encoding='utf-8-sig')
        print(f"\n✅ 成功爬取 {len(movie_data)} 条数据，已保存到 {csv_file}")
else:
    print("\n⚠️ 没有爬取到任何数据")

# 关闭浏览器
driver.quit()
