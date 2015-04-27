# -*- coding: utf-8 -*-
from ngflaskcurd import admin
from .models import Project
from ngflaskcurd.core.database import dbs
from flask.ext.admin.contrib import sqla

admin.add_view(sqla.ModelView(Project, dbs.session, name=u"网址"))

