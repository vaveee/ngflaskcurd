#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .core.app import ngflaskcurdFlask # Flask with custom template loader
from ngflaskcurd.utils.filters import EnvFilters
from flask import Flask, session
import logging
import os

logger = logging.getLogger()

try:
    from .core.admin import create_admin
    admin = create_admin()
except:
    pass

def create_app(config=None, test=False, admin_instance=None, **settings):
    app = ngflaskcurdFlask('ngflaskcurd')
    app.config.from_envvar("APP_SETTINGS", silent=True)
    
    app.config.from_object('ngflaskcurd.settings')
    
    if config:
        app.config.from_pyfile(config)

    # Settings from mode
    mode = os.environ.get('MODE')
    if mode:
        app.config.from_object('ngflaskcurd.%s_settings' % mode)

    # Local settings
    if not test:
        app.config.from_pyfile(
            os.path.join(os.path.dirname(__file__), 'local_settings.py'),
            silent=True
        )

    # Overide settings
    app.config.update(settings)
    from .ext import configure_extensions
    configure_extensions(app, admin)
    EnvFilters(app)
    app.jinja_env.variable_start_string = '{{ '
    app.jinja_env.variable_end_string = ' }}' 
    return app


