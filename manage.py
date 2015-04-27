#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask.ext.script import Manager, Server
from flask.ext.collect import Collect
from ngflaskcurd import create_app

app = create_app()
manager = Manager(app)
manager.add_option("-c", "--config",
                   dest="config", required=False,
                   default='ngflaskcurd.settings')

collect = Collect()
collect.init_script(manager)

@manager.shell
def make_shell_context():
    " Update shell. "
    return dict(app=app)

@manager.command
def check():
    """Prints app status"""
    from pprint import pprint
    print("Extensions.")
    pprint(app.extensions)
    print("Modules.")
    pprint(app.blueprints)
    print("App.")
    return app

@manager.command
def populate():
    """Populate the database with sample data"""
    from ngflaskcurd.utils.populate import Populate
    Populate()()

@manager.command
def show_config():
    "print all config variables"
    from pprint import pprint
    print("Config.")
    pprint(dict(app.config))

manager.add_command("run0", Server(
    use_debugger=True,
    use_reloader=True,
    host='0.0.0.0',
    port=8000
))


if __name__ == '__main__':
    manager.run()
