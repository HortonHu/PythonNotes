# -*- coding:utf-8 -*-
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REMOTE_DIR = '/home/horton/md5_test/files'

for root, dirnames, filenames in os.walk(os.path.join(BASE_DIR, 'files')):
    # print root, dirnames, filenames
    # print os.path.relpath(root, os.path.join(BASE_DIR, 'files')).replace('\\', '/')
    for f in filenames:
        local_file_path = os.path.join(BASE_DIR, 'file', os.path.relpath(root, os.path.join(BASE_DIR, 'files')), f)
        remote_file_path = '{0}/{1}'.format(REMOTE_DIR,
                                            os.path.relpath(root, os.path.join(BASE_DIR, 'files')).replace('\\', '/')
                                            )
        print f, local_file_path, remote_file_path


