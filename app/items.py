def stripSpecial(s):
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join([c if c in chars else '' for c in s])

from flask import session
from sqlalchemy import and_
from app.database import db_session
from app.models import Item, ItemConnection

def addConnections(item):
    for i in session['items']:
        s = stripSpecial(i.upper())
        conn1 = ItemConnection.query.filter(and_(ItemConnection.item1 == item, ItemConnection.item2 == s)).first()
        conn2 = ItemConnection.query.filter(and_(ItemConnection.item1 == s, ItemConnection.item2 == item)).first()
        if conn1 == None:
            db_session.add(ItemConnection(item, s))
            db_session.commit()
            conn1 = ItemConnection.query.filter(and_(ItemConnection.item1 == item, ItemConnection.item2 == s)).first()
        conn1.occurrences += 1
        if conn2 == None:
            db_session.add(ItemConnection(s, item))
            db_session.commit()
            conn2 = ItemConnection.query.filter(and_(ItemConnection.item1 == s, ItemConnection.item2 == item)).first()
        conn2.occurrences += 1
        db_session.commit()

def add(s):
    s1 = stripSpecial(s.upper())
    if 'items' not in session:
        session['items'] = []
    if 'allItems' not in session:
        session['allItems'] = []
    if s not in session['items'] and s1:
        item = Item.query.filter(Item.name == s1).first()
        if item == None:
            db_session.add(Item(s1))
            db_session.commit()
            item = Item.query.filter(Item.name == s1).first()
        if s not in session['allItems']:
            item.occurrences += 1
            db_session.commit()
            addConnections(s1)
            session['allItems'].append(s)
        session['items'].append(s)
        return s1
    return ''

def remove(s):
    if s in session['items']:
        session['items'].remove(s)

def updateSuggestions():
    items = {}
    if 'items' not in session:
        session['items'] = []
    for i in session['items']:
        s = stripSpecial(i.upper())
        conn = ItemConnection.query.filter(and_(ItemConnection.item1 == s, ~ItemConnection.item2.in_([stripSpecial(x.upper()) for x in session['items']]))).all()
        for c in conn:
            if c.item2 not in items:
                items[c.item2] = c.occurrences
            else:
                items[c.item2] += c.occurrences
    session['suggestions'] = sorted(items)[:min(len(items), 5)]

def getSuggestions():
    updateSuggestions()
    return ','.join(session['suggestions'])

def removeSuggestion(s):
    pass
