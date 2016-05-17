#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask, request, render_template

app = Flask(__name__)                   # 初始化


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
    return '<h1>Your name is %s</h1>' % str(username)


@app.route('/<int:user_num>')
def show_user_num(user_num):
    return '<h1>Your Number is %s</h1>' % user_num


if __name__ == '__main__':
    app.run()
