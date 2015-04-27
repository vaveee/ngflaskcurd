#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import absolute_import

import logging
from logging.handlers import RotatingFileHandler

from flask import current_app

FORMAT = logging.Formatter(
    '%(asctime)s:[%(levelname)s]%(name)s:%(filename)s#%(lineno)d: %(message)s'
)


def stream_handler(level):
    handler = logging.StreamHandler()
    handler.setLevel(level)
    handler.setFormatter(FORMAT)
    return handler


def file_handler(level, log_file):
    handler = RotatingFileHandler(log_file,
                                  maxBytes=1024 * 1024 * 200,
                                  backupCount=100)
    handler.setLevel(level)
    handler.setFormatter(FORMAT)
    return handler


class FlaskLogger(object):
    def __int__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.app = app
        log_level = app.config.pop('LOG_LEVEL', logging.INFO)
        log_file = app.config.pop('LOG_FILE', None)
        assert log_file, 'LOG_FILE has not benn configured'
        app.logger.addHandler(file_handler(level=log_level, log_file=log_file))
        app.logger.info('Flask Logger inited')

    @property
    def __logger(self):
        # 继承flask.current_app 的线程安全特性
        try:
            logger = current_app.logger
        except RuntimeError:
            logger = self.app.logger
            logger.info('Get logger for Flask instance')
        return logger

    def debug(self, msg, *args, **kwargs):
        return self.__logger.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        return self.__logger.info(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        return self.__logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        return self.__logger.error(msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        return self.__logger.critical(msg, *args, **kwargs)

logger = FlaskLogger()
