# coding: utf-8
from . import babel, blueprints, error_handlers, \
    before_request, views, fixtures
from ngflaskcurd.core.admin import configure_admin
from ngflaskcurd.core.database import dbs
from ngflaskcurd.core.log import logger
from flask import Flask, session
from flask.ext.mail import Mail
from flask.ext.security import Security, SQLAlchemyUserDatastore
from flask.ext.session import Session

def configure_extensions(app, admin):
    Session().init_app(app)
    babel.configure(app)
    Mail(app)
    error_handlers.configure(app)
    dbs.init_app(app)
    logger.init_app(app)
    fixtures.configure(app)
    
    if app.config.get('ADMIN_ENABLED'):
        configure_admin(app, admin)
    blueprints.load_from_folder(app)
    if app.config.get('DEBUG_TOOLBAR_ENABLED'):
        try:
            from flask_debugtoolbar import DebugToolbarExtension
            DebugToolbarExtension(app)
        except:
            pass
    before_request.configure(app)
    views.configure(app)
    return app
