import requests
# response01=requests.get('https://www.cqipc.edu.cn')
# html_text=response01.text
# print(html_text)
# file1=open('baidu.text','w',encoding='utf-8')
# file1.write(html_text)
# file1.close()

path='https://www.cqipc.edu.cn/images/19/12/11/14wij5ezbv/'
list_len=0
for i in range(0,50):
    res = requests.get(path+'{}.jpg'.format(i),timeout=5)
    #print(res.status_code)
    status_code = "[" + str(res. status_code) + "]"
    if str(res.status_code)!="404":
        list_len+=1
        print(list_len)
def geturls(a):
    for i in range(1,a+1):
        url=path+"{}.jpg".format(i)
        print(url)
        # webbrowser.open(url)
        response01 = requests.get(url)
        html_text=response01.content
        file=open('图片/picture{}.jpg'.format(i),'wb')
        file.write(html_text)
    file.close()
    return
geturls(list_len)
