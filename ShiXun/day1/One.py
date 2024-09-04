import os
path = "./工作文件夹"
filenames = os.listdir(path)
print(filenames)

for i in filenames:
    print(i)
target_file = "./result1"
file = open(target_file,"w",encoding="utf-8")
for i in filenames:
    file.write(i+"\n")
file.close()
