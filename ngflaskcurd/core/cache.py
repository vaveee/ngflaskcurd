# -*- coding:utf-8 -*-

from __future__ import absolute_import
from ngflaskcurd.core.const import SIT_AMOUNT_KEY_PRE, SIT_VALUE_KEY_PRE
from ngflaskcurd.modules.site.models import Site
from flask.globals import current_app


def get_site_amount_from_cache(key):
    amount = current_app.cache_mgr.get(SIT_AMOUNT_KEY_PRE + key)
    if amount:
        return amount
    else:
        site = Site.query.filter_by(key = key).first()
        current_app.cache_mgr.set(SIT_AMOUNT_KEY_PRE + key, site.amount)
        return site.amount

def get_site_value_from_cache(key):
    value = current_app.cache_mgr.get(SIT_VALUE_KEY_PRE + key)
    if value:
        return value
    else:
        site = Site.query.filter_by(key = key).first()
        current_app.cache_mgr.set(SIT_VALUE_KEY_PRE + key, site.value)
        return site.value


