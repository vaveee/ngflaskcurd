# coding: utf-8

from ngflaskcurd.core.database import dbs
from ngflaskcurd.modules.accounts.models import User, Role
from ngflaskcurd.utils import gen_sn
from werkzeug import check_password_hash, generate_password_hash

class Populate(object):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.roles = {}
        self.users = {}

    def __call__(self, *args, **kwargs):
        pass
    
                
