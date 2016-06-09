#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required


# 定义表单类
class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')
