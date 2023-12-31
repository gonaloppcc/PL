
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'u z\n    capicua : z capicua z\n            | u capicua u\n            | z\n            | u\n            |\n    '
    
_lr_action_items = {'z':([0,2,3,4,6,7,],[2,2,2,6,-1,-2,]),'u':([0,2,3,5,6,7,],[3,3,3,7,-1,-2,]),'$end':([0,1,2,3,6,7,],[-5,0,-3,-4,-1,-2,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'capicua':([0,2,3,],[1,4,5,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> capicua","S'",1,None,None,None),
  ('capicua -> z capicua z','capicua',3,'p_gramatica','dir_sin.py',8),
  ('capicua -> u capicua u','capicua',3,'p_gramatica','dir_sin.py',9),
  ('capicua -> z','capicua',1,'p_gramatica','dir_sin.py',10),
  ('capicua -> u','capicua',1,'p_gramatica','dir_sin.py',11),
  ('capicua -> <empty>','capicua',0,'p_gramatica','dir_sin.py',12),
]
