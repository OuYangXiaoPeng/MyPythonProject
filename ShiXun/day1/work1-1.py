import os
path = "./cqipc"
target_file = "result2-2.txt"
filenames = os.listdir(path)
file = open(target_file,"w",encoding="utf-8")
for i in range(1, len(filenames)):
    temp = open("./cqipc/第{}段.txt".format(i), encoding="utf-8")
    data = temp.read()
    file.write(data+"\n")
    print(data)
file.close()