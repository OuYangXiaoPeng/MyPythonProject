import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def clawData():
    # 设置浏览器
    options = Options()
    options.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    service = Service()

    # 创建浏览器对象
    driver = webdriver.Chrome(options=options, service=service)
    driver.maximize_window()

    # 发送请求
    driver.get('https://www.cqupt.edu.cn/')
    time.sleep(3)

    # 获取所有顶级菜单项
    top_menu_items = driver.find_elements(By.CSS_SELECTOR, 'ul.wrap.page-navs > li')
    listD = []

    for item in top_menu_items:
        try:
            # 获取顶级菜单名称和链接
            a_tag = item.find_element(By.TAG_NAME, 'a')
            menu_name = a_tag.text.strip()
            menu_link = a_tag.get_attribute('href')

            # 先添加主菜单项
            listD.append({
                '菜单名称': menu_name,
                '链接': menu_link,
                '菜单类型': '主菜单',
                '父菜单': ''
            })

            # 尝试展开子菜单（悬停操作）
            try:
                ActionChains(driver).move_to_element(item).perform()
                time.sleep(0.5)  # 等待子菜单展开
            except:
                pass

            # 检查是否有子菜单
            sub_menus = item.find_elements(By.CSS_SELECTOR, 'ul.page-navs-inner li a')

            for sub_menu in sub_menus:
                sub_name = sub_menu.text.strip()
                sub_link = sub_menu.get_attribute('href')

                # 只有当子菜单名称存在且不等于父菜单名称时才添加
                if sub_name and sub_name != menu_name:
                    listD.append({
                        '菜单名称': sub_name,
                        '链接': sub_link,
                        '菜单类型': '子菜单',
                        '父菜单': menu_name
                    })

        except Exception as e:
            print(f"提取数据时出错: {e}")

    # 关闭浏览器
    driver.quit()
    return listD


def save_to_csv(data, filename):
    with open(filename, mode='w', encoding='utf-8-sig', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['菜单名称', '链接', '菜单类型', '父菜单'])
        writer.writeheader()
        writer.writerows(data)
    print(f"数据已保存到 {filename}")


if __name__ == '__main__':
    # 采集数据
    data = clawData()

    # 保存到CSV
    csv_filename = '重邮大官网菜单.csv'
    save_to_csv(data, csv_filename)

    # 打印结果
    print(f"共采集到 {len(data)} 条菜单数据：")
    for idx, d in enumerate(data, 1):
        menu_display = f"{d['父菜单']} > {d['菜单名称']}" if d['父菜单'] else d['菜单名称']
        print(f"{idx}. {d['菜单类型']}: {menu_display}")
        print(f"   链接: {d['链接']}")
        print("-" * 60)