import os
path = "./cqipc"
filenames = os.listdir(path)
for i in filenames:
    print(i)
target_file = "./result2"
file = open(target_file,"w",encoding="utf-8")
for i in filenames:
    file.write(i+"\n")
file.close()