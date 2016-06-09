# -*- coding:utf-8 -*-
import os
import ConfigParser

basedir = os.path.abspath(os.path.dirname(__file__))
cf = ConfigParser.ConfigParser()
cf.readfp(open('mydata.ini'))


# 定义Config基类
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

    # Database
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True        # 请求结束后都会自动提交数据库中的变动

    # Mail
    MAIL_SERVER = 'smtp.sina.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USERNAME = cf.get("MAIL", "MAIL_USERNAME")
    MAIL_PASSWORD = cf.get("MAIL", "MAIL_PASSWORD")
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


# 注册不同的配置环境
# 3 个子类中SQLALCHEMY_DATABASE_URI 变量都被指定了不同的值。这样程序就可在不同的配置环境中运行，每个环境都使用不同的数据库
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}