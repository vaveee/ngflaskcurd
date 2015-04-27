# -*- coding: utf-8 -*-

import os
from string import Template
import pkg_resources
import abu.admin

class Admin(abu.admin.Interface):

    def version(self):
        return '0.1'

    def init(self, path):
        settings = {}
        t = raw_input('Debug Mode [n]:')
        settings['debug'] = 'True' if t.lower() == 'y' else 'False'
        t = raw_input('Port [5000]:')
        settings['port'] = t if t.strip() else '5000'
        t = raw_input('MySQL Host [localhost]:')
        settings['db_host'] = t if t.strip() else 'localhost'
        t = raw_input('MySQL Port [3306]:')
        settings['db_port'] = t if t.strip() else '3306'
        t = raw_input('MySQL User [ngflaskcurd]:')
        settings['db_user'] = t if t.strip() else 'ngflaskcurd'
        t = raw_input('MySQL Password:')
        settings['db_pwd'] = t
        t = raw_input('MySQL Database Name [ngflaskcurd]:')
        settings['db_db'] = t if t.strip() else 'ngflaskcurd'
        
        a2wsgi = {}
        a2wsgi['dir'] = os.path.abspath(path)

        with open(os.path.join(path, 'setting.py'), 'w') as fd:
            fd.write(pkg_resources.resource_string(
                'ngflaskcurd',
                'config_templates/settings.py') % settings)
            
        with open(os.path.join(path, 'run.py'), 'w') as fd:
            fd.write(Template(pkg_resources.resource_string(
                'ngflaskcurd',
                'wsgi.py')).substitute(a2wsgi))
            
        if not os.path.exists(os.path.join(path, 'log')):
            os.mkdir(os.path.join(path, 'log'))
