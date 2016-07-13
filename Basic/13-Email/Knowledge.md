MUA: Mail User Agent     —— 邮件用户代理
MTA: Mail Transfer Agent —— 邮件传输代理
MDA: Mail Delivery Agent —— 邮件投递代理
一封电子邮件的旅程就是:
发件人 -> MUA -> MTA -> 若干个MTA -> MDA <- MUA <- 收件人

要编写程序来发送和接收邮件，本质上就是：
1. 编写MUA把邮件发到MTA；
2. 编写MUA从MDA上收邮件。

发邮件时，MUA和MTA使用的协议就是SMTP：Simple Mail Transfer Protocol，后面的MTA到另一个MTA也是用SMTP协议。
收邮件时，MUA和MDA使用的协议有两种：
POP：Post Office Protocol，目前版本是3，俗称POP3；
IMAP：Internet Message Access Protocol，目前版本是4，优点是不但能取邮件，还可以直接操作MDA上存储的邮件
