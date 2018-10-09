#!/usr/bin/env python2.7

import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')

app.run(debug=True,host='0.0.0.0',port=8888)
