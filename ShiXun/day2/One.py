import csv
file = open(r"./表格等文件/test1.txt","r",encoding="utf-8")
filereader = file.readlines()
file.close()
# print(filereader)
str1 = filereader[0]
list1 =str1.split(",")
# print(list1)
list1.insert(2," ")
list1.insert(2," ")
# print(list1)
a_list=[]
for i in range(0,len(list1),4):
    name = list1[i:i+4]
    # print(name)
    a_list.append(name)
print(a_list)

with open('test_tar.csv', 'w', encoding='GBK', newline='') as target_file:
    target_writer = csv.writer(target_file)
    for line in a_list:
          target_writer.writerow(line)