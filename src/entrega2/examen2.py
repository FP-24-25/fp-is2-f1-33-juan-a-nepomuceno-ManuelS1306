'''
Created on 21 nov 2024

@author: manue
'''
from __future__ import annotations
from entrega2.tipos.Agregado_lineal import Agregado_lineal
from typing import TypeVar, Generic, List, Callable, Optional
from abc import ABC, abstractmethod

E = TypeVar('E')

class ColaConLimite(Agregado_lineal[E]): #Clase que hereda de Agregado_lineal y tiene una capacidad máxima.
    def __init__(self, capacidad:int):
        super().__init__()
        self._capacidad: int = capacidad
        
    @staticmethod
    def of(capacidad:int) -> ColaConLimite[E]:
        return ColaConLimite(capacidad)
    
    def add(self, e:E) ->None:
        if self.is_full():
            raise OverflowError('La cola está llena')
        else:
            self._elements.append(e)
            
    def is_full(self) ->bool:
        return self.size == self._capacidad
    

def TestColaConLimite1():
    print('Test 1 de la clase ColaConLimite:')
    cola: ColaConLimite = ColaConLimite.of(3)
    cola.add('Tarea 1')                         #Añado tres elementos a la cola.
    cola.add('Tarea 2')
    cola.add('Tarea 3')
    print('Añadimos los elemenntos: Tarea 1, Tarea 2 y Tarea 3')
    print('Intentamos añadir un cuarto elemento: Tarea 4')
    try:                                        #Pruebo si salta la exción de OverflowError.
        cola.add('Tarea 4')
    except OverflowError as e:
        print(e)
    print('Eliminamos el primer elemento:')
    print(cola.remove())                        #Elimino el primer elemento de la cola.
    
def TestColaConLimite2():
    print('Test 2 de la clase ColaConLimite:')  #Pruebo si el método is_full() funciona correctamente.
    print('Añado cuatro elementos a la cola')
    cola: ColaConLimite = ColaConLimite.of(5)
    cola.add_all(['Tarea 1', 'Tarea 2', 'Tarea 3', 'Tarea 4'])
    print('¿La cola está llena?')
    print(cola.is_full())
    print('Añadimos un elemento más:')
    cola.add('Tarea 5')
    print(cola.is_full())


# Copio el código de Agregado_lineal para poder hacer las modificaciones necesarias.
class Agregado_lineal2(Generic[E]):      #Cambio algunas cosas para poder realizar los test.
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
    
    
    def add(self, e:E) ->None:      #Implemento el método add que añade un elemento al agregado.
        self._elements.append(e)

    
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
    
    #Comienzan las modificaciones:
    
    def contains(self, e:E) ->bool:  # Método que determina si un elemento está en el agregado. 
        return e in self._elements #Si el elemento está en la lista, devuelve True, de lo contrario, devuelve False.
    
    def find(self, func:Callable[[E], bool]) -> Optional[E]:  # Método que busca un elemento en el agregado.
        for e in self._elements:   #Recorre los elementos del agregado y si encuentra uno que cumpla con la condición, lo devuelve. Solo devuelve el primer elemento que cumpla la condición.
            if func(e):
                return e  
        return None       #Si no existe ningún elemento que cumpla con la condición, devuelve None.
    
    def filter(self, func:Callable[[E], bool]) -> list[E]:  # Método que filtra los elementos del agregado.
        elementos_filtrados: list[E] = []     #Inicializa una lista vacía en la que añadirán los elementos filtrados.
        for e in self._elements:              #Recorre los elementos del agregado, los filtra y los añade a la lista.
            if func(e):
                elementos_filtrados.append(e)
        return elementos_filtrados            #Devuelve la lista con los elementos filtrados.

def TestAgregado_lineal2():
    print('Test de la clase Agregado_lineal2:')
    agregado: Agregado_lineal2 = Agregado_lineal2()
    agregado.add_all([1, 2, 3, 4, 5])
    print('Añadimos los elementos: 1, 2, 3, 4 y 5')
    print('¿El agregado contiene el elemento 3?')
    print(agregado.contains(3))
    print('¿El agregado contiene el elemento 6?')
    print(agregado.contains(6))
    print('Buscamos el primer elemento que sea mayor que 3:')
    print(agregado.find(lambda x: x > 3))
    print('Buscamos el primer elemento que sea mayor que 5:')
    print(agregado.find(lambda x: x > 5))
    print('Filtramos los elementos que sean mayores que 3:')
    print(agregado.filter(lambda x: x > 3))
    print('Filtramos los elementos que sean mayores que 5:')
    print(agregado.filter(lambda x: x > 5))


if __name__ == '__main__':
    TestColaConLimite1()
    TestColaConLimite2()
    TestAgregado_lineal2()
    
    
    