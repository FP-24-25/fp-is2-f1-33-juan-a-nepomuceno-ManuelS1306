'''
Created on 13 nov 2024

@author: manue
'''

from __future__ import annotations
from typing import TypeVar, Generic, List, Tuple

E = TypeVar('E')
P = TypeVar('P', int, float, str)

class Cola_de_prioridad(Generic[E, P]):
    def __init__(self):
        self._elements: List[E] = []
        self._priorities: List[P] = []
        
    @property
    def size(self) ->int:
        return len(self._elements)
    
    @property
    def is_empty(self) ->bool:
        return self.size == 0
    
    @property
    def elements(self) ->list[E]:
        return self._elements
    
    def add(self, e:E, priority:P) ->None:
        posicion = self.__index_order(priority)
        self._elements.insert(posicion, e)
        self._priorities.insert(posicion, priority)
    
    def add_all(self, ls:list[tuple[E, P]]) ->None:
        for elemento, prioridad in ls:
            self.add(elemento, prioridad)
    
    def remove(self) ->E:
        assert len(self._elements) > 0, 'El agregado está vacío'
        
        elemento = self._elements[0]
        del self._elements[0]
        return elemento
        
        
    def remove_all(self) -> list[E]:
        elementos_eliminados:list[E] = []
        
        while not self.is_empty:
            elementos_eliminados.append(self.remove())
            
        return elementos_eliminados
    
    def __index_order(self, priority: P) -> int:
        if not self._elements:
            return 0
        
        for i in range(len(self._priorities)):
            if priority < self._priorities[i]:
                return i
        
        return len(self._priorities)
    
    def decrease_priority(self, e:E, new_priority:P) -> None:
        if e in self._elements:
            posicion = self._elements.index(e)
            priority = self._priorities[posicion]
            
            if new_priority < priority:
                del self._elements[posicion]
                del self._priorities[posicion]
                self.add(e, new_priority)
    
    def __str__(self) ->str:
        cola_de_prioridad:List[Tuple[E, P]] = []
        for i in range(len(self._elements)):
            cola_de_prioridad.append((self._elements[i], self._priorities[i]))
            
        return f'ColaPrioridad[{cola_de_prioridad}]'