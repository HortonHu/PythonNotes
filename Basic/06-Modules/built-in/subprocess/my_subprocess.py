# -*- coding:utf-8 -*-
# 用于替换os.system()和os.popen()
import subprocess


# 执行命令 打印返回值
subprocess.call('echo 123')

# 检查命令的返回的结果 不为1则报错
subprocess.check_call('echo 123')

