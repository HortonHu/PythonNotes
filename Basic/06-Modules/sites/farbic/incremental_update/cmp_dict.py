# -*- coding:utf-8 -*-
import os
import json

BASE_DIR = r'C:\Users\K\Documents\codes\temp'
LOCAL_JSON = 'SVN1'
REMOTE_JSON = 'SVN'

# BASE_DIR = r'C:\Users\K\Documents\codes\PythonNotes\Basic\06-Modules\sites\farbic\incremental_update'
# LOCAL_JSON = 'module_test4'
# REMOTE_JSON = 'module_test'

with open(BASE_DIR + r'\{}.json'.format(LOCAL_JSON), 'r') as f:
    local_md5_dict = json.load(f)
with open(BASE_DIR + r'\{}.json'.format(REMOTE_JSON), 'r') as f:
    remote_md5_dict = json.load(f)

update_list = []


def get_path(directory):
    path_list = []
    for x in directory['children']:
        if x['type'] == 'file':
            path_list.append(x['path'])
        if x['type'] == 'directory':
            path_list.extend(get_path(x))
    return path_list


def check_md5(local_md5_dict, remote_md5_dict):
    if local_md5_dict['md5'] != remote_md5_dict['md5']:
        for x in local_md5_dict['children']:
            if x['type'] == 'directory':
                for y in remote_md5_dict['children']:
                    # 文件夹名称对应但是内容不同的情况
                    if y['type'] == 'directory' and y['name'] == x['name']:
                        if x['md5'] != y['md5']:
                            check_md5(x, y)
                        else:
                            break

                # 本地有目录 远程无目录 把本地目录下全部推送情况
                if x['name'] not in [y['name'] for y in remote_md5_dict['children'] if y['type'] == 'directory']:
                    update_list.extend(get_path(x))
            if x['type'] == 'file':
                for y in remote_md5_dict['children']:
                    if x['name'] == y['name'] and x['md5'] == y['md5']:
                        break
                else:
                    update_list.append(x['path'])

check_md5(local_md5_dict, remote_md5_dict)
print update_list


# try:
#     if local_md5_dict['md5'] != remote_md5_dict['md5']:
#         for x in local_md5_dict['children']:
#             for y in remote_md5_dict['children']:
#                 if x['md5'] == y['md5']:
#                     break
#             else:
#                 update_list.append(x['path'])
#         print update_list
# except KeyError, e:
#     update_list.extend([x['path'] for x in local_md5_dict['children']])
#
# print update_list


# def check(d1, d2):
#     if d1['md5'] == d2['md5']:
#         return []
#     else:
#         return None
#
# update_list.extend(check(local_md5_dict, remote_md5_dict))


# if local_md5_dict['md5'] != remote_md5_dict['md5']:
#     for x in local_md5_dict['children']:
#         if x['type'] == 'directory':
#             for y in remote_md5_dict['children']:
#                 if y['type'] == 'directory' and y['name'] == x['name']:     # 文件夹对应，只是文件不同的情况
#                     if x['md5'] == y['md5']:        # 两个文件夹MD5匹配
#                         break
#                     else:                           # 两个文件夹MD5不匹配的处理情况（包括文件增改两种情况）
#                         for xx in x['children']:
#                             for yy in y['children']:
#                                 if xx['md5'] == yy['md5']:
#                                     break
#                             else:
#                                 update_list.append(xx['path'])
#             else:   # 本地有目录 远程无目录 把本地目录下全部推送情况
#                 update_list.extend([xx['path'] for xx in x['children']])
#         if x['type'] == 'file':
#             for y in remote_md5_dict['children']:
#                 if x['md5'] == y['md5']:
#                     break
#             else:
#                 update_list.append(x['path'])
#
#
# print update_list
