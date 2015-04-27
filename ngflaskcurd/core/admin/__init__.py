#!/usr/bin/env python
# -*- coding: utf-8 -*

import logging
from werkzeug.utils import import_string
from flask import request, session
from flask.ext.admin import Admin

from .views import IndexView

logger = logging.getLogger()


class ngflaskcurdAdmin(Admin):
    def register(self, model, view=None, *args, **kwargs):
        View = view
        self.add_view(View(model, *args, **kwargs))

def create_admin(app=None):
    index_view = IndexView()
    return ngflaskcurdAdmin(app, index_view=index_view)

def configure_admin(app, admin):
    if admin.app is None:
        admin.init_app(app)
    return admin
