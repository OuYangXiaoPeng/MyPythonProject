import jieba
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud

try:
    from PIL import Image
except ImportError:
    import Image

Name = input("请输入要生成的章节（比如：1，2...61）\n")
path = "目录/第" + Name + "章.txt"


def get_Frequency():
    txt = open(path, "r", encoding='utf-8').read()  # 加载txt文本
    words = jieba.cut(txt)  # 返回可迭代的数据
    stop = open("stopwords.txt", "r", encoding='utf-8').read()  # 加载停用词表

    counts = {}  # 创建列表

    for word in words:
        if word not in stop:  # 去除停用词
            if len(word) == 1:
                continue  # 如果字长为1则去除
            else:
                counts[word] = counts.get(word, 0) + 1  # 字长不为1且不是停用词的词，频率加1
    items = list(counts.items())  # 转换为列表

    items.sort(key=lambda x: x[1], reverse=True)  # 对词频进行降序排序
    for i in range(15):  # 输出频率最高的前十五个词
        word, count = items[i]
        print("{0:<10}{1:<5}".format(word, count))  # 输出
    return items, counts


# 绘制云图
def makeImage(text):
    # 想生成带特定形状的词云，首先得准备具备该形状的mask图片
    # 在mask图片中除了目标形状外，其他地方都是空白的
    mask = np.array(Image.open("background.jpg"))

    wc = WordCloud(background_color="white", mask=mask, max_words=1000, repeat=True)
    wc.generate_from_frequencies(text)

    plt.axis("off")
    plt.imshow(wc, interpolation='bilinear')
    plt.show()

    # 绘制饼图
def draw_pie(labels, quants):
    # 做一个正方形的图形
    plt.figure(1, figsize=(6, 6))
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
    # 突出显示第一
    expl = [0.0] * len(quants)
    expl[0] = 0.1  # 第二块即China离开圆心0.1
    # 设置颜色（循环显示）
    colors = ["blue", "red", "coral", "green", "yellow", "orange"]
    # 绘制饼图
    # 百分数格式
    plt.pie(quants, explode=expl, colors=colors, labels=labels, autopct='%1.1f%%', pctdistance=0.8, shadow=True)
    plt.title('小说词频统计', bbox={'facecolor': '0.8', 'pad': 5})
    plt.show()
    plt.savefig("小说词频统计.jpg")
    plt.close()


if __name__ == "__main__":
    # 绘制词云
    fullTermsDict = get_Frequency()[1]
    # print(fullTermsDict)
    makeImage(fullTermsDict)

    # 绘制饼图(前15个词语)
    # labels: 词语
    itemList = get_Frequency()[0]
    print(itemList)
    # 设置要绘制的词语个数
    num = 15
    labels = []
    for i in range(0, num):
        labels.append(itemList[i][0])
    # quants: 出现次数
    quants = []
    for i in range(0, num):
        quants.append(itemList[i][1])
    draw_pie(labels, quants)
