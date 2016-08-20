# -*- coding:utf-8 -*-

import os
import json
import hashlib
import time

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# module = r'module_test'

BASE_DIR = r'C:\Users\K\Documents\codes\temp'
module = 'SVN'


def get_md5(file_path):
    md5 = hashlib.md5()
    with open(file_path, 'r') as f:
        md5.update(f.read())
    return md5.hexdigest()


def path_to_dict(path):
    d = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = []
        paths = [os.path.join(path, x) for x in os.listdir(path)]   # 所有子目录和子文件

        # Just the children that contains at least a valid file
        for p in paths:
            c = path_to_dict(p)
            if c is not None:
                d['children'].append(c)
        # 对于空文件夹
        if not d['children']:
            return None
        else:
            md5 = hashlib.md5()
            for c in d['children']:
                md5.update(c['md5'])
            d['md5'] = md5.hexdigest()
    else:
        d['type'] = "file"
        d['md5'] = get_md5(path)
        d['path'] = path
    return d

if __name__ == '__main__':
    start_time = time.clock()
    with open(BASE_DIR + r'\{}1.json'.format(module), 'w') as f:
        json.dump(path_to_dict(os.path.join(BASE_DIR, module)), f, indent=2)
    end_time = time.clock()
    print 'Total time:', end_time - start_time
