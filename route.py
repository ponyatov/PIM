from httpd import *
from FORTH import *

@app.route('/')
def index():
    return flask.render_template('index.html',S=S,W=W,PEGJS=PEGJS,PAD=PAD)
