import smtplib
from email.header import Header
from email.mime.text import MIMEText

msg = MIMEText('重庆工业职业技术学院电物院21计应301','plain','utf-8')
msg['From'] = Header("2096008975@qq.com")
msg['To'] = Header("欧阳小鹏")
subject = "Python SMTP 邮件测试"
msg['Subject'] = Header(subject,"utf-8")

server = smtplib.SMTP_SSL("smtp.qq.com")
server.connect("smtp.qq.com",465)
server.login("2096008975@qq.com","qgbhsbqkjviqceeg")
server.sendmail("2096008975@qq.com","2096008975@qq.com",msg.as_string())
server.quit()
