#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
from flask import current_app
from app import create_app, db


class BasicsTestCase(unittest.TestCase):
    def setUp(self):                                   # 创建测试环境
        self.app = create_app('testing')                # 创建程序
        self.app_context = self.app.app_context()
        self.app_context.push()                         # 激活程序上下文
        db.create_all()                                 # 创建一个全新的数据库

    def tearDown(self):
        db.session.remove()
        db.drop_all()                                   # 删除数据库
        self.app_context.pop()                          # 删除程序上下文

    # 测试确保程序实例存在
    def test_app_exists(self):
        self.assertFalse(current_app is None)

    # 测试确保程序在测试配置中运行
    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])
