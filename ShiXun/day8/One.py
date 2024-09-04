import re
string2 = '''Together, we discovered that a free market discovered only thrives when there are rules to
ensure competition and fair discovered play, Together celebration of initiative and enterprise Together'''
print(re.search('\w*o\w*',string2, flags = re.I).group(0))
print(re.findall('Together',string2, flags = re.I))
print(re.findall('discovered',string2, flags = re.I))

print()
s2= '此次新朗逸主要搭载了1.5L和1.5T两种动力总成的发动机。别克英朗则搭载了1.0T和1.3T的动力总成。'
print(re.findall('1...' ,s2))
print(re.findall('1\...',s2))

print()
s3='距离2019北京马拉松开跑只有两周时间了，\n 今年的北京马拉松预报名人数超过16万人，\t媒体公布的中签率只有16%左右，再创历年来的新低。\n '
print(s3)
print(re.sub('\s','',s3))

print()
s4= '用户联系方式:13612345566，用户编号为11011254321'
print(re.findall('1[356789]\d\d\d\d\d\d\d\d\d', s4))
s5= '通过对比新朗逸1.5L和1.5T两种动力在1.5年行驶期后的数据。发现1.5T的口碑相对较好!'
print(re.findall('1.5[a-zA-Z]',s5))

print()
s6 = 'id:1, name:Tom, age:3, gender:1; id:2, name:Lily, age:5, gender:O'
print(re.findall('\d',s6))
print(re.findall('age:\d',s6))
print(re.findall('age:(\d)',s6))

#超链接的匹配
print()
URL1 = 'https://www.baidu.com/'
URL2 = 'http://www.gov.cn/ '
pattern = 'https?://www\..*?'
print(re.findall(pattern,URL1))

#邮箱地址的匹配
print()
email1 = 'Lsxxx2011@163.com'
email2 = '654088115@qq.com'
pattern = '[0-9a-zA-Z_\.\-]+@[a-zA-Z0-9_1-]+\.com'
print(re.findall(pattern,email2))

#提取出产品名称中含奶粉字样的产品
print()
prod =['婴儿袜','亨氏奶粉','奶粉勺','多功能奶瓶','幼儿奶粉量筒','磨牙棒']
res = []
for i in prod:
    res.extend(re.findall('.*奶粉.*', i))
print(res)

#取出字符中所有的天气状态
print()
string1 = "{ymd:'2018-01-01',tianqi:'晴' aqilnfo:轻度污染'}{ymd:2018-01-O2',tianqi:阴~小雨'aqilnfo:优},fymd:2018-01-03',tianqi:'小雨~中雨' aqilnfo:'优',ymd:2018-01-04',tianqi'中雨~小雨',aqilnfo:'优}"
print(re.findall("tianqi:'(.*?)'", string1))

#将每一部分的内容分割开
print()
string4 = '2室2厅|101.62平|低区/7层|朝南\n上海未来–浦东–金杨-2005年建'
split = re.split('[-\|\n]', string4)
print(split)
split_strip = [i.strip() for i in split]
print(split_strip)
