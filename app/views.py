from flask import render_template
from app import app
from app import items

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/add/<item>')
def addItem(item):
    items.add(item)
    return item

@app.route('/remove/<item>')
def removeItem(item):
    items.remove(item)
    return item
