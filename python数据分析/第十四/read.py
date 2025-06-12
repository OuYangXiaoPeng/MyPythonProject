import csv

f = open("white-wine.csv", "r")
reader = csv.reader(f)
data = []
for row in reader:
    data.append(row)
# for i in range(5):
#     print(data[i])
f.close()
print(data[0])