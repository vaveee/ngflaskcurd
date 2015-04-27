#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import absolute_import

import re
import datetime
from jinja2 import evalcontextfilter, Markup, escape
from HTMLParser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

class EnvFilters(object):
    def __init__(self, app):
        if not app:
            return
        self.app = app
        self.addEnvFilters()
        
    def addEnvFilters(self):
        self.app.jinja_env.filters['num_to_letter'] = num_to_letter
        self.app.jinja_env.filters['sanitize_html'] = sanitize_html


def num_to_letter(value):
    return chr(value-1 + ord('A'))

def sanitize_html(html):
    s = MLStripper()
    s.feed(html)
    if len(s.get_data())>110:
        return s.get_data()[:100]+"..."
    return s.get_data()     
