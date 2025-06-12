import pandas as pd

if __name__ == "__main__":
    data = pd.read_csv("../data/爬取数据.csv")
    # print(data.loc[25:35, ])
    # print(data.head(10))
    # print(data.tail(10))
    # print(data.dtypes)

    # pandas中 先列 后行
    # del data['总价']#删除列  del方便
    # data.drop(columns='总价',inplace=True)#inplace 在原数据上直接操作
    # 删除指定的行
    del_index = data[data['编号'] == '编号'].index
    print(del_index)
    data.drop(labels=del_index, inplace=True)  # inplace 在原数据上直接操作

    # for i in range(1,data["编号"]+1):
    #     data["编号"][i-1] = i

    data.reset_index(inplace=True)  # 重置索引
    del data['编号']
    del data['index']
    data.reset_index(inplace=True, names='编号')  # 重置索引
    # print(data)

    # 重置 '编号' 列，使其从 0 开始连续排列
    # data['编号'] = range(len(data))
    # print(data['编号'])

    # 存储数据
    # a = [1, 2, 3, 4]
    # with open("../data/aaa.csv", "w+") as f:#r+      w+:会自动创建
    #     f.write(str(a[0]))
    data.to_csv("../data/初步清洗.csv", index=False)
