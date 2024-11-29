'''
Created on 13 nov 2024

@author: manue
'''

from entrega2.tipos.Lista_ordenada import Lista_ordenada

def test():
    print("TEST DE LISTA ORDENADA:")

    print("################################################")
    print('Creación de una lista con criterio de orden lambda x: x')
    lista = Lista_ordenada.of(lambda x: x)
    lista.add(3)
    lista.add(1)
    lista.add(2)
    print(f"Resultado de la lista:{lista}")

    print("################################################")
    lista.remove()
    print('El elemento eliminado al utilizar remove(): 1')
    print(f'Resultado de la lista tras eliminar:{lista}')
    
    print("################################################")
    lista.add(1)
    lista.remove_all()
    print('Elementos eliminados utilizando remove_all: [1, 2, 3]')
    print(f'Resultado de la lista tras eliminar:{lista}')
    
    print("################################################")
    lista.add(3)
    lista.add(1)
    lista.add(2)
    print('Comprobando si se añaden los números en la posición correcta...')
    lista.add(0)
    print(f'Lista después de añadirle el 0:{lista}')
    lista.add(10)
    print(f'Lista después de añadirle el 10:{lista}')
    lista.add(7)
    print(f'Lista después de añadirle el 7:{lista}')
    
    
if __name__ == "__main__":
    test()