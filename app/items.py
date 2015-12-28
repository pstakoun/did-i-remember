def standardize(s):
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join([c if c in chars else '' for c in s.upper()])

from flask import session
from sqlalchemy import and_
from app.database import db_session
from app.models import Item, ItemConnection, ItemSpelling

def addSpelling(item, spelling):
    itemSpelling = ItemSpelling.query.filter(and_(ItemSpelling.item == item, ItemSpelling.spelling == spelling)).first()
    if itemSpelling == None:
        db_session.add(ItemSpelling(item, spelling))
        db_session.commit()
        itemSpelling = ItemSpelling.query.filter(and_(ItemSpelling.item == item, ItemSpelling.spelling == spelling)).first()
    itemSpelling.occurrences += 1
    db_session.commit()

def addConnections(item):
    for i in session['items']:
        s = standardize(i)
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
    s1 = standardize(s)
    if 'items' not in session:
        session['items'] = []
    if 'allItems' not in session:
        session['allItems'] = []
    if s1 not in [standardize(x) for x in session['items']] and s1:
        item = Item.query.filter(Item.name == s1).first()
        if item == None:
            db_session.add(Item(s1))
            db_session.commit()
            item = Item.query.filter(Item.name == s1).first()
        if s not in session['allItems']:
            item.occurrences += 1
            db_session.commit()
            addSpelling(s1, s)
            addConnections(s1)
            session['allItems'].append(s)
        session['items'].append(s)
        return s1
    return ''

def remove(s):
    if s in session['items']:
        session['items'].remove(s)

def getSpelling(s):
    spellings = ItemSpelling.query.filter(ItemSpelling.item == s).all()
    best = s
    bestOcc = 0
    for spell in spellings:
        if spell.occurrences > bestOcc:
            best = spell.spelling
            bestOcc = spell.occurrences
    return best

def updateSuggestions():
    items = {}
    if 'items' not in session:
        session['items'] = []
    if 'removedSuggestions' not in session:
        session['removedSuggestions'] = []
    for i in session['items']:
        s = standardize(i)
        conns = ItemConnection.query.filter(and_(ItemConnection.item1 == s, ~ItemConnection.item2.in_([standardize(x) for x in session['items']]))).all()
        for c in conns:
            if c.item2 in session['removedSuggestions']:
                continue
            if c.item2 not in items:
                items[c.item2] = c.occurrences
            else:
                items[c.item2] += c.occurrences
    session['suggestions'] = [getSpelling(s) for s in list(reversed(sorted(items, key=items.get)))[:min(len(items), 5)]]

def getSuggestions():
    updateSuggestions()
    return ','.join(session['suggestions'])

def removeSuggestion(s):
    if 'removedSuggestions' not in session:
        session['removedSuggestions'] = []
    if s not in session['removedSuggestions']:
        session['removedSuggestions'].append(standardize(s))
