#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask, request, render_template, make_response, redirect, abort, url_for
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

from datetime import datetime

# 初始化
app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

# app.config 字典可用来存储框架、扩展和程序本身的配置变量。
# SECRET_KEY 配置变量是通用密钥，可在 Flask 和多个第三方扩展中使用。
# 密钥不应该直接写入代码，而要保存在环境变量中
app.config['SECRET_KEY'] = 'SSSKey'


@app.route('/', methods=['GET', 'POST'])
def home():
    user_agent = request.headers.get('User-Agent')
    return render_template('home.html', user_agent=user_agent, current_time=datetime.utcnow())


@app.route('/formtest', methods=['GET', 'POST'])
def form_test():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
    form.name.data = ''
    return render_template('form_test.html', form=form, name=name)


@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')


@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)


@app.route('/user/<username>')
def show_name(username):
    real_loc = url_for('show_name', username=username, _external=True)
    return render_template('user.html', name=username, real_loc=real_loc)


@app.route('/<int:user_num>')
def show_user_num(user_num):
    return '<h1>Your Number is %s</h1>' % user_num


# 产生cookies
@app.route('/makecookie')
def make_cookies():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response


# 重定向
@app.route('/redirect')
def do_redirect():
    return redirect('http://www.baidu.com')


# 错误处理
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


# 定义表单类
class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')

if __name__ == '__main__':
    app.run()
    # manager.run()