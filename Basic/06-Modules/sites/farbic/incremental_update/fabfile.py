# -*- coding:utf-8 -*-


import os
from fabric.api import *


env.user = 'horton'
env.password = 'hththt'
env.hosts = ['192.168.2.197']

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def update(*modules):
    # print 'hello'
    # run('ls /home', warn_only=True)
    # run('md5sum /home/horton/md5_test/1.txt', warn_only=True)
    # run('mkdir /home/horton/md5_test/files', warn_only=True)
    # put(os.path.join(BASE_DIR, 'files', '1.txt'), '/home/horton/md5_test/files/', use_sudo=True)

    for module in modules:
        REMOTE_DIR = os.path.join('/home/horton/md5_test/', module)
        for root, dirnames, files in os.walk(os.path.join(BASE_DIR, module)):
            for dirname in dirnames:
                run('mkdir {0}/{1}/{2}'.format(REMOTE_DIR,
                                               os.path.relpath(root, os.path.join(BASE_DIR, module)).replace('\\', '/'),
                                               dirname), warn_only=True)
            for f in files:
                local_file_path = os.path.join(BASE_DIR, module, os.path.relpath(root, os.path.join(BASE_DIR, module)), f)
                remote_file_path = '{0}/{1}'.format(REMOTE_DIR,
                                                    os.path.relpath(root, os.path.join(BASE_DIR, module)).replace('\\', '/')
                                                    )
                put(local_file_path, remote_file_path, use_sudo=True)




