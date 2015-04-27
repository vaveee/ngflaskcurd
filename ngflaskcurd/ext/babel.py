from flask.ext.babelex import Babel
babel = Babel()

def configure(app):
    babel.init_app(app)