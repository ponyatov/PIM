# -*- coding: utf-8 -*-
## @file
## @brief Symbolic class system

## @defgroup sym Symbolic class system
## @{

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
    
## @defgroup prim Primitive
## @ingroup sym
## @{

## @brief primitive
class Primitive(Object): pass

## @brief symbol names sw and model entities 
class Symbol(Primitive): pass

## @brief number
class Number(Primitive): pass

## @brief integer number
class Integer(Number): pass

## @brief machine hex number
class Hex(Integer): pass

## @brief bit string
class Bin(Integer): pass

## @brief string
class String(Primitive): pass

## @}

## @defgroup cont Container
## @ingroup sym
## @{

## @brief data container
class Container(Object): pass

## @brief LIFO stack
class Stack(Container): pass

## @brief associative (key/value) array 
class Map(Container): pass

## @}

## @}
