#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import absolute_import

import json
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import types
from ..utils import sha1sum
import logging
logger = logging.getLogger()


def get_or_create(model, defaults=None, **kwargs):
    """
    获取或者创建对象，模仿django的。
    """
    instance = model.query.filter_by(**kwargs).first()
    if instance:
        setattr(instance, 'is_new', False)
    else:
        kwargs.update(defaults)
        logger.debug(kwargs)
        instance = model(**kwargs)
        dbs.session.add(instance)
        dbs.session.commit()
        setattr(instance, 'is_new', True)
    return instance


class JSONEncodedDict(types.TypeDecorator):
    """
    Represents an immutable structure as a json-encoded string.

    Usage::

        dbs.JSONEncodedDict(255)

    """

    impl = types.VARCHAR

    def process_bind_param(self, value, dialect):
        if value is not None:
            value = json.dumps(value)
        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            value = json.loads(value)
        return value


class ChoiceType(types.TypeDecorator):
    """
    example::
    choices=(
        ('key1', 'value1'),
        ('key2', 'value2')
    )

    filed::
        db.Column(db.ChoiceType(length=xx, choices=choices))

    """
    impl = types.String

    def __init__(self, choices, **kw):
        self.choices = dict(choices)
        super(ChoiceType, self).__init__(**kw)

    def process_bind_param(self, value, dialect):
        return [k for k, v in self.choices.iteritems() if k == value][0]

    def process_result_value(self, value, dialect):
        return self.choices[value]

class Password(types.TypeDecorator):
    """
    这是password字段类型。就不需要到处都是加密操作了
    """
    impl = types.String

    def process_bind_param(self, value, dialect):
        return sha1sum(value) if value else None


class DataBase(SQLAlchemy):
    ChoiceType = ChoiceType
    JSONEncodedDict = JSONEncodedDict
    Password = Password

    def init_app(self, app):
        """需要用到。要不sqlalchemy部分功能无法正常使用"""
        self.app = app
        super(DataBase, self).init_app(app)


dbs = DataBase()


class Model(dbs.Model):
    __abstract__ = True
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8',
    }


dbs.Model = Model


from functools import wraps


def close_session(action):
    """ 关闭当前的session，并把操作数据库的代码放在try...catch...finally中 """
    def _close_session(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                rs = func(*args, **kwargs)
                return rs
            except Exception, ex:
                dbs.session.close()
                logger.error(ex.message)
            finally:
                if action in ('update', 'delete', 'insert'):
                    dbs.session.commit()
                dbs.session.close()
        return wrapper
    return _close_session
