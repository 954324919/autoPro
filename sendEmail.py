#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
import email.MIMEMultipart
from email.header import Header
import os
import mimetypes

def send_email(receivers= ['2766905938@qq.com'], file_names=[], test_result=0):

    # 第三方 SMTP 服务
    print receivers
    mail_host="smtp.163.com"  #设置服务器
    mail_user="13051755990@163.com"    #用户名
    mail_pass="daqian123"   #口令,QQ邮箱是输入授权码，在qq邮箱设置 里用验证过的手机发送短信获得，不含空格
    sender = '13051755990@163.com'
    reciverstr="通过"

    #设置邮件中的测试结果
    if test_result==0:
        reciverstr="通过"
    else:
        reciverstr = "失败"

    main_msg = email.MIMEMultipart.MIMEMultipart()
    #message = MIMEText('附件是本次自动化构建的报告，请注意查收 \n\n', 'plain', 'utf-8')
    message = MIMEText('附件中为测试详细报告。 \n\n', 'plain', 'utf-8')
    main_msg.attach(message)
    #print reciverstr
    result = MIMEText('测试最终结果： '+reciverstr, 'plain', 'utf-8')
    main_msg.attach(result)
    ## 读入文件内容并格式化

    for file_name in file_names:
        data = open(file_name, 'rb')
        ctype,encoding = mimetypes.guess_type(file_name)
        if ctype is None or encoding is not None:
            ctype = 'application/octet-stream'
        maintype,subtype = ctype.split('/',1)
        file_msg = email.MIMEBase.MIMEBase(maintype, subtype)
        file_msg.set_payload(data.read())
        data.close()
        email.Encoders.encode_base64(file_msg)#把附件编码

        basename = os.path.basename(file_name)
        file_msg.add_header('Content-Disposition','attachment', filename = basename)#修改邮件头
        main_msg.attach(file_msg)


    main_msg['From'] = "13051755990@163.com"
    reciverstr = ';'.join(receivers)
    main_msg['To'] = reciverstr

    subject = '请查收测试结果'
    main_msg['Subject'] = subject


    try:
        smtpObj = smtplib.SMTP_SSL()
        smtpObj.connect(mail_host, 465)
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(sender, receivers, main_msg.as_string())
        print "邮件发送成功。"
    except smtplib.SMTPException, e:
        print "Error: 无法发送邮件。错误原因：", e


def sendEmail():
    # 第三方 SMTP 服务
    mail_host = "smtp.163.com"  # SMTP服务器
    mail_user = "13051755990@163.com"  # 用户名
    mail_pass = "daqian123"  # 授权密码，非登录密码

    sender = '13051755990@163.com'  # 发件人邮箱(最好写全, 不然会失败)
    receivers = ['2766905938@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    content = '我用Python'
    title = '测试'  # 邮件主题
    message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        print("mail has been send successfully.")
    except smtplib.SMTPException as e:
        print(e)

def send_email2(SMTP_host, from_account, from_passwd, to_account, subject, content):
    email_client = smtplib.SMTP(SMTP_host)
    email_client.login(from_account, from_passwd)
    # create msg
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')  # subject
    msg['From'] = from_account
    msg['To'] = to_account
    email_client.sendmail(from_account, to_account, msg.as_string())

    email_client.quit()

if __name__ == '__main__':
    send_email(file_names=['/Users/anthony/Desktop/white.txt'],test_result=1)
    #sendEmail()