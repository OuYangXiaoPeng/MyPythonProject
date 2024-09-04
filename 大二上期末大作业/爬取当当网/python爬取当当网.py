import openpyxl
import requests
from lxml import etree

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = '图书数据'
sheet['A1'] = '书名'
sheet['B1'] = '价格'
sheet['C1'] = '时间'
sheet['D1'] = '作者'
sheet['E1'] = '出版社'
sheet['F1'] = '链接'

sheet.column_dimensions["A"].width = 55
sheet.column_dimensions["B"].width = 15
sheet.column_dimensions["C"].width = 20
sheet.column_dimensions["D"].width = 45
sheet.column_dimensions["E"].width = 25
sheet.column_dimensions["F"].width = 40


print('开始爬取数据：')


def get_page(key, page):
    for page in range(1, page + 1):
        url = 'http://search.dangdang.com/?key=' + key + '&act=input&sort_type=sort_score_desc&page_index=' + str(
            page) + '#J_tab'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
        }
        response = requests.get(url=url, headers=headers)
        parse_page(response)
        print('page %s over!!!' % page)


def parse_page(response):
    tree = etree.HTML(response.text)
    li_list = tree.xpath('//ul[@class="bigimg"]/li')
    # print(len(li_list))  # 测试
    for li in li_list:
        try:
            # 获取书的标题,并添加到列表中
            title = li.xpath('./a/@title')[0].strip()

            # 获取商品链接,并添加到列表中
            commodity_url = li.xpath('./p[@class="name"]/a/@href')[0]

            # 获取价格,并添加到列表中
            price = li.xpath('./p[@class="price"]/span[1]/text()')[0]

            # 获取作者,并添加到列表中
            author = ''.join(li.xpath('./p[@class="search_book_author"]/span[1]//text()')).strip()

            # 获取出版时间,并添加到列表中
            time = li.xpath('./p[@class="search_book_author"]/span[2]/text()')[0]

            # 获取出版社
            publis = ''.join(li.xpath('./p[@class="search_book_author"]/span[3]//text()')).strip()

            sheet.append([title, price, time, author, publis, commodity_url])

        except:
            pass



if __name__ == '__main__':
    key = input('请输入关键字：')
    page = int(input('请输入爬取的页数：'))
    # key = 'python'
    get_page(key, page)

    print('爬取完毕，在同目录查找表格文件')
    wb.save(key+'.xlsx')
