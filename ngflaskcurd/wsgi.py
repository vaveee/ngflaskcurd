# -*- coding: utf-8 -*-

from ngflaskcurd import create_app
from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware
import os


here = os.path.dirname(os.path.realpath(__file__))
config_file = os.path.join(here, 'setting.py')

application = DispatcherMiddleware(create_app(config=config_file), {})

if __name__ == "__main__":
    run_simple(
        '0.0.0.0',
        5000,
        application,
        use_reloader=True,
        use_debugger=True
    )
