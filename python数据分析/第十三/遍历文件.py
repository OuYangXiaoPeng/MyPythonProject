# file = open("泰戈尔的诗.txt", mode="r", encoding="utf-8")
# content = file.read()
# print(content)
# file.close()
# print(type(content))

# import csv
# with open("student.csv") as f:
#     reader = csv.reader(f)
#     rows = [row for row in reader]
# for item in rows:
#     print(item)

import csv
contect = [
    ['0', 'hanmeimei', '23', '81'],
    ['1', 'mayi', '18', '99'],
    ['2', 'jack', '21', '89']
]
f = open('test.csv', 'w', newline='')
contect_out = csv.writer(f)
for con in contect:
    contect_out.writerow(con)
f.close()
