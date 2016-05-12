#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask, url_for, request
app = Flask(__name__)

@app.route('/')
def index():
    return 'This is the index of the site.'


@app.route('/hello')
def hello_world():
    return 'Hello World!'


@app.route('/user/<username>')
def show_name(username):
    return 'Your name is ' + str(username)


@app.route('/user/<int:post_id>')
def show_id(post_id):
    return 'Your ID is ' + post_id


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.methods == 'GET':
#         do_the_login()
#     else:


with app.test_request_context():
    print url_for('index')
    print url_for('login')
    print url_for('login', next='/')
    print url_for('show_name', username='Jia Jia')




if __name__ == '__main__':
    app.run()
