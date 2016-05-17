#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask, request, render_template, make_response, redirect, abort, url_for
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)                   # 初始化
# manager = Manager(app)
bootstrap = Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def home():                             # 视图函数
    user_agent = request.headers.get('User-Agent')
    return render_template('home.html', user_agent=user_agent)


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


@app.route('/makecookie')
def make_cookies():         # 生产cookies
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response


@app.route('/redirect')
def do_redirect():          # 重定向
    return redirect('http://www.baidu.com')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run()
    # manager.run()