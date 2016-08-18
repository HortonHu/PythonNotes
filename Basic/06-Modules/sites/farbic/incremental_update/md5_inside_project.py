# -*- coding:utf-8 -*-
import os
import hashlib
import time

# BASE_DIR = r'C:\Users\K\Desktop\test'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
module = 'module_test'

start_time = time.clock()
for root, dir_list, file_list in os.walk(os.path.join(BASE_DIR, module), topdown=False):
    md5_list = []

    # 计算一个目录下所有文件的md5和文件名 加入md5_list
    for filename in file_list:
        if filename != (os.path.basename(root) + '.md5'):
            local_file_path = os.path.join(BASE_DIR, module, os.path.relpath(root, os.path.join(BASE_DIR, module)), filename)
            with open(local_file_path) as f:
                md5 = hashlib.md5()
                md5.update(f.read())
                md5_list.append('  '.join([md5.hexdigest(), filename]))

    # 计算一个目录下所有从子目录计算得到的MD5文件 然后写入当前目录的文件的md5 加入md5_list
    for dir_name in dir_list:
        local_file_path = os.path.join(BASE_DIR, module, os.path.relpath(root, os.path.join(BASE_DIR, module)), dir_name) + '.md5'
        with open(local_file_path) as f:
            md5 = hashlib.md5()
            md5.update(f.read())
            md5_list.append('  '.join([md5.hexdigest(), dir_name + '.md5']))

    # 父目录下存一个MD5
    with open(os.path.join(os.path.dirname(root), os.path.basename(root)+'.md5'), 'w') as md5_file:
        md5 = hashlib.md5()
        md5.update(''.join(md5_list))
        md5_file.write(md5.hexdigest())
        print md5.hexdigest(), os.path.basename(root)

    # 当前目录存一个MD5
    with open(os.path.join(root, os.path.basename(root) + '.md5'), 'w') as md5_file:
        md5_file.write('\n'.join(md5_list))

    temp_time = time.clock()
    print 'Time passed: ', temp_time - start_time