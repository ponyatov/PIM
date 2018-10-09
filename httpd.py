#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

## @file
## @brief httpd server using Flask

## @brief core generic object
class Qbject:
    def __init__(self,V):
        self.type  = self.__class__.__name__.lower()
        self.value = V
    def __repr__(self):
        return self.dump()
    def dump(self,depth=0):
        return self.head()
    def head(self,prefix=''):
        return '%s<%s:%s>'%(prefix,self.type,self.value)

## @brief primitive
class Primitive(Qbject): pass

## @brief symbol names sw and model entities 
class Symbol(Primitive): pass

## @brief number
class Number(Primitive): pass

## @brief string
class String(Primitive): pass

## @brief data container
class Container(Qbject): pass

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

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html',S=S,W=W,PEGJS=PEGJS,PAD=PAD)

app.run(debug=True,host='0.0.0.0',port=8888)
