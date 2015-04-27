# -*- coding: utf-8 -*-
from ...core.const import *
from ...core.database import dbs
from ...core.log import logger
from ...utils import gen_sn
from .models import Note
from flask import request
from flask.json import jsonify
from flask.views import MethodView
from datetime import datetime
from flask_security.decorators import login_required
import json


class Notes(MethodView):
    def get(self):
        notes = Note.query.all()
        logger.debug('notes:%s', notes)
        if not notes:
            notes = [{"id":1417207904666,"title":"Seven Wonders of the World","content":"I want to visit the seven wonders of the ancient world!\n\n* The Colossus of Rhodes\n* The Great Pyramid of Giza\n* The Hanging Gardens of Babylon\n* The Lighthouse of Alexandria\n* The Mausoleum at Halicarnassus\n* The Statue of Zeus at Olympia\n* The Temple of Artemis at Ephesus","date":"2014-11-23T21:10:51.974Z"},{"id":1417204504666,"title":"Grocery List","content":"### Food items\n\n* Milk\n* Eggs\n* Cookies\n* Salad\n* Flour\n\n### Home items\n\n* Paper towels\n* Aspirin\n* Dish soap","date":"2014-11-23T21:40:04.089Z"},{"id":1417107904666,"title":"Cookie Recipe","content":"Makes 90-100 cookies.\n\n#### Ingredients\n* 2 1/2 cups butter, softened\n* 2 cups sugar\n* 2 eggs\n* 1/4 cup milk\n* 2 teaspoons Vanilla Extract\n* 8 cups all-purpose flour\n* 4 teaspoons baking powder\n* 1 teaspoon salt\n\n#### Directions\n1. In a large bowl, cream the butter and sugar. \n2. Add eggs, milk and vanilla to the bowl and mix well. \n3. Combine the flour, baking powder and salt gradually into creamed mixture.\n2. Drop cookies onto greased baking sheet, with 2 inches between.\n3. Bake at 375°F for 10-12 minutes or until bottoms are lightly browned.","date":"2014-11-23T21:46:01.400Z"},{"id":1417007904666,"title":"Holiday List","content":"Some gift ideas for the family.\n\n* John: Mountain bike\n* Julie: Lego set\n* Lindsey: Tricycle \n* Mom: Earrings\n* Dad: Beer of the month","date":"2014-11-23T21:58:27.327Z"},{"id":1416907904666,"title":"Meeting Notes","content":"Production reports being 2 weeks behind schedule. James will make a plan to get back on track.\n\nEngineering tested 5 prototypes for the next version, and 2 are currently undergoing the second round of tests. Expect final results next week.\n\nSales has secured buyers for the latest production run, and is putting pressure on production to keep up with demand.","date":"2014-11-23T22:01:12.988Z"},{"title":"我勒个去","content":"### Food items\n\n* Milk\n* Eggs\n* Cookies\n* Salad\n* Flour\n\n### Home items\n\n* Paper towels\n* Aspirin\n* Dish soap","date":"2015-04-27T02:57:52.584Z","id":1430102940289}]
            for i in notes:
                note = Note(id = i.get('id'),title = i.get('title'),content = i.get('content'),)
                dbs.session.add(note)
                dbs.session.commit()
            return  json.dumps(notes)
        return json.dumps([i.serialize for i in notes])
        
    def post(self):
        params = json.loads(request.data)
        logger.debug('params:%s', params)
        note = Note(
                    id = params.get('id'),
                    title = params.get('title'),
                    content = params.get('content'),
                    created = datetime.now(),
                    updated = datetime.now(),
                    )
        dbs.session.add(note)
        dbs.session.commit()
        return json.dumps('ok')
    
    def put(self, uuid):
        params = json.loads(request.data)
        logger.debug('params:%s', params)
        note = Note.query.filter_by(uuid = uuid).first()
        note.title = params.get('title')
        note.content = params.get('content')
        note.updated = datetime.now()
        dbs.session.add(note)
        dbs.session.commit()
        return json.dumps('ok')
    
    def delete(self, uuid):
        note = Note.query.filter_by(uuid = uuid).first()
        dbs.session.delete(note)
        dbs.session.commit()
        return json.dumps('ok')
    
