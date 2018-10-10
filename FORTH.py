from SYM import *

## @brief ForthVM stack
S = Stack('DATA')

## @brief ForthVM vocabulary
W = Map('FORTH')

## @brief client-side gramma for PEG.js
PEGJS = String('''// PEG.js ''')

## @brief client-side command field template
PAD = String('\ FORTH command')

