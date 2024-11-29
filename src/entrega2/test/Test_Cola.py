'''
Created on 13 nov 2024

@author: manue
'''

from entrega2.tipos.Cola import Cola

def test():
    print("TEST DE COLA:")
    lista = [23, 47, 1, 2, -3, 4, 5]
    print("################################################")
    print(f'Creación de una cola vacía a la que luego se le añaden con un solo método los números:{lista}')
    cola = Cola.of()
    cola.add_all(lista)
    print(f'Resultado de la cola: {cola}')
    
    print("################################################")
    cola.remove_all()
    print(f'Elementos elimnados utilizando remove_all:{lista}')
    print(f'Cola después de eliminar todos sus elementos: {cola}')
    
if __name__ == '__main__':
    test()