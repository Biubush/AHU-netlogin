#!python3

#引用和初始化
import requests
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header
mail_host="smtp.qq.com"#这里填smtp服务器地址，用若QQ邮箱则无需更改
mail_user=""#这里填用来发送邮件的邮箱
mail_pass=""#这里填smtp密码
sender = ''#这里填用来发送邮件的邮箱
receivers = ['']#这里填你要发送对象的邮箱
url = ''#这里填你抓取的网址

#取中间文本函数
def get_mid_str(s, start_str, stop_str):
    start_pos = s.find(start_str)
    if start_pos == -1:
        return None
    start_pos += len(start_str)
    stop_pos = s.find(stop_str, start_pos)
    if stop_pos == -1:
        return None
    return s[start_pos:stop_pos]

#脚本主部分
print("脚本已启动！")
var = 1
success = 0
while var == 1 :
    response = requests.get(url)
    text = response.text
    returncode = get_mid_str(text, 'result":"', '","msg')
    if returncode == '1' :
        success = success + 1
        times = str(success)
        message = MIMEText('自上次启动脚本开始，你的服务器已为您自动登陆了'+times+'次校园网！', 'plain', 'utf-8')
        message['From'] = Header("校园网登陆", 'utf-8')
        message['To'] =  Header("接收者", 'utf-8')
        subject = '自动登录'+times+'次'
        message['Subject'] = Header(subject, 'utf-8')
        time.sleep(2)
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(mail_host, 25)#25是smtp端口号，有需要才改
            smtpObj.login(mail_user,mail_pass)
            smtpObj.sendmail(sender, receivers, message.as_string())
            print ("脚本成功执行了"+times+'次')
        except smtplib.SMTPException:
            print ("Error: 发送邮件失败")