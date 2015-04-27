#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
INSTANCE_PATH = os.path.abspath(os.path.dirname(__file__))
DEBUG = %(debug)s
HOST = '0.0.0.0'
PORT = %(port)s

SECRET_KEY = 'ngflaskcurd9kh92ndsg34nsldglasgi2nsdgsdjgk'

DATABASE_HOST = '%(db_host)s'
DATABASE_PORT = %(db_port)s
DATABASE_USER = '%(db_user)s'
DATABASE_PWD = '%(db_pwd)s'
DATABASE_NAME = '%(db_db)s'

SQLALCHEMY_DATABASE_URI = 'mysql://' + DATABASE_USER + ':' + DATABASE_PWD + '@' + \
                          DATABASE_HOST + ':' + str(DATABASE_PORT) + '/' + DATABASE_NAME + '?charset=utf8'
SQLALCHEMY_ECHO = DEBUG

ADMIN_ENABLED=False

SESSION_TYPE = 'filesystem'
ADMIN_ENABLED = True

UPLOAD= os.path.join(INSTANCE_PATH, 'uploads')



