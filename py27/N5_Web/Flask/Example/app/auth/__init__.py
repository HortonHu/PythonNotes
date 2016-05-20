#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 认证系统
from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views
