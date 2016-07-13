# -*- coding:utf-8 -*-


# SMTP
# SMTP是发送邮件的协议，Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件。
# Python对SMTP支持有smtplib和email两个模块
# email负责构造邮件
# smtplib负责发送邮件。


# 构造邮件
from email.mime.text import MIMEText
# 构造MIMEText对象时，
# 第一个参数就是邮件正文，
# 第二个参数是MIME的subtype，传入'plain'，最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性。
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
from_addr = 'weiyijingtu@sina.com'
password = raw_input('Input your password: ')
to_addr = raw_input('Input To email address : ')
smtp_server = 'smtp.sina.com'               # 输入SMTP服务器地址:

# 发送邮件
import smtplib
server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25 该端口可开启SSL
server.starttls()                       # 开启SSL
server.set_debuglevel(1)                # 用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
server.login(from_addr, password)       # login()方法用来登录SMTP服务器
server.sendmail(from_addr, [to_addr], msg.as_string())      # sendmail()方法发邮件
server.quit()
# SMTP协议就是简单的文本命令和响应
# 由于可以一次发给多个人，所以传入一个list，邮件正文是一个str，as_string()把MIMEText对象变成str
# 邮件主题、如何显示发件人、收件人等信息并不是通过SMTP协议发给MTA，而是包含在发给MTA的文本中的


# 必须把From、To和Subject添加到MIMEText中，才是一封完整的邮件：
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


# 格式化一个邮件地址。
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

from_addr = raw_input('From: ')
password = raw_input('Password: ')
to_addr = raw_input('To: ')
smtp_server = raw_input('SMTP server: ')

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'来自SMTP的问候……', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.starttls()       # 很多邮箱都要求SSL登陆 用25端口+TLS的方式实现SSL
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
# 注意不能简单地传入name <addr@example.com>，因为如果包含中文，需要通过Header对象进行编码。
# msg['To']接收的是字符串而不是list，如果有多个邮件地址，用,分隔即可


# 发送HTML邮件
# 在构造MIMEText对象时，把HTML字符串传进去，再把第二个参数由plain变为html就可以了：
msg = MIMEText('<html><body><h1>Hello</h1>' + '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8')


# 发送附件
# 构造一个MIMEMultipart对象代表邮件本身，
# 然后往里面加上一个MIMEText作为邮件正文，再继续往里面加上表示附件的MIMEBase对象即可：
# 邮件对象:
msg = MIMEMultipart()
msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'来自SMTP的问候……', 'utf-8').encode()

# 邮件正文是MIMEText:
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('/Users/michael/Downloads/test.png', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'png', filename='test.png')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='test.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)
# 按正常发送流程把msg（注意类型已变为MIMEMultipart）发送出去，就可以收到如下带附件的邮件：


# 发送图片
# 要把图片嵌入到邮件正文中，我们只需按照发送附件的方式，先把邮件作为附件添加进去
# 然后，在HTML中通过引用src="cid:0"就可以把附件作为图片嵌入了。
# 如果有多个图片，给它们依次编号，然后引用不同的cid:x即可。
# 把上面代码加入MIMEMultipart的MIMEText从plain改为html，然后在适当的位置引用图片：
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p><img src="cid:0"></p>' +
    '</body></html>', 'html', 'utf-8'))


# 同时支持HTML和Plain格式
# 如果收件人使用的设备太古老，查看不了HTML邮件怎么办？
# 办法是在发送HTML的同时再附加一个纯文本，如果收件人无法查看HTML格式的邮件，就可以自动降级查看纯文本邮件
# 利用MIMEMultipart就可以组合一个HTML和Plain，要注意指定subtype是alternative：
# msg = MIMEMultipart('alternative')
# msg['From'] = ...
# msg['To'] = ...
# msg['Subject'] = ...

msg.attach(MIMEText('hello', 'plain', 'utf-8'))
msg.attach(MIMEText('<html><body><h1>Hello</h1></body></html>', 'html', 'utf-8'))
# 正常发送msg对象


# 加密SMTP
# 使用标准的25端口连接SMTP服务器时，使用的是明文传输，发送邮件的整个过程可能会被窃听。
# 要更安全地发送邮件，可以加密SMTP会话，实际上就是先创建SSL安全连接，然后再使用SMTP协议发送邮件。
# Gmail，提供的SMTP服务必须要加密传输。我们来看看如何通过Gmail提供的安全SMTP发送邮件。
# Gmail的SMTP端口是587，因此，修改代码如下：
smtp_server = 'smtp.gmail.com'
smtp_port = 587
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
# 剩下的代码和前面的一模一样:
server.set_debuglevel(1)
# 只需要在创建SMTP对象后，立刻调用starttls()方法，就创建了安全连接。后面的代码和前面的发送邮件代码完全一样
# 现在很多邮箱通过25端口打开tls建立安全连接






