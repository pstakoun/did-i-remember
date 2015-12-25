def stripSpecial(s):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return "".join([c if c in chars else "" for c in s])

from flask import session
from app.database import db_session
from app.models import Item, ItemConnection

def addConnections(item, items):
    for i in session['items']:
        pass

def add(s):
    s1 = stripSpecial(s.upper())
    if 'items' not in session:
        session['items'] = []
    if 'allItems' not in session:
        session['allItems'] = []
    if s not in session['items']:
        item = Item.query.filter(Item.name == s1).first()
        if item == None:
            db_session.add(Item(s1))
        elif s not in session['allItems']:
            item.occurrences += 1
            addConnections(s1)
            session['allItems'].append(s)
        session['items'].append(s)
        db_session.commit()

def remove(s):
    if s in session['items']:
        session['items'].remove(s)
