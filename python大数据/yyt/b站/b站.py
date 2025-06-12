import csv
import re
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# 设置浏览器选项
options = Options()
options.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("--mute-audio")  # 静音模式
# options.add_argument('--headless')  # 无头模式，不显示浏览器窗口

# 启动服务
service = Service()

# 创建浏览器对象
driver = webdriver.Chrome(options=options, service=service)
driver.maximize_window()

# 打开目标页面
url = 'https://www.bilibili.com/v/popular/rank/all'
driver.get(url)

# 等待页面加载
time.sleep(5)

# 获取页面 HTML
html = driver.page_source
html = html.replace('\n', '').replace(' ', '')

# 视频url
VideoUrl = re.findall('class="img"><ahref="//(.*?)"target="_blank"><img', html)
# print("视频URL:", VideoUrl)

# up主
Up = re.findall('8176975z"fill="currentColor"></path></svg>(.*?)</span></a><divclass="detail-state">', html)
# print("UP主:", Up)

# 存储视频详情数据
video_details = []

# 爬取的数据量（自己调节，一共是有100条应该是都能拿到的）
num = 10
# 遍历每个视频URL获取详情
for i, url in enumerate(VideoUrl[:num]):
    try:
        full_url = f"https://{url}"
        print(f"\n正在处理视频 {i + 1}: {full_url}")

        # 打开新标签页
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(full_url)

        # 等待页面加载
        time.sleep(5)  # 增加等待时间确保数据加载

        # 获取视频页面HTML
        video_html = driver.page_source
        cleaned_html = video_html.replace('\n', '').replace(' ', '')

        # 关闭当前标签页
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

        # 视频名
        title_match = re.search(r'<h1[^>]*?title="([^"]*)"', video_html)
        PianMing = title_match.group(1) if title_match else "N/A"

        # 播放量
        view_match = re.search(r'<divclass="view-text"[^>]*?>(.*?)</div>', cleaned_html)
        BoFangLiang = view_match.group(1) if view_match else "N/A"

        # 提取发布时间
        displaytime = re.findall(r'<divclass="pubdate-ip-text"[^>]*?>(.*?)</div>', cleaned_html)
        if displaytime:
            # 处理时间格式：在日期和时间之间添加空格
            # 从 "2025-05-1012:28:17" 变成 "2025-05-10 12:28:17"
            displaytime_str = re.sub(r'(\d{4}-\d{2}-\d{2})(\d{2}:\d{2}:\d{2})', r'\1 \2', displaytime[0])
        else:
            displaytime_str = "N/A"


        # 提取弹幕数
        danmu = re.findall(r'<divclass="dm-text"[^>]*?>(.*?)</div>', cleaned_html)
        danmu_count = danmu[0] if danmu else "N/A"

        # 提取点赞数
        like = re.search(r'<spanclass="video-like-info[^>]*?>(.*?)</span>', cleaned_html)
        like_count = like.group(1) if like else "N/A"

        # 提取投币数
        coin = re.search(r'<spanclass="video-coin-info[^>]*?>(.*?)</span>', cleaned_html)
        coin_count = coin.group(1) if coin else "N/A"

        # 提取收藏数
        favorite = re.search(r'<spanclass="video-fav-info[^>]*?>(.*?)</span>', cleaned_html)
        favorite_count = favorite.group(1) if favorite else "N/A"

        # 提取分享数
        share = re.search(r'<spandata-v-12f7cbf0=""class="video-share-info-text">(.*?)</span>', cleaned_html)
        share_count = share.group(1) if share else "N/A"

        # 存储视频详情
        video_details.append({
            "序号": i + 1,
            "视频标题": PianMing,
            "视频URL": full_url,
            "UP主": Up[i] if i < len(Up) else "N/A",
            "播放量": BoFangLiang,
            "发布时间": displaytime_str,
            "弹幕数": danmu_count,
            "点赞数": like_count,
            "投币数": coin_count,
            "收藏数": favorite_count,
            "转发数": share_count
        })

        print(f"视频 {i + 1} 详情数据获取成功")
        print(f"标题: {PianMing}, UP主: {Up[i]}, 播放量: {BoFangLiang}")
        print(f"发布时间: {displaytime_str}")
        print(
            f"弹幕数: {danmu_count}, 点赞数: {like_count}, 投币数: {coin_count}, 收藏数: {favorite_count}, 转发数: {share_count}")

    except Exception as e:
        print(f"处理视频 {i + 1} 时出错: {str(e)}")
        # 确保回到主窗口
        if len(driver.window_handles) > 1:
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
        continue

# 关闭浏览器
driver.quit()

# 保存为CSV文件
csv_filename = 'b站top.csv'
with open(csv_filename, mode='w', encoding='utf-8-sig', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=[
        "序号", "视频标题", "视频URL", "UP主", "播放量", "发布时间",
        "弹幕数", "点赞数", "投币数", "收藏数", "转发数"
    ])
    writer.writeheader()
    writer.writerows(video_details)

print(f"\n数据已保存到 {csv_filename}")
