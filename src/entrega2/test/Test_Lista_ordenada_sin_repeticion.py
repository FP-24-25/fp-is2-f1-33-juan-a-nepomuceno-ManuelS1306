'''
Created on 13 nov 2024

@author: manue
'''

from entrega2.tipos.Lista_ordenada_sin_repeticion import Lista_ordenada_sin_repeticion

def test():
    print("TEST DE LISTA ORDENADA SIN REPETICIÓN:")

    print("################################################")
    print("Creación de una lista con criterio de orden lambda x: -x")
    lista = Lista_ordenada_sin_repeticion.of(lambda x: -x)
    lista.add(23)
    lista.add(47)
    lista.add(47)
    lista.add(1)
    lista.add(2)
    lista.add(-3)
    lista.add(4)
    lista.add(5)
    print('Se añaden en este orden: 23, 47, 47, 1, 2, -3, 4, 5')
    print(f'El resultado de la lista ordenada sin repetición es: {lista}')
    
    print("################################################")
    lista.remove()
    print('El elemento eliminado al utilizar remove(): 47')
    print(f'Resultado de la lista tras eliminar:{lista}')
    
    print("################################################")
    lista.add(47)
    lista.remove_all()
    print('Elementos eliminados utilizando remove_all: [23, 47, 1, 2, -3, 4, 5]')
    print(f'Resultado de la lista tras eliminar:{lista}')
    
    print("################################################")
    lista.add(23)
    lista.add(47)
    lista.add(47)
    lista.add(1)
    lista.add(2)
    lista.add(-3)
    lista.add(4)
    lista.add(5)
    print('Comprobando si se añaden los números en la posición correcta...')
    lista.add(0)
    print(f'Lista después de añadirle el 0:{lista}')
    lista.add(0)
    print(f'Lista después de añadirle el 0:{lista}')
    lista.add(7)
    print(f'Lista después de añadirle el 7:{lista}')
    
if __name__ == "__main__":
    test()