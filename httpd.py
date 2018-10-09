#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import os,sys

## @file
## @brief httpd server using Flask

## @brief core generic object
class Object:
    ## constructor
    def __init__(self,V):
        ## class/type tag (compatible with @ref PLY)
        self.type  = self.__class__.__name__.lower()
        ## single value (compatible with @ref PLY)
        self.value = V
    ## @brief print any object
    def __repr__(self):
        return self.dump()
    ## @brief dump in full tree form
    def dump(self,depth=0):
        return self.head()
    ## @brief dump in short `<type:value` form
    def head(self,prefix=''):
        return '%s<%s:%s>'%(prefix,self.type,self.value)

## @brief primitive
class Primitive(Object): pass

## @brief symbol names sw and model entities 
class Symbol(Primitive): pass

## @brief number
class Number(Primitive): pass

## @brief string
class String(Primitive): pass

## @brief data container
class Container(Object): pass

## @brief LIFO stack
class Stack(Container): pass

## @brief associative (key/value) array 
class Map(Container): pass

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
