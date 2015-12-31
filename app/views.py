from flask import render_template, session
from app import app, items

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/add/<path:item>')
def addItem(item):
    return items.add(item)

@app.route('/remove/<path:item>')
def removeItem(item):
    items.remove(item)
    return ''

@app.route('/suggestions')
def suggestions():
    return items.getSuggestions()

@app.route('/removesuggestion/<path:item>')
def removeSuggestion(item):
    items.removeSuggestion(item)
    return ''

@app.route('/clear')
def clear():
    session.clear()
    return ''
