import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# 设置浏览器
options = Options()
options.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
service = Service()

# 获取用户输入
keyword = input("请输入书名:")

# 创建浏览器对象
driver = webdriver.Chrome(options=options, service=service)
driver.maximize_window()

# 发送请求
driver.get(f'https://www.ptpress.com.cn/search?keyword={keyword}')
time.sleep(3)

# 获取所有图书元素
books = driver.find_elements(By.CSS_SELECTOR, 'div.col-md-4.col-sm-6.col-xs-12')

# 提取每本书的信息
book_list = []
for book in books:
    try:
        book_list.append({
            '书名': book.find_element(By.CSS_SELECTOR, 'p').text,
            '链接': book.find_element(By.CSS_SELECTOR, 'a').get_attribute('href'),
            '图片': book.find_element(By.CSS_SELECTOR, 'img').get_attribute('src')
        })
    except Exception as e:
        print(f"提取数据时出错: {e}")

# 打印结果
for book in book_list:
    print(f"书名: {book['书名']}")
    print(f"链接: {book['链接']}")
    print(f"图片: {book['图片']}")
    print("-" * 50)

# 保存为CSV文件
if book_list:
    df = pd.DataFrame(book_list)
    df.to_csv(f'{keyword}_books.csv', index=False, encoding='utf_8_sig')  # utf_8_sig支持中文
    print(f"数据已保存到 {keyword}_books.csv")
else:
    print("未找到相关书籍")

# 关闭浏览器
driver.quit()
