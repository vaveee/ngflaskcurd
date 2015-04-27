#coding: utf-8
import os

INSTANCE_PATH = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
MODE = 'development'

DATABASE_HOST = 'localhost'
DATABASE_PORT = '3306'
DATABASE_USER = 'ngflaskcurd'
DATABASE_PWD = 'ngflaskcurd'
DATABASE_NAME = 'ngflaskcurd'
SQLALCHEMY_ECHO = False
SQLALCHEMY_DATABASE_URI = 'mysql://'+DATABASE_USER+':'+DATABASE_PWD+'@'+DATABASE_HOST+':'+DATABASE_PORT+'/'+DATABASE_NAME+'?charset=utf8'

BABEL_DEFAULT_LOCALE = 'zh'
SECRET_KEY = "KeepThisS3cr3t"
SECURITY_MSG_UNAUTHORIZED = (u'您没有操作权限,请联系管理员！', 'warning')
SECURITY_MSG_LOGIN = (u'你还没有登陆！如果您是微信用户，请用微信访问。', 'warning')

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

MAP_STATIC_ROOT = ('/robots.txt', '/sitemap.xml', '/favicon.ico')

BLUEPRINTS_PATH = 'modules'
BLUEPRINTS_OBJECT_NAME = 'module'

COLLECT_STATIC_ROOT = STATIC_ROOT

"""
Debug toolbar only works if installed
pip install flask-debugtoolbar
"""
DEBUG_TB_INTERCEPT_REDIRECTS = False
DEBUG_TB_PROFILER_ENABLED = True
DEBUG_TB_TEMPLATE_EDITOR_ENABLED = True
DEBUG_TB_PANELS = (
    'flask_debugtoolbar.panels.versions.VersionDebugPanel',
    'flask_debugtoolbar.panels.timer.TimerDebugPanel',
    'flask_debugtoolbar.panels.headers.HeaderDebugPanel',
    'flask_debugtoolbar.panels.request_vars.RequestVarsDebugPanel',
    'flask_debugtoolbar.panels.template.TemplateDebugPanel',
    'flask.ext.mongoengine.panels.MongoDebugPanel',
    'flask_debugtoolbar.panels.logger.LoggingPanel',
    'flask_debugtoolbar.panels.profiler.ProfilerDebugPanel',
)

"""
By default DEBUG_TOOLBAR is disabled
do not change it here, do it in local_settings.py
DEBUG_TOOLBAR_ENABLED = True
"""
DEBUG_TOOLBAR_ENABLED = False

UPLOAD= os.path.join(INSTANCE_PATH, 'uploads')
LOG_FILE = os.path.join(INSTANCE_PATH, 'ngflaskcurd.log')

# WTForms
CSRF_ENABLED = True
CSRF_SESSION_KEY = "somethingimpossibletoguess"


"""
It configures the default logger for app instance
"""
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    datefmt='%d.%m %H:%M:%S')
logging.info("Core settings loaded.")

