'''
Created on 13 nov 2024

@author: manue
'''

from __future__ import annotations
from entrega2.tipos.Agregado_lineal import Agregado_lineal
from typing import TypeVar, Generic, Callable


E = TypeVar('E')
R = TypeVar('R',int, float, str)

class Lista_ordenada(Agregado_lineal[E], Generic[E, R]):
    def __init__(self, order:Callable[[E], R]):
        super().__init__()
        self.__order: Callable[[E], R] = order
        
    @staticmethod
    def of(order:Callable[[E], R]) ->Lista_ordenada[E, R]:
        return Lista_ordenada(order)
    
    def __index_order(self, e:E) ->int:
        if not self._elements:
            return 0
        
        if self.__order(e) < self.__order(self._elements[0]):
            return 0
        
        if self.__order(e) > self.__order(self._elements[-1]):
            return len(self._elements)
        
        for i in range(1, len(self._elements)):
            if self.__order(self._elements[i-1]) <= self.__order(e) < self.__order(self._elements[i]):
                return i
        
        return len(self._elements)
            
    def add(self, e:E) ->None:
        posicion:int = self.__index_order(e)
        self._elements.insert(posicion, e)
        
    def __str__(self) ->str:
        return f'ListaOrdenada({self._elements})'