#!flask/bin/python
import os
from app import app
app.run(host='0.0.0.0', port=os.environ.get("PORT", 5000), debug=True)
