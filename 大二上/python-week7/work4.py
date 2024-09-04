import string

import pyecharts.options as opts
from pyecharts.charts import WordCloud

file = open("英语学习计划.txt", encoding="utf-8")
content = file.read()

data = []
upconnect = content.upper()
newconnect = upconnect.strip()
words = newconnect.split()
for word in words:
    aa = word.strip(string.punctuation)
    data.append(aa)
print()

# 导入这个统计器
from collections import Counter
count = Counter(data)
data2=[]
for i in count:
    t = (i, count[i])
    data2.append(t)
print(data2)

(
    WordCloud()
    .add(series_name="英语词云图", data_pair=data2, word_size_range=[15, 100])
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="英语词云图", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
        ),
        tooltip_opts=opts.TooltipOpts(is_show=True),
    )
    .render("basic_wordcloud.html")
)
import webbrowser

webbrowser.open("basic_wordcloud.html")
