#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
## @file
## @brief httpd server using Flask

import os,sys

from SYM import *
from attr import validators

## @brief client-side gramma for PEG.js
PEGJS = String('''// PEG.js ''')

## @brief client-side command field template
PAD = String('\ FORTH command')

## @brief ForthVM stack
S = Stack('DATA')

## @brief ForthVM vocabulary
W = Map('FORTH')

import flask
import flask_wtf,wtforms

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY') \
                            or 'you-will-never-guess'

@app.route('/')
def index():
    return flask.render_template('index.html',S=S,W=W,PEGJS=PEGJS,PAD=PAD)

@app.route('/docs/<path:path>')
def docs(path):
    return flask.send_from_directory('docs',path)

class LoginForm(flask_wtf.FlaskForm):
    login  = wtforms.StringField('user',\
                validators = [wtforms.validators.DataRequired()])
    passwd = wtforms.PasswordField('password',\
                validators = [wtforms.validators.DataRequired()])
    cookie = wtforms.BooleanField('remember me')
    submit = wtforms.SubmitField('login')
    
@app.route('/login')
def login():
    return flask.render_template('login.html',form=LoginForm())

app.run(debug=True,host='0.0.0.0',port=8888)
