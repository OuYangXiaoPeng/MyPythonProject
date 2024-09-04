import string
from collections import Counter

import matplotlib.pyplot as plt

strText = "Thank you very much. I've just received a call from Secretary Clinton. Shecongratulated us. It is about " \
          "us. On our victory, and I congratulated her and herfamily on a very, very hard-fought campaign I mean she " \
          "fought very hard.Hillaryhas worked very 1ong and very hard over a long period of time, and we owe her " \
          "amajor debt of gratitude for her service to our country. I mean that verysincerely "


# 统计词频
def statistics(data):
    count = Counter(data)
    print(count)
    values = []
    keys = []
    for key, value in count.items():
        keys.append(key)
        values.append(value)
    print(keys)
    print(values)
    return keys, values


# 绘制为柱状图
def drowing(X, lenList):
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
    # 分辨率参数-dpi，画布大小参数-figsize
    plt.figure(dpi=144, figsize=(16, 7))
    # 改变文字大小参数-fontsize
    plt.xticks(fontsize=8, rotation=60)
    plt.bar(X, lenList, 0.8, color="green", linestyle='-', linewidth=3)
    for a, b in zip(X, lenList):  # 柱子上的数字显示5
        plt.text(a, b, '%d' % b, ha='center', va='bottom', fontsize=15)
    plt.xlabel("单词", fontsize=20)
    plt.ylabel("出现数", fontsize=20)
    plt.title("分词词频柱状图", bbox={'facecolor': '0.8', 'pad': 15})
    plt.show()
    plt.savefig("分词词频柱状图.jpg")
    plt.close()


# 获取单词
data = []
upconnect = strText.upper()
newconnect = upconnect.strip()
words = newconnect.split()
for word in words:
    data1 = word.strip(string.punctuation)
    data.append(data1)
print(data)

strList = statistics(data)
drowing(strList[0], strList[1])
