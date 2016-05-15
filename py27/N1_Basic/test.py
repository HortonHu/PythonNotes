# -*- coding: utf-8 -*-

from email.mime.text import MIMEText
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
# 构造MIMEText对象时，第一个参数就是邮件正文，
# 第二个参数是MIME的subtype，传入'plain'，最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性。

# 通过SMTP发出去：
# 输入Email地址和口令:
from_addr = '857018659@qq.com'
password = raw_input('Password: ')
# 输入SMTP服务器地址:
smtp_server = 'smtp.qq.com'
# 输入收件人地址:
to_addr = 'wcbieyuan@gmail.com'

import smtplib
server = smtplib.SMTP(smtp_server, 25)     # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()