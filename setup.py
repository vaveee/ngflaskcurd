from setuptools import setup, find_packages
import sys, os

version = '0.3.1'

setup(name='ngflaskcurd',
      version=version,
      description="",
      long_description="""""",
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'flask',
        'flask-script',
        'Flask-Babel',
        'Flask-Bcrypt',
        'flask-htmlbuilder',
        'Flask-Login',
        'Flask-Principal',
        'flask-security',
        'Flask-Mail',
        'flask-collect',
        'Flask-SQLAlchemy',
        'Flask-Testing',
        'flask-admin',
        'flask-babelex',
        'flask-session',
        'abu.admin',
        'Mysql-python>=1.2.3',
        'selenium',
        'Babel==1.3',
        'HTMLParser',
        'requests',
        'six',
        'lxml',
        'tornado',
        'redis',
        'wsgiref==0.1.2',
#        'wechat-sdk',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [abu.admin]
      ngflaskcurd = ngflaskcurd.admin:Admin
      """,
      )
