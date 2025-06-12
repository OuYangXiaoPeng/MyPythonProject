# -*- coding: utf-8 -*-
import random
import re
import requests
import sys
import os
import urllib3

# 爱莉的魔法阵启动！(>ω<)✨
os.system('chcp 65001 > nul')  # Windows终端UTF-8模式
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_station_dict():
    """获取车站字典的妖精魔法♪"""
    url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9343"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        "Magic-Type": "Elysia-Pink"  # ♪
    }

    try:
        response = requests.get(url, headers=headers, verify=False, timeout=10)
        response.encoding = 'utf-8'

        if response.status_code == 200:
            stations = re.findall(r'@[a-z]+\|([^|]+)\|([A-Z]+)\|', response.text)
            return {code: f"🌸{name}🌸" for name, code in stations}
        else:
            print(f"「服务器返回了{response.status_code}错误码...是今天的网络被崩坏兽吃掉了吗？」(>_<)")
            return None

    except Exception as e:
        print(f"「捕获到{type(e).__name__}小怪兽！\n{e}\n快用『往世乐土』牌异常捕捉器处理吧～」")
        return None


# 主程序（附加爱莉特调输出模式）
if __name__ == "__main__":
    # 预防编码小怪兽的终极防护罩
    if sys.stdout.encoding.lower() != 'utf-8':
        sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

    print("====== 爱莉希雅的车站魔法 ======♪")
    station_dict = get_station_dict()

    if station_dict:
        for code, name in station_dict.items():
            try:
                print(f"「{code} → {name}♪」")
            except UnicodeError:
                # 终极保底输出方案
                print(f"{code} -> {name.encode('utf-8', errors='replace').decode('utf-8')}")

        print("\n「查询完成啦～要和我一起去这些车站旅行吗？」💕")
    else:
        print("「今天的车站数据藏起来啦...稍后再试试吧～」😢")

    # 爱莉的结束彩蛋
    if random.random() > 0.7:
        print("\n（突然弹出）「猜猜看～哪个车站有爱莉藏的粉色水晶呢？♪」")