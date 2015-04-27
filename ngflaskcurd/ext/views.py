# coding: utf-8
from flask import send_from_directory, current_app, request
from ngflaskcurd.modules.front.views import Index
from ngflaskcurd.modules.project.views import Notes


def configure(app):

    app.add_url_rule('/', view_func=Index.as_view('index'))
    app.add_url_rule('/notes', view_func=Notes.as_view('notes'))
    app.add_url_rule('/notes/<string:uuid>', view_func=Notes.as_view('notes_uuid'))
    

def media(filename):
    return send_from_directory(current_app.config.get('MEDIA_ROOT'), filename)

def static_from_root():
    return send_from_directory(current_app.static_folder, request.path[1:])



