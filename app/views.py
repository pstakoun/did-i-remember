from flask import render_template
from app import app
from app import items

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/add/<path:item>')
def addItem(item):
    return item if items.add(item) else ""

@app.route('/remove/<path:item>')
def removeItem(item):
    items.remove(item)
    return item
