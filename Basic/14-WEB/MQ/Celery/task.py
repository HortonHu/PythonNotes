# -*- coding:utf-8 -*-


import time
from celery import Celery


app = Celery('tasks', backend='redis://localhost', broker='amqp://')


@app.task
def add(x, y):
    return x + y
