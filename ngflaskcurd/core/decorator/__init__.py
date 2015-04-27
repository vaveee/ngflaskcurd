# -*- coding: utf-8 -*-
from ...core import const
from ...core.const import ITEMS_PER_PAGE
from ...core.database import dbs
from flask import request, flash, url_for, redirect, render_template
from flask.ext.login import login_user, logout_user, current_user
from flask.views import MethodView
from flask_security.decorators import roles_accepted, login_required
import json
import logging

from functools import wraps

def authorized(*roles):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            rule = request.url_rule
            roles = current_user.roles
            operations = []
            for role in roles:
                operations += role.operations
                
            for operation in operations:
                contains = rule.rule.count(operation.url) > 0
                if contains:
                    return fn(*args, **kwargs)
                
            flash(u'您没有操作权限,请联系管理员！', 'waring')
            return redirect(request.referrer or '/')
        return decorated_view
    return wrapper

