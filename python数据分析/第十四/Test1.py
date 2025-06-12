import csv

f = open("white-wine.csv", "r")
reader = csv.reader(f)
data = []
for row in reader:
    data.append(row)
for i in range(5):
    print(data[i])
f.close()

quality_list = []
for row in data[1:]:
    quality_list.append(int(row[-1]))
quality_count = set(quality_list)
print("白葡萄酒共有%d种等级，分别是:%r" % (len(quality_count), quality_count))

content_dict = {}
for row in data[1:]:
    quality = int(row[-1])
    if quality not in content_dict:
        content_dict[quality] = []
    content_dict[quality].append(row)
for key in content_dict:
    print(key, ":", len(content_dict[key]))
print()


mean_list = []
for key, value in content_dict.items():
    sum = 0
    for row in value:
        sum += float(row[0])  # fixed acidity是第一列
    mean_list.append((key, sum / len(value)))
for item in mean_list:
    print(item[0], ":", item[1])
