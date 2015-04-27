# -*- coding: utf-8 -*-
from ...core.database import dbs
from datetime import datetime

class Note(dbs.Model):
    __tablename__ = 'note'
    
    id = dbs.Column(dbs.Integer(), primary_key=True)
    
    uuid = dbs.Column(dbs.String(127))
    
    created = dbs.Column(dbs.DateTime)
    updated = dbs.Column(dbs.DateTime)

    title = dbs.Column(dbs.String(255))
    content = dbs.Column(dbs.TEXT)
    
    def __unicode__(self):
        return unicode(self.title) or u''
    
    def __init__(self,**kw):
        self.uuid = kw.get("id")
        self.created = kw.get("created") or datetime.now()
        self.updated = kw.get("updated") or datetime.now()
        self.title = kw.get("title")
        self.content = kw.get("content")
        
    @property
    def serialize(self):
        return {
           "id" : self.uuid,
           "title" : self.title,
           "content" : self.content,
           "date" : str(self.updated),
       }
