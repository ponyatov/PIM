#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
## @file
## @brief httpd server using Flask

import os,sys

from SYM import *

## @brief client-side gramma for PEG.js
PEGJS = String('''// PEG.js ''')

## @brief client-side command field template
PAD = String('\ FORTH command')

## @brief ForthVM stack
S = Stack('DATA')

## @brief ForthVM vocabulary
W = Map('FORTH')

import flask
import flask_wtf

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY') or 'you-will-never-guess'

@app.route('/')
def index():
    return flask.render_template('index.html',S=S,W=W,PEGJS=PEGJS,PAD=PAD)

app.run(debug=True,host='0.0.0.0',port=8888)
