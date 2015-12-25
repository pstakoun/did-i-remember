from flask import Flask

app = Flask(__name__)
from app import views

app.secret_key = '\x05\xa7FI\xfe\x1bL\x9b\r\xe6\x85\xc8\x8f\x1a|B\xa1\x91\xba\x85s\xd1\xbb\xac'

from app.database import init_db, db_session

init_db()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
