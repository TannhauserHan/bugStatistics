from email.mime.base import MIMEBase
from ReOpenRateplot import *
import time
import smtplib,os
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email import encoders

from_addr = 'hanchang@xcdtech.cn'
password = 'vWJ8kgiTVNBrCWDB'
to_addr = 'hanchang@xcdtech.cn'

Date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
subject = str(Date) + " Bug统计"

newBugEverDayStr = Date + "-newBugEverDay.png"
Dev_Bug = Date + "-Bug.png"

def Mail():
    """
    邮件发送
    """
    msgRoot = MIMEMultipart('related')
    msgRoot['From'] = Header(str(Date) + " Bug统计",'utf-8')
    msgRoot['to'] = Header('xcd','utf-8')
    msgRoot['Subject'] = Header(subject,'utf-8')

    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)

    mail_msg = """
    <p><img src="cid:image1"></p>
    """
    msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))

    sendimagefile = open(Dev_Bug,'rb').read()
    msgInmage = MIMEImage(sendimagefile)
    msgInmage.add_header('Content-ID','<image1>')

    msgRoot.attach(msgInmage)

    try:
        smtp = smtplib.SMTP()
        smtp.connect('smtp.exmail.qq.com')
        smtp.login(from_addr,password)
        smtp.sendmail(from_addr,to_addr,msgRoot.as_string())
        smtp.quit()
        print("发送成功")
    except smtplib.SMTPException as e:
        print("error：发送失败")

#Mail()
def MailTwo():
    msgRoot = MIMEMultipart('related')
    msgRoot['From'] = Header(str(Date) + " Bug统计",'utf-8')
    msgRoot['to'] = Header('xcd','utf-8')
    msgRoot['Subject'] = Header(subject,'utf-8')

    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)

    allFlieList = os.listdir()
    content = '<br><br>'
    for index in range(len(allFlieList)):
        content +='<p><img src="cid:' + str(index) + '"></p>'
    index = 0
    for file in allFlieList:
        if file.find('png')>0:
            sendimagefile = open(file,'rb').read()
            mime = MIMEImage(sendimagefile)
            mime.add_header('Content-ID','<'+ str(index) + '>')
            index +=1
            msgRoot.attach(mime)
    msgAlternative.attach(MIMEText(content, 'html', 'utf-8'))
    try:
        smtp = smtplib.SMTP()
        smtp.connect('smtp.exmail.qq.com')
        smtp.login(from_addr,password)
        smtp.sendmail(from_addr,to_addr,msgRoot.as_string())
        smtp.quit()
        print("发送成功")
    except smtplib.SMTPException as e:
        print("error：发送失败")
Demo()
newBugEverDay()
MailTwo()