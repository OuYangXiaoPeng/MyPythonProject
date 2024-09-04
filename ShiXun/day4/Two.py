import csv
from openpyxl import load_workbook
import smtplib
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# to_addrs = []
# while True:
#     a=input('请输入收件人邮箱:')#输入收件人邮箱
#     to_addrs.append(a)#写入列表
#     b=input('是否继续输入，n退出，任意键继续: ')#询问是否继续输入
#     if b == 'n':
#         break
def mail():
    headers = ["姓名","邮箱"]
    data = [headers,['欧阳小鹏','2096008975@qq.com']]
    with open('to_addrs.csv', 'w', encoding="GBK", newline="") as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)
    from pandas import read_csv

    f = open('./to_addrs.csv')
    data = read_csv(f)
    data.to_excel('./收件人目录.xlsx')


    with open('to_addrs.csv', 'r', encoding="GBK") as f:
        reader = csv.reader(f)
        for row in reader:
            to_addrs = row[1]

            text = '''我是21计应301xxx，此邮件中包含多个附件'''
            msg = MIMEMultipart()
            msg['From'] = Header("2096008975@qq.com")
            msg['To'] = Header(''.join(to_addrs))
            subject = "Python SMTP 邮件测试"
            msg['Subject'] = Header(subject, "utf-8")
            msg.attach(MIMEText(text))

    # 构造附件1，传送当前目录下的 test1.txt 文件
    xlsxFile = '收件人目录.xlsx'
    xlsxApart = MIMEApplication(open(xlsxFile, 'rb').read())
    xlsxApart.add_header('Content-Disposition', 'attachment', filename=xlsxFile)
    msg.attach(xlsxApart)

    xlsxFile = '21计应301.xlsx'
    xlsxApart = MIMEApplication(open(xlsxFile, 'rb').read())
    xlsxApart.add_header('Content-Disposition', 'attachment', filename=xlsxFile)
    msg.attach(xlsxApart)


    try:
        server = smtplib.SMTP_SSL("smtp.qq.com")
        server.connect("smtp.qq.com", 465)
        server.login("2096008975@qq.com", "qgbhsbqkjviqceeg")
        server.sendmail("2096008975@qq.com", to_addrs, msg.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("无法发送邮件")
    finally:
        server.quit()

if __name__ == '__main__':
    mail()