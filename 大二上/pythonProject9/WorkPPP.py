#输入一个单词
import string

word = input("请输入一个单词:")
# 把单词中所有字母转大写
word1 = list(word.upper())
# print(word1)
# 复习def使用
for i in word1:
    print(i.strip())
def getword(words):
    myword = []
    return myword
#利用字典统计 counter
# from collections import Counter
# c = Counter();
# print(c)
# pyecharts  代码
# 统计的数值：画个词云图
# 自己去找个长文本
# 中文词云
file = open("英语学习计划.txt", encoding="utf-8")
data = file.readlines()
# print(data)
