#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sqlite3
from flask import Flask, request, sessions, g, redirect, url_for, \
    abort, render_template,flash
from contextlib import closing

DATABASE = r'C:\Users\dell\Documents\GitHub\PythonStudy\py27\N5_Web\Flask\hor\tmp\hor.db'
DEBUG = True
SECRET_KEY = 'development ley'
USERNAME = 'admin'
PASSWORD = 'default'

# 创造应用
app = Flask(__name__)
# app.config.from_envvar('HOR_SETTING', silent=True)
app.config.from_object(__name__)


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request():
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()
    g.db.close()


if __name__ == '__main__':
    # init_db()
    app.run()
