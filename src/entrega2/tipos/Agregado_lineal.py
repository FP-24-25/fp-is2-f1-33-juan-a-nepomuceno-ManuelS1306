'''
Created on 13 nov 2024

@author: manue
'''

from __future__ import annotations
from typing import TypeVar, Generic, List
from abc import ABC, abstractmethod

E = TypeVar('E')


class Agregado_lineal(ABC, Generic[E]):
    def __init__(self):
        self._elements: List[E] = []
        
    @property
    def size(self) ->int:
        return len(self._elements)
    
    @property
    def is_empty(self) ->bool:
        return self.size == 0
    
    @property
    def elements(self) ->list[E]:
        return self._elements
    
    @abstractmethod
    def add(self, e:E) ->None:
        pass
    
    def add_all(self, ls:list[E]) ->None:
        for j in ls:
            self.add(j)
            
    def remove(self) -> E:
        assert len(self._elements) > 0, 'El agregado está vacío'
        elemento_eliminado = self._elements[0]
        self._elements.remove(elemento_eliminado)
        return elemento_eliminado

    def remove_all(self) -> list[E]:
        elementos_eliminados: list[E] = []

        while not self.is_empty:
            elementos_eliminados.append(self.remove())

        return elementos_eliminados