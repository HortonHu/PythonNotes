#!/usr/bin/env python
# -*- coding:utf-8 -*-
from . import db
from werkzeug.security import generate_password_hash, check_password_hash


# 定义模板类
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)                            # 设置id为主键
    name = db.Column(db.String(64), unique=True)                            # 不允许重复
    users = db.relationship('User', backref='role', lazy='dynamic')         # 建立关系

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))      # 将roles_id定义为外键

    def __repr__(self):
        return '<User %r>' % self.username

    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
