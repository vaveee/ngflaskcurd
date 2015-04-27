# coding: utf-8

from ...core import const
from ...core.database import dbs
from ...core.log import logger
from ngflaskcurd.core.const import SIT_AMOUNT_KEY_PRE
from datetime import datetime
from flask import Blueprint, render_template, redirect, request, session, \
    make_response, url_for, flash, current_app, jsonify, g, abort, Flask, session
from flask.views import MethodView
from flask_login import logout_user, login_user, current_user, login_required
from sqlalchemy.sql.expression import or_

#默认首页
class Index(MethodView):
    def get(self):
        return render_template('front/index.html')
    
