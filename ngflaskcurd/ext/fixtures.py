# coding: utf-8

from ngflaskcurd.core.database import dbs

def configure(app):
    with app.test_request_context('/'):
        dbs.create_all()
