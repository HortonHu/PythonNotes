#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask, request, render_template, make_response, redirect, abort, \
    url_for, session, flash
from flask.ext.script import Manager, Shell
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.mail import Mail

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

from datetime import datetime
import os


# 初始化
app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)
mail = Mail(app)

basedir = os.path.abspath(os.path.dirname(__file__))

# app.config 字典可用来存储框架、扩展和程序本身的配置变量。
# SECRET_KEY 配置变量是通用密钥，可在 Flask 和多个第三方扩展中使用。
# 密钥不应该直接写入代码，而要保存在环境变量中
app.config['SECRET_KEY'] = 'SSSKey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS '] = True
app.config['MAIL_SERVER'] = 'smtp.sina.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USL_TLS'] = True
# app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
# app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_USERNAME'] = 'hortonhutest@sina.com'
app.config['MAIL_PASSWORD'] = raw_input('MAIL_PASSWORD')
app.config['FLASK_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
app.config['FLASK_MAIL_SENDER'] = 'Flask admin <flasky@example.com>'


@app.route('/', methods=['GET', 'POST'])
def home():
    user_agent = request.headers.get('User-Agent')
    return render_template('home.html', user_agent=user_agent, current_time=datetime.utcnow())


@app.route('/formtest', methods=['GET', 'POST'])
def form_test():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['know'] = False
        else:
            session['know'] = True
        session['name'] = form.name.data
        form.name.data = ''

        # old_name = session.get('name')
        # if old_name is not None and old_name != form.name.data:
        #     flash('Looks like you have changed your name!')
        # session['name'] = form.name.data
        return redirect(url_for('form_test'))
    return render_template('form_test.html', form=form, name=session.get('name'), know=session.get('know', False))


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


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)

# Shell配置
manager.add_command("shell", Shell(make_context=make_shell_context))

# 数据库迁移配置
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


# 发送邮件
def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)


if __name__ == '__main__':
    # app.run()
    manager.run()
