# -*- coding:utf-8 -*-
import time

# 时间戳 → 本地时间元祖，默认当前时间
print time.localtime()
print time.localtime(0)
# 时间戳 → 格林威治天文时间下的时间元组 0时区的时间
print time.gmtime()
print time.gmtime(0)

# 时间元组 → 一个可读的形式为Weekday Month Day HH:MM:SS Year的字符。
print time.asctime(time.localtime())

# 时间元组 → 时间辍
print time.mktime(time.localtime())

# 返回当前时间，相当于 time.asctime(time.localtime())
print time.ctime()
time.sleep(1)
print time.ctime()

# 返回当前时间的时间戳
print time.time()

# time.strftime(fmt[,tupletime])
# 接收以时间元组，并返回字符串。
print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

# 输出参数中，格式化字符串的含义：
# 格式化字符串	日期/时间单元	范围
# %Y	        年	            1900-...
# %m	        月	            12-Jan
# %B	        月名	        January,...
# %b	        月名缩写	    Jan,...
# %d	        日	            31-Jan
# %A	        星期	        Sunday,...
# %a	        星期缩写	    Sun,...
# %H	        时(24时制)	    00-23
# %I	        时(12时制)	    12-Jan
# %p	        上午/下午	    AM,PM
# %M	        分	00-59
# %S	        秒	00-59