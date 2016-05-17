#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask, request, render_template, make_response, redirect, abort
from flask.ext.script import Manager

app = Flask(__name__)                   # 初始化
manager = Manager(app)


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
    if username != 'hortonhu':
        abort(404)
    return '<h1>Your name is %s</h1>' % str(username)


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


if __name__ == '__main__':
    # app.run()
    manager.run()