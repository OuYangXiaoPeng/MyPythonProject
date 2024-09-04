import csv
import re
import requests
class Weather:
    # 定义目标url以及headers信息
    def __init__(self):
        self.url = 'http://www.weather.com.cn/weather/101040100.shtml'
        self.headers = {
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42"
        }
    def Get_Html(self):
        html = requests.get(url=self.url, headers=self.headers)
        return html.content.decode('utf-8')
    def parse_html(self):
        resoult = self.Get_Html()
        print(resoult)
        uls = re.match(r'.*?(<ul class="t clearfix">.*?</ul>).*?', resoult, re.S).group(1)
        lis = re.findall(r'<li.*?>.*?</li>', uls, re.S)
        pattern = re.compile(
            r'<li.*?">.*?<h1>(.*?)</h1>.*?<p.*?>(.*?)</p>.*?<span>(.*?)</span>.*?<i>(.*?)</i>.*?<i>(.*?)</i>.*?</li>',
            re.S)
        lists = []
        for i in lis:
            r = pattern.match(i)
            print(r.group(1), r.group(2), r.group(3), r.group(4), r.group(5))
            lit = [r.group(1), r.group(3), r.group(4)]
            lists.append(lit)
        return lists
    def save_data(self):
        data = self.parse_html()
        # print(data)
        title = ("日期", '最高温度', "最低温度")
        with open('./天气.csv', 'w', encoding='GBK', newline='') as f:
            write = csv.writer(f)
            write.writerow(title)
            write.writerows(data)
if __name__ == '__main__':
    res = Weather()
    res.save_data()

from pandas import read_csv
f = open('./天气.csv')
data = read_csv(f)
data.to_excel('./天气.xlsx')
