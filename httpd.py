#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
## @file
## @brief httpd server using Flask

import os,sys,datetime

from FORTH import *

import flask

app = flask.Flask(__name__)

class Config:
	try:
	    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY') or \
	                open('/etc/machine-id').readline()[:-1]
	    SQLALCHEMY_DATABASE_URI = os.environ.get('PIM_DATABASE_URL') or \
	                            'mysql://flask:%s@127.0.0.1/PIM' % SECRET_KEY
	except IOError:
		SECRET_KEY = 'Windoze'
		basedir = os.path.abspath(os.path.dirname(__file__))
		SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
	
	SQLALCHEMY_TRACK_MODIFICATIONS = False
                            
app.config.from_object(Config)

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.SmallInteger,primary_key = True)
    login = db.Column(db.String(32), index=True, unique=True, nullable=False)
    email = db.Column(db.String(128), index=True, unique=True, nullable=True)
    pwdhash = db.Column(db.String(128), nullable=False)
    commands = db.relationship('Command', backref='author', lazy='dynamic')
    
    def __init__(self,login,passwd,email=None):
        self.login = login
        self.email = email
        self.pwdhash = str(hash(passwd))
        
    def __repr__(self):
        return '%s / %s '%(self.login,self.email)

# print User('ponyatov','gjyznjd','dponyatov@gmail.com')

class Command(db.Model):
    id = db.Column(db.SmallInteger,primary_key = True)
    ts = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow)
    body = db.Column(db.String(0x100))
    user = db.Column(db.SmallInteger,db.ForeignKey('user.id'))

import flask_wtf,wtforms

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
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flask.flash('login: %s with %s'%(form.login.data,form.passwd.data))
        return flask.redirect(flask.url_for('index'))
    return flask.render_template('login.html',form=form)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8888)
