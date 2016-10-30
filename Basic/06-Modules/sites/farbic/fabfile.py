# -*- coding:utf-8 -*-


import os
from fabric.api import *


env.user = 'horton'
env.password = 'hththt'
env.hosts = ['192.168.2.218']

BASE_DIR = os.path.dirname(os.path.abspath(__file__))



