'''
Created on 13 nov 2024

@author: manue
'''

from __future__ import annotations
from entrega2.tipos.Agregado_lineal import Agregado_lineal
from typing import TypeVar


E = TypeVar('E')

class Pila(Agregado_lineal[E]):
    
    @staticmethod 
    def of() ->Pila[E]:
        return Pila()
    
    def add(self, e:E) ->None:
        self._elements.insert(0, e)